# -*- coding: utf-8 -*-
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data import BANDS, P, PHASES, PATHS, REFS, THANKS_GROUPS
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402

FA = '۰۱۲۳۴۵۶۷۸۹'
def fa(n):
    return ''.join(FA[int(c)] for c in str(n))
def fa2(n):
    return fa('%02d' % n)

BY = {p['n']: p for p in P}
BAND = {b['k']: b for b in BANDS}
TOTAL_C = sum(len(p['concepts_fa']) for p in P)
TOTAL_REF = sum(len(g[2]) for g in REFS)

CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'
SOFT = 'background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 14px;'
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
EYE = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: #2F5233; margin: 0 0 12px;'
H2 = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
LEAD = 'font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 10px;'
MUTE = 'font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 22px;'

o = []
w = o.append

# ---------------------------------------------------------------- سر صفحه
w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>شانزده ستون — معماری سواد هوش مصنوعی</title>
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
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  ::selection{background:#E7ECE4;color:#1F3A22}
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F5F3EE; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1120px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13.5px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <nav style="display: flex; gap: 2px; margin-inline-start: auto; flex-wrap: wrap;">
        <a href="#s1" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۱ نقشه</a>
        <a href="#s2" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۲ تقدم</a>
        <a href="#s3" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۳ خط زمان</a>
        <a href="#s4" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۴ عمق</a>
        <a href="#s5" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۵ ستون‌ها</a>
        <a href="#s6" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۶ مسیرها</a>
        <a href="#s7" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۷ منابع</a>
      </nav>
    </div>
  </header>

  <main>
''')

# ---------------------------------------------------------------- هیرو
w('''
    <section style="max-width: 1120px; margin: 0 auto; padding: 58px 24px 10px;">
      <p style="%s">معماری یادگیری · ۱۶ ستون · %s مفهوم · ۵ لایه · ۳ سطح عمق</p>
      <h1 style="font-size: clamp(30px, 5vw, 50px); line-height: 1.38; font-weight: 800; margin: 0 0 20px; letter-spacing: -0.01em;">شانزده ستون</h1>
      <p style="font-size: 18.5px; line-height: 1.95; color: #45494F; max-width: 64ch; margin: 0 0 18px;">این نقشهٔ کسی است که می‌خواهد بداند <b>همهٔ آن چیزهایی که باید دربارهٔ هوش مصنوعی بداند، چیست</b> — و در هرکدام <b>تا کجا می‌تواند عمیق شود</b>.</p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">مشکل یادگیری این حوزه کمبود منبع نیست؛ نداشتن نقشه است. آدم‌ها از یک ویدیو به یک دورهٔ دیگر می‌پرند، صد اصطلاح یاد می‌گیرند و باز هم نمی‌دانند چه چیزی را <i>نمی‌دانند</i>. این معماری برای همین ساخته شد: نه یک فهرست خواندنی، یک <b>ساختار</b> — که بشود در آن جای خودت را پیدا کنی، بدانی گام بعدی‌ات کدام است، و بدانی کجا می‌توانی آگاهانه بایستی و جلوتر نروی.</p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">مسیر را این‌طور طراحی کردم که هر ستون فقط به ستون‌های قبل از خودش تکیه کند، هیچ ستونی برای همه اجباری نباشد، و برای هرکدام سه سطح عمق روشن باشد: <b>آشنا</b>، <b>کاربر</b>، <b>سازنده</b>. خروجی ساده است — دیگر لازم نیست همهٔ راه را بروی تا بفهمی کجایش به کار تو می‌آید.</p>
      <p style="font-size: 14.5px; line-height: 1.9; color: #666158; max-width: 64ch; margin: 0 0 30px;">۱۶ ستون، %s مفهوم و ۵ لایه؛ در بخش ۰۷ هم %s منبعی که این معماری با آن‌ها سنجیده و غنی شده فهرست شده است.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="#s1" style="font-size: 14.5px; font-weight: 700; color: #FFFFFF; background: #2F5233; padding: 13px 26px; border-radius: 10px;">دیدن نقشه</a>
        <a href="#s6" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">من از کجا شروع کنم؟</a>
        <a href="Literacy.dc.html" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">سنجش سواد فعلی‌ام ←</a>
      </div>
    </section>
''' % (EYE, fa(TOTAL_C), fa(TOTAL_C), fa(TOTAL_REF)))

# سه قاعدهٔ طراحی
w('''
    <section style="max-width: 1120px; margin: 0 auto; padding: 30px 24px 10px;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">''')
RULES = [
    ('۰۱', 'هیچ ستونی پیش‌نیازِ نداشته ندارد', 'هر ستون فقط به ستون‌هایی تکیه می‌کند که قبل از آن آمده‌اند. اگر جایی گیر کردی، یعنی یک ستون عقب‌تر را رد کرده‌ای — نه اینکه کم‌هوشی.'),
    ('۰۲', 'عمق، انتخاب است نه تکلیف', 'برای هر ستون سه سطح تعریف شده. یک پژوهشگر بازاریابی لازم نیست در بنیادهای فنی از سطح یک جلوتر برود، و این کمبود نیست؛ تصمیم است.'),
    ('۰۳', 'ایمنی از روز اول', 'در بیشتر دوره‌ها ایمنی آخرین فصل است. اینجا هم‌زمان با ستون دوم شروع می‌شود، چون کسی که بلد است استفاده کند و بلد نیست راستی‌آزمایی کند، خطرناک‌تر از کسی است که بلد نیست.'),
]
for num, t, d in RULES:
    w('''        <div style="%s padding: 22px 24px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #2F5233; margin-bottom: 9px;">قاعدهٔ %s</div>
          <h3 style="font-size: 16px; font-weight: 800; margin: 0 0 10px; line-height: 1.55;">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, num, t, d))
