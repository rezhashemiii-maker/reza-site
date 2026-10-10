# -*- coding: utf-8 -*-
import io, os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data import ACCENT, SCALE, TL, GAMES, ENGINES, LINKS, IDEAS, PREDICTIONS, REFS, METHOD
from narrative import narrative
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] for c in str(n))
def toint(s): return int(''.join(str(FAD.index(c)) for c in s))

TLS = sorted(TL, key=lambda e: toint(e['y']))
TOTAL_REF = sum(len(g[2]) for g in REFS)

CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'
SOFT = 'background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 14px;'
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
EYE = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %s; margin: 0 0 12px;' % ACCENT
H2 = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
LEAD = 'font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 10px;'
MUTE = 'font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 22px;'

o = []
w = o.append

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>شصت‌وچهار خانه — شطرنج، یادگیری ماشین و نظریهٔ بازی‌ها</title>
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
  ::selection{background:#F3E3E7;color:#8A1538}
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F5F3EE; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1120px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13.5px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <nav style="display: flex; gap: 2px; margin-inline-start: auto; flex-wrap: wrap;">
        <a href="#s1" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۱ بازی</a>
        <a href="#s2" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۲ اعداد</a>
        <a href="#s3" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۳ خط زمان</a>
        <a href="#s4" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۴ نظریهٔ بازی‌ها</a>
        <a href="#s5" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۵ سه فلسفه</a>
        <a href="#s6" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۶ ارتباط‌ها</a>
        <a href="#s7" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۷ ایده‌ها</a>
        <a href="#s8" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۸ منابع</a>
      </nav>
    </div>
  </header>

  <main>
''')

# ----------------------------------------------------------------- هیرو
w('''
    <section style="max-width: 1120px; margin: 0 auto; padding: 58px 24px 10px;">
      <p style="%s">یادداشت بلند · %s رویداد · %s ارتباط کشف‌شده · %s منبع</p>
      <h1 style="font-size: clamp(30px, 5vw, 50px); line-height: 1.38; font-weight: 800; margin: 0 0 20px; letter-spacing: -0.01em;">شصت‌وچهار خانه</h1>
      <p style="font-size: 18.5px; line-height: 1.95; color: #45494F; max-width: 64ch; margin: 0 0 18px;">در سال ۱۹۱۳، ارنست زرملو ثابت کرد <b>شطرنج یک جواب دارد</b>. نه استعاره — اثبات ریاضی. یکی از این سه جمله قطعاً درست است: سفید با بازی بی‌نقص می‌برد، سیاه با بازی بی‌نقص می‌برد، یا بازی بی‌نقص به تساوی می‌رسد.</p>
      <p style="font-size: 18.5px; line-height: 1.95; color: %s; max-width: 64ch; margin: 0 0 22px; font-weight: 700;">صد و سیزده سال گذشته و هیچ‌کس روی زمین نمی‌داند کدام یکی.</p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">این چیزی است که شطرنج را از یک بازی به یک <b>آزمایشگاه</b> تبدیل می‌کند: مسئله‌ای که می‌دانیم جواب دارد، می‌دانیم جوابش متناهی است، و با این‌حال از توان محاسباتی کل تمدن بشری بیرون است. کرونرد در ۱۹۶۵ اسمش را گذاشت «مگس سرکهٔ هوش مصنوعی» — موجودی کوچک و ساده که روی آن می‌شود چیزهای بزرگ را فهمید.</p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">این نوشته سه چیز را کنار هم می‌گذارد که معمولاً جدا خوانده می‌شوند: <b>شطرنج</b>، <b>نظریهٔ بازی‌ها</b> و <b>یادگیری ماشین</b>. ادعایم این است که اینها سه موضوع نیستند؛ یک موضوع‌اند که از سه زاویه دیده شده — و بعضی از مهم‌ترین ایده‌های یادگیری ماشین امروز، دهه‌ها قبل در این شصت‌وچهار خانه ساخته شدند و بعد اسمشان عوض شد.</p>
      <p style="font-size: 14.5px; line-height: 1.9; color: #666158; max-width: 64ch; margin: 0 0 30px;">بخش ۰۱ خودِ بازی را تعریف می‌کند — شاه، قربانی، تمپو، و اینکه چرا اسب در گوشهٔ صفحه دارد به دیوار نگاه می‌کند. بخش ۰۶ قلب این نوشته است: %s ارتباط میان شطرنج و یادگیری ماشین که بعضی‌شان هم‌ریشگی ریاضی دقیق دارند و بعضی‌شان استعاره‌اند — و در هر کارت نوشته‌ام کدام کدام است. بخش ۰۷ هم ایده‌هایی است که خودم از دل این ارتباط‌ها ساخته‌ام.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="#s1" style="font-size: 14.5px; font-weight: 700; color: #FFFFFF; background: %s; padding: 13px 26px; border-radius: 10px;">اول، خودِ بازی را تعریف کن</a>
        <a href="#s6" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">ارتباط‌های شطرنج و یادگیری ماشین ←</a>
      </div>
    </section>
''' % (EYE, fa(len(TLS)), fa(len(LINKS)), fa(TOTAL_REF), ACCENT, fa(len(LINKS)), ACCENT))

w(narrative())

# ----------------------------------------------------------------- ۰۲ اعداد
w('''
    <section id="s2" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۲ — اندازهٔ مسئله</p>
      <h2 style="%s">چرا جوابی که وجود دارد، پیدا نمی‌شود</h2>
      <p style="%s">این نمودار <b>لگاریتمی</b> است: هر واحد، ده برابر. اگر خطی رسمش می‌کردم، میلهٔ شطرنج چند میلیارد برابر عرض صفحهٔ تو می‌شد. عددِ کنار هر میله، تعداد صفرهای آن است.</p>
      <p style="%s">به فاصلهٔ دو میلهٔ چکرز و شطرنج نگاه کن: چکرز در ۲۰۰۷ حل شد، با هجده سال محاسبهٔ بی‌وقفه. شطرنج ۱۰^۲۴ برابر بزرگ‌تر است — یعنی هزار میلیارد میلیارد برابر.</p>''' % (EYE, H2, LEAD, MUTE))

w('''      <div style="%s padding: 24px 26px; margin-bottom: 14px;">''' % CARD)
for s in SCALE:
    pct = s['exp'] / 170.0 * 100
    w('''        <div style="margin-bottom: 18px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 7px;">
            <span style="font-size: 14px; font-weight: 700; color: #16181C;">%s</span>
            <span style="font-size: 11.5px; color: #666158;">%s</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="flex: 1; height: 14px; background: #F0EEE7; border-radius: 7px; overflow: hidden;">
              <div style="width: %.1f%%; height: 100%%; background: %s; border-radius: 7px;"></div>
            </div>
            <span style="font-size: 12.5px; font-weight: 700; color: %s; width: 92px; flex-shrink: 0; text-align: left; %s">10^%d</span>
          </div>
        </div>''' % (s['fa'], s['note'], pct, s['c'], s['c'], LTR, s['exp']))
w('''        <p style="font-size: 11.5px; color: #666158; margin: 4px 0 0; padding-top: 14px; border-top: 1px solid #F0EEE7;">مقیاس لگاریتمی — طول هر میله به تعداد صفرهای عدد است، نه به خود عدد.</p>
      </div>''')

NUMS = [
    ('۶۴', 'خانه', 'کل میدان بازی. از همین شصت‌وچهار خانه، فضایی بزرگ‌تر از جهان بیرون می‌آید.'),
    ('۲۰', 'حرکت در شروع', 'در اولین نوبت فقط بیست انتخاب داری. در حرکت چهلم، به‌طور متوسط حدود سی. ضربشان در هم، همهٔ ماجراست.'),
    ('۷', 'مهره', 'سقف چیزی که تا امروز کامل حل شده. برای هر وضعیت با هفت مهره یا کمتر، جواب دقیق ذخیره شده است: ۱۸.۴ ترابایت حقیقت محض. برای هشت مهره هنوز نه.'),
]
w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin-bottom: 14px;">''')
for n, lab, d in NUMS:
    w('''        <div style="%s padding: 22px 24px;">
          <div style="display: flex; align-items: baseline; gap: 9px; margin-bottom: 10px;">
            <span style="font-size: 30px; font-weight: 800; color: %s; line-height: 1;">%s</span>
            <span style="font-size: 13px; color: #666158;">%s</span>
          </div>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, ACCENT, n, lab, d))
w('''      </div>''')

w('''      <div style="background: #F3E3E7; border: 1px solid #E8CDD4; border-radius: 16px; padding: 24px 26px;">
        <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 10px;">قضیهٔ زرملو، دقیق‌تر</h3>
        <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0 0 12px; max-width: 72ch;">زرملو ثابت نکرد که سفید می‌برد. ثابت کرد که <b>سؤال جواب دارد</b>: در هر بازی متناهی، دونفره، نوبتی و با اطلاعات کامل که در آن شانس نقشی ندارد، یکی از دو بازیکن راهبردی دارد که دست‌کم نتیجهٔ مشخصی را تضمین می‌کند. یعنی شطرنج از جنس مسائل بازِ ریاضی نیست؛ از جنس مسائلی است که جوابشان نوشته شده و در صندوقی است که کلیدش را نداریم.</p>
        <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0; max-width: 72ch;">و این دقیقاً همان چیزی است که شطرنج را به آزمایشگاه بی‌نظیر یادگیری ماشین تبدیل کرد: هدف روشن است، قواعد ثابت‌اند، نتیجه بی‌ابهام است، و با این حال مسئله آن‌قدر بزرگ است که راه‌حل سرراست جواب نمی‌دهد. هر روشی که اینجا کار کند، چیزی دربارهٔ هوش گفته است.</p>
      </div>
    </section>''')

# ----------------------------------------------------------------- ۰۲ خط زمان
KIND_C = {'نظریه': '#7E22CE', 'محاسبه': '#45494F', 'شناخت': '#0E6FB4', 'سنجش': '#B4530E',
          'رویارویی': '#8A1538', 'انسان و ماشین': '#2F5233', 'حل': '#0D9488',
          'یادگیری': '#C2410C', 'هم‌راستایی': '#0E6FB4', 'تفسیرپذیری': '#7E22CE', 'فرهنگ': '#666158'}
w('''
    <section id="s3" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۳ — خط زمان</p>
      <h2 style="%s">صد و سیزده سال، در %s ایستگاه</h2>
      <p style="%s">این خط زمان را از ۱۹۱۳ شروع کرده‌ام، نه از تاریخ شطرنج. چون داستانی که می‌خواهم بگویم از لحظه‌ای شروع می‌شود که شطرنج از یک بازی به یک <b>موضوع علمی</b> تبدیل شد — و از آن لحظه تا امروز، تقریباً هر ایدهٔ بزرگ هوش مصنوعی یک بار از این صفحه رد شده است.</p>
      <p style="%s">رنگ کنار هر ایستگاه، جنس آن را نشان می‌دهد: نظریه، محاسبه، شناخت انسانی، یادگیری، یا رویارویی مستقیم.</p>''' % (EYE, H2, fa(len(TLS)), LEAD, MUTE))

w('''      <div style="display: flex; gap: 8px 14px; flex-wrap: wrap; margin-bottom: 22px; padding-bottom: 18px; border-bottom: 1px solid #F0EEE7;">''')
seen = []
for e in TLS:
    if e['k'] not in seen:
        seen.append(e['k'])
for k in seen:
    w('''        <span style="display: inline-flex; align-items: center; gap: 7px; font-size: 12px; color: #45494F;"><span style="width: 10px; height: 10px; border-radius: 50%%; background: %s; flex-shrink: 0;"></span>%s</span>''' % (KIND_C[k], k))
w('''      </div>''')

for i, e in enumerate(TLS):
    c = KIND_C[e['k']]
    w('''      <div style="display: grid; grid-template-columns: auto 1fr; gap: 16px; align-items: stretch;">
        <div style="display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 5px 0 12px; width: 12px;">
          <span style="width: 12px; height: 12px; border-radius: 50%%; background: %s; flex-shrink: 0;"></span>''' % c)
    if i < len(TLS) - 1:
        w('''          <span style="flex: 1; width: 2px; min-height: 18px; background: #EAE7DE;"></span>''')
    w('''        </div>
        <div style="padding-bottom: 20px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 4px;">
            <span style="font-size: 17px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>
            <h3 style="font-size: 15.5px; font-weight: 700; margin: 0; line-height: 1.55;">%s</h3>
            <span style="font-size: 10.5px; color: #FFFFFF; background: %s; border-radius: 999px; padding: 3px 9px;">%s</span>
          </div>
          <p style="font-size: 11.5px; color: #666158; margin: 0 0 8px; %s">%s</p>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0; max-width: 74ch;">%s</p>
        </div>
      </div>''' % (c, e['y'], e['fa'], c, e['k'], LTR, e['en'], e['note']))
w('''      </div>
    </section>''')

# ----------------------------------------------------------------- ۰۳ نظریهٔ بازی‌ها
w('''
    <section id="s4" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۴ — نظریهٔ بازی‌ها</p>
      <h2 style="%s">شطرنج، آسان‌ترین نوع بازی است</h2>
      <p style="%s">این جمله عجیب به نظر می‌رسد، ولی از نگاه نظریهٔ بازی‌ها دقیقاً درست است. بازی‌ها را با چهار محور می‌سنجند، و شطرنج در <b>هر چهار محور</b> در ساده‌ترین حالت ممکن قرار دارد: متناهی است، هیچ اطلاعاتی پنهان نیست، آنچه یکی می‌برد دیگری می‌بازد، و بازیکن‌ها نوبتی حرکت می‌کنند.</p>
      <p style="%s">و با این‌همه حل نشده. این مهم‌ترین چیزی است که نظریهٔ بازی‌ها دربارهٔ انتظارات ما از هوش مصنوعی می‌گوید.</p>''' % (EYE, H2, LEAD, MUTE))

w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 12px; margin-bottom: 14px;">''')
for g in GAMES:
    w('''        <div style="%s padding: 20px 22px; border-top: 3px solid %s;">
          <h3 style="font-size: 16.5px; font-weight: 800; margin: 0 0 3px;">%s</h3>
          <p style="font-size: 11.5px; color: #666158; margin: 0 0 14px; %s">%s</p>
          <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px;">''' % (CARD, g['c'], g['fa'], LTR, g['en']))
    for v in (g['fin'], g['info'], g['sum_'], g['turn']):
        w('''<span style="font-size: 11.5px; color: #45494F; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 5px 10px;">%s</span>''' % v)
    w('''          </div>
          <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % g['sol'])
w('''      </div>''')

w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 14px;">
        <div style="%s padding: 24px 26px; border-top: 3px solid #8A1538;">
          <div style="font-size: 11.5px; font-weight: 700; color: #8A1538; margin-bottom: 9px;">چرا بلوف در شطرنج معنا ندارد</div>
          <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">راهبرد قطعی در برابر راهبرد تصادفی</h3>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">در شطرنج حریف همه‌چیز را می‌بیند. اگر راهبرد بهینه‌ای وجود داشته باشد، <b>قطعی</b> است: همیشه همان حرکت، در همان وضعیت. پنهان‌کاری ممکن نیست، پس بلوف بی‌معناست.</p>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">در پوکر برعکس: فون نویمان ثابت کرد وقتی اطلاعات ناقص است، راهبرد بهینه <b>ناگزیر تصادفی</b> است. بلوف یک ترفند روان‌شناختی نیست؛ یک الزام ریاضی است. اگر هرگز بلوف نزنی، حریف از همین قابل‌پیش‌بینی بودن سوءاستفاده می‌کند.</p>
        </div>
        <div style="%s padding: 24px 26px; border-top: 3px solid #0D9488;">
          <div style="font-size: 11.5px; font-weight: 700; color: #0D9488; margin-bottom: 9px;">و این دقیقاً یک تصمیم مهندسی است</div>
          <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">سیاست قطعی یا سیاست تصادفی؟</h3>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">در یادگیری تقویتی همین انتخاب وجود دارد و معمولاً بدون فکر گرفته می‌شود. اگر محیط تو کسی را دارد که از رفتارت یاد می‌گیرد — رقیب، مهاجم، کاربری که سامانه را دور می‌زند — سیاست قطعی یعنی قابل‌پیش‌بینی بودن، و قابل‌پیش‌بینی بودن یعنی قابل‌سوءاستفاده بودن.</p>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">قاعدهٔ سرانگشتی‌ای که از این بیرون می‌آید: <b>هرجا محیط به تصمیم تو واکنش نشان می‌دهد، بهینه‌بودن کافی نیست؛ غیرقابل‌پیش‌بینی بودن هم بخشی از بهینگی است.</b></p>
        </div>
      </div>

      <div style="%s padding: 24px 26px;">
        <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px;">و مسئلهٔ تو، کدام ردیف است؟</h3>
        <p style="font-size: 14px; line-height: 2.05; color: #45494F; margin: 0 0 12px; max-width: 74ch;">تقریباً هر مسئلهٔ واقعی — بازار، مذاکره، قیمت‌گذاری، امنیت، سازمان — در ردیف آخر همین فهرست است: نامتناهی، با اطلاعات ناقص، غیرِحاصل‌جمع صفر، و با بازیکنانی که حتی قواعد را هم عوض می‌کنند. برای آن ردیف، «راه‌حل بهینه» وجود ندارد؛ فقط راهبرد خوب وجود دارد.</p>
        <p style="font-size: 14px; line-height: 2.05; color: #45494F; margin: 0 0 14px; max-width: 74ch;">پس وقتی کسی می‌گوید «هوش مصنوعی شطرنج را حل کرد، پس فلان مسئله را هم حل می‌کند»، جوابش این است: شطرنج حل نشده، و حتی اگر می‌شد، آسان‌ترین نوع مسئله بود.</p>
        <a href="GameTheory.dc.html" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: #2F5233; padding: 11px 22px; border-radius: 10px; display: inline-block;">نظریهٔ بازی‌ها از نگاه کسی که مدل می‌سازد ←</a>
      </div>
    </section>''' % (CARD, CARD, SOFT))

