# -*- coding: utf-8 -*-
# بخش ۰۱ — «نبرد هوش»: تعریف خود بازی، پیش از ریاضیاتش
from data import ACCENT

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] for c in str(n))

CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'
SOFT = 'background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 14px;'
LTR = 'direction: ltr; text-align: left; unicode-bidi: isolate;'
EYE = 'font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: %s; margin: 0 0 12px;' % ACCENT
H2 = 'font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px; line-height: 1.45;'
H3 = 'font-size: 17.5px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;'
LEAD = 'font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 10px;'
MUTE = 'font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 22px;'
BODY = 'font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0 0 12px; max-width: 74ch;'

FILES = 'abcdefgh'

def knight_moves(f, r):
    n = 0
    for df, dr in ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)):
        if 0 <= f+df < 8 and 0 <= r+dr < 8:
            n += 1
    return n

PIECES = [
    ('♔', 'شاه', 'King', 1, 8, None, 'هرگز گرفته نمی‌شود. وقتی هر حرکت ممکنش به مرگ برسد، بازی تمام است.'),
    ('♕', 'وزیر', 'Queen', 1, 27, 9, 'قدرتمندترین مهره: رخ و فیل با هم. از مرکز صفحه ۲۷ خانه را کنترل می‌کند.'),
    ('♖', 'رخ', 'Rook', 2, 14, 5, 'تنها مهره‌ای که قدرتش به جایش بستگی ندارد — همیشه ۱۴ خانه. فقط ستون باز می‌خواهد.'),
    ('♗', 'فیل', 'Bishop', 2, 13, 3, 'تا ابد روی یک رنگ خانه می‌ماند. اگر سربازهایت مسیرش را ببندند، به «فیل بد» تبدیل می‌شود.'),
    ('♘', 'اسب', 'Knight', 2, 8, 3, 'تنها مهره‌ای که از روی بقیه می‌پرد. از مرکز ۸ خانه، از گوشه فقط ۲ خانه.'),
    ('♙', 'سرباز', 'Pawn', 8, 2, 1, 'جلو می‌رود و مورب می‌زند. اگر به آخر صفحه برسد، وزیر می‌شود.'),
]

MOB = [('وزیر', 'Queen', 27, '#8A1538'), ('رخ', 'Rook', 14, '#45494F'), ('فیل', 'Bishop', 13, '#2F5233'),
       ('اسب', 'Knight', 8, '#0E6FB4'), ('شاه', 'King', 8, '#7E22CE'), ('سرباز', 'Pawn', 2, '#B4530E')]

FORCE = [
    ('وزیر را رها می‌کنی', 'به نظر اشتباه می‌آید', '#B9B3A6'),
    ('حریف می‌زند', 'طمع، تنها حرکت طبیعی', '#666158'),
    ('کیش', 'مسیری که باز شد', '#8A1538'),
    ('پاسخ اجباری', 'شاه فقط یک خانه دارد', '#8A1538'),
    ('کیش', 'تونل یک‌طرفه', '#8A1538'),
    ('مات', 'وزیر طعمه نبود؛ کلید بود', '#16181C'),
]

Q3 = [
    ('۱', 'حریف الان چه تهدیدی دارد؟', 'نه «من چه بزنم؟». اول «او چه می‌خواهد؟». نود درصد اشتباه‌های بازیکن متوسط از نپرسیدن همین سؤال می‌آید.'),
    ('۲', 'اگر این حرکت را بکنم، او چه جواب‌هایی دارد؟', 'حرکت خوب آن نیست که قشنگ به نظر برسد؛ آن است که در برابر بهترین پاسخ حریف هم سر پا بماند.'),
    ('۳', 'بهترین حرکت اجباری من چیست؟', 'اگر بتوانی زنجیرهٔ «کیش، پاسخ اجباری، تهدید، پاسخ اجباری، مات» را ببینی، دیگر داری شطرنج واقعی بازی می‌کنی.'),
]