w('''      </div>
    </section>''')

# ---------------------------------------------------------------- ۰۱ نقشهٔ لایه‌ها
w('''
    <section id="s1" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۱ — نقشهٔ لایه‌ها</p>
      <h2 style="%s">پنج لایه، شانزده ستون</h2>
      <p style="%s">شانزده ستون زیاد به نظر می‌رسد تا وقتی ببینی در <b>پنج لایه</b> جا می‌شوند. هر لایه یک کار می‌کند، و ترتیب لایه‌ها همان ترتیب منطقی یادگیری است: اول <b>ببین</b>، بعد <b>به کار ببر</b>، بعد <b>بفهم</b>، بعد اگر خواستی <b>بساز</b>، و در تمام مسیر <b>داوری کن</b>.</p>
      <p style="%s">عدد کنار هر ستون، شمار مفهوم‌هایی است که زیر آن ستون فهرست شده‌اند — نشانهٔ تقریبی وسعت آن ستون، نه سختی‌اش.</p>''' % (EYE, H2, LEAD, MUTE))

for b in BANDS:
    mem = [p for p in P if p['band'] == b['k']]
    cnt = sum(len(p['concepts_fa']) for p in mem)
    w('''      <div style="background: %s; border: 1px solid %s; border-radius: 16px; padding: 20px 22px; margin-bottom: 12px;">
        <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 4px;">
          <span style="width: 26px; height: 26px; border-radius: 8px; background: %s; color: #FFFFFF; font-size: 13px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">%s</span>
          <h3 style="font-size: 18px; font-weight: 800; margin: 0;">لایهٔ %s</h3>
          <span style="font-size: 12px; color: #666158;">%s ستون · %s مفهوم</span>
        </div>
        <p style="font-size: 12.5px; color: #666158; margin: 0 0 4px; %s">%s</p>
        <p style="font-size: 14px; line-height: 1.95; color: #45494F; margin: 0 0 16px; max-width: 72ch;">%s</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 10px;">''' % (
        b['tint'], b['color'] + '33', b['color'], b['k'], b['fa'], fa(len(mem)), fa(cnt), LTR, b['en'], b['why']))
    for p in mem:
        w('''          <a href="#p%d" style="display: flex; flex-direction: column; background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 12px; padding: 14px 16px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
              <span style="font-size: 15px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>
              <h4 style="font-size: 14px; font-weight: 700; color: #16181C; margin: 0; line-height: 1.5;">%s</h4>
            </div>
            <span style="font-size: 11.5px; color: #666158; margin-bottom: 7px; %s">%s</span>
            <span style="font-size: 11.5px; color: #666158;">%s مفهوم</span>
          </a>''' % (p['n'], b['color'], fa2(p['n']), p['fa'], LTR, p['en'], fa(len(p['concepts_fa']))))
    w('''        </div>
      </div>''')

w('''      <div style="%s padding: 20px 22px;">
        <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">دو ستون عمداً در لایه‌ای نیستند که انتظارش را داری: <b>بهره‌وری</b> و <b>خلق کردن</b> در لایهٔ «به‌کار بردن» نشسته‌اند، نه در لایهٔ «ساختن». چون برای ساختن یک چیز زیبا یا آزاد کردن ده ساعت در هفته، لازم نیست یک خط کد بنویسی.</p>
      </div>
    </section>''' % SOFT)

