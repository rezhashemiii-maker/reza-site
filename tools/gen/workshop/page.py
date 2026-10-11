# -*- coding: utf-8 -*-
"""«کارگاه» — فهرستِ آموزش ابزارهای کاربردی → src/Workshop.dc.html

برای افزودن ابزار تازه: یک دیکشنری به TOOLS اضافه کن، صفحه‌اش را در همین
پوشه بساز، و در tools/build.mjs ثبتش کن.
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from paths import SRC  # noqa: E402
import kit as K  # noqa: E402
import hf_data as HF  # noqa: E402

TOOLS = [
    dict(href='Higgsfield.dc.html', name='هیگزفیلد', en='Higgsfield',
         kind='تصویر و ویدئو',
         blurb='یک میزِ کار در مرورگر که چند ده مدلِ تصویر و ویدئو و صدا را زیر یک اشتراک '
               'جمع کرده، به‌علاوهٔ ابزارهای خودش برای فیلم‌سازی، شخصیتِ ثابت و ساختِ تبلیغ.',
         stats='۱۶ بخش، %s منبع رسمی · نقشهٔ کاملِ رابط · دستور کارِ روز اول' % K.fa(len(HF.SOURCES)),
         date='۱۹ مهر ۱۴۰۵', ready=True),
]

PLANNED = [
    'ابزارهایی که خودم هر روز استفاده می‌کنم و راهنمای فارسیِ درست‌وحسابی ندارند.',
    'هر کدام وقتی نوشته می‌شود که به‌اندازهٔ کافی باهاش کار کرده باشم که بدانم '
    'کجاها آدم را اذیت می‌کند — نه همان روزی که معرفی می‌شود.',
]

RULES = [
    ('هر دکمه، نه هر قابلیت',
     'فهرستِ قابلیت‌ها را خودِ سازنده بهتر می‌نویسد. چیزی که کم است این است که '
     'وقتی وارد شدی، این دکمه‌ای که جلویت است برای چیست و زدنش چه می‌کند.'),
    ('هزینه را پنهان نمی‌کنم',
     'در هر ابزاری که پولی است، یک بخش فقط دربارهٔ این است که پول کجا می‌رود و '
     'کجا بی‌دلیل هدر می‌شود. معمولاً همین بخش است که در راهنماهای دیگر نیست.'),
    ('نامِ انگلیسی سرِ جایش می‌ماند',
     'دکمه‌ای که در برنامه نوشته شده با همان املا نوشته می‌شود، روی خطِ خودش. '
     'ترجمه‌کردنِ نامِ دکمه فقط باعث می‌شود نتوانی پیدایش کنی.'),
    ('می‌گویم چه چیزی را نمی‌دانم',
     'هر جا منابعِ رسمی با هم نخوانند، هر دو روایت نوشته می‌شود. و هر جا '
     'نتوانسته‌ام خودم ببینم، نوشته می‌شود که ندیده‌ام.'),
]

P = K.Page()
w = P.w
V = P.v

NAV = [('tools', 'ابزارها'), ('how', 'روش')]

w(K.head('کارگاه — آموزش ابزارهای کاربردی'))
w(K.header('Main.dc.html#writing', 'بازگشت به نوشته‌ها', NAV))
w('\n  <main>\n')

w('''
    <section style="max-width: 1060px; margin: 0 auto; padding: 56px 24px 30px;">
      <p style="%(EYE)s">آموزش · گام‌به‌گام</p>
      <h1 style="font-size: clamp(32px, 5vw, 52px); font-weight: 800; margin: 0 0 20px; line-height: 1.35; letter-spacing: -0.01em;">کارگاه</h1>
      <p style="%(LEAD)s">راهنمای کاملِ ابزارهایی که هر روز به کار می‌آیند — از صفر، و تا آخر. نه معرفی، نه فهرستِ قابلیت‌ها: <b>وارد که شدی، این دکمه‌ای که جلویت است برای چیست.</b></p>
      <p style="%(BODY)s">هر راهنما طوری نوشته می‌شود که بشود پیش از نصب و پیش از پرداخت خواندش و فهمید این ابزار به دردت می‌خورد یا نه. و اگر خوردش، بشود کنار دستت بازش گذاشت.</p>
    </section>

    <section id="tools" style="background: #FFFFFF; border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s;">
      <div style="max-width: 1060px; margin: 0 auto; padding: 46px 24px;">
        <p style="%(EYE)s">ابزارها</p>
        <h2 style="%(H2)s">راهنماهای آماده</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-top: 24px;">''')

for t in TOOLS:
    w('''          <a href="%(href)s" style="display: flex; flex-direction: column; %(SOFTC)s padding: 24px 26px; border-top: 3px solid %(AC)s;">
            <span style="font-size: 11px; font-weight: 700; color: %(AC)s; margin-bottom: 11px;">%(kind)s</span>
            <h3 style="font-size: 20px; font-weight: 800; color: %(INK)s; margin: 0 0 8px; line-height: 1.5;">%(name)s</h3>
            <div style="margin-bottom: 13px;">%(en)s</div>
            <p style="font-size: 13.5px; line-height: 1.95; color: %(MID)s; margin: 0 0 15px; flex: 1;">%(blurb)s</p>
            <span style="font-size: 11.5px; color: %(DIM)s; margin-bottom: 10px;">%(stats)s</span>
            <span style="font-size: 11.5px; color: %(DIM)s; margin-bottom: 12px;">نوشته‌شده %(date)s</span>
            <span style="font-size: 13.5px; font-weight: 700; color: %(AC)s;">خواندن راهنما ←</span>
          </a>''', href=t['href'], kind=t['kind'], name=t['name'],
      en=K.en(t['en'], size='12px'), blurb=t['blurb'], stats=t['stats'], date=t['date'])

w('''        </div>

        <div style="%(SOFTC)s border: 1px dashed #D8D2C6; background: transparent; padding: 22px 24px; margin-top: 16px;">
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: %(DIM)s; margin-bottom: 11px;">بعدی‌ها</div>''')
for t in PLANNED:
    w('          <p style="font-size: 13.5px; line-height: 1.98; color: %(MID)s; margin: 0 0 9px; max-width: 72ch;">%(t)s</p>', t=t)
w('''        </div>
      </div>
    </section>

    <section id="how" style="max-width: 1060px; margin: 0 auto; padding: 46px 24px 20px;">
      <p style="%(EYE)s">روش</p>
      <h2 style="%(H2)s">هر راهنما با این چهار قاعده نوشته می‌شود</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px; margin-top: 24px;">''')
for i, (t, d) in enumerate(RULES):
    w('''        <div style="%(CARD)s padding: 21px 23px;">
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 10px;">
            <span style="font-size: 12px; font-weight: 800; color: %(AC)s;">%(n)s</span>
            <h3 style="font-size: 14.5px; font-weight: 700; margin: 0; line-height: 1.6;">%(t)s</h3>
          </div>
          <p style="font-size: 13.5px; line-height: 1.98; color: %(MID)s; margin: 0;">%(d)s</p>
        </div>''', n=K.fa('%02d' % (i + 1)), t=t, d=d)

w('''      </div>
      <p style="font-size: 14px; line-height: 2.05; color: %(MID)s; margin: 26px 0 20px; max-width: 70ch;">و یک چیز که این‌جا با «رصدخانه» فرق دارد: رصدخانه ثبتِ چیزی است که اتفاق می‌افتد؛ کارگاه ثبتِ چیزی است که <b>خودت می‌توانی انجام بدهی</b>. آن یکی خبر است، این یکی مهارت.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
        <a href="Watch.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">رصدخانه ←</a>
        <a href="Services.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">هفتادوپنج سرویسِ فروشنی ←</a>
        <a href="AILiteracy.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">معماری سواد هوش مصنوعی ←</a>
      </div>
    </section>

  </main>
''')

w('''
  <footer style="border-top: 1px solid %(LINE)s; background: #FFFFFF;">
    <div style="max-width: 1060px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: %(DIM)s;">رضا هاشمی · کارگاه</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1060,"height":1200}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>
</body>
</html>
''')

html = P.html()
io.open(os.path.join(SRC, 'Workshop.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'chars ·', len(TOOLS), 'tools')
