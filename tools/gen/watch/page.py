# -*- coding: utf-8 -*-
"""«رصدخانه» — دفترِ روزانهٔ آنچه در هوش مصنوعی رصد می‌شود.

قالب‌ها با کلیدِ نام‌دار پر می‌شوند (`%(AC)s`) نه با ترتیب، چون این صفحه مدام
بلندتر می‌شود و شمردنِ آرگومان‌ها در بلوک‌های بلند همیشه جایی غلط از آب درمی‌آید.
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from paths import SRC  # noqa: E402
import data as D  # noqa: E402
import logic as L  # noqa: E402

V = dict(
    AC='#16494D',          # پاتینهٔ ابزارِ رصد
    SOFT='#E2EDEC',
    INK='#16181C',
    MID='#45494F',
    DIM='#666158',
    LINE='#E4E1D6',
    RUST='#B4530E',
)
V['LTR'] = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
V['EYE'] = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %(AC)s; margin: 0 0 12px;' % V
V['H2'] = 'font-size: clamp(21px, 2.8vw, 28px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
V['BODY'] = 'font-size: 15.5px; line-height: 2.1; color: %(MID)s; max-width: 68ch; margin: 0 0 16px;' % V
V['LEAD'] = 'font-size: 16.5px; line-height: 2.05; color: %(MID)s; max-width: 66ch; margin: 0 0 16px;' % V
V['SOFTC'] = 'background: #FAFAF7; border: 1px solid %(LINE)s; border-radius: 14px;' % V

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))

N_ITEMS = sum(len(e['items']) for e in D.EDITIONS)
N_SRC = sum(len(i.get('sources', [])) for e in D.EDITIONS for i in e['items'])
LAST = D.EDITIONS[0]
V['LASTFA'] = LAST['fa']

NAV = [('log', 'دفتر'), ('howto', 'چطور بخوانیدش'), ('method', 'روش')]

o = []
def w(s, **extra):
    vals = dict(V)
    vals.update(extra)
    o.append(s % vals if '%(' in s else s)


w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>رصدخانه — آنچه در هوش مصنوعی اتفاق می‌افتد</title>
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
  a{color:#16494D;text-decoration:none}
  a:hover{text-decoration:underline}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  b,strong{font-weight:700;color:#16181C}
  input{font-family:inherit}
  ::selection{background:#E2EDEC;color:#16494D}
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
      <nav data-sections="1" style="display: flex; gap: 2px; margin-inline-start: auto; flex-wrap: wrap;">''')
for sid, lab in NAV:
    w('        <a href="#%(sid)s" style="font-size: 12px; color: #45494F; padding: 6px 10px; border-radius: 999px;">%(lab)s</a>',
      sid=sid, lab=lab)
w('''      </nav>
    </div>
  </header>

  <main>

    <!-- هیرو -->
    <section style="max-width: 1060px; margin: 0 auto; padding: 56px 24px 30px;">
      <p style="%(EYE)s">دفترِ رصد · به‌روز می‌شود</p>
      <h1 style="font-size: clamp(32px, 5vw, 52px); font-weight: 800; margin: 0 0 20px; line-height: 1.35; letter-spacing: -0.01em;">رصدخانه</h1>
      <p style="%(LEAD)s">این‌جا دفترِ چیزهایی است که در هوش مصنوعی اتفاق می‌افتد: مدل تازه، قابلیت تازهٔ یک ابزار قدیمی، پرونده‌ای در دادگاه، عددی در بازار، و حاشیه‌هایی که معمولاً از خودِ خبر مهم‌ترند.</p>
      <p style="%(BODY)s">هر رصد به <b>تاریخ همان روز</b> ثبت می‌شود و دیگر دست نمی‌خورد. اگر بعداً معلوم شد اشتباه بوده، پاکش نمی‌کنم — زیرش می‌نویسم چه شد. دفترِ رصد همین است: ارزشش به این است که بشود برگشت و دید آن روز چه فکر می‌کردیم.</p>
      <p style="%(BODY)s">و یک چیز که این‌جا را از فهرست خبر جدا می‌کند: <b>بالای هر رصد نوشته‌ام از کجا آمده و چقدر می‌شود باورش کرد.</b> چون در این حوزه، بیشترِ آنچه «خبر» نامیده می‌شود اطلاعیهٔ مطبوعاتیِ خودِ شرکت است.</p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin-top: 28px; max-width: 760px;">''')

for num, lab in [(fa(N_ITEMS), 'رصد ثبت‌شده'), (fa(len(D.EDITIONS)), 'دفتر'),
                 (fa(N_SRC), 'پیوند به منبع'), (fa(len(D.CATS)), 'دسته')]:
    w('''        <div style="%(SOFTC)s padding: 18px 20px;">
          <div style="font-size: 26px; font-weight: 800; color: %(AC)s; line-height: 1.2;">%(num)s</div>
          <div style="font-size: 12.5px; color: %(DIM)s; margin-top: 4px;">%(lab)s</div>
        </div>''', num=num, lab=lab)

w('''      </div>

      <div data-sectionlist="1" style="display: none; gap: 6px; flex-wrap: wrap; margin-top: 24px;">''')
for sid, lab in NAV:
    w('        <a href="#%(sid)s" style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 7px 13px; border-radius: 999px;">%(lab)s</a>',
      sid=sid, lab=lab)
w('''      </div>
    </section>

    <!-- چطور بخوانیدش -->
    <section id="howto" style="background: #FFFFFF; border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 46px 24px;">
        <p style="%(EYE)s">راهنما</p>
        <h2 style="%(H2)s">بالای هر رصد یک برچسب هست؛ آن را اول بخوان</h2>
        <p style="%(BODY)s">چهار حالت بیشتر ندارد. همهٔ فرقِ میان «این اتفاق افتاد» و «یک شرکت گفت این اتفاق افتاد» در همین چهار برچسب است.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; margin-top: 22px;">''')

for key, lab, col, soft, desc in D.CONF:
    w('''          <div style="background: #FAFAF7; border: 1px solid %(LINE)s; border-radius: 14px; padding: 18px 20px; border-top: 3px solid %(col)s;">
            <span style="display: inline-block; font-size: 11.5px; font-weight: 700; color: %(col)s; background: %(soft)s; border-radius: 999px; padding: 4px 11px; margin-bottom: 11px;">%(lab)s</span>
            <p style="font-size: 13.5px; line-height: 1.95; color: %(MID)s; margin: 0;">%(desc)s</p>
          </div>''', col=col, soft=soft, lab=lab, desc=desc)

w('''        </div>
        <p style="font-size: 13.5px; line-height: 1.95; color: %(MID)s; margin: 22px 0 0; max-width: 72ch; padding-top: 16px; border-top: 1px solid #F0EEE7;">جایی هم که منابع با هم نمی‌خوانند، اختلافشان را پاک نمی‌کنم؛ زیر رصد می‌نویسم کدام منبع چه گفته. عددی که دو جا دو جور نوشته شده، خودش یک خبر است.</p>
      </div>
    </section>

    <!-- دفتر -->
    <section id="log" style="max-width: 1060px; margin: 0 auto; padding: 46px 24px 20px;">
      <p style="%(EYE)s">دفتر</p>
      <h2 style="%(H2)s">هرچه رصد شده</h2>
      <p style="%(BODY)s">تازه‌ترین بالا. با جست‌وجو و دو فیلتر می‌شود فهرست را باریک کرد.</p>

      <div style="%(SOFTC)s padding: 18px 20px; margin: 22px 0 26px;">
        <label for="q" style="display: block; font-size: 12px; font-weight: 700; color: %(MID)s; margin-bottom: 8px;">جست‌وجو در متن رصدها</label>
        <input id="q" type="search" value="{{q}}" onInput="{{onQ}}" placeholder="نام مدل، شرکت، موضوع…" aria-label="جست‌وجو در رصدخانه" style="width: 100%%; box-sizing: border-box; font-size: 14.5px; padding: 11px 14px; border: 1px solid %(LINE)s; border-radius: 10px; background: #FFFFFF; color: #16181C; margin-bottom: 16px;">

        <div style="font-size: 11.5px; font-weight: 700; color: %(DIM)s; margin-bottom: 8px;">دسته</div>
        <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px;">
          <sc-for list="{{catChips}}" as="c" hint-placeholder-count="7">
            <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}<sc-if value="{{c.hasCount}}"><span style="font-size: 11px; opacity: 0.7;">{{c.count}}</span></sc-if></button>
          </sc-for>
        </div>

        <div style="font-size: 11.5px; font-weight: 700; color: %(DIM)s; margin-bottom: 8px;">اعتبار رصد</div>
        <div style="display: flex; gap: 6px; flex-wrap: wrap;">
          <sc-for list="{{confChips}}" as="c" hint-placeholder-count="5">
            <button style="{{c.style}}" onClick="{{c.onClick}}">{{c.label}}<sc-if value="{{c.hasCount}}"><span style="font-size: 11px; opacity: 0.7;">{{c.count}}</span></sc-if></button>
          </sc-for>
        </div>

        <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-top: 16px; padding-top: 14px; border-top: 1px solid #F0EEE7;">
          <span style="font-size: 13px; color: %(MID)s;"><b>{{countFa}}</b> رصد</span>
          <sc-if value="{{filtered}}">
            <button style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid %(LINE)s; border-radius: 999px; padding: 7px 14px; cursor: pointer;" onClick="{{onClear}}">برداشتن فیلترها</button>
          </sc-if>
        </div>
      </div>

      <sc-if value="{{empty}}">
        <div style="%(SOFTC)s padding: 34px 24px; text-align: center;">
          <p style="font-size: 14.5px; color: %(DIM)s; margin: 0;">با این فیلترها چیزی نیست. فیلترها را بردار یا واژهٔ دیگری امتحان کن.</p>
        </div>
      </sc-if>

      <div style="display: flex; flex-direction: column; gap: 14px;">
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="16">
          <div>
            <sc-if value="{{r.newDay}}">
              <div style="display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin: 26px 0 14px; padding-bottom: 10px; border-bottom: 2px solid %(AC)s;">
                <span style="font-size: 19px; font-weight: 800; color: %(AC)s;">{{r.edFa}}</span>
                <span style="font-size: 13px; color: %(DIM)s;">{{r.edGreg}}</span>
              </div>
            </sc-if>

            <div style="background: #FFFFFF; border: 1px solid %(LINE)s; border-radius: 16px; padding: 24px 26px; border-inline-start: 4px solid {{r.catColor}};">
              <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 13px;">
                <span style="font-size: 11px; font-weight: 700; color: {{r.catColor}}; background: {{r.catSoft}}; border-radius: 999px; padding: 4px 11px;">{{r.catLabel}}</span>
                <span style="font-size: 11px; font-weight: 700; color: {{r.confColor}}; background: {{r.confSoft}}; border-radius: 999px; padding: 4px 11px;">{{r.confLabel}}</span>
                <span style="font-size: 11.5px; color: %(DIM)s; margin-inline-start: auto;">{{r.date}}</span>
              </div>

              <h3 style="font-size: 18px; font-weight: 800; color: %(INK)s; margin: 0 0 14px; line-height: 1.65;">{{r.title}}</h3>

              <sc-for list="{{r.body}}" as="p" hint-placeholder-count="3">
                <p style="font-size: 15px; line-height: 2.1; color: %(MID)s; margin: 0 0 14px; max-width: 70ch;">{{p.t}}</p>
              </sc-for>

              <sc-if value="{{r.hasCode}}">
                <pre style="%(SOFTC)s font-size: 13px; line-height: 1.95; color: %(MID)s; margin: 0 0 16px; padding: 14px 16px; %(LTR)s white-space: pre-wrap; overflow-wrap: anywhere; font-family: inherit;">{{r.code}}</pre>
              </sc-if>

              <sc-if value="{{r.hasWhy}}">
                <div style="background: %(SOFT)s; border-radius: 12px; padding: 15px 18px; margin: 0 0 14px;">
                  <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 7px;">چرا مهم است</div>
                  <p style="font-size: 14px; line-height: 2; color: %(MID)s; margin: 0; max-width: 68ch;">{{r.why}}</p>
                </div>
              </sc-if>

              <sc-if value="{{r.hasNote}}">
                <div style="border: 1px dashed #D8D2C6; border-radius: 12px; padding: 14px 17px; margin: 0 0 14px;">
                  <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(RUST)s; margin-bottom: 7px;">دستِ‌کم بدان</div>
                  <p style="font-size: 13.5px; line-height: 1.95; color: %(MID)s; margin: 0; max-width: 70ch;">{{r.note}}</p>
                </div>
              </sc-if>

              <div style="padding-top: 13px; border-top: 1px solid #F0EEE7;">
                <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(DIM)s; margin-bottom: 9px;">منبع</div>
                <div style="display: flex; flex-direction: column; gap: 7px;">
                  <sc-for list="{{r.srcs}}" as="s" hint-placeholder-count="2">
                    <a href="{{s.url}}" target="_blank" rel="noopener" style="font-size: 12.5px; font-weight: 600; color: %(AC)s; display: inline-block; max-width: 100%%; overflow-wrap: anywhere;">{{s.label}} ↗</a>
                  </sc-for>
                </div>
              </div>
            </div>
          </div>
        </sc-for>
      </div>
    </section>
''')

# ------------------------------------------------------------------ روش
RULES = [
    ('چه چیزی این‌جا می‌آید',
     'چیزی که اگر شش ماه بعد برگردی و بخوانی، هنوز معنا داشته باشد: مدلی که بیرون آمد، '
     'قابلیتی که به ابزاری اضافه شد، حکمی که صادر شد، عددی که جهت بازار را عوض کرد. '
     'و حاشیه‌هایی که چیزی دربارهٔ رفتارِ این صنعت می‌گویند.'),
    ('چه چیزی نمی‌آید',
     'نمرهٔ بنچمارکی که فقط خودِ سازنده گرفته و کسی تکرارش نکرده؛ «فلانی در مصاحبه گفت»؛ '
     'گردِ سرمایه‌گذاری‌ای که هیچ‌چیز جز عددش خبر نیست؛ و هر چیزی که فقط یک توییت پشتش باشد.'),
    ('تاریخ‌ها',
     'تاریخِ بالای هر رصد، تاریخِ خودِ رویداد است نه روزی که من نوشته‌ام. تاریخِ دفتر، روزِ ثبت است. '
     'وقتی این دو فاصله دارند، یعنی رصد را دیر دیده‌ام و همان را هم می‌نویسم.'),
    ('اصلاح',
     'رصد غلط پاک نمی‌شود. زیرش یادداشت اصلاح می‌آید با تاریخ خودش. دفتری که می‌شود ویرایشش کرد، '
     'دیگر دفتر نیست.'),
    ('منبع',
     'هر رصد دست‌کم یک پیوند بیرونی دارد. اگر پیوند به صفحهٔ خودِ سازنده است، برچسبش «منبع دست‌اول» '
     'می‌شود؛ وگرنه نه. هیچ رصدی بدون منبع ثبت نمی‌شود.'),
    ('سوگیری‌ای که دارم',
     'من این ابزارها را هر روز استفاده می‌کنم و از آن‌ها نان می‌خورم. پس احتمالاً نسبت به خبرهای خوب '
     'نرم‌ترم تا خبرهای بد. آن برچسب‌های اعتبار تا حدی برای مهار کردنِ همین است، نه فقط برای تو.'),
]

w('''
    <section id="method" style="background: #FFFFFF; border-top: 1px solid %(LINE)s; margin-top: 40px;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 50px 24px;">
        <p style="%(EYE)s">روش</p>
        <h2 style="%(H2)s">قاعده‌هایی که این دفتر با آن نوشته می‌شود</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px; margin-top: 24px;">''')

for i, (t, d) in enumerate(RULES):
    w('''          <div style="%(SOFTC)s padding: 20px 22px;">
            <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 9px;">
              <span style="font-size: 12px; font-weight: 800; color: %(AC)s;">%(n)s</span>
              <h3 style="font-size: 14.5px; font-weight: 700; margin: 0; line-height: 1.6;">%(t)s</h3>
            </div>
            <p style="font-size: 13.5px; line-height: 1.95; color: %(MID)s; margin: 0;">%(d)s</p>
          </div>''', n=fa('%02d' % (i + 1)), t=t, d=d)

w('''        </div>

        <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 26px 0 20px; max-width: 70ch;">یک حرف آخر دربارهٔ اسم. رصدخانه جایی است که آدم شب‌ها می‌نشیند و چیزی را که خودش کنترلش نمی‌کند، مرتب ثبت می‌کند. کارِ رصدگر پیش‌بینی نیست؛ ثبتِ دقیق است. هرچه این‌جا می‌نویسم با همین نیت نوشته می‌شود.</p>

        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <a href="Library.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">کتابخانهٔ منابع ←</a>
          <a href="AILiteracy.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">معماری سواد هوش مصنوعی ←</a>
          <a href="Services.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">هفتادوپنج در ←</a>
        </div>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid %(LINE)s; background: #FFFFFF;">
    <div style="max-width: 1060px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: %(DIM)s;">رضا هاشمی · رصدخانه · آخرین دفتر %(LASTFA)s</span>
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
io.open(os.path.join(SRC, 'Watch.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars ·', N_ITEMS, 'items ·', len(D.EDITIONS), 'editions ·', N_SRC, 'sources')
