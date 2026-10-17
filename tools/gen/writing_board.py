# -*- coding: utf-8 -*-
"""تختهٔ آرتیفکتیِ «نوشته‌ها» را از بخشِ نوشته‌های صفحهٔ اصلی پر می‌کند.

صفحهٔ اصلی مرجع است؛ این‌جا همان بلوک می‌نشیند با پیوندهای آرتیفکتی.

پیش‌تر این کار با یک اسکریپتِ دستی انجام می‌شد که فقط «اولین شبکهٔ کارت»
را جایگزین می‌کرد، در حالی که بلوکِ تازه دو گروه داشت. هر اجرا، گروه دومِ
اجرای قبلی را جا می‌گذاشت و یک نسخهٔ تازه هم می‌افزود — تا جایی که گروهِ
«بیرون از فناوری» پنج بار پشتِ سر هم روی سایت نشست.

حالا ناحیه با دو نشانهٔ ثابت مشخص می‌شود و هر بار کاملاً برداشته و دوباره
نوشته می‌شود. چون این گام داخلِ run.py است، بررسیِ همگامیِ CI هم هر
واگراییِ تازه را می‌گیرد.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from paths import SRC  # noqa: E402

WR = os.path.join(HERE, 'artifact', 'Writing.dc.html')
OPEN_MARK = '<!-- نوشته‌ها از src/Main.dc.html — tools/gen/writing_board.py -->'
CLOSE_MARK = '<!-- پایان نوشته‌ها -->'

GROUP_HEAD = ('        <div style="display: flex; align-items: baseline; gap: 12px; '
              'flex-wrap: wrap; margin: 0 0 6px;">')
SECTION_END = '      </div>\n    </section>'


def writings_block():
    """ناحیهٔ نوشته‌های صفحهٔ اصلی: از سرخطِ گروه اول تا پایانِ بخش."""
    main = io.open(os.path.join(SRC, 'Main.dc.html'), encoding='utf-8').read()
    start = main.index('<section id="writing"')
    a = main.index(GROUP_HEAD, start)
    b = main.index(SECTION_END, a)
    block = main[a:b].rstrip() + '\n'
    # در آرتیفکت، پروندهٔ عراق تختهٔ خودش را دارد
    block = block.replace('href="iraq.html"', 'href="Iraq.dc.html"')
    return block


def inject(block):
    s = io.open(WR, encoding='utf-8').read()
    if OPEN_MARK in s:
        a = s.index(OPEN_MARK)
        b = s.index(CLOSE_MARK) + len(CLOSE_MARK)
        # خطِ تازه‌ی بعد از نشانه هم باید برود، وگرنه هر اجرا یک خطِ خالی
        # اضافه می‌کند و فایل آرام‌آرام رشد می‌کند.
        if s[b:b + 1] == '\n':
            b += 1
        s = s[:a] + s[b:]
    else:
        # نخستین اجرا: ناحیهٔ قدیمی را از سرخطِ گروه اول تا پایانِ بخش برمی‌داریم
        a = s.index(GROUP_HEAD)
        b = s.index(SECTION_END, a)
        s = s[:a] + s[b:]
        a = len(s[:a])
    body = OPEN_MARK + '\n' + block + CLOSE_MARK + '\n'
    s = s[:a] + body + s[a:]
    io.open(WR, 'w', encoding='utf-8').write(s)
    return s


if __name__ == '__main__':
    block = writings_block()
    s = inject(block)
    groups = s.count(GROUP_HEAD)
    cards = s.count('flex-direction: column; background: #FFFFFF')
    print('تختهٔ نوشته‌ها همگام شد · %d گروه · %d کارت' % (groups, cards))
    assert groups == 2, 'باید دقیقاً دو گروه باشد، %d تا هست' % groups
