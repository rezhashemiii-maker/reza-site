# -*- coding: utf-8 -*-
"""بررسی پیوندهای داخلی و لنگرهای خروجی سایت."""
import re, os, glob, sys

# ریشهٔ مخزن از روی جای خودِ این فایل درمی‌آید، نه از یک مسیر ثابت؛
# وگرنه روی رانرِ گیت‌هاب که مخزن جای دیگری است، اجرا نمی‌شود.
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# وقتی سایت زیرپوشه‌ای منتشر می‌شود (مثل /reza-site/)، صفحهٔ ۴۰۴ ناچار است
# پیوندهایش را مطلق بنویسد، چون در هر عمقی سرو می‌شود. آن پیشوند باید
# پیش از رسیدگی برداشته شود، وگرنه هر پیوندِ درست «شکسته» شمرده می‌شود.
#
# پیشوند را از خودِ خروجیِ ساخته‌شده درمی‌آوریم، نه از متغیر محیطی: در
# گردش‌کار، SITE_URL فقط به قدمِ ساخت داده می‌شود و این قدم آن را ندارد.
# هر طور که ساخته شده باشد، نشانیِ site.css همان پیشوند را نشان می‌دهد.
def _base():
    try:
        t404 = open('404.html', encoding='utf-8').read()
    except OSError:
        t404 = ''
    m = re.search(r'href="(/[^"]*?)assets/site\.css"', t404)
    if m:
        return m.group(1).strip('/')
    site = (os.environ.get('SITE_URL') or '').rstrip('/')
    if site:
        from urllib.parse import urlparse
        return urlparse(site + '/').path.strip('/')
    return ''


BASE = _base()
pages = {os.path.basename(f): re.sub(r'<script\b.*?</script>', '', open(f, encoding='utf-8').read(), flags=re.S)
         for f in glob.glob('*.html')}
ids = {k: set(re.findall(r'id="([^"]+)"', v)) for k, v in pages.items()}
bad = {}
for f, t in sorted(pages.items()):
    for href in re.findall(r'<a [^>]*href="([^"]+)"', t):
        if href.startswith(('http', 'mailto:', 'data:')):
            continue
        page, sep, frag = href.partition('#')
        if BASE and page.startswith('/' + BASE):
            page = page[len(BASE) + 1:]
        page = page.lstrip('/')
        if page in ('', '.', './'):
            target = 'index.html' if page else f
        else:
            target = page.lstrip('./')
        if target not in pages:
            bad.setdefault(f, set()).add(href + '  [صفحه نیست]')
        elif frag and frag not in ids[target]:
            bad.setdefault(f, set()).add(href + '  [لنگر نیست]')
for f, s in sorted(bad.items()):
    print(f, '→', sorted(s))
n = sum(len(s) for s in bad.values())
print('پیوند شکسته:', n)
sys.exit(1 if n else 0)
