# -*- coding: utf-8 -*-
"""انتقال آرتبوردهای آرتیفکت به src/ مخزن، با پاک‌سازی جاهای ناتمام."""
import io, os, re, sys

AF = '/tmp/claude-0/-home-user-reza-site/33dd78ae-a2ff-5a12-96f6-fd8a58212c20/scratchpad/artifact-files/53663088-e6c9-4773-90f2-fa9a60239869/project'
SRC = '/home/user/reza-site/src'

IA = ['Writing', 'Books', 'About', 'Work', 'Process', 'FAQ', 'Contact']
AIE = ['AiEngineer'] + ['Aie%d%02d' % (s, i) for s in range(1, 7) for i in range(1, 11)]
NAMES = IA + AIE

GITHUB = 'https://github.com/rezhashemiii-maker/reza-site'

def clean(t, name):
    n = []

    # ۱) جانگهدارهای نیمه‌کارهٔ شبکه‌های اجتماعی
    before = t
    t = t.replace(
        '''            <span style="font-size: 13px; color: #666158;">[لینک LinkedIn]</span>\n'''
        '''            <span style="font-size: 13px; color: #666158;">[لینک GitHub]</span>\n''',
        '''            <a href="%s" target="_blank" rel="noopener" style="font-size: 13px; color: #4A4F58; direction: ltr; unicode-bidi: isolate;">github.com/rezhashemiii-maker</a>\n''' % GITHUB)
    if t != before: n.append('footer-links')

    before = t
    t = t.replace(
        '''<p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0;">[لینک LinkedIn] · [لینک GitHub]</p>''',
        '''<p style="font-size: 13px; line-height: 1.9; color: #4A4F58; margin: 0;">مخزن سایت: <a href="%s" target="_blank" rel="noopener" style="font-weight: 600; direction: ltr; unicode-bidi: isolate;">github.com/rezhashemiii-maker/reza-site</a></p>''' % GITHUB)
    if t != before: n.append('about-links')

    # ۲) برچسب فاز توسعه، که روی سایت زنده معنا ندارد
    before = t
    t = t.replace('<span style="font-size: 12.5px; color: #666158;">فاز ۱ · طراحی و نمایش</span>',
                  '<a href="Library.dc.html" style="font-size: 12.5px; color: #666158;">کتابخانهٔ منابع سایت</a>')
    if t != before: n.append('phase-label')

    # ۳) کمپین فقط روی آرتیفکت است؛ در مخزن پیوندش حذف می‌شود
    before = t
    t = t.replace('<a href="Campaign.dc.html" style="font-size: 13.5px; font-weight: 700; color: #2F5233;">مشاهده کمپین ←</a>',
                  '<span style="font-size: 12.5px; color: #666158;">این کمپین روی سایت منتشر نشده است.</span>')
    if t != before: n.append('campaign-link')

    before = t
    t = t.replace(
        '''<p style="font-size: 13px; line-height: 1.9; color: #666158; margin: 0;">یا اگر ترجیح می‌دهی: [لینک LinkedIn] · [لینک GitHub]</p>''',
        '''<p style="font-size: 13px; line-height: 1.9; color: #4A4F58; margin: 0;">یا اگر ترجیح می‌دهی، کد همین سایت را این‌جا ببین:<br><a href="%s" target="_blank" rel="noopener" style="font-weight: 600; direction: ltr; unicode-bidi: isolate;">github.com/rezhashemiii-maker/reza-site</a></p>''' % GITHUB)
    if t != before: n.append('contact-links')

    # ۴) بازگشت به نوشته‌ها در مخزن یعنی همان بخش صفحهٔ اصلی هم کار کند
    #    (پیوندهای .dc.html را خود خط لوله بازنویسی می‌کند)

    # ۵) نشانی ایمیل تکراری در فوتر و بدنه — دست‌نخورده می‌ماند
    return t, n