# ---------------------------------------------------------------- ۰۲ تقدم یادگیری
STAGES = [
    ('A', [1], 'ورود', 'بدون این لایه هر چیز دیگری حفظ‌کردنی می‌شود. کوتاه‌ترین لایه است — چند ساعت، نه چند هفته.'),
    ('B', [2, 4, 14, 15, 3], 'به‌کارگیری و تفکر', 'بیشترین بازده همین‌جاست. ترتیب درون این لایه مهم است: ستون ۲ اول، و ستون ۳ آخر — چون تا دستت به کار نرفته باشد، تقسیم کار بین انسان و ماشین برایت انتزاعی است.'),
    ('C', [5, 6, 7], 'فهم فنی', 'اینجا مسیر دو شاخه می‌شود. اگر فقط می‌خواهی خوب استفاده کنی، سطح یک این سه ستون کافی است و می‌توانی همین‌جا بایستی.'),
    ('D', [8, 9, 10], 'ساختن', 'اختیاری، ولی یک‌طرفه: هر کس از اینجا بگذرد دیگر برای ساختن چیزی به کسی وابسته نیست.'),
    ('E', [11, 12, 13, 16], 'داوری', 'این لایه خط پایان نیست؛ خط موازی است. ستون ۱۱ از همان لایهٔ B شروع می‌شود و تا آخر ادامه دارد.'),
]
w('''
    <section id="s2" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۲ — تقدم یادگیری</p>
      <h2 style="%s">چه چیزی قبل از چه چیزی</h2>
      <p style="%s">این فلوچارت، قلب معماری است. هر لایه فقط به لایهٔ پیش از خودش تکیه می‌کند، و درون هر لایه هم ترتیب پیشنهادی مشخص است. فلش‌ها <b>تقدم</b> را نشان می‌دهند، نه اجبار: می‌توانی یک لایه را در سطح یک رد کنی و جلو بروی، ولی نمی‌توانی ردش کنی و انتظار داشته باشی لایهٔ بعد جا بیفتد.</p>
      <p style="%s">نکتهٔ مهم در این نمودار، <b>شاخهٔ موازی</b> است: لایهٔ داوری از همان ابتدا کنار بقیه می‌دود و منتظر پایان مسیر نمی‌ماند.</p>''' % (EYE, H2, LEAD, MUTE))

for i, (bk, seq, label, why) in enumerate(STAGES):
    b = BAND[bk]
    w('''      <div style="display: grid; grid-template-columns: auto 1fr; gap: 14px; align-items: stretch;">
        <div style="display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 4px 0 14px;">
          <span style="width: 34px; height: 34px; border-radius: 10px; background: %s; color: #FFFFFF; font-size: 15px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">%s</span>''' % (b['color'], b['k']))
    if i < len(STAGES) - 1:
        w('''          <span style="flex: 1; width: 2px; min-height: 26px; background: linear-gradient(to bottom, %s, #E4E1D6);"></span>''' % b['color'])
    w('''        </div>
        <div style="border: 1px solid #E4E1D6; border-inline-start: 3px solid %s; border-radius: 14px; padding: 18px 20px; margin-bottom: 14px; background: #FAFAF7;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 12px;">
            <h3 style="font-size: 16.5px; font-weight: 800; margin: 0;">%s</h3>
            <span style="font-size: 12px; color: #666158;">لایهٔ %s</span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center; margin-bottom: 14px;">''' % (b['color'], label, b['fa']))
    for j, pn in enumerate(seq):
        p = BY[pn]
        if j:
            w('''            <span style="font-size: 14px; color: #B9B3A6; flex-shrink: 0;">←</span>''')
        w('''            <a href="#p%d" style="display: inline-flex; align-items: center; gap: 7px; background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 999px; padding: 7px 13px; font-size: 13px; color: #16181C;"><span style="font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>%s</a>''' % (pn, BAND[p['band']]['color'], fa2(pn), p['fa']))
    w('''          </div>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>
      </div>''' % why)

w('''      <div style="%s padding: 22px 24px; margin-top: 10px;">
        <h3 style="font-size: 16px; font-weight: 800; margin: 0 0 10px;">پیش‌نیاز هر ستون، سر جمع</h3>
        <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0 0 16px;">همان فلوچارت بالا، این بار ستون‌به‌ستون. ستون‌هایی که پیش‌نیاز ندارند، نقطهٔ شروع ممکن‌اند.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px;">''' % CARD)
