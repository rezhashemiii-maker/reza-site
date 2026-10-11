# -*- coding: utf-8 -*-
"""دو ابزار تعاملی «مبانی ریاضی».

۱) نردبان عدد: هر پله یک بحران و یک بهای پرداخت‌شده. جدولِ خاصیت‌ها پله‌پله
   از تیک به ضربدر می‌رود — همان چیزی که در مدرسه هیچ‌وقت نشان داده نمی‌شود.
۲) قطرِ کانتور: استدلال را رقم‌به‌رقم جلوی چشم می‌سازد.
"""
import io, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

# نام‌ها و نمادهای لاتین داخل جملهٔ فارسی: بدون جداسازی، نقطه و پرانتزِ کنارشان
# به سمت غلط می‌پرد. LRI/PDI همان کار unicode-bidi: isolate را در متن ساده می‌کند.
LRI, PDI = '\u2066', '\u2069'
_LAT = re.compile(r'[A-Za-z0-9][A-Za-z0-9×⁄²³·.+\-/]*(?:[ ][A-Za-z0-9][A-Za-z0-9×⁄²³·.+\-/]*)*')
_HASLAT = re.compile(r'[A-Za-z]')


def _wrap(m):
    run = m.group(0)
    if not _HASLAT.search(run):
        return run
    tail = ''
    while run and run[-1] in '.+-/·':
        tail = run[-1] + tail
        run = run[:-1]
    return LRI + run + PDI + tail


def iso(t):
    return _LAT.sub(_wrap, t)


# ------------------------------------------------------------------ نردبان
# خاصیت‌ها به ترتیبی که از دست می‌روند
PROPS = [
    'هر عدد، عددِ بعدی دارد',
    'همیشه می‌شود تفریق کرد',
    'همیشه می‌شود تقسیم کرد',
    'هر عدد نسبتِ دو عدد درست است',
    'ترتیبِ سازگار با حساب دارد',
    'ترتیبِ ضرب مهم نیست',
]

