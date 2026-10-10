# -*- coding: utf-8 -*-
import io, os, sys, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import logic as L
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402

ROWS = L.ROWS
AC = '#1F4E5F'
SOFTAC = '#E2EDF1'
CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'
SOFT = 'background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 14px;'
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
EYE = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %s; margin: 0 0 12px;' % AC
H2 = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
LEAD = 'font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 10px;'
MUTE = 'font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 22px;'
fa = L.fa

N = len(ROWS)
YEARS = [r['year'] for r in ROWS]
Y0, Y1 = min(YEARS), max(YEARS)
NLINK = sum(1 for r in ROWS if r['link'])
CROSS = [r for r in ROWS if len(r['domains']) > 1]
DEC = collections.Counter((y // 10) * 10 for y in YEARS)
DECS = sorted(DEC)
DMAX = max(DEC.values())

o = []
w = o.append

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>کتابخانه — هر چیزی که این سایت به آن تکیه کرده</title>
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
  a{color:#2F5233;text-decoration:none}
  a:hover{color:#1F3A22}
  button{font-family:inherit;cursor:pointer;border:none}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  ::selection{background:#E2EDF1;color:#1F4E5F}
  input{font-family:inherit;font-size:15px;color:#16181C;background:#FFFFFF;border:1px solid #D9D5C9;border-radius:12px;padding:13px 16px;width:100%;box-sizing:border-box}
  input:focus{outline:2px solid #1F4E5F;outline-offset:1px}
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F5F3EE; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1120px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13.5px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <nav style="display: flex; gap: 2px; margin-inline-start: auto; flex-wrap: wrap;">
        <a href="#s1" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۱ شتاب</a>
        <a href="#s2" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۲ ستون فقرات</a>
        <a href="#s3" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۳ کتابخانه</a>
        <a href="#s4" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۴ روش</a>
      </nav>
    </div>
  </header>

  <main>
''')

# ---------------------------------------------------------------- هیرو
w('''
    <section style="max-width: 1120px; margin: 0 auto; padding: 58px 24px 10px;">
      <p style="%s">کتابخانهٔ یکپارچه · %s منبع · ۵ بخش · از %s تا %s</p>
      <h1 style="font-size: clamp(30px, 5vw, 50px); line-height: 1.38; font-weight: 800; margin: 0 0 20px; letter-spacing: -0.01em;">کتابخانه</h1>
      <p style="font-size: 18.5px; line-height: 1.95; color: #45494F; max-width: 64ch; margin: 0 0 18px;">هر ادعایی که در این سایت نوشته شده، به یکی از این <b>%s اثر</b> برمی‌گردد. تا امروز این ارجاع‌ها ته هر صفحه پخش بودند؛ این‌جا همه‌شان یک‌جا، قابل جست‌وجو و فیلتر.</p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">یک دلیل ساده برای ساختنش داشتم: اگر چیزی را نشود بررسی کرد، ادعا است نه نوشته. این صفحه کاری می‌کند که بشود هر جمله‌ای از این سایت را تا سرچشمه‌اش دنبال کرد — <b>%s تای این آثار پیوند مستقیم</b> به متن اصلی دارند.</p>
      <p style="font-size: 14.5px; line-height: 1.9; color: #666158; max-width: 64ch; margin: 0 0 30px;">و یک چیز غیرمنتظره هم از دلش بیرون آمد: <b>%s اثر</b> در بیش از یک بخش سایت ارجاع شده‌اند. این‌ها نقطه‌هایی‌اند که موضوع‌های ظاهراً جدا به هم می‌رسند — بخش ۰۲ همین‌هاست.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="#s3" style="font-size: 14.5px; font-weight: 700; color: #FFFFFF; background: %s; padding: 13px 26px; border-radius: 10px;">جست‌وجو در کتابخانه</a>
        <a href="#s2" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">آثاری که همه‌جا تکرار شده‌اند ←</a>
      </div>
    </section>
''' % (EYE, fa(N), fa(Y0), fa(Y1), fa(N), fa(NLINK), fa(len(CROSS)), AC))

# آمار کوتاه
STATS = [(fa(N), 'اثر یکتا'), (fa(NLINK), 'با پیوند مستقیم'), (fa(len(CROSS)), 'در چند بخش'),
         (fa(Y1 - Y0), 'سال، از %s تا %s' % (fa(Y0), fa(Y1)))]
w('''    <section style="max-width: 1120px; margin: 0 auto; padding: 26px 24px 10px;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px;">''')
for v, lab in STATS:
    w('''        <div style="%s padding: 20px 22px;">
          <div style="font-size: 28px; font-weight: 800; color: %s; line-height: 1;">%s</div>
          <div style="font-size: 12.5px; color: #666158; margin-top: 8px;">%s</div>
        </div>''' % (CARD, AC, v, lab))
w('''      </div>
    </section>''')

# ---------------------------------------------------------------- ۰۱ شتاب
w('''
    <section id="s1" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۱ — شتاب</p>
      <h2 style="%s">همهٔ این منابع، به ترتیب دهه</h2>
      <p style="%s">این نمودار ادعای بزرگی ندارد: فقط نشان می‌دهد <b>من</b> از کدام دهه‌ها بیشتر خوانده‌ام. ولی شکلش تصادفی نیست — هرچه به امروز نزدیک‌تر می‌شویم، کارهای تعیین‌کننده بیشتر می‌شوند.</p>
      <p style="%s">دههٔ ۲۰۲۰ هنوز تمام نشده و همین حالا %s اثر دارد.</p>
      <div style="%s padding: 24px 26px; margin-bottom: 14px;">''' % (EYE, H2, LEAD, MUTE, fa(DEC[2020]), CARD))
for d in DECS:
    c = DEC[d]
    w('''        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
          <span style="font-size: 12.5px; font-weight: 700; color: #45494F; width: 54px; flex-shrink: 0; font-variant-numeric: tabular-nums;">%s</span>
          <div style="flex: 1; height: 15px; background: #F0EEE7; border-radius: 8px; overflow: hidden;">
            <div style="width: %.1f%%; height: 100%%; background: %s; border-radius: 8px;"></div>
          </div>
          <span style="font-size: 12px; color: #666158; width: 38px; flex-shrink: 0; text-align: left;">%s</span>
        </div>''' % (fa(d), c / DMAX * 100, AC, fa(c)))
w('''        <p style="font-size: 11.5px; color: #666158; margin: 8px 0 0; padding-top: 14px; border-top: 1px solid #F0EEE7;">این فهرست سوگیری دارد و می‌دانمش: کارهای تازه هنوز غربال تاریخی نشده‌اند و احتمالاً چند تایشان ده سال دیگر بی‌اهمیت به نظر می‌رسند.</p>
      </div>
    </section>''')

# ---------------------------------------------------------------- ۰۲ ستون فقرات
w('''
    <section id="s2" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۲ — ستون فقرات</p>
      <h2 style="%s">%s اثری که در بیش از یک بخش سایت آمده‌اند</h2>
      <p style="%s">این‌ها را از قبل انتخاب نکرده بودم؛ وقتی همهٔ ارجاع‌ها را کنار هم گذاشتم، خودشان بیرون آمدند. هر کدام جایی است که دو موضوع ظاهراً بی‌ربط به یک مقاله می‌رسند.</p>
      <p style="%s">مثلاً «توجه تمام آن چیزی است که لازم داری» هم در مسیر یادگیری ماشین آمده و هم در معماری سواد — و «استخراج دادهٔ آموزش» هم در امنیت و هم در سواد. این دومی دقیقاً همان جایی است که امنیت و هوش مصنوعی یک مسئلهٔ مشترک پیدا می‌کنند.</p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px;">''' % (EYE, H2, fa(len(CROSS)), LEAD, MUTE))
for r in CROSS:
    cols = [L.DOMCOL[d] for d in r['domains']]
    w('''        <div style="%s padding: 20px 22px; border-top: 3px solid %s;">
          <div style="display: flex; align-items: baseline; gap: 9px; flex-wrap: wrap; margin-bottom: 8px;">
            <span style="font-size: 15px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>
            <span style="font-size: 11px; color: #666158;">%s</span>
          </div>
          <p style="font-size: 13.5px; line-height: 1.7; font-weight: 600; color: #16181C; margin: 0 0 10px; %s">%s</p>
          <div style="display: flex; gap: 6px; flex-wrap: wrap;">''' % (
        SOFT, cols[0][0], cols[0][0], fa(r['year']), r['kind'], LTR, r['titleEn']))
    for d in r['domains']:
        c, s = L.DOMCOL[d]
        w('''<span style="font-size: 11px; font-weight: 700; color: %s; background: %s; border-radius: 999px; padding: 4px 10px;">%s</span>''' % (c, s, d))
    w('''          </div>
        </div>''')
w('''      </div>
      </div>
    </section>''')

# ---------------------------------------------------------------- ۰۳ کتابخانه (تعاملی)
w('''
    <section id="s3" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۳ — کتابخانه</p>
      <h2 style="%s">هر %s اثر، قابل جست‌وجو</h2>
      <p style="%s">در عنوان فارسی و انگلیسی، نام پدیدآور، سال و توضیح جست‌وجو می‌شود. فیلترها با هم کار می‌کنند.</p>

      <div style="%s padding: 22px 24px; margin-bottom: 16px;">
        <input id="q" type="search" value="{{q}}" onInput="{{onQ}}" placeholder="جست‌وجو: نام اثر، پدیدآور، سال یا موضوع…" aria-label="جست‌وجو در کتابخانه">

        <div style="margin-top: 18px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">بخش سایت</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{domChips}}" as="c" hint-placeholder-count="6">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}<sc-if value="{{c.hasCount}}"><span style="font-size: 11px; opacity: 0.7;">{{c.count}}</span></sc-if></button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 16px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">نوع اثر</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{kindChips}}" as="c" hint-placeholder-count="5">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}<sc-if value="{{c.hasCount}}"><span style="font-size: 11px; opacity: 0.7;">{{c.count}}</span></sc-if></button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 16px; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
          <span style="font-size: 11.5px; font-weight: 700; color: #666158;">ترتیب</span>
          <sc-for list="{{sortChips}}" as="c" hint-placeholder-count="2">
            <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
          </sc-for>
        </div>

        <div style="margin-top: 18px; padding-top: 16px; border-top: 1px solid #F0EEE7; display: flex; gap: 12px; flex-wrap: wrap; align-items: center;">
          <span style="font-size: 13px; color: #45494F;"><b>{{countFa}}</b> اثر</span>
          <sc-if value="{{filtered}}">
            <button style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 999px; padding: 7px 14px; cursor: pointer;" onClick="{{onClear}}">برداشتن فیلترها</button>
          </sc-if>
        </div>
      </div>

      <sc-if value="{{empty}}">
        <div style="%s border-style: dashed; padding: 40px; text-align: center;">
          <p style="font-size: 14.5px; color: #45494F; margin: 0 0 6px;">با این فیلترها اثری پیدا نشد.</p>
          <p style="font-size: 13px; color: #666158; margin: 0;">شاید با عنوان انگلیسی یا نام پدیدآور جست‌وجو کنی.</p>
        </div>
      </sc-if>

      <div style="display: flex; flex-direction: column; gap: 10px;">
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="12">
          <div style="background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 14px; padding: 18px 20px; border-inline-start: 3px solid {{r.color}};">
            <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
              <span style="font-size: 16px; font-weight: 800; color: {{r.color}}; font-variant-numeric: tabular-nums;">{{r.yFa}}</span>
              <span style="font-size: 11px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 3px 9px;">{{r.kind}}</span>
              <sc-if value="{{r.cross}}">
                <span style="font-size: 11px; font-weight: 700; color: #1F4E5F; background: #E2EDF1; border-radius: 999px; padding: 3px 9px;">در {{r.crossFa}} بخش</span>
              </sc-if>
            </div>
            <sc-if value="{{r.hasFa}}">
              <h3 style="font-size: 15px; font-weight: 700; margin: 0 0 5px; line-height: 1.6; color: #16181C;">{{r.fa}}</h3>
            </sc-if>
            <p style="font-size: 13.5px; line-height: 1.7; font-weight: 600; color: #16181C; margin: 0 0 5px; direction: ltr; text-align: left; unicode-bidi: isolate;">{{r.en}}</p>
            <p style="font-size: 12px; line-height: 1.75; color: #666158; margin: 0 0 10px; direction: ltr; text-align: left; unicode-bidi: isolate;">{{r.who}}</p>
            <sc-if value="{{r.hasNote}}">
              <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0 0 12px; max-width: 78ch;">{{r.note}}</p>
            </sc-if>
            <div style="display: flex; gap: 7px; flex-wrap: wrap; align-items: center;">
              <sc-for list="{{r.doms}}" as="d" hint-placeholder-count="1">
                <sc-if value="{{d.sec}}"><a href="Security.dc.html" style="font-size: 11px; font-weight: 700; color: {{d.color}}; background: {{d.soft}}; border-radius: 999px; padding: 4px 10px;">{{d.name}} ←</a></sc-if>
                <sc-if value="{{d.learn}}"><a href="Learn.dc.html" style="font-size: 11px; font-weight: 700; color: {{d.color}}; background: {{d.soft}}; border-radius: 999px; padding: 4px 10px;">{{d.name}} ←</a></sc-if>
                <sc-if value="{{d.ai}}"><a href="AILiteracy.dc.html" style="font-size: 11px; font-weight: 700; color: {{d.color}}; background: {{d.soft}}; border-radius: 999px; padding: 4px 10px;">{{d.name}} ←</a></sc-if>
                <sc-if value="{{d.chess}}"><a href="Chess.dc.html" style="font-size: 11px; font-weight: 700; color: {{d.color}}; background: {{d.soft}}; border-radius: 999px; padding: 4px 10px;">{{d.name}} ←</a></sc-if>
                <sc-if value="{{d.game}}"><a href="GameTheory.dc.html" style="font-size: 11px; font-weight: 700; color: {{d.color}}; background: {{d.soft}}; border-radius: 999px; padding: 4px 10px;">{{d.name}} ←</a></sc-if>
              </sc-for>
              <sc-if value="{{r.hasLink}}">
                <a href="{{r.link}}" target="_blank" rel="noopener" style="font-size: 11.5px; font-weight: 700; color: #1F4E5F; margin-inline-start: auto;">متن اصلی ←</a>
              </sc-if>
            </div>
          </div>
        </sc-for>
      </div>
    </section>''' % (EYE, H2, fa(N), LEAD, CARD, CARD))

# ---------------------------------------------------------------- ۰۴ روش
METHOD = [
    ('از کجا آمده', 'این فهرست دست‌نویس نیست: از خودِ صفحه‌های سایت استخراج شده. ارجاع‌های «پنجاه سال دفاع»، «شانزده ستون»، «شصت‌وچهار خانه»، «مسیر یادگیری ماشین» و «نظریهٔ بازی‌ها» یک‌جا جمع شدند و تکراری‌ها ادغام.'),
    ('ادغام چطور انجام شد', 'تطبیق بر اساس عنوان اصلی اثر، پس از عادی‌سازی. از %s ارجاع خام، %s اثر یکتا ماند و %s تا در بیش از یک بخش بودند. هر ادغام را خودم بررسی کردم؛ هیچ دو اثر متفاوتی اشتباهی یکی نشده‌اند.' % (fa(182), fa(N), fa(len(CROSS)))),
    ('سال انتشار', 'سال <b>اولین انتشار عمومی</b> ملاک است، نه سال ویرایش بعدی یا سال کنفرانس. برای کارهایی که اول روی arXiv آمده‌اند، همان سال ثبت شده.'),
    ('چه چیزی این‌جا نیست', 'منابعی که فقط برای بررسی خوانده شده‌اند ولی در هیچ صفحه‌ای به آن‌ها ارجاع نشده. این کتابخانه، کتابخانهٔ <b>ارجاع‌هاست</b>، نه هر چیزی که خوانده‌ام.'),
    ('پیوندها', '%s اثر از %s تا پیوند مستقیم دارند. بقیه عنوان و پدیدآور کامل دارند تا بشود مستقیم جست‌وجو کرد؛ برای کتاب‌ها و استانداردها عمداً پیوند نگذاشته‌ام چون نشانی‌شان زود عوض می‌شود.' % (fa(NLINK), fa(N))),
    ('به‌روز می‌ماند', 'هر نوشتهٔ تازه‌ای که به سایت اضافه شود، منابعش خودکار به این فهرست می‌آید — چون این صفحه از همان داده ساخته می‌شود، نه جدا از آن.'),
]
w('''
    <section id="s4" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 64px;">
      <p style="%s">۰۴ — روش</p>
      <h2 style="%s">این فهرست چطور ساخته شد</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px; margin-bottom: 18px;">''' % (EYE, H2))
for t, d in METHOD:
    w('''        <div style="%s padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, t, d))
w('''      </div>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="Security.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">نقشهٔ ادبیات امنیت ←</a>
        <a href="AILiteracy.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">معماری سواد هوش مصنوعی ←</a>
        <a href="Chess.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">شطرنج و یادگیری ماشین ←</a>
        <a href="Glossary.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">واژه‌نامهٔ ۲۸۵ اصطلاح ←</a>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid #E4E1D6; background: #FFFFFF;">
    <div style="max-width: 1120px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: #666158;">رضا هاشمی · کتابخانهٔ منابع</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1120,"height":1400}}'>
''' + L.LOGIC.strip() + '''
</script>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'Library.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars ·', N, 'refs ·', len(CROSS), 'cross')
