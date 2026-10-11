# -*- coding: utf-8 -*-
"""«ریاضی، از راهِ شکستن» → src/Foundations.dc.html

ایدهٔ صفحه: مدرسه ریاضی را مثل ساختمانی تمام‌شده نشان می‌دهد. ولی این
ساختمان با شکستن ساخته شده — هر مفهوم تازه وقتی آمد که چیزی از کار افتاد،
و هر تعمیری بهایی داشت. همان بها چیزی است که هیچ‌جا گفته نمی‌شود.
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from paths import SRC  # noqa: E402
import logic as L  # noqa: E402

V = dict(
    AC='#4C3575',          # بنفشِ عمیق
    SOFT='#EDE6F6',
    INK='#16181C',
    MID='#45494F',
    DIM='#666158',
    LINE='#E4E1D6',
    RUST='#B4530E',
    GREEN='#2F5233',
)
V['LTR'] = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
V['EYE'] = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %(AC)s; margin: 0 0 12px;' % V
V['H2'] = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 16px; line-height: 1.45;'
V['H3'] = 'font-size: 16px; font-weight: 800; margin: 0 0 10px; line-height: 1.6;'
V['BODY'] = 'font-size: 16px; line-height: 2.12; color: %(MID)s; max-width: 66ch; margin: 0 0 17px;' % V
V['LEAD'] = 'font-size: 17.5px; line-height: 2.08; color: %(MID)s; max-width: 64ch; margin: 0 0 17px;' % V
V['SOFTC'] = 'background: #FAFAF7; border: 1px solid %(LINE)s; border-radius: 14px;' % V
V['CARD'] = 'background: #FFFFFF; border: 1px solid %(LINE)s; border-radius: 16px;' % V

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))

o = []
def w(s, **extra):
    vals = dict(V); vals.update(extra)
    o.append(s % vals if '%(' in s else s)

NAV = [('s1', '۰۱ چرا نفهمیدی'), ('s2', '۰۲ قاعدهٔ بازی'), ('s3', '۰۳ نردبان عدد'),
       ('s4', '۰۴ بی‌نهایت'), ('s5', '۰۵ فضا'), ('s6', '۰۶ قطعیت'),
       ('s7', '۰۷ اصل موضوع'), ('s8', '۰۸ اثبات'), ('s9', '۰۹ سه حرکت'),
       ('s10', '۱۰ نقشهٔ شاخه‌ها'), ('s11', '۱۱ چطور یاد بگیری'), ('s12', '۱۲ روش')]

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>ریاضی، از راهِ شکستن — مبانی و مفاهیم پایه</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&amp;display=swap">
<style>
  body{margin:0;font-family:'Vazirmatn',system-ui,sans-serif;background:#F6F4F2;color:#16181C;-webkit-font-smoothing:antialiased}
  a{color:#4C3575;text-decoration:none}
  a:hover{text-decoration:underline}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  b,strong{font-weight:700;color:#16181C}
  ::selection{background:#EDE6F6;color:#4C3575}
  @media (max-width:860px){
    nav[data-sections]{display:none !important}
    div[data-sectionlist]{display:flex !important}
  }
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F6F4F2; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(246,244,242,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1060px; margin: 0 auto; padding: 12px 24px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <nav data-sections="1" style="display: flex; gap: 1px; margin-inline-start: auto; flex-wrap: wrap;">''')
for sid, lab in NAV:
    w('        <a href="#%(sid)s" style="font-size: 11.5px; color: #45494F; padding: 5px 7px; border-radius: 999px;">%(lab)s</a>',
      sid=sid, lab=lab)
w('''      </nav>
    </div>
  </header>

  <main>

    <section style="max-width: 1060px; margin: 0 auto; padding: 56px 24px 26px;">
      <p style="%(EYE)s">مبانی ریاضی · از راهی که کسی نشانت نداده</p>
      <h1 style="font-size: clamp(30px, 4.6vw, 48px); font-weight: 800; margin: 0 0 20px; line-height: 1.35; letter-spacing: -0.01em;">ریاضی، از راهِ شکستن</h1>
      <p style="%(LEAD)s">در مدرسه ریاضی را مثل ساختمانی تمام‌شده نشانت دادند: این تعریف، این قاعده، حالا صد تا تمرین. و تو هیچ‌وقت نفهمیدی این قاعده‌ها <b>از کجا آمدند</b> و چرا کسی باید به فکرشان می‌افتاد.</p>
      <p style="%(BODY)s">این صفحه از راه دیگری می‌رود. هر مفهومِ بزرگِ ریاضی وقتی به دنیا آمد که <b>چیزی از کار افتاد</b> — مسئله‌ای که قاعده‌های موجود نمی‌توانستند حلش کنند. و هر تعمیری، بهایی داشت: چیزی به دست آمد و چیزی از دست رفت.</p>
      <p style="%(BODY)s">آن <b>بها</b> چیزی است که تقریباً هیچ‌جا گفته نمی‌شود. و دقیقاً همان است که مفهوم را از یک قاعدهٔ دلبخواهی به یک تصمیمِ ناگزیر تبدیل می‌کند.</p>
''')

w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-top: 26px; max-width: 780px;">''')
for num, lab in [('۶', 'پلهٔ عدد'), ('۴', 'شکستِ بزرگ'), ('۲', 'ابزار تعاملی'), ('۱۲', 'بخش')]:
    w('''        <div style="%(SOFTC)s padding: 18px 20px;">
          <div style="font-size: 26px; font-weight: 800; color: %(AC)s; line-height: 1.2;">%(n)s</div>
          <div style="font-size: 12.5px; color: %(DIM)s; margin-top: 4px;">%(l)s</div>
        </div>''', n=num, l=lab)
w('      </div>')
w('      <div data-sectionlist="1" style="display: none; gap: 6px; flex-wrap: wrap; margin-top: 24px;">')
for sid, lab in NAV:
    w('        <a href="#%(sid)s" style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 7px 12px; border-radius: 999px;">%(lab)s</a>',
      sid=sid, lab=lab)
w('      </div>\n    </section>\n')


def sec(sid, eyebrow, title, white=False):
    bg = '#FFFFFF' if white else 'transparent'
    bd = ('border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s;' % V) if white else ''
    w('''
    <section id="%(sid)s" style="background: %(bg)s; %(bd)s margin-top: 38px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">%(eye)s</p>
      <h2 style="%(H2)s">%(title)s</h2>''', sid=sid, bg=bg, bd=bd, eye=eyebrow, title=title)


def endsec():
    w('      </div>\n    </section>\n')


def p(t):
    w('      <p style="%(BODY)s">%(t)s</p>', t=t)


def box(label, t, color=None, soft=None):
    w('''      <div style="background: %(bg)s; border-inline-start: 4px solid %(c)s; border-radius: 13px; padding: 17px 20px; margin: 0 0 20px; max-width: 72ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(c)s; margin-bottom: 9px;">%(l)s</div>
        <p style="font-size: 14.5px; line-height: 2.08; color: %(MID)s; margin: 0;">%(t)s</p>
      </div>''', c=(color or V['AC']), bg=(soft or V['SOFT']), l=label, t=t)


def dash(label, t):
    w('''      <div style="border: 1px dashed #D5CEDF; border-radius: 13px; padding: 16px 19px; margin: 0 0 20px; max-width: 72ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(RUST)s; margin-bottom: 9px;">%(l)s</div>
        <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 0;">%(t)s</p>
      </div>''', l=label, t=t)


# ------------------------------------------------------------------ ۰۱
sec('s1', '۰۱ — تشخیص', 'چرا ریاضی برایت بی‌معنا ماند، و تقصیر تو نبود')
p('یک تجربهٔ فکری: فرض کن موسیقی را این‌طور درس می‌دادند. ده سال نت‌خوانی. قاعده‌های هارمونی. امتحانِ تشخیصِ فاصله‌ها. و <b>هیچ‌وقت سازی در دست نگیری و هیچ‌وقت آهنگی نشنوی</b>. بعد در پانزده‌سالگی به خودت بگویی «من ذوق موسیقی ندارم».')
p('این دقیقاً بلایی است که سر ریاضی آمده. چیزی که در مدرسه خواندی <b>حسابِ سریع</b> بود، نه ریاضی. ریاضی‌دان‌ها همان‌قدر وقت صرف حساب‌کردن می‌کنند که نویسنده‌ها صرف غلط‌گیری املایی.')
box('شکایتی که معلمِ ریاضی نوشت',
    'پل لاکهارت، معلم ریاضی، در جستاری به نام «شکایتِ یک ریاضی‌دان» همین را گفت: '
    'دانش‌آموز یاد می‌گیرد استدلال‌ها را <b>تقلید</b> کند، نه اینکه خودش قصدِ اثبات کند. '
    'تعریف و اثباتِ کتاب روی تخته کپی می‌شود، از تخته در دفتر، و بعد در تمرین‌ها تکرار. '
    'دانش‌آموز در کارِ خلاقانه‌ای که اسمش ریاضی است، تماشاچی است.')
p('پس سؤال درست این نیست که «چطور در ریاضی بهتر شوم». سؤال این است: <b>آن کارِ خلاقانه چه بود که هیچ‌وقت ندیدی؟</b>')
p('جوابش در بخش بعد است، و بقیهٔ این صفحه تمرینِ همان است.')
endsec()

# ------------------------------------------------------------------ ۰۲
sec('s2', '۰۲ — قاعدهٔ بازی', 'هیچ مفهومی در ریاضی مجانی نیامده', white=True)
p('این کلِ ایدهٔ این صفحه است و در یک جمله جا می‌شود:')
w('''      <p style="font-size: 20px; line-height: 1.95; font-weight: 700; color: %(AC)s; max-width: 60ch; margin: 0 0 22px; padding: 20px 24px; background: %(SOFT)s; border-radius: 14px;">هر مفهومِ تازهٔ ریاضی وقتی ساخته شد که چیزی شکست. و هر تعمیری، چیزی را که داشتی از تو گرفت.</p>''')
p('مدرسه نیمهٔ اول را می‌گوید (گاهی) و نیمهٔ دوم را هرگز. ولی نیمهٔ دوم همان چیزی است که مفهوم را فهمیدنی می‌کند. وقتی بدانی چه چیزی را از دست داده‌ای، می‌فهمی چرا کسی حاضر شده این معامله را بکند.')
p('و یک چیز دیگر: تقریباً هر مفهومی که امروز بدیهی به نظر می‌رسد، روزی <b>رسوایی</b> بود. منفی مزخرف بود. گنگ راز بود. موهومی تحقیر بود. بی‌نهایت بیماری بود. هندسهٔ غیراقلیدسی مسخره بود. هیچ‌کدام از این‌ها با آغوش باز وارد نشدند.')
w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin: 22px 0 0;">''')
for t, d in [
    ('۱. چه چیزی شکست', 'مسئله‌ای پیدا شد که قاعده‌های موجود جوابش را نمی‌دادند. '
     'نه «سخت» بود — اصلاً در آن دستگاه معنا نداشت.'),
    ('۲. چه چیزی ساخته شد', 'کسی چیزِ تازه‌ای تعریف کرد که آن در را باز می‌کرد. '
     'معمولاً بقیه مسخره‌اش کردند.'),
    ('۳. چه چیزی از دست رفت', 'دستگاهِ تازه یک خاصیتِ دستگاهِ قدیم را نداشت. '
     'این بخشِ پنهانِ معامله است.'),
]:
    w('''        <div style="%(SOFTC)s padding: 20px 22px;">
          <h3 style="%(H3)s color: %(AC)s;">%(t)s</h3>
          <p style="font-size: 13.5px; line-height: 2; color: %(MID)s; margin: 0;">%(d)s</p>
        </div>''', t=t, d=d)
w('      </div>')
endsec()

# ------------------------------------------------------------------ ۰۳ نردبان (تعاملی)
sec('s3', '۰۳ — نردبان عدد', 'شش پله، و خاصیتی که در هر پله از دست می‌رود')
p('این نردبان را خودت بالا برو. روی هر پله کلیک کن و <b>جدولِ پایینش</b> را نگاه کن: تیک‌ها یکی‌یکی به ضربدر تبدیل می‌شوند. این جدول، دقیقاً همان چیزی است که هیچ‌وقت نشانت ندادند.')

w('''
      <div style="%(CARD)s padding: 24px 26px; margin: 0 0 22px;">
        <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 22px;">
          <sc-for list="{{rungBtns}}" as="b" hint-placeholder-count="6">
            <button style="{{b.style}}" onClick="{{b.onClick}}">{{b.label}}</button>
          </sc-for>
        </div>

        <div style="display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; margin-bottom: 6px;">
          <span style="font-size: 38px; font-weight: 800; color: %(AC)s; line-height: 1;">{{sym}}</span>
          <span style="font-size: 20px; font-weight: 800; color: %(INK)s;">عددهای {{rname}}</span>
          <span style="%(LTR)s font-size: 14px; color: %(DIM)s;">{{rfa}}</span>
        </div>
        <p style="font-size: 12.5px; color: %(DIM)s; margin: 0 0 20px;">{{keptFa}} خاصیت از {{totalFa}} تا هنوز سر جایش است</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 13px; margin-bottom: 20px;">
          <div style="background: #FAFAF7; border-radius: 13px; padding: 18px 20px;">
            <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(RUST)s; margin-bottom: 9px;">چه چیزی شکست</div>
            <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 0;">{{broke}}</p>
          </div>
          <div style="background: #F1F6EF; border-radius: 13px; padding: 18px 20px;">
            <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(GREEN)s; margin-bottom: 9px;">چه چیزی به دست آمد</div>
            <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 0;">{{gain}}</p>
          </div>
          <div style="background: #F7E3D6; border-radius: 13px; padding: 18px 20px;">
            <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(RUST)s; margin-bottom: 9px;">چه چیزی از دست رفت</div>
            <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 0;">{{loss}}</p>
          </div>
          <div style="background: %(SOFT)s; border-radius: 13px; padding: 18px 20px;">
            <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 9px;">کِی و کجا</div>
            <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 0;">{{when}}</p>
          </div>
        </div>

        <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0 0 20px; padding: 15px 18px; background: #FAFAF7; border-radius: 12px;"><b>یک مثالِ دمِ دست:</b> {{ex}}</p>

        <div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: %(DIM)s; margin-bottom: 11px;">در این پله چه چیزی هنوز برقرار است</div>
        <div style="display: flex; flex-direction: column; gap: 7px;">
          <sc-for list="{{props}}" as="pr" hint-placeholder-count="6">
            <div style="{{pr.style}}">
              <span style="{{pr.markStyle}}">{{pr.mark}}</span>
              <span style="{{pr.textStyle}}">{{pr.name}}</span>
              <sc-if value="{{pr.hasBadge}}">
                <span style="{{pr.badgeStyle}}">{{pr.badge}}</span>
              </sc-if>
            </div>
          </sc-for>
        </div>
      </div>''')

dash('چیزی که نردبان نمی‌گوید',
     'این بالا رفتن بی‌پایان نیست. قضیه‌ای هست (هورویتس) که می‌گوید فقط <b>چهار</b> دستگاهِ '
     'عددیِ متناهی‌البُعد با این خاصیت‌ها وجود دارد: حقیقی، مختلط، کواترنیون، و یکی دیگر '
     'به نام اوکتونیون که در آن حتی <b>شرکت‌پذیری</b> هم از دست می‌رود — یعنی '
     '(a×b)×c دیگر برابر a×(b×c) نیست. بعد از آن، در بسته است. '
     'یعنی ریاضی هم جایی تمام می‌شود.')
endsec()

# ------------------------------------------------------------------ ۰۴ کانتور
sec('s4', '۰۴ — بی‌نهایت', 'بزرگ‌ترین شکست: معلوم شد بی‌نهایت یکی نیست', white=True)
p('تا قرن نوزدهم، بی‌نهایت یک واژه بود نه یک عدد. «بی‌شمار»، «بی‌پایان»، و تمام. گئورگ کانتور پرسید: آیا می‌شود دو بی‌نهایت را با هم مقایسه کرد؟')
p('روشش ساده‌ترین چیز دنیاست و از خودِ شمردن می‌آید: اگر بتوانی اعضای دو مجموعه را <b>دوبه‌دو جفت کنی</b> و هیچ‌کدام اضافه نیاید، اندازه‌شان یکی است. بدون اینکه بشماری. مثل جفت‌کردن صندلی و آدم در یک تالار.')
p('با همین، چیزهای عجیبی درآمد: عددهای زوج به اندازهٔ همهٔ عددهای شمارشی‌اند (هر ⁦n⁩ را با ⁦۲n⁩ جفت کن). کسرها هم همین‌قدرند. تا این‌جا انگار همهٔ بی‌نهایت‌ها یکی‌اند.')
p('و بعد کانتور در سال ۱۸۹۱ نشان داد عددهای حقیقی <b>نیستند</b>. استدلالش را خودت پایین اجرا کن.')

w('''
      <div style="%(CARD)s padding: 24px 26px; margin: 0 0 22px;">
        <div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 14px;">استدلالِ قطری — قدم {{dStepFa}} از {{dTotalFa}}</div>
        <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0 0 18px; max-width: 70ch;">{{dMsg}}</p>

        <div style="%(LTR)s font-size: 15px; margin: 0 0 18px; overflow-wrap: anywhere;">
          <sc-for list="{{rows}}" as="r" hint-placeholder-count="8">
            <div style="{{r.style}}">
              <span style="direction: rtl; font-size: 11.5px; color: #666158; min-width: 6.5em;">{{r.label}}</span>
              <span style="font-weight: 600; letter-spacing: 0.04em;">۰٫<sc-for list="{{r.digits}}" as="d" hint-placeholder-count="10"><span style="{{d.style}}">{{d.t}}</span></sc-for>…</span>
            </div>
          </sc-for>
        </div>

        <div style="background: %(SOFT)s; border-radius: 12px; padding: 16px 19px; margin: 0 0 18px;">
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 9px;">عددی که داریم می‌سازیم</div>
          <div style="%(LTR)s font-size: 19px; font-weight: 800; color: %(AC)s; letter-spacing: 0.06em;">۰٫{{built}}<span style="color: #B5ADC4;">{{pad}}</span>…</div>
          <sc-if value="{{hasBuilt}}">
            <p style="font-size: 12.5px; line-height: 1.9; color: %(MID)s; margin: 11px 0 0;">قاعده‌اش یک خط است: هر رقمِ قطری اگر ۵ بود، ۴ بگذار؛ وگرنه ۵.</p>
          </sc-if>
        </div>

        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <sc-for list="{{dBtns}}" as="b" hint-placeholder-count="3">
            <button style="{{b.style}}" onClick="{{b.onClick}}">{{b.label}}</button>
          </sc-for>
        </div>
      </div>''')

p('این استدلال فقط یک نتیجه نداد، یک <b>ابزار</b> داد. همین ترفند بعدها در اثباتِ قضیهٔ گودل و در جوابِ تورینگ به مسئلهٔ توقف به کار رفت. یعنی یکی از پرکاربردترین ایده‌های قرن بیستم.')
dash('استقبالی که نشد',
     'کرونکر، استادِ بانفوذِ همان دوره، سرسختانه مخالفت کرد؛ بنا بر چند روایت تا جایی که '
     'کانتور را شارلاتان خواند. پوانکاره نظریهٔ مجموعه‌ها را یک «بیماری» دانست. '
     'در مقابل، ددکیند و بعدها هیلبرت و زرملو پشتش ایستادند. '
     'امروز این استدلال در هر درسِ مقدماتیِ ریاضیِ دانشگاهی هست.')
endsec()

# ------------------------------------------------------------------ ۰۵
sec('s5', '۰۵ — فضا', 'دو هزار سال فکر می‌کردیم هندسه یکی بیشتر نیست')
p('اقلیدس حدود ۳۰۰ سال پیش از میلاد، کلِ هندسه را روی پنج فرضِ ساده بنا کرد. چهارتایش بدیهی بود. پنجمی — <b>اصلِ توازی</b> — پیچیده‌تر بود: از یک نقطهٔ بیرونِ یک خط، فقط <b>یک</b> خط می‌گذرد که با آن موازی باشد.')
p('دو هزار سال، ریاضی‌دان‌ها تلاش کردند این پنجمی را از آن چهارتای دیگر <b>نتیجه بگیرند</b>. همه شکست خوردند. تا اینکه در قرن نوزدهم کسی سؤال را برگرداند: چه می‌شود اگر فرض کنیم <b>غلط</b> است؟')
p('جوابش این بود: هیچ تناقضی پیش نمی‌آید. فقط هندسهٔ دیگری درمی‌آید — به همان اندازه سازگار و به همان اندازه واقعی. اصلِ پنجم یک حقیقت نبود؛ یک <b>انتخاب</b> بود.')
box('کِی و چه کسی',
    'لوباچفسکی و بویویی مستقل از هم و تقریباً هم‌زمان به آن رسیدند. منابع سر تاریخ‌ها '
    'یکی نیستند: لوباچفسکی حدود ۱۸۲۹ آن را علنی کرد و بویویی در ۱۸۳۲ منتشرش کرد. '
    'گاوس سال‌ها پیش‌تر به همین رسیده بود ولی منتشر نکرد — و وقتی کارِ بویویی را دید، '
    'نوشت که خودش همهٔ این‌ها را سال‌ها قبل فکر کرده بود. '
    'کارشان اولش نادیده گرفته و مسخره شد؛ لوباچفسکی بی‌آنکه پذیرفته‌شدنش را ببیند مرد.')
p('پیامدش از خودِ هندسه بزرگ‌تر بود. تا آن روز فکر می‌کردند ریاضی <b>حقیقتِ جهان</b> را توصیف می‌کند. بعد از آن معلوم شد ریاضی می‌گوید: «اگر این فرض‌ها را بگذاری، این‌ها نتیجه می‌شوند» — و اینکه کدام فرض به جهانِ واقعی می‌خورد، سؤالِ فیزیک است نه ریاضی.')
dash('و جوابِ فیزیک چه بود',
     'شصت سال بعد، اینشتین برای نسبیت عام دقیقاً به همان هندسهٔ غیراقلیدسی نیاز داشت. '
     'فضا-زمانِ واقعی تخت نیست. یعنی آن «بازیِ بی‌فایدهٔ ریاضی‌دان‌ها» سرانجام '
     'توصیفِ درستِ جهان از آب درآمد — و هندسهٔ اقلیدسی تقریبی بود.')
endsec()

# ------------------------------------------------------------------ ۰۶
sec('s6', '۰۶ — قطعیت', 'و بعد ریاضی خواست خودش را اثبات کند', white=True)
p('اوایل قرن بیستم نقشه‌ای بود: همهٔ ریاضی را روی چند اصلِ ساده بنا کنیم و ثابت کنیم این بنا هیچ‌وقت به تناقض نمی‌رسد. دو ضربه خورد.')
w('''      <h3 style="%(H3)s margin-top: 26px;">ضربهٔ اول: یک نامه</h3>''')
p('شانزدهم ژوئن ۱۹۰۲، برتراند راسل نامه‌ای به گوتلوب فرگه نوشت. جلد دومِ کتابِ عمرِ فرگه زیر چاپ بود. راسل بعد از ابراز احترام، خبر را ملایم داد: یکی از اصل‌های پایه‌ای فرگه به تناقض می‌رسد.')
p('مسئله را می‌شود بدون هیچ ریاضی گفت. در یک شهر، سلمانی موی <b>هر کسی را می‌زند که موی خودش را نمی‌زند</b> — و فقط همان‌ها را. حالا بپرس: سلمانی موی خودش را می‌زند؟')
w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px; margin: 0 0 20px; max-width: 76ch;">
        <div style="%(SOFTC)s padding: 18px 20px;">
          <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 0;"><b>اگر بزند:</b> پس جزو کسانی است که موی خودشان را می‌زنند، و سلمانی موی این‌ها را نمی‌زند. پس نباید بزند.</p>
        </div>
        <div style="%(SOFTC)s padding: 18px 20px;">
          <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 0;"><b>اگر نزند:</b> پس جزو کسانی است که موی خودشان را نمی‌زنند، و سلمانی موی همین‌ها را می‌زند. پس باید بزند.</p>
        </div>
      </div>''')
p('این بازیِ لفظی نیست. فرگه اجازه داده بود برای <b>هر</b> ویژگی‌ای، مجموعهٔ چیزهایی که آن ویژگی را دارند بسازی. راسل ویژگی «عضوِ خودش نیست» را گذاشت و بنا فرو ریخت.')
p('فرگه در شش روز جواب داد. پیوستی شتاب‌زده به کتاب اضافه کرد و تا آخر عمر از این ضربه کمر راست نکرد. تعمیرش هم همان شکلِ همیشگی را داشت: قاعده‌ها را <b>تنگ‌تر</b> کردند. دیگر هر دسته‌ای مجموعه نیست.')

w('''      <h3 style="%(H3)s margin-top: 30px;">ضربهٔ دوم: گودل، ۱۹۳۱</h3>''')
p('کورت گودل نشان داد نقشه از پایه شدنی نیست. دو نتیجه:')
w('''      <div style="display: flex; flex-direction: column; gap: 11px; margin: 0 0 20px; max-width: 74ch;">''')
for n, t in [
    ('۱', 'هر دستگاهِ صوریِ سازگار که به اندازهٔ کافی حساب در خود داشته باشد، '
          '<b>ناتمام</b> است: گزاره‌هایی هستند که نه خودشان و نه نقیضشان در آن دستگاه اثبات‌پذیرند.'),
    ('۲', 'چنین دستگاهی نمی‌تواند <b>سازگاریِ خودش</b> را اثبات کند. برای این کار '
          'به دستگاهِ بزرگ‌تری نیاز داری — که خودش همین مشکل را دارد.'),
]:
    w('''        <div style="%(SOFTC)s padding: 17px 20px; display: flex; gap: 14px; align-items: flex-start;">
          <span style="font-size: 13px; font-weight: 800; color: %(AC)s; flex-shrink: 0; margin-top: 3px;">%(n)s</span>
          <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0;">%(t)s</p>
        </div>''', n=n, t=t)
w('      </div>')
p('روشِ اثباتش هم همان ترفندِ قطریِ کانتور بود، با یک پیچ: گودل راهی پیدا کرد که دستگاه دربارهٔ <b>خودش</b> حرف بزند.')

dash('و حالا چیزی که گودل نگفت — و همه به او نسبت می‌دهند',
     'این بخش را هیچ‌جا نمی‌گویند و بیشترِ چیزی که دربارهٔ گودل شنیده‌ای غلط است. '
     '<b>یک:</b> نگفت «حقیقت‌هایی هستند که اثبات‌پذیر نیستند». قضیه دربارهٔ اثبات‌پذیری '
     'در <b>یک دستگاهِ مشخص</b> است، نه اثبات‌پذیری به‌طور مطلق. همان گزاره در دستگاهِ '
     'بزرگ‌تر اثبات‌پذیر است. '
     '<b>دو:</b> نگفت «هر دستگاهِ سازگاری ناتمام است». دستگاه باید حسابِ کافی در خود '
     'داشته باشد؛ دستگاه‌های سازگار و تمامِ فراوانی وجود دارند. '
     '<b>سه:</b> دربارهٔ حدِ دانشِ بشر، حدِ عقل، یا ذهنِ انسان هیچ نگفت. آن‌ها '
     'تعمیم‌های بعدیِ دیگران‌اند. '
     '<b>چهار:</b> خودش در همان مقالهٔ ۱۹۳۱ نوشت که این نتیجه با دیدگاهِ صوری‌گرایانهٔ '
     'هیلبرت در تناقض نیست — یعنی روایتِ «گودل برنامهٔ هیلبرت را کشت» را خودش تأیید نمی‌کند.')
endsec()

# ------------------------------------------------------------------ ۰۷
sec('s7', '۰۷ — اصل موضوع', 'قاعده‌هایی که خودت می‌گذاری، و بعد تسلیمشان می‌شوی')
p('حالا که دیدی هندسه یک انتخاب بود و بنا فرو ریخت و دوباره ساخته شد، می‌شود گفت ریاضی واقعاً چیست.')
p('<b>اصلِ موضوع</b> یعنی چیزی که بدون اثبات می‌پذیری. نه چون بدیهی است — چون می‌خواهی ببینی اگر بپذیری چه نتیجه‌ای می‌دهد. مثل قاعده‌های یک بازی: «اسب به شکل L حرکت می‌کند» نه درست است نه غلط. قاعده است.')
p('ولی یک تفاوت هولناک با بازی دارد: <b>بعد از اینکه قاعده‌ها را گذاشتی، نتیجه‌ها دیگر دستِ تو نیستند.</b> تو تصمیم می‌گیری مهره‌ها چطور حرکت کنند؛ تصمیم نمی‌گیری چه کسی می‌برد.')
w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px; margin: 22px 0 20px;">''')
for t, d, y in [
    ('پنج اصلِ اقلیدس', 'کلِ هندسهٔ کلاسیک از پنج جمله. پنجمی‌اش همان بود که دو هزار سال سرش دعوا شد.', 'حدود ۳۰۰ پیش از میلاد'),
    ('اصل‌های پئانو', 'کلِ عددهای شمارشی از چند جمله: یک صفر هست، هر عدد یک بعدی دارد، و… همین.', '۱۸۸۹'),
    ('اصل‌های نظریهٔ مجموعه‌ها', 'بنایی که بعد از ضربهٔ راسل ساخته شد و امروز زیرِ تقریباً کلِ ریاضی است.', 'قرن بیستم'),
]:
    w('''        <div style="%(CARD)s padding: 20px 22px;">
          <h3 style="%(H3)s">%(t)s</h3>
          <p style="font-size: 11.5px; color: %(DIM)s; margin: 0 0 10px;">%(y)s</p>
          <p style="font-size: 13.5px; line-height: 2; color: %(MID)s; margin: 0;">%(d)s</p>
        </div>''', t=t, d=d, y=y)
w('      </div>')
box('پس ریاضی چه می‌گوید',
    'ریاضی هیچ‌وقت نمی‌گوید «این درست است». می‌گوید: <b>«اگر این فرض‌ها را بپذیری، '
    'آن نتیجه ناگزیر است.»</b> همین و بس. اینکه کدام فرض به جهانِ واقعی می‌خورد، '
    'کارِ فیزیک و مهندسی و تجربه است — نه کارِ ریاضی. '
    'و همین است که ریاضی را از همهٔ رشته‌های دیگر جدا می‌کند: تنها جایی که '
    'قاعده‌ها را خودت می‌گذاری و نتیجه‌ها قابل مذاکره نیستند.')
endsec()

# ------------------------------------------------------------------ ۰۸
sec('s8', '۰۸ — اثبات', 'تنها کاری که ریاضی را ریاضی می‌کند', white=True)
p('در همهٔ علوم دیگر، <b>شاهد</b> جمع می‌کنی. هزار قو دیدی و همه سفید بودند؟ احتمالاً قوها سفیدند. یک قوی سیاه پیدا شود، حرف عوض می‌شود.')
p('در ریاضی این کافی نیست و اصلاً به حساب نمی‌آید. هزار مثال هیچ چیزی را ثابت نمی‌کند. <b>اثبات</b> یعنی زنجیره‌ای از قدم‌ها که از فرض‌ها شروع می‌شود و هر قدمش انکارناپذیر است. اگر درست باشد، تا ابد درست است و هیچ مشاهده‌ای نمی‌تواند خرابش کند.')
p('بهترین راهِ فهمیدنش این است که یکی را کامل ببینی. این یکی از همه مشهورتر است و فقط شش خط دارد — همان اثباتی که عددهای گنگ را به دنیا آورد.')

PROOF = [
    ('ادعا', 'هیچ کسری نیست که مربعش دقیقاً ۲ باشد. یعنی ⁦√۲⁩ را نمی‌شود به صورت ⁦a⁄b⁩ نوشت.'),
    ('۱', 'فرض کن می‌شود. پس ⁦√۲ = a⁄b⁩، و کسر را تا جایی ساده کرده‌ایم که ⁦a⁩ و ⁦b⁩ <b>هر دو زوج نباشند</b> (وگرنه باز هم ساده می‌شد).'),
    ('۲', 'دو طرف را به توان دو برسان: ⁦۲ = a²⁄b²⁩. یعنی ⁦a² = ۲b²⁩.'),
    ('۳', 'پس ⁦a²⁩ زوج است. و اگر مربعِ عددی زوج باشد، خودش هم زوج است. پس <b>⁦a⁩ زوج است</b>.'),
    ('۴', 'اگر ⁦a⁩ زوج است، یعنی ⁦a = ۲k⁩ برای یک عدد درستِ ⁦k⁩. جایش بگذار: ⁦(۲k)² = ۲b²⁩، یعنی ⁦۴k² = ۲b²⁩، یعنی ⁦۲k² = b²⁩.'),
    ('۵', 'پس ⁦b²⁩ هم زوج است، پس <b>⁦b⁩ هم زوج است</b>.'),
    ('۶', 'ولی در قدم ۱ گفتیم هر دو زوج نیستند. تناقض.'),
    ('نتیجه', 'فرضِ اول غلط بود. چنین کسری وجود ندارد — و نه چون پیدایش نکرده‌ایم، بلکه چون <b>ممکن نیست</b> وجود داشته باشد.'),
]
w('      <div style="display: flex; flex-direction: column; gap: 9px; margin: 0 0 22px; max-width: 72ch;">')
for n, t in PROOF:
    head = n in ('ادعا', 'نتیجه')
    w('''        <div style="background: %(bg)s; border: 1px solid %(bd)s; border-radius: 12px; padding: 15px 18px; display: flex; gap: 14px; align-items: flex-start;">
          <span style="font-size: 12px; font-weight: 800; color: %(AC)s; flex-shrink: 0; margin-top: 3px; min-width: 3.2em;">%(n)s</span>
          <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0;">%(t)s</p>
        </div>''', n=n, t=t,
      bg=(V['SOFT'] if head else '#FAFAF7'), bd=('#D5CEDF' if head else V['LINE']))
w('      </div>')
p('به شکلِ استدلال نگاه کن، نه به محتوایش. فرض کردیم چیزی هست، تا تناقض دنبالش رفتیم، و نتیجه گرفتیم نیست. به این می‌گویند <b>برهانِ خلف</b> و یکی از چند حرکتِ اصلیِ کلِ ریاضی است.')
dash('و افسانه‌ای که باید با احتیاط شنید',
     'معروف است که کاشفِ این حقیقت را پیروانِ فیثاغورس در دریا غرق کردند. '
     'شواهدِ تاریخی‌اش ضعیف است: منابعِ باستانی یا نامی از او نمی‌برند، یا دلیلِ دیگری '
     'برای غرق‌شدنش می‌گویند، و با هم نمی‌خوانند. '
     'روایتِ محتاطانه‌تر این است که یونانی‌ها این مقدارها را از دایرهٔ «عدد» بیرون گذاشتند '
     'و به‌جایش در هندسه جایشان دادند — که خودش به‌اندازهٔ کافی گویاست.')
endsec()

# ------------------------------------------------------------------ ۰۹
sec('s9', '۰۹ — سه حرکت', 'هر کاری که ریاضی‌دان‌ها می‌کنند، یکی از این سه تاست')
p('اگر این صفحه را فردا فراموش کنی و فقط یک چیز یادت بماند، این باشد. کلِ ریاضی سه حرکت است:')
MOVES = [
    ('انتزاع', 'فراموش‌کردنِ آنچه مهم نیست',
     'هفت گوسفند، هفت سنگ و هفت روز هیچ شباهتی به هم ندارند. ریاضی همه‌چیزشان را '
     'دور می‌ریزد جز یک چیز: «هفت». هر بار که چیزهای بی‌ربط را زیر یک نام می‌آوری، '
     'انتزاع کرده‌ای. و هر بار قدرتت بیشتر می‌شود، چون حالا یک کشف برای همه‌شان کار می‌کند.'),
    ('ساختار', 'دیدنِ آنچه وقتی چیزها عوض می‌شوند، عوض نمی‌شود',
     'چرخشِ یک مربع، جابه‌جایی مهره‌های یک پازل، و ترکیبِ دو عملِ ریاضی — هر سه '
     'یک قاعده دارند. وقتی آن قاعدهٔ مشترک را جدا می‌کنی و اسم رویش می‌گذاری '
     '(مثلاً «گروه»)، هرچه دربارهٔ آن ثابت کنی، همان لحظه دربارهٔ هر سه ثابت شده. '
     'این موتورِ اصلیِ ریاضیِ دو قرن اخیر است.'),
    ('اثبات', 'رفتن از فرض به نتیجه، بدون هیچ شکافی',
     'تفاوتِ ریاضی با همه‌چیز. نه شاهد، نه آزمایش، نه نظرِ اکثریت. زنجیره‌ای که '
     'هر حلقه‌اش انکارناپذیر است. چیزی که با این روش به دست می‌آید، '
     'تا ابد درست می‌ماند.'),
]
w('      <div style="display: flex; flex-direction: column; gap: 13px; margin: 0 0 20px;">')
for i, (t, sub, d) in enumerate(MOVES):
    w('''        <div style="%(CARD)s padding: 24px 26px; border-inline-start: 4px solid %(AC)s;">
          <div style="display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 11px;">
            <span style="font-size: 13px; font-weight: 800; color: %(AC)s;">%(n)s</span>
            <h3 style="font-size: 19px; font-weight: 800; margin: 0;">%(t)s</h3>
            <span style="font-size: 13.5px; color: %(DIM)s;">%(sub)s</span>
          </div>
          <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0; max-width: 70ch;">%(d)s</p>
        </div>''', n=fa('%02d' % (i + 1)), t=t, sub=sub, d=d)
w('      </div>')
p('و حالا به نردبانِ بالا برگرد. هر پله‌اش دقیقاً همین سه حرکت بود: چیزی شکست، کسی مفهومی را <b>انتزاع</b> کرد، <b>ساختارش</b> را کشف کرد، و با <b>اثبات</b> نشان داد سازگار است.')
endsec()

# ------------------------------------------------------------------ ۱۰
sec('s10', '۱۰ — نقشهٔ شاخه‌ها', 'هر شاخهٔ ریاضی جوابِ یک سؤال است', white=True)
p('اسم شاخه‌ها را شنیده‌ای ولی کسی نگفته هر کدام دنبال چه می‌گردند. یک جمله برای هر کدام:')
BR = [
    ('حساب و نظریهٔ اعداد', 'خودِ عددهای درست چه خاصیت‌هایی دارند؟', 'ساده‌ترین سؤال‌ها، سخت‌ترین جواب‌ها. بعضی‌شان هنوز باز است.'),
    ('جبر', 'وقتی عددها را با نماد عوض کنیم، چه قاعده‌هایی باقی می‌مانند؟', 'و بعد: خودِ آن قاعده‌ها چه ساختاری دارند؟ این‌جا جبر مدرن شروع می‌شود.'),
    ('هندسه', 'شکل و فاصله و فضا چه خاصیت‌هایی دارند؟', 'و بعد از قرن نوزدهم: کدام فضا؟ چون بیش از یکی هست.'),
    ('آنالیز', 'وقتی چیزی پیوسته تغییر می‌کند چه اتفاقی می‌افتد؟', 'حد، مشتق، انتگرال. بدون عددهای حقیقی هیچ‌کدامش ممکن نیست.'),
    ('احتمال و آمار', 'وقتی نمی‌دانی، چقدر نمی‌دانی؟', 'تنها شاخه‌ای که ندانستن را خودش به عدد تبدیل می‌کند.'),
    ('توپولوژی', 'چه چیزی وقتی شکل را بکشی و بپیچانی (ولی پاره نکنی) عوض نمی‌شود؟', 'به همین دلیل فنجان و دونات یکی‌اند: هر دو یک سوراخ دارند.'),
    ('منطق و نظریهٔ مجموعه‌ها', 'خودِ اثبات و خودِ مجموعه چه خاصیتی دارند؟', 'ریاضی وقتی به خودش نگاه می‌کند. گودل و راسل این‌جایند.'),
    ('ریاضیات گسسته', 'وقتی چیزها پیوسته نیستند و دانه‌دانه‌اند چه؟', 'گراف، شمارش، الگوریتم. پایهٔ کلِ علوم کامپیوتر.'),
]
w('      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 12px;">')
for t, q, d in BR:
    w('''        <div style="%(SOFTC)s padding: 20px 22px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px; line-height: 1.55;">%(t)s</h3>
          <p style="font-size: 14px; line-height: 1.95; color: %(AC)s; font-weight: 600; margin: 0 0 9px;">%(q)s</p>
          <p style="font-size: 13px; line-height: 1.95; color: %(MID)s; margin: 0;">%(d)s</p>
        </div>''', t=t, q=q, d=d)
w('      </div>')
endsec()

# ------------------------------------------------------------------ ۱۱
sec('s11', '۱۱ — چطور یاد بگیری', 'روش، نه سرفصل')
p('سرفصل زیاد است و همه‌جا هست. چیزی که کم است روش است. پنج چیزی که واقعاً فرق می‌کند:')
HOW = [
    ('از سؤال شروع کن، نه از تعریف',
     'هر وقت تعریفی دیدی که بی‌معنا به نظر رسید، نپرس «این چیست». بپرس '
     '<b>«چه چیزی خراب بود که این را ساختند»</b>. تقریباً همیشه جواب دارد و '
     'تقریباً همیشه در کتاب نیست.'),
    ('مثالِ نقض بساز',
     'وقتی قاعده‌ای یاد گرفتی، سعی کن بشکنی‌اش. دنبال موردی بگرد که در آن جواب ندهد. '
     'یا پیدایش می‌کنی و چیزِ مهمی فهمیده‌ای، یا نمی‌کنی و تازه می‌فهمی قاعده چه می‌گوید.'),
    ('کوچک‌ترین حالت را با دست حساب کن',
     'هر چیزی را با ۱ و ۲ و ۳ امتحان کن، روی کاغذ، بدون ماشین‌حساب. '
     'الگو را در عددهای کوچک می‌بینی. ریاضی‌دان‌های حرفه‌ای هم همین کار را می‌کنند '
     'و هیچ‌کس این را به دانش‌آموز نمی‌گوید.'),
    ('برای کسی توضیحش بده',
     'هر جا توضیحت گیر کرد، همان‌جا نفهمیده‌ای. این دقیق‌ترین آزمونِ فهمیدن است '
     'و هیچ امتحانی جایش را نمی‌گیرد.'),
    ('آهسته برو، و برگرد',
     'ریاضی تنها جایی است که اگر صفحهٔ ۴۰ را نفهمی، صفحهٔ ۴۱ هم غیرممکن می‌شود. '
     'برخلاف بقیهٔ چیزها، این‌جا رد شدن از یک تکه جبران نمی‌شود. وقتی گیر کردی، '
     'مشکل تقریباً همیشه چند صفحه عقب‌تر است.'),
]
w('      <div style="display: flex; flex-direction: column; gap: 11px; margin: 0 0 20px;">')
for i, (t, d) in enumerate(HOW):
    w('''        <div style="%(CARD)s padding: 20px 23px; display: flex; gap: 15px; align-items: flex-start;">
          <span style="font-size: 13px; font-weight: 800; color: %(AC)s; flex-shrink: 0; margin-top: 3px;">%(n)s</span>
          <div>
            <div style="font-size: 15px; font-weight: 700; color: %(INK)s; margin-bottom: 7px; line-height: 1.6;">%(t)s</div>
            <div style="font-size: 14px; line-height: 2.05; color: %(MID)s; max-width: 68ch;">%(d)s</div>
          </div>
        </div>''', n=fa('%02d' % (i + 1)), t=t, d=d)
w('      </div>')
box('و یک نکتهٔ آخر',
    'اگر جایی از این صفحه حس کردی «این که خیلی ساده بود، پس چرا ده سال نفهمیدم» — '
    'جوابش همان بخش اول است. مفهوم‌ها سخت نیستند؛ <b>بی‌دلیل</b> ارائه شده‌اند. '
    'وقتی بحران را بدانی، تعریف خودش می‌آید.', V['GREEN'], '#F1F6EF')
endsec()

# ------------------------------------------------------------------ ۱۲
sec('s12', '۱۲ — روش و منابع', 'این صفحه از کجا آمده و کجا باید با احتیاط خواندش', white=True)
p('ادعاهای <b>ریاضیِ</b> این صفحه دانشِ پایه‌اند و در هر کتاب مقدماتی هست: نردبانِ دستگاه‌های عددی، خاصیت‌هایی که در هر پله از دست می‌رود، استدلال قطری، و اثباتِ گنگ‌بودنِ ریشهٔ دو. این‌ها جای بحث ندارند.')
p('ادعاهای <b>تاریخی</b> فرق دارند. برای هر کدام منبع آورده‌ام، و هر جا منابع با هم نخوانده‌اند هر دو روایت را نوشته‌ام و نگفته‌ام کدام درست است:')
CARE = [
    'افسانهٔ غرق‌شدنِ کاشفِ عددهای گنگ سندِ محکمی ندارد؛ منابعِ باستانی با هم نمی‌خوانند.',
    '«تحقیرآمیز بودنِ» نامِ موهومی از خلاصه‌های بعدی می‌آید، نه از صریحِ متنِ دکارت.',
    'تاریخ‌های هندسهٔ غیراقلیدسی در منابع مختلف فرق می‌کند (۱۸۲۳ تا ۱۸۴۰).',
    'جمله‌های منسوب به کرونکر دربارهٔ کانتور از روایت‌های دست‌دوم‌اند.',
    'کَنده‌کاریِ همیلتون روی پل دیگر وجود ندارد؛ روایت به گفتهٔ خودش و لوحِ امروزی تکیه دارد.',
]
w('      <div style="display: flex; flex-direction: column; gap: 8px; margin: 0 0 24px; max-width: 74ch;">')
for t in CARE:
    w('''        <div style="%(SOFTC)s padding: 14px 18px; display: flex; gap: 12px; align-items: flex-start;">
          <span style="color: %(RUST)s; font-weight: 800; flex-shrink: 0;">!</span>
          <span style="font-size: 13.5px; line-height: 1.98; color: %(MID)s;">%(t)s</span>
        </div>''', t=t)
w('      </div>')

SOURCES = [
    ('دانشنامهٔ فلسفهٔ استنفورد — قضیه‌های ناتمامیت گودل',
     'https://plato.stanford.edu/entries/goedel-incompleteness/',
     'دقیق‌ترین مرجع برای اینکه این قضیه‌ها چه می‌گویند و چه نمی‌گویند.'),
    ('یادداشتی دربارهٔ بدفهمی‌های قضیه‌های گودل',
     'https://arxiv.org/html/1902.05902v1',
     'فهرستِ خطاهای رایج — پایهٔ بخشِ «چیزی که گودل نگفت».'),
    ('دانشنامهٔ فلسفهٔ استنفورد — پارادوکس راسل',
     'https://plato.stanford.edu/entries/russell-paradox/',
     'تاریخِ نامهٔ ۱۹۰۲ و جوابِ فرگه.'),
    ('مک‌تیوتر — زندگی‌نامهٔ براهماگوپتا',
     'https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/',
     'قاعده‌های سال ۶۲۸ برای صفر و منفی، و خطاهای خودِ براهماگوپتا در تقسیم بر صفر.'),
    ('ویکی‌پدیا — هیپاسوس',
     'https://en.wikipedia.org/wiki/Hippasus',
     'اینکه هیچ نویسندهٔ باستانی کشفِ گنگ‌بودن را مشخصاً به او نسبت نمی‌دهد.'),
    ('ویکی‌پدیا — استدلال قطری کانتور',
     'https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument',
     'تاریخ ۱۸۹۱، و اینکه همین ترفند در کارِ گودل و تورینگ به کار رفت.'),
    ('ویکی‌پدیا — جدال بر سر نظریهٔ کانتور',
     'https://en.wikipedia.org/wiki/Controversy_over_Cantor%27s_theory',
     'مخالفتِ کرونکر و پوانکاره، و پشتیبانیِ ددکیند و هیلبرت.'),
    ('بریتانیکا — لوباچفسکی',
     'https://www.britannica.com/biography/Nikolay-Ivanovich-Lobachevsky',
     'تاریخِ علنی‌شدنِ هندسهٔ هذلولوی و واکنشی که گرفت.'),
    ('ولفرام متورلد — اصل توازی',
     'https://mathworld.wolfram.com/ParallelPostulate.html',
     'صورتِ دقیقِ اصل پنجم و تاریخ‌های بویویی و لوباچفسکی.'),
    ('ویکی‌پدیا — تاریخ کواترنیون',
     'https://en.wikipedia.org/wiki/History_of_quaternions',
     'شانزدهم اکتبر ۱۸۴۳، پلِ دوبلین، و سرنوشتِ کَنده‌کاری.'),
    ('nLab — جبرهای تقسیمِ نرم‌دار',
     'https://ncatlab.org/nlab/show/normed+division+algebra',
     'قضیهٔ هورویتس: فقط چهار تا، و اینکه در هر پله چه خاصیتی می‌رود.'),
    ('ویکی‌پدیا — عدد موهومی',
     'https://en.wikipedia.org/wiki/Imaginary_number',
     'نام‌گذاریِ دکارت در ۱۶۳۷ و جاافتادنش با اویلر.'),
    ('متنِ «شکایتِ یک ریاضی‌دان» نوشتهٔ پل لاکهارت',
     'https://worrydream.com/refs/Lockhart_2002_-_A_Mathematician%27s_Lament.pdf',
     'جستاری که بخشِ اولِ این صفحه رویش ایستاده.'),
]
w('      <h3 style="%(H3)s margin-top: 10px;">منابع</h3>')
w('      <div style="display: flex; flex-direction: column; gap: 9px;">')
for i, (t, u, why) in enumerate(SOURCES):
    w('''        <div style="%(SOFTC)s padding: 17px 19px;">
          <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 7px;">
            <span style="font-size: 11.5px; font-weight: 800; color: %(AC)s;">%(n)s</span>
            <span style="font-size: 14px; font-weight: 700; color: %(INK)s; line-height: 1.6;">%(t)s</span>
          </div>
          <p style="font-size: 13px; line-height: 1.9; color: %(MID)s; margin: 0 0 8px;">%(why)s</p>
          <p style="margin: 0;"><a href="%(u)s" target="_blank" rel="noopener" style="%(LTR)s font-size: 12px; font-weight: 700; color: %(AC)s; display: inline-block; max-width: 100%%; overflow-wrap: anywhere;">%(u)s ↗</a></p>
        </div>''', n=fa('%02d' % (i + 1)), t=t, why=why, u=u)
w('      </div>')

w('''      <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 26px 0 20px; max-width: 70ch;">و یک حرفِ آخر دربارهٔ خودِ این قالب. دلیلِ اینکه این صفحه از راهِ شکستن می‌رود، سلیقه نیست. مفهوم‌های ریاضی وقتی که از بحرانشان جدا شوند، شبیه قاعده‌های دلبخواهی می‌شوند — و حفظ‌کردنِ قاعدهٔ دلبخواهی کاری است که مغز از آن متنفر است. بحران را که بدانی، تعریف دیگر حفظ‌کردنی نیست.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="Math.dc.html" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: #1E3A5F; padding: 12px 22px; border-radius: 10px;">ریاضیات هوش مصنوعی ←</a>
        <a href="Plain.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">برنامه‌نویسی به زبان ساده ←</a>
        <a href="Library.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">کتابخانهٔ منابع ←</a>
      </div>''')
endsec()

w('''
  </main>

  <footer style="border-top: 1px solid %(LINE)s; background: #FFFFFF;">
    <div style="max-width: 1060px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: %(DIM)s;">رضا هاشمی · ریاضی، از راهِ شکستن</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1060,"height":1400}}'>
''')
o.append(L.LOGIC.strip())
o.append('''
</script>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'Foundations.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars ·', len(NAV), 'sections ·', len(SOURCES), 'sources')
