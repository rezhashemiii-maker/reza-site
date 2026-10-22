# -*- coding: utf-8 -*-
"""«مسئله، به‌عنوان دارایی» → src/Money.dc.html

پول درآوردن از مسئله‌های ریاضی: پیدا کردن، حل کردن، و ساختن. شکلِ
تکه‌ها از tools/gen/lib/longform.py می‌آید و متن از
tools/gen/money/text.py؛ این فایل فقط پالت، ناوبری و چیدمان را دارد.
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'lib'))
sys.path.insert(0, HERE)
from paths import SRC  # noqa: E402
import longform as LF  # noqa: E402
import text as T  # noqa: E402

V = dict(
    AC='#2C5A4E',        # سبزِ عمیق
    SOFT='#E3EEEA',
    INK='#16181C',
    MID='#45494F',
    DIM='#666158',
    LINE='#E4E1D6',
    WARM='#B4530E',
    WSOFT='#F7E3D6',
    KEY='#1F5B3A',
    KSOFT='#E6F0E9',
    CODE='#1B1F27',
)
V['WHYLAB'] = 'نکتهٔ عملی'
V = LF.style(V)

fa = LF.fa
o, w, block = LF.writer(V)

NAVLAB = dict(three='سه الگو', solved='نمونه‌های حل‌شده', prizes='جایزه‌ها',
              designed='مسئله‌سازی', paths='هشت راه', future='دوازده پیشنهاد',
              traps='تله‌ها', how='از صفر')
NAV = [(s['id'], NAVLAB[s['id']]) for s in T.S]
NAV += [('src', 'منابع')]

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>مسئله، به‌عنوان دارایی — پول درآوردن از مسئله‌های ریاضی</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&amp;display=swap">
<style>
  body{margin:0;font-family:'Vazirmatn',system-ui,sans-serif;background:#F4F7F5;color:#16181C;-webkit-font-smoothing:antialiased}
  a{color:#2C5A4E;text-decoration:none}
  a:hover{text-decoration:underline}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  b,strong{font-weight:700;color:#16181C}
  ::selection{background:#E3EEEA;color:#2C5A4E}
  @media (max-width:900px){
    nav[data-sections]{display:none !important}
    div[data-sectionlist]{display:flex !important}
  }
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F4F7F5; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(244,247,245,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1000px; margin: 0 auto; padding: 12px 24px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <nav data-sections="1" style="display: flex; gap: 1px; margin-inline-start: auto; flex-wrap: wrap;">''')
for sid, lab in NAV:
    w('        <a href="#%(sid)s" style="font-size: 11.5px; color: #45494F; padding: 5px 8px; border-radius: 999px;">%(lab)s</a>',
      sid=sid, lab=lab)
w('''      </nav>
    </div>
  </header>

  <main>

    <section style="max-width: 1000px; margin: 0 auto; padding: 56px 24px 20px;">
      <p style="%(EYE)s">نوشتهٔ بلند · مسئله و پول · هشت بخش</p>
      <h1 style="font-size: clamp(30px, 4.6vw, 48px); font-weight: 800; margin: 0 0 22px; line-height: 1.34; letter-spacing: -0.015em;">مسئله،<br>به‌عنوان دارایی</h1>''')
for p in T.LEAD:
    w('      <p style="%(LEAD)s">%(t)s</p>', t=p)
w('''      <div style="background: %(SOFT)s; border-inline-start: 4px solid %(AC)s; border-radius: 0 13px 13px 0; padding: 17px 20px; margin: 24px 0 0; max-width: 68ch;">
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0;">%(t)s</p>
      </div>

      <div data-sectionlist="1" style="display: none; gap: 6px; flex-wrap: wrap; margin-top: 24px;">''', t=T.LEAD_NOTE)
for sid, lab in NAV:
    w('        <a href="#%(sid)s" style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 7px 12px; border-radius: 999px;">%(lab)s</a>',
      sid=sid, lab=lab)
w('      </div>\n    </section>\n')

# ───────────────────────────────────────────── دوازده قصه
for i, sec in enumerate(T.S):
    white = (i % 2 == 0)
    bg = '#FFFFFF' if white else 'transparent'
    bd = ('border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s;' % V) if white else ''
    w('''
    <section id="%(id)s" style="background: %(bg)s; %(bd)s margin-top: 34px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">%(eye)s</p>
      <h2 style="%(H2)s">%(t)s</h2>''', id=sec['id'], eye=sec['eye'], t=sec['t'], bg=bg, bd=bd)
    for it in sec['body']:
        block(it)
    w('      </div>\n    </section>\n')

# ───────────────────────────────────────────── منابع
w('''
    <section id="src" style="background: #FFFFFF; border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s; margin-top: 38px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">روش و منابع</p>
      <h2 style="%(H2)s">کجا باید با احتیاط خواند</h2>
      <p style="%(BODY)s">%(note)s</p>
      <div style="display: flex; flex-direction: column; gap: 9px; max-width: 72ch;">''', note=T.SRC_NOTE)
for i, (t, u, why) in enumerate(T.SOURCES):
    w('''        <div style="%(SOFTC)s padding: 17px 19px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 7px;">
            <span style="font-size: 11.5px; font-weight: 800; color: %(AC)s;">%(n)s</span>
            <span style="font-size: 14px; font-weight: 700; color: %(INK)s; line-height: 1.65;">%(t)s</span>
          </div>
          <p style="font-size: 13px; line-height: 1.95; color: %(MID)s; margin: 0 0 8px;">%(why)s</p>''',
      n=fa('%02d' % (i + 1)), t=t, why=why)
    if u:
        w('''          <p style="margin: 0;"><a href="%(u)s" target="_blank" rel="noopener" style="direction: ltr; unicode-bidi: isolate; font-size: 12px; font-weight: 700; color: %(AC)s; display: inline-block; max-width: 100%%; overflow-wrap: anywhere;">%(u)s ↗</a></p>''',
          u=u)
    else:
        w('''          <p style="font-size: 12px; color: %(DIM)s; margin: 0;">کتاب است و نسخهٔ آزادِ آنلاین ندارد؛ با همین عنوان و شابک پیدا می‌شود.</p>''')
    w('        </div>')
w('      </div>')

w('''      <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 26px;">
        <a href="Prob.dc.html" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: %(AC)s; padding: 12px 22px; border-radius: 10px;">پنج هزار سال تاس — تولدِ احتمال ←</a>
        <a href="Foundations.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">ریاضی، از راهِ شکستن ←</a>
      </div>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid %(LINE)s; background: #FFFFFF;">
    <div style="max-width: 1000px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: %(DIM)s;">رضا هاشمی · مسئله، به‌عنوان دارایی</span>
    </div>
  </footer>

</div>
</x-dc>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'Money.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'نویسه ·', len(T.S), 'بخش ·', len(T.SOURCES), 'منبع')
