# -*- coding: utf-8 -*-
import json, io, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data as D

CATS = D.CATS
CATNAME = {c[0]: c[1] for c in CATS}
CATCOL = {c[0]: (c[2], c[3]) for c in CATS}

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))

DIFF_L = {1: 'بدون کد', 2: 'کم‌کد', 3: 'نیمه‌فنی', 4: 'فنی', 5: 'مهندسی'}
DEM_L  = {1: 'بسیار کم', 2: 'کم', 3: 'متوسط', 4: 'بالا', 5: 'بسیار بالا'}
SAT_L  = {1: 'تقریباً خالی', 2: 'کم‌رقابت', 3: 'متوسط', 4: 'پررقابت', 5: 'اشباع'}
SPD_L  = {1: 'ماه‌ها', 2: 'هفته‌ها', 3: 'روزها'}
CAP_L  = {1: 'تقریباً صفر', 2: 'کم', 3: 'متوسط'}
RISK_L = {1: 'کم', 2: 'متوسط', 3: 'بالا'}

SMAX = 23  # ۵×۲ + ۵ + ۳ + ۵

def score(s):
    return s['dem'] * 2 + (6 - s['diff']) + s['spd'] + (6 - s['sat'])

def pct(s):
    return int(round(score(s) * 100.0 / SMAX))

GOOD = '#166534'
MID  = '#8A8578'
BAD  = '#B4530E'

def _m(name, v, mx, lab, lower_better):
    """نوار هر سنجه: هرچه بلندتر، برای سازندهٔ سرویس بهتر"""
    g = (mx - v) / float(mx - 1) if lower_better else (v - 1) / float(mx - 1)
    col = GOOD if g >= 0.66 else (MID if g >= 0.34 else BAD)
    return dict(name=name, lab=lab, vFa=fa(v),
                w='%d%%' % int(round(12 + g * 88)),
                bar='width: %d%%; height: 100%%; border-radius: 6px; background: %s;'
                    % (int(round(12 + g * 88)), col),
                col=col)

def meters(s):
    """شش سنجه، به ترتیب ثابت"""
    return [
        _m('سختی فنی',      s['diff'], 5, DIFF_L[s['diff']], True),
        _m('تقاضا',          s['dem'],  5, DEM_L[s['dem']],   False),
        _m('رقابت',          s['sat'],  5, SAT_L[s['sat']],   True),
        _m('تا اولین درآمد', s['spd'],  3, SPD_L[s['spd']],   False),
        _m('سرمایهٔ اولیه',  s['cap'],  3, CAP_L[s['cap']],   True),
        _m('ریسک',           s['risk'], 3, RISK_L[s['risk']], True),
    ]

ITEMS = []
for i, s in enumerate(D.S):
    col, soft = CATCOL[s['cat']]
    hay = ' '.join([s['fa'], CATNAME[s['cat']], s['give'], s['who'], s['need'],
                    s['price'], s['edge'], s['model'], s['market']]).lower()
    ITEMS.append(dict(
        id='sv%02d' % (i + 1), fa=s['fa'], cat=s['cat'], catName=CATNAME[s['cat']],
        color=col, soft=soft,
        diff=s['diff'], dem=s['dem'], sat=s['sat'], spd=s['spd'], cap=s['cap'], risk=s['risk'],
        market=s['market'], model=s['model'],
        give=s['give'], who=s['who'], need=s['need'], price=s['price'], edge=s['edge'],
        sc=score(s), pct=pct(s), pctFa=fa(pct(s)),
        diffLab=DIFF_L[s['diff']], demLab=DEM_L[s['dem']], satLab=SAT_L[s['sat']],
        spdLab=SPD_L[s['spd']], capLab=CAP_L[s['cap']], riskLab=RISK_L[s['risk']],
        meters=meters(s), hay=hay,
        dom=(s['market'] != 'جهانی'), glob=(s['market'] != 'داخلی'),
    ))

N = len(ITEMS)
CNT_CAT = collections.Counter(it['cat'] for it in ITEMS)
CNT_MODEL = collections.Counter(it['model'] for it in ITEMS)

cats_js = [dict(key=k, name=n, color=c, soft=s, count=CNT_CAT[k]) for (k, n, c, s) in CATS]
models_js = [dict(name=m, count=CNT_MODEL.get(m, 0)) for m in D.MODELS]

