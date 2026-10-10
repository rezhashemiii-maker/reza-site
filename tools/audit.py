# -*- coding: utf-8 -*-
"""بررسی بهداشت صفحه‌های ساخته‌شده: تیتر، شناسهٔ تکراری، alt، rel، متا."""
import re, os, glob, collections, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
files = sorted(glob.glob('*.html'))
issues = collections.defaultdict(list)
for f in files:
    raw = open(f, encoding='utf-8').read()
    t = re.sub(r'<script\b.*?</script>', '', raw, flags=re.S)
    h1 = re.findall(r'<h1\b', t)
    # iraq.html یک برنامهٔ تک‌صفحه‌ای است: هر فصل h1 خودش را دارد و
    # هر لحظه فقط یکی‌شان نمایش داده می‌شود؛ بقیه hidden‌اند.
    if len(h1) != 1 and f not in ('404.html', 'iraq.html'):
        issues['h1 != 1'].append('%s (%d)' % (f, len(h1)))
    ids = re.findall(r'\bid="([^"]+)"', t)
    dup = [k for k, v in collections.Counter(ids).items() if v > 1]
    if dup:
        issues['شناسهٔ تکراری'].append('%s: %s' % (f, dup[:5]))
    for img in re.findall(r'<img\b[^>]*>', t):
        if 'alt=' not in img:
            issues['img بدون alt'].append(f)
    for a in re.findall(r'<a\b[^>]*target="_blank"[^>]*>', t):
        if 'rel=' not in a:
            issues['target=_blank بدون rel'].append(f + ' :: ' + a[:80])
    if '<html lang="fa" dir="rtl">' not in raw:
        issues['lang/dir'].append(f)
    title = re.search(r'<title>(.*?)</title>', raw, re.S)
    if not title or not title.group(1).strip():
        issues['بدون عنوان'].append(f)
    elif len(title.group(1)) > 70:
        issues['عنوان بلندتر از ۷۰ نویسه'].append('%s (%d)' % (f, len(title.group(1))))
    d = re.search(r'<meta name="description" content="([^"]*)"', raw)
    if d and len(d.group(1)) > 185:
        issues['توضیح بلندتر از ۱۸۵ نویسه'].append('%s (%d)' % (f, len(d.group(1))))

# دارایی‌های یتیم
used = set()
for f in files:
    raw = open(f, encoding='utf-8').read()
    used |= set(re.findall(r'assets/[A-Za-z0-9_.-]+', raw))
have = {p for p in glob.glob('assets/*')}
orphan = sorted(have - used)
if orphan:
    issues['دارایی یتیم'].extend(orphan)

for k, v in issues.items():
    print('\n### %s (%d)' % (k, len(v)))
    for x in sorted(set(v))[:14]:
        print('   ', x)
    if len(set(v)) > 14: print('    … و %d مورد دیگر' % (len(set(v)) - 14))
if not issues:
    print('هیچ موردی پیدا نشد')

sys.exit(1 if issues else 0)
