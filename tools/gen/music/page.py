# -*- coding: utf-8 -*-
"""«ریاضیاتِ موسیقی» → src/Music.dc.html

هفت شب قصه، برای بلند خواندن پیش از خواب. متن برای بچه است و بخشِ فنی
پایینِ صفحه، جدا، برای کسی که می‌خواند.

صدا: هر نت از سه هارمونیک ساخته می‌شود (f، ۲f، ۳f). این فقط تزئین نیست —
با موجِ سادهٔ سینوسی، «پنجمِ دقیق» و «پنجمِ پیانو» عیناً یک‌جور شنیده
می‌شوند و شبِ ششم بی‌معنا می‌شود. با هارمونیک سوم، ضربانِ ۱٫۵ هرتز
بینشان شنیدنی می‌شود.
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from paths import SRC  # noqa: E402
import story as S  # noqa: E402

V = dict(
    AC='#3C4A86',        # آبیِ شب
    SOFT='#E7EAF7',
    INK='#16181C',
    MID='#45494F',
    DIM='#666158',
    LINE='#E4E1D6',
    WARM='#B4530E',
    WSOFT='#F7E3D6',
    GREEN='#2F5233',
    V2='#8A6A1F',        # طلاییِ چراغ — فقط برای افزوده‌های ویرایش دوم
    V2SOFT='#FBF5E6',
)
V['LTR'] = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
V['EYE'] = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %(AC)s; margin: 0 0 12px;' % V
V['H2'] = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 18px; line-height: 1.45;'
V['BODY'] = 'font-size: 16px; line-height: 2.12; color: %(MID)s; max-width: 66ch; margin: 0 0 17px;' % V
V['LEAD'] = 'font-size: 17.5px; line-height: 2.08; color: %(MID)s; max-width: 64ch; margin: 0 0 17px;' % V
V['CARD'] = 'background: #FFFFFF; border: 1px solid %(LINE)s; border-radius: 16px;' % V
V['SOFTC'] = 'background: #FAFAF7; border: 1px solid %(LINE)s; border-radius: 14px;' % V
# متنِ قصه درشت‌تر و بازتر است، چون قرار است در نور کم و بلند خوانده شود
V['TALE'] = 'font-size: 19px; line-height: 2.25; color: #23262B; max-width: 58ch; margin: 0 0 15px;'
# بندِ افزوده: همان قلمِ قصه، با نوارِ طلایی در کنارش
V['TALE2'] = ('font-size: 19px; line-height: 2.25; color: #23262B; max-width: 58ch; '
              'margin: 0 0 15px; border-inline-start: 3px solid %(V2)s; '
              'background: %(V2SOFT)s; border-radius: 0 10px 10px 0; padding: 10px 16px 10px 14px;') % V

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))


def add_in_box(t):
    """افزودهٔ ویرایش دوم، داخلِ جعبه‌ای که از ویرایش اول مانده."""
    if not t:
        return ''
    return ('\n        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; '
            'margin: 11px 0 0; padding-inline-start: 13px; border-inline-start: 3px solid %(V2)s;">'
            '<span style="display: block; font-size: 10px; font-weight: 700; '
            'letter-spacing: 0.08em; color: %(V2)s; margin-bottom: 5px;">افزودهٔ ویرایش دوم</span>'
            '%(t)s</p>') % dict(V, t=t)

o = []
def w(s, **extra):
    vals = dict(V); vals.update(extra)
    o.append(s % vals if '%(' in s else s)

NAV = [('n%d' % n['n'], 'شب %s' % fa(n['n'])) for n in S.NIGHTS]
NAV += [('self', 'برای خودت'), ('v2', 'ویرایش دوم'), ('src', 'منابع')]

w('''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>ریاضیاتِ موسیقی — هفت شب قصه برای پیش از خواب</title>
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
  a{color:#3C4A86;text-decoration:none}
  a:hover{text-decoration:underline}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  b,strong{font-weight:700;color:#16181C}
  ::selection{background:#E7EAF7;color:#3C4A86}
  @media (max-width:860px){
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

    <section style="max-width: 1000px; margin: 0 auto; padding: 56px 24px 26px;">
      <p style="%(EYE)s">قصه برای پیش از خواب · هفت شب · ویرایش دوم</p>
      <h1 style="font-size: clamp(30px, 4.6vw, 48px); font-weight: 800; margin: 0 0 20px; line-height: 1.35; letter-spacing: -0.01em;">ریاضیاتِ موسیقی</h1>
      <p style="%(LEAD)s">این یک درس نیست. هفت شب قصهٔ کوتاه است که بلند می‌خوانی، و تهش بچه یکی از قدیمی‌ترین و زیباترین کشف‌های آدمی را می‌داند — بی‌آنکه بفهمد ریاضی یاد گرفته.</p>
      <p style="%(BODY)s">هر شب حدود چهار دقیقه طول می‌کشد. هیچ ابزاری لازم نیست جز صدای خودتان، یک کِش، و اگر بود، یک ساز. چند جا هم دکمهٔ صدا هست که با هم گوش می‌دهید.</p>

      <div style="background: %(SOFT)s; border-inline-start: 4px solid %(AC)s; border-radius: 13px; padding: 18px 21px; margin: 24px 0 0; max-width: 68ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 10px;">سه چیز، پیش از شب اول</div>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0 0 10px;"><b>توضیح نده.</b> قصه را بخوان و کاری که گفته را بکن. فهمیدن کارِ خودش است، و دیرتر می‌آید.</p>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0 0 10px;"><b>عجله نکن.</b> هر شب یک شب. اگر شبِ دوم را دو بار خواست، دو بار بخوان.</p>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0;"><b>بخشِ فنی پایینِ صفحه است</b>، نه وسطِ قصه — تا وقتِ خواندن حواست پرت نشود. اگر خودت کنجکاو شدی، بعد از خواباندنش بخوانش.</p>
      </div>

      <div style="border-inline-start: 4px solid %(V2)s; background: %(V2SOFT)s; border-radius: 0 13px 13px 0; padding: 16px 20px; margin: 20px 0 0; max-width: 72ch;">
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0;"><b>ویرایش دوم.</b> قصه یک بار نوشته شد و یک بار خوانده شد؛ جاهایی که موقع خواندن گیر داشت باز شدند. هر چیزی که تازه است <b>نوارِ طلایی</b> کنارش دارد، مثل همین کادر. فهرستِ کاملِ تغییرها <a href="#v2">پایینِ صفحه</a> است.</p>
      </div>

      <div data-sectionlist="1" style="display: none; gap: 6px; flex-wrap: wrap; margin-top: 24px;">''')
for sid, lab in NAV:
    w('        <a href="#%(sid)s" style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 7px 12px; border-radius: 999px;">%(lab)s</a>',
      sid=sid, lab=lab)
w('      </div>\n    </section>\n')

# ------------------------------------------------------------------ هفت شب
for i, N in enumerate(S.NIGHTS):
    white = (i % 2 == 1)
    bg = '#FFFFFF' if white else 'transparent'
    bd = ('border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s;' % V) if white else ''
    w('''
    <section id="n%(n)s" style="background: %(bg)s; %(bd)s margin-top: 34px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 46px 24px;">
      <p style="%(EYE)s">شب %(nfa)s</p>
      <h2 style="%(H2)s">%(t)s</h2>''', n=N['n'], nfa=fa(N['n']), t=N['t'], bg=bg, bd=bd)

    first2 = True
    for line in N['story']:
        if isinstance(line, tuple):
            tag = ('<span style="display: block; font-size: 10.5px; font-weight: 700; '
                   'letter-spacing: 0.08em; color: %(V2)s; margin-bottom: 7px;">'
                   'افزودهٔ ویرایش دوم</span>') % V if first2 else ''
            w('      <p style="%(TALE2)s">%(tag)s%(t)s</p>', t=line[1], tag=tag)
            first2 = False
        else:
            w('      <p style="%(TALE)s">%(t)s</p>', t=line)

    if N['play']:
        w('''      <div style="%(CARD)s padding: 20px 22px; margin: 22px 0 20px; max-width: 68ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 13px;">با هم گوش بدهید</div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">''')
        for lab, tones, mode in N['play']:
            w('''          <button data-tone="%(tones)s" data-mode="%(mode)s" style="font-size: 13.5px; font-weight: 600; padding: 10px 16px; border-radius: 10px; cursor: pointer; font-family: inherit; border: 1px solid #C6CCE4; background: #FFFFFF; color: %(AC)s;">%(lab)s</button>''',
              lab=lab, tones=tones, mode=mode)
        w('''        </div>
        <p style="font-size: 12px; color: %(DIM)s; margin: 12px 0 0;">اگر صدایی نیامد، صدای گوشی را بالا ببر و دوباره بزن.</p>
      </div>''')

    w('''      <div style="background: %(WSOFT)s; border-inline-start: 4px solid %(WARM)s; border-radius: 13px; padding: 17px 20px; margin: 20px 0 16px; max-width: 68ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(WARM)s; margin-bottom: 9px;">با هم امتحان کنید</div>
        <p style="font-size: 15px; line-height: 2.1; color: %(MID)s; margin: 0;">%(do)s</p>%(do2)s
      </div>

      <div style="%(SOFTC)s padding: 17px 20px; max-width: 68ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(DIM)s; margin-bottom: 9px;">اگر پرسید</div>
        <p style="font-size: 14.5px; font-weight: 700; color: %(INK)s; line-height: 1.9; margin: 0 0 9px;">«%(ask)s»</p>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0;">%(answer)s</p>%(ans2)s
      </div>''', do=N['do'], ask=N['ask'], answer=N['answer'],
      do2=add_in_box(N.get('do2')), ans2=add_in_box(N.get('answer2')))

    for title, body in N.get('extra', []):
        w('''      <div style="border: 1px solid #E6DCC2; border-inline-start: 3px solid %(V2)s; background: %(V2SOFT)s; border-radius: 13px; padding: 18px 21px; margin: 16px 0 0; max-width: 68ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(V2)s; margin-bottom: 9px;">افزودهٔ ویرایش دوم — %(title)s</div>
        <p style="font-size: 15px; line-height: 2.15; color: %(MID)s; margin: 0;">%(body)s</p>
      </div>''', title=title, body=body)

    w('      </div>\n    </section>\n')


# ------------------------------------------------------------------ برای خودت
w('''
    <section id="self" style="background: #FFFFFF; border-top: 1px solid %(LINE)s; border-bottom: 1px solid %(LINE)s; margin-top: 38px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">بعد از قصه</p>
      <h2 style="%(H2)s">همان هفت شب، این بار با عدد</h2>
      <p style="%(BODY)s">این بخش برای بچه نیست. برای توست، که اگر پرسید «واقعاً؟» بدانی جوابش چیست و کجا باید احتیاط کنی.</p>

      <h3 style="font-size: 16px; font-weight: 800; margin: 26px 0 12px;">نسبت‌ها</h3>
      <p style="%(BODY)s">سیمی که به دو سومِ طولش کوتاه شود، یک‌ونیم برابر تندتر می‌لرزد. طول و بسامد وارونهٔ هم‌اند. این‌ها نسبت‌های «طبیعی»اند — همان‌هایی که از هارمونیک‌های خودِ سیم می‌آیند:</p>''')

RATIOS = [
    ('اکتاو', '۲ به ۱', '۱۲۰۰', 'همان صدا، یک پله بالاتر. شبِ دوم.'),
    ('پنجمِ درست', '۳ به ۲', '۷۰۱٫۹۶', 'نزدیک‌ترین دوستِ بعدی. شبِ سوم.'),
    ('چهارمِ درست', '۴ به ۳', '۴۹۸٫۰۴', 'همان پنجم، از آن طرف.'),
    ('سومِ بزرگ', '۵ به ۴', '۳۸۶٫۳۱', 'پلّهٔ بعدیِ سادگی.'),
]
w('      <div style="display: flex; flex-direction: column; gap: 9px; margin: 0 0 22px; max-width: 72ch;">')
for nm, r, cents, note in RATIOS:
    w('''        <div style="%(SOFTC)s padding: 15px 18px; display: flex; gap: 14px; align-items: baseline; flex-wrap: wrap;">
          <span style="font-size: 14px; font-weight: 700; color: %(INK)s; min-width: 7em;">%(nm)s</span>
          <span style="font-size: 14px; font-weight: 800; color: %(AC)s; min-width: 5em;">%(r)s</span>
          <span style="font-size: 12.5px; color: %(DIM)s; min-width: 7em;">%(c)s سنت</span>
          <span style="font-size: 13px; color: %(MID)s; flex: 1; min-width: 180px;">%(note)s</span>
        </div>''', nm=nm, r=r, c=cents, note=note)
w('      </div>')

w('''      <h3 style="font-size: 16px; font-weight: 800; margin: 26px 0 12px;">آن ذرّه‌ای که در شبِ پنجم ماند</h3>''')
w('''      <p style="%(BODY)s">دوازده پلّهٔ «سه به دو» برابر است با <span style="%(LTR)s">(3/2)¹² = 129.746…</span> و هفت اکتاو برابر است با <span style="%(LTR)s">2⁷ = 128</span>. این دو باید یکی می‌شدند؛ نمی‌شوند. نسبتشان <span style="%(LTR)s">531441 / 524288 ≈ 1.0136</span> است، یعنی حدود <b>۲۳٫۴۶ سنت</b> — تقریباً یک‌چهارمِ یک نیم‌پرده. نامش «کمای فیثاغورسی» است.</p>''')
w('''      <p style="%(BODY)s">دلیلش حسابی است، نه موسیقایی: ۲ و ۳ عددِ اول‌اند، پس هیچ توانی از ۳ هیچ‌وقت توانی از ۲ نمی‌شود. همان حرفی که در <a href="Foundations.dc.html#s3">نردبانِ عدد</a> هم آمد — بعضی درها بسته‌اند، و بسته‌بودنشان قابل اثبات است.</p>''')

w('''      <h3 style="font-size: 16px; font-weight: 800; margin: 26px 0 12px;">و دروغِ کوچکِ شبِ ششم</h3>''')
w('''      <p style="%(BODY)s">راهِ حل این شد که هر نیم‌پرده را دقیقاً <span style="%(LTR)s">2^(1/12) ≈ 1.059463</span> بگیرند. آن‌وقت دوازده پلّه دقیقاً می‌شود یک اکتاو، و خطا بینِ همه پخش می‌شود. بهایش این است که پنجمِ پیانو <span style="%(LTR)s">2^(7/12) ≈ 1.498307</span> است نه <span style="%(LTR)s">1.5</span> — حدود <b>دو سنت</b> پایین‌تر. نامش «هم‌خوان‌سازیِ مساوی» است.</p>''')
w('''      <p style="%(BODY)s">دکمه‌های شبِ ششم همین دو تا را پشتِ سر هم می‌زنند: <span style="%(LTR)s">440</span> با <span style="%(LTR)s">660</span>، و <span style="%(LTR)s">440</span> با <span style="%(LTR)s">659.26</span>. چیزی که می‌شنوی یک ضربانِ آرام است، حدود یک‌ونیم بار در ثانیه — و همان ضربان است که کوک‌کنندهٔ پیانو با شمردنش کار می‌کند.</p>''')

w('''      <div style="background: %(SOFT)s; border-inline-start: 4px solid %(AC)s; border-radius: 13px; padding: 18px 21px; margin: 22px 0 0; max-width: 72ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 10px;">چرا اکتاو «همان صدا» شنیده می‌شود</div>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0;">چون سیمِ لرزان یک بسامد تنها تولید نمی‌کند؛ یک بسامدِ پایه دارد و هارمونیک‌هایی روی آن، که دقیقاً دو برابر، سه برابر و بیشترِ پایه‌اند. هارمونیکِ دومِ هر نت، عیناً اکتاوش است. پس گوش پیش از آنکه اکتاو را جدا بشنود، آن را داخلِ خودِ نت شنیده — جوابی که شبِ دوم به زبان بچه گفته شده.</p>
      </div>
      </div>
    </section>
''')

# ------------------------------------------------------------- ویرایش دوم
w("""
    <section id="v2" style="margin-top: 38px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">ویرایش دوم</p>
      <h2 style="%(H2)s">چه چیزی عوض شد، و چرا</h2>
      <p style="%(BODY)s">قصه یک بار نوشته شد و یک بار خوانده شد. این فهرست می‌گوید در خواندن کجا گیر داشت و در ویرایش دوم چطور باز شد. هر افزوده روی صفحه نوارِ طلایی دارد، پس اگر بخواهی می‌توانی دقیقاً ببینی کجا اضافه شده.</p>
      <p style="%(BODY)s">هیچ‌کدام از افزوده‌ها برای بلندتر کردنِ قصه نیستند. قرار بود ساده‌تر شود، نه بیشتر.</p>
      <div style="display: flex; flex-direction: column; gap: 11px; max-width: 72ch;">""")
for i, (t, d) in enumerate(S.CHANGES):
    w("""        <div style="border: 1px solid #E6DCC2; border-inline-start: 3px solid %(V2)s; background: %(V2SOFT)s; border-radius: 13px; padding: 17px 20px;">
          <div style="font-size: 14px; font-weight: 700; color: %(INK)s; margin-bottom: 7px;">%(n)s — %(t)s</div>
          <p style="font-size: 13.5px; line-height: 2.05; color: %(MID)s; margin: 0;">%(d)s</p>
        </div>""", n=fa('%02d' % (i + 1)), t=t, d=d)
w("""      </div>
      </div>
    </section>