# ----------------------------------------------------------------- ۰۴ سه فلسفه
w('''
    <section id="s5" style="background: #F3E3E7; border-top: 1px solid #E8CDD4; border-bottom: 1px solid #E8CDD4; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۵ — سه فلسفه، یک بازی</p>
      <h2 style="%s">دویست میلیون، هشتاد هزار، صفر</h2>
      <p style="%s">شانون در ۱۹۵۰ دو راه پیشنهاد داد. <b>نوع A</b>: همه‌چیز را تا عمق ثابت بررسی کن. <b>نوع B</b>: هوشمندانه انتخاب کن کجا را نگاه کنی. هفتاد سال بعد، معلوم شد جواب هیچ‌کدام نیست — و در عین حال هر دو.</p>
      <p style="%s">نمودار زیر، تعداد وضعیت‌هایی است که هر موتور در یک ثانیه بررسی می‌کند. مقیاس لگاریتمی است.</p>''' % (EYE, H2, LEAD, MUTE))

mx = math.log10(200_000_000)
w('''      <div style="%s padding: 24px 26px; margin-bottom: 16px;">''' % CARD)
for e in ENGINES:
    pct = (math.log10(e['nps']) / mx * 100) if e['nps'] > 0 else 2.5
    w('''        <div style="margin-bottom: 18px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 7px;">
            <span style="font-size: 14.5px; font-weight: 700; color: #16181C;">%s</span>
            <span style="font-size: 11.5px; color: #666158; %s">%s</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="flex: 1; height: 16px; background: #F0EEE7; border-radius: 8px; overflow: hidden;">
              <div style="width: %.1f%%; height: 100%%; background: %s; border-radius: 8px;"></div>
            </div>
            <span style="font-size: 12.5px; font-weight: 700; color: %s; width: 104px; flex-shrink: 0; text-align: left;">%s</span>
          </div>
        </div>''' % (e['fa'], LTR, e['en'], pct, e['c'], e['c'], e['npsfa']))