J = lambda x: json.dumps(x, ensure_ascii=False)

LOGIC = '''
var ITEMS = %s;
var CATS = %s;
var MODELS = %s;

function faSep(x) {
  return faNum(Math.round(x).toLocaleString('en-US')).replace(/,/g, '\u066C');
}

function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}

var PRESETS = [
  { key: 'start', name: 'برای شروع همین هفته', hint: 'بدون کد یا کم‌کد، اولین درآمد در چند روز',
    test: function (it) { return it.diff <= 2 && it.spd === 3; } },
  { key: 'recur', name: 'درآمد تکرارشونده', hint: 'قرارداد ماهانه، نه کار یک‌بارهٔ پروژه‌ای',
    test: function (it) { return it.model === 'اشتراک ماهانه'; } },
  { key: 'blue', name: 'کم‌رقابت و پرتقاضا', hint: 'تقاضای بالا و رقابت کم — سخت‌تر ولی خالی‌تر',
    test: function (it) { return it.sat <= 2 && it.dem >= 4; } },
  { key: 'light', name: 'بدون سرمایه و کم‌ریسک', hint: 'سرمایهٔ اولیهٔ تقریباً صفر و ریسک کم',
    test: function (it) { return it.cap === 1 && it.risk === 1; } }
];

var QCODE = [
  { key: 'none', name: 'اصلاً', hint: 'هیچ کدی نمی‌نویسم', max: 1 },
  { key: 'some', name: 'کمی', hint: 'می‌توانم چیزی را دستکاری کنم', max: 2 },
  { key: 'glue', name: 'ابزارها را وصل می‌کنم', hint: 'با ابزارهای بدون کد راحتم', max: 3 },
  { key: 'dev',  name: 'برنامه‌نویسم', hint: 'محدودیت فنی ندارم', max: 5 }
];
var QTIME = [
  { key: 'low',  name: 'زیر ۱۰ ساعت در هفته', hint: 'کنار کار اصلی' },
  { key: 'mid',  name: '۱۰ تا ۲۵ ساعت', hint: 'نیمه‌وقت جدی' },
  { key: 'full', name: 'تمام‌وقت', hint: 'این کار اصلی من است' }
];
var QSPEED = [
  { key: 'now',   name: 'همین ماه', hint: 'باید زود پول بدهد' },
  { key: 'soon',  name: 'تا سه ماه', hint: 'می‌توانم صبر کنم' },
  { key: 'later', name: 'عجله ندارم', hint: 'دنبال چیز بادوام‌ترم' }
];
var QMODEL = [
  { key: 'recur', name: 'قرارداد ماهانه', hint: 'درآمد تکرارشونده' },
  { key: 'once',  name: 'پروژهٔ یک‌باره', hint: 'کار را تحویل بده و تمام' },
  { key: 'any',   name: 'فرقی نمی‌کند', hint: '' }
];
var QMARKET = [
  { key: 'dom',  name: 'داخل ایران', hint: '' },
  { key: 'glob', name: 'بیرون از ایران', hint: '' },
  { key: 'any',  name: 'هر دو', hint: '' }
];

var SORTS = [
  { key: 'score', name: 'امتیاز کلی' },
  { key: 'easy',  name: 'آسان‌ترین' },
  { key: 'dem',   name: 'پرتقاضاترین' },
  { key: 'blue',  name: 'کم‌رقابت‌ترین' },
  { key: 'fast',  name: 'سریع‌ترین درآمد' }
];

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = {
      q: '', cat: 'all', model: 'all', market: 'all', maxdiff: 0, satf: 'all', preset: 'none', sort: 'score',
      pCode: 'some', pTime: 'low', pSpeed: 'now', pModel: 'any', pMarket: 'any',
      cPrice: 400, cN: 6, cH: 8, cTarget: 3000, cUnit: 'usd'
    };
  }

  filtered() {
    var s = this.state;
    var q = s.q.trim().toLowerCase();
    var pre = null;
    PRESETS.forEach(function (p) { if (p.key === s.preset) { pre = p; } });

    var out = ITEMS.filter(function (it) {
      if (s.cat !== 'all' && it.cat !== s.cat) { return false; }
      if (s.model !== 'all' && it.model !== s.model) { return false; }
      if (s.market === 'dom' && !it.dom) { return false; }
      if (s.market === 'glob' && !it.glob) { return false; }
      if (s.maxdiff && it.diff > s.maxdiff) { return false; }
      if (s.satf === 'low' && it.sat > 2) { return false; }
      if (s.satf === 'high' && it.sat < 3) { return false; }
      if (pre && !pre.test(it)) { return false; }
      if (q && it.hay.indexOf(q) === -1) { return false; }
      return true;
    });

    out = out.slice();
    var k = s.sort;
    out.sort(function (a, b) {
      if (k === 'easy') { return (a.diff - b.diff) || (b.sc - a.sc); }
      if (k === 'dem')  { return (b.dem - a.dem) || (b.sc - a.sc); }
      if (k === 'blue') { return (a.sat - b.sat) || (b.dem - a.dem); }
      if (k === 'fast') { return (b.spd - a.spd) || (a.diff - b.diff); }
      return (b.sc - a.sc) || (a.diff - b.diff);
    });
    return out;
  }

  chip(label, count, on, onClick, color, soft) {
    return {
      label: label,
      count: count === null ? '' : faNum(count),
      hasCount: count !== null,
      style: 'display: inline-flex; align-items: center; gap: 7px; font-size: 13px; font-weight: '
        + (on ? '700' : '500') + '; padding: 8px 14px; border-radius: 999px; cursor: pointer; '
        + 'border: 1px solid ' + (on ? (color || '#166534') : '#E4E1D6') + '; '
        + 'background: ' + (on ? (soft || '#E3EEE1') : '#FFFFFF') + '; '
        + 'color: ' + (on ? (color || '#166534') : '#45494F') + ';',
      onClick: onClick
    };
  }

  picks() {
    var s = this.state;
    var code = QCODE.filter(function (x) { return x.key === s.pCode; })[0] || QCODE[1];
    var out = [];
    ITEMS.forEach(function (it) {
      if (it.diff > code.max) { return; }
      if (s.pMarket === 'dom' && !it.dom) { return; }
      if (s.pMarket === 'glob' && !it.glob) { return; }
      var bonus = 0;
      var why = [];
      if (s.pSpeed === 'now' && it.spd === 3) { bonus += 4; why.push('اولین درآمد در چند روز'); }
      else if (s.pSpeed === 'soon' && it.spd >= 2) { bonus += 2; why.push('درآمد در چند هفته'); }
      else if (s.pSpeed === 'later' && it.sat <= 2) { bonus += 3; why.push('رقابت کم، بادوام‌تر'); }
      if (s.pModel === 'recur' && it.model === 'اشتراک ماهانه') { bonus += 4; why.push('قرارداد ماهانه'); }
      if (s.pModel === 'once' && it.model === 'پروژه‌ای') { bonus += 4; why.push('کار پروژه‌ای'); }
      if (s.pTime === 'low' && it.diff <= 2 && it.cap === 1) { bonus += 3; why.push('سبک، برای وقت کم'); }
      if (s.pTime === 'mid' && it.diff <= 3) { bonus += 1; }
      if (s.pTime === 'full' && it.dem === 5) { bonus += 2; why.push('تقاضای بسیار بالا'); }
      if (it.diff === 1) { why.push('بدون کد'); }
      if (s.pMarket === 'dom' && it.market === 'داخلی') { bonus += 2; why.push('ساخته‌شده برای بازار داخلی'); }
      out.push({ it: it, v: it.sc + bonus, why: why.slice(0, 3) });
    });
    out.sort(function (a, b) { return (b.v - a.v) || (a.it.diff - b.it.diff); });
    return out.slice(0, 5).map(function (r, i) {
      var o = {};
      for (var k in r.it) { o[k] = r.it[k]; }
      o.rankFa = faNum(i + 1);
      o.why = r.why.join(' · ');
      o.hasWhy = r.why.length > 0;
      return o;
    });
  }

  num(x, d) {
    var v = Number(x);
    if (!isFinite(v) || v < 0) { return d; }
    return v;
  }

  money() {
    var s = this.state;
    var price = this.num(s.cPrice, 0);
    var n = Math.round(this.num(s.cN, 0));
    var h = this.num(s.cH, 0);
    var target = this.num(s.cTarget, 0);
    var unit = s.cUnit === 'usd' ? 'دلار' : 'میلیون تومان';

    var rev = price * n;
    var hours = n * h;
    var rate = hours > 0 ? rev / hours : 0;
    var cap = Math.min(100, hours / 160 * 100);
    var need = price > 0 ? Math.ceil(target / price) : 0;
    var needH = need * h;

    var verdict, vcol;
    if (hours > 160) {
      verdict = 'این از ظرفیت یک نفر بیشتر است. یا قیمت را بالا ببر، یا ساعت هر مشتری را کم کن، یا کسی را اضافه کن.';
      vcol = '#B4530E';
    } else if (hours > 120) {
      verdict = 'تقریباً تمام‌وقت. جا برای مشتری تازه یا کار فروش نمی‌ماند — و بدون کار فروش، ماه بعد خالی است.';
      vcol = '#B4530E';
    } else if (rev === 0) {
      verdict = 'عددها را وارد کن تا حساب شود.';
      vcol = '#8A8578';
    } else {
      verdict = 'در ظرفیت یک نفر جا می‌شود و برای پیدا کردن مشتری تازه هم وقت می‌ماند.';
      vcol = '#166534';
    }

    var reach, rcol;
    if (price <= 0 || target <= 0) { reach = ''; rcol = '#8A8578'; }
    else if (needH > 160) {
      reach = 'با این قیمت، رسیدن به هدف ' + faNum(need) + ' مشتری و ' + faSep(needH)
        + ' ساعت کار می‌خواهد — بیشتر از یک ماه کاری. قیمت کم است، نه تعداد مشتری.';
      rcol = '#B4530E';
    } else {
      reach = 'برای رسیدن به هدف، ' + faNum(need) + ' مشتری لازم داری و ' + faSep(needH)
        + ' ساعت کار در ماه.';
      rcol = '#166534';
    }

    return {
      unit: unit,
      revFa: faSep(rev),
      hoursFa: faSep(hours),
      rateFa: faSep(rate),
      capFa: faNum(Math.round(cap)),
      capBar: 'width: ' + Math.max(2, Math.round(cap)) + '%%; height: 100%%; border-radius: 7px; background: '
        + (hours > 160 ? '#B4530E' : (hours > 120 ? '#8A8578' : '#166534')) + ';',
      verdict: verdict,
      verdictStyle: 'font-size: 13.5px; line-height: 1.95; font-weight: 600; margin: 0; color: ' + vcol + ';',
      reach: reach, hasReach: reach !== '',
      reachStyle: 'font-size: 13px; line-height: 1.95; margin: 10px 0 0; color: ' + rcol + ';'
    };
  }

  renderVals() {
    var self = this;
    var s = this.state;
    var rows = this.filtered();

    var catChips = [this.chip('همه', ITEMS.length, s.cat === 'all', function () { self.setState({ cat: 'all' }); })];
    CATS.forEach(function (c) {
      catChips.push(self.chip(c.name, c.count, s.cat === c.key,
        function () { self.setState({ cat: c.key }); }, c.color, c.soft));
    });

    var diffChips = [
      this.chip('هر سطحی', null, s.maxdiff === 0, function () { self.setState({ maxdiff: 0 }); }),
      this.chip('فقط بدون کد', null, s.maxdiff === 1, function () { self.setState({ maxdiff: 1 }); }),
      this.chip('تا کم‌کد', null, s.maxdiff === 2, function () { self.setState({ maxdiff: 2 }); }),
      this.chip('تا نیمه‌فنی', null, s.maxdiff === 3, function () { self.setState({ maxdiff: 3 }); })
    ];

    var satChips = [
      this.chip('هر رقابتی', null, s.satf === 'all', function () { self.setState({ satf: 'all' }); }),
      this.chip('کم‌رقابت', null, s.satf === 'low', function () { self.setState({ satf: 'low' }); }),
      this.chip('پررقابت', null, s.satf === 'high', function () { self.setState({ satf: 'high' }); })
    ];

    var marketChips = [
      this.chip('هر بازاری', null, s.market === 'all', function () { self.setState({ market: 'all' }); }),
      this.chip('بازار داخلی', null, s.market === 'dom', function () { self.setState({ market: 'dom' }); }),
      this.chip('بازار جهانی', null, s.market === 'glob', function () { self.setState({ market: 'glob' }); })
    ];

    var modelChips = [this.chip('هر مدلی', null, s.model === 'all', function () { self.setState({ model: 'all' }); })];
    MODELS.forEach(function (m) {
      modelChips.push(self.chip(m.name, m.count, s.model === m.name,
        function () { self.setState({ model: m.name }); }));
    });

    var sortChips = [];
    SORTS.forEach(function (o) {
      sortChips.push(self.chip(o.name, null, s.sort === o.key, function () { self.setState({ sort: o.key }); }));
    });

    var presetCards = PRESETS.map(function (p) {
      var on = s.preset === p.key;
      var n = 0;
      ITEMS.forEach(function (it) { if (p.test(it)) { n++; } });
      return {
        name: p.name, hint: p.hint, countFa: faNum(n),
        style: 'text-align: right; padding: 16px 18px; border-radius: 14px; cursor: pointer; width: 100%%; '
          + 'box-sizing: border-box; border: 1px solid ' + (on ? '#166534' : '#E4E1D6') + '; '
          + 'background: ' + (on ? '#E3EEE1' : '#FFFFFF') + ';',
        nameStyle: 'font-size: 14px; font-weight: 800; margin: 0 0 6px; color: ' + (on ? '#166534' : '#16181C') + ';',
        onClick: function () {
          self.setState({ preset: on ? 'none' : p.key, cat: 'all', model: 'all', market: 'all', maxdiff: 0, satf: 'all' });
        }
      };
    });

    var dirty = s.q !== '' || s.cat !== 'all' || s.model !== 'all' || s.market !== 'all'
      || s.maxdiff !== 0 || s.satf !== 'all' || s.preset !== 'none';

    return {
      q: s.q,
      onQ: function (e) { self.setState({ q: e.target.value }); },
      onClear: function () {
        self.setState({ q: '', cat: 'all', model: 'all', market: 'all', maxdiff: 0, satf: 'all', preset: 'none' });
      },
      rows: rows,
      countFa: faNum(rows.length),
      totalFa: faNum(ITEMS.length),
      empty: rows.length === 0,
      dirty: dirty,
      catChips: catChips,
      diffChips: diffChips,
      satChips: satChips,
      marketChips: marketChips,
      modelChips: modelChips,
      sortChips: sortChips,
      presetCards: presetCards,

      codeChips: QCODE.map(function (o) { return self.chip(o.name, null, s.pCode === o.key, function () { self.setState({ pCode: o.key }); }); }),
      timeChips: QTIME.map(function (o) { return self.chip(o.name, null, s.pTime === o.key, function () { self.setState({ pTime: o.key }); }); }),
      speedChips: QSPEED.map(function (o) { return self.chip(o.name, null, s.pSpeed === o.key, function () { self.setState({ pSpeed: o.key }); }); }),
      pmodelChips: QMODEL.map(function (o) { return self.chip(o.name, null, s.pModel === o.key, function () { self.setState({ pModel: o.key }); }); }),
      pmarketChips: QMARKET.map(function (o) { return self.chip(o.name, null, s.pMarket === o.key, function () { self.setState({ pMarket: o.key }); }); }),
      picks: this.picks(),
      noPicks: this.picks().length === 0,

      cPrice: s.cPrice, cN: s.cN, cH: s.cH, cTarget: s.cTarget,
      onPrice: function (e) { self.setState({ cPrice: e.target.value }); },
      onN: function (e) { self.setState({ cN: e.target.value }); },
      onH: function (e) { self.setState({ cH: e.target.value }); },
      onTarget: function (e) { self.setState({ cTarget: e.target.value }); },
      unitChips: [
        self.chip('دلار', null, s.cUnit === 'usd', function () { self.setState({ cUnit: 'usd' }); }),
        self.chip('میلیون تومان', null, s.cUnit === 'toman', function () { self.setState({ cUnit: 'toman' }); })
      ],
      m: this.money()
    };
  }
}
''' % (J(ITEMS), J(cats_js), J(models_js))

if __name__ == '__main__':
    io.open(os.path.join(HERE, 'logic.js'), 'w', encoding='utf-8').write(LOGIC)
    print('logic', len(LOGIC), 'chars ·', N, 'items')