for p in P:
    pre = p['prereq']
    if pre:
        txt = 'پس از ستون ' + ' و '.join(fa2(x) for x in pre)
    else:
        txt = 'نقطهٔ شروع — بدون پیش‌نیاز'
    w('''          <div style="background: #FAFAF7; border-radius: 11px; padding: 13px 15px; border-inline-start: 3px solid %s;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 5px;">
              <span style="font-size: 13.5px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>
              <h4 style="font-size: 13.5px; font-weight: 700; margin: 0; line-height: 1.5;">%s</h4>
            </div>
            <p style="font-size: 12px; color: #666158; margin: 0;">%s</p>
          </div>''' % (BAND[p['band']]['color'], BAND[p['band']]['color'], fa2(p['n']), p['fa'], txt))
w('''        </div>
      </div>
      </div>
    </section>''')

# ---------------------------------------------------------------- ۰۳ خط زمان
TOTW = sum(ph['w'] for ph in PHASES)
w('''
    <section id="s3" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۳ — خط زمان</p>
      <h2 style="%s">دوازده هفته، اگر هفته‌ای پنج ساعت وقت بگذاری</h2>
      <p style="%s">این خط زمان یک <b>برنامهٔ پیشنهادی</b> است، نه وعده. فرضش ساده است: هفته‌ای حدود پنج ساعت، یعنی مجموعاً حدود شصت ساعت. چیزی که این برنامه را از فهرست‌های معمول جدا می‌کند، <b>خروجی قابل‌دیدن</b> در پایان هر مرحله است — اگر آن خروجی را نداشتی، مرحله تمام نشده، هر چند هفته هم گذشته باشد.</p>
      <p style="%s">عرض هر مرحله در نوار پایین، به تعداد هفته‌هایش است.</p>''' % (EYE, H2, LEAD, MUTE))

w('''      <div style="%s padding: 22px 24px; margin-bottom: 14px;">
        <div style="display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 8px;">''' % CARD)
for ph in PHASES:
    w('''          <div style="flex: %d 1 120px; min-width: 110px;">
            <div style="height: 12px; border-radius: 6px; background: %s;"></div>
            <div style="font-size: 11.5px; color: #666158; margin-top: 7px;">%s</div>
            <div style="font-size: 13.5px; font-weight: 800; color: %s; margin-top: 2px;">%s</div>
          </div>''' % (ph['w'], ph['color'], ph['label'], ph['color'], ph['fa']))
w('''        </div>
        <p style="font-size: 11.5px; color: #666158; margin: 10px 0 0;">مجموع: ۱۲ هفته · حدود ۶۰ ساعت · ۱۲ ستون از ۱۶ ستون</p>
      </div>''')

w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 14px; margin-bottom: 14px;">''')
for ph in PHASES:
    w('''        <div style="%s padding: 22px 24px; border-top: 3px solid %s;">
          <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 8px;">%s · %s هفته</div>
          <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px;">%s</h3>
          <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px;">''' % (CARD, ph['color'], ph['color'], ph['label'], fa(ph['w']), ph['fa']))
    for pn in ph['pillars']:
        w('''            <a href="#p%d" style="display: inline-flex; align-items: center; gap: 6px; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 6px 11px; font-size: 12.5px; color: #16181C;"><span style="font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>%s</a>''' % (pn, BAND[BY[pn]['band']]['color'], fa2(pn), BY[pn]['fa']))
    w('''          </div>
          <div style="background: #FAFAF7; border-radius: 11px; padding: 13px 15px;">
            <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 6px;">خروجی این مرحله</div>
            <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>
        </div>''' % ph['out'])
w('''      </div>''')

w('''      <div style="%s padding: 22px 24px; border-top: 3px solid #0D9488;">
        <div style="font-size: 11.5px; font-weight: 700; color: #0D9488; margin-bottom: 8px;">پس از هفتهٔ ۱۲ · بی‌پایان</div>
        <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px;">زمینه و داوری</h3>
        <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px;">''' % CARD)
for pn in (12, 13, 16):
    w('''          <a href="#p%d" style="display: inline-flex; align-items: center; gap: 6px; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 6px 11px; font-size: 12.5px; color: #16181C;"><span style="font-weight: 800; color: #0D9488; font-variant-numeric: tabular-nums;">%s</span>%s</a>''' % (pn, fa2(pn), BY[pn]['fa']))