w('''        <p style="font-size: 11.5px; line-height: 1.85; color: #666158; margin: 4px 0 0; padding-top: 14px; border-top: 1px solid #F0EEE7;">واحد: وضعیت بررسی‌شده در هر ثانیه، روی سخت‌افزار گزارش‌شدهٔ خودِ هر پروژه. مدل ۲۰۲۴ اصلاً جست‌وجو نمی‌کند، پس میله‌اش فقط نشانه است نه عدد.</p>
      </div>''')

w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 16px;">''')
for e in ENGINES:
    w('''        <div style="%s padding: 22px 24px; border-top: 3px solid %s;">
          <h3 style="font-size: 16px; font-weight: 800; margin: 0 0 3px;">%s</h3>
          <p style="font-size: 11px; color: #666158; margin: 0 0 12px; %s">%s</p>
          <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 10px;">%s</div>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0 0 12px;">%s</p>
          <div style="background: #FAFAF7; border-radius: 11px; padding: 13px 15px;">
            <p style="font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>
        </div>''' % (CARD, e['c'], e['fa'], LTR, e['en'], e['c'], e['idea'], e['how'], e['lesson']))
w('''      </div>''')

w('''      <div style="%s padding: 26px 28px;">
        <h3 style="font-size: 18px; font-weight: 800; margin: 0 0 12px;">چیزی که این سه عدد می‌گویند</h3>
        <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0 0 12px; max-width: 74ch;">در بیست‌وهفت سال، تعداد وضعیت‌هایی که ماشین نگاه می‌کند <b>هشت مرتبهٔ بزرگی کم شد</b> و قدرتش بالا رفت. این تصادف نیست و معجزه هم نیست: محاسبه حذف نشد، فقط جابه‌جا شد — از زمان اجرا به زمان آموزش.</p>
        <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0 0 12px; max-width: 74ch;">دیپ‌بلو در لحظهٔ بازی فکر می‌کرد و دانشش را انسان نوشته بود. آلفازیرو قبل از بازی فکر کرده بود و دانشش را خودش ساخته بود. مدل ۲۰۲۴ تمام فکرکردنش را در آموزش انجام داده و در بازی فقط <b>می‌بیند</b>.</p>
        <p style="font-size: 15px; line-height: 2.05; color: #16181C; margin: 0; max-width: 74ch; font-weight: 700;">قدرت به تعداد حالت‌هایی که بررسی می‌کنی نیست؛ به کیفیت بازنمایی‌ای است که با آن نگاه می‌کنی.</p>
      </div>
      </div>
    </section>''' % CARD)

