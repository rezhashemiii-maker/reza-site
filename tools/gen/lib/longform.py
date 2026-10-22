# -*- coding: utf-8 -*-
"""ساختِ نوشته‌های بلند: همان چند تکه‌ای که در هر دو صفحهٔ بلند تکرار می‌شد.

«پروندهٔ یک کلمه» و «پنج هزار سال تاس» یک زبانِ مشترک دارند: بدنهٔ هر
بخش فهرستی از تکه‌هاست و هر تکه یک شکلِ مشخص دارد.

  str                  بندِ معمولی
  ('h3', t)            زیرعنوان
  ('why', t)           کادرِ نکتهٔ اصلیِ بخش
  ('note', ti, t)      کادرِ حاشیه
  ('quote', t, who)    نقلِ مستقیم
  ('rows', ti, [(a,b)])  فهرستِ دوستونی، به‌شکلِ کارت — نه جدولِ اسکرول‌دار
  ('steps', [(a,b)])   مرحله‌های شماره‌دار
  ('ltr', t)           فرمولِ وسط‌چین
  ('code', t)          کدِ یک‌زبانه
  ('list', [t, …])     فهرستِ شماره‌دارِ ساده

رنگ‌ها از صفحه می‌آیند، نه از این فایل؛ هر صفحه پالتِ خودش را دارد و
این‌جا فقط شکل‌ها نوشته شده‌اند.
"""

FAD = '۰۱۲۳۴۵۶۷۸۹'


def fa(n):
    return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))


def style(V):
    """کلیدهای مشترکِ سبک را به پالتِ صفحه اضافه می‌کند."""
    V = dict(V)
    V['EYE'] = ('font-size: 12px; letter-spacing: 0.1em; font-weight: 700; '
                'color: %(AC)s; margin: 0 0 12px;') % V
    V['H2'] = ('font-size: clamp(23px, 3.2vw, 33px); font-weight: 800; '
               'margin: 0 0 20px; line-height: 1.42; letter-spacing: -0.01em;')
    V['H3'] = ('font-size: 17.5px; font-weight: 800; color: %(INK)s; '
               'margin: 34px 0 14px;') % V
    V['BODY'] = ('font-size: 16.5px; line-height: 2.15; color: #2A2E34; '
                 'max-width: 64ch; margin: 0 0 17px;')
    V['LEAD'] = ('font-size: 18px; line-height: 2.1; color: %(MID)s; '
                 'max-width: 62ch; margin: 0 0 17px;') % V
    V['CARD'] = ('background: #FFFFFF; border: 1px solid %(LINE)s; '
                 'border-radius: 15px;') % V
    V['SOFTC'] = ('background: #FAFAF7; border: 1px solid %(LINE)s; '
                  'border-radius: 14px;') % V
    return V