w('''        </div>
        <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0; max-width: 72ch;">این سه ستون تاریخ پایان ندارند، چون موضوعشان هر فصل عوض می‌شود. برنامهٔ پیشنهادی من این است: ماهی یک بار یکی از این سه را مرور کن، نه اینکه یک بار برای همیشه بخوانی‌شان.</p>
      </div>
    </section>''')

# ---------------------------------------------------------------- ۰۴ عمق
LVL = [
    ('سطح ۱ · آشنا', '#B9B3A6', 'واژه‌ها را می‌فهمی و گفت‌وگوی دیگران را دنبال می‌کنی. نه بیشتر، و برای خیلی از ستون‌ها همین کافی است.'),
    ('سطح ۲ · کاربر', '#2F5233', 'در کار واقعی خودت به‌کارش می‌بری و می‌دانی کجا جواب می‌دهد و کجا نه.'),
    ('سطح ۳ · سازنده', '#C2410C', 'می‌توانی بسازی، بسنجی و به دیگری یاد بدهی. گران‌ترین سطح، و لازم نیست در همهٔ ستون‌ها به آن برسی.'),
]
AUD = [('مخاطب عمومی', '#0E6FB4'), ('حرفه‌ای غیرفنی', '#2F5233'), ('سازنده', '#C2410C')]
w('''
    <section id="s4" style="background: #EDF1EB; border-top: 1px solid #D5DDD2; border-bottom: 1px solid #D5DDD2; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۴ — عمق</p>
      <h2 style="%s">در هرکدام چقدر می‌توانی عمیق شوی؟</h2>
      <p style="%s">این بخش جواب نیمهٔ دوم سؤال است. برای هر ستون سه سطح تعریف شده، و مهم‌ترین حرف این صفحه همین است: <b>هیچ‌کس لازم نیست در همهٔ شانزده ستون به سطح سه برسد.</b> دانستنِ اینکه کجا باید بایستی، خودش بخشی از سواد است.</p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; margin: 22px 0;">''' % (EYE, H2, LEAD))
