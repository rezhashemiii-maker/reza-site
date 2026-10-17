# -*- coding: utf-8 -*-
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import logic as L
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402

I = L.ITEMS
N = len(I)
fa = L.fa
AC = '#166534'
SOFTAC = '#E3EEE1'
CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'
SOFT = 'background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 14px;'
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
EYE = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %s; margin: 0 0 12px;' % AC
H2 = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
H3 = 'font-size: 15px; font-weight: 800; margin: 0 0 10px; line-height: 1.6;'
LEAD = 'font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 10px;'
MUTE = 'font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 22px;'
NOTE = 'font-size: 11.5px; line-height: 1.85; color: #666158; margin: 8px 0 0; padding-top: 14px; border-top: 1px solid #F0EEE7;'
GRID = 'display: grid; grid-template-columns: repeat(auto-fit, minmax(%dpx, 1fr)); gap: %dpx;'

q = lambda f: [x for x in I if f(x)]
NOCODE = len(q(lambda x: x['diff'] == 1))
LOWCODE = len(q(lambda x: x['diff'] <= 2))
RECUR = len(q(lambda x: x['model'] == 'اشتراک ماهانه'))
FAST = len(q(lambda x: x['spd'] == 3))
BOTH = len(q(lambda x: x['market'] == 'هر دو'))
DOMONLY = len(q(lambda x: x['market'] == 'داخلی'))
GLOBONLY = len(q(lambda x: x['market'] == 'جهانی'))
NCAT = len(L.CATS)

o = []
w = o.append