def writer(V):
    """یک نویسندهٔ تازه برمی‌گرداند: (تکه‌ها، w، block)."""
    o = []

    def w(s, **extra):
        vals = dict(V)
        vals.update(extra)
        o.append(s % vals if '%(' in s else s)

    def block(it):
        if isinstance(it, str):
            w('      <p style="%(BODY)s">%(t)s</p>', t=it)
            return
        kind = it[0]
        if kind == 'h3':
            w('      <h3 style="%(H3)s">%(t)s</h3>', t=it[1])
        elif kind == 'why':
            w('''      <div style="background: %(KSOFT)s; border-inline-start: 4px solid %(KEY)s; border-radius: 0 14px 14px 0; padding: 18px 21px; margin: 22px 0; max-width: 68ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(KEY)s; margin-bottom: 10px;">%(WHYLAB)s</div>
        <p style="font-size: 15.5px; line-height: 2.1; color: %(MID)s; margin: 0;">%(t)s</p>
      </div>''', t=it[1])
        elif kind == 'note':
            w('''      <div style="%(SOFTC)s padding: 17px 20px; margin: 20px 0; max-width: 68ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(DIM)s; margin-bottom: 9px;">%(ti)s</div>
        <p style="font-size: 14.5px; line-height: 2.1; color: %(MID)s; margin: 0;">%(t)s</p>
      </div>''', ti=it[1], t=it[2])
        elif kind == 'quote':
            w('''      <blockquote style="margin: 22px 0; padding: 0 0 0 0; border-inline-start: 3px solid %(AC)s; padding-inline-start: 18px; max-width: 62ch;">
        <p style="font-size: 17px; line-height: 2.05; color: %(INK)s; font-weight: 500; margin: 0 0 9px;">%(t)s</p>
        <footer style="font-size: 13px; color: %(DIM)s;">%(who)s</footer>
      </blockquote>''', t=it[1], who=it[2])
        elif kind == 'rows':
            w('''      <div style="margin: 22px 0; max-width: 70ch;">
        <div style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.08em; color: %(AC)s; margin-bottom: 11px;">%(ti)s</div>
        <div style="display: flex; flex-direction: column; gap: 9px;">''', ti=it[1])
            for a, b in it[2]:
                w('''          <div style="%(CARD)s padding: 16px 19px;">
            <div style="font-size: 14.5px; font-weight: 700; color: %(INK)s; line-height: 1.75; margin-bottom: 7px;">%(a)s</div>
            <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0;">%(b)s</p>
          </div>''', a=a, b=b)
            w('        </div>\n      </div>')
        elif kind == 'steps':
            w('      <div style="display: flex; flex-direction: column; gap: 10px; margin: 22px 0; max-width: 70ch;">')
            for i, (a, b) in enumerate(it[1]):
                w('''        <div style="display: flex; gap: 14px; align-items: flex-start;">
          <span style="flex: 0 0 auto; width: 26px; height: 26px; border-radius: 50%%; background: %(SOFT)s; color: %(AC)s; font-size: 12.5px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-top: 4px;">%(n)s</span>
          <div style="flex: 1; min-width: 0;">
            <div style="font-size: 14.5px; font-weight: 700; color: %(INK)s; line-height: 1.8; margin-bottom: 5px;">%(a)s</div>
            <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0;">%(b)s</p>
          </div>
        </div>''', n=fa(i + 1), a=a, b=b)
            w('      </div>')
        elif kind == 'ltr':
            w('''      <p style="direction: ltr; text-align: center; unicode-bidi: isolate; font-size: 16px; font-weight: 600; color: %(AC)s; background: %(SOFT)s; border-radius: 12px; padding: 16px 18px; margin: 20px 0; max-width: 68ch; overflow-wrap: anywhere;">%(t)s</p>''',
              t=it[1])
        elif kind == 'code':
            w('''      <pre style="direction: ltr; text-align: left; unicode-bidi: isolate; background: %(CODE)s; color: #E8ECF2; border-radius: 13px; padding: 18px 20px; margin: 20px 0; max-width: 68ch; overflow-x: auto; font-size: 13px; line-height: 1.95;"><code>%(t)s</code></pre>''',
              t=it[1].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
        elif kind == 'puzzle':
            # یک نوارِ خانه‌دار: خانهٔ پر پررنگ، خانهٔ خالی کم‌رنگ
            w('      <div style="margin: 18px 0; max-width: 68ch;">\n'
              '        <div style="font-size: 11.5px; font-weight: 700; color: %(DIM)s; margin-bottom: 9px;">%(cap)s</div>\n'
              '        <div style="display: flex; flex-wrap: wrap; gap: 4px; direction: ltr; unicode-bidi: isolate;">',
              cap=it[2])
            for c in it[1]:
                full = c not in ('.', '·', '')
                w('          <span style="width: 27px; height: 31px; display: inline-flex;'
                  ' align-items: center; justify-content: center; font-size: 14px;'
                  ' font-weight: %(fw)s; border: 1px solid %(bd)s; border-radius: 5px;'
                  ' background: %(bg)s; color: %(fg)s;">%(c)s</span>',
                  c=(c if full else '·'),
                  fw=('800' if full else '400'),
                  bd=(V['AC'] if full else '#DCD7CA'),
                  bg=('#FFFFFF' if full else '#FAFAF7'),
                  fg=(V['AC'] if full else '#B9B3A5'))
            w('        </div>\n      </div>')
        elif kind == 'list':
            w('      <div style="display: flex; flex-direction: column; gap: 9px; margin: 20px 0; max-width: 68ch;">')
            for i, t in enumerate(it[1]):
                w('''        <div style="%(SOFTC)s padding: 15px 18px; display: flex; gap: 12px;">
          <span style="flex: 0 0 auto; font-size: 13px; font-weight: 800; color: %(AC)s;">%(n)s</span>
          <p style="font-size: 14.5px; line-height: 2.05; color: %(MID)s; margin: 0;">%(t)s</p>
        </div>''', n=fa('%02d' % (i + 1)), t=t)
            w('      </div>')
        else:
            raise ValueError('تکهٔ ناشناخته: %r' % (kind,))

    return o, w, block
