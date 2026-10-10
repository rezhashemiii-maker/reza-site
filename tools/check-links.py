# -*- coding: utf-8 -*-
"""بررسی پیوندهای داخلی و لنگرهای خروجی سایت."""
import re, os, glob, sys
os.chdir('/home/user/reza-site')
pages = {os.path.basename(f): re.sub(r'<script\b.*?</script>', '', open(f, encoding='utf-8').read(), flags=re.S)
         for f in glob.glob('*.html')}
ids = {k: set(re.findall(r'id="([^"]+)"', v)) for k, v in pages.items()}
bad = {}
for f, t in sorted(pages.items()):
    for href in re.findall(r'<a [^>]*href="([^"]+)"', t):
        if href.startswith(('http', 'mailto:', 'data:')):
            continue
        page, sep, frag = href.partition('#')
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