NAV = [('s1', '۰۱ قاعده‌ها'), ('s2', '۰۲ اعداد'), ('s3', '۰۳ خط زمان'), ('s4', '۰۴ نقشه'),
       ('s5', '۰۵ انتخابگر'), ('s6', '۰۶ فهرست'), ('s7', '۰۷ ماشین‌حساب'), ('s8', '۰۸ ضدفهرست'),
       ('s9', '۰۹ ماشین و تو'), ('s10', '۱۰ شروع'), ('s11', '۱۱ قیمت'), ('s12', '۱۲ محدودیت'),
       ('s13', '۱۳ روش')]

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>هفتادوپنج در — سرویس‌هایی که با هوش مصنوعی می‌شود ساخت و فروخت</title>
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
  a{color:#166534;text-decoration:none}
  a:hover{color:#0F4A24}
  button{font-family:inherit;cursor:pointer;border:none}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:92px}
  ::selection{background:#E3EEE1;color:#166534}
  input{font-family:inherit;font-size:15px;color:#16181C;background:#FFFFFF;border:1px solid #D9D5C9;border-radius:12px;padding:13px 16px;width:100%;box-sizing:border-box}
  input:focus{outline:2px solid #166534;outline-offset:1px}
  input[type=number]{font-variant-numeric:tabular-nums;text-align:center}
  /* روی نمایشگر کوچک، نوار بخش‌ها از هدر چسبان بیرون می‌آید و به یک کارت ثابت زیر هیرو می‌رود */
  @media (max-width:860px){
    nav[data-sections]{display:none !important}
    div[data-sectionlist]{display:flex !important}
  }
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F5F3EE; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1120px; margin: 0 auto; padding: 12px 24px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
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
    <section style="max-width: 1120px; margin: 0 auto; padding: 56px 24px 10px;">
      <p style="%s">%s سرویس، %s دسته، ۶ سنجه برای هر سرویس، و ۳ ابزار تعاملی</p>
      <h1 style="font-size: clamp(30px, 5vw, 50px); line-height: 1.38; font-weight: 800; margin: 0 0 20px; letter-spacing: -0.01em;">هفتادوپنج در</h1>
      <p style="font-size: 18.5px; line-height: 1.95; color: #45494F; max-width: 64ch; margin: 0 0 18px;">این فهرست جواب یک سؤال مشخص است: <b>با ابزارهایی مثل کلاد، و بدون دانش کدنویسی زیاد، چه چیزی می‌شود ساخت که کسی پولش را بدهد؟</b></p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">هیچ‌کدام از این %s مورد «ایدهٔ استارتاپ» نیست. همه‌شان <b>سرویس</b>‌اند: کاری که یک نفر امروز برای یک کسب‌وکار انجام می‌دهد، فاکتور می‌دهد و پول می‌گیرد. تفاوتش با فهرست‌های معمول این است که هر ردیف شش عدد دارد — سختی فنی، تقاضا، رقابت، فاصله تا اولین درآمد، سرمایهٔ اولیه و ریسک — و می‌توانی روی هر شش‌تا فیلتر بگذاری.</p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">سه چیز این صفحه را از یک فهرست ساده جدا می‌کند: یک <b>انتخابگر</b> که با پنج سؤال پنج پیشنهاد می‌دهد، یک <b>ماشین‌حساب</b> که می‌گوید عددهایت اصلاً جمع می‌شود یا نه، و یک <b>ضدفهرست</b> از ده چیزی که نباید بسازی.</p>
      <p style="font-size: 14.5px; line-height: 1.9; color: #666158; max-width: 64ch; margin: 0 0 30px;">یک هشدار صادقانه از همان اول: <b>%s تا</b> از این %s مورد واقعاً بدون کدنویسی قابل اجراست و <b>%s تا</b> حداکثر «کم‌کد». بقیه یعنی باید بلد باشی چند ابزار را به هم وصل کنی. هیچ کدام هم «درآمد غیرفعال» نیست — همه‌شان کار است.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="#s5" style="font-size: 14.5px; font-weight: 700; color: #FFFFFF; background: %s; padding: 13px 26px; border-radius: 10px;">پنج سؤال، پنج پیشنهاد</a>
        <a href="#s6" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">فهرست کامل ←</a>
        <a href="#s8" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">ده چیزی که نساز ←</a>
      </div>
    </section>
''' % (EYE, fa(N), fa(NCAT), fa(N), fa(NOCODE), fa(N), fa(LOWCODE), AC))

STATS = [(fa(N), 'سرویس بررسی‌شده'), (fa(NOCODE), 'کاملاً بدون کد'),
         (fa(RECUR), 'با درآمد ماهانهٔ تکرارشونده'), (fa(FAST), 'اولین درآمد در چند روز')]
w('''    <section style="max-width: 1120px; margin: 0 auto; padding: 26px 24px 10px;">
      <div style="%s">''' % (GRID % (190, 12)))
for v, lab in STATS:
    w('''        <div style="%s padding: 20px 22px;">
          <div style="font-size: 28px; font-weight: 800; color: %s; line-height: 1;">%s</div>
          <div style="font-size: 12.5px; color: #666158; margin-top: 8px;">%s</div>
        </div>''' % (CARD, AC, v, lab))
w('''      </div>
    </section>''')

# فهرست بخش‌ها — فقط روی نمایشگر کوچک، به‌جای نوار هدر
w('''    <section style="max-width: 1120px; margin: 0 auto; padding: 18px 24px 0;">
      <div data-sectionlist="1" style="display: none; flex-wrap: wrap; gap: 7px; %s padding: 18px 20px;">
        <div style="width: 100%%; font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 4px;">فهرست بخش‌ها</div>''' % CARD)
for sid, lab in NAV:
    w('''        <a href="#%s" style="font-size: 12.5px; color: #45494F; background: #FAFAF7; border: 1px solid #EDEAE1; border-radius: 999px; padding: 7px 12px;">%s</a>''' % (sid, lab))
w('''      </div>
    </section>''')

# ------------------------------------------------------------------ ۰۱ قاعده‌ها
RULES = [
    ('یک درد، نه یک ابزار',
     'کسی برای «هوش مصنوعی» پول نمی‌دهد. برای «صندوق پشتیبانی‌ام هر روز شصت تیکت دارد و دو نفر تمام‌وقت درگیرند» پول می‌دهد. هر ردیف این فهرست با یک دردِ قابل گفتن شروع می‌شود، نه با نام یک مدل.'),
    ('خروجی قابل تحویل، نه دسترسی',
     'فروش «حساب هوش مصنوعی» سرویس نیست. فروش «ده قطعه محتوای آمادهٔ انتشار هر هفته» سرویس است. مشتری باید بتواند خروجی را ببیند، رد کند یا تأیید کند.'),
    ('تکرارشونده بر یک‌باره می‌چربد',
     'پروژهٔ یک‌باره درآمد می‌دهد؛ قرارداد ماهانه کسب‌وکار می‌سازد. %s تا از این %s سرویس ذاتاً ماهانه‌اند. اگر بین دو گزینه شک داری، آن را بردار که ماه بعد هم تکرار می‌شود.'),
    ('انسان در حلقه، همان چیزی است که می‌فروشی',
     'مدل، پیش‌نویس می‌دهد. چیزی که مشتری می‌خرد این است که یک نفر پیش‌نویس را بازبینی کرده و مسئولیتش را پذیرفته. این «بازبینی» نقطهٔ ضعف سرویس نیست، <b>محصول</b> است. بخش ۰۹ همین را عدد می‌کند.'),
    ('اول باریک، بعد عمیق',
     '«دستیار هوش مصنوعی برای همه» فروش نمی‌رود. «دستیار نوبت‌دهی برای مطب دندان‌پزشکی» فروش می‌رود. باریک شروع کن تا بتوانی در جلسهٔ اول دقیقاً حرف مشتری را بزنی.'),
    ('چیزی که اندازه‌گیری می‌شود، تمدید می‌شود',
     'اگر نتوانی بگویی «این ماه فلان‌قدر وقت یا فلان‌قدر هزینه کم شد»، قرارداد در اولین فشار بودجه حذف می‌شود. از روز اول یک عدد تعریف کن و ماهانه گزارشش بده.'),
]
w('''
    <section id="s1" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۱ — قاعده‌ها</p>
      <h2 style="%s">شش چیزی که یک سرویس را فروشنی می‌کند</h2>
      <p style="%s">قبل از فهرست، این شش قاعده را بگذارم؛ چون ترتیب فهرست از همین‌ها بیرون آمده. اگر این‌ها را بپذیری، نیمی از ایده‌های رایج بازار خودشان حذف می‌شوند.</p>
      <div style="%s">''' % (EYE, H2, LEAD, GRID % (290, 14)))
for i, (t, d) in enumerate(RULES):
    body = d % (fa(RECUR), fa(N)) if '%s' in d else d
    w('''        <div style="%s padding: 22px 24px; border-top: 3px solid %s;">
          <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 8px;">%s</div>
          <h3 style="%s">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, AC, AC, fa('%02d' % (i + 1)), H3, t, body))
w('''      </div>
    </section>''')

# ------------------------------------------------------------------ ۰۲ اعداد
w('''
    <section id="s2" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۲ — اعداد</p>
      <h2 style="%s">بازار چه می‌گوید</h2>
      <p style="%s">این بخش کوتاه است و عمداً فقط چند عدد دارد — عددهایی که خودم به منبعشان رسیدم. هرجا عدد خودگزارش‌شده یا تبلیغاتی بوده، همان‌جا نوشته‌ام.</p>
      <p style="%s">نکتهٔ مهم این است: رشد تقاضا در سمت <b>مهارت</b> است، نه در سمت <b>ابزار</b>. کسی که ابزار را به یک کار مشخص وصل می‌کند، گران‌تر از کسی است که ابزار را می‌شناسد.</p>''' % (EYE, H2, LEAD, MUTE))

GROWTH = [
    ('مهارت‌های مرتبط با هوش مصنوعی، در کل', 109, 'در برابر ۲۳٪ برای بقیهٔ مهارت‌ها'),
    ('تولید و تدوین ویدیو با هوش مصنوعی', 329, 'بیشترین رشد کل فهرست'),
    ('یکپارچه‌سازی هوش مصنوعی در محصول و فرایند', 178, 'اتصال مدل به کاری که از قبل انجام می‌شد'),
    ('برچسب‌زنی و آماده‌سازی داده', 154, 'کار دقیق و تکراری، با تقاضای بالا'),
    ('ساخت چت‌بات', 71, 'رشد دارد ولی از بقیه کمتر — یعنی رقابتی‌تر'),
]
GMAX = 329
w('''      <div style="%s padding: 24px 26px; margin-bottom: 14px;">
        <h3 style="%s">رشد تقاضای سال‌به‌سال در بازار کار آزاد</h3>
        <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0 0 18px;">بر پایهٔ گزارش «مهارت‌های پرتقاضا» آپورک، منتشرشده در بهمن ۱۴۰۴ / فوریهٔ ۲۰۲۶. اعداد، رشد تعداد آگهی‌های کار است نسبت به سال قبل.</p>''' % (SOFT, H3))
for name, v, note in GROWTH:
    w('''        <div style="margin-bottom: 14px;">
          <div style="display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; margin-bottom: 6px;">
            <span style="font-size: 13.5px; font-weight: 700; color: #16181C;">%s</span>
            <span style="font-size: 14px; font-weight: 800; color: %s; margin-inline-start: auto; font-variant-numeric: tabular-nums;">+%s٪</span>
          </div>
          <div style="height: 13px; background: #F0EEE7; border-radius: 7px; overflow: hidden;">
            <div style="width: %.1f%%; height: 100%%; background: %s; border-radius: 7px;"></div>
          </div>
          <p style="font-size: 11.5px; color: #666158; margin: 6px 0 0;">%s</p>
        </div>''' % (name, AC, fa(v), v * 100.0 / GMAX, AC, note))
w('''        <p style="%s">این اعداد از یک بازار کار آزاد می‌آیند، نه از کل اقتصاد. سوگیری‌اش روشن است: کارهایی که از راه دور و پروژه‌ای انجام می‌شوند بیش‌نمایی می‌شوند. ولی برای تصمیم «چه سرویسی بسازم»، دقیقاً همین بازار است که اهمیت دارد.</p>
      </div>''' % NOTE)

FACTS = [
    ('۵۸٪', 'از کسب‌وکارهای کوچک آمریکا از هوش مصنوعی مولد استفاده می‌کنند',
     'در ۲۰۲۴ این عدد ۴۰٪ بود. منبع: اتاق بازرگانی آمریکا. این «استفاده» تعریف گسترده‌ای دارد — از یک بار امتحان‌کردن تا استفادهٔ روزانه.'),
    ('~۱۸٪', 'از کسب‌وکارها هوش مصنوعی را در <b>تولید واقعی</b> به کار می‌برند',
     'سرشماری آمریکا، نظرسنجی روند کسب‌وکارها، اردیبهشت ۱۴۰۵. فاصلهٔ این عدد با ۵۸٪ بالا، خودِ بازار تو است: خیلی‌ها امتحان کرده‌اند، کم‌تری‌ها به فرایند رسانده‌اند.'),
    ('۹۵–۲۳۵ دلار', 'نرخ ساعتی خودگزارش‌شدهٔ کسانی که اتوماسیون می‌فروشند',
     'از یک نرخ‌نامهٔ خودگزارش‌شده با ۵۴ پاسخ‌دهنده. عدد کوچکی است و نمونهٔ آماری معتبر نیست — به چشم «بازهٔ تقریبی» نگاهش کن، نه آمار.'),
    ('۱٬۸۰۰–۴٬۵۰۰ دلار', 'برای یک پروژهٔ کامل «فرم سایت تا سامانهٔ مشتریان تا اعلان»',
     'از همان نرخ‌نامه. پروژه‌های بزرگ‌تر تا ۲۶ هزار دلار و قراردادهای ماهانه ۱٬۲۰۰ تا ۱۲٬۰۰۰ دلار گزارش شده‌اند.'),
    ('۹۹–۲۹۹ دلار ماهانه', 'قیمت رایج «منشی تلفنی هوشمند» برای یک کسب‌وکار کوچک',
     'از صفحهٔ قیمت فروشندگان این سرویس، نه از نظرسنجی مستقل. هزینهٔ تمام‌شدهٔ هر دقیقه را ۰٫۱۵ تا ۰٫۲۵ دلار اعلام می‌کنند.'),
    ('دو کاربرد، همیشه اول', 'محتوا و بازاریابی، و پشتیبانی مشتری',
     'در هر نظرسنجی‌ای که دیدم، این دو اول بودند — با اعدادی که از نظرسنجی تا نظرسنجی خیلی فرق می‌کند، چون تعریفشان فرق می‌کند. ترتیبشان اما ثابت است.'),
]
w('''      <div style="%s">''' % (GRID % (290, 14)))
for v, t, d in FACTS:
    w('''        <div style="%s padding: 22px 24px;">
          <div style="font-size: 22px; font-weight: 800; color: %s; line-height: 1.3; margin-bottom: 8px;">%s</div>
          <h3 style="font-size: 14px; font-weight: 700; margin: 0 0 10px; line-height: 1.7;">%s</h3>
          <p style="font-size: 13px; line-height: 1.95; color: #666158; margin: 0;">%s</p>
        </div>''' % (CARD, AC, v, t, d))
w('''      </div>
      </div>
    </section>''')

# ------------------------------------------------------------------ ۰۳ خط زمان
TL = [
    ('۱۹۹۵', 'اینترنت خانگی و اولین برون‌سپاری متن', 'تایپ، ترجمه، ورود داده', 'ارزانیِ نیروی کار از راه دور', False),
    ('۲۰۰۵', 'بازارهای کار آزاد آنلاین جا می‌افتند', 'ساعت کار، از هر کجای دنیا', 'دسترسی به بازار جهانی', False),
    ('۲۰۰۸', 'سئو به یک صنعت تبدیل می‌شود', 'مقالهٔ کلیدواژه‌محور، انبوه', 'دانستن اینکه گوگل چه می‌خواهد', False),
    ('۲۰۱۱', 'ابزارهای اتصال بدون کد می‌آیند', 'وصل‌کردن دو نرم‌افزار به هم', 'شناخت ابزارها', False),
    ('۲۰۱۵', 'آپورک از ادغام دو بازار بزرگ ساخته می‌شود', 'پروفایل، امتیاز، و اعتبار قابل اثبات', 'سابقهٔ قابل بررسی', False),
    ('۲۰۱۷', 'مقالهٔ ترنسفورمر منتشر می‌شود', 'هنوز هیچ — فقط یک معماری', 'هیچ‌کس هنوز چیزی نمی‌فروخت', True),
    ('۲۰۲۰', 'مدل‌های زبانی بزرگ به‌کارگیری می‌شوند', 'نوشتن ماشینی', 'دسترسی زودهنگام', True),
    ('۲۰۲۲', 'چت‌بات‌ها عمومی می‌شوند', 'جملهٔ جادویی — «پرامپت»', 'بلدبودن اینکه چه بنویسی', True),
    ('۲۰۲۳', 'سال پرامپت‌فروشی', 'بستهٔ پرامپت، دورهٔ پرامپت', 'و در همان سال، قیمتش به صفر رفت', True),
    ('۲۰۲۴', 'عامل‌ها و اتصال مدل به ابزارها', 'وصل‌کردن مدل به فرایند واقعی', 'شناخت فرایند، نه شناخت مدل', True),
    ('۲۰۲۶', 'رشد ۱۰۹٪ مهارت‌های مرتبط با هوش مصنوعی', 'قضاوت، بازبینی، و پذیرفتن مسئولیت', 'همان چیزی که ماشین ندارد', True),
]
w('''
    <section id="s3" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۳ — خط زمان</p>
      <h2 style="%s">لایهٔ سرویس همیشه یک پله بالا می‌رود</h2>
      <p style="%s">این بخش را اضافه کردم چون فکر می‌کنم مهم‌ترین چیزی است که در انتخاب سرویس باید بدانی — و تقریباً هیچ‌جا نوشته نمی‌شود. سی سال است که یک الگوی ثابت تکرار می‌شود: هر کاری که ماشین خوب انجامش می‌دهد، ظرف دو سال قیمتش به صفر میل می‌کند، و کسانی که ماندند آن‌هایی بودند که یک پله بالاتر رفتند.</p>
      <p style="%s">ستون سوم هر ردیف مهم‌تر از بقیه است: <b>چه چیزی واقعاً فروخته می‌شد.</b> هیچ‌وقت خود ابزار نبود.</p>
      <div style="%s padding: 24px 26px;">''' % (EYE, H2, LEAD, MUTE, CARD))
for i, (year, ev, sold, edge, ai) in enumerate(TL):
    col = AC if ai else '#8A8578'
    soft = SOFTAC if ai else '#F0EEE7'
    last = (i == len(TL) - 1)
    w('''        <div style="display: flex; gap: 14px; align-items: stretch;">
          <div style="flex-shrink: 0; width: 54px; text-align: center;">
            <div style="font-size: 13px; font-weight: 800; color: %s; font-variant-numeric: tabular-nums;">%s</div>
            <div style="width: 2px; background: %s; margin: 6px auto 0; height: calc(100%% - 26px); %s"></div>
          </div>
          <div style="flex: 1; min-width: 0; padding-bottom: %dpx;">
            <div style="background: %s; border-radius: 12px; padding: 14px 16px;">
              <h3 style="font-size: 14.5px; font-weight: 800; margin: 0 0 8px; line-height: 1.6; color: #16181C;">%s</h3>
              <p style="font-size: 13px; line-height: 1.85; color: #45494F; margin: 0 0 6px;"><span style="color: #666158;">چه فروخته می‌شد:</span> %s</p>
              <p style="font-size: 12.5px; line-height: 1.85; color: %s; margin: 0; font-weight: 600;">%s</p>
            </div>
          </div>
        </div>''' % (col, year, soft, 'opacity: 0;' if last else '', 10 if not last else 0,
                     soft, ev, sold, col, edge))
w('''        <div style="margin-top: 18px; padding: 18px 20px; background: %s; border-radius: 12px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 8px; color: %s;">قاعده‌ای که از این خط بیرون می‌آید</h3>
          <p style="font-size: 14px; line-height: 2; color: #16181C; margin: 0;">سرویست را روی کاری نبند که ماشین دارد خوب انجامش می‌دهد؛ روی کاری ببند که <b>ورودی</b> یا <b>خروجی</b> آن کار است. تولید متن کالا شد، ولی تصمیم اینکه چه متنی لازم است نشد. رونویسی کالا شد، ولی اینکه از دل آرشیو چه چیزی باید بیرون بیاید نشد. هر بار که یک لایه کالا می‌شود، لایهٔ بالاترش گران‌تر می‌شود.</p>
        </div>
        <p style="%s">تاریخ‌ها رویدادهای عمومی و قابل بررسی‌اند. ستون «چه چیزی واقعاً فروخته می‌شد» قضاوت من است از آنچه در هر دوره بازار داشت — نه داده‌ای که از جایی استخراج شده باشد.</p>
      </div>
    </section>''' % (SOFTAC, AC, NOTE))

# ------------------------------------------------------------------ ۰۴ نقشه
QUADS = [
    ('آسان و خالی', lambda x: x['diff'] <= 2 and x['sat'] <= 2, AC,
     'سختی فنی کم، رقابت کم. اگر تازه شروع می‌کنی، جای درست همین‌جاست — هم سریع می‌توانی تحویل بدهی، هم لازم نیست با ده نفر ارزان‌تر بجنگی.'),
    ('آسان و پررقابت', lambda x: x['diff'] <= 2 and x['sat'] >= 3, '#B4530E',
     'ورود راحت است و همه وارد شده‌اند. این‌ها را فقط با یک تمایز روشن بردار — یک صنعت خاص، یک زبان خاص، یا کیفیتی که قابل نشان‌دادن باشد. وگرنه سر قیمت می‌جنگی.'),
    ('سخت‌تر و خالی', lambda x: x['diff'] >= 3 and x['sat'] <= 2, '#1F4E5F',
     'باید چند ابزار را به هم وصل کنی و وقت بگذاری، ولی رقیب کم است. این‌ها سنگرهای بلندمدت‌اند: دیرتر به درآمد می‌رسند و سخت‌تر از دست می‌روند.'),
    ('سخت و پررقابت', lambda x: x['diff'] >= 3 and x['sat'] >= 3, '#8A1538',
     'هم ورود سخت است هم بازار پر. فقط وقتی سراغش برو که یک مزیت واقعی داری — مشتری آماده، دادهٔ اختصاصی، یا تجربهٔ همان صنعت.'),
]
w('''
    <section id="s4" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۴ — نقشه</p>
      <h2 style="%s">چهار ناحیه: سختی در برابر رقابت</h2>
      <p style="%s">یک چیز را باید همین اول بگویم: <b>تقاضا در این فهرست ستون تفکیک‌کننده نیست.</b> چون فهرست را از اول غربال کرده‌ام، هر %s مورد تقاضای بالا دارند. آنچه واقعاً آن‌ها را از هم جدا می‌کند دو چیز است: چقدر سخت است، و چند نفر دیگر دارند همین را می‌فروشند.</p>
      <p style="%s">در فهرست بخش ۰۶ می‌توانی با دو فیلتر «سختی» و «رقابت» دقیقاً همین چهار ناحیه را جدا کنی.</p>
      <div style="%s">''' % (EYE, H2, LEAD, fa(N), MUTE, GRID % (300, 14)))
for name, f, col, desc in QUADS:
    rows = sorted(q(f), key=lambda x: (-x['sc'], x['diff']))
    w('''        <div style="%s padding: 24px 26px; border-top: 3px solid %s;">
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 10px;">
            <h3 style="font-size: 17px; font-weight: 800; margin: 0; color: %s;">%s</h3>
            <span style="font-size: 13px; font-weight: 700; color: #666158; margin-inline-start: auto;">%s سرویس</span>
          </div>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0 0 14px;">%s</p>
          <div style="padding-top: 14px; border-top: 1px solid #F0EEE7;">
            <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 9px;">نمونه‌ها</div>
            <div style="display: flex; flex-direction: column; gap: 7px;">''' % (SOFT, col, col, name, fa(len(rows)), desc))
    for r in rows[:5]:
        w('''              <div style="font-size: 13px; line-height: 1.7; color: #16181C; padding-inline-start: 11px; border-inline-start: 2px solid %s;">%s</div>''' % (r['soft'], r['fa']))
    if len(rows) > 5:
        w('''              <div style="font-size: 12px; color: #666158; padding-inline-start: 11px;">و %s مورد دیگر در همین ناحیه</div>''' % fa(len(rows) - 5))
    w('''            </div>
          </div>
        </div>''')
w('''      </div>''')

# نیمرخ دسته‌ها
CATNOTE = {
    'content': 'بزرگ‌ترین و پررقابت‌ترین دسته. ورود آسان، ماندن سخت.',
    'support': 'تقاضای پایدار و قرارداد ماهانه؛ ولی مرز مسئولیت را باید روشن کنی.',
    'sales': 'قابل اثبات با عدد، پس گران‌تر فروش می‌رود — و زودتر تمدید می‌شود.',
    'data': 'کم‌هیجان‌ترین و یکی از سودآورترین‌ها. کسی برایش محتوا تولید نمی‌کند، پس کسی هم رقابت نمی‌کند.',
    'auto': 'نزدیک‌ترین دسته به «مهندسی»، و همان جایی که بالاترین نرخ‌های ساعتی گزارش شده.',
    'learn': 'سریع‌ترین راه به اولین پول، و بهترین راه برای فهمیدن اینکه بعد چه بسازی.',
    'design': 'سریع و دیدنی، ولی خروجی‌اش را همه می‌توانند با هم مقایسه کنند.',
    'audio': 'تازه‌ترین دسته. رقابت هنوز کم است، مخصوصاً به فارسی.',
    'research': 'کم‌رقابت‌ترین دستهٔ فهرست، چون واقعاً حوصله و دقت می‌خواهد.',
    'vertical': 'سخت‌ترین ورود و وفادارترین مشتری. اگر به یک صنعت دسترسی داری، از این‌جا شروع کن.',
}
w('''      <h3 style="font-size: 18px; font-weight: 800; margin: 28px 0 8px;">نیمرخ ده دسته</h3>
      <p style="font-size: 13.5px; line-height: 1.9; color: #666158; margin: 0 0 18px; max-width: 70ch;">میانگین سه سنجهٔ هر دسته، کنار هم. این نمودار نمی‌گوید کدام دسته بهتر است — می‌گوید هر دسته چه شکلی دارد.</p>
      <div style="%s">''' % (GRID % (300, 14)))
for key, cname, col, soft in L.CATS:
    rows = [x for x in I if x['cat'] == key]
    n = len(rows)
    av = lambda k: sum(x[k] for x in rows) / float(n)
    bars = [('آسانی', (5 - av('diff')) / 4.0), ('کم‌رقابتی', (5 - av('sat')) / 4.0),
            ('سرعت درآمد', (av('spd') - 1) / 2.0)]
    w('''        <div style="%s padding: 22px 24px; border-top: 3px solid %s;">
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 12px;">
            <h4 style="font-size: 15px; font-weight: 800; margin: 0; color: %s;">%s</h4>
            <span style="font-size: 12px; font-weight: 700; color: #666158; margin-inline-start: auto;">%s سرویس</span>
          </div>''' % (CARD, col, col, cname, fa(n)))
    for lab, g in bars:
        w('''          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span style="font-size: 11.5px; color: #666158; width: 62px; flex-shrink: 0;">%s</span>
            <div style="flex: 1; height: 9px; background: #F0EEE7; border-radius: 5px; overflow: hidden;">
              <div style="width: %d%%; height: 100%%; background: %s; border-radius: 5px;"></div>
            </div>
          </div>''' % (lab, max(4, int(round(12 + g * 88))), col))
    w('''          <p style="font-size: 12.5px; line-height: 1.9; color: #45494F; margin: 12px 0 0;">%s</p>
        </div>''' % CATNOTE[key])
w('''      </div>''')

# ده برتر
TOP = sorted(I, key=lambda x: (-x['sc'], x['diff']))[:10]
w('''      <div style="%s padding: 24px 26px; margin-top: 14px;">
        <h3 style="%s">ده سرویس با بالاترین امتیاز ترکیبی</h3>
        <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0 0 18px;">امتیاز یک میان‌بر است، نه حقیقت. فرمولش را عمداً نوشته‌ام تا بتوانی قبولش نکنی:</p>
        <div style="%s padding: 14px 16px; margin: 0 0 20px; font-size: 13px; line-height: 1.9; color: #16181C;">امتیاز &nbsp;=&nbsp; (تقاضا × ۲) &nbsp;+&nbsp; آسانی &nbsp;+&nbsp; سرعت رسیدن به درآمد &nbsp;+&nbsp; کم‌رقابتی<br><span style="color: #666158; font-size: 12px;">بیشینهٔ ممکن ۲۳، و اعداد به ۱۰۰ نرمال شده‌اند.</span></div>''' % (SOFT, H3, CARD))
for i, r in enumerate(TOP):
    w('''        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 11px;">
          <span style="font-size: 12px; font-weight: 700; color: #666158; width: 22px; flex-shrink: 0;">%s</span>
          <span style="font-size: 13px; color: #16181C; flex: 1 1 180px; min-width: 0; line-height: 1.6;">%s</span>
          <div style="flex: 1 1 90px; height: 11px; background: #F0EEE7; border-radius: 6px; overflow: hidden; min-width: 60px;">
            <div style="width: %d%%; height: 100%%; background: %s; border-radius: 6px;"></div>
          </div>
          <span style="font-size: 12px; font-weight: 700; color: %s; width: 32px; flex-shrink: 0; text-align: left; font-variant-numeric: tabular-nums;">%s</span>
        </div>''' % (fa(i + 1), r['fa'], r['pct'], r['color'], AC, r['pctFa']))
w('''        <p style="%s">بازهٔ امتیاز کل فهرست باریک است (%s تا %s از ۱۰۰) و این اتفاقی نیست: هر هفتادوپنج مورد را از قبل غربال کرده‌ام. یعنی امتیاز برای <b>مرتب‌کردن</b> خوب است، برای <b>حذف‌کردن</b> نه. شش سنجهٔ هر کارت را بخوان، نه فقط عدد را.</p>
      </div>
      </div>
    </section>''' % (NOTE, fa(min(x['pct'] for x in I)), fa(max(x['pct'] for x in I))))

# ------------------------------------------------------------------ ۰۵ انتخابگر
QS = [('چقدر کد بلدی؟', 'codeChips', 4),
      ('در هفته چقدر وقت داری؟', 'timeChips', 3),
      ('چقدر زود باید پول بدهد؟', 'speedChips', 3),
      ('چه شکل درآمدی می‌خواهی؟', 'pmodelChips', 3),
      ('مشتری‌ات کجاست؟', 'pmarketChips', 3)]
w('''
    <section id="s5" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۵ — انتخابگر</p>
      <h2 style="%s">پنج سؤال، پنج پیشنهاد</h2>
      <p style="%s">فهرست هفتادوپنج‌تایی برای مرور خوب است و برای تصمیم بد. این ابزار همان فهرست را با وضعیت <b>تو</b> می‌سنجد: دو فیلتر سخت (سطح کد و بازار) و چهار امتیاز نرم.</p>
      <p style="%s">نتیجه فوراً عوض می‌شود و زیر هر پیشنهاد نوشته‌ام <b>چرا</b> آمده. اگر دلیلش را قبول نداری، همان جواب را عوض کن.</p>
      <div style="%s padding: 24px 26px; margin-bottom: 16px;">''' % (EYE, H2, LEAD, MUTE, CARD))
for i, (qt, key, cnt) in enumerate(QS):
    w('''        <div style="margin-bottom: 18px;">
          <div style="font-size: 13.5px; font-weight: 700; color: #16181C; margin-bottom: 10px;"><span style="color: %s; margin-inline-end: 6px;">%s</span>%s</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{%s}}" as="c" hint-placeholder-count="%d">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
            </sc-for>
          </div>
        </div>''' % (AC, fa(i + 1), qt, key, cnt))
w('''      </div>

      <sc-if value="{{noPicks}}">
        <div style="%s border-style: dashed; padding: 36px; text-align: center;">
          <p style="font-size: 14.5px; color: #45494F; margin: 0;">با این ترکیب چیزی نماند. سطح کد یا بازار را عوض کن.</p>
        </div>
      </sc-if>

      <div style="display: flex; flex-direction: column; gap: 12px;">
        <sc-for list="{{picks}}" as="p" hint-placeholder-count="5">
          <div style="background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px; padding: 22px 24px; border-inline-start: 4px solid {{p.color}};">
            <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 10px;">
              <span style="font-size: 20px; font-weight: 800; color: %s; line-height: 1;">{{p.rankFa}}</span>
              <h3 style="font-size: 17px; font-weight: 800; margin: 0; line-height: 1.6; color: #16181C;">{{p.fa}}</h3>
              <span style="font-size: 11px; font-weight: 700; color: {{p.color}}; background: {{p.soft}}; border-radius: 999px; padding: 4px 11px; margin-inline-start: auto;">{{p.catName}}</span>
            </div>
            <sc-if value="{{p.hasWhy}}">
              <div style="background: %s; border-radius: 10px; padding: 10px 14px; margin-bottom: 12px;">
                <span style="font-size: 11px; font-weight: 700; color: %s;">چرا این یکی:</span>
                <span style="font-size: 13px; color: #16181C; margin-inline-start: 6px;">{{p.why}}</span>
              </div>
            </sc-if>
            <p style="font-size: 13.5px; line-height: 1.95; color: #16181C; margin: 0 0 10px;">{{p.give}}</p>
            <p style="font-size: 13px; line-height: 1.95; color: #666158; margin: 0 0 12px;">{{p.who}}</p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <span style="font-size: 11.5px; color: #45494F; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 4px 11px;">{{p.diffLab}}</span>
              <span style="font-size: 11.5px; color: #45494F; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 4px 11px;">تقاضا {{p.demLab}}</span>
              <span style="font-size: 11.5px; color: #45494F; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 4px 11px;">رقابت {{p.satLab}}</span>
              <span style="font-size: 11.5px; color: #45494F; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 4px 11px;">{{p.model}}</span>
              <a href="#{{p.id}}" style="font-size: 12px; font-weight: 700; color: %s; margin-inline-start: auto; align-self: center;">دیدن کارت کامل ←</a>
            </div>
          </div>
        </sc-for>
      </div>
      <p style="%s">این ابزار پیش‌گویی نمی‌کند. فقط همان شش عددی را که خودم گذاشته‌ام با جواب‌های تو ترکیب می‌کند. اگر عددهای من را قبول نداری، خروجی این بخش هم به همان اندازه بی‌اعتبار است — و همین درست است.</p>
    </section>''' % (CARD, AC, SOFTAC, AC, AC, NOTE))

# ------------------------------------------------------------------ ۰۶ فهرست
w('''
    <section id="s6" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۶ — فهرست</p>
      <h2 style="%s">هر %s سرویس، با شش سنجه و شش فیلتر</h2>
      <p style="%s">فیلترها با هم کار می‌کنند. چهار پیش‌تنظیم بالا هم میان‌برند: هر کدام را بزنی، بقیهٔ فیلترها صفر می‌شوند و فقط همان شرط می‌ماند.</p>
      <p style="%s">در جست‌وجو، نام سرویس و متن هر چهار بند توضیح (تحویل، خریدار، ابزار، تمایز) جست‌وجو می‌شود. مثلاً بنویس «فروشگاه» یا «کلینیک» یا «اکسل» یا «آرشیو».</p>

      <div style="%s margin-bottom: 18px;">
        <sc-for list="{{presetCards}}" as="p" hint-placeholder-count="4">
          <button style="{{p.style}}" onClick="{{p.onClick}}">
            <div style="{{p.nameStyle}}">{{p.name}}</div>
            <div style="font-size: 12.5px; line-height: 1.8; color: #666158;">{{p.hint}}</div>
            <div style="font-size: 11.5px; font-weight: 700; color: #45494F; margin-top: 8px;">{{p.countFa}} سرویس</div>
          </button>
        </sc-for>
      </div>

      <div style="%s padding: 22px 24px; margin-bottom: 16px;">
        <input id="q" type="search" value="{{q}}" onInput="{{onQ}}" placeholder="جست‌وجو: نام سرویس، صنعت، ابزار یا نوع مشتری…" aria-label="جست‌وجو در سرویس‌ها">

        <div style="margin-top: 18px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">دسته</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{catChips}}" as="c" hint-placeholder-count="11">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}<sc-if value="{{c.hasCount}}"><span style="font-size: 11px; opacity: 0.7;">{{c.count}}</span></sc-if></button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 16px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">سختی فنی</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{diffChips}}" as="c" hint-placeholder-count="4">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 16px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">رقابت</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{satChips}}" as="c" hint-placeholder-count="3">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 16px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">بازار</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{marketChips}}" as="c" hint-placeholder-count="3">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 16px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">مدل درآمد</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{modelChips}}" as="c" hint-placeholder-count="6">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}<sc-if value="{{c.hasCount}}"><span style="font-size: 11px; opacity: 0.7;">{{c.count}}</span></sc-if></button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 16px;">
          <div style="font-size: 11.5px; font-weight: 700; color: #666158; margin-bottom: 10px;">ترتیب</div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{sortChips}}" as="c" hint-placeholder-count="5">
              <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
            </sc-for>
          </div>
        </div>

        <div style="margin-top: 18px; padding-top: 16px; border-top: 1px solid #F0EEE7; display: flex; gap: 12px; flex-wrap: wrap; align-items: center;">
          <span style="font-size: 13px; color: #45494F;"><b>{{countFa}}</b> از {{totalFa}} سرویس</span>
          <sc-if value="{{dirty}}">
            <button style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 999px; padding: 7px 14px; cursor: pointer;" onClick="{{onClear}}">برداشتن همهٔ فیلترها</button>
          </sc-if>
        </div>
      </div>

      <div style="%s padding: 14px 18px; margin-bottom: 16px; font-size: 12.5px; line-height: 1.9; color: #666158;">در نوارهای هر کارت، <b>هرچه نوار بلندتر و سبزتر، برای تو بهتر</b> — یعنی آسان‌تر، پرتقاضاتر، کم‌رقابت‌تر، سریع‌تر، ارزان‌تر و کم‌ریسک‌تر. نارنجی یعنی همان‌جا باید حساب کنی.</div>

      <sc-if value="{{empty}}">
        <div style="%s border-style: dashed; padding: 40px; text-align: center;">
          <p style="font-size: 14.5px; color: #45494F; margin: 0 0 6px;">با این فیلترها چیزی پیدا نشد.</p>
          <p style="font-size: 13px; color: #666158; margin: 0;">فیلترها را بردار یا یک کلمهٔ دیگر امتحان کن.</p>
        </div>
      </sc-if>

      <div style="display: flex; flex-direction: column; gap: 12px;">
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="10">
          <div id="{{r.id}}" style="background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px; padding: 22px 24px; border-inline-start: 3px solid {{r.color}};">

            <div style="display: flex; align-items: baseline; gap: 9px; flex-wrap: wrap; margin-bottom: 12px;">
              <span style="font-size: 11px; font-weight: 700; color: {{r.color}}; background: {{r.soft}}; border-radius: 999px; padding: 4px 11px;">{{r.catName}}</span>
              <span style="font-size: 11px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 3px 10px;">{{r.model}}</span>
              <span style="font-size: 11px; color: #666158; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 3px 10px;">بازار: {{r.market}}</span>
              <span style="font-size: 12px; font-weight: 800; color: #166534; margin-inline-start: auto; font-variant-numeric: tabular-nums;">امتیاز {{r.pctFa}}</span>
            </div>

            <h3 style="font-size: 17.5px; font-weight: 800; margin: 0 0 14px; line-height: 1.6; color: #16181C;">{{r.fa}}</h3>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin-bottom: 16px; padding: 14px 16px; background: #FAFAF7; border: 1px solid #F0EEE7; border-radius: 12px;">
              <sc-for list="{{r.meters}}" as="m" hint-placeholder-count="6">
                <div>
                  <div style="font-size: 11px; color: #666158; margin-bottom: 6px;">{{m.name}}</div>
                  <div style="height: 10px; background: #EDEAE1; border-radius: 6px; overflow: hidden; margin-bottom: 6px;">
                    <div style="{{m.bar}}"></div>
                  </div>
                  <div style="font-size: 12px; font-weight: 700; color: {{m.col}};">{{m.lab}}</div>
                </div>
              </sc-for>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
              <div>
                <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 6px;">چه تحویل می‌دهی</div>
                <p style="font-size: 13.5px; line-height: 1.95; color: #16181C; margin: 0;">{{r.give}}</p>
              </div>
              <div>
                <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 6px;">چه کسی می‌خرد</div>
                <p style="font-size: 13.5px; line-height: 1.95; color: #16181C; margin: 0;">{{r.who}}</p>
              </div>
              <div>
                <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 6px;">چه چیزی لازم داری</div>
                <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">{{r.need}}</p>
              </div>
              <div>
                <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 6px;">چطور قیمت بگذاری</div>
                <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">{{r.price}}</p>
              </div>
            </div>

            <div style="margin-top: 14px; padding: 14px 16px; background: #E3EEE1; border-radius: 12px;">
              <div style="font-size: 11px; font-weight: 700; color: #166534; margin-bottom: 6px;">چطور معمولی نباشی</div>
              <p style="font-size: 13.5px; line-height: 1.95; color: #16181C; margin: 0;">{{r.edge}}</p>
            </div>

          </div>
        </sc-for>
      </div>
      </div>
    </section>''' % (EYE, H2, fa(N), LEAD, MUTE, GRID % (240, 12), CARD, SOFT, CARD))

# ------------------------------------------------------------------ ۰۷ ماشین‌حساب
w('''
    <section id="s7" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۷ — ماشین‌حساب</p>
      <h2 style="%s">این عددها اصلاً جمع می‌شود؟</h2>
      <p style="%s">بیشتر سرویس‌های این فهرست نه به‌خاطر بدبودن ایده، که به‌خاطر <b>حساب‌نکردن</b> شکست می‌خورند: قیمت کم، ساعت زیاد، و در ماه سوم فهمیدن اینکه کار تمام‌وقت شده بدون اینکه درآمد تمام‌وقت باشد.</p>
      <p style="%s">این چهار عدد را عوض کن و ببین چه می‌شود. محاسبه ساده است و عمداً هم ساده مانده: ضرب و تقسیم، بدون فرض پنهان.</p>

      <div style="%s padding: 24px 26px; margin-bottom: 14px;">
        <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; align-items: center;">
          <span style="font-size: 11.5px; font-weight: 700; color: #666158;">واحد</span>
          <sc-for list="{{unitChips}}" as="c" hint-placeholder-count="2">
            <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}</button>
          </sc-for>
        </div>

        <div style="%s">
          <div>
            <label for="cp" style="display: block; font-size: 12.5px; font-weight: 700; color: #45494F; margin-bottom: 8px;">قیمت هر مشتری در ماه</label>
            <input id="cp" type="number" min="0" step="10" value="{{cPrice}}" onInput="{{onPrice}}">
          </div>
          <div>
            <label for="cn" style="display: block; font-size: 12.5px; font-weight: 700; color: #45494F; margin-bottom: 8px;">تعداد مشتری</label>
            <input id="cn" type="number" min="0" step="1" value="{{cN}}" onInput="{{onN}}">
          </div>
          <div>
            <label for="ch" style="display: block; font-size: 12.5px; font-weight: 700; color: #45494F; margin-bottom: 8px;">ساعت کار هر مشتری در ماه</label>
            <input id="ch" type="number" min="0" step="1" value="{{cH}}" onInput="{{onH}}">
          </div>
          <div>
            <label for="ct" style="display: block; font-size: 12.5px; font-weight: 700; color: #45494F; margin-bottom: 8px;">درآمد ماهانهٔ هدف</label>
            <input id="ct" type="number" min="0" step="100" value="{{cTarget}}" onInput="{{onTarget}}">
          </div>
        </div>
      </div>

      <div style="%s margin-bottom: 14px;">
        <div style="%s padding: 22px 24px;">
          <div style="font-size: 12px; color: #666158; margin-bottom: 8px;">درآمد ماهانه</div>
          <div style="font-size: 28px; font-weight: 800; color: %s; line-height: 1.2;">{{m.revFa}}</div>
          <div style="font-size: 12.5px; color: #666158; margin-top: 6px;">{{m.unit}}</div>
        </div>
        <div style="%s padding: 22px 24px;">
          <div style="font-size: 12px; color: #666158; margin-bottom: 8px;">ساعت کار در ماه</div>
          <div style="font-size: 28px; font-weight: 800; color: %s; line-height: 1.2;">{{m.hoursFa}}</div>
          <div style="font-size: 12.5px; color: #666158; margin-top: 6px;">ساعت</div>
        </div>
        <div style="%s padding: 22px 24px;">
          <div style="font-size: 12px; color: #666158; margin-bottom: 8px;">نرخ مؤثر ساعتی</div>
          <div style="font-size: 28px; font-weight: 800; color: %s; line-height: 1.2;">{{m.rateFa}}</div>
          <div style="font-size: 12.5px; color: #666158; margin-top: 6px;">{{m.unit}} در ساعت</div>
        </div>
        <div style="%s padding: 22px 24px;">
          <div style="font-size: 12px; color: #666158; margin-bottom: 8px;">پرشدن ظرفیت یک نفر</div>
          <div style="font-size: 28px; font-weight: 800; color: %s; line-height: 1.2;">{{m.capFa}}٪</div>
          <div style="height: 11px; background: #F0EEE7; border-radius: 7px; overflow: hidden; margin-top: 10px;">
            <div style="{{m.capBar}}"></div>
          </div>
        </div>
      </div>

      <div style="%s padding: 22px 24px;">
        <p style="{{m.verdictStyle}}">{{m.verdict}}</p>
        <sc-if value="{{m.hasReach}}">
          <p style="{{m.reachStyle}}">{{m.reach}}</p>
        </sc-if>
        <p style="%s">فرض‌ها را صریح می‌نویسم: ماه کاری ۱۶۰ ساعت حساب شده، هزینهٔ ابزار و مالیات در این عددها نیست، و «ساعت کار» یعنی ساعت واقعیِ صرف‌شده برای مشتری — نه ساعتی که فاکتور می‌کنی. وقت فروش، حسابداری و پیگیری هم در این عدد نیست و معمولاً یک‌سوم وقت را می‌گیرد.</p>
      </div>
    </section>''' % (EYE, H2, LEAD, MUTE, CARD, GRID % (200, 14), GRID % (190, 12),
                     CARD, AC, CARD, AC, CARD, AC, CARD, AC, CARD, NOTE))

# ------------------------------------------------------------------ ۰۸ ضدفهرست
ANTI = [
    ('قیمتش به صفر می‌رود', '#B4530E', [
        ('فروش پرامپت و بستهٔ پرامپت',
         'به نظر می‌رسد دانش کمیابی است که می‌شود بسته‌بندی کرد.',
         'یک بار فروخته می‌شود و بی‌نهایت بار کپی. ضمناً هر نسخهٔ تازهٔ مدل، نصف پرامپت‌های دیروز را بی‌مصرف می‌کند. در ۲۰۲۳ بازارش ساخته شد و در همان سال خوابید.'),
        ('تولید انبوه مقاله برای سئو، کیلویی',
         'تقاضا هست و تولیدش تقریباً رایگان است.',
         'دقیقاً به همین دلیل: چیزی که تولیدش رایگان است، قیمتش هم به صفر می‌رود. اضافه کن که موتورهای جست‌وجو صریحاً محتوای انبوهِ بی‌ارزش را هدف گرفته‌اند — یعنی ممکن است به مشتری ضرر بزنی.'),
        ('«نوشتن با هوش مصنوعی» به‌عنوان کل سرویس',
         'ساده و قابل فهم است.',
         'تعریف‌نشده است. مشتری نمی‌داند چه می‌خرد و تو نمی‌دانی کی تمام شده. هر سرویسی که نشود در یک جمله گفت «چه چیزی تحویل می‌گیری»، سر قیمت می‌شکند.'),
        ('درآمد کاملاً غیرفعال با اتوماسیون',
         'یک بار بساز، همیشه پول بگیر.',
         'هر اتوماسیونی می‌شکند: رابط‌ها عوض می‌شوند، قیمت‌ها تغییر می‌کنند، مشتری چیز تازه می‌خواهد. نگهداری همیشه هست. بهتر است همان نگهداری را از روز اول بفروشی — در فهرست هم یک ردیف برایش هست.'),
    ]),
    ('مسئولیتش مال توست', '#8A1538', [
        ('تشخیص پزشکی یا توصیهٔ درمانی خودکار',
         'بازار بزرگ است و درد واقعی.',
         'یک خروجی غلط، سلامت یک نفر است. بدون پزشک تأییدکننده و چارچوب قانونی، این سرویس نیست؛ ریسکی است که روی خودت برمی‌داری. نسخهٔ قابل فروشش «دستیار اداری مطب» است، نه تشخیص.'),
        ('مشاورهٔ حقوقی بدون وکیل در حلقه',
         'هزینهٔ وکیل بالاست و تقاضا زیاد.',
         'همان دلیل تقاضا، همان دلیل ریسک است. خلاصه‌کردن قرارداد و پیدا کردن بندهای کلیدی فروختنی است؛ گفتن «این کار را بکن» نه. مرز را در قرارداد بنویس.'),
        ('کپی‌کردن صدا یا چهرهٔ یک نفر بدون اجازهٔ خودش',
         'از نظر فنی امروز آسان شده.',
         'این دیگر مسئلهٔ کیفیت نیست، مسئلهٔ حق یک آدم است. حتی وقتی مشتری اصرار کند، اجازهٔ مکتوب صاحب صدا و چهره را بگیر یا کار را رد کن.'),
        ('تولید نظر، بازخورد یا امتیاز ساختگی',
         'سفارشش زیاد است و پولش خوب.',
         'جعل است، حتی وقتی اسمش را «محتوای تقویتی» بگذارند. پلتفرم‌ها حذفش می‌کنند، مشتری اعتبارش را از دست می‌دهد، و اسم تو به آن وصل می‌ماند.'),
    ]),
    ('مشتری ندارد', '#8A8578', [
        ('«پلتفرم جامع هوش مصنوعی برای همه»',
         'بزرگ و جاه‌طلبانه به نظر می‌رسد.',
         'هیچ‌کس خودش را در «همه» پیدا نمی‌کند. در جلسهٔ اول نمی‌توانی بگویی «مشکل شما این است» و همین، فروش را تمام می‌کند. بزرگ‌فکرکردن اشکالی ندارد؛ بزرگ شروع‌کردن دارد.'),
        ('تضمین رتبهٔ اول یا تضمین فروش',
         'مشتری دقیقاً همین را می‌خواهد بشنود.',
         'چیزی را تضمین می‌کنی که در کنترلت نیست. یک بار که نشود، نه‌تنها پول را پس می‌دهی، اعتبارت را هم می‌دهی. به‌جایش فرایند را تضمین کن و عدد را گزارش بده.'),
    ]),
]
w('''
    <section id="s8" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۸ — ضدفهرست</p>
      <h2 style="%s">ده چیزی که نساز</h2>
      <p style="%s">هر فهرست «چه بساز» بدون فهرست «چه نساز» ناقص است. این ده مورد همان‌هایی‌اند که بیشترین بار پرسیده می‌شوند و بدترین نتیجه را می‌دهند — و برای هرکدام نوشته‌ام <b>چرا جذاب به نظر می‌رسد</b>، چون اگر این را نگویم، یک سال دیگر دوباره جذاب به نظر می‌رسد.</p>
      <p style="%s">سه دلیل متفاوت برای رد کردن وجود دارد و به همین ترتیب دسته‌بندی‌شان کرده‌ام.</p>''' % (EYE, H2, LEAD, MUTE))
for gname, gcol, items in ANTI:
    w('''      <h3 style="font-size: 17px; font-weight: 800; margin: 24px 0 14px; color: %s; display: flex; align-items: center; gap: 10px;"><span style="width: 10px; height: 10px; border-radius: 3px; background: %s; flex-shrink: 0;"></span>%s</h3>
      <div style="%s">''' % (gcol, gcol, gname, GRID % (290, 14)))
    for name, why, fail in items:
        w('''        <div style="%s padding: 22px 24px; border-top: 3px solid %s;">
          <h4 style="font-size: 15px; font-weight: 800; margin: 0 0 12px; line-height: 1.6;">%s</h4>
          <div style="margin-bottom: 12px;">
            <div style="font-size: 11px; font-weight: 700; color: #666158; margin-bottom: 5px;">چرا جذاب به نظر می‌رسد</div>
            <p style="font-size: 13px; line-height: 1.9; color: #45494F; margin: 0;">%s</p>
          </div>
          <div style="padding-top: 12px; border-top: 1px solid #F0EEE7;">
            <div style="font-size: 11px; font-weight: 700; color: %s; margin-bottom: 5px;">چرا نمی‌گیرد</div>
            <p style="font-size: 13.5px; line-height: 1.95; color: #16181C; margin: 0;">%s</p>
          </div>
        </div>''' % (SOFT, gcol, name, why, gcol, fail))
    w('''      </div>''')
w('''      <p style="%s">این فهرست قضاوت من است، نه قانون. دو موردش (کپی صدا و چهره، و نظر ساختگی) اما قضاوت نیست — آن‌ها را اگر کسی پیشنهاد داد، فارغ از قیمت رد کن.</p>
      </div>
    </section>''' % NOTE)

# ------------------------------------------------------------------ ۰۹ ماشین و تو
SPLIT = [
    ('فهمیدن مسئله', 0, 100, 'ماشین نمی‌داند مشتری چه دردی دارد. این را فقط با حرف‌زدن با آدم‌ها می‌فهمی و تمامش کار توست.'),
    ('تصمیم اینکه چه ورودی بدهی', 10, 90, 'مدل هر چیزی بدهی را پردازش می‌کند. اینکه <b>چه چیزی</b> باید بدهی — کدام سند، کدام نمونه، کدام مثال — تصمیم توست.'),
    ('تولید پیش‌نویس', 90, 10, 'این تنها جایی است که ماشین بیشتر کار را می‌کند. و دقیقاً به همین دلیل، این تنها جایی است که نمی‌توانی روی آن قیمت بگذاری.'),
    ('بازبینی و تصحیح', 15, 85, 'ماشین می‌تواند کمک کند، ولی تشخیص اینکه چه چیزی غلط است به دانش زمینه نیاز دارد. این‌جا جایی است که آدم‌های خوب از بقیه جدا می‌شوند.'),
    ('تحویل و توضیح به مشتری', 5, 95, 'جلسه، ایمیل، توضیح اینکه چرا این‌طور شد و چه چیزی عوض شده. هیچ ابزاری این را از تو نمی‌گیرد.'),
    ('پذیرفتن مسئولیت', 0, 100, 'وقتی خروجی غلط باشد، مشتری با تو حرف می‌زند. این صددرصد، همان چیزی است که در واقع می‌فروشی.'),
]
w('''
    <section id="s9" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۰۹ — ماشین و تو</p>
      <h2 style="%s">در هر سرویس، ماشین چه می‌کند و تو چه می‌کنی</h2>
      <p style="%s">این شاید مهم‌ترین تصویر این صفحه باشد. آدم‌ها فکر می‌کنند چون مدل نود درصد نوشتن را انجام می‌دهد، نود درصد کار را انجام داده. ولی نوشتن فقط یکی از شش مرحله است.</p>
      <p style="%s">درصدها تخمین من‌اند از یک پروژهٔ معمول، نه اندازه‌گیری. نسبت‌ها را ببین، نه عددها را.</p>
      <div style="%s">''' % (EYE, H2, LEAD, MUTE, GRID % (290, 14)))
for stage, mach, you, note in SPLIT:
    w('''        <div style="%s padding: 22px 24px;">
          <h3 style="%s">%s</h3>
          <div style="display: flex; height: 14px; border-radius: 7px; overflow: hidden; margin-bottom: 10px; background: #F0EEE7;">
            <div style="width: %d%%; background: #8A8578;"></div>
            <div style="width: %d%%; background: %s;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 700; margin-bottom: 12px;">
            <span style="color: #8A8578;">ماشین %s٪</span>
            <span style="color: %s;">تو %s٪</span>
          </div>
          <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, H3, stage, mach, you, AC, fa(mach), AC, fa(you), note))
w('''      </div>
      <div style="%s padding: 22px 24px; margin-top: 14px;">
        <p style="font-size: 15px; line-height: 2; color: #16181C; margin: 0;">جمعش این است: <b>قیمت سرویس تو روی ستون راست بسته می‌شود، نه ستون چپ.</b> هر وقت دیدی داری سر قیمت می‌جنگی، احتمالاً داری ستون چپ را می‌فروشی.</p>
      </div>
    </section>''' % SOFT)

# ------------------------------------------------------------------ ۱۰ شروع
PATHS = [
    ('مسیر اول: یک سرویس، یک صنعت', 'سی روز',
     [('هفتهٔ ۱', 'یک سرویس از ناحیهٔ «آسان و خالی» بردار و یک صنعت را انتخاب کن که به آن دسترسی داری — جایی که آشنا داری یا قبلاً کار کرده‌ای.'),
      ('هفتهٔ ۲', 'برای <b>سه</b> کسب‌وکار از آن صنعت، خروجی واقعی بساز. رایگان، بدون اینکه بخواهند. فقط بفرست.'),
      ('هفتهٔ ۳', 'با همان سه نفر حرف بزن. نه برای فروش — برای اینکه بفهمی چه چیزی را بد فهمیده بودی. یکی‌شان احتمالاً می‌خرد.'),
      ('هفتهٔ ۴', 'قیمت را ثابت کن، یک قرارداد یک‌صفحه‌ای بنویس، و همان را به ده کسب‌وکار دیگرِ همان صنعت بفرست — با نمونهٔ کار واقعی.')],
     'مناسب کسی که هنوز هیچ مشتری ندارد. کندتر به نظر می‌رسد و سریع‌ترین مسیر است.'),
    ('مسیر دوم: از جایی که از قبل هستی', 'دو هفته',
     [('گام ۱', 'اگر جایی کار می‌کنی یا کرده‌ای، یک فرایند دستی و تکراری همان‌جا را انتخاب کن که خودت از نزدیک دیده‌ای.'),
      ('گام ۲', 'با همان ابزارها اتوماتیکش کن. اول برای خودت، بدون قرارداد.'),
      ('گام ۳', 'عدد بگیر: چند ساعت کم شد؟ چند خطا کم شد؟ همین عدد، کل ارائهٔ فروش بعدی تو است.'),
      ('گام ۴', 'همان را به دو شرکت مشابه بفروش. دانش صنعت را از قبل داری — این بزرگ‌ترین مزیتی است که می‌توانی داشته باشی.')],
     'سریع‌ترین مسیر، اگر تجربهٔ کاری در یک صنعت داری. مزیتش دانش است، نه ابزار.'),
    ('مسیر سوم: آموزش پیش از ساختن', 'یک هفته',
     [('گام ۱', 'یک کارگاه نیم‌روزه برای یک تیم طراحی کن: «هوش مصنوعی در کار روزمرهٔ شما».'),
      ('گام ۲', 'در همان کارگاه، فرایندهای دستی‌شان را فهرست کن. این فهرست از هر تحقیق بازاری ارزشمندتر است.'),
      ('گام ۳', 'در پایان، سه مورد را که می‌توانی اتوماتیک کنی پیشنهاد بده. کارگاه خودش پول داده و تو حالا خریدار داری.')],
     'بالاترین امتیاز فهرست همین است. دلیلش ساده است: هم فوراً پول می‌دهد، هم دقیقاً نشانت می‌دهد بعد چه بسازی.'),
]
SCRIPTS = [
    ('پیام اول، به کسی که نمی‌شناسدت',
     'کوتاه، بدون تعریف و تمجید، و با یک چیز رایگانِ از قبل انجام‌شده.',
     '''سلام [نام].
[یک جملهٔ دقیق که نشان می‌دهد کارشان را دیده‌ای — نه تعریف، مشاهده.]
یک نمونه برایتان درست کردم، بدون اینکه بخواهید: [پیوند یا پیوست].
اگر به‌دردتان خورد، می‌توانم ماهانه همین را انجام بدهم.
اگر نه، همین نمونه مال خودتان.'''),
    ('اسکلت پروپوزال یک‌صفحه‌ای',
     'یک صفحه. بیشتر از این، خوانده نمی‌شود و تصمیم را عقب می‌اندازد.',
     '''۱. مسئله — با کلمات خودِ مشتری، نه کلمات من.
۲. چه چیزی تحویل می‌دهم — قابل شمارش، با نمونه.
۳. چه چیزی تحویل نمی‌دهم — مرز را همین‌جا بنویس.
۴. عددی که با آن سنجیده می‌شود.
۵. قیمت و سقف حجم.
۶. تاریخ شروع و اولین تحویل.'''),
    ('جواب «چقدر می‌گیری؟» در جلسهٔ اول',
     'عدد بده. «بستگی دارد» یعنی هنوز نمی‌دانی چه می‌فروشی.',
     '''برای [تحویل مشخص]، ماهی [عدد].
این شامل [سقف حجم] است؛ بیشتر از آن جدا حساب می‌شود.
اگر بخواهید اول کوچک امتحان کنید، یک دورهٔ دو هفته‌ای با [عدد کمتر] هست
که اگر ادامه دادید، از ماه اول کم می‌شود.'''),
    ('گزارش ماهانه، پنج خط',
     'همین پنج خط است که قرارداد را تمدید می‌کند، نه خودِ کار.',
     '''این ماه: [تعداد] مورد تحویل شد.
عددی که دنبالش بودیم: [قبل] → [بعد].
چه چیزی بهتر شد و چرا.
چه چیزی کار نکرد — یکی را صادقانه بنویس.
ماه بعد پیشنهاد می‌کنم: [یک چیز].'''),
]
w('''
    <section id="s10" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۱۰ — شروع</p>
      <h2 style="%s">سه مسیر برای اینکه از فهرست بیرون بیایی</h2>
      <p style="%s">فهرست خواندن آسان است و شروع‌کردن سخت. این سه مسیر را طوری نوشته‌ام که هیچ‌کدام به سرمایه یا اجازهٔ کسی نیاز نداشته باشد.</p>
      <p style="%s">یک چیز در هر سه مشترک است و اتفاقی نیست: <b>اول خروجی، بعد فروش.</b> هیچ‌کدام با «ساختن سایت و لوگو» شروع نمی‌شود.</p>
      <div style="%s">''' % (EYE, H2, LEAD, MUTE, GRID % (300, 14)))
for title, dur, steps, note in PATHS:
    w('''        <div style="%s padding: 24px 26px;">
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px; flex-wrap: wrap;">
            <h3 style="font-size: 16px; font-weight: 800; margin: 0; line-height: 1.55;">%s</h3>
            <span style="font-size: 11px; font-weight: 700; color: %s; background: %s; border-radius: 999px; padding: 4px 11px; flex-shrink: 0; margin-inline-start: auto;">%s</span>
          </div>''' % (SOFT, title, AC, SOFTAC, dur))
    for lab, body in steps:
        w('''          <div style="display: flex; gap: 11px; align-items: stretch; margin-bottom: 12px;">
            <div style="flex-shrink: 0; width: 52px; font-size: 11px; font-weight: 700; color: %s; padding-top: 2px;">%s</div>
            <div style="flex: 1; min-width: 0; padding-inline-start: 13px; border-inline-start: 2px solid #EDEAE1; font-size: 13.5px; line-height: 1.95; color: #45494F;">%s</div>
          </div>''' % (AC, lab, body))
    w('''          <p style="%s">%s</p>
        </div>''' % (NOTE, note))
w('''      </div>

      <h3 style="font-size: 18px; font-weight: 800; margin: 30px 0 8px;">چهار متنی که لازمت می‌شود</h3>
      <p style="font-size: 13.5px; line-height: 1.9; color: #666158; margin: 0 0 18px; max-width: 70ch;">این‌ها را گذاشتم چون در عمل، آدم‌ها سر همین چهار جمله گیر می‌کنند، نه سر کار فنی. قلاب‌ها را با مال خودت پر کن و بقیه را دست نزن — کوتاهی‌شان عمدی است.</p>
      <div style="%s">''' % (GRID % (290, 14)))
for title, note, body in SCRIPTS:
    w('''        <div style="%s padding: 22px 24px; border-top: 3px solid %s;">
          <h4 style="font-size: 15px; font-weight: 800; margin: 0 0 7px; line-height: 1.6;">%s</h4>
          <p style="font-size: 12.5px; line-height: 1.9; color: #666158; margin: 0 0 14px;">%s</p>
          <div style="background: #FAFAF7; border: 1px solid #EDEAE1; border-radius: 12px; padding: 16px 18px; font-size: 13px; line-height: 2.1; color: #16181C; white-space: pre-wrap; overflow-wrap: anywhere;">%s</div>
        </div>''' % (CARD, AC, title, note, body))
w('''      </div>
      </div>
    </section>''')

# ------------------------------------------------------------------ ۱۱ قیمت
PRICE = [
    ('ساعتی نفروش — مگر برای مشاوره',
     'وقتی ساعتی می‌فروشی، هرچه بهتر و سریع‌تر شوی کمتر می‌گیری. این دقیقاً خلاف جهت ابزاری است که داری استفاده می‌کنی. ساعتی را فقط برای منتورینگ و مشاوره نگه دار، جایی که خودِ وقتِ تو محصول است.'),
    ('بر اساس نتیجه قیمت بگذار، نه بر اساس زحمت',
     'مشتری نمی‌داند و برایش مهم نیست که کار تو ده دقیقه طول کشیده یا ده ساعت. مهم است که چه چیزی برایش عوض شد. «ماهی ده قطعه محتوای آمادهٔ انتشار» قیمت دارد؛ «چند ساعت کار با مدل» ندارد.'),
    ('سه پله بساز، وسطی را بفروش',
     'یک بستهٔ پایه، یک وسط و یک بالا. اکثر مشتری‌ها وسطی را می‌گیرند و وجود بستهٔ بالا باعث می‌شود وسطی منطقی به نظر برسد. بستهٔ پایه برای این است که «نه» گفتن سخت شود.'),
    ('هزینهٔ مصرف را جدا کن',
     'هزینهٔ مدل، ابزار و زیرساخت را از حق‌الزحمهٔ خودت جدا نگه دار — چه در فاکتور، چه در ذهن خودت. قیمت این ابزارها تغییر می‌کند و نباید هر بار قرارداد تو را به هم بزند.'),
    ('پایلوت کوتاه و پول‌دار، نه رایگان بی‌انتها',
     'یک پایلوت دو هفته‌ای با مبلغ کم بفروش، نه نمونهٔ رایگان نامحدود. کسی که برای پایلوت پول داده، برای قرارداد هم پول می‌دهد؛ کسی که رایگان گرفته، معمولاً فقط کنجکاو بوده.'),
    ('سقف را خودت تعیین کن',
     'در قرارداد ماهانه بنویس تا چه حجمی شامل است و از آن به بعد چه. بی این بند، سرویس ماهانهٔ سودآور در ماه سوم تبدیل به کار تمام‌وقت بی‌مزد می‌شود. این رایج‌ترین اشتباه این نوع قراردادهاست — و ماشین‌حساب بخش ۰۷ دقیقاً همین را نشان می‌دهد.'),
]
w('''
    <section id="s11" style="max-width: 1120px; margin: 0 auto; padding: 46px 24px 10px;">
      <p style="%s">۱۱ — قیمت</p>
      <h2 style="%s">شش قاعدهٔ قیمت‌گذاری</h2>
      <p style="%s">این بخش را جدا نوشته‌ام چون در عمل، قیمت‌گذاری بیشتر از انتخاب سرویس تعیین می‌کند کار دوام می‌آورد یا نه.</p>
      <div style="%s">''' % (EYE, H2, LEAD, GRID % (290, 14)))
for i, (t, d) in enumerate(PRICE):
    w('''        <div style="%s padding: 22px 24px;">
          <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 8px;">%s</div>
          <h3 style="%s">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (CARD, AC, fa('%02d' % (i + 1)), H3, t, d))
w('''      </div>
    </section>''')

# ------------------------------------------------------------------ ۱۲ محدودیت
w('''
    <section id="s12" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۱۲ — محدودیت</p>
      <h2 style="%s">یک واقعیت که باید سرِ جایش نوشته شود</h2>
      <p style="%s">این فهرست برای کسی نوشته شده که ممکن است در ایران باشد. پس بی‌تعارف: چند تا از این سرویس‌ها به دسترسی مستقیم به سکوی هوش مصنوعی وابسته‌اند، و آن دسترسی از ایران رسمی نیست.</p>
      <p style="%s">این را به‌عنوان یک بند برنامه‌ریزی می‌نویسم، نه نصیحت. اگر بدانی کدام بخش کار به دسترسی وابسته است و کدام بخش نیست، تصمیم بهتری می‌گیری.</p>
      <div style="%s padding: 24px 26px; margin-bottom: 14px;">
        <h3 style="%s">آنچه در سند رسمی نوشته شده</h3>
        <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0 0 12px;">صفحهٔ «کشورها و مناطق پشتیبانی‌شده»ی انتروپیک یک فهرست دارد و یک جملهٔ صریح: هر کشوری که در فهرست نیست، پشتیبانی نمی‌شود. ایران در آن فهرست نیست. عراق و ترکیه هستند.</p>
        <p style="%s" dir="ltr">Anthropic — Supported countries and regions · “Any country or region not listed is unsupported.”</p>
        <p style="font-size: 12px; line-height: 1.9; color: #666158; margin: 12px 0 0;">آخرین بازبینی این صفحه: ۱۸ مهر ۱۴۰۵ / ۱۰ اکتبر ۲۰۲۶. این فهرست‌ها تغییر می‌کنند؛ قبل از هر تصمیمی خودت نگاهش کن.</p>
      </div>''' % (EYE, H2, LEAD, MUTE, SOFT, H3,
                   LTR + ' font-size: 13px; line-height: 1.8; color: #16181C; background: #FFFFFF; border: 1px solid #F0EEE7; border-radius: 10px; padding: 12px 14px; margin: 0;'))

IRAN = [
    ('چه چیزی وابسته به دسترسی است',
     'سرویس‌هایی که قلبشان یک مدل همیشه‌روشن است — چت‌بات، منشی تلفنی، دستیار داخلی — به دسترسی پایدار و قابل اتکا نیاز دارند. اگر دسترسی تو شکننده باشد، سرویسی که به مشتری فروخته‌ای هم شکننده است؛ و این دیگر مشکل فنی نیست، مشکل اعتبار است.'),
    ('چه چیزی وابسته نیست',
     'بخش گران هر کدام از این %s سرویس، مدل نیست: شناخت صنعت، تشخیص اینکه چه چیزی ارزش اتوماتیک‌شدن دارد، بازبینی خروجی و پذیرفتن مسئولیتش. بخش ۰۹ همین را عدد کرده — و هیچ فهرست کشوری آن ستون را محدود نمی‌کند.' % fa(N)),
    ('پول، سخت‌تر از محصول است',
     'برای فروش به بیرون، گره اصلی معمولاً ساختن سرویس نیست؛ گرفتن پول است. سامانهٔ پرداخت، فاکتور و هویت حقوقی تعیین می‌کنند چه چیزی عملی است. قبل از ساختن، این را حل کن — نه بعد از پیدا کردن اولین مشتری.'),
    ('بازار داخلی، بازار واقعی',
     'از این %s سرویس، %s تا در هر دو بازار فروش می‌رود، %s تا عملاً فقط داخلی است و %s تا فقط جهانی. یعنی بخش بزرگ فهرست، همین‌جا هم خریدار دارد — با قیمت کمتر و رقابت کمتر.' % (fa(N), fa(BOTH), fa(DOMONLY), fa(GLOBONLY))),
    ('شکاف فارسی، یک مزیت است',
     'کیفیت خروجی فارسی مدل‌ها هنوز به‌مراتب از انگلیسی پایین‌تر است — در ترجمه، زیرنویس، لحن و اصطلاح تخصصی. هر جایی که ماشین بد کار می‌کند، جایی است که کار انسانی قیمت دارد. دستهٔ «صدا و گفتار» دقیقاً به همین دلیل در این فهرست کم‌رقابت است.'),
    ('سرویسی نساز که وعده‌اش «دسترسی» باشد',
     'اگر کل ارزش پیشنهادی تو این باشد که «من دسترسی دارم و تو نداری»، کسب‌وکارت روی چیزی بنا شده که فردا می‌تواند عوض شود. وعده را بگذار روی چیزی که مال خودت است: قضاوت، سرعت، و اینکه پشت خروجی می‌ایستی.'),
]
w('''      <div style="%s">''' % (GRID % (290, 14)))
for t, d in IRAN:
    w('''        <div style="%s padding: 22px 24px;">
          <h3 style="%s">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (SOFT, H3, t, d))
w('''      </div>
      </div>
    </section>''')

# ------------------------------------------------------------------ ۱۳ روش و منابع
METHOD = [
    ('شش سنجه از کجا آمده',
     'تقاضا و رقابت را از ترکیب گزارش‌های بازار و آگهی‌های واقعی کار برآورد کرده‌ام. سختی فنی، سرعت رسیدن به درآمد، سرمایهٔ اولیه و ریسک <b>قضاوت من</b> است، نه اندازه‌گیری. هیچ‌کدام از این شش عدد را از یک نظرسنجی بیرون نکشیده‌ام و وانمود نمی‌کنم که دقیق‌اند — برای مقایسهٔ نسبی ساخته شده‌اند، نه برای استناد.'),
    ('چرا تقاضای همه بالاست',
     'چون فهرست از اول غربال شده. سؤال این بود «چه چیزی پرتقاضا و شدنی است»، پس هر چیزی که تقاضای کم داشت وارد فهرست نشد. نتیجه‌اش این است که ستون تقاضا تفکیک‌کننده نیست و بازهٔ امتیاز باریک است. این عیب داده نیست؛ نتیجهٔ مستقیم صورت سؤال است.'),
    ('امتیاز و انتخابگر را جدی نگیر',
     'فرمول امتیاز را نوشته‌ام تا بتوانی با آن مخالفت کنی. تقاضا را ضرب در دو کرده‌ام چون به نظرم مهم‌ترین سنجه است — ولی این یک انتخاب است، نه یک کشف. انتخابگر بخش ۰۵ هم روی همین عددها سوار است: اگر عددها را قبول نداری، خروجی‌اش هم بی‌اعتبار است.'),
    ('ماشین‌حساب چه چیزی را حساب نمی‌کند',
     'هزینهٔ ابزار، مالیات، وقت فروش و پیگیری، و ماه‌هایی که یک مشتری می‌رود و جایش خالی می‌ماند. ماه کاری را ۱۶۰ ساعت گرفته‌ام. این ماشین‌حساب برای این است که زود بفهمی یک ترکیب <b>جمع نمی‌شود</b>، نه برای اینکه ثابت کند جمع می‌شود.'),
    ('قیمت‌ها لنگرند، نه نرخ‌نامه',
     'عددهای دلاری از نرخ‌نامه‌های خودگزارش‌شده و صفحه‌های قیمت فروشندگان می‌آیند — یعنی سمت بالای بازار را نشان می‌دهند، نه میانه را. برای بازار داخلی هیچ عدد قابل اتکایی پیدا نکردم و عمداً عددی از خودم نساختم.'),
    ('چه چیزی این‌جا نیست',
     'هر چیزی که به سرمایهٔ جدی، تیم، یا مجوز نیاز دارد. همچنین هر چیزی که «محصول» باشد نه «سرویس» — ساختن اپلیکیشن و فروش اشتراک، بازی دیگری است با ریسک دیگری. و هیچ‌چیزی که وعدهٔ درآمد بدون کار بدهد؛ ده موردِ بخش ۰۸ همان‌هایی‌اند که عمداً بیرون گذاشته شده‌اند.'),
    ('خط زمان بخش ۰۳',
     'تاریخ‌ها رویدادهای عمومی و قابل بررسی‌اند. ولی ستون «چه چیزی واقعاً فروخته می‌شد» تفسیر من است از آنچه در هر دوره بازار داشت. اگر دورهٔ دیگری را از نزدیک دیده‌ای و روایتت فرق می‌کند، احتمالاً حق با توست.'),
    ('سوگیری‌هایی که می‌دانم',
     'یک: فهرست به سمت کارهای از-راه-دور و پروژه‌ای سوگیری دارد، چون داده‌های بازار کار آزاد همین‌جا شفاف‌ترند. دو: به سمت کسب‌وکارهای کوچک و متوسط سوگیری دارد. سه: چیزی که امروز «کم‌رقابت» است، تا دو سال دیگر می‌تواند اشباع شود — بخش ۰۳ نشان می‌دهد این دقیقاً همان چیزی است که تا حالا هر بار اتفاق افتاده.'),
]
SOURCES = [
    ('گزارش مهارت‌های پرتقاضای ۲۰۲۶، آپورک', 'Upwork — In-Demand Skills 2026 (published February 2026)',
     'https://www.upwork.com/research', 'منبع همهٔ درصدهای رشد در بخش ۰۲. داده‌اش از آگهی‌های کار همان سکو است.'),
    ('نظرسنجی روند و چشم‌انداز کسب‌وکارها، سرشماری آمریکا', 'U.S. Census Bureau — Business Trends and Outlook Survey (BTOS)',
     'https://www.census.gov/hfp/btos/', 'تنها منبع دولتی و دوهفته‌ای دربارهٔ به‌کارگیری واقعی هوش مصنوعی در بنگاه‌ها. عدد «در تولید واقعی» از این‌جاست.'),
    ('گزارش فناوری و کسب‌وکار کوچک، اتاق بازرگانی آمریکا', 'U.S. Chamber of Commerce — Technology and small business research',
     'https://www.uschamber.com/technology', 'منبع عدد ۵۸٪. تعریف «استفاده» در این نظرسنجی گسترده است و باید با همین احتیاط خواند.'),
    ('کشورها و مناطق پشتیبانی‌شده، انتروپیک', 'Anthropic — Supported countries and regions',
     'https://www.anthropic.com/supported-countries', 'سند رسمی بخش ۱۲. در ۱۸ مهر ۱۴۰۵ خودم بازش کردم و بررسی کردم.'),
    ('نرخ‌نامهٔ خودگزارش‌شدهٔ سازندگان اتوماسیون', 'Self-reported automation rate card (54 respondents)',
     '', 'بازهٔ ۹۵ تا ۲۳۵ دلار ساعتی و عددهای پروژه از این‌جاست. نمونهٔ کوچک و خودگزارش‌شده — آمار نیست، لنگر است.'),
    ('صفحه‌های قیمت فروشندگان منشی تلفنی هوشمند', 'Vendor pricing pages, AI phone receptionist services',
     '', 'عدد ۹۹ تا ۲۹۹ دلار ماهانه و ۰٫۱۵ تا ۰٫۲۵ دلار بر دقیقه. این‌ها ادعای فروشنده‌اند، نه قیمت تمام‌شدهٔ مستقل.'),
]
w('''
    <section id="s13" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۱۳ — روش و منابع</p>
      <h2 style="%s">این فهرست چطور ساخته شد و کجا ضعیف است</h2>
      <p style="%s">هر فهرستی از این جنس، پشتش قضاوت است. ترجیح می‌دهم قضاوت‌هایم را بنویسم تا بتوانی ردشان کنی.</p>
      <div style="%s margin-bottom: 26px;">''' % (EYE, H2, LEAD, GRID % (290, 14)))
for t, d in METHOD:
    w('''        <div style="%s padding: 22px 24px;">
          <h3 style="%s">%s</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (SOFT, H3, t, d))
w('''      </div>

      <h3 style="font-size: 18px; font-weight: 800; margin: 0 0 8px;">منابع</h3>
      <p style="font-size: 13.5px; line-height: 1.9; color: #666158; margin: 0 0 18px; max-width: 70ch;">شش منبع، و برای هر کدام نوشته‌ام چه چیزی از آن برداشته‌ام و چقدر می‌شود به آن تکیه کرد. دو تای آخر عمداً بی‌پیوندند، چون ادعای فروشنده و خودگزارش‌شده‌اند و نمی‌خواهم با پیوند، اعتبارِ نداشته به آن‌ها بدهم.</p>
      <div style="display: flex; flex-direction: column; gap: 10px;">''')
for i, (fat, ent, url, note) in enumerate(SOURCES):
    w('''        <div style="%s padding: 20px 22px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
            <span style="font-size: 12px; font-weight: 700; color: %s;">%s</span>
            <h4 style="font-size: 14.5px; font-weight: 700; margin: 0; line-height: 1.6;">%s</h4>
          </div>
          <p style="%s font-size: 12.5px; line-height: 1.8; color: #45494F; margin: 0 0 9px;">%s</p>
          <p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0;">%s</p>''' % (
        SOFT, AC, fa('%02d' % (i + 1)), fat, LTR, ent, note))
    if url:
        w('''          <p style="margin: 9px 0 0;"><a href="%s" target="_blank" rel="noopener" style="font-size: 12px; font-weight: 700; color: %s; %s">%s ←</a></p>''' % (url, AC, LTR, url))
    w('''        </div>''')
w('''      </div>

      <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 26px 0 18px; max-width: 70ch;">و یک تشکر: بخش زیادی از آنچه در این صفحه «قاعده» نامیده‌ام، از خواندن کار کسانی آمده که سال‌ها پیش از این موج، دربارهٔ خدمات‌فروشی و قیمت‌گذاری نوشتند. هر جا توانستم به منبع برگردم، برگشتم؛ هر جا نتوانستم، به‌جای جعل ارجاع، همان را قضاوت خودم نوشتم.</p>

      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="AILiteracy.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">معماری سواد هوش مصنوعی ←</a>
        <a href="Library.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">کتابخانهٔ منابع سایت ←</a>
        <a href="Ideas.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 22px; border-radius: 10px;">صد ایدهٔ یادگیری ماشین ←</a>
      </div>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid #E4E1D6; background: #FFFFFF;">
    <div style="max-width: 1120px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: #666158;">رضا هاشمی · هفتادوپنج در</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1120,"height":1600}}'>
''' + L.LOGIC.strip() + '''
</script>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'Services.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars ·', N, 'services ·', len(NAV), 'sections')
