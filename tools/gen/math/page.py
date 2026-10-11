# -*- coding: utf-8 -*-
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from paths import SRC  # noqa: E402
import logic as L  # noqa: E402

AC = '#1E3A5F'          # آسمان شب
SOFT = '#E3E9F1'
INK = '#16181C'
MID = '#45494F'
DIM = '#666158'
LINE = '#E4E1D6'
GREEN = '#2F5233'
RUST = '#B4530E'
SEPIA = '#6B4226'       # رنگ نامهٔ اول

CARD = 'background: #FFFFFF; border: 1px solid %s; border-radius: 16px;' % LINE
SOFTC = 'background: #FAFAF7; border: 1px solid %s; border-radius: 14px;' % LINE
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
EYE = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %s; margin: 0 0 12px;' % AC
H2 = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
H3 = 'font-size: 15.5px; font-weight: 800; margin: 0 0 10px; line-height: 1.6;'
LEAD = 'font-size: 16px; line-height: 2.05; color: %s; max-width: 68ch; margin: 0 0 14px;' % MID
BODY = 'font-size: 15.5px; line-height: 2.1; color: %s; max-width: 68ch; margin: 0 0 16px;' % MID
NOTE = 'font-size: 12px; line-height: 1.9; color: %s; margin: 10px 0 0; padding-top: 14px; border-top: 1px solid #F0EEE7;' % DIM
GRID = 'display: grid; grid-template-columns: repeat(auto-fit, minmax(%dpx, 1fr)); gap: %dpx;'

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))

o = []
w = o.append


def aside(*paras):
    """جعبهٔ «کمی بیشتر» — جوابِ چیزهایی که خواننده سرشان گیر می‌کند، بدون نوشتن پرسش."""
    body = '\n'.join(
        '        <p style="font-size: 14px; line-height: 2.05; color: %s; margin: 0 0 12px;">%s</p>' % (MID, x)
        for x in paras)
    return ('      <div style="background: #FFFFFF; border: 1px dashed #C9D3DE; border-radius: 14px; '
            'padding: 20px 22px; margin: 0 0 18px; max-width: 72ch;">\n'
            '        <div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: %s; '
            'margin-bottom: 11px;">کمی بیشتر</div>\n%s\n      </div>' % (AC, body))


def era(tag, text):
    """نشانهٔ «چند سال بعد از تو»."""
    return ('      <div style="display: inline-flex; align-items: baseline; gap: 10px; background: %s; '
            'border-radius: 999px; padding: 7px 16px; margin: 0 0 16px;">'
            '<span style="font-size: 12px; font-weight: 800; color: %s;">%s</span>'
            '<span style="font-size: 12.5px; color: %s;">%s</span></div>' % (SOFT, AC, tag, MID, text))