TERMS_FA = ['کیش', 'مات', 'قربانی', 'تمپو', 'قلعه', 'ارتقای سرباز', 'ساختار سرباز', 'ستون باز',
            'خانهٔ ضعیف', 'فیل بد', 'سرباز عقب‌افتاده', 'مهرهٔ بیش‌ازحد تحت فشار', 'توسعهٔ مهره‌ها', 'کنترل مرکز']
TERMS_EN = ['Check', 'Checkmate', 'Sacrifice', 'Tempo', 'Castling', 'Promotion', 'Pawn Structure', 'Open File',
            'Weak Square', 'Bad Bishop', 'Backward Pawn', 'Overloaded Piece', 'Development', 'Center Control']

READ = [
    ('این خانه ضعیف است', 'هیچ سربازی دیگر نمی‌تواند از آن دفاع کند — پس یک اسب می‌تواند تا ابد آن‌جا بنشیند.'),
    ('این فیل بد است', 'سربازهای خودت مسیرش را بسته‌اند. روی صفحه هست، ولی در بازی نیست.'),
    ('این شاه امنیت ندارد', 'سربازهای جلویش حرکت کرده‌اند. هنوز خطری نیست، ولی هر حمله‌ای از این به بعد جدی است.'),
    ('این ستون باز شده', 'هیچ سربازی در آن نمانده — یعنی یک بزرگراه برای رخ.'),
    ('این مهره بیش‌ازحد تحت فشار است', 'هم‌زمان از دو چیز دفاع می‌کند. یکی را بگیر، آن یکی می‌افتد.'),
    ('این سرباز عقب افتاده', 'از هم‌قطارهایش جا مانده و هیچ‌کس نمی‌تواند از او دفاع کند. یک ضعف دائمی.'),
]


def narrative():
    o = []
    w = o.append

    w('''
    <section id="s1" style="background: #FFFFFF; border-top: 1px solid #E4E1D6; border-bottom: 1px solid #E4E1D6; margin-top: 40px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 52px 24px;">
      <p style="%s">۰۱ — خودِ بازی</p>
      <h2 style="%s">نبرد هوش</h2>
      <p style="%s">قبل از هر عدد و هر نموداری، بگذار شطرنج را آن‌طور تعریف کنم که باید: نه «یک بازی با مهره‌های عجیب»، بلکه یک <b>نبرد هوش میان دو نفر</b>. دو پادشاه، دو ارتش، دو ذهن، روبه‌روی هم.</p>
      <p style="%s">و نکتهٔ ترسناکش این است: هیچ‌چیز در شطرنج تصادفی نیست. هر حرکتت یک پیام است.</p>

      <div style="background: #F3E3E7; border: 1px solid #E8CDD4; border-radius: 16px; padding: 30px 32px; margin-bottom: 20px;">
        <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 12px;">شطرنج در یک جمله</div>
        <p style="font-size: clamp(19px, 2.6vw, 25px); line-height: 1.75; font-weight: 800; color: #16181C; margin: 0 0 16px; max-width: 60ch;">شطرنج بازیِ ساختن تهدیدهایی است که حریف <i>مجبور</i> شود به آن‌ها پاسخ بدهد.</p>
        <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0; max-width: 68ch;">تو فقط مهره جابه‌جا نمی‌کنی. داری حریف را مجبور می‌کنی: «این کار را نکن»، «آن مهره را نجات بده»، «به این حمله جواب بده»، «اگر این را بگیری، آن یکی را از دست می‌دهی». و کم‌کم آزادی حرکتش را می‌گیری — تا جایی که شاه دیگر راه فراری ندارد.</p>
      </div>
''' % (EYE, H2, LEAD, MUTE, ACCENT))

    # ---------------- چرا شاه
    w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">
        <div style="%s padding: 26px 28px; border-top: 3px solid %s;">
          <h3 style="%s">چرا شاه این‌قدر مهم است؟</h3>
          <p style="%s">برخلاف خیلی از بازی‌ها، هدف گرفتن بیشترین مهره نیست. حتی هدف «کشتن شاه» هم نیست — <b>شاه هیچ‌وقت گرفته نمی‌شود</b>. وقتی در موقعیتی قرار بگیرد که هر حرکت ممکنش به مرگ برسد، بازی همان‌جا تمام است.</p>
          <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0; max-width: 74ch;">یعنی باید کاری کنی که حریف <i>مجبور شود تسلیم شود</i>. و این فوق‌العاده است: تمام آن ارتش برای محافظت از یک موجود نسبتاً ضعیف ساخته شده.</p>
        </div>
        <div style="%s padding: 26px 28px; border-top: 3px solid #45494F;">
          <h3 style="%s">و این یک تصمیم طراحی است</h3>
          <p style="%s">شطرنج می‌توانست بازیِ «بیشترین مهره را بگیر» باشد. نیست. هدفش یک <b>شرط وضعیتی</b> است، نه یک شمارش.</p>
          <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0; max-width: 74ch;">همین یک انتخاب، بازی را از یک مسابقهٔ انباشت به یک مسئلهٔ <b>ساختار</b> تبدیل کرد — و دلیل اینکه هفتاد سال بعد، تعریف تابع هدف در یادگیری ماشین هنوز سخت‌ترین بخش کار است، دقیقاً همین است.</p>
        </div>
      </div>