for name, col, desc in LVL:
    w('''        <div style="%s padding: 20px 22px; border-top: 3px solid %s;">
          <h3 style="font-size: 15.5px; font-weight: 800; margin: 0 0 10px; color: %s;">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, col, col, name, desc))
w('''      </div>''')

w('''      <div style="%s padding: 24px 26px;">
        <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 6px;">عمق پیشنهادی برای سه مخاطب</h3>
        <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0 0 8px;">هر ردیف یک ستون است و هر نوار، سطح پیشنهادی من برای یک مخاطب. نوار خالی یعنی <b>لازم نیست</b> — نه اینکه بی‌ارزش است.</p>
        <p style="font-size: 12.5px; line-height: 1.9; color: #666158; margin: 0 0 20px;">این اعداد قضاوت من‌اند، نه خروجی یک سنجه. اگر جایی با کار تو جور نیست، همان‌جا را عوض کن.</p>
        <div style="display: flex; gap: 10px 18px; flex-wrap: wrap; margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid #F0EEE7;">''' % CARD)
for name, col in AUD:
    w('''          <span style="display: inline-flex; align-items: center; gap: 7px; font-size: 12.5px; color: #45494F;"><span style="width: 11px; height: 11px; border-radius: 3px; background: %s; flex-shrink: 0;"></span>%s</span>''' % (col, name))
w('''        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 12px;">''')
for p in P:
    w('''          <div style="background: #FAFAF7; border-radius: 12px; padding: 14px 16px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 11px;">
              <span style="font-size: 13.5px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>
              <h4 style="font-size: 13.5px; font-weight: 700; margin: 0; line-height: 1.5;"><a href="#p%d" style="color: #16181C;">%s</a></h4>
            </div>''' % (BAND[p['band']]['color'], fa2(p['n']), p['n'], p['fa']))
    for (name, col), lv in zip(AUD, p['need']):
        w('''            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
              <span style="font-size: 11px; color: #666158; width: 88px; flex-shrink: 0;">%s</span>
              <span style="display: flex; gap: 3px; flex: 1;">''' % name)
        for k in (1, 2, 3):
            bg = col if k <= lv else '#E4E1D6'
            w('''<span style="height: 8px; flex: 1; border-radius: 4px; background: %s;"></span>''' % bg)
        w('''</span>
              <span style="font-size: 11px; color: #666158; width: 44px; flex-shrink: 0; text-align: left;">%s</span>
            </div>''' % ('سطح ' + fa(lv) if lv else 'لازم نیست'))
    w('''          </div>''')
w('''        </div>
      </div>
      </div>
    </section>''')

# ---------------------------------------------------------------- ۰۵ ستون‌ها
w('''
    <section id="s5" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۵ — شانزده ستون</p>
      <h2 style="%s">یکی‌یکی، با همهٔ مفهوم‌هایش</h2>
      <p style="%s">هر کارت یک ستون است: توضیح، اصلِ کلیدی‌اش، فهرست مفهوم‌هایی که زیرش می‌آید، و سه سطح عمقش. مفهوم‌ها دو بار آمده‌اند — یک بار به فارسی و یک بار در بلوک جدا به انگلیسی — چون هر دو را لازم داری: فارسی برای فهمیدن، انگلیسی برای جست‌وجو کردن.</p>
      <p style="%s">قدم بعدی این پروژه، ساختن یک صفحهٔ مستقل برای هر ستون و در ادامه برای هر مفهوم است؛ بعد هر جای این سایت که آن واژه آمده باشد، به صفحهٔ خودش پیوند می‌خورد.</p>''' % (EYE, H2, LEAD, MUTE))

for p in P:
    b = BAND[p['band']]
    pre = p['prereq']
    pretxt = ('پیش‌نیاز: ستون ' + ' و '.join(fa2(x) for x in pre)) if pre else 'بدون پیش‌نیاز'
    w('''      <div id="p%d" style="%s padding: 26px 28px; margin-bottom: 14px; border-top: 3px solid %s;">
        <div style="display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 4px;">
          <span style="font-size: 26px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums; line-height: 1;">%s</span>
          <h3 style="font-size: 21px; font-weight: 800; margin: 0; line-height: 1.45;">%s</h3>
        </div>
        <p style="font-size: 13px; color: #666158; margin: 0 0 6px; %s">%s</p>
        <div style="display: flex; gap: 8px 12px; flex-wrap: wrap; margin-bottom: 16px;">
          <span style="font-size: 11.5px; font-weight: 700; color: %s; background: %s; border-radius: 999px; padding: 5px 11px;">لایهٔ %s</span>
          <span style="font-size: 11.5px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 5px 11px;">%s</span>
          <span style="font-size: 11.5px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 5px 11px;">%s</span>
          <span style="font-size: 11.5px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 5px 11px;">%s مفهوم</span>
        </div>
        <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0 0 16px; max-width: 74ch;">%s</p>
        <div style="background: %s; border-radius: 12px; padding: 16px 18px; margin-bottom: 18px; border-inline-start: 3px solid %s;">
          <div style="font-size: 11px; font-weight: 700; color: %s; margin-bottom: 7px;">%s</div>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0; max-width: 72ch;">%s</p>
        </div>''' % (
        p['n'], CARD, b['color'], b['color'], fa2(p['n']), p['fa'], LTR, p['en'],
        b['color'], b['tint'], b['fa'], p['tag'], pretxt, fa(len(p['concepts_fa'])),
        p['lead'], b['tint'], b['color'], b['color'], p['keyk'], p['key']))

    w('''        <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 9px;">مفهوم‌های این ستون</div>
        <div style="display: flex; gap: 7px; flex-wrap: wrap; margin-bottom: 14px;">''')
    for c in p['concepts_fa']:
        w('''<span style="font-size: 12.5px; color: #16181C; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 8px; padding: 6px 11px;">%s</span>''' % c)
    w('''        </div>
        <div style="background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 12px; padding: 14px 16px; margin-bottom: 18px;">
          <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 8px;">همان مفهوم‌ها، برای جست‌وجو</div>
          <p style="font-size: 12.5px; line-height: 2; color: #45494F; margin: 0; %s">%s</p>
        </div>''' % (LTR, ' · '.join(p['terms_en'])))

    w('''        <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">سه سطح عمق در این ستون</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 10px;">''')
    for (name, col, _), txt in zip(LVL, p['depth']):
        w('''          <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px; border-top: 2px solid %s;">
            <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 7px;">%s</div>
            <p style="font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>''' % (col, col, name, txt))
    w('''        </div>
      </div>''')
w('''    </section>''')

# ---------------------------------------------------------------- ۰۶ مسیرها
w('''
    <section id="s6" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۶ — مسیرها</p>
      <h2 style="%s">من از کجا شروع کنم؟</h2>
      <p style="%s">شانزده ستون برای همه نیست؛ برای <b>همهٔ موقعیت‌ها</b> است. سه مسیر زیر، سه برش از همین نقشه‌اند — هر کدام ترتیب خودش را دارد و هیچ‌کدام ناقص نیست. برآورد ساعت‌ها قضاوت من است و با پیشینهٔ هر نفر فرق می‌کند.</p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px;">''' % (EYE, H2, LEAD))
for pa in PATHS:
    w('''        <div style="%s padding: 24px 26px; border-top: 3px solid %s;">
          <h3 style="font-size: 18px; font-weight: 800; margin: 0 0 4px;">%s</h3>
          <p style="font-size: 12.5px; color: #666158; margin: 0 0 12px; %s">%s</p>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0 0 14px;">%s</p>
          <div style="display: flex; gap: 8px 10px; flex-wrap: wrap; align-items: center; margin-bottom: 14px;">''' % (CARD, pa['color'], pa['fa'], LTR, pa['en'], pa['who']))
    for j, pn in enumerate(pa['seq']):
        if j:
            w('''            <span style="font-size: 13px; color: #B9B3A6;">←</span>''')
        w('''            <a href="#p%d" style="display: inline-flex; align-items: center; gap: 6px; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 6px 11px; font-size: 12.5px; color: #16181C;"><span style="font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>%s</a>''' % (pn, pa['color'], fa2(pn), BY[pn]['fa']))
    w('''          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px;">
            <span style="font-size: 11.5px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 5px 11px;">%s ستون</span>
            <span style="font-size: 11.5px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 5px 11px;">برآورد: %s</span>
          </div>
          <p style="font-size: 12.8px; line-height: 1.95; color: #666158; margin: 0;">%s</p>
        </div>''' % (fa(len(pa['seq'])), pa['est'], pa['note']))
w('''      </div>
      <div style="%s padding: 22px 24px; margin-top: 14px;">
        <h3 style="font-size: 16px; font-weight: 800; margin: 0 0 10px;">نمی‌دانی در کدام مسیری؟</h3>
        <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0 0 14px; max-width: 72ch;">یک آزمون سی‌سؤالی در همین سایت هست که در ده دقیقه نیمرخ شش‌بعدی سواد فعلی‌ات را رسم می‌کند. خروجی‌اش دقیقاً به همین نقشه وصل می‌شود: می‌بینی در کدام ستون‌ها از سطح پیشنهادی جلوتری و در کدام‌ها عقب.</p>
        <a href="Literacy.dc.html" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: #2F5233; padding: 11px 22px; border-radius: 10px; display: inline-block;">شروع آزمون سواد ←</a>
      </div>
      </div>
    </section>''' % SOFT)

# ---------------------------------------------------------------- ۰۷ منابع
w('''
    <section id="s7" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۷ — منابع و تشکر</p>
      <h2 style="%s">روی شانهٔ چه کسانی ایستاده‌ام</h2>
      <p style="%s">این معماری را خودم چیدم، ولی هیچ‌کدام از اجزایش را من کشف نکرده‌ام. لایه‌بندی، سطح‌های عمق و فهرست مفهوم‌ها را با چارچوب‌های موجود سنجیدم و توضیح هر ستون را با همین منابع غنی کردم. برای شفافیت، هرچه خوانده و استفاده کرده‌ام این‌جا آمده — %s منبع در %s گروه.</p>
      <p style="%s">هر مدخل دو خط دارد: خط اول فارسی، خط دوم عنوان و پدیدآور به انگلیسی و بدون ترجمه، تا بشود مستقیم جست‌وجو کرد.</p>''' % (EYE, H2, LEAD, fa(TOTAL_REF), fa(len(REFS)), MUTE))

for gi, (gname, gwhy, items) in enumerate(REFS):
    w('''      <div style="%s padding: 24px 26px; margin-bottom: 14px;">
        <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 4px;">
          <h3 style="font-size: 17px; font-weight: 800; margin: 0;">%s</h3>
          <span style="font-size: 12px; color: #666158;">%s منبع</span>
        </div>
        <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0 0 18px;">%s</p>
        <div style="display: flex; flex-direction: column; gap: 10px;">''' % (CARD, gname, fa(len(items)), gwhy))
    for ii, (f, e) in enumerate(items):
        w('''          <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px; border-inline-start: 3px solid #D9D5C9;">
            <p style="font-size: 13.5px; line-height: 1.95; color: #16181C; margin: 0 0 8px;">%s</p>
            <p style="font-size: 12px; line-height: 1.8; color: #666158; margin: 0; %s">%s</p>
          </div>''' % (f, LTR, e))
    w('''        </div>
      </div>''')

w('''      <div style="background: #EDF1EB; border: 1px solid #D5DDD2; border-radius: 16px; padding: 28px 30px; margin-bottom: 14px;">
        <h3 style="font-size: 19px; font-weight: 800; margin: 0 0 12px;">تشکر</h3>
        <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0 0 20px; max-width: 72ch;">این نقشه بدون کار کسانی که نامشان بالا آمده — و هزاران نفر که نامشان نیامده — وجود نداشت. چیزی که این حوزه را در چند سال این‌قدر جلو برد، استعداد نبود؛ <b>باز گذاشتن کار</b> بود: مقاله‌هایی که پیش از انتشار رسمی آزاد منتشر شدند، کدی که رایگان ماند، استانداردی که بدون هزینه در دسترس گذاشته شد، و معلم‌هایی که بی‌مزد توضیح دادند.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px;">''')
for t, d in THANKS_GROUPS:
    w('''          <div style="background: #FFFFFF; border-radius: 12px; padding: 18px 20px;">
            <h4 style="font-size: 14.5px; font-weight: 800; margin: 0 0 9px; line-height: 1.5;">%s</h4>
            <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>''' % (t, d))
w('''        </div>
        <p style="font-size: 13.5px; line-height: 2; color: #45494F; margin: 20px 0 0; max-width: 72ch;">اگر منبعی را جا انداخته‌ام یا جایی اشتباه نسبت داده‌ام، بگویید تا اصلاح کنم. این فهرست بسته نیست.</p>
      </div>''')

# روش و گام بعدی
w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px; margin-bottom: 20px;">
        <div style="%s padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">این معماری چطور چیده شد</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">از یک سؤال شروع شد: اگر بخواهم به یک نفر همهٔ آن چیزی را که باید دربارهٔ این فناوری بداند بگویم، فهرستش چه می‌شود؟ فهرست اول بی‌ترتیب بود. بعد هر مفهوم را به ستونی بردم که بدون آن معنا نمی‌داد، و ستون‌ها را طوری مرتب کردم که هیچ‌کدام به ستون بعد از خودش تکیه نکند.</p>
        </div>
        <div style="%s padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">چه چیزی قضاوت من است</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">لایه‌بندی، ترتیب ستون‌ها، سطح‌های عمق و همهٔ برآوردهای ساعت — همه قضاوت‌اند، نه خروجی یک سنجه. فهرست مفهوم‌ها پایدارتر است؛ ترتیب و عمق را می‌شود با کار و هدف هر نفر عوض کرد.</p>
        </div>
        <div style="%s padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">محدودیت‌هایی که می‌دانم</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">نقشه به سمت هوش مولد سنگین است، چون امروز بیشترین کاربرد همان‌جاست — ولی این یعنی رباتیک و بینایی ماشین کم‌تر از سهمشان جا دارند. ستون ۱۶ هم به‌سرعت تاریخ می‌گذرد و باید دوره‌ای بازنویسی شود.</p>
        </div>
        <div style="%s padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">گام بعدی</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">برای هر ستون یک صفحهٔ مستقل نوشته می‌شود و بعد برای مفهوم‌های اصلی هر ستون هم. بعد از آن، هر جای این سایت که یکی از این %s مفهوم آمده باشد، به صفحهٔ خودش پیوند می‌خورد — تا نقشه از یک تصویر به یک شبکهٔ قابل‌گشتن تبدیل شود.</p>
        </div>
      </div>
      <div style="display: flex; gap: 10px; flex-wrap: wrap; padding-bottom: 20px;">
        <a href="Glossary.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">واژه‌نامهٔ ۲۸۵ اصطلاح ←</a>
        <a href="Learn.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">مسیر یادگیری ماشین ←</a>
        <a href="Security.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">نقشهٔ ادبیات امنیت ←</a>
      </div>
    </section>''' % (CARD, CARD, CARD, CARD, fa(TOTAL_C)))

w('''
  </main>

  <footer style="border-top: 1px solid #E4E1D6; background: #FFFFFF;">
    <div style="max-width: 1120px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: #666158;">رضا هاشمی · معماری سواد هوش مصنوعی</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1120,"height":1400}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'AILiteracy.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars')