""")

# ------------------------------------------------------------------ منابع
w('''
    <section id="src" style="margin-top: 38px;">
      <div style="max-width: 1000px; margin: 0 auto; padding: 48px 24px;">
      <p style="%(EYE)s">روش و منابع</p>
      <h2 style="%(H2)s">کجا باید با احتیاط خواند</h2>
      <p style="%(BODY)s">نسبت‌های این صفحه فیزیک‌اند و جای بحث ندارند: بسامدِ سیم با طولش وارونه است، و هارمونیک‌ها مضربِ درستِ پایه‌اند. ولی یک داستانِ مشهور این وسط هست که <b>غلط</b> است و تقریباً همه‌جا تکرار می‌شود:</p>

      <div style="border: 1px dashed #C6CCE4; border-radius: 13px; padding: 18px 21px; margin: 0 0 22px; max-width: 72ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(WARM)s; margin-bottom: 10px;">افسانهٔ چکش‌های آهنگری</div>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0 0 11px;">روایت می‌گوید فیثاغورس از کنار دکانِ آهنگری گذشت، صدای چکش‌ها را شنید، وزنشان را سنجید و دید نسبت‌هایشان ۱۲ و ۹ و ۸ و ۶ است. این روایت از نیکوماخوس در قرن دوم میلادی مانده.</p>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0;">ولی از نظر فیزیکی ممکن نیست: بسامد با <b>جذرِ کشش</b> رابطه دارد، نه با وزنِ چکش. ویچنتزو گالیله — پدرِ گالیلئو — در سال ۱۵۸۱ همین را با آزمایش نشان داد. آنچه درست است، همان رابطهٔ طولِ سیم است، نه قصهٔ چکش‌ها. این صفحه عمداً قصهٔ چکش‌ها را تعریف نمی‌کند.</p>
      </div>''')

SOURCES = [
    ('ویکی‌پدیا — چکش‌های فیثاغورسی',
     'https://en.wikipedia.org/wiki/Pythagorean_hammers',
     'خودِ افسانه، منبعِ باستانی‌اش، و اینکه چرا از نظر فیزیکی ممکن نیست.'),
    ('ویکی‌پدیا — کمای فیثاغورسی',
     'https://en.wikipedia.org/wiki/Pythagorean_comma',
     'عددِ ۵۳۱۴۴۱ به ۵۲۴۲۸۸ و ۲۳٫۴۶ سنت.'),
    ('ویکی‌پدیا — هم‌خوان‌سازیِ مساوی',
     'https://en.wikipedia.org/wiki/Equal_temperament',
     'ریشهٔ دوازدهمِ دو، و بهایی که پنجم می‌پردازد.'),
    ('ویکی‌پدیا — سریِ هارمونیک در موسیقی',
     'https://en.wikipedia.org/wiki/Harmonic_series_(music)',
     'چرا اکتاو داخلِ خودِ نت از قبل هست.'),
    ('دانشنامهٔ فلسفهٔ استنفورد — فیثاغورس',
     'https://plato.stanford.edu/entries/pythagoras/',
     'چه چیزی واقعاً به فیثاغورس برمی‌گردد و چه چیزی بعدها به او نسبت داده شده.'),
]
w('      <h3 style="font-size: 16px; font-weight: 800; margin: 10px 0 12px;">منابع</h3>')
w('      <div style="display: flex; flex-direction: column; gap: 9px; max-width: 72ch;">')
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

w('''      <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 26px;">
        <a href="Foundations.dc.html" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: %(AC)s; padding: 12px 22px; border-radius: 10px;">ریاضی، از راهِ شکستن ←</a>
        <a href="Plain.dc.html" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid %(LINE)s; padding: 12px 22px; border-radius: 10px;">برنامه‌نویسی به زبان ساده ←</a>
      </div>
      </div>
    </section>
''')

w('''
  </main>

  <footer style="border-top: 1px solid %(LINE)s; background: #FFFFFF;">
    <div style="max-width: 1000px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: %(DIM)s;">رضا هاشمی · ریاضیاتِ موسیقی</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1000,"height":1300}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
  componentDidMount() {
(function () {
  'use strict';
  var ctx = null;
  function audio() {
    if (!ctx) {
      var C = window.AudioContext || window.webkitAudioContext;
      if (!C) { return null; }
      ctx = new C();
    }
    if (ctx.state === 'suspended') { ctx.resume(); }
    return ctx;
  }
  // هر نت سه هارمونیک دارد. با سینوسِ تنها، پنجمِ دقیق و پنجمِ پیانو
  // یک‌جور شنیده می‌شوند و شبِ ششم بی‌اثر می‌ماند.
  var PARTIALS = [[1, 1.0], [2, 0.42], [3, 0.22]];
  function note(c, f, at, dur, gain) {
    PARTIALS.forEach(function (p) {
      var o = c.createOscillator(), g = c.createGain();
      o.type = 'sine';
      o.frequency.value = f * p[0];
      var peak = gain * p[1];
      g.gain.setValueAtTime(0.0001, at);
      g.gain.exponentialRampToValueAtTime(peak, at + 0.05);
      g.gain.setValueAtTime(peak, at + dur - 0.18);
      g.gain.exponentialRampToValueAtTime(0.0001, at + dur);
      o.connect(g); g.connect(c.destination);
      o.start(at); o.stop(at + dur + 0.05);
    });
  }
  function play(freqs, mode) {
    var c = audio();
    if (!c) { return; }
    var t = c.currentTime + 0.03;
    if (mode === 'seq') {
      freqs.forEach(function (f, i) { note(c, f, t + i * 1.15, 1.0, 0.16); });
    } else if (mode === 'both') {
      var g = 0.22 / freqs.length;
      freqs.forEach(function (f) { note(c, f, t, 2.8, g); });
    } else {
      note(c, freqs[0], t, 1.2, 0.18);
    }
  }
  var btns = document.querySelectorAll('button[data-tone]');
  Array.prototype.forEach.call(btns, function (b) {
    b.addEventListener('click', function () {
      var fs = b.getAttribute('data-tone').split(',').map(parseFloat);
      play(fs, b.getAttribute('data-mode') || 'one');
      b.style.background = '#E7EAF7';
      setTimeout(function () { b.style.background = '#FFFFFF'; }, 260);
    });
  });
})();
  }
}
</script>
</body>
</html>
''')

html = ''.join(o)
io.open(os.path.join(SRC, 'Music.dc.html'), 'w', encoding='utf-8').write(html)
print('written', len(html), 'نویسه ·', len(S.NIGHTS), 'شب ·',
      sum(len(n['play']) for n in S.NIGHTS), 'دکمهٔ صدا ·', len(SOURCES), 'منبع')