# ----------------------------------------------------------------- ۰۵ ارتباط‌ها
w('''
    <section id="s6" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۶ — ارتباط‌های کشف‌شده</p>
      <h2 style="%s">%s پلی که میان شطرنج و یادگیری ماشین پیدا کردم</h2>
      <p style="%s">این بخش قلب نوشته است. هر کارت یک ارتباط است و سه قسمت دارد: <b>در شطرنج چه بود</b>، <b>در یادگیری ماشین چه نام گرفت</b>، و <b>چرا به کار امروز می‌آید</b>.</p>
      <p style="%s">صادق باشم: بعضی از این‌ها هم‌ریشگی ریاضی دقیق دارند — الو و رگرسیون لجستیک واقعاً یک فرمول‌اند. بعضی دیگر استعاره‌اند و در متنشان گفته‌ام که استعاره‌اند. این تفکیک را عمداً نگه داشته‌ام، چون قاطی‌کردنشان همان کاری است که بیشتر نوشته‌های این حوزه می‌کنند.</p>''' % (EYE, H2, fa(len(LINKS)), LEAD, MUTE))

for i, l in enumerate(LINKS):
    w('''      <div id="c%s" style="%s padding: 24px 26px; margin-bottom: 14px; border-inline-start: 4px solid %s;">
        <div style="display: flex; align-items: baseline; gap: 11px; flex-wrap: wrap; margin-bottom: 16px;">
          <span style="font-size: 13px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>
          <h3 style="font-size: 18.5px; font-weight: 800; margin: 0; line-height: 1.5;">%s</h3>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px; margin-bottom: 14px;">
          <div style="background: #FAFAF7; border-radius: 12px; padding: 16px 18px; border-top: 2px solid %s;">
            <div style="font-size: 11px; font-weight: 700; color: %s; margin-bottom: 8px;">در شطرنج</div>
            <p style="font-size: 13.3px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>
          <div style="background: #FAFAF7; border-radius: 12px; padding: 16px 18px; border-top: 2px solid #45494F;">
            <div style="font-size: 11px; font-weight: 700; color: #45494F; margin-bottom: 8px;">در یادگیری ماشین</div>
            <p style="font-size: 13.3px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>
        </div>
        <div style="background: %s; border-radius: 12px; padding: 16px 18px;">
          <div style="font-size: 11px; font-weight: 700; color: %s; margin-bottom: 8px;">چرا به کار می‌آید</div>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0; max-width: 76ch;">%s</p>
        </div>
      </div>''' % ('%02d' % (i + 1), CARD, l['c'], l['c'], fa('%02d' % (i + 1)), l['fa'], l['c'], l['c'],
                   l['chess'], l['ml'], '#F3E3E7' if l['c'] == ACCENT else '#FAFAF7', l['c'], l['so']))