if __name__ == '__main__':
    total = []
    for name in NAMES:
        src = os.path.join(AF, name + '.dc.html')
        t = io.open(src, encoding='utf-8').read()
        t, notes = clean(t, name)
        io.open(os.path.join(SRC, name + '.dc.html'), 'w', encoding='utf-8').write(t)
        total.append((name, len(t), notes))
    for name, n, notes in total:
        if notes: print('%-12s %7d  %s' % (name, n, ', '.join(notes)))
    print('--- %d فایل منتقل شد' % len(total))
    left = []
    for name in NAMES:
        t = io.open(os.path.join(SRC, name + '.dc.html'), encoding='utf-8').read()
        if '[لینک' in t or 'فاز ۱' in t or 'Campaign.dc.html' in t:
            left.append(name)
    print('جانگهدار باقی‌مانده:', left or 'هیچ')

# ---------------------------------------------------------------- توضیح متا
# صفحه‌های منتقل‌شده description ندارند؛ از بند اول خودشان می‌سازیمش.
def describe():
    import json, html as H
    OUT = {}
    FAD = '۰۱۲۳۴۵۶۷۸۹'
    def fa(n):
        return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))

    def text(x):
        x = re.sub(r'<[^>]+>', '', x)
        return H.unescape(re.sub(r'\s+', ' ', x)).strip()

    hand = {
        'ai-engineer.html': 'مسیر مهندس هوش مصنوعی شدن در شش مرحله، از پایتون و مهندسی نرم‌افزار تا RAG و Agentهای آمادهٔ Production — با ۶۰ پروژهٔ کاربردی که دیتاستشان رایگان است و هر کدام صفحهٔ خودش را دارد.',
        'writing.html': 'فهرست نوشته‌های رضا هاشمی: یادگیری ماشین، امنیت، شطرنج، سواد هوش مصنوعی و پروندهٔ عراق — هر مفهوم با ارجاع به مقالهٔ اصلی‌اش.',
        'books.html': 'کتاب‌ها و منابعی که خوانده‌ام و ارزش معرفی دارند، دسته‌بندی‌شده بر اساس حوزه.',
        'about.html': 'دربارهٔ رضا هاشمی: یادگیرندهٔ یادگیری ماشین با پس‌زمینهٔ کشاورزی و برندسازی، و اینکه چرا این صفحه‌ها را می‌سازم.',
        'work.html': 'کارهایی که ساخته‌ام: سیستم ثبت و تصمیم مزرعهٔ دُرّین، دموی پل فرماندهی، و پروژه‌های تحقیقاتی سایت.',
        'process.html': 'روش کار: از فهمیدن مسئله تا تحویل سیستمی که تیم خودتان بتواند تغییرش بدهد.',
        'faq.html': 'پرسش‌های پرتکرار دربارهٔ ساخت سیستم ثبت و تصمیم: زمان، مالکیت کد و داده، دادهٔ حساس، و اینکه کی اصلاً به سیستم نیاز ندارید.',
        'contact.html': 'راه‌های تماس با رضا هاشمی برای ساخت سیستم ثبت و تصمیم یا گفت‌وگو دربارهٔ یادگیری ماشین.',
    }
    OUT.update(hand)

    for s in range(1, 7):
        for i in range(1, 11):
            name = 'Aie%d%02d' % (s, i)
            t = io.open(os.path.join(SRC, name + '.dc.html'), encoding='utf-8').read()
            h1 = text(re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S).group(1))
            lead = text(re.search(r'</h1>\s*<p[^>]*>(.*?)</p>', t, re.S).group(1))
            what = re.search(r'این پروژه چیه\؟</h2>\s*<p[^>]*>(.*?)</p>', t, re.S)
            d = '%s — پروژهٔ %s.%s از مسیر مهندس هوش مصنوعی. %s' % (h1, fa(s), fa(i), lead)
            if what:
                d += ' ' + text(what.group(1))
            OUT['aie-%d%02d.html' % (s, i)] = d[:300]

    io.open(os.path.join(SRC, 'descriptions.auto.json'), 'w', encoding='utf-8').write(
        json.dumps(OUT, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    print('توضیح متا برای %d صفحه نوشته شد' % len(OUT))

describe()