RUNGS = [
    dict(sym='ℕ', name='شمارشی', fa='۱، ۲، ۳، …',
         keep=[1, 0, 0, 1, 1, 1],
         broke='هیچ‌چیز هنوز نشکسته. این‌جا شروعِ کار است: انگشت‌ها. '
               'ولی همین‌جا یک در بسته است — «پنج منهای هشت» جواب ندارد.',
         when='از پیش از تاریخ',
         gain='شمردن. و همین کافی است برای اینکه بدانی گله‌ات کم شده یا نه.',
         loss='چیزی از دست نرفته، چون چیزی نبوده.',
         ex='اگر پنج گوسفند داری و هشت تا بدهکاری، در این دستگاه این جمله بی‌معناست.'),

    dict(sym='ℤ', name='درست', fa='…، −۲، −۱، ۰، ۱، ۲، …',
         keep=[1, 1, 0, 1, 1, 1],
         broke='تفریق از کار افتاده بود. برای اینکه «پنج منهای هشت» معنا پیدا کند، '
               'باید چیزی ساخته می‌شد که «کمتر از هیچ» باشد — و این برای قرن‌ها '
               'مزخرف به نظر می‌رسید.',
         when='براهماگوپتا، سال ۶۲۸ میلادی، قاعده‌های دارایی و بدهی را نوشت. '
              'اروپا چند قرن بعد هم هنوز با منفی کنار نیامده بود.',
         gain='تفریق همیشه جواب دارد. و عددها جهت پیدا کردند: جلو و عقب.',
         loss='«کوچک‌ترین عدد» از بین رفت. در شمارشی، یک آغاز بود. حالا هیچ کفی نیست.',
         ex='بدهی، دمای زیر صفر، طبقهٔ منفیِ پارکینگ. هیچ‌کدام بدون این پله گفتنی نیست.'),

    dict(sym='ℚ', name='گویا', fa='۱⁄۲، ۳⁄۴، −۷⁄۵، …',
         keep=[0, 1, 1, 1, 1, 1],
         broke='تقسیم از کار افتاده بود. «یک نان میان سه نفر» در عددهای درست جواب ندارد.',
         when='مصر و بابل، هزاران سال پیش. این پله از همه قدیمی‌تر است.',
         gain='تقسیم همیشه جواب دارد (جز بر صفر). و میانِ هر دو عدد، بی‌نهایت عدد دیگر هست.',
         loss='««عددِ بعدی» از بین رفت.» بعد از ۳ چه عددی می‌آید؟ هیچ. '
              'هر عددی که بگویی، میانش و ۳ باز هم عدد هست. این بزرگ‌ترین بهایی است '
              'که تا این‌جا داده‌ای و تقریباً هیچ‌کس در مدرسه به آن اشاره نمی‌کند.',
         ex='اگر بخواهی چیزها را پشت سر هم بشماری، دیگر نمی‌توانی. ترتیب هست، ولی «بعدی» نیست.'),

    dict(sym='ℝ', name='حقیقی', fa='⁦√۲⁩، π، e، …',
         keep=[0, 1, 1, 0, 1, 1],
         broke='قطرِ یک مربعِ یک‌درمتر. درازایش نه با کسر نوشتنی است نه با عدد درست. '
               'اثباتش هم ساده است و پایین‌تر خط‌به‌خط می‌آید.',
         when='یونان، حدود قرن پنجم پیش از میلاد. داستانِ مشهورِ غرق‌شدنِ کاشفش '
              'سندِ محکمی ندارد و منابع باستانی هم با هم نمی‌خوانند.',
         gain='خطِ عدد بی‌سوراخ شد. هر درازایی که بشود کشید، حالا عددی دارد. '
              'بدون این پله، حساب دیفرانسیل وجود نداشت.',
         loss='«بیشترِ عددها دیگر نوشتنی نیستند.» نه به صورت کسر، نه با هیچ '
              'دستورِ متناهی. و بدتر: شمردنی هم نیستند — که بحثِ بخش بعد است.',
         ex='اگر مربعی به ضلع یک متر بکشی، قطرش عددی است که هیچ کسری دقیقاً نشانش نمی‌دهد.'),

    dict(sym='ℂ', name='مختلط', fa='۳ + ۴i',
         keep=[0, 1, 1, 0, 0, 1],
         broke='x² = −۱ جواب نداشت. ریاضی‌دان‌های قرن شانزدهم در حل معادلهٔ درجه سه '
               'مجبور شدند وسطِ راه از ریشهٔ عددِ منفی رد شوند تا به جوابِ درستِ '
               'حقیقی برسند — پس آن چیزِ «ناممکن» وسط راه لازم بود.',
         when='دکارت در سال ۱۶۳۷ نامِ «موهومی» را رویشان گذاشت. چند منبع می‌گویند '
              'این نام تحقیرآمیز بوده؛ خودِ متنِ دکارت این را صریح نمی‌گوید. '
              'اویلر در قرن بعد جاافتاده‌شان کرد.',
         gain='«هر معادلهٔ چندجمله‌ای جواب دارد.» این دیگر در هیچ پلهٔ بعدی بهتر نمی‌شود — '
              'این‌جا تهِ راه است. موج، برق، کوانتوم، چرخش: همه این‌جا ساده می‌شوند.',
         loss='«ترتیب از بین رفت.» نمی‌شود گفت i از ۱ بزرگ‌تر است یا کوچک‌تر — '
              'یعنی هیچ ترتیبی وجود ندارد که با جمع و ضرب سازگار باشد. '
              'واژهٔ «بزرگ‌تر» این‌جا بی‌معنا می‌شود.',
         ex='هر چرخشی در صفحه، ضرب در یک عدد مختلط است. همین و بس.'),

    dict(sym='ℍ', name='کواترنیون', fa='a + bi + cj + dk',
         keep=[0, 1, 1, 0, 0, 0],
         broke='مختلط چرخش در «صفحه» را حل کرد. همیلتون ده سال دنبال چیزی بود که '
               'چرخش در «فضا» را همان‌قدر ساده کند.',
         when='شانزدهم اکتبر ۱۸۴۳، روی پلی در دوبلین. بنا بر روایت خودش، فرمول را '
              'همان‌جا روی سنگِ پل کند. آن کَنده‌کاری دیگر نیست و امروز لوحی جایش است.',
         gain='چرخش در فضای سه‌بعدی، بدون گیرکردن. امروز در گرافیک، ربات و ماهواره '
              'دقیقاً به همین دلیل به کار می‌رود.',
         loss='«a×b دیگر برابر b×a نیست.» ترتیبِ ضرب مهم شد — همان‌طور که '
              'ترتیبِ دو چرخشِ پشت سر هم مهم است. یک کتاب را دو بار بچرخان، '
              'جایشان را عوض کن، و ببین نتیجه فرق می‌کند.',
         ex='اگر گوشی‌ات را اول حول محور عمودی بچرخانی بعد افقی، به جای دیگری '
            'می‌رسی تا برعکسش. ریاضیاتش همین است.'),
]