w('''    </section>''')

# ----------------------------------------------------------------- ۰۶ ایده‌ها
w('''
    <section id="s7" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۷ — ایده‌پردازی</p>
      <h2 style="%s">هشت چیزی که می‌شود از این‌ها ساخت</h2>
      <p style="%s">این بخش دیگر گزارش نیست؛ <b>پیشنهاد</b> است. هیچ‌کدام از این‌ها را جایی ندیده‌ام و هیچ‌کدام هم آزموده نشده‌اند. عمداً طوری نوشته‌ام که بشود هر کدام را در یک هفته روی یک مسئلهٔ واقعی امتحان کرد — و اگر جواب نداد، معلوم شود.</p>
      <p style="%s">هر ایده سه خط دارد: چه کاری، چرا، و از کجای شطرنج آمده.</p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 14px;">''' % (EYE, H2, LEAD, MUTE))
for d in IDEAS:
    w('''        <div style="%s padding: 24px 26px; border-top: 3px solid %s;">
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 12px;">
            <span style="font-size: 13px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</span>
            <h3 style="font-size: 17px; font-weight: 800; margin: 0; line-height: 1.5;">%s</h3>
          </div>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 14px;">%s</p>
          <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px; margin-bottom: 10px;">
            <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 7px;">چرا</div>
            <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>
          <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px;">
            <div style="font-size: 11px; font-weight: 700; color: %s; margin-bottom: 7px;">قاعدهٔ شطرنجی‌اش</div>
            <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>
        </div>''' % (SOFT, d['c'], d['c'], fa('%02d' % d['n']), d['fa'], d['what'], d['why'], d['c'], d['how']))
