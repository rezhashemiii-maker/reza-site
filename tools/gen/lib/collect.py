# -*- coding: utf-8 -*-
"""گردآوری همهٔ ارجاع‌های پراکندهٔ سایت در یک فهرست یکپارچه."""
import re, io, os, sys, json, html, unicodedata
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402

SP = '/tmp/claude-0/-home-user-reza-site/33dd78ae-a2ff-5a12-96f6-fd8a58212c20/scratchpad'
SRC = SRC
FAD = '۰۱۲۳۴۵۶۷۸۹'

def fa2int(s):
    return int(''.join(str(FAD.index(c)) for c in s))

def deFa(s):
    return ''.join(str(FAD.index(c)) if c in FAD else c for c in s)

def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

NOISE = (
    r'arXiv[:\s]*\d{4}\.\d{4,5}',   # شناسهٔ arXiv مثل 2006.01855
    r'\b\d{4}/\d{4}\b',             # شمارهٔ مقرره مثل 2024/1689
    r'\(\d{1,4}\)',                 # شمارهٔ شماره/جلد مثل (6419)
    r'\b\d{3}\(\d+\)',
)

def year_of(*texts):
    for t in texts:
        t = deFa(t or '')
        for n in NOISE:
            t = re.sub(n, ' ', t)
        ys = [int(y) for y in re.findall(r'\b(19\d\d|20[0-2]\d)\b', t)]
        if ys:
            return min(ys)          # سال انتشار اول، نه سال ویرایش بعدی
    return None

