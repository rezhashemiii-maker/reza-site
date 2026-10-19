# -*- coding: utf-8 -*-
"""«پروندهٔ یک کلمه» → src/Sets.dc.html

یک نوشتهٔ بلند. ساختارش از tools/gen/sets/text.py می‌آید و این فایل فقط
آن را به HTML درمی‌آورد.

دو قاعده که در این صفحه رعایت شده‌اند:
  • هیچ جدولِ اسکرول‌دار. هر چیزی که در منبع جدول بود، این‌جا فهرستی از
    کارت‌هاست تا در عرضِ ۳۹۰ پیکسل هم بی‌سرریز باشد.
  • هیچ لاتینی بدونِ جداسازی. l() در text.py این کار را می‌کند و در
    کد هم هر تکهٔ لاتین داخلِ span با direction: ltr می‌رود.
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'lib'))
from paths import SRC  # noqa: E402
import longform as LF  # noqa: E402
import text as T  # noqa: E402

V = dict(
    AC='#2E5B7A',        # آبیِ پرونده
    SOFT='#E4EDF3',
    INK='#16181C',
    MID='#45494F',
    DIM='#666158',
    LINE='#E4E1D6',
    WARM='#B4530E',
    WSOFT='#F7E3D6',
    KEY='#1F5B3A',       # سبزِ «چه چیزی مجبورشان کرد»
    KSOFT='#E6F0E9',
    CODE='#1B1F27',
)
V['WHYLAB'] = 'چه چیزی مجبورشان کرد'
V = LF.style(V)

fa = LF.fa
o, w, block = LF.writer(V)


NAVLAB = dict(fear='ممنوعیت', fourier='فوریه', birth='تولدِ مجموعه',
              cut='برش', count='شمارایی', diag='قطر', dust='غبار',
              build='از هیچ', crack='ترک', law='قانون', today='امروز')
NAV = [('locks', 'سه قفل')] + [(s['id'], NAVLAB[s['id']]) for s in T.S]
NAV += [('tasks', 'تمرین'), ('left', 'جا مانده'), ('src', 'منابع')]

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>پروندهٔ یک کلمه — نظریهٔ مجموعه‌ها، از فشارِ فنی تا قانون‌نویسی</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&amp;display=swap">
<style>
  body{margin:0;font-family:'Vazirmatn',system-ui,sans-serif;background:#F6F5F2;color:#16181C;-webkit-font-smoothing:antialiased}
  a{color:#2E5B7A;text-decoration:none}
  a:hover{text-decoration:underline}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  b,strong{font-weight:700;color:#16181C}
  code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
  ::selection{background:#E4EDF3;color:#2E5B7A}
  @media (max-width:900px){
    nav[data-sections]{display:none !important}
    div[data-sectionlist]{display:flex !important}
  }
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F6F5F2; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(246,245,242,0.94); backdrop-filter: blur(10px);">
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
      <p style="%(EYE)s">نوشتهٔ بلند · نظریهٔ مجموعه‌ها · ده پرده</p>
      <h1 style="font-size: clamp(31px, 4.8vw, 50px); font-weight: 800; margin: 0 0 22px; line-height: 1.32; letter-spacing: -0.015em;">پروندهٔ یک کلمه</h1>''')
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

# ───────────────────────────────────────────── سه قفل
w('''
    <section id="locks" style="background: #FFFFFF; border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s; margin-top: 34px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">پیش از شروع</p>
      <h2 style="%(H2)s">سه قفل</h2>
      <p style="%(BODY)s">این سه را اول بخوان و قبل از دیدنِ جواب، خودت یک موضع بگیر. هر سه واقعی‌اند و هر سه در ادامهٔ نوشته برمی‌گردند.</p>''')
for i, k in enumerate(T.LOCKS):
    w('''      <div style="%(CARD)s padding: 21px 23px; margin: 0 0 12px; max-width: 70ch;">
        <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 12px;">
          <span style="font-size: 11.5px; font-weight: 800; color: %(AC)s;">قفلِ %(n)s · %(k)s</span>
          <span style="font-size: 15.5px; font-weight: 700; color: %(INK)s; line-height: 1.7;">%(t)s</span>
        </div>''', n=fa(i + 1), k=k['k'], t=k['t'])
    for q in k['q']:
        w('        <p style="font-size: 15.5px; line-height: 2.1; color: %(MID)s; margin: 0 0 12px;">%(t)s</p>', t=q)
    w('''        <div style="border-inline-start: 3px solid %(WARM)s; background: %(WSOFT)s; border-radius: 0 10px 10px 0; padding: 13px 16px;">
          <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0;">%(t)s</p>
        </div>
      </div>''', t=k['hook'])
for p in T.LOCKS_BRIDGE:
    w('      <p style="%(BODY)s">%(t)s</p>', t=p)
w('      </div>\n    </section>\n')

# ───────────────────────────────────────────── پرده‌ها
for i, sec in enumerate(T.S):
    white = (i % 2 == 1)
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

# ───────────────────────────────────────────── تمرین‌ها
w('''
    <section id="tasks" style="margin-top: 38px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">دوازده تمرین</p>
      <h2 style="%(H2)s">شش معما، و شش جایی که می‌شود سرِ خواننده را کلاه گذاشت</h2>
      <p style="%(BODY)s">نیمی از این‌ها معماست و نیمِ دیگر مغلطه — استدلالی که درست به نظر می‌رسد و نیست. پاسخ‌ها زیرِ هر کدام است، ولی بازش نکن تا خودت یک جواب نداشته باشی. این‌ها همان چیزی‌اند که روی کاغذهای چرک‌نویس اتفاق می‌افتد.</p>
      <div style="display: flex; flex-direction: column; gap: 11px; max-width: 70ch;">''')
for q in T.TASKS:
    tag = V['WARM'] if q['kind'] == 'مغلطه' else V['AC']
    soft = V['WSOFT'] if q['kind'] == 'مغلطه' else V['SOFT']
    w('''        <details style="%(CARD)s padding: 18px 21px;">
          <summary style="cursor: pointer; list-style: none;">
            <span style="display: inline-block; font-size: 10.5px; font-weight: 700; letter-spacing: 0.06em; color: %(tag)s; background: %(soft)s; border-radius: 999px; padding: 4px 10px; margin-bottom: 10px;">%(kind)s %(n)s</span>
            <span style="display: block; font-size: 15.5px; font-weight: 700; color: %(INK)s; line-height: 1.7; margin-bottom: 10px;">%(t)s</span>
            <span style="display: block; font-size: 14.5px; line-height: 2.05; color: %(MID)s;">%(q)s</span>
            <span style="display: block; font-size: 12.5px; font-weight: 700; color: %(AC)s; margin-top: 12px;">پاسخ ↓</span>
          </summary>
          <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 14px 0 0; padding-top: 14px; border-top: 1px solid %(LINE)s;">%(a)s</p>
        </details>''', tag=tag, soft=soft, kind=q['kind'], n=fa(q['n']),
      t=q['t'], q=q['q'], a=q['a'])
w('      </div>\n      </div>\n    </section>\n')

# ───────────────────────────────────────────── جا مانده
w('''
    <section id="left" style="background: #FFFFFF; border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s; margin-top: 38px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">پایان</p>
      <h2 style="%(H2)s">چهار چیزی که این نوشته بی‌اثبات از رویشان پرید</h2>''')
for it in T.LEFT:
    block(it)
w('      </div>\n    </section>\n')

# ───────────────────────────────────────────── منابع
w('''
    <section id="src" style="margin-top: 38px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">روش و منابع</p>
      <h2 style="%(H2)s">کجا باید با احتیاط خواند</h2>
      <p style="%(BODY)s">%(note)s</p>
      <div style="display: flex; flex-direction: column; gap: 9px; max-width: 72ch;">''', note=T.SRC_NOTE)
for i, (t, u, why) in enumerate(T.SOURCES):
    w('''        <div style="%(SOFTC)s padding: 17px 19px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 7px;">
            <span style="font-size: 11.5px; font-weight: 800; color: %(AC)s;">%(n)s</span>
            <span style="direction: ltr; unicode-bidi: isolate; font-size: 14px; font-weight: 700; color: %(INK)s; line-height: 1.6;">%(t)s</span>
          </div>
          <p style="font-size: 13px; line-height: 1.95; color: %(MID)s; margin: 0 0 8px;">%(why)s</p>
          <p style="margin: 0;"><a href="%(u)s" target="_blank" rel="noopener" style="direction: ltr; unicode-bidi: isolate; font-size: 12px; font-weight: 700; color: %(AC)s; display: inline-block; max-width: 100%%; overflow-wrap: anywhere;">%(u)s ↗</a></p>
        </div>''', n=fa('%02d' % (i + 1)), t=t, why=why, u=u)
w('      </div>')

w('''      <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 26px;">
        <a href="Foundations.dc.html" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: %(AC)s; padding: 12px 22px; border-radius: 10px;">ریاضی، از راهِ شکستن ←</a>
        <a href="Music.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">ریاضیاتِ موسیقی ←</a>
      </div>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid %(LINE)s; background: #FFFFFF;">
    <div style="max-width: 1000px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: %(DIM)s;">رضا هاشمی · پروندهٔ یک کلمه</span>
    </div>
  </footer>

</div>
</x-dc>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'Sets.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'نویسه ·', len(T.S), 'پرده ·', len(T.TASKS),
      'تمرین ·', len(T.SOURCES), 'منبع')