w('''      </div>''')

w('''      <div style="%s padding: 26px 28px; margin-top: 16px;">
        <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 8px;">سه پیش‌بینی قابل‌سنجش</h3>
        <p style="font-size: 13.5px; line-height: 1.9; color: #666158; margin: 0 0 18px;">این‌ها پیش‌بینی‌اند، نه نتیجه‌گیری از داده. عمداً طوری نوشته شده‌اند که بشود بعداً غلط‌بودنشان را ثابت کرد.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">''' % CARD)
for i, p in enumerate(PREDICTIONS):
    w('''          <div style="background: #FAFAF7; border-radius: 12px; padding: 18px 20px;">
            <div style="font-size: 12px; font-weight: 700; color: %s; margin-bottom: 8px;">%s</div>
            <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
          </div>''' % (ACCENT, fa('%02d' % (i + 1)), p))
w('''        </div>
      </div>
      </div>
    </section>''')

# ----------------------------------------------------------------- ۰۷ منابع
w('''
    <section id="s8" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۸ — منابع و روش</p>
      <h2 style="%s">هر عددی که در این صفحه دیدی، از کجا آمده</h2>
      <p style="%s">%s منبع در %s گروه. هر مدخل دو خط دارد: خط اول فارسی، خط دوم عنوان و پدیدآور به انگلیسی و بدون ترجمه، تا بشود مستقیم جست‌وجو کرد.</p>''' % (EYE, H2, LEAD, fa(TOTAL_REF), fa(len(REFS))))