NAV = [('s1', '۰۱ شمردن'), ('s2', '۰۲ روش'), ('s3', '۰۳ شمارِ راه‌ها'), ('s4', '۰۴ بخت'),
       ('s5', '۰۵ اعداد بزرگ'), ('s6', '۰۶ باور'), ('s7', '۰۷ بهترین خط'), ('s8', '۰۸ سراشیبی'),
       ('s9', '۰۹ بازگشت'), ('s10', '۱۰ خبر'), ('s11', '۱۱ یادگیری'), ('s12', '۱۲ همه با هم'),
       ('s13', '۱۳ ترجمه'), ('s14', '۱۴ روش')]

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>نامهٔ دوم به ابوریحان — ریاضیاتِ حدس زدن</title>
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
  a{color:#1E3A5F;text-decoration:none}
  a:hover{opacity:.82}
  button{font-family:inherit;cursor:pointer;border:none}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:92px}
  ::selection{background:#E3E9F1;color:#1E3A5F}
  @media (max-width:860px){
    nav[data-sections]{display:none !important}
    div[data-sectionlist]{display:flex !important}
  }
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F5F3EE; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1060px; margin: 0 auto; padding: 12px 24px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <a href="Logic.dc.html" style="font-size: 12.5px; font-weight: 700; color: #6B4226;">نامهٔ اول ←</a>
      <nav data-sections="1" style="display: flex; gap: 1px; margin-inline-start: auto; flex-wrap: wrap;">''')
for sid, lab in NAV:
    w('''        <a href="#%s" style="font-size: 11.5px; color: #45494F; padding: 5px 8px; border-radius: 999px;">%s</a>''' % (sid, lab))
w('''      </nav>
    </div>
  </header>

  <main>
''')

# ------------------------------------------------------------------ هیرو
w('''
    <section style="max-width: 1060px; margin: 0 auto; padding: 56px 24px 10px;">
      <p style="%s">مبانی ریاضی و آماری هوش مصنوعی، با ابزار هزار سال پیش</p>
      <h1 style="font-size: clamp(30px, 5vw, 50px); line-height: 1.38; font-weight: 800; margin: 0 0 22px; letter-spacing: -0.01em;">نامهٔ دوم به ابوریحان</h1>
      <p style="font-size: 19px; line-height: 2; color: %s; max-width: 62ch; margin: 0 0 18px;">در <a href="Logic.dc.html" style="font-weight: 700;">نامهٔ اول</a> گفتم ماشین چیست و چطور فرمان می‌گیرد. آن ماشین چیزی نمی‌فهمید و فقط اطاعت می‌کرد. این نامه دربارهٔ چیز دیگری است: <b>چطور همان ماشینِ نفهم می‌تواند حدس بزند.</b></p>
      <p style="%s">و جواب، بر خلاف آنچه به نظر می‌رسد، در فلسفه نیست؛ در <b>ریاضیات</b> است. دقیق‌تر: در شمردن، در اندازه‌گیریِ بخت، و در یک قاعدهٔ ساده برای عوض‌کردن باور وقتی خبر تازه‌ای می‌رسد.</p>
      <p style="%s">باز هم قاعده همان است: هیچ واژه‌ای که تو نشناسی اجازهٔ ورود ندارد. ولی این بار یک تفاوت هست — بخشی از این ریاضیات <b>پیش از تو</b> ساخته شده و تو نامِ سازندگانش را می‌شناسی. بقیه‌اش در نهصد سال بعد از تو ساخته می‌شود، و من هر بار می‌گویم چند سال بعد.</p>
      <p style="%s">یک چیز را هم از همین اول بگویم تا در راه گم نشویم: <b>همهٔ آنچه امروز «هوش مصنوعی» می‌نامند، روی چهار کار استوار است</b> — شمردن، برازشِ یک الگو بر شمارش‌ها، سُر خوردن به سمت کم‌ترین خطا، و به‌روز کردن باور با خبر تازه. هر چهارتا در این نامه می‌آید. هیچ کدام جادو نیست.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 28px;">
        <a href="#s1" style="font-size: 14.5px; font-weight: 700; color: #FFFFFF; background: %s; padding: 13px 26px; border-radius: 10px;">شروع نامه</a>
        <a href="#s8" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">خودت خط را جا بینداز ←</a>
        <a href="#s12" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">خط زمان ←</a>
      </div>
    </section>
''' % (EYE, MID, BODY, BODY, BODY, AC))

STATS = [('۴', 'کارِ پایه که همهٔ هوش مصنوعی روی آن ایستاده'),
         ('۱۱۰۰', 'سال، از الکندی تا امروز'),
         ('۱۲', 'دانشمند، هر کدام با تاریخ و منبع'),
         ('۱', 'خط که خودت جا می‌اندازی و بعد ماشین')]
w('''    <section style="max-width: 1060px; margin: 0 auto; padding: 26px 24px 10px;">
      <div style="%s">''' % (GRID % (190, 12)))
for v, lab in STATS:
    w('''        <div style="%s padding: 20px 22px;">
          <div style="font-size: 30px; font-weight: 800; color: %s; line-height: 1;">%s</div>
          <div style="font-size: 12.5px; line-height: 1.8; color: %s; margin-top: 8px;">%s</div>
        </div>''' % (CARD, AC, v, DIM, lab))
w('''      </div>
    </section>

    <section style="max-width: 1060px; margin: 0 auto; padding: 18px 24px 0;">
      <div data-sectionlist="1" style="display: none; flex-wrap: wrap; gap: 7px; %s padding: 18px 20px;">
        <div style="width: 100%%; font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 4px;">فهرست بخش‌ها</div>''' % (CARD, DIM))
for sid, lab in NAV:
    w('''        <a href="#%s" style="font-size: 12.5px; color: #45494F; background: #FAFAF7; border: 1px solid #EDEAE1; border-radius: 999px; padding: 7px 12px;">%s</a>''' % (sid, lab))
w('''      </div>
    </section>''')

# ------------------------------------------------------------------ ۰۱ شمردن (الکندی)
FREQ = [('ا', 100), ('ل', 82), ('ی', 70), ('م', 58), ('ن', 52), ('و', 46),
        ('ر', 38), ('ب', 30), ('ه', 26), ('ت', 22), ('س', 16), ('ک', 12),
        ('ژ', 3), ('ذ', 2), ('ث', 2)]
bars = []
for i, (ch, v) in enumerate(FREQ):
    x = 668 - i * 44
    h = v / 100.0 * 150
    col = AC if i < 6 else (DIM if i < 12 else RUST)
    bars += ['          <rect x="%d" y="%.1f" width="30" height="%.1f" rx="4" fill="%s"/>'
             % (x, 196 - h, h, col),
             '          <text x="%d" y="%d" font-size="13" fill="%s" font-weight="700" text-anchor="middle">%s</text>'
             % (x + 15, 216, INK, ch)]
bars += ['          <text x="600" y="24" font-size="12.5" fill="%s" font-weight="700" text-anchor="middle" direction="rtl">پرتکرارها</text>' % AC,
         '          <text x="130" y="24" font-size="12.5" fill="%s" font-weight="700" text-anchor="middle" direction="rtl">کم‌تکرارها</text>' % RUST,
         '          <text x="360" y="244" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">نسبت تقریبی حرف‌ها در یک متن فارسیِ بلند — نمایشی، برای نشان‌دادن شکل توزیع</text>' % DIM]
svg1 = ('0 0 720 256', '\n'.join(bars))

w('''
    <section id="s1" style="max-width: 1060px; margin: 0 auto; padding: 48px 24px 10px;">
      <p style="%s">۰۱ — شمردن</p>
      <h2 style="%s">نخستین باری که کسی از شمردن، چیزی پنهان را بیرون کشید</h2>
%s
      <p style="%s">ابوریحان، از جایی شروع می‌کنم که تو خودت می‌شناسی‌اش. <b>ابویوسف یعقوب بن اسحاق الکِندی</b> رساله‌ای دارد دربارهٔ گشودن نامه‌های رمزی. تا جایی که می‌دانیم، این کهن‌ترین متنی است که در آن کسی روشی برای شکستن رمز نوشته — و روشش چیزی جز <b>شمردن</b> نیست.</p>
      <p style="%s">فرض کن کسی نامه‌ای نوشته و در آن هر حرف را با نشانهٔ دیگری عوض کرده: هر جا «الف» بوده، «ج» گذاشته؛ هر جا «ل» بوده، «ط». نامه خوانا نیست. کلیدش را هم نداری.</p>
      <p style="%s">الکندی گفت: لازم نیست کلید داشته باشی. <b>بشمار.</b> در هر زبانی بعضی حرف‌ها بسیار پرتکرارند و بعضی بسیار کمیاب. در یک متن بلند، این نسبت‌ها تقریباً ثابت می‌مانند. پس پرتکرارترین نشانهٔ نامهٔ رمزی، به احتمال زیاد همان پرتکرارترین حرف آن زبان است.</p>''' % (
    EYE, H2, era('۲۰۰ سال پیش از تو', 'الکِندی (۸۰۱–۸۷۳) · رساله‌اش حدود سال ۸۵۰'), LEAD, BODY, BODY))
w('      <figure style="margin: 0 0 18px; %s padding: 20px 18px;">\n'
  '        <svg viewBox="%s" role="img" aria-label="%s" style="width: 100%%; max-width: 100%%; height: auto; display: block; font-family: inherit;">\n%s\n        </svg>\n'
  '        <figcaption style="font-size: 12.5px; line-height: 1.9; color: %s; margin-top: 14px; text-align: center;">%s</figcaption>\n'
  '      </figure>' % (SOFTC, svg1[0],
                      'نمودار میله‌ای نسبت تکرار حرف‌ها در یک متن فارسی، از پرتکرار تا کمیاب',
                      svg1[1], DIM,
                      'شکل این نمودار، همان چیزی است که رمز را می‌شکند. اگر در نامهٔ رمزی هم چنین شکلی ببینی، بلندترین میلهٔ آن‌جا با بلندترین میلهٔ این‌جا یکی است.'))
w(aside(
  'اگر هیچ‌وقت با رمز کار نکرده‌ای: «رمز» در ساده‌ترین شکلش یعنی یک جدول جایگزینی. برای هر حرف الفبا، نشانهٔ دیگری انتخاب می‌کنی و همه‌جا به‌جایش همان را می‌گذاری. گیرنده جدول را دارد و برمی‌گرداند؛ کسی که ندارد، چیزی جز حروف بی‌معنا نمی‌بیند.',
  'و اینکه چرا شمردن کار می‌کند: چون نسبت حرف‌ها خاصیتِ <b>زبان</b> است، نه خاصیتِ یک نامهٔ بخصوص. هر کسی هر چه بنویسد، باز هم «الف» و «ل» بیشتر از «ژ» و «ث» به کار می‌روند. جایگزینی، حرف‌ها را عوض می‌کند ولی <b>نسبت‌ها را دست‌نخورده می‌گذارد</b> — و همین، راهِ ورود است.'))
w(aside(
  'یک نکتهٔ ظریف که بعدها <b>ابن عَدلان</b> رویش انگشت گذاشت: این روش روی متن کوتاه کار نمی‌کند. اگر نامه فقط ده کلمه باشد، ممکن است اتفاقی «ژ» سه بار آمده باشد و «الف» یک بار.',
  'این همان چیزی است که امروز به آن «کم‌بودن نمونه» می‌گویند و یکی از دو سه خطای کشندهٔ کل این حرفه است. نسبت‌ها وقتی قابل اعتمادند که از <b>شمار زیادی</b> مشاهده آمده باشند. در بخش ۰۵ می‌بینی این «زیاد» یعنی چه و کجا باز هم نجاتت نمی‌دهد.'))
w('''      <p style="%s">حالا بگذار بگویم چرا این رساله برای نامهٔ من این‌قدر مهم است. الکندی کاری کرد که پیش از او کسی نکرده بود: <b>از شمارشِ چیزهای دیدنی، به چیزی نادیدنی رسید.</b> او جدول رمز را ندید؛ آن را از روی عددها <i>حدس زد</i>.</p>
      <p style="%s">هر چیزی که امروز «هوش مصنوعی» می‌نامند، در ته ماجرا همین کار را می‌کند — فقط با شمارش‌های بسیار بزرگ‌تر و حدس‌های بسیار پیچیده‌تر. ماشینی که حدس می‌زند کلمهٔ بعدی چه خواهد بود، دارد دقیقاً همان کاری را می‌کند که الکندی با حرف‌ها کرد.</p>
      <div style="%s padding: 22px 24px; border-inline-start: 4px solid %s;">
        <p style="font-size: 16px; line-height: 2.05; color: %s; margin: 0;">پس تاریخ هوش مصنوعی از ماشین شروع نمی‌شود. از <b>شمردن</b> شروع می‌شود — و آن، هزار و دویست سال پیش در بغداد اتفاق افتاد.</p>
      </div>
    </section>''' % (BODY, BODY, SOFTC, AC, INK))

# ------------------------------------------------------------------ ۰۲ روش (خوارزمی)
w('''
    <section id="s2" style="background: #FFFFFF; border-top: 1px solid %s; border-bottom: 1px solid %s; margin-top: 44px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
      <p style="%s">۰۲ — روش</p>
      <h2 style="%s">هم‌ولایتیِ تو که نامش روی کل این حرفه ماند</h2>
%s
      <p style="%s"><b>محمد بن موسی خوارزمی</b> در بیت‌الحکمهٔ بغداد کاری کرد که در نگاه اول کوچک به نظر می‌رسد: به‌جای حل کردن یک مسئله، <b>روشی نوشت که هر مسئله‌ای از آن دسته را حل می‌کند.</b></p>
      <p style="%s">تفاوت را ببین. اگر بگویم «مالی داشتم، ثلثش را دادم، ده دینار ماند؛ چقدر بود؟» و من جوابش را پیدا کنم، یک مسئله حل شده. ولی اگر قاعده‌ای بنویسم که برای <i>هر</i> عددی در جای ثلث و ده کار کند، چیز دیگری ساخته‌ام: چیزی که دیگر به هوش من احتیاج ندارد. هر کسی می‌تواند آن را دنبال کند، حتی اگر نفهمد چرا کار می‌کند.</p>''' % (
    LINE, LINE, EYE, H2,
    era('۲۰۰ سال پیش از تو', 'خوارزمی (حدود ۷۸۰–۸۵۰) · اهل خوارزم، مثل تو'), LEAD, BODY))
w(aside(
  'و اگر «جبر» برایت واژهٔ آشنایی نیست — که برای خوانندهٔ امروزی هم اغلب نیست — در ساده‌ترین بیان یعنی: پیدا کردن چیزی که نمی‌دانی، از روی چیزهایی که می‌دانی، با دنبال کردن چند قاعدهٔ ثابت.',
  'نام کتاب خوارزمی «الجبر و المقابله» بود. «جبر» یعنی سر جای خودش برگرداندن — وقتی چیزی از یک طرف تساوی کم شده، همان‌قدر را به طرف دیگر هم می‌افزایی تا تعادل برگردد. واژهٔ امروزی «algebra» از همین «الجبر» آمده است.'))
w('''      <p style="%s">و حالا آن چیزی که به تو مربوط می‌شود: نام او، وقتی کتابش قرن‌ها بعد به لاتین ترجمه شد، به صورت <b>Algoritmi</b> نوشته شد. آن واژه ماند، معنایش عوض شد، و امروز به هر «روشِ مشخصِ انجام یک کار در گام‌های معلوم» می‌گویند <b>الگوریتم</b>.</p>
      <p style="%s">پس وقتی امروز کسی از «الگوریتمِ فلان شبکهٔ اجتماعی» حرف می‌زند، بی‌آنکه بداند دارد نام یک هم‌ولایتیِ تو را تکرار می‌کند.</p>
      <p style="%s">چرا این مهم‌ترین قدم بود؟ چون پل میان نامهٔ اول و نامهٔ دوم است. آن ماشینِ نفهمِ نامهٔ اول فقط وقتی به درد می‌خورد که روشی داشته باشی که بشود بی‌فهم دنبالش کرد. <b>خوارزمی آن جور فکر کردن را اختراع کرد؛ هزار سال بعد کسی ماشینی ساخت که بتواند دنبالش کند.</b></p>
      </div>
    </section>''' % (BODY, BODY, BODY))

# ------------------------------------------------------------------ ۰۳ شمارِ راه‌ها
tri = []
ROWS = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
for r, row in enumerate(ROWS):
    y = 34 + r * 38
    for c, v in enumerate(row):
        x = 360 + (c - (len(row) - 1) / 2.0) * 58
        hot = (r == 3 and c in (1, 2))
        tri += ['          <circle cx="%.1f" cy="%d" r="15" fill="%s" stroke="%s" stroke-width="1.5"/>'
                % (x, y, SOFT if hot else '#FFFFFF', AC if hot else LINE),
                '          <text x="%.1f" y="%d" font-size="12.5" fill="%s" font-weight="%s" text-anchor="middle">%s</text>'
                % (x, y + 4, AC if hot else INK, '800' if hot else '600', fa(v))]
    tri += ['          <text x="648" y="%d" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">%s چیز</text>'
            % (y + 4, DIM, fa(r))]
tri += ['          <text x="360" y="272" font-size="12" fill="%s" text-anchor="middle" direction="rtl">در ردیف «۳ چیز»، عدد ۳ یعنی: برای برداشتن ۱ تا از ۳ تا، سه راه هست</text>' % AC]
svg3 = ('0 0 720 286', '\n'.join(tri))

w('''
    <section id="s3" style="max-width: 1060px; margin: 0 auto; padding: 48px 24px 10px;">
      <p style="%s">۰۳ — شمارِ راه‌ها</p>
      <h2 style="%s">پیش از آنکه بشود بخت را اندازه گرفت، باید راه‌ها را شمرد</h2>
%s
      <p style="%s">این یکی عجیب‌ترین بخش نامه است، چون دربارهٔ <b>همین حالا</b>ی توست. در بغداد مردی هست به نام <b>ابوبکر الکَرَجی</b> که جدولی از عددها ساخته. خودِ نوشته‌اش به دست ما نرسیده؛ آنچه داریم از نقل‌قول‌های <b>السموأل</b> است که بعد از او آمد.</p>
      <p style="%s">جدول ساده است: هر عدد، جمعِ دو عددِ بالای خودش است. ولی آنچه می‌شمارد اصلاً ساده نیست — این جدول جواب این پرسش را می‌دهد که <b>از میان n چیز، چند راه برای برداشتن k تا هست.</b></p>''' % (
    EYE, H2, era('در زمان خودِ تو', 'الکَرَجی (حدود ۹۵۳–۱۰۲۹) · جدولش حدود سال ۱۰۰۰'), LEAD, BODY))
w('      <figure style="margin: 0 0 18px; %s padding: 20px 18px;">\n'
  '        <svg viewBox="%s" role="img" aria-label="%s" style="width: 100%%; max-width: 100%%; height: auto; display: block; font-family: inherit;">\n%s\n        </svg>\n'
  '        <figcaption style="font-size: 12.5px; line-height: 1.9; color: %s; margin-top: 14px; text-align: center;">%s</figcaption>\n'
  '      </figure>' % (SOFTC, svg3[0], 'مثلث عددی که هر عدد جمع دو عدد بالای خودش است، تا شش ردیف',
                      svg3[1], DIM,
                      'هر ردیف، همهٔ راه‌های برداشتن از آن تعداد چیز را می‌شمارد. ردیف چهارم: یک راه برای برنداشتن، سه راه برای یکی، سه راه برای دوتا، یک راه برای هر سه.'))
w(aside(
  'بیایید یک بار با دست بشماریم تا عددها از آسمان نیفتند. سه کوزه داری: الف، ب، ج. می‌خواهی یکی برداری. سه راه هست: الف، یا ب، یا ج.',
  'حالا می‌خواهی دو تا برداری. باز هم سه راه: الف‌وب، الف‌وج، ب‌وج. (الف‌وب با ب‌والف یکی است، چون ترتیب مهم نیست.) هر سه را برداری؟ یک راه. هیچ‌کدام را؟ باز یک راه.',
  'پس برای سه چیز: ۱، ۳، ۳، ۱. دقیقاً همان ردیف چهارم جدول. جدول فقط این شمارش دستی را برای هر عددی انجام می‌دهد، بی‌آنکه مجبور باشی تک‌تک بنویسی.'))
w('''      <p style="%s">و حالا چرا این برای نامهٔ من حیاتی است. اگر بخواهی بگویی «بخت این پیشامد چقدر است»، تنها راهش این است که <b>راه‌های ممکن را بشماری</b> و ببینی چند تایشان آن چیزی است که می‌خواهی. بدون شمردن راه‌ها، بخت عددی ندارد.</p>''' % BODY)
w(aside(
  'مثال کوچکی که همه‌چیز را روشن می‌کند. سه سکه می‌اندازی. چند حالت ممکن است؟ هر سکه دو حالت دارد، پس دو در دو در دو، یعنی هشت حالت. (همان دوبرابرشدنِ نخ‌های بافنده در نامهٔ اول.)',
  'حالا چند تا از این هشت حالت دقیقاً یک «شیر» دارد؟ سه تا — چون از سه سکه باید یکی را انتخاب کنی که شیر باشد، و دیدیم که سه راه دارد.',
  'پس بخت اینکه دقیقاً یک شیر بیاید، سه از هشت است. <b>همین، تعریف احتمال است</b>: شمار راه‌های دلخواه، تقسیم بر شمار همهٔ راه‌ها. چیزی بیشتر از این نیست — و تا راه‌ها را نشماری، این کسر وجود ندارد.'))
w('''      <p style="%s">و یک چیز دیگر که دلم می‌خواهد بدانی، هرچند نخواهی دید: <b>در همان سالی که تو از دنیا می‌روی، کودکی به دنیا می‌آید</b> که همین جدول را دوباره می‌سازد و پیش می‌برد. نامش <b>عمر خیام</b> است و مرگ و تولدتان هر دو در سال ۴۲۷ هجری است. امروز به آن جدول، هم «مثلث کرجی» می‌گویند و هم «مثلث خیام».</p>
      <p style="%s">این جدول از شرق به غرب می‌رود و قرن‌ها بعد در اروپا به نام کس دیگری شناخته می‌شود. ولی ریشه‌اش این‌جاست، در همین سال‌هایی که تو زنده‌ای.</p>
    </section>''' % (BODY, BODY))

# ------------------------------------------------------------------ ۰۴ بخت
w('''
    <section id="s4" style="background: #FFFFFF; border-top: 1px solid %s; border-bottom: 1px solid %s; margin-top: 44px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
      <p style="%s">۰۴ — بخت</p>
      <h2 style="%s">روزی که «بخت» از یک حرف، به یک عدد تبدیل شد</h2>
%s
      <p style="%s">ششصد سال بعد از تو، در فرانسه، قماربازی مسئله‌ای را پیش دو ریاضی‌دان می‌برد. مسئله این است: دو نفر بازی می‌کنند و هر کس زودتر به امتیاز معین برسد، تمام شرط‌بندی را می‌برد. ولی بازی نیمه‌کاره قطع می‌شود. <b>پول را چطور تقسیم کنند؟</b></p>
      <p style="%s">به نظر پرسش کوچکی می‌آید. نیست. تا پیش از آن، «بخت» چیزی بود که دربارهٔ آن حرف می‌زدند؛ بعد از آن، چیزی شد که <b>حساب می‌کردند</b>. <b>بلز پاسکال</b> و <b>پی‌یر دو فرما</b> در نامه‌نگاری تابستان و پاییز ۱۶۵۴ جوابش را پیدا کردند، و همان نامه‌ها را امروز نقطهٔ آغاز نظریهٔ احتمال می‌دانند.</p>''' % (
    LINE, LINE, EYE, H2, era('۶۰۰ سال بعد از تو', 'پاسکال و فرما · نامه‌نگاری سال ۱۶۵۴'), LEAD, BODY))
w(aside(
  'جوابشان این بود: پول را بر اساس آنچه <i>تا حالا</i> شده تقسیم نکن؛ بر اساس <b>آنچه از این به بعد می‌توانست بشود</b> تقسیم کن.',
  'یعنی همهٔ راه‌هایی را که بازی می‌توانست ادامه پیدا کند بشمار (همان جدول بخش ۰۳)، ببین در چند تایشان نفر اول می‌برد و در چند تا نفر دوم، و پول را به همان نسبت تقسیم کن.',
  'این یک جهش فکری بزرگ است: <b>آینده‌ای که هرگز اتفاق نیفتاد، باز هم قابل شمردن است.</b> هر پیش‌بینی‌ای که امروز هر ماشینی می‌کند، روی همین فرض ایستاده.'))
w('''      <p style="%s">و از دل همین کار، مفهومی بیرون آمد که ستون فقرات همهٔ تصمیم‌گیری‌های امروز است: <b>امید ریاضی</b>. یعنی اگر کاری را هزار بار تکرار کنی، به‌طور متوسط چه عایدت می‌شود.</p>''' % BODY)
w(aside(
  'با عدد روشن‌تر می‌شود. فرض کن قماری هست که با بختِ یک‌دهم، صد دینار می‌دهد، و با بختِ نه‌دهم، هیچ.',
  'امید ریاضی‌اش این است: یک‌دهمِ صد، به‌علاوهٔ نه‌دهمِ صفر — یعنی ده دینار. پس اگر بیش از ده دینار برای ورود بدهی، در درازمدت ضرر می‌کنی؛ کمتر بدهی، سود.',
  'دقت کن این عدد در <b>هیچ یک</b> از دفعات واقعی اتفاق نمی‌افتد: یا صد می‌گیری یا هیچ، هیچ‌وقت ده. «ده» میانگینِ درازمدت است، نه پیش‌گوییِ دفعهٔ بعد. این تفاوت، جایی است که بیشترین سوءتفاهم‌ها دربارهٔ پیش‌بینی ماشینی از آن می‌آید.'))
w('''      <p style="%s">و اینکه چرا این همه با قمار شروع شد، دلیل ساده‌ای دارد: قمار تنها جایی بود که <b>همهٔ راه‌های ممکن را می‌شد روی کاغذ نوشت</b>. دنیا بیرون از میز قمار آن‌قدر راه دارد که شمردنشان ممکن نیست. ریاضیات همیشه از جایی شروع می‌کند که بشود شمرد، و بعد بیرون می‌زند.</p>
      </div>
    </section>''' % BODY)

# ------------------------------------------------------------------ ۰۵ قانون اعداد بزرگ
lln = []
import random as _r
_r.seed(7)
pts = []
run = 0
for i in range(1, 121):
    run += 1 if _r.random() < 0.5 else 0
    pts.append((i, run / float(i)))
# نسبت صفر تا یک روی نوار ۴۴..۱۶۴ می‌نشیند، پس «نیم» دقیقاً روی ۱۰۴ می‌افتد.
# در نگارش قبلی خط‌چینِ «نیم» روی ۱۰۰ بود ولی منحنی با مقیاس دیگری کشیده می‌شد:
# نمودار به خط‌چین نمی‌رسید و درست خلافِ حرفِ همین بخش را نشان می‌داد.
def _ly(v):
    return 164 - v * 120
path = ' '.join('%.1f,%.1f' % (70 + (i - 1) / 119.0 * 600, _ly(v)) for i, v in pts)
lln += ['          <line x1="70" y1="104" x2="670" y2="104" stroke="%s" stroke-width="1.5" stroke-dasharray="6 4"/>' % AC,
        '          <text x="678" y="108" font-size="11.5" fill="%s" text-anchor="start" direction="rtl">نیم</text>' % AC,
        '          <polyline points="%s" fill="none" stroke="%s" stroke-width="2"/>' % (path, RUST),
        '          <text x="120" y="182" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">۱۰ پرتاب</text>' % DIM,
        '          <text x="620" y="182" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">۱۲۰ پرتاب</text>' % DIM,
        '          <text x="360" y="26" font-size="12.5" fill="%s" text-anchor="middle" direction="rtl" font-weight="700">نسبت «شیر» در پرتاب‌های پیاپی یک سکهٔ سالم</text>' % INK,
        '          <text x="360" y="202" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">اول بالا و پایین می‌پرد؛ هرچه جلوتر، به نیم نزدیک‌تر و آرام‌تر</text>' % DIM]
svg5 = ('0 0 720 214', '\n'.join(lln))

w('''
    <section id="s5" style="max-width: 1060px; margin: 0 auto; padding: 48px 24px 10px;">
      <p style="%s">۰۵ — اعداد بزرگ</p>
      <h2 style="%s">چرا شمردنِ بیشتر، حدس را بهتر می‌کند — و کجا نمی‌کند</h2>
%s
      <p style="%s">الکندی در بخش ۰۱ فرض کرده بود که نسبت حرف‌ها در متن بلند «تقریباً ثابت» است. حدسِ خوبی بود، ولی اثبات نداشت. هفتصد سال بعد، <b>یاکوب برنولی</b> آن را ثابت کرد.</p>
      <p style="%s">کتابش «هنر حدس زدن» بعد از مرگش منتشر شد و در آن چیزی هست که امروز <b>قانون اعداد بزرگ</b> می‌نامندش. حرفش این است: هرچه بیشتر مشاهده کنی، نسبتی که می‌بینی به نسبتِ واقعی نزدیک‌تر می‌شود — و می‌شود دقیقاً گفت چقدر نزدیک.</p>''' % (
    EYE, H2, era('۷۰۰ سال بعد از تو', 'یاکوب برنولی · «Ars Conjectandi»، منتشرشده در ۱۷۱۳'), LEAD, BODY))
w('      <figure style="margin: 0 0 18px; %s padding: 20px 18px;">\n'
  '        <svg viewBox="%s" role="img" aria-label="%s" style="width: 100%%; max-width: 100%%; height: auto; display: block; font-family: inherit;">\n%s\n        </svg>\n'
  '        <figcaption style="font-size: 12.5px; line-height: 1.9; color: %s; margin-top: 14px; text-align: center;">%s</figcaption>\n'
  '      </figure>' % (SOFTC, svg5[0], 'نمودار نسبت شیر در پرتاب‌های پیاپی سکه که به تدریج به نیم نزدیک می‌شود',
                      svg5[1], DIM,
                      'این همان قانون است، به چشم. نوسان‌های اول بزرگ‌اند و بعد کوچک می‌شوند — ولی هیچ‌وقت دقیقاً صفر نمی‌شوند.'))
w(aside(
  'یک سوءتفاهم رایج را همین‌جا ببندم، چون قدیمی است و هنوز زنده: این قانون نمی‌گوید اگر ده بار پشت سر هم «خط» آمد، حالا «شیر» <i>بدهکار</i> است.',
  'سکه حافظه ندارد. پرتاب بعدی باز هم نیم-نیم است. چیزی که اتفاق می‌افتد این است که آن ده تای ناهموار، در میان هزار پرتاب بعدی <b>رقیق</b> می‌شود، نه اینکه جبران شود.',
  'به همین دلیل در نمودار بالا خط به نیم نزدیک می‌شود ولی هیچ‌وقت نمی‌پرد تا «جبران» کند.'))
w(aside(
  'و حالا مهم‌ترین هشدار این کل نامه، که اگر فقط یک جمله از این بخش یادت بماند باید این باشد: <b>شمارِ بیشتر، فقط بی‌نظمی را درمان می‌کند؛ کجیِ نمونه را نه.</b>',
  'اگر بخواهی بدانی مردم این شهر چه می‌خورند و فقط از کسانی بپرسی که در بازار بزرگ‌اند، هزار جوابِ هم‌سو هم تو را به جواب درست نمی‌رساند. فقط مطمئن‌تر می‌شوی که <i>چیز غلط</i> را درست شمرده‌ای.',
  'هر مشکلی که امروز دربارهٔ «سوگیری» ماشین‌ها می‌شنوی، از همین‌جاست. آن‌ها از آنچه دیده‌اند یاد می‌گیرند، و اگر آنچه دیده‌اند کج باشد، بزرگ‌تر شدنشان فقط کجی را محکم‌تر می‌کند.'))
w('''      <p style="%s">و اینکه «چقدر مشاهده کافی است»، جواب ثابتی ندارد. بستگی دارد به اینکه می‌خواهی چقدر دقیق باشی و چقدر حاضری اشتباه کنی. کار برنولی دقیقاً همین را قابل حساب کرد: به‌جای «زیاد»، عدد گذاشت.</p>
    </section>''' % BODY)

# ------------------------------------------------------------------ ۰۶ بیز
bx = []
def cell(x, y, wd, ht, fill, stroke, label, sub, lc):
    return ['          <rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="1.5"/>'
            % (x, y, wd, ht, fill, stroke),
            '          <text x="%d" y="%d" font-size="12.5" fill="%s" font-weight="700" text-anchor="middle" direction="rtl">%s</text>'
            % (x + wd / 2, y + ht / 2 - 4, lc, label),
            '          <text x="%d" y="%d" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">%s</text>'
            % (x + wd / 2, y + ht / 2 + 15, DIM, sub)]
bx += ['          <text x="360" y="22" font-size="12.5" fill="%s" font-weight="700" text-anchor="middle" direction="rtl">هزار سکه در کیسه</text>' % INK]
bx += cell(470, 36, 200, 56, SOFT, AC, '۱۰ سکهٔ تقلبی', 'یک در صد', AC)
bx += cell(50, 36, 390, 56, '#FFFFFF', LINE, '۹۹۰ سکهٔ سالم', 'نودونه در صد', INK)
bx += ['          <text x="360" y="118" font-size="12" fill="%s" text-anchor="middle" direction="rtl">صرّاف می‌گوید «تقلبی است». او نُه بار از ده بار درست می‌گوید.</text>' % MID]
bx += cell(560, 134, 110, 52, SOFT, AC, '۹', 'درست', AC)
bx += cell(440, 134, 110, 52, '#FFFFFF', LINE, '۱', 'جا انداخت', DIM)
bx += cell(230, 134, 200, 52, '#FBEBE2', RUST, '۹۹', 'اشتباه گفت تقلبی', RUST)
bx += cell(50, 134, 170, 52, '#FFFFFF', LINE, '۸۹۱', 'درست گفت سالم', DIM)
bx += ['          <text x="360" y="212" font-size="13" fill="%s" font-weight="700" text-anchor="middle" direction="rtl">از ۱۰۸ سکه‌ای که «تقلبی» خوانده شد، فقط ۹ تا واقعاً تقلبی است — کمتر از یک‌دوازدهم</text>' % RUST]
svg6 = ('0 0 720 226', '\n'.join(bx))

w('''
    <section id="s6" style="background: #FFFFFF; border-top: 1px solid %s; border-bottom: 1px solid %s; margin-top: 44px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
      <p style="%s">۰۶ — باور</p>
      <h2 style="%s">قاعده‌ای برای عوض کردن باور، وقتی خبر تازه می‌رسد</h2>
%s
      <p style="%s">این مهم‌ترین بخش نامه است. اگر بقیه را فراموش کنی و فقط این یکی بماند، باز هم چیز بزرگی برده‌ای.</p>
      <p style="%s">کشیشی انگلیسی به نام <b>توماس بِیز</b> در زمان زندگی‌اش این را منتشر نکرد. پس از مرگش دوستی به نام <b>ریچارد پرایس</b> نوشته‌اش را آماده کرد و در دسامبر ۱۷۶۳ در انجمن سلطنتی خوانده شد.</p>
      <p style="%s">حرفش در یک جمله: <b>باورِ تازه = باورِ پیشین، تصحیح‌شده با قوّتِ شاهد.</b> نه خبرِ تازه به‌تنهایی تعیین‌کننده است، نه باور قبلی. هر دو با هم.</p>''' % (
    LINE, LINE, EYE, H2,
    era('۷۰۰ سال بعد از تو', 'توماس بِیز (۱۷۰۲–۱۷۶۱) · رساله در ۱۷۶۳، پس از مرگش'), LEAD, BODY, BODY))
w('      <figure style="margin: 0 0 18px; %s padding: 20px 18px;">\n'
  '        <svg viewBox="%s" role="img" aria-label="%s" style="width: 100%%; max-width: 100%%; height: auto; display: block; font-family: inherit;">\n%s\n        </svg>\n'
  '        <figcaption style="font-size: 12.5px; line-height: 1.9; color: %s; margin-top: 14px; text-align: center;">%s</figcaption>\n'
  '      </figure>' % (SOFTC, svg6[0],
                      'نمودار هزار سکه: ده تقلبی و نهصدونود سالم، و نتیجهٔ تشخیص صرافی که نه بار از ده بار درست می‌گوید',
                      svg6[1], DIM,
                      'کل تلهٔ ماجرا در پهنای مستطیل‌هاست: صرّاف در هر دو طرف به یک اندازه دقیق است، ولی چون طرف راست بسیار کوچک‌تر است، خطاهای طرف چپ آن را غرق می‌کنند.'))
w(aside(
  'بگذار با دست حساب کنیم، چون این جایی است که تقریباً همه اشتباه می‌کنند — و اشتباهشان هم همیشه در یک جهت است.',
  'هزار سکه داری که ده تایش تقلبی است. صرّافی داری که نُه بار از هر ده بار درست تشخیص می‌دهد. سکه‌ای را نشانش می‌دهی و می‌گوید «تقلبی است». چقدر باور کنی؟',
  'از ده سکهٔ تقلبیِ واقعی، نُه تا را درست می‌گیرد. از نهصدونود سکهٔ سالم، یک‌دهمشان را اشتباهاً تقلبی می‌خواند — یعنی نودونه تا. پس روی هم صد و هشت سکه «تقلبی» خوانده می‌شوند، که فقط نُه تایشان واقعاً تقلبی است.',
  'یعنی وقتی صرّاف می‌گوید «تقلبی»، احتمال اینکه راست بگوید حدود <b>هشت در صد</b> است — نه نود در صد. و این با اینکه صرّاف واقعاً دقیق است هیچ تناقضی ندارد. <b>کمیاب بودنِ تقلبی، حرفِ صرّاف را رقیق می‌کند.</b>'))
w('''      <p style="%s">این همان چیزی است که بیز قاعده‌مندش کرد. باورِ پیشینِ تو این بود که «یک سکه از صد تقلبی است». شاهد آمد و باورت را بالا برد — از یک درصد به هشت درصد. هشت برابر شد، ولی هنوز به نود نرسید. <b>شاهد باور را جابه‌جا می‌کند؛ جایش نمی‌نشیند.</b></p>
      <p style="%s">و اگر باز هم صرّاف دومی هم همان را بگوید، باورت از هشت درصد شروع می‌شود، نه از یک درصد. این‌طور با هر شاهد تازه، عدد را به‌روز می‌کنی. <b>یادگیری، در ساده‌ترین تعریف ریاضی‌اش، همین است.</b></p>''' % (BODY, BODY))
w(aside(
  'و اینکه «باور» چطور می‌تواند عدد باشد: عددی میان صفر و یک که می‌گوید چقدر به چیزی اطمینان داری. صفر یعنی محال، یک یعنی قطعی، و نیم یعنی هیچ ترجیحی نداری.',
  'این قسمت در زمان خودش جنجالی بود و هنوز هم کسانی با آن مخالف‌اند. ایرادشان این است که عددِ باورِ <i>پیشین</i> را از کجا می‌آوری؟ گاهی از شمارش (مثل همین ده سکه از هزار)، ولی گاهی فقط از قضاوت خودت — و آن‌وقت جواب نهایی هم به همان قضاوت آلوده است.',
  'جواب عملی‌اش این است: پیشین را صریح بنویس تا دیگران بتوانند با آن مخالفت کنند. چیزی که پنهان بماند قابل نقد نیست. ماشین‌های امروزی هم همین کار را می‌کنند، فقط پیشینشان از میلیون‌ها مشاهده می‌آید نه از قضاوت یک نفر.'))
w('''      </div>
    </section>''')

# ------------------------------------------------------------------ ۰۷ بهترین خط
w('''
    <section id="s7" style="max-width: 1060px; margin: 0 auto; padding: 48px 24px 10px;">
      <p style="%s">۰۷ — بهترین خط</p>
      <h2 style="%s">وقتی اندازه‌گیری‌ها با هم نمی‌خوانند</h2>
%s
      <p style="%s">این بخش را مخصوص تو نوشته‌ام، چون مسئله‌اش دقیقاً مسئلهٔ خودِ توست.</p>
      <p style="%s">تو از بالای کوهی نزدیک قلعهٔ ناندنه، فرورفتگی افق را اندازه گرفتی و از روی آن شعاع زمین را حساب کردی. کاری که کردی زیرکانه بود، چون بر خلاف روش‌های پیش از تو به کاروان و سفرِ طولانی نیاز نداشت — از یک جا، با یک اندازه‌گیری.</p>
      <p style="%s">ولی یک مشکل داری که می‌دانمش: <b>اگر دو بار اندازه بگیری، دو عدد کمی متفاوت در می‌آید.</b> کدام درست است؟ میانگین؟ دقیق‌ترین؟ آن یکی که با انتظارت می‌خواند؟</p>''' % (
    EYE, H2, era('۸۰۰ سال بعد از تو', 'لوژاندر ۱۸۰۵ · گاوس ۱۸۰۹ · هر دو از دل نجوم'), LEAD, BODY, BODY))
w(aside(
  'این مسئله هزار سال بی‌جواب ماند و دلیلش هم روشن است: تا وقتی فکر می‌کنی خطا «اشتباهِ اندازه‌گیر» است، دنبال حذفش می‌گردی نه حسابش.',
  'جهش فکری این بود که بپذیریم خطا اجتناب‌ناپذیر است و خودش <b>قاعده</b> دارد: خطاهای کوچک بیشتر از بزرگ پیش می‌آیند، و کم‌و‌زیاد تقریباً به یک اندازه. وقتی خطا قاعده داشته باشد، می‌شود رویش ریاضی بنا کرد.'))
w('''      <p style="%s">هشتصد سال بعد از تو، دو نفر جداگانه جوابش را دادند. <b>آدرین-ماری لوژاندر</b> در ۱۸۰۵ نخستین شرح روشن آن را منتشر کرد، در کتابی دربارهٔ تعیین مدار دنباله‌دارها. <b>کارل فریدریش گاوس</b> در ۱۸۰۹ نسخهٔ خودش را منتشر کرد و گفت از ۱۷۹۵ به کارش می‌برده — که دعوای تقدمِ مفصلی راه انداخت.</p>
      <p style="%s">روششان را «کمترین مربعات» می‌نامند و منطقش ساده است: از میان همهٔ خط‌های ممکن، آن را بردار که <b>جمعِ مربعِ فاصله‌ها</b> از مشاهده‌هایت کمترین باشد.</p>''' % (BODY, BODY))
w(aside(
  'چرا مربع؟ دو دلیل، و هر دو را می‌شود با دست دید.',
  '<b>یک:</b> اگر فقط فاصله‌ها را جمع کنی، خطای «دو واحد بالاتر» و «دو واحد پایین‌تر» همدیگر را خنثی می‌کنند و جمعشان صفر می‌شود — یعنی خطی که از همهٔ نقطه‌ها دور است، می‌تواند نمرهٔ صفر بگیرد. مربع‌کردن علامت را از بین می‌برد.',
  '<b>دو:</b> مربع، خطای بزرگ را به‌شدت تنبیه می‌کند. خطای دو واحدی چهار امتیاز بد می‌گیرد، ولی خطای چهار واحدی شانزده تا. پس خط ترجیح می‌دهد از کنار همه کمی رد شود تا از کنار یکی خیلی دور باشد.',
  'و یک پیامد که باید بدانی: همین خاصیت، کمترین مربعات را در برابر یک مشاهدهٔ خیلی پرت <b>حساس</b> می‌کند. یک عدد غلط می‌تواند کل خط را بکشد.'))
w('''      <p style="%s">و مشهورترین نمایشش دقیقاً در رشتهٔ تو اتفاق افتاد. سیارکی به نام سرس کشف شد و بعد پشت خورشید گم شد. فقط چند مشاهدهٔ کوتاه در دست بود. گاوسِ بیست‌وچهار ساله با همین روش پیش‌بینی کرد کجا دوباره پیدا می‌شود — و تنها پیش‌بینی‌ای بود که به درد خورد. ستاره‌شناس‌ها همان‌جا پیدایش کردند.</p>
      <div style="%s padding: 22px 24px; border-inline-start: 4px solid %s; margin-bottom: 4px;">
        <p style="font-size: 16px; line-height: 2.05; color: %s; margin: 0;">این، تا جایی که من می‌فهمم، <b>نخستین یادگیری ماشینیِ تاریخ</b> است: چند مشاهدهٔ ناقص و پر خطا رفت تو، یک قاعده بیرون آمد، و آن قاعده چیزی را درست پیش‌بینی کرد که هیچ‌کس ندیده بود. نهصد سال بعد هم کاری که ماشین‌ها می‌کنند دقیقاً همین است — فقط به‌جای یک خط، میلیاردها عدد.</p>
      </div>
    </section>''' % (BODY, SOFTC, AC, INK))

# ------------------------------------------------------------------ ۰۸ سراشیبی (تعاملی)
w('''
    <section id="s8" style="background: #FFFFFF; border-top: 1px solid %s; border-bottom: 1px solid %s; margin-top: 44px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
      <p style="%s">۰۸ — سراشیبی</p>
      <h2 style="%s">و حالا خودت خط را جا بینداز</h2>
%s
      <p style="%s">شش کرت داری. به هر کدام چند پیمانه آب داده‌ای و چند خروار برداشته‌ای. حالا می‌خواهی خطی بکشی که بتواند بگوید کرت هفتم با هشت پیمانه آب چه می‌دهد.</p>
      <p style="%s">دو دکمهٔ اول، <b>شیب</b> خط را عوض می‌کنند و دو تای بعد آن را بالا و پایین می‌برند. عددی که باید کوچکش کنی، همان جمعِ مربعِ فاصله‌هاست. اول با دست امتحان کن — بعد بگذار ماشین خودش پیدایش کند.</p>

      <div style="%s padding: 22px 24px; margin-bottom: 14px;">
        <svg viewBox="0 0 520 268" role="img" aria-label="نمودار پراکندگی شش کرت با خط برازش و فاصلهٔ هر نقطه تا خط" style="width: 100%%; max-width: 100%%; height: auto; display: block; font-family: inherit;">
          <sc-for list="{{ticksY}}" as="t" hint-placeholder-count="5">
            <line x1="{{t.gx1}}" y1="{{t.gy}}" x2="{{t.gx2}}" y2="{{t.gy}}" stroke="#F0EEE7" stroke-width="1"/>
            <text x="{{t.x}}" y="{{t.y}}" font-size="11" fill="%s" text-anchor="middle">{{t.t}}</text>
          </sc-for>
          <line x1="70" y1="232" x2="480" y2="232" stroke="%s" stroke-width="1.5"/>
          <line x1="70" y1="232" x2="70" y2="26" stroke="%s" stroke-width="1.5"/>
          <sc-for list="{{ticksX}}" as="t" hint-placeholder-count="6">
            <text x="{{t.x}}" y="{{t.y}}" font-size="11" fill="%s" text-anchor="middle">{{t.t}}</text>
          </sc-for>
          <text x="275" y="262" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">پیمانهٔ آب</text>
          <text x="22" y="130" font-size="11.5" fill="%s" text-anchor="middle" direction="rtl">خروار</text>
          <sc-for list="{{dots}}" as="d" hint-placeholder-count="6">
            <line x1="{{d.cx}}" y1="{{d.cy}}" x2="{{d.cx}}" y2="{{d.ey}}" stroke="{{d.eCol}}" stroke-width="2" stroke-dasharray="3 3"/>
          </sc-for>
          <line x1="{{lx1}}" y1="{{ly1}}" x2="{{lx2}}" y2="{{ly2}}" stroke="%s" stroke-width="2.5"/>
          <sc-for list="{{dots}}" as="d" hint-placeholder-count="6">
            <circle cx="{{d.cx}}" cy="{{d.cy}}" r="5.5" fill="#FFFFFF" stroke="%s" stroke-width="2"/>
          </sc-for>
        </svg>
      </div>

      <div style="%s margin-bottom: 14px;">
        <div style="%s padding: 20px 22px;">
          <div style="font-size: 12px; color: %s; margin-bottom: 8px;">شیب خط</div>
          <div style="font-size: 30px; font-weight: 800; color: %s; line-height: 1;">{{aFa}}</div>
          <div style="font-size: 11.5px; color: %s; margin-top: 8px;">هر پیمانه آب، این‌قدر خروار</div>
        </div>
        <div style="%s padding: 20px 22px;">
          <div style="font-size: 12px; color: %s; margin-bottom: 8px;">نقطهٔ شروع</div>
          <div style="font-size: 30px; font-weight: 800; color: %s; line-height: 1;">{{bFa}}</div>
          <div style="font-size: 11.5px; color: %s; margin-top: 8px;">برداشت با صفر پیمانه</div>
        </div>
        <div style="%s padding: 20px 22px;">
          <div style="font-size: 12px; color: %s; margin-bottom: 8px;">جمع مربع فاصله‌ها</div>
          <div style="font-size: 30px; font-weight: 800; color: %s; line-height: 1;">{{errFa}}</div>
          <div style="height: 9px; background: #F0EEE7; border-radius: 5px; overflow: hidden; margin-top: 10px;">
            <div style="width: {{barW}}%%; height: 100%%; background: %s; border-radius: 5px;"></div>
          </div>
        </div>
        <div style="%s padding: 20px 22px;">
          <div style="font-size: 12px; color: %s; margin-bottom: 8px;">گام‌های سراشیبی</div>
          <div style="font-size: 30px; font-weight: 800; color: %s; line-height: 1;">{{stepsFa}}</div>
          <div style="font-size: 11.5px; color: %s; margin-top: 8px;">کمترین خطای ممکن: {{bestFa}}</div>
        </div>
      </div>

      <div style="display: flex; gap: 9px; flex-wrap: wrap; margin-bottom: 12px;">
        <sc-for list="{{btns}}" as="c" hint-placeholder-count="4">
          <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
        </sc-for>
      </div>
      <div style="display: flex; gap: 9px; flex-wrap: wrap; align-items: center;">
        <sc-for list="{{runs}}" as="c" hint-placeholder-count="4">
          <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
        </sc-for>
      </div>
      <p style="{{vStyle}}; margin-top: 14px;">{{verdict}}</p>
''' % (LINE, LINE, EYE, H2,
       era('۸۰۰ سال بعد از تو', 'اوگوستن-لویی کوشی · یادداشت سال ۱۸۴۷'), LEAD, BODY,
       SOFTC, DIM, LINE, LINE, DIM, DIM, DIM, AC, AC,
       GRID % (190, 12), CARD, DIM, AC, DIM, CARD, DIM, AC, DIM,
       CARD, DIM, AC, RUST, CARD, DIM, AC, DIM))
w(aside(
  'اگر دکمهٔ «تا ته برو» را بزنی، ماشین در چند صد گام به شیب ۱٫۶ و نقطهٔ شروع ۱٫۱ می‌رسد و خطا روی ۴٫۵۳ می‌ایستد. این دقیقاً همان جوابی است که روش لوژاندر و گاوس با یک حساب مستقیم می‌دهد.',
  'پس اگر جواب مستقیم هست، چرا سُر خوردن؟ چون برای یک خط ساده جوابِ مستقیم وجود دارد، ولی برای مدل‌های امروزی — که به‌جای دو عدد، میلیاردها عدد دارند — هیچ فرمول مستقیمی نیست. تنها راه، همین پایین رفتن گام‌به‌گام است.',
  'به این سُر خوردن می‌گویند «کاهش گرادیان» و معمولاً سرچشمه‌اش را به یادداشت کوتاهی از <b>کوشی</b> در سال ۱۸۴۷ برمی‌گردانند — هرچند او آن را برای حل دستگاه معادله‌ها نوشت، نه برای یادگیری.'))
w(aside(
  'تصویرش ساده است: کسی را در شیب کوه گذاشته‌اند و چشم‌بندی زده‌اند. نمی‌داند دره کجاست. تنها کاری که می‌تواند بکند این است که با پا بسنجد کدام طرف سرازیرتر است و یک قدم آن طرف بردارد. بعد دوباره. و دوباره.',
  'اندازهٔ قدم خیلی مهم است. قدم بسیار کوچک یعنی تا شب هم به دره نمی‌رسی. قدم بسیار بزرگ یعنی از دره می‌پری آن طرف و بالا می‌روی، و گاهی هرگز آرام نمی‌گیری. پیدا کردن اندازهٔ درست قدم، هنوز یکی از دردسرهای روزمرهٔ این حرفه است.',
  'و یک محدودیت که تا امروز هم هست: اگر کوه چند درهٔ جدا داشته باشد، این آدم در نزدیک‌ترین دره گیر می‌افتد، نه لزوماً در گودترین. برای خط راست این مشکل وجود ندارد (یک دره بیشتر نیست)، ولی برای مدل‌های بزرگ همیشه هست.'))
w('''      </div>
    </section>''')

# ------------------------------------------------------------------ ۰۹ بازگشت
w('''
    <section id="s9" style="max-width: 1060px; margin: 0 auto; padding: 48px 24px 10px;">
      <p style="%s">۰۹ — بازگشت</p>
      <h2 style="%s">چرا پسرِ مردان بسیار بلند، معمولاً کوتاه‌تر از پدرش است</h2>
%s
      <p style="%s"><b>فرانسیس گالتون</b> قد صدها خانواده را اندازه گرفت — پدر و مادر، و فرزندانشان در بزرگ‌سالی — و چیز عجیبی دید.</p>
      <p style="%s">پسرانِ پدرانِ بسیار بلند، به‌طور متوسط بلندتر از میانگین بودند، ولی <b>کوتاه‌تر از پدرانشان</b>. و پسرانِ پدرانِ بسیار کوتاه، کوتاه‌تر از میانگین بودند ولی <b>بلندتر از پدرانشان</b>. انگار چیزی قد فرزندان را به سمت میانهٔ جمعیت می‌کشید.</p>
      <p style="%s">او اسمش را گذاشت «بازگشت به سوی میانمایگی». امروز آن واژهٔ تحقیرآمیز را برداشته‌اند و می‌گویند «بازگشت به میانگین» — ولی خودِ واژهٔ <b>«رگرسیون»</b>، که امروز نام یکی از پرکاربردترین ابزارهای هوش مصنوعی است، از همین مقاله مانده است.</p>''' % (
    EYE, H2, era('۸۴۰ سال بعد از تو', 'فرانسیس گالتون · مقالهٔ سال ۱۸۸۶'), LEAD, BODY, BODY))
w(aside(
  'اول بگویم این <b>چه چیزی نیست</b>، چون سوءتفاهمش خیلی گران تمام می‌شود.',
  'این نمی‌گوید نسل‌ها به سمت یکسان‌شدن می‌روند و بالاخره همه هم‌قد می‌شوند. اگر این‌طور بود، تا حالا شده بود. پراکندگی قدها نسل به نسل تقریباً ثابت می‌ماند.',
  'چیزی که می‌گوید دربارهٔ <b>انتخابِ نمونه</b> است: وقتی تو کسانی را انتخاب می‌کنی که در یک اندازه‌گیری <i>نهایت</i> بوده‌اند، بخشی از آن نهایت بودن از بخت آمده، نه از جوهر. و بخت در دفعهٔ بعد تکرار نمی‌شود.',
  'آن پدرِ بسیار بلند، هم ذاتاً بلند بوده و هم کمی خوش‌شانس. پسرش ذات را به ارث می‌برد، شانس را نه.'))
w(aside(
  'و حالا تلهٔ عملی‌اش، که در هر دوره‌ای کسانی را فریب داده است.',
  'فرض کن پس از هر برداشتِ بسیار بد، سرکارگر را سرزنش می‌کنی، و پس از هر برداشت بسیار خوب، او را می‌ستایی. چه می‌بینی؟ بعد از سرزنش، کار بهتر می‌شود. بعد از ستایش، بدتر. نتیجه می‌گیری سرزنش مؤثر است و ستایش مضر.',
  'ولی دقیقاً همین را می‌دیدی حتی اگر هیچ‌کدام را نگفته بودی. برداشتِ خیلی بد تا حدی بدشانسی بوده و دفعهٔ بعد خودبه‌خود بهتر می‌شود؛ خیلی خوب هم همین‌طور. <b>بازگشت به میانگین، تأثیرِ کارِ تو را جعل می‌کند.</b>',
  'به همین دلیل در سنجیدن هر درمان و هر روش و هر مدل، باید گروهی هم باشد که کاری رویش نکرده‌ای. بدون آن، داری اثرِ بخت را به حساب خودت می‌گذاری.'))
w('''      <p style="%s">و پیوندش با بخش قبل: آن خطی که در بخش ۰۸ جا انداختی، شیبش همیشه <b>کمتر</b> از آن است که از روی نقطه‌های حدی حدس بزنی. خط، عمداً محتاط است. این محافظه‌کاری عیب نیست — همان چیزی است که باعث می‌شود پیش‌بینی‌اش برای کرت هفتم قابل اعتماد باشد.</p>
    </section>''' % BODY)

# ------------------------------------------------------------------ ۱۰ خبر
sh = []
SURP = [('حرف «الف»', 'خیلی پرتکرار', 12, 'خبر کم'), ('حرف «ر»', 'متوسط', 44, 'خبر متوسط'),
        ('حرف «ژ»', 'خیلی کمیاب', 92, 'خبر زیاد')]
for i, (name, freq, bar, note) in enumerate(SURP):
    y = 36 + i * 64
    # در متن راست‌به‌چپ، «start» یعنی لبهٔ راست. با «end» نوشته‌ها از x به راست
    # کشیده می‌شدند: برچسب‌ها از کادر بیرون می‌زدند و «کم/متوسط/زیاد» روی میله می‌افتاد.
    sh += ['          <text x="668" y="%d" font-size="13" fill="%s" font-weight="700" text-anchor="start" direction="rtl">%s</text>' % (y + 4, INK, name),
           '          <text x="668" y="%d" font-size="11" fill="%s" text-anchor="start" direction="rtl">%s</text>' % (y + 24, DIM, freq),
           '          <rect x="%d" y="%d" width="%d" height="22" rx="6" fill="%s"/>' % (520 - bar * 4.4, y - 10, bar * 4.4, AC),
           '          <text x="%d" y="%d" font-size="11.5" fill="%s" text-anchor="start" direction="rtl">%s</text>' % (505 - bar * 4.4, y + 6, AC, note)]
sh += ['          <text x="360" y="232" font-size="12" fill="%s" text-anchor="middle" direction="rtl">هرچه دیدنِ چیزی کم‌انتظارتر باشد، خبرِ بیشتری با خود می‌آورد</text>' % MID]
svg10 = ('0 0 720 246', '\n'.join(sh))

w('''
    <section id="s10" style="background: #FFFFFF; border-top: 1px solid %s; border-bottom: 1px solid %s; margin-top: 44px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
      <p style="%s">۱۰ — خبر</p>
      <h2 style="%s">اینکه «خبر» را هم می‌شود اندازه گرفت</h2>
%s
      <p style="%s">نهصد سال بعد از تو، مهندسی به نام <b>کلود شانون</b> مقاله‌ای نوشت که در آن کاری کرد که تا آن روز به نظر نشدنی می‌آمد: <b>خبر را اندازه گرفت.</b></p>
      <p style="%s">ایده‌اش به شکل غریبی به الکندیِ بخش ۰۱ وصل است. شانون گفت مقدار خبری که یک پیام می‌آورد، به این بستگی دارد که <b>چقدر غافلگیرکننده</b> باشد. چیزی که انتظارش را داشتی، خبر کمی دارد. چیزی که بعید بود، خبر زیادی دارد.</p>''' % (
    LINE, LINE, EYE, H2,
    era('۹۰۰ سال بعد از تو', 'کلود شانون · مقالهٔ ۱۹۴۸، در دو بخش'), LEAD, BODY))
w('      <figure style="margin: 0 0 18px; %s padding: 20px 18px;">\n'
  '        <svg viewBox="%s" role="img" aria-label="%s" style="width: 100%%; max-width: 100%%; height: auto; display: block; font-family: inherit;">\n%s\n        </svg>\n'
  '        <figcaption style="font-size: 12.5px; line-height: 1.9; color: %s; margin-top: 14px; text-align: center;">%s</figcaption>\n'
  '      </figure>' % (SOFTC, svg10[0], 'نمودار سه حرف با بسامد متفاوت و مقدار خبری که هر کدام می‌آورند',
                      svg10[1], DIM,
                      'همان نمودار بسامد بخش ۰۱، وارونه. حرفی که الکندی را به جواب می‌رساند کم‌خبرترین حرف است؛ و حرفی که به‌ندرت می‌آید، وقتی بیاید بیشترین خبر را دارد.'))
w(aside(
  'چرا این وارونگی معنا دارد: اگر بگویم «فردا خورشید طلوع می‌کند»، چیزی به دانش تو اضافه نکرده‌ام. اگر بگویم «فردا خورشید طلوع نمی‌کند»، جمله‌ای به همان کوتاهی گفته‌ام ولی دنیای تو را زیر و رو کرده.',
  'پس «مقدار خبر» خاصیتِ خودِ جمله نیست؛ خاصیت رابطهٔ جمله با <b>انتظار پیشینِ</b> شنونده است. و همین، این بخش را مستقیم به قاعدهٔ بیز در بخش ۰۶ وصل می‌کند: خبری که باور تو را خیلی جابه‌جا می‌کند، خبر پرمایه‌ای است.',
  'شانون واحدی هم برایش گذاشت و نامش را «بیت» نهاد. یک بیت یعنی خبری که دقیقاً یکی از دو حالتِ هم‌بخت را روشن می‌کند — همان «رو یا زیرِ نخ» در نامهٔ اول.'))
w('''      <p style="%s">و چرا این برای ماشین‌های امروزی مرکزی است: ماشینی که حدس می‌زند کلمهٔ بعدی چیست، در هر گام دارد می‌پرسد «کدام گزینه کم‌غافلگیرکننده‌تر است؟» و آموزش دادنش یعنی تنظیم کردن عددهایش تا <b>روی متن‌های واقعی کمتر غافلگیر شود</b>. معیاری که با آن سنجیده می‌شود، نوهٔ مستقیم همین مقالهٔ ۱۹۴۸ است.</p>
      </div>
    </section>''' % BODY)

# ------------------------------------------------------------------ ۱۱ یادگیری
w('''
    <section id="s11" style="max-width: 1060px; margin: 0 auto; padding: 48px 24px 10px;">
      <p style="%s">۱۱ — یادگیری</p>
      <h2 style="%s">ماشینی که به‌جای فرمان گرفتن، مثال می‌بیند</h2>
%s
      <p style="%s">حالا همهٔ قطعه‌ها را داریم و می‌شود آن چیزی را ساخت که نامهٔ اول نمی‌توانست توضیحش بدهد.</p>
      <p style="%s">در نامهٔ اول، هر کاری که ماشین می‌کرد را کسی از پیش نوشته بود. <b>فرانک رزنبلات</b> دستگاهی ساخت که این‌طور نبود. به آن مثال نشان می‌دادی — این تصویر «الف» است، آن یکی نیست — و خودش عددهای درونی‌اش را کم‌وزیاد می‌کرد تا کمتر اشتباه کند.</p>''' % (
    EYE, H2, era('۹۱۰ سال بعد از تو', 'فرانک رزنبلات · پرسپترون، سال ۱۹۵۸'), LEAD, BODY))
w(aside(
  'و «یاد گرفتن» این‌جا هیچ معنای رازآلودی ندارد. دقیقاً همان کاری است که در بخش ۰۸ با دست انجام دادی.',
  'دستگاه برای هر ورودی یک عدد دارد — به آن می‌گویند «وزن»، چون تعیین می‌کند آن ورودی چقدر در تصمیم اثر بگذارد. جواب می‌دهد، با جواب درست می‌سنجد، و اگر اشتباه کرد وزن‌ها را کمی در جهتی عوض می‌کند که دفعهٔ بعد خطا کمتر باشد. همین، هزاران بار.',
  '<b>تفاوت با فرمان‌گرفتن این است:</b> در نامهٔ اول تو می‌گفتی «چه کن». این‌جا تو می‌گویی «چه چیزی درست است» و دستگاه خودش «چه کن» را پیدا می‌کند. تو هدف را تعریف می‌کنی، نه راه را.'))
w('''      <p style="%s">پس بگذار صادقانه بگویم این چیست و چه نیست. دستگاهی که «یاد می‌گیرد» چیزی را نمی‌فهمد؛ عددهایش را طوری تنظیم می‌کند که روی مثال‌هایی که دیده کمتر خطا کند. همان خدمتکار نفهمِ نامهٔ اول است — فقط این بار به‌جای فهرست فرمان، <b>یک معیارِ خطا</b> به او داده‌ای و گفته‌ای کمش کن.</p>
      <p style="%s">و این همه را که کنار هم بگذاری، چیزی که به دست می‌آید حیرت‌انگیز است ولی مرموز نیست:</p>
      <div style="%s">''' % (BODY, BODY, GRID % (250, 14)))
PIPE = [('۱. شمردن', 'از انبوه مثال‌ها، بسامدها و الگوها شمرده می‌شود.', 'الکندی، ۸۵۰', AC),
        ('۲. برازش', 'قاعده‌ای انتخاب می‌شود که به مشاهده‌ها نزدیک‌ترین باشد.', 'لوژاندر و گاوس، ۱۸۰۵', GREEN),
        ('۳. سراشیبی', 'عددهای قاعده گام‌به‌گام تغییر می‌کنند تا خطا کم شود.', 'کوشی، ۱۸۴۷', RUST),
        ('۴. به‌روز کردن', 'با هر شاهد تازه، باور جابه‌جا می‌شود، نه جایگزین.', 'بیز، ۱۷۶۳', SEPIA)]
for title, what, who, col in PIPE:
    w('''        <div style="%s padding: 22px 24px; border-top: 3px solid %s;">
          <h3 style="%s color: %s;">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: %s; margin: 0 0 12px;">%s</p>
          <div style="font-size: 11.5px; color: %s; padding-top: 10px; border-top: 1px solid #F0EEE7;">%s</div>
        </div>''' % (CARD, col, H3, col, title, MID, what, DIM, who))
w('''      </div>
    </section>''')

# ------------------------------------------------------------------ ۱۲ خط زمان
# سالِ هر سطر، سالِ خودِ کار است نه سال مرگ: «الجبر» خوارزمی حدود ۸۲۰ نوشته شد،
# پس پیش از رسالهٔ الکندی می‌نشیند.
TL = [('۸۲۰', 'خوارزمی', 'جبر و اندیشهٔ «روش»', 'واژهٔ الگوریتم از نام او ماند', True),
      ('۸۵۰', 'الکِندی', 'شکستن رمز با شمردن حرف‌ها', 'نخستین استنتاج آماریِ شناخته‌شده', True),
      ('۱۰۰۰', 'الکَرَجی', 'جدول شمارش راه‌ها', 'در زمان خودِ ابوریحان', True),
      ('۱۰۴۸', 'خیام', 'همان جدول، پیش‌تر برده', 'سال مرگ ابوریحان، سال تولد خیام', True),
      ('۱۶۵۴', 'پاسکال و فرما', 'بخت، عدد می‌شود', 'نقطهٔ آغاز نظریهٔ احتمال', False),
      ('۱۷۱۳', 'یاکوب برنولی', 'قانون اعداد بزرگ', 'چرا شمردنِ بیشتر بهتر است', False),
      ('۱۷۶۳', 'توماس بیز', 'به‌روز کردن باور با شاهد', 'هستهٔ یادگیری امروز', False),
      ('۱۸۰۵', 'لوژاندر و گاوس', 'کمترین مربعات', 'نخستین مدلِ پیش‌بینی‌کننده', False),
      ('۱۸۴۷', 'کوشی', 'سُر خوردن به سمت کمینه', 'راهی که امروز همهٔ مدل‌ها یاد می‌گیرند', False),
      ('۱۸۸۶', 'گالتون', 'بازگشت به میانگین', 'واژهٔ «رگرسیون» از این‌جاست', False),
      ('۱۹۴۸', 'شانون', 'اندازه‌گیری خبر', 'معیاری که مدل‌ها با آن سنجیده می‌شوند', False),
      ('۱۹۵۸', 'رزنبلات', 'ماشینی که از مثال یاد می‌گیرد', 'نخستین گام به سمت امروز', False)]

w('''
    <section id="s12" style="background: #FFFFFF; border-top: 1px solid %s; border-bottom: 1px solid %s; margin-top: 44px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
      <p style="%s">۱۲ — همه با هم</p>
      <h2 style="%s">هزار و صد سال، روی یک خط</h2>
      <p style="%s">نقطه‌های پررنگ در زمان تو یا پیش از تواند. بقیه بعد می‌آیند، و فاصله‌شان را که ببینی چیزی دستگیرت می‌شود: <b>میان نخستین شمردن و نخستین ماشینی که یاد گرفت، هزار و صد سال فاصله است</b> — و هیچ‌کدام از گام‌های میانی را نمی‌شد پرید.</p>
      <div style="%s padding: 26px 28px;">''' % (LINE, LINE, EYE, H2, LEAD, CARD))
for i, (year, who, what, note, old) in enumerate(TL):
    col = AC if old else DIM
    bg = SOFT if old else '#FAFAF7'
    last = (i == len(TL) - 1)
    w('''        <div style="display: flex; gap: 14px; align-items: stretch;">
          <div style="flex-shrink: 0; width: 56px; text-align: center;">
            <div style="font-size: 13px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</div>
            <div style="width: 2px; background: %s; margin: 6px auto 0; height: calc(100%% - 26px); %s"></div>
          </div>
          <div style="flex: 1; min-width: 0; padding-bottom: %dpx;">
            <div style="background: %s; border-radius: 12px; padding: 13px 16px;">
              <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 5px;">
                <span style="font-size: 14.5px; font-weight: 800; color: %s;">%s</span>
                <span style="font-size: 13px; color: #16181C;">%s</span>
              </div>
              <p style="font-size: 12.5px; line-height: 1.8; color: %s; margin: 0;">%s</p>
            </div>
          </div>
        </div>''' % (col, year, SOFT if old else '#F0EEE7', 'opacity: 0;' if last else '',
                     10 if not last else 0, bg, col, who, what, DIM, note))
w('''      </div>
      <div style="%s padding: 24px 26px; margin-top: 16px; border-inline-start: 4px solid %s;">
        <h3 style="%s">و آنچه هنوز نمی‌کند</h3>
        <p style="font-size: 15px; line-height: 2.05; color: %s; margin: 0 0 12px;">هر چهار کارِ بالا دربارهٔ <b>الگو</b>ست، نه دربارهٔ <b>علت</b>. ماشین می‌بیند هر وقت آب بیشتر داده‌ای برداشت بیشتر شده، ولی از خودِ این شمارش نمی‌تواند بفهمد آب باعث برداشت است یا هر دو از چیز سومی می‌آیند — مثلاً اینکه کرت‌های بهتر هم آب بیشتری گرفته‌اند و هم خاک بهترى داشته‌اند.</p>
        <p style="font-size: 15px; line-height: 2.05; color: %s; margin: 0;">این تفاوت میان «با هم می‌آیند» و «یکی سبب دیگری است»، قدیمی‌ترین دامِ این حوزه است و هنوز باز است. هیچ مقدار شمردن، به‌تنهایی، آن را حل نمی‌کند. برای فهمیدن علت باید <b>مداخله</b> کنی: عمداً به یک کرت آب بیشتر بدهی و ببینی چه می‌شود. و این دیگر ریاضی نیست، آزمایش است.</p>
      </div>
      </div>
    </section>''' % (SOFTC, RUST, H3, MID, MID))

# ------------------------------------------------------------------ ۱۳ ترجمه
GLOSS = [
    ('شمردن بسامد حرف‌ها', 'تحلیل بسامد', 'frequency analysis', 'استنتاج چیزی پنهان از روی شمارش چیزهای دیدنی.', 's1'),
    ('روشِ مشخصِ کار', 'الگوریتم', 'algorithm', 'دنباله‌ای متناهی از گام‌های معلوم که مسئله‌ای را حل می‌کند.', 's2'),
    ('شمارِ راه‌ها', 'ترکیبیات', 'combinatorics', 'شمردن اینکه چند راه برای یک کار هست؛ پایهٔ احتمال.', 's3'),
    ('جدول کرجی و خیام', 'ضرایب دوجمله‌ای', 'binomial coefficients', 'چند راه برای برداشتن k چیز از n چیز.', 's3'),
    ('بخت، به‌صورت عدد', 'احتمال', 'probability', 'عددی میان صفر و یک: شمار راه‌های دلخواه بر شمار همهٔ راه‌ها.', 's4'),
    ('میانگین درازمدت', 'امید ریاضی', 'expected value', 'اگر بی‌شمار بار تکرار کنی، به‌طور متوسط چه عایدت می‌شود.', 's4'),
    ('هرچه بیشتر بشماری، دقیق‌تر', 'قانون اعداد بزرگ', 'law of large numbers', 'نسبتِ مشاهده‌شده با افزایش مشاهده به نسبت واقعی نزدیک می‌شود.', 's5'),
    ('نمونهٔ کج', 'سوگیری نمونه‌گیری', 'sampling bias', 'وقتی مشاهده‌هایت نمایندهٔ واقعیت نیستند؛ بیشتر شدنشان درمانش نمی‌کند.', 's5'),
    ('باورِ پیش از شاهد', 'پیشین', 'prior', 'اطمینانی که پیش از دیدن شاهد تازه داشتی.', 's6'),
    ('باور پس از شاهد', 'پسین', 'posterior', 'اطمینان به‌روزشده، بعد از اینکه شاهد را دیدی.', 's6'),
    ('به‌روز کردن باور با شاهد', 'قاعدهٔ بیز', "Bayes' rule", 'قاعده‌ای که پیشین و قوّت شاهد را به پسین تبدیل می‌کند.', 's6'),
    ('کمیاب بودن که حرف شاهد را رقیق می‌کند', 'خطای نرخ پایه', 'base rate fallacy', 'نادیده گرفتن اینکه خودِ پیشامد از اول چقدر نادر بوده.', 's6'),
    ('بهترین خط از میان نقطه‌ها', 'رگرسیون خطی', 'linear regression', 'ساده‌ترین مدل پیش‌بینی: از x به y با یک خط.', 's7'),
    ('جمع مربع فاصله‌ها', 'کمترین مربعات', 'least squares', 'معیاری که می‌گوید کدام خط به نقطه‌ها نزدیک‌تر است.', 's7'),
    ('فاصلهٔ هر نقطه تا خط', 'باقی‌مانده', 'residual', 'اختلاف میان آنچه دیدی و آنچه مدل پیش‌بینی کرد.', 's7'),
    ('سُر خوردن به سمت کمترین خطا', 'کاهش گرادیان', 'gradient descent', 'گام‌به‌گام در جهت سرازیری رفتن تا خطا کمینه شود.', 's8'),
    ('اندازهٔ قدم', 'نرخ یادگیری', 'learning rate', 'چقدر در هر گام جابه‌جا شوی؛ کوچک یعنی کند، بزرگ یعنی پریدن.', 's8'),
    ('درهٔ نزدیک به‌جای گودترین دره', 'کمینهٔ محلی', 'local minimum', 'جایی که دیگر سرازیری نیست، ولی بهترین جای ممکن هم نیست.', 's8'),
    ('کشیده‌شدن به سمت میانه', 'بازگشت به میانگین', 'regression to the mean', 'مقدارهای حدی در اندازه‌گیری بعدی به میانه نزدیک‌تر می‌شوند.', 's9'),
    ('اندازهٔ غافلگیری', 'آنتروپی', 'entropy · information', 'مقدار خبری که یک پیام می‌آورد؛ واحدش بیت است.', 's10'),
    ('عددی که اثر هر ورودی را تعیین می‌کند', 'وزن', 'weight', 'همان چیزی که در آموزش کم‌وزیاد می‌شود.', 's11'),
    ('معیار اینکه چقدر بد کار می‌کند', 'تابع زیان', 'loss function', 'عددی که آموزش می‌کوشد کمینه‌اش کند.', 's11'),
    ('نخستین ماشینی که از مثال یاد گرفت', 'پرسپترون', 'perceptron', 'مدل سادهٔ رزنبلات؛ جدِ شبکه‌های امروزی.', 's11'),
    ('با هم آمدن، در برابر سبب بودن', 'همبستگی و علیت', 'correlation vs. causation', 'شمردن، دومی را ثابت نمی‌کند؛ برای آن باید مداخله کرد.', 's12'),
]
w('''
    <section id="s13" style="max-width: 1060px; margin: 0 auto; padding: 48px 24px 10px;">
      <p style="%s">۱۳ — ترجمه</p>
      <h2 style="%s">حالا برگردیم به امروز</h2>
      <p style="%s">باز هم بدون هیچ واژهٔ تخصصی تا این‌جا آمدیم. این جدول همان نامه است با نام‌های امروزی، و ستون انگلیسی را جدا گذاشته‌ام تا وقت خواندن فارسی به چشم نیاید.</p>
      <div style="display: flex; flex-direction: column; gap: 10px;">''' % (EYE, H2, LEAD))
for old, new, en, what, sid in GLOSS:
    w('''        <div style="%s padding: 18px 22px; border-inline-start: 3px solid %s;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
            <span style="font-size: 14.5px; color: %s;">%s</span>
            <span style="font-size: 13px; color: %s;">←</span>
            <span style="font-size: 15.5px; font-weight: 800; color: %s;">%s</span>
            <a href="#%s" style="font-size: 11.5px; color: %s; margin-inline-start: auto;">بخش مربوط ←</a>
          </div>
          <p style="%s font-size: 12.5px; line-height: 1.7; color: %s; margin: 0 0 8px;">%s</p>
          <p style="font-size: 13.5px; line-height: 1.95; color: %s; margin: 0;">%s</p>
        </div>''' % (CARD, AC, DIM, old, DIM, INK, new, sid, DIM, LTR, MID, en, MID, what))
w('''      </div>
      <p style="%s">بیست‌وچهار واژه. با بیست‌وپنج واژهٔ <a href="Logic.dc.html" style="font-weight: 700;">نامهٔ اول</a> روی هم می‌شود چهل‌ونه — و این تقریباً همهٔ واژگانی است که برای خواندن یک کتاب مقدماتی یادگیری ماشین لازم داری.</p>
    </section>''' % BODY)

# ------------------------------------------------------------------ ۱۴ روش و منابع
METHOD = [
    ('چه چیزی واقعیت تاریخی است',
     'تاریخ‌ها، نام‌ها و عنوان آثار. الکندی (۸۰۱–۸۷۳) و رساله‌اش حدود ۸۵۰؛ خوارزمی (حدود ۷۸۰–۸۵۰) و «الجبر» حدود ۸۲۰؛ الکَرَجی (حدود ۹۵۳–۱۰۲۹) و جدولش حدود ۱۰۰۰؛ خیام (۱۰۴۸–۱۱۳۱)؛ نامه‌نگاری پاسکال و فرما در ۱۶۵۴؛ «Ars Conjectandi» در ۱۷۱۳؛ رسالهٔ بیز در ۱۷۶۳؛ لوژاندر ۱۸۰۵ و گاوس ۱۸۰۹؛ کوشی ۱۸۴۷؛ گالتون ۱۸۸۶؛ شانون ۱۹۴۸؛ رزنبلات ۱۹۵۸.'),
    ('چه چیزی قالب است',
     'خودِ نامه. ابوریحان هیچ‌وقت چنین نامه‌ای نگرفت و هیچ‌چیز از این مفاهیم نخواند. خطاب‌های شخصی («تو که اندازه گرفتی») آرایهٔ ادبی‌اند، نه ادعای تاریخی. جایی هم که گفته‌ام فلان‌کس «پیوندی با هوش مصنوعی دارد»، تفسیر من از خطِ فکری است، نه ادعای اینکه خودش چنین قصدی داشته.'),
    ('دربارهٔ «نخستین»ها احتیاط کرده‌ام',
     'رسالهٔ الکندی را «کهن‌ترین متن شناخته‌شده» در این باره نوشته‌ام، نه «نخستین». نوشته‌های پیش‌تر ممکن است از میان رفته باشند. جدول الکَرَجی هم از راه نقل‌قول‌های السموأل به ما رسیده، چون خودِ اثرش در دست نیست.'),
    ('دعواهای تقدم را پنهان نکرده‌ام',
     'لوژاندر زودتر منتشر کرد و گاوس زودتر ادعای کشف کرد؛ دعوایشان واقعی و حل‌نشده است. دربارهٔ اینکه چقدر از قاعدهٔ بیز واقعاً از خودِ بیز است هم میان مورخان بحث هست. کوشی هم یادداشت ۱۸۴۷ را برای حل دستگاه معادله‌ها نوشت، نه برای یادگیری؛ انتسابِ رایجِ «نخستین کاهش گرادیان» به او، نسبت‌دادنِ پسینی است.'),
    ('عددها را خودم حساب کرده‌ام',
     'مثال سکه‌های تقلبی در بخش ۰۶ و عددهای بخش ۰۸ ساختگی ولی درست‌اند: اگر خودت حسابشان کنی به همین می‌رسی. خطِ بهینهٔ بخش ۰۸ واقعاً شیب ۱٫۶ و مبدأ ۱٫۰۷ دارد و کمترین خطایش ۴٫۵۳ است — و کاهش گرادیانِ همان صفحه دقیقاً به همین می‌رسد.'),
    ('چه چیزی این‌جا نیست',
     'شبکه‌های عصبی چندلایه، پس‌انتشار خطا، و هر چیزی که بعد از ۱۹۵۸ آمده. این نامه تا جایی می‌آید که <b>پایه</b> ساخته می‌شود. و نمودار بسامد حرف‌های فارسی در بخش ۰۱ نمایشی است، نه برگرفته از یک پیکرهٔ اندازه‌گیری‌شده — شکلش درست است، عددهایش دقیق نیستند.'),
]
SOURCES = [
    ('رسالهٔ رمزگشایی الکندی', 'Al-Kindi — Manuscript on Deciphering Cryptographic Messages (c. 850)',
     'https://en.wikipedia.org/wiki/Al-Kindi',
     'کهن‌ترین متن شناخته‌شده دربارهٔ تحلیل بسامد. ابن عَدلان بعدها نکتهٔ حجم نمونه را افزود.'),
    ('ریشهٔ واژهٔ الگوریتم', 'Algorism — from al-Khwārizmī',
     'https://en.wikipedia.org/wiki/Algorism', 'زنجیرهٔ نام خوارزمی تا واژهٔ امروزی.'),
    ('مثلث الکَرَجی', 'Al-Karaji — Pascal’s triangle c. 1000, via al-Samaw’al',
     'https://mathshistory.st-andrews.ac.uk/Biographies/Al-Karaji/',
     'ساخت کلی مثلث به الکَرَجی نسبت داده می‌شود؛ اثرش گم شده و از راه نقل‌قول می‌شناسیمش.'),
    ('رسالهٔ بیز', 'An Essay towards solving a Problem in the Doctrine of Chances (1763)',
     'https://en.wikipedia.org/wiki/An_Essay_Towards_Solving_a_Problem_in_the_Doctrine_of_Chances',
     'خوانده‌شده در انجمن سلطنتی در ۲۳ دسامبر ۱۷۶۳، به کوشش ریچارد پرایس، پس از مرگ بیز در ۱۷۶۱.'),
    ('کمترین مربعات', 'Least squares — Legendre 1805, Gauss 1809, and Ceres',
     'https://en.wikipedia.org/wiki/Least_squares',
     'نخستین شرح روشن از لوژاندر در ۱۸۰۵؛ پیش‌بینی گاوسِ بیست‌وچهارساله همان چیزی بود که سرس را دوباره پیدا کرد.'),
    ('کاهش گرادیان', 'Gradient descent — attributed to Cauchy, Comptes rendus 25 (1847)',
     'https://en.wikipedia.org/wiki/Gradient_descent',
     'یادداشت ۱۸۴۷ دربارهٔ حل دستگاه معادله‌ها بود؛ هادامار در ۱۹۰۷ مستقلاً روش مشابهی پیشنهاد کرد.'),
    ('بازگشت به میانگین', 'Galton — Regression towards Mediocrity in Hereditary Stature (1886)',
     'https://galton.org/bib/JournalItem.aspx_action=view_id=157',
     'مجلهٔ انجمن انسان‌شناسی، جلد ۱۵، صفحهٔ ۲۴۶ تا ۲۶۳.'),
    ('نظریهٔ اطلاعات', 'Shannon — A Mathematical Theory of Communication (1948)',
     'https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication',
     'در دو بخش، در شماره‌های ژوئیه و اکتبر مجلهٔ فنی بل. واژهٔ «بیت» از همین‌جاست.'),
    ('پرسپترون', 'Rosenblatt — The Perceptron, Psychological Review 65(6), 1958',
     'https://pubmed.ncbi.nlm.nih.gov/13602029/', 'صفحهٔ ۳۸۶ تا ۴۰۸.'),
    ('اندازه‌گیری زمین به دست بیرونی', 'Al-Biruni’s method — measuring Earth’s radius at Nandana',
     'https://dictionary.obspm.fr/terms/birunis-method/',
     'از بالای تپه‌ای نزدیک قلعهٔ ناندنه، با زاویهٔ فرورفتگی افق. برخلاف روش‌های پیشین به سفر طولانی نیاز نداشت.'),
]
w('''
    <section id="s14" style="background: #FFFFFF; border-top: 1px solid %s; margin-top: 44px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
      <p style="%s">۱۴ — روش و منابع</p>
      <h2 style="%s">کجا واقعیت است، کجا قالب، و کجا احتیاط کرده‌ام</h2>
      <p style="%s">این نامه پر از تاریخ و نام است و قالب ادبی‌اش می‌تواند گمراه کند. پس مرزها را صریح می‌نویسم.</p>
      <div style="%s margin-bottom: 26px;">''' % (LINE, EYE, H2, LEAD, GRID % (290, 14)))
for t, d in METHOD:
    w('''        <div style="%s padding: 22px 24px;">
          <h3 style="%s">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: %s; margin: 0;">%s</p>
        </div>''' % (SOFTC, H3, t, MID, d))
w('''      </div>
      <h3 style="font-size: 18px; font-weight: 800; margin: 0 0 8px;">منابع</h3>
      <p style="font-size: 13.5px; line-height: 1.9; color: %s; margin: 0 0 18px; max-width: 70ch;">ده منبع، برای ادعاهای تاریخی. خودِ مفهوم‌های ریاضی منبع جداگانه ندارند چون در هر کتاب مقدماتی آمار و احتمال هستند.</p>
      <div style="display: flex; flex-direction: column; gap: 10px;">''' % DIM)
for i, (fat, ent, url, note) in enumerate(SOURCES):
    w('''        <div style="%s padding: 20px 22px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
            <span style="font-size: 12px; font-weight: 700; color: %s;">%s</span>
            <h4 style="font-size: 14.5px; font-weight: 700; margin: 0; line-height: 1.6;">%s</h4>
          </div>
          <p style="%s font-size: 12.5px; line-height: 1.8; color: %s; margin: 0 0 9px; overflow-wrap: anywhere;">%s</p>
          <p style="font-size: 13px; line-height: 1.9; color: %s; margin: 0 0 9px;">%s</p>
          <p style="margin: 0;"><a href="%s" target="_blank" rel="noopener" style="font-size: 12px; font-weight: 700; color: %s; %s display: inline-block; max-width: 100%%; overflow-wrap: anywhere;">%s ↗</a></p>
        </div>''' % (SOFTC, AC, fa('%02d' % (i + 1)), fat, LTR, MID, ent, DIM, note, url, AC, LTR, url))
w('''      </div>
      <p style="font-size: 14px; line-height: 2.05; color: %s; margin: 26px 0 18px; max-width: 70ch;">و یک حرف آخر، همان که در نامهٔ اول هم گفتم: هر جا نتوانستم مفهومی را با ابزار هزار سال پیش توضیح بدهم، مشکل از مخاطب فرضی نبود. از این بود که خودم خوب نفهمیده بودمش.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="Logic.dc.html" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: %s; padding: 12px 22px; border-radius: 10px;">← نامهٔ اول: منطق برنامه‌نویسی</a>
        <a href="AiEngineer.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %s; padding: 12px 22px; border-radius: 10px;">قدم بعدی: مسیر مهندس هوش مصنوعی ←</a>
        <a href="AILiteracy.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %s; padding: 12px 22px; border-radius: 10px;">معماری سواد هوش مصنوعی ←</a>
        <a href="Library.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %s; padding: 12px 22px; border-radius: 10px;">کتابخانهٔ منابع ←</a>
      </div>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid %s; background: #FFFFFF;">
    <div style="max-width: 1060px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: %s;">رضا هاشمی · نامهٔ دوم به ابوریحان</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1060,"height":1400}}'>
''' % (MID, SEPIA, LINE, LINE, LINE, LINE, DIM) + L.LOGIC.strip() + '''
</script>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'Math.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars ·', len(NAV), 'sections ·', len(GLOSS), 'glossary ·',
      html.count('کمی بیشتر'), 'asides')
