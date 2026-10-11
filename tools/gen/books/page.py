# -*- coding: utf-8 -*-
import io, os, sys, importlib.util
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402
HERE = os.path.dirname(os.path.abspath(__file__))

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

D = load('bookdata', os.path.join(HERE, 'data.py'))
SEC = load('secdata', os.path.join(os.path.dirname(HERE), 'sec', 'data.py'))
CAT = {c['key']: c for c in SEC.CATS}

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))

BY = {b['id']: b for b in D.B}
ORDER = [b['id'] for b in D.B]

CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'
SOFT = 'background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 14px;'
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
GRID = 'display: grid; grid-template-columns: repeat(auto-fit, minmax(%dpx, 1fr)); gap: %dpx;'

def num(bid): return int(bid[1:])

def page(b):
    c = CAT[b['cat']]
    col, soft = c['color'], c['soft']
    i = ORDER.index(b['id'])
    prev = BY[ORDER[i - 1]] if i > 0 else None
    nxt = BY[ORDER[i + 1]] if i < len(ORDER) - 1 else None
    pair = BY[b['pair'][0]]
    o = []
    w = o.append
    w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>%s — %s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&amp;display=swap">
<style>
  body{margin:0;font-family:'Vazirmatn',system-ui,sans-serif;background:#F5F3EE;color:#16181C;-webkit-font-smoothing:antialiased}
  a{color:%s;text-decoration:none}
  a:hover{opacity:.82}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:78px}
  ::selection{background:%s;color:%s}
</style>
</helmet>

<div style="width: 100%%; min-height: 100vh; background: #F5F3EE; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 30; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 900px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
      <a href="Security.dc.html" style="font-size: 13.5px; font-weight: 600; color: #45494F;">← پنجاه سال دفاع</a>
      <a href="Library.dc.html" style="font-size: 13px; color: #666158; margin-inline-start: auto;">کتابخانهٔ منابع</a>
    </div>
  </header>

  <main style="max-width: 900px; margin: 0 auto; padding: 44px 24px 70px;">

    <div style="display: flex; align-items: center; gap: 9px; flex-wrap: wrap; margin-bottom: 18px;">
      <span style="font-size: 11.5px; font-weight: 700; color: %s; background: %s; border-radius: 999px; padding: 4px 12px;">%s</span>
      <span style="font-size: 11.5px; color: #666158; background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 999px; padding: 4px 12px;">کتاب، %s</span>
      <span style="font-size: 11.5px; color: #666158;">%s از ۱۵ کتاب فهرست</span>
    </div>

    <h1 style="font-size: clamp(27px, 4vw, 40px); font-weight: 800; line-height: 1.45; margin: 0 0 14px;">%s</h1>
    <p style="%s font-size: 17px; font-weight: 600; line-height: 1.7; color: #45494F; margin: 0 0 8px; overflow-wrap: anywhere;">%s</p>
    <p style="font-size: 14.5px; line-height: 1.8; color: #666158; margin: 0 0 30px;">%s</p>

    <div style="background: %s; border-inline-start: 4px solid %s; border-radius: 14px; padding: 22px 24px; margin-bottom: 30px;">
      <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 9px;">یک ایده که از این کتاب می‌ماند</div>
      <p style="font-size: 17px; line-height: 1.95; font-weight: 600; color: #16181C; margin: 0;">%s</p>
    </div>