for gname, gwhy, items in REFS:
    w('''      <div style="%s padding: 24px 26px; margin-bottom: 14px;">
        <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 4px;">
          <h3 style="font-size: 17px; font-weight: 800; margin: 0;">%s</h3>
          <span style="font-size: 12px; color: #666158;">%s منبع</span>
        </div>
        <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0 0 18px;">%s</p>
        <div style="display: flex; flex-direction: column; gap: 10px;">''' % (CARD, gname, fa(len(items)), gwhy))
    for f, e in items:
        w('''          <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px; border-inline-start: 3px solid #D9D5C9;">
            <p style="font-size: 13.5px; line-height: 1.95; color: #16181C; margin: 0 0 8px;">%s</p>
            <p style="font-size: 12px; line-height: 1.8; color: #666158; margin: 0; %s">%s</p>
          </div>''' % (f, LTR, e))
    w('''        </div>
      </div>''')

w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px; margin-bottom: 18px;">''')
for t, d in METHOD:
    w('''        <div style="%s padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, t, d))
w('''      </div>

      <div style="background: #F3E3E7; border: 1px solid #E8CDD4; border-radius: 16px; padding: 26px 28px; margin-bottom: 18px;">
        <h3 style="font-size: 18px; font-weight: 800; margin: 0 0 12px;">تشکر</h3>
        <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0 0 12px; max-width: 74ch;">به زرملو که در ۱۹۱۳ نشان داد می‌شود دربارهٔ یک بازی قضیه ثابت کرد. به شانون که در ۱۹۵۰ راه را نشان داد و خودش هرگز برنامه‌اش را ننوشت. به دخروت و سایمون که زحمت کشیدند بفهمند در سر یک استاد چه می‌گذرد. به کاسپاروف که باخت و بعد دربارهٔ باختش فکر کرد و ایدهٔ سانتور را داد.</p>
        <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0; max-width: 74ch;">و به جامعهٔ متن‌باز شطرنج — استاک‌فیش، لیلا، لیچس، جدول‌های سیزیجی — که قوی‌ترین موتورهای تاریخ و کامل‌ترین پایگاه‌های داده را رایگان در اختیار همه گذاشتند. بدون آن‌ها نصف اعداد این صفحه قابل‌بررسی نبود.</p>
      </div>

      <div style="display: flex; gap: 10px; flex-wrap: wrap; padding-bottom: 20px;">
        <a href="GameTheory.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">نظریهٔ بازی‌ها و یادگیری ماشین ←</a>
        <a href="AILiteracy.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">معماری سواد هوش مصنوعی ←</a>
        <a href="Security.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">نقشهٔ ادبیات امنیت ←</a>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid #E4E1D6; background: #FFFFFF;">
    <div style="max-width: 1120px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: #666158;">رضا هاشمی · شطرنج، یادگیری ماشین و نظریهٔ بازی‌ها</span>
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
io.open(os.path.join(SRC, 'Chess.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars')
