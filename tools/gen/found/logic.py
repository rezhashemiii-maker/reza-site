# -*- coding: utf-8 -*-
"""دو ابزار تعاملی «مبانی ریاضی».

۱) نردبان عدد: هر پله یک بحران و یک بهای پرداخت‌شده. جدولِ خاصیت‌ها پله‌پله
   از تیک به ضربدر می‌رود — همان چیزی که در مدرسه هیچ‌وقت نشان داده نمی‌شود.
۲) قطرِ کانتور: استدلال را رقم‌به‌رقم جلوی چشم می‌سازد.
"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import more as M  # noqa: E402
import books as BK  # noqa: E402

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
var PROPS = @@PROPS@@;
var RUNGS = @@RUNGS@@;
var DEC = @@DEC@@;
var DIAG = @@DIAG@@;
var NEWD = @@NEWD@@;
var RULES = @@RULES@@;
var FX = @@FX@@;
var GRP_SYS = @@GRP_SYS@@;
var GRP_PROPS = @@GRP_PROPS@@;
var GRP_UNIV = @@GRP_UNIV@@;
var BOOKS = @@BOOKS@@;
var BSTAGES = @@BSTAGES@@;

function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}

function fa1(x) {
  return faNum((Math.round(x * 10) / 10).toFixed(1)).replace('.', '٫');
}

var AC = '#4C3575', SOFT = '#EDE6F6', GREEN = '#2F5233', RUST = '#B4530E', DIM = '#666158';

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = {
      rung: 0, dstep: 0,
      rule: 0,
      fx: 0, fxPart: 0,
      mSeed: 20261011, mPlays: 0, mStay: 0, mSwitch: 0,
      grpCur: -1, grpSel: [],
      bkStage: -1, bkSpine: false, bkFree: false
    };
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


    // ---- ده قاعده‌ای که حفظ کردی
    var rules = RULES.map(function (x, i) {
      var open = i === s.rule;
      return {
        num: faNum(i + 1), r: x.r, tag: x.tag, school: x.school,
        why: x.why, breaks: x.breaks, open: open, sign: open ? '–' : '+',
        onClick: function () { self.setState({ rule: open ? -1 : i }); },
        rowStyle: 'border: 1px solid ' + (open ? '#D5CEDF' : '#E4E1D6')
          + '; background: ' + (open ? '#FFFFFF' : '#FAFAF7')
          + '; border-radius: 14px; overflow: hidden;',
        headStyle: 'display: flex; align-items: center; gap: 11px; width: 100%; text-align: start; '
          + 'cursor: pointer; border: 0; background: transparent; padding: 15px 18px; '
          + 'font-family: inherit; flex-wrap: wrap;',
        numStyle: 'font-size: 11.5px; font-weight: 800; color: ' + AC + '; flex-shrink: 0;',
        titleStyle: 'font-size: 15px; font-weight: 700; color: #16181C; line-height: 1.6;',
        tagStyle: 'direction: ltr; unicode-bidi: isolate; font-size: 13px; font-weight: 700; color: '
          + (open ? AC : '#8D8678') + ';',
        signStyle: 'margin-inline-start: auto; font-size: 18px; font-weight: 800; color: '
          + AC + '; flex-shrink: 0; line-height: 1;'
      };
    });

    // ---- فرمول‌خوانی
    var f = FX[s.fx];
    var fxTabs = FX.map(function (x, i) {
      return self.btn(x.name, i === s.fx, function () { self.setState({ fx: i, fxPart: 0 }); });
    });
    var fxParts = f.parts.map(function (pt, i) {
      var on = i === s.fxPart;
      return {
        t: pt.t, on: on,
        onClick: function () { self.setState({ fxPart: i }); },
        style: 'font-size: 17px; font-weight: ' + (on ? '800' : '600') + '; padding: 10px 13px; '
          + 'border-radius: 10px; cursor: pointer; font-family: inherit; white-space: nowrap; '
          + 'border: 1px solid ' + (on ? AC : '#E4E1D6')
          + '; background: ' + (on ? SOFT : '#FFFFFF')
          + '; color: ' + (on ? AC : '#45494F') + ';'
      };
    });
    var fxCur = f.parts[s.fxPart];
    var fxStep = 'تکهٔ ' + faNum(s.fxPart + 1) + ' از ' + faNum(f.parts.length);

    // ---- مونتی هال: دانهٔ تصادفی در state است و فقط با کلیک عوض می‌شود،
    // تا رندرِ سرور و مرورگر یکی بماند.
    function lehmer(x) { return (x * 48271) % 2147483647; }
    function runMonty(n) {
      var st = self.state;
      var seed = st.mSeed, stay = st.mStay, sw = st.mSwitch;
      for (var k = 0; k < n; k++) {
        seed = lehmer(seed); var car = seed % 3;
        seed = lehmer(seed); var pick = seed % 3;
        if (pick === car) { stay++; } else { sw++; }
      }
      self.setState({ mSeed: seed, mPlays: st.mPlays + n, mStay: stay, mSwitch: sw });
    }
    var mHas = s.mPlays > 0;
    var mStayP = mHas ? (s.mStay * 100 / s.mPlays) : 0;
    var mSwP = mHas ? (s.mSwitch * 100 / s.mPlays) : 0;
    var mBars = [
      { lab: 'ماندم', winFa: faNum(s.mStay), pctFa: fa1(mStayP), w: mStayP, c: '#8D8678', bg: '#EFEDE6' },
      { lab: 'عوض کردم', winFa: faNum(s.mSwitch), pctFa: fa1(mSwP), w: mSwP, c: AC, bg: SOFT }
    ].map(function (b) {
      return {
        lab: b.lab, winFa: b.winFa, pctFa: b.pctFa,
        labStyle: 'font-size: 13.5px; font-weight: 700; color: ' + b.c + '; min-width: 6em;',
        barStyle: 'flex: 1; min-width: 90px; height: 11px; border-radius: 999px; background: ' + b.bg + ';',
        fillStyle: 'width: ' + b.w + '%; height: 100%; border-radius: 999px; background: ' + b.c + ';',
        pctStyle: 'font-size: 13.5px; font-weight: 800; color: ' + b.c + '; min-width: 4.5em; text-align: start;'
      };
    });
    var mBtns = [
      self.btn('۱۰ بازی', false, function () { runMonty(10); }),
      self.btn('۱۰۰ بازی', false, function () { runMonty(100); }),
      self.btn('۱۰۰۰ بازی', false, function () { runMonty(1000); }),
      self.btn('از نو', false, function () { self.setState({ mPlays: 0, mStay: 0, mSwitch: 0 }); })
    ];

    // ---- خودت انتزاع کن
    var grpFound = 0;
    for (var gi = 0; gi < GRP_UNIV.length; gi++) {
      if (s.grpSel.indexOf(GRP_UNIV[gi]) >= 0) { grpFound++; }
    }
    var grpProps = GRP_PROPS.map(function (x, i) {
      var open = i === s.grpCur;
      var seen = s.grpSel.indexOf(i) >= 0;
      var univ = GRP_UNIV.indexOf(i) >= 0;
      return {
        q: x.q, nick: x.nick, why: x.why, open: open, seen: seen, univ: univ, notUniv: !univ,
        verdict: univ ? 'هر چهار دستگاه این را دارند' : 'مشترک نیست — کنار می‌رود',
        marks: GRP_SYS.map(function (sy, j) {
          var ok = x.have[j] === 1;
          return {
            sym: sy.sym, mark: ok ? '✓' : '✗',
            style: 'display: inline-flex; align-items: center; gap: 6px; padding: 6px 11px; '
              + 'border-radius: 999px; font-size: 12.5px; font-weight: 700; '
              + 'background: ' + (ok ? '#E7F0E3' : '#F7E3D6') + '; '
              + 'color: ' + (ok ? GREEN : RUST) + ';'
          };
        }),
        onClick: function () {
          var sel = self.state.grpSel.slice();
          if (sel.indexOf(i) < 0) { sel.push(i); }
          self.setState({ grpCur: open ? -1 : i, grpSel: sel });
        },
        rowStyle: 'border: 1px solid ' + (open ? '#D5CEDF' : (seen ? '#E4E1D6' : '#E4E1D6'))
          + '; background: ' + (open ? '#FFFFFF' : (seen ? '#FDFDFB' : '#FAFAF7'))
          + '; border-radius: 14px; overflow: hidden;',
        headStyle: 'display: flex; align-items: center; gap: 11px; width: 100%; text-align: start; '
          + 'cursor: pointer; border: 0; background: transparent; padding: 15px 18px; '
          + 'font-family: inherit; flex-wrap: wrap;',
        qStyle: 'font-size: 14.5px; font-weight: 700; line-height: 1.7; color: '
          + (seen ? '#16181C' : '#45494F') + ';',
        tickStyle: 'margin-inline-start: auto; font-size: 12px; font-weight: 800; flex-shrink: 0; color: '
          + (univ ? GREEN : RUST) + ';',
        verdictStyle: 'font-size: 12.5px; font-weight: 800; color: ' + (univ ? GREEN : RUST) + ';'
      };
    });
    var grpRevealed = grpFound >= GRP_UNIV.length;
    var grpLeft = GRP_UNIV.length - grpFound;

    // ---- فهرست کتاب‌ها
    var bkSpineN = 0, bkFreeN = 0;
    BOOKS.forEach(function (b) { if (b.spine) { bkSpineN++; } if (b.free) { bkFreeN++; } });
    var bkPass = BOOKS.filter(function (b) {
      if (s.bkStage >= 0 && b.st !== s.bkStage) { return false; }
      if (s.bkSpine && !b.spine) { return false; }
      if (s.bkFree && !b.free) { return false; }
      return true;
    });
    var bkGroups = [];
    BSTAGES.forEach(function (st) {
      var list = bkPass.filter(function (b) { return b.st === st.i; });
      if (!list.length) { return; }
      bkGroups.push({
        stFa: faNum(st.i), name: st.n, desc: st.d, countFa: faNum(list.length),
        books: list.map(function (b) {
          return {
            fa: b.fa, en: b.en, who: b.who, yrLat: String(b.yr), why: b.why,
            note: b.note, hasNote: !!b.note, free: b.free, hasFree: !!b.free,
            spine: !!b.spine, idFa: faNum(b.id),
            style: 'background: #FFFFFF; border: 1px solid ' + (b.spine ? '#D5CEDF' : '#E4E1D6')
              + '; border-radius: 15px; padding: 20px 22px;'
              + (b.spine ? ' box-shadow: inset 3px 0 0 ' + AC + ';' : '')
          };
        })
      });
    });
    var bkBtns = [self.btn('همه', s.bkStage < 0, function () { self.setState({ bkStage: -1 }); })].concat(
      BSTAGES.map(function (st) {
        return self.btn(faNum(st.i) + '  ' + st.n, s.bkStage === st.i,
          function () { self.setState({ bkStage: st.i }); });
      }));
    var bkToggles = [
      self.btn('فقط ستونِ فقرات (' + faNum(bkSpineN) + ')', s.bkSpine,
        function () { self.setState({ bkSpine: !self.state.bkSpine }); }, AC, SOFT),
      self.btn('فقط رایگان (' + faNum(bkFreeN) + ')', s.bkFree,
        function () { self.setState({ bkFree: !self.state.bkFree }); }, GREEN, '#E7F0E3')
    ];

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
      ],

      rules: rules,

      fxTabs: fxTabs, fxParts: fxParts, fxStep: fxStep,
      fxName: f.name, fxTag: f.tag, fxRead: f.read, fxGist: f.gist,
      fxLab: fxCur.lab, fxSay: fxCur.say, fxWhy: fxCur.why,

      mBars: mBars, mBtns: mBtns, mHas: mHas, mNone: !mHas,
      mPlaysFa: faNum(s.mPlays),

      grpProps: grpProps, grpRevealed: grpRevealed, grpNotYet: !grpRevealed,
      grpFoundFa: faNum(grpFound), grpTotalFa: faNum(GRP_UNIV.length),
      grpLeftFa: faNum(grpLeft),

      bkBtns: bkBtns, bkToggles: bkToggles, bkGroups: bkGroups,
      bkCountFa: faNum(bkPass.length), bkTotalFa: faNum(BOOKS.length),
      bkNone: bkPass.length === 0, bkSome: bkPass.length > 0
    };
  }
}
'''

_DATA = [
    ('PROPS', PROPS), ('RUNGS', RUNGS), ('DEC', DEC), ('DIAG', DIAG), ('NEWD', NEWD),
    ('RULES', M.RULES), ('FX', M.FX), ('GRP_SYS', M.GRP_SYS),
    ('GRP_PROPS', M.GRP_PROPS), ('GRP_UNIV', M.GRP_UNIV),
    ('BOOKS', BK.B), ('BSTAGES', [dict(i=i, n=n, d=d) for i, n, d in BK.STAGES]),
]
for _k, _v in _DATA:
    LOGIC = LOGIC.replace('@@' + _k + '@@', J(_v))
assert '@@' not in LOGIC

if __name__ == '__main__':
    io.open(os.path.join(HERE, 'logic.js'), 'w', encoding='utf-8').write(LOGIC)
    print('logic', len(LOGIC), 'chars ·', len(RUNGS), 'rungs ·', len(PROPS), 'props · diag', ''.join(DIAG), '→', ''.join(NEWD))