''' % (b['fa'], 'کتاب‌های امنیت', col, soft, col,
       col, soft, c['name'], fa(b['year']), fa(num(b['id'])),
       b['fa'], LTR, b['en'], b['who_wrote'],
       soft, col, col, b['idea']))

    w('''    <section style="%s padding: 26px 28px; margin-bottom: 14px;">
      <h2 style="font-size: 19px; font-weight: 800; margin: 0 0 14px;">چرا این کتاب مهم است</h2>''' % CARD)
    for p in b['why']:
        w('''      <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0 0 14px;">%s</p>''' % p)
    w('''    </section>''')

    w('''    <section style="%s padding: 26px 28px; margin-bottom: 14px;">
      <h2 style="font-size: 19px; font-weight: 800; margin: 0 0 6px;">داخلش چیست</h2>
      <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0 0 16px;">در سطح کلی، نه فهرست فصل‌به‌فصل.</p>
      <div style="display: flex; flex-direction: column; gap: 10px;">''' % CARD)
    for it in b['inside']:
        w('''        <div style="display: flex; gap: 11px; align-items: flex-start;">
          <span style="width: 7px; height: 7px; border-radius: 50%%; background: %s; flex-shrink: 0; margin-top: 9px;"></span>
          <span style="font-size: 14.5px; line-height: 1.95; color: #45494F;">%s</span>
        </div>''' % (col, it))
    w('''      </div>
    </section>''')

    w('''    <section style="%s padding: 26px 28px; margin-bottom: 14px;">
      <h2 style="font-size: 19px; font-weight: 800; margin: 0 0 12px;">برای چه کسی</h2>
      <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0;">%s</p>
    </section>''' % (CARD, b['who']))

    w('''    <div style="%s margin-bottom: 14px;">
      <section style="%s padding: 24px 26px; border-top: 3px solid #B4530E;">
        <h2 style="font-size: 16px; font-weight: 800; margin: 0 0 12px; color: #B4530E;">چه چیزی کهنه شده</h2>
        <p style="font-size: 14.5px; line-height: 2; color: #45494F; margin: 0;">%s</p>
      </section>
      <section style="%s padding: 24px 26px; border-top: 3px solid #166534;">
        <h2 style="font-size: 16px; font-weight: 800; margin: 0 0 12px; color: #166534;">چه چیزی کهنه نشده</h2>
        <p style="font-size: 14.5px; line-height: 2; color: #45494F; margin: 0;">%s</p>
      </section>
    </div>''' % (GRID % (280, 14), SOFT, b['stale'], SOFT, b['alive']))

    pc = CAT[pair['cat']]
    w('''    <section style="%s padding: 26px 28px; margin-bottom: 14px;">
      <h2 style="font-size: 19px; font-weight: 800; margin: 0 0 14px;">کنارش چه بخوان</h2>
      <a href="SecBook%02d.dc.html" style="display: block; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 12px; padding: 18px 20px; border-inline-start: 3px solid %s;">
        <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 7px;">%s، %s</div>
        <div style="font-size: 15.5px; font-weight: 700; color: #16181C; margin-bottom: 6px;">%s</div>
        <div style="font-size: 13.5px; line-height: 1.85; color: #45494F;">%s</div>
      </a>
      <p style="font-size: 13.5px; line-height: 2; color: #666158; margin: 16px 0 0;"><b>کجا پیدایش کنی:</b> %s</p>
      <p style="margin: 10px 0 0;"><a href="%s" target="_blank" rel="noopener" style="font-size: 13px; font-weight: 700; color: %s; %s display: inline-block; max-width: 100%%; overflow-wrap: anywhere;">%s ↗</a></p>
    </section>''' % (CARD, num(pair['id']), pc['color'], pc['color'], pc['name'], fa(pair['year']),
                     pair['fa'], b['pair'][1], b['where'], b['link'], col, LTR, b['link']))

    w('''    <nav style="display: flex; gap: 14px; align-items: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #E4E1D6; flex-wrap: wrap;">''')
    if prev:
        w('''      <a href="SecBook%02d.dc.html" style="font-size: 13.5px; font-weight: 600; color: %s;">→ %s (%s)</a>''' % (num(prev['id']), col, prev['fa'], fa(prev['year'])))
    w('''      <span style="flex: 1;"></span>''')
    if nxt:
        w('''      <a href="SecBook%02d.dc.html" style="font-size: 13.5px; font-weight: 600; color: %s;">%s (%s) ←</a>''' % (num(nxt['id']), col, nxt['fa'], fa(nxt['year'])))
    w('''    </nav>
  </main>

  <footer style="border-top: 1px solid #E4E1D6; background: #FFFFFF;">
    <div style="max-width: 900px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Security.dc.html" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نقشهٔ ۶۱ اثر</a>
      <span style="font-size: 12.5px; color: #666158;">رضا هاشمی · کتاب‌های امنیت</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":900,"height":1200}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>
</body>
</html>
''')
    return ''.join(o)