''' % (CARD, ACCENT, H3, BODY, CARD, H3, BODY))

    # ---------------- ارتش
    w('''      <h3 style="font-size: 20px; font-weight: 800; margin: 30px 0 10px;">ارتش تو</h3>
      <p style="%s">هر طرف شانزده مهره دارد. ولی نکتهٔ مهم این است: <b>قدرت مهره‌ها ثابت نیست</b>. یک اسب ممکن است وسط بازی هیولا باشد و آخر بازی تقریباً بی‌فایده.</p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(255px, 1fr)); gap: 12px; margin-bottom: 14px;">''' % LEAD)
    for g, f, e, cnt, mob, val in [(p[0], p[1], p[2], p[3], p[4], p[5]) for p in PIECES]:
        note = [p[6] for p in PIECES if p[1] == f][0]
        w('''        <div style="%s padding: 20px 22px;">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <span style="font-size: 30px; line-height: 1; color: %s; font-family: 'Segoe UI Symbol','Noto Sans Symbols 2','DejaVu Sans',serif;">%s</span>
            <div>
              <div style="font-size: 15.5px; font-weight: 800; color: #16181C;">%s <span style="font-size: 12px; font-weight: 500; color: #666158;">× %s</span></div>
              <div style="font-size: 11px; color: #666158; %s">%s</div>
            </div>
          </div>
          <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
            <span style="font-size: 11px; color: #45494F; background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 999px; padding: 4px 10px;">سقف کنترل: %s خانه</span>
            <span style="font-size: 11px; color: #45494F; background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 999px; padding: 4px 10px;">%s</span>
          </div>
          <p style="font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (SOFT, ACCENT, g, f, fa(cnt), LTR, e, fa(mob),
                     ('ارزش تقریبی: %s' % fa(val)) if val else 'ارزش: بی‌نهایت', note))
    w('''      </div>''')

    # نمودار تحرک
    w('''      <div style="%s padding: 24px 26px; margin-bottom: 14px;">
        <h3 style="font-size: 16px; font-weight: 800; margin: 0 0 6px;">بیشترین خانه‌ای که هر مهره می‌تواند کنترل کند</h3>
        <p style="font-size: 12.8px; line-height: 1.9; color: #666158; margin: 0 0 20px;">روی صفحهٔ خالی و از بهترین خانهٔ ممکن. این عددها «قدرت» نیستند، ولی توضیح می‌دهند چرا شطرنج‌بازها این‌قدر دربارهٔ مرکز صفحه حرف می‌زنند.</p>''' % CARD)
    for f, e, v, c in MOB:
        w('''        <div style="margin-bottom: 14px;">
          <div style="display: flex; align-items: baseline; gap: 9px; margin-bottom: 6px;">
            <span style="font-size: 13.5px; font-weight: 700; color: #16181C;">%s</span>
            <span style="font-size: 11px; color: #666158; %s">%s</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="flex: 1; height: 13px; background: #F0EEE7; border-radius: 7px; overflow: hidden;">
              <div style="width: %.1f%%; height: 100%%; background: %s; border-radius: 7px;"></div>
            </div>
            <span style="font-size: 12.5px; font-weight: 700; color: %s; width: 58px; flex-shrink: 0; text-align: left;">%s خانه</span>
          </div>
        </div>''' % (f, LTR, e, v / 27.0 * 100, c, c, fa(v)))
    w('''        <p style="font-size: 11.5px; color: #666158; margin: 6px 0 0; padding-top: 14px; border-top: 1px solid #F0EEE7;">رخ تنها مهره‌ای است که این عدد برایش همه‌جا یکسان است. بقیه به جایشان وابسته‌اند — و این یعنی در شطرنج، <b>موقعیت</b> بخشی از قدرت است.</p>
      </div>''')

    # ---------------- صفحه یک نقشه است: گرمانقشهٔ اسب
    w('''      <h3 style="font-size: 20px; font-weight: 800; margin: 30px 0 10px;">صفحه، در واقع یک نقشه است</h3>
      <p style="%s">شصت‌وچهار خانه داری، ولی همهٔ خانه‌ها ارزش یکسان ندارند. این نقشه دقیقاً نشان می‌دهد چرا: هر عدد، تعداد خانه‌هایی است که <b>یک اسب از آن خانه</b> کنترل می‌کند.</p>
      <p style="%s">اسب وسط صفحه هشت خانه را می‌بیند. همان اسب در گوشه، فقط دو تا. دارد به دیوار نگاه می‌کند.</p>
      <div style="%s padding: 24px 26px; margin-bottom: 14px;">
        <div style="max-width: 520px; margin: 0 auto;">
          <div style="display: grid; grid-template-columns: repeat(8, 1fr); gap: 3px; direction: ltr; aspect-ratio: 1;">''' % (LEAD, MUTE, CARD))
    for r in range(7, -1, -1):
        for f in range(8):
            v = knight_moves(f, r)
            a = 0.10 + (v - 2) / 6.0 * 0.82
            name = FILES[f] + str(r + 1)
            corner = (f in (0, 7) and r in (0, 7))
            center = (f in (3, 4) and r in (3, 4))
            txtc = '#FFFFFF' if v >= 6 else '#16181C'
            ring = 'box-shadow: inset 0 0 0 2px #16181C;' if (corner or center) else ''
            w('''<div style="background: rgba(138,21,56,%.2f); border-radius: 5px; display: flex; flex-direction: column; align-items: center; justify-content: center; %s"><span style="font-size: clamp(11px, 2.1vw, 15px); font-weight: 800; color: %s; line-height: 1.1;">%s</span>''' % (a, ring, txtc, fa(v)))
            if corner or center:
                w('''<span style="font-size: clamp(7px, 1.2vw, 9px); color: %s; opacity: 0.75; line-height: 1.1;">%s</span>''' % (txtc, name))
            w('''</div>''')
    w('''          </div>
        </div>
        <div style="display: flex; gap: 10px 20px; flex-wrap: wrap; align-items: center; justify-content: center; margin-top: 18px; padding-top: 16px; border-top: 1px solid #F0EEE7;">
          <span style="font-size: 12px; color: #45494F;">کم‌رنگ‌تر = خانه‌های کمتر</span>
          <span style="display: inline-flex; gap: 3px; align-items: center;">''')
    for v in (2, 3, 4, 6, 8):
        a = 0.10 + (v - 2) / 6.0 * 0.82
        w('''<span style="width: 26px; height: 13px; border-radius: 4px; background: rgba(138,21,56,%.2f);"></span>''' % a)
    w('''          </span>
          <span style="font-size: 12px; color: #45494F;">پررنگ‌تر = خانه‌های بیشتر</span>
          <span style="font-size: 11.5px; color: #666158;">چهار گوشه و چهار خانهٔ مرکزی علامت خورده‌اند</span>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 20px;">
        <div style="%s padding: 22px 24px; text-align: center;">
          <div style="font-size: 34px; font-weight: 800; color: %s; line-height: 1;">۸</div>
          <div style="font-size: 13px; color: #45494F; margin-top: 8px;">خانه، برای اسبی در مرکز</div>
          <div style="font-size: 11px; color: #666158; margin-top: 4px; %s">d4, d5, e4, e5</div>
        </div>
        <div style="%s padding: 22px 24px; text-align: center;">
          <div style="font-size: 34px; font-weight: 800; color: #B9B3A6; line-height: 1;">۲</div>
          <div style="font-size: 13px; color: #45494F; margin-top: 8px;">خانه، برای همان اسب در گوشه</div>
          <div style="font-size: 11px; color: #666158; margin-top: 4px; %s">a1, a8, h1, h8</div>
        </div>
        <div style="%s padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 9px;">پس ترتیب کار این است</h3>
          <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;">''' % (SOFT, ACCENT, LTR, SOFT, LTR, CARD))
    for i, st in enumerate(['مرکز', 'توسعه', 'امنیت شاه', 'حمله']):
        if i:
            w('''<span style="font-size: 13px; color: #B9B3A6;">←</span>''')
        w('''<span style="font-size: 12.5px; color: #16181C; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 999px; padding: 6px 11px;">%s</span>''' % st)
    w('''          </div>
          <p style="font-size: 12.5px; line-height: 1.9; color: #666158; margin: 12px 0 0;">نه اینکه از حرکت اول دنبال مات باشی.</p>
        </div>
      </div>''')

    # ---------------- معمای چندلایه + الگو
    w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">
        <div style="%s padding: 26px 28px; border-top: 3px solid #45494F;">
          <h3 style="%s">معمای چندلایه</h3>
          <p style="%s">فرض کن حریفت اسبی دارد که می‌تواند مهرهٔ تو را بزند. تو می‌توانی اسب را بزنی. اما اگر بزنی، وزیر حریف تو را می‌زند. اگر وزیر را بزنی، رخش وارد می‌شود. اگر رخ را بزنی، شاه…</p>
          <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0; max-width: 74ch;">تو حرکت اول را نمی‌بینی. باید ببینی: بعد از حرکت من او چه می‌کند؟ بعد من چه می‌کنم؟ بعد او چه می‌کند؟ — و همین‌طور ادامه بدهی. این دقیقاً همان درخت مینیماکسی است که در بخش ۰۶ دربارهٔ آن حرف می‌زنم.</p>
        </div>
        <div style="%s padding: 26px 28px; border-top: 3px solid #0E6FB4;">
          <h3 style="%s">ولی نابغهٔ شطرنج بیست حرکت جلوتر را حفظ نیست</h3>
          <p style="%s">این یک سوءتفاهم رایج است. بازیکن قوی بیش از آنکه آینده را پیش‌بینی کند، <b>الگو می‌شناسد</b>. می‌بیند شاه حریف پشت سه سرباز گیر کرده، وزیرش این‌جاست، رخش آن‌جا، یک قطر باز شده — و مغزش می‌گوید: این‌جا بوی مات می‌آید.</p>
          <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0 0 12px; max-width: 74ch;">همان چیزی که یک فوتبالیست حرفه‌ای را قبل از رسیدن توپ، سر جای درست می‌گذارد.</p>
          <a href="#c02" style="font-size: 13px; font-weight: 700; color: #0E6FB4;">این دقیقاً همان چیزی است که در ۱۹۷۳ اندازه‌اش گرفتند ←</a>
        </div>
      </div>''' % (CARD, H3, BODY, CARD, H3, BODY))

    # ---------------- قربانی
    w('''      <h3 style="font-size: 20px; font-weight: 800; margin: 30px 0 10px;">و این‌جاست که شطرنج واقعاً شیطانی می‌شود</h3>
      <p style="%s">گاهی بهترین حرکت تو آن نیست که مهره بزند؛ آن است که حریف را <b>وسوسه</b> کند. وزیرت را عمداً جلوی فیل حریف می‌گذاری. او فکر می‌کند مجانی است. می‌زند. و با باز شدن آن مسیر، رخ تو وارد می‌شود.</p>
      <div style="%s padding: 26px 28px; margin-bottom: 14px;">
        <div style="font-size: 11.5px; font-weight: 700; color: %s; margin-bottom: 16px;">زنجیرهٔ اجبار</div>
        <div style="display: flex; gap: 8px 10px; flex-wrap: wrap; align-items: stretch;">''' % (LEAD, CARD, ACCENT))
    for i, (t, sub, c) in enumerate(FORCE):
        if i:
            w('''          <span style="display: flex; align-items: center; font-size: 15px; color: #B9B3A6;">←</span>''')
        w('''          <div style="flex: 1 1 140px; min-width: 130px; background: #FAFAF7; border: 1px solid #E4E1D6; border-top: 3px solid %s; border-radius: 12px; padding: 14px 15px;">
            <div style="font-size: 13.5px; font-weight: 800; color: %s; margin-bottom: 6px;">%s</div>
            <div style="font-size: 11.5px; line-height: 1.75; color: #666158;">%s</div>
          </div>''' % (c, c, t, sub))
    w('''        </div>
        <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 20px 0 0; max-width: 74ch;">حریف تازه می‌فهمد وزیر اصلاً طعمه نبود؛ قربانی شده بود تا شاه را وارد یک تونل یک‌طرفه کند.</p>
      </div>

      <div style="background: #F3E3E7; border: 1px solid #E8CDD4; border-radius: 16px; padding: 26px 28px; margin-bottom: 20px;">
        <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-bottom: 12px;">
          <h3 style="font-size: 19px; font-weight: 800; margin: 0;">قربانی</h3>
          <span style="font-size: 12px; color: #666158; %s">Sacrifice</span>
        </div>
        <p style="font-size: 14.5px; line-height: 2.05; color: #45494F; margin: 0 0 14px; max-width: 74ch;">گاهی عمداً چیزی باارزش می‌دهی تا چیزی بسیار باارزش‌تر به دست بیاوری. وزیرت را می‌دهی و شاه حریف را می‌گیری. یک اسب می‌دهی و قلعهٔ دفاعی‌اش را خراب می‌کنی. یک سرباز می‌دهی و یک ستون برای رخت باز می‌کنی.</p>
        <p style="font-size: 16px; line-height: 1.95; font-weight: 700; color: #16181C; margin: 0; max-width: 64ch;">ارزش یک چیز فقط به خودش نیست؛ به کاری است که با فدا کردنش می‌توانی انجام بدهی.</p>
      </div>''' % LTR)

    # ---------------- تهدید، سرباز، قلعه، تمپو
    w('''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px; margin-bottom: 20px;">

        <div style="%s padding: 24px 26px; border-top: 3px solid %s;">
          <h3 style="%s">تهدید: کوچک‌کردن فضای تصمیم</h3>
          <p style="%s">فرض کن می‌توانی وزیر حریف را بزنی و نمی‌زنی. در عوض حرکتی می‌کنی که اگر او اشتباه کند، وزیرش را می‌گیری. حالا او باید انتخاب کند: وزیر را نجات بدهد؟ حمله کند؟ دفاع کند؟</p>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">داری <b>فضای تصمیم‌گیری</b> حریف را کوچک می‌کنی. این یکی از عمیق‌ترین جنبه‌های شطرنج است — و دقیقاً همان کاری که یک راهبرد خوب در بازار می‌کند.</p>
        </div>

        <div style="%s padding: 24px 26px; border-top: 3px solid #B4530E;">
          <h3 style="%s">سربازها، داستان خودشان را دارند</h3>
          <p style="%s">سرباز فقط به جلو می‌رود ولی مورب می‌زند. همین محدودیت، ساختار سربازها را به مهم‌ترین عنصر معماری صفحه تبدیل می‌کند.</p>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">یک سرباز می‌تواند مسیر یک فیل را ببندد، یک خانه را کنترل کند، شاه را پناه بدهد، جلوی اسب دشمن را بگیرد — یا به آخر صفحه برسد و <b>وزیر شود</b>.</p>
          <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px;">
            <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">ضعیف‌ترین مهرهٔ بازی می‌تواند در سکوت خودش را به انتهای میدان برساند و قدرتمندترین مهره شود. و اگر سربازها بد چیده شوند، همان‌ها کل ارتش خودت را خفه می‌کنند.</p>
          </div>
        </div>

        <div style="%s padding: 24px 26px; border-top: 3px solid #2F5233;">
          <div style="display: flex; align-items: baseline; gap: 9px; flex-wrap: wrap; margin-bottom: 12px;">
            <h3 style="font-size: 17.5px; font-weight: 800; margin: 0;">قلعه</h3>
            <span style="font-size: 11.5px; color: #666158; %s">Castling</span>
          </div>
          <p style="%s">یک حرکت عجیب: شاه و رخ تقریباً هم‌زمان جابه‌جا می‌شوند. چرا؟ چون اوایل بازی، مرکز صفحه برای شاه خطرناک است.</p>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">شاه را به گوشه می‌بری و رخ را فعال می‌کنی. با یک حرکت، هم <b>امنیت</b> و هم <b>توسعهٔ نیرو</b>.</p>
          <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px;">
            <p style="font-size: 13px; line-height: 1.95; color: #45494F; margin: 0;">و این یکی از اصول بزرگ شطرنج است: مهره‌ها را فقط جابه‌جا نکن؛ <b>موقعیتشان را بهتر کن</b>.</p>
          </div>
        </div>

        <div style="%s padding: 24px 26px; border-top: 3px solid #7E22CE;">
          <div style="display: flex; align-items: baseline; gap: 9px; flex-wrap: wrap; margin-bottom: 12px;">
            <h3 style="font-size: 17.5px; font-weight: 800; margin: 0;">تمپو: بازی دربارهٔ زمان است</h3>
            <span style="font-size: 11.5px; color: #666158; %s">Tempo</span>
          </div>
          <p style="%s">از یک جایی به بعد، بازی دیگر دربارهٔ مهره‌ها نیست. می‌توانی یک سرباز بگیری، ولی گرفتنش سه حرکت می‌خواهد — و در همان سه حرکت، حریف حمله می‌کند.</p>
          <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">پس آن سرباز «رایگان» نبود؛ بابتش <b>زمان</b> دادی. شطرنج حرفه‌ای پر است از همین معامله‌های نامرئی — و این همان چیزی است که در هر پروژه‌ای هم هست و تقریباً هیچ‌وقت در صورت‌حساب نمی‌آید.</p>
        </div>
      </div>''' % (CARD, ACCENT, H3, BODY, CARD, H3, BODY, CARD, LTR, BODY, CARD, LTR, BODY))

    # ---------------- سه سؤال طلایی
    w('''      <div style="background: #16181C; border-radius: 18px; padding: 32px 30px; margin-bottom: 20px;">
        <div style="font-size: 11.5px; letter-spacing: 0.1em; font-weight: 700; color: #E8CDD4; margin-bottom: 12px;">اگر فقط یک چیز از شطرنج یاد بگیری</div>
        <h3 style="font-size: clamp(20px, 2.6vw, 26px); font-weight: 800; color: #FFFFFF; margin: 0 0 10px;">سه سؤال طلایی</h3>
        <p style="font-size: 14.5px; line-height: 2; color: #C8C3B8; margin: 0 0 24px; max-width: 66ch;">بعد از هر حرکت، به همین ترتیب از خودت بپرس. ترتیبشان مهم‌تر از خودشان است.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">''')
    for n, q, d in Q3:
        w('''          <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 20px 22px;">
            <div style="font-size: 12px; font-weight: 800; color: #E8CDD4; margin-bottom: 10px;">%s</div>
            <h4 style="font-size: 15.5px; font-weight: 800; color: #FFFFFF; margin: 0 0 10px; line-height: 1.6;">%s</h4>
            <p style="font-size: 13px; line-height: 1.95; color: #C8C3B8; margin: 0;">%s</p>
          </div>''' % (n, q, d))
    w('''        </div>
      </div>''')

    # ---------------- صفحه با تو حرف می‌زند
    w('''      <h3 style="font-size: 20px; font-weight: 800; margin: 30px 0 10px;">و بعد از مدتی، صفحه با تو حرف می‌زند</h3>
      <p style="%s">وقتی یک صفحه را ببینی، دیگر فقط این را نمی‌بینی که اسب این‌جاست و رخ آن‌جا. چیز دیگری می‌بینی:</p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(265px, 1fr)); gap: 12px; margin-bottom: 20px;">''' % LEAD)
    for t, d in READ:
        w('''        <div style="%s padding: 18px 20px; border-inline-start: 3px solid %s;">
          <div style="font-size: 14px; font-weight: 800; color: #16181C; margin-bottom: 7px;">«%s»</div>
          <p style="font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 0;">%s</p>
        </div>''' % (SOFT, ACCENT, t, d))
    w('''      </div>''')

    # اصطلاح‌نامه
    w('''      <div style="%s padding: 24px 26px; margin-bottom: 20px;">
        <h3 style="font-size: 16px; font-weight: 800; margin: 0 0 6px;">واژه‌هایی که در این بخش آمد</h3>
        <p style="font-size: 12.8px; line-height: 1.9; color: #666158; margin: 0 0 16px;">فارسی برای فهمیدن، انگلیسی برای جست‌وجو کردن.</p>
        <div style="display: flex; gap: 7px; flex-wrap: wrap; margin-bottom: 14px;">''' % CARD)
    for t in TERMS_FA:
        w('''<span style="font-size: 12.5px; color: #16181C; background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 8px; padding: 6px 11px;">%s</span>''' % t)
    w('''        </div>
        <div style="background: #FAFAF7; border: 1px solid #E4E1D6; border-radius: 12px; padding: 14px 16px;">
          <p style="font-size: 12.5px; line-height: 2; color: #45494F; margin: 0; %s">%s</p>
        </div>
      </div>''' % (LTR, ' · '.join(TERMS_EN)))

    # بستن بخش
    w('''      <div style="background: #F3E3E7; border: 1px solid #E8CDD4; border-radius: 18px; padding: 32px 30px;">
        <p style="font-size: clamp(17px, 2.3vw, 22px); line-height: 1.85; font-weight: 800; color: #16181C; margin: 0 0 18px; max-width: 62ch;">دو نفر روبه‌روی هم نشسته‌اند. نه تاسی هست، نه شانسی، نه داوری که به‌جای تو تصمیم بگیرد. صفحه کاملاً جلوی هر دو باز است.</p>
        <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0 0 14px; max-width: 70ch;">و با این حال، بعد از چند ساعت یکی می‌گوید «مات»، و دیگری به صفحه نگاه می‌کند و می‌فهمد: من پنج حرکت پیش باخته بودم؛ فقط هنوز نمی‌دانستم.</p>
        <p style="font-size: 15px; line-height: 2.05; color: #45494F; margin: 0 0 14px; max-width: 70ch;">این شطرنج است. بازی‌ای دربارهٔ مهره‌ها نیست؛ دربارهٔ <b>دیدن چیزی است که هنوز اتفاق نیفتاده</b>. و شاید به همین دلیل است که بعد از قرن‌ها، هنوز وقتی دو نفر پشت یک صفحهٔ هشت در هشت می‌نشینند، یکی از عمیق‌ترین رقابت‌های انسانی شروع می‌شود.</p>
        <p style="font-size: 15px; line-height: 2.05; color: #16181C; margin: 0 0 20px; max-width: 70ch; font-weight: 700;">و حالا که می‌دانی بازی چیست، بقیهٔ این نوشته دربارهٔ چیزی است که وقتی ماشین‌ها سعی کردند همین را یاد بگیرند، دربارهٔ خودِ هوش فهمیدیم.</p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <a href="#s2" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; background: %s; padding: 12px 24px; border-radius: 10px;">حالا اندازهٔ مسئله ←</a>
          <a href="#s6" style="font-size: 13.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 12px 24px; border-radius: 10px;">یا مستقیم سراغ ارتباط‌ها ←</a>
        </div>
      </div>
      </div>
    </section>''' % ACCENT)

    return ''.join(o)