# ------------------------------------------------------------------ قطر کانتور
# فهرستی فرضی از عددهای میان صفر و یک. قطرش عمداً رقم‌های متنوعی دارد.
DEC = [
    '3141592653', '2718281828', '1414213562', '7320508075',
    '6180339887', '5772156649', '3010299956', '2302585092',
]
# رقمِ قطری در هر سطر: DEC[i][i]
DIAG = [DEC[i][i] for i in range(len(DEC))]
NEWD = ['4' if d == '5' else '5' for d in DIAG]

for _r in RUNGS:
    for _k in ('broke', 'when', 'gain', 'loss', 'ex', 'fa'):
        _r[_k] = iso(_r[_k])

J = lambda x: json.dumps(x, ensure_ascii=False)

LOGIC = '''
var PROPS = %s;
var RUNGS = %s;
var DEC = %s;
var DIAG = %s;
var NEWD = %s;

function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}

var AC = '#4C3575', SOFT = '#EDE6F6', GREEN = '#2F5233', RUST = '#B4530E', DIM = '#666158';

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { rung: 0, dstep: 0 };
  }

  btn(label, on, onClick, color, soft) {
    return {
      label: label,
      style: 'font-size: 13.5px; font-weight: ' + (on ? '700' : '600') + '; padding: 9px 15px; '
        + 'border-radius: 10px; cursor: pointer; border: 1px solid ' + (on ? (color || AC) : '#E4E1D6')
        + '; background: ' + (on ? (soft || AC) : '#FFFFFF')
        + '; color: ' + (on ? (soft ? (color || AC) : '#FFFFFF') : '#45494F') + ';',
      onClick: onClick
    };
  }

  renderVals() {
    var self = this;
    var s = this.state;
    var r = RUNGS[s.rung];

    // ---- نردبان
    var rungBtns = RUNGS.map(function (x, i) {
      return self.btn(x.sym + '  ' + x.name, i === s.rung, function () { self.setState({ rung: i }); });
    });

    // «از دست رفت» یعنی پلهٔ قبل داشت و این پله ندارد — نه صرفاً اینکه ندارد.
    // در پلهٔ اول هیچ‌چیز از دست نرفته، چون هنوز چیزی نبوده.
    var props = PROPS.map(function (p, i) {
      var on = r.keep[i] === 1;
      var had = s.rung > 0 && RUNGS[s.rung - 1].keep[i] === 1;
      var justLost = !on && had;
      var justGained = on && s.rung > 0 && RUNGS[s.rung - 1].keep[i] === 0;
      // «هنوز نیست» فقط وقتی درست است که این خاصیت تا این‌جا هیچ‌وقت نبوده باشد؛
      // وگرنه قبلاً داشته‌ایم و پله‌های قبل گرفته‌اندش.
      var everHad = false;
      for (var k = 0; k < s.rung; k++) { if (RUNGS[k].keep[i] === 1) { everHad = true; break; } }
      var notYet = !on && !had && !everHad;
      var lostBefore = !on && !had && everHad;
      var badge = justLost ? 'همین‌جا از دست رفت'
        : (justGained ? 'همین‌جا به دست آمد'
        : (lostBefore ? 'پیش‌تر از دست رفت' : 'هنوز نیست'));
      return {
        name: p, on: on, off: !on, justLost: justLost, justGained: justGained,
        notYet: notYet, lostBefore: lostBefore, hasBadge: !on || justGained, badge: badge,
        badgeStyle: 'font-size: 11px; font-weight: 700; margin-inline-start: auto; flex-shrink: 0; color: '
          + (justLost ? RUST : (justGained ? GREEN : '#A9A398')) + ';',
        mark: on ? '✓' : '✗',
        style: 'display: flex; align-items: center; gap: 11px; padding: 11px 14px; border-radius: 10px; '
          + 'background: ' + (justLost ? '#F7E3D6' : (justGained ? '#E7F0E3' : (on ? '#F1F6EF' : '#FAFAF7'))) + '; '
          + 'border: 1px solid ' + (justLost ? '#E8C9AE' : (justGained ? '#C9DDC1' : '#E4E1D6')) + ';',
        markStyle: 'font-size: 15px; font-weight: 800; flex-shrink: 0; width: 1.4em; text-align: center; color: '
          + (on ? GREEN : (justLost ? RUST : '#BDB8AD')) + ';',
        textStyle: 'font-size: 13.5px; line-height: 1.7; color: ' + (on ? '#16181C' : DIM)
          + '; ' + (justLost || justGained ? 'font-weight: 700;' : '')
      };
    });

    var kept = r.keep.reduce(function (a, b) { return a + b; }, 0);

    // ---- قطر کانتور
    var n = DEC.length;
    var step = Math.min(s.dstep, n);
    var rows = DEC.map(function (d, i) {
      var digits = d.split('').map(function (c, j) {
        var isDiag = i === j;
        var done = isDiag && i < step;
        return {
          t: faNum(c),
          style: 'display: inline-block; width: 1.25em; text-align: center; padding: 2px 0; border-radius: 5px; '
            + (isDiag ? ('font-weight: 800; color: ' + (done ? '#FFFFFF' : AC) + '; background: '
                         + (done ? AC : SOFT) + ';') : 'color: #45494F;')
        };
      });
      return {
        label: 'عددِ ' + faNum(i + 1),
        digits: digits,
        dim: i >= step,
        style: 'display: flex; align-items: center; gap: 12px; flex-wrap: wrap; padding: 7px 0; opacity: '
          + (i < step ? '1' : '0.55') + ';'
      };
    });

    var built = NEWD.slice(0, step).map(function (c) { return faNum(c); }).join('');
    var pad = new Array(n - step + 1).join('؟');
    var done = step >= n;

    var dMsg;
    if (step === 0) {
      dMsg = 'فرض کن کسی ادعا کند همهٔ عددهای میان صفر و یک را در این فهرست نوشته است. '
           + 'هر عددی که دوست داری بگذار؛ فرقی نمی‌کند. حالا یک رقم جلو برو.';
    } else if (!done) {
      dMsg = 'رقمِ ' + faNum(step) + 'مِ عددِ تازه را طوری انتخاب کردیم که با رقمِ '
           + faNum(step) + 'مِ عددِ ' + faNum(step) + ' «فرق داشته باشد». '
           + 'پس عددِ تازه قطعاً عددِ ' + faNum(step) + ' نیست.';
    } else {
      dMsg = 'تمام شد. عددِ ساخته‌شده با «هر سطر» دست‌کم در یک رقم فرق دارد، '
           + 'پس در فهرست نیست. ولی فهرست قرار بود همه را داشته باشد. '
           + 'یعنی آن ادعا غلط بود — و برای «هر» فهرستی غلط است.';
    }

    return {
      rungBtns: rungBtns,
      sym: r.sym, rname: r.name, rfa: r.fa,
      broke: r.broke, when: r.when, gain: r.gain, loss: r.loss, ex: r.ex,
      props: props,
      keptFa: faNum(kept), totalFa: faNum(PROPS.length),
      first: s.rung === 0, notFirst: s.rung !== 0,

      rows: rows,
      built: built, pad: pad, hasBuilt: step > 0,
      dMsg: dMsg, dDone: done, dStepFa: faNum(step), dTotalFa: faNum(n),
      dBtns: [
        self.btn('یک رقم جلو', false, function () { self.setState({ dstep: Math.min(n, self.state.dstep + 1) }); }),
        self.btn('تا آخر', false, function () { self.setState({ dstep: n }); }),
        self.btn('از نو', false, function () { self.setState({ dstep: 0 }); })
      ]
    };
  }
}
''' % (J(PROPS), J(RUNGS), J(DEC), J(DIAG), J(NEWD))

if __name__ == '__main__':
    io.open(os.path.join(HERE, 'logic.js'), 'w', encoding='utf-8').write(LOGIC)
    print('logic', len(LOGIC), 'chars ·', len(RUNGS), 'rungs ·', len(PROPS), 'props · diag', ''.join(DIAG), '→', ''.join(NEWD))
