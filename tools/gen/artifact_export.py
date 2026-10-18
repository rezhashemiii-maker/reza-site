# -*- coding: utf-8 -*-
"""تبدیلِ یک تختهٔ src/ به نسخهٔ آرتیفکتِ طراحی.

روی آرتیفکت، تخته‌ها کنارِ هم‌اند و صفحهٔ «شروع» همان Main.dc.html است،
نه index.html. پس دو تفاوت همیشه لازم است:

  ۱ پیوندِ بازگشت: در مخزن به Main.dc.html#writing می‌رود، روی آرتیفکت
    به تختهٔ Writing.dc.html.
  ۲ نوارِ تب‌های آرتیفکت (شروع / نوشته‌ها / کتاب‌ها / رصدخانه) که در
    مخزن کارِ build.mjs است و این‌جا باید داخلِ خودِ تخته باشد.

این فایل همان دو کار را می‌کند و idempotent است: اگر تخته از قبل نوار
داشته باشد، دوباره اضافه نمی‌کند.

    python3 tools/gen/artifact_export.py Sets.dc.html Music.dc.html
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from paths import SRC, ROOT  # noqa: E402

# خروجی عمداً نسخه‌برداری‌شدنی است و در مخزن نگه داشته نمی‌شود؛
# منبعش src/ است و هر وقت لازم شد دوباره ساخته می‌شود.
OUT = os.path.join(ROOT, 'tools', 'gen', 'artifact', 'out')

CSS = (
    '.stabs{background:#FFFFFF;border-bottom:1px solid #E4E1D6}'
    '.stabs-in{max-width:1120px;margin:0 auto;padding:7px 16px;display:flex;'
    'align-items:center;gap:5px;flex-wrap:wrap}'
    '.stabs-brand{display:inline-flex;align-items:center;gap:8px;font-weight:800;'
    'font-size:14px;color:#16181C;margin-inline-end:8px;text-decoration:none}'
    '.stabs-brand span{width:9px;height:9px;border-radius:50%;background:#2F5233;'
    'flex-shrink:0}'
    '.stab{font-size:13px;color:#4A4F58;padding:6px 11px;border-radius:999px;'
    'text-decoration:none;white-space:nowrap}'
    '.stab:hover{background:#F0EEE7;color:#16181C;text-decoration:none}'
    '.stab[aria-current]{background:#2F5233;color:#FFFFFF;font-weight:700}'
    '@media (min-width:861px){.stabs{position:sticky;top:0;z-index:60}'
    'body header{top:43px !important}[id]{scroll-margin-top:122px !important}}'
    '@media (max-width:860px){.stabs-in{padding:6px 12px;gap:3px}'
    '.stabs-brand{font-size:13px;margin-inline-end:5px}'
    '.stab{font-size:12.5px;padding:5px 9px}}'
)

BAR = ('<nav class="stabs" aria-label="منوی اصلی"><div class="stabs-in">'
       '<a class="stabs-brand" href="Main.dc.html"><span></span>رضا هاشمی</a>'
       '<a class="stab" href="Main.dc.html">شروع</a>'
       '<a class="stab" href="Writing.dc.html">نوشته‌ها</a>'
       '<a class="stab" href="Books.dc.html">کتاب‌ها</a>'
       '<a class="stab" href="Watch.dc.html">رصدخانه</a></div></nav>')


def convert(name):
    s = io.open(os.path.join(SRC, name), encoding='utf-8').read()
    s = s.replace('href="Main.dc.html#writing"', 'href="Writing.dc.html"')
    if 'class="stabs"' not in s:
        s = s.replace('</style>\n</helmet>', CSS + '\n</style>\n</helmet>', 1)
        i = s.index('direction: rtl;">') + len('direction: rtl;">')
        s = s[:i] + '\n\n' + BAR + '\n' + s[i:]
    assert 'Main.dc.html#writing' not in s, 'پیوندِ بازگشت جا مانده'
    assert s.count('class="stabs"') == 1, 'نوارِ تب تکراری شد'
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    io.open(os.path.join(OUT, name), 'w', encoding='utf-8').write(s)
    return len(s)


if __name__ == '__main__':
    names = sys.argv[1:] or ['Sets.dc.html', 'Music.dc.html']
    for n in names:
        print(n, convert(n), 'نویسه → tools/gen/artifact/out/')
