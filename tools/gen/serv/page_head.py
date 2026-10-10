# -*- coding: utf-8 -*-
import io, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import logic as L

I = L.ITEMS
N = len(I)
fa = L.fa
AC = '#166534'
SOFTAC = '#E3EEE1'
CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'
SOFT = 'background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 14px;'
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
EYE = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %s; margin: 0 0 12px;' % AC
H2 = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
H3 = 'font-size: 15px; font-weight: 800; margin: 0 0 10px; line-height: 1.6;'
LEAD = 'font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 10px;'
MUTE = 'font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 22px;'
NOTE = 'font-size: 11.5px; line-height: 1.85; color: #666158; margin: 8px 0 0; padding-top: 14px; border-top: 1px solid #F0EEE7;'

q = lambda f: [x for x in I if f(x)]
NOCODE = len(q(lambda x: x['diff'] == 1))
LOWCODE = len(q(lambda x: x['diff'] <= 2))
RECUR = len(q(lambda x: x['model'] == 'اشتراک ماهانه'))
FAST = len(q(lambda x: x['spd'] == 3))
LIGHT = len(q(lambda x: x['cap'] == 1 and x['risk'] == 1))
BLUE = len(q(lambda x: x['sat'] <= 2))
DOMONLY = len(q(lambda x: x['market'] == 'داخلی'))
GLOBONLY = len(q(lambda x: x['market'] == 'جهانی'))
BOTH = len(q(lambda x: x['market'] == 'هر دو'))
