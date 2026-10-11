# -*- coding: utf-8 -*-
"""اجزای مشترک «کارگاه».

قالب‌ها با کلیدِ نام‌دار پر می‌شوند (`%(AC)s`) نه با ترتیب — صفحه‌های این بخش
بلندند و شمردنِ آرگومان در بلوک بلند همیشه جایی غلط از آب درمی‌آید.
"""
import re

V = dict(
    AC='#6B2152',          # ارغوانیِ کارگاه
    SOFT='#F3E4EE',
    INK='#16181C',
    MID='#45494F',
    DIM='#666158',
    LINE='#E4E1D6',
    RUST='#B4530E',
    GREEN='#2F5233',
)
V['LTR'] = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
V['EYE'] = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %(AC)s; margin: 0 0 12px;' % V
V['H2'] = 'font-size: clamp(21px, 2.8vw, 28px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
V['H3'] = 'font-size: 16px; font-weight: 800; margin: 0 0 10px; line-height: 1.6;'
V['BODY'] = 'font-size: 15.5px; line-height: 2.1; color: %(MID)s; max-width: 68ch; margin: 0 0 16px;' % V
V['LEAD'] = 'font-size: 16.5px; line-height: 2.05; color: %(MID)s; max-width: 66ch; margin: 0 0 16px;' % V
V['SOFTC'] = 'background: #FAFAF7; border: 1px solid %(LINE)s; border-radius: 14px;' % V
V['CARD'] = 'background: #FFFFFF; border: 1px solid %(LINE)s; border-radius: 16px;' % V

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n):
    return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# نام‌های لاتینِ رابط داخل جملهٔ فارسی می‌آیند و بدون جداسازی، نقطهٔ پایان جمله
# به سمت غلط می‌پرد و پاره‌شدنِ خط هم «Epic Scale.» را «Scale.» و «Epic» می‌کند.
# LRI/PDI همان کار unicode-bidi: isolate را در متن ساده می‌کند.
LRI, PDI = '\u2066', '\u2069'
_TAG = re.compile(r'<[^>]+>')
_LAT = re.compile(r'[A-Za-z0-9][A-Za-z0-9._+\-/]*(?:[ ][A-Za-z0-9][A-Za-z0-9._+\-/]*)*')
_HASLAT = re.compile(r'[A-Za-z]')


def _wrap(m):
    run = m.group(0)
    if not _HASLAT.search(run):          # عددِ تنها، نه نامِ لاتین
        return run
    tail = ''
    while run and run[-1] in '._+-/':
        tail = run[-1] + tail
        run = run[:-1]
    return LRI + run + PDI + tail


def iso(t):
    """جداسازیِ دوجهتهٔ نام‌های لاتین، بدون دست‌زدن به برچسب‌های HTML."""
    out, last = [], 0
    for m in _TAG.finditer(t):
        out.append(_LAT.sub(_wrap, t[last:m.start()]))
        out.append(m.group(0))
        last = m.end()
    out.append(_LAT.sub(_wrap, t[last:]))
    return ''.join(out)


def en(txt, size='13px', weight='700'):
    """برچسبِ لاتینِ رابط، همیشه روی خطِ خودش و در جعبهٔ چپ‌به‌راست.

    قاعدهٔ سایت: فارسی و انگلیسی در یک خط قاتی نمی‌شوند. این‌جا که کلِ موضوع
    «این دکمه چه اسمی دارد» است، اسم انگلیسی در بلوک جدا می‌نشیند."""
    return ('<span style="%s display: inline-block; font-size: %s; font-weight: %s; '
            'color: %s; background: %s; border-radius: 7px; padding: 3px 9px; '
            'max-width: 100%%; overflow-wrap: anywhere;">%s</span>'
            % (V['LTR'], size, weight, V['AC'], V['SOFT'], esc(txt)))


class Page(object):
    """انباشتِ خروجی با پرکردنِ نام‌دارِ قالب."""

    def __init__(self, **extra):
        self.o = []
        self.v = dict(V)
        self.v.update(extra)

    def w(self, s, **extra):
        if '%(' in s:
            vals = dict(self.v)
            vals.update(extra)
            s = s % vals
        self.o.append(s)

    def html(self):
        return ''.join(self.o)


def head(title, accent_css=True):
    return '''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>%s</title>
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
  a{color:#6B2152;text-decoration:none}
  a:hover{text-decoration:underline}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:84px}
  b,strong{font-weight:700;color:#16181C}
  ::selection{background:#F3E4EE;color:#6B2152}
  @media (max-width:860px){
    nav[data-sections]{display:none !important}
    div[data-sectionlist]{display:flex !important}
  }
</style>
</helmet>

<div style="width: 100%%; min-height: 100vh; background: #F5F3EE; direction: rtl;">
''' % title


def header(back_href, back_label, nav):
    out = ['''
  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1060px; margin: 0 auto; padding: 12px 24px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
      <a href="%s" style="font-size: 13px; font-weight: 600; color: #45494F;">← %s</a>
      <nav data-sections="1" style="display: flex; gap: 1px; margin-inline-start: auto; flex-wrap: wrap;">''' % (back_href, back_label)]
    for sid, lab in nav:
        out.append('        <a href="#%s" style="font-size: 11.5px; color: #45494F; padding: 5px 8px; border-radius: 999px;">%s</a>' % (sid, lab))
    out.append('''      </nav>
    </div>
  </header>
''')
    return '\n'.join(out)


def sectionlist(nav):
    out = ['      <div data-sectionlist="1" style="display: none; gap: 6px; flex-wrap: wrap; margin-top: 24px;">']
    for sid, lab in nav:
        out.append('        <a href="#%s" style="font-size: 12.5px; color: #45494F; background: #FFFFFF; border: 1px solid %s; padding: 7px 13px; border-radius: 999px;">%s</a>'
                   % (sid, V['LINE'], lab))
    out.append('      </div>')
    return '\n'.join(out)


def footer(tag):
    return '''
  <footer style="border-top: 1px solid %s; background: #FFFFFF;">
    <div style="max-width: 1060px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Workshop.dc.html" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به کارگاه</a>
      <span style="font-size: 12.5px; color: %s;">%s</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1060,"height":1400}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>
</body>
</html>
''' % (V['LINE'], V['DIM'], tag)