if __name__ == '__main__':
    import json
    desc = {}
    for b in D.B:
        html = page(b)
        out = os.path.join(SRC, 'SecBook%02d.dc.html') % num(b['id'])
        io.open(out, 'w', encoding='utf-8').write(html)
        desc['sec-book-%02d.html' % num(b['id'])] = (
            '%s (%s) نوشتهٔ %s — چرا این کتاب مهم است، داخلش چیست، چه چیزی کهنه شده و چه چیزی نشده.'
            % (b['fa'], fa(b['year']), b['who_wrote'].split(' · ')[0])
        )
    p = os.path.join(SRC, 'descriptions.books.json')
    io.open(p, 'w', encoding='utf-8').write(json.dumps(desc, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    print('۱۵ صفحهٔ کتاب نوشته شد')


# ---------------------------------------------------------------- شبکهٔ کتاب‌ها در صفحهٔ «کتاب‌ها»
SENTINEL = '<!-- شبکهٔ پانزده کتاب امنیت — tools/books -->'

def inject_books_page():
    """پانزده کارت کتاب را در src/Books.dc.html می‌گذارد. بی‌خطر و تکرارپذیر:
    اگر قبلاً گذاشته شده باشد، اول برش می‌دارد و دوباره می‌نویسد."""
    p = os.path.join(SRC, 'Books.dc.html')
    t = io.open(p, encoding='utf-8').read()

    import re as _re
    t = _re.sub(_re.escape(SENTINEL) + '.*?' + _re.escape(SENTINEL) + r'\n', '', t, flags=_re.S)

    o = []
    w = o.append
    w(SENTINEL)
    w('''
        <h2 style="font-size: 18px; font-weight: 800; margin: 40px 0 6px;">پانزده کتاب، هر کدام با صفحهٔ خودش</h2>
        <p style="font-size: 14.5px; line-height: 1.95; color: #4A4F58; max-width: 66ch; margin: 0 0 20px;">این پانزده کتاب از دل نقشهٔ <a href="Security.dc.html" style="font-weight: 600;">پنجاه سال دفاع</a> بیرون آمده‌اند. برای هر کدام نوشته‌ام چرا مهم است، داخلش چیست، <b>چه چیزی کهنه شده</b> و چه چیزی نشده — چون در این رشته، نگفتنِ بخش دوم به اندازهٔ نگفتن بخش اول گمراه‌کننده است.</p>
        <div style="''' + (GRID % (260, 14)) + '''">''')
    for b in D.B:
        c = CAT[b['cat']]
        w('''          <a href="SecBook%02d.dc.html" style="display: flex; flex-direction: column; background: #FFFFFF; border: 1px solid #D5DDD2; border-radius: 14px; padding: 20px 22px; border-top: 3px solid %s;">
            <div style="display: flex; align-items: baseline; gap: 8px; margin-bottom: 10px; flex-wrap: wrap;">
              <span style="font-size: 11px; font-weight: 700; color: %s;">%s</span>
              <span style="font-size: 11px; color: #666158; margin-inline-start: auto;">%s</span>
            </div>
            <h3 style="font-size: 14.5px; font-weight: 700; color: #16181C; margin: 0 0 7px; line-height: 1.6;">%s</h3>
            <p style="font-size: 11.5px; line-height: 1.6; color: #666158; margin: 0 0 10px; %s">%s</p>
            <p style="font-size: 12.8px; line-height: 1.85; color: #4A4F58; margin: 0 0 12px; flex: 1;">%s</p>
            <span style="font-size: 12.5px; font-weight: 700; color: %s;">معرفی کامل ←</span>
          </a>''' % (num(b['id']), c['color'], c['color'], c['name'], fa(b['year']),
                     b['fa'], LTR, b['en'], b['idea'], c['color']))
    w('''        </div>''')
    w(SENTINEL)

    block = '\n'.join(o)
    anchor = '''        </div>
      </div>
    </section>

  </main>'''
    assert t.count(anchor) == 1, 'جای تزریق در Books.dc.html پیدا نشد'
    t = t.replace(anchor, '        </div>\n' + block + '\n      </div>\n    </section>\n\n  </main>', 1)
    io.open(p, 'w', encoding='utf-8').write(t)
    print('شبکهٔ ۱۵ کتاب به صفحهٔ کتاب‌ها اضافه شد')

inject_books_page()