def norm(t):
    t = unicodedata.normalize('NFKD', (t or '').lower())
    t = re.sub(r'[^a-z0-9 ]+', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

STD = ('iso/iec', 'regulation', 'nist ', 'owasp', 'digcomp', 'tcsec', 'common criteria',
       'rfc ', 'framework for citizens')
BOOKPAT = ('press', 'o’reilly', "o'reilly", 'mit press', 'arco', 'mouton', 'addison',
           'wiley', 'springer', 'no starch')

def kind_of(en, fa, group=''):
    e, f, g = en.lower(), fa or '', group or ''
    if 'کتاب' in g or 'کتاب' in f[:40]:
        return 'کتاب'
    if any(k in e for k in STD):
        return 'استاندارد'
    # «Report» فقط وقتی نشانهٔ گزارش است که در نام نشریه بیاید، نه در عنوان اثر
    outside = re.sub(r'"[^"]*"', ' ', en).lower()
    if re.search(r'\breport\b', outside) or 'گزارش' in g:
        return 'گزارش'
    if any(k in e for k in BOOKPAT):
        return 'کتاب'
    return 'مقاله'

# عنوان بدون گیومه دنبالهٔ ناشر/سال می‌گیرد؛ آن دنباله بریده می‌شود
TAIL = re.compile(r'(19\d\d|20[0-2]\d|press|mouton|arco|o.reilly|mit |wiley|springer|'
                  r'dissertation|edition|c\.\s*\d|vol\b|pp\.)', re.I)

def trim_title(t):
    parts = [p.strip() for p in t.split(',')]
    while len(parts) > 1 and TAIL.search(parts[-1]):
        parts.pop()
    return ', '.join(parts).strip(' ,.')

out = []

# ---------------------------------------------------------------- ۱) امنیت
sys.path.insert(0, os.path.join(SP, 'sec'))
import data as secdata
CATNAME = {c['key']: c['name'] for c in secdata.CATS}
for (y, cat, kind, tfa, ten, who, impact, note, link) in secdata.ITEMS:
    out.append(dict(year=y, titleEn=ten, titleFa=tfa, who=who, kind=kind, note=note,
                    link=link or None, impact=impact, domains=['امنیت'], topic=CATNAME[cat]))
sys.path.pop(0)

# ---------------------------------------------------------------- ۲) سواد هوش مصنوعی و ۳) شطرنج
def from_refs(mod_dir, mod_name, domain):
    sys.path.insert(0, os.path.join(SP, mod_dir))
    for m in list(sys.modules):
        if m == mod_name:
            del sys.modules[m]
    mod = __import__(mod_name)
    rows = []
    for gname, _gwhy, items in mod.REFS:
        for fa, en in items:
            # عنوان انگلیسی: داخل گیومه، وگرنه بعد از اولین خط تیره
            mq = re.search(r'"([^"]+)"', en)
            title = mq.group(1) if mq else trim_title(re.split(r'\s+—\s+', en, 1)[-1])
            who = re.split(r'\s+—\s+', en, 1)[0]
            mfa = re.search(r'«([^»]+)»', fa)
            # توضیح، نه تکرار عنوان: فقط پرانتز پایانی که در آن «چه چیزی را جلو برد» نوشته شده
            mp = re.search(r'\(([^()]*)\)\s*$', fa)
            note = mp.group(1).strip() if mp else ''
            rows.append(dict(year=year_of(en, fa), titleEn=title.strip(), titleFa=(mfa.group(1) if mfa else None),
                             who=who.strip(), kind=kind_of(en, fa, gname), note=note, link=None,
                             impact=None, domains=[domain], topic=gname, raw_en=en))
    sys.path.pop(0)
    return rows

out += from_refs('a16', 'data', 'سواد هوش مصنوعی')
out += from_refs('chess', 'data', 'شطرنج')

# ---------------------------------------------------------------- ۴) مسیر یادگیری و ۵) نظریهٔ بازی
CARD = re.compile(
  r'<a href="(https://[^"]+)" target="_blank" rel="noopener" style="display: block;[^"]*">'
  r'<div style="[^"]*direction: ltr;[^"]*">(.*?)</div>'
  r'<div style="[^"]*">(.*?)</div>'
  r'<div style="[^"]*">(.*?)</div>', re.S)

for fname, domain in (('Learn.dc.html', 'یادگیری ماشین'), ('GameTheory.dc.html', 'نظریهٔ بازی')):
    s = io.open(os.path.join(SRC, fname), encoding='utf-8').read()
    for link, title, meta, note in CARD.findall(s):
        title, meta, note = strip_tags(title), strip_tags(meta), strip_tags(note)
        bits = [b.strip() for b in meta.split('·')]
        who = bits[0] if bits else ''
        venue = bits[2] if len(bits) > 2 else None
        out.append(dict(year=year_of(meta, title), titleEn=title, titleFa=None,
                        who=who + (' · ' + venue if venue else ''), kind=kind_of(title + ' ' + (venue or ''), '', ''),
                        note=note, link=link, impact=None, domains=[domain], topic=None))

# ---------------------------------------------------------------- ادغام تکراری‌ها
merged = {}
order = []
for r in out:
    k = norm(r['titleEn'])[:70]
    if k in merged:
        m = merged[k]
        for d in r['domains']:
            if d not in m['domains']:
                m['domains'].append(d)
        if not m.get('link') and r.get('link'):
            m['link'] = r['link']
        if not m.get('titleFa') and r.get('titleFa'):
            m['titleFa'] = r['titleFa']
        if m.get('year') is None:
            m['year'] = r['year']
        # یادداشت دوم را نگه می‌داریم تا در صفحه هر دو نگاه دیده شود
        m.setdefault('alt', []).append(dict(domain=r['domains'][0], note=r['note']))
    else:
        merged[k] = dict(r)
        order.append(k)

rows = [merged[k] for k in order]
rows.sort(key=lambda r: (r['year'] is None, r['year'] or 0, norm(r['titleEn'])))

print('خام:', len(out), '| یکتا:', len(rows), '| چنددامنه‌ای:', sum(1 for r in rows if len(r['domains']) > 1))
print('بدون سال:', [r['titleEn'][:50] for r in rows if r['year'] is None])
from collections import Counter
print('دامنه:', Counter(d for r in rows for d in r['domains']))
print('نوع:', Counter(r['kind'] for r in rows))
print('با پیوند:', sum(1 for r in rows if r['link']))
io.open(os.path.join(SP, 'lib', 'refs.json'), 'w', encoding='utf-8').write(
    json.dumps(rows, ensure_ascii=False, indent=1))
