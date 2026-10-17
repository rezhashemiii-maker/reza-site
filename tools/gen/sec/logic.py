# -*- coding: utf-8 -*-
import json, io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data import CATS, ITEMS, EVENTS

def slugify(en):
    s = re.sub(r'[^a-z0-9]+', '-', en.lower()).strip('-')
    return s[:48]

items = []
for (yr, cat, kind, fa, en, who, imp, adv, href) in sorted(ITEMS, key=lambda r: (r[0], r[1])):
    c = next(x for x in CATS if x['key'] == cat)
    items.append(dict(y=yr, cat=cat, catName=c['name'], color=c['color'], soft=c['soft'],
                      kind=kind, fa=fa, en=en, who=who, imp=imp, adv=adv, href=href,
                      slug=slugify(en),
                      hay=(fa + ' ' + en + ' ' + who + ' ' + adv + ' ' + c['name'] + ' ' + kind + ' ' + str(yr)).lower()))

KINDS = ['کتاب', 'مقاله', 'استاندارد و چارچوب']
KIND_MAP = {'استاندارد': 'استاندارد و چارچوب', 'چارچوب': 'استاندارد و چارچوب',
            'فهرست': 'استاندارد و چارچوب', 'مقررات': 'استاندارد و چارچوب',
            'بیانیه': 'استاندارد و چارچوب', 'گزارش': 'مقاله', 'رویداد': 'مقاله'}
for it in items:
    it['kindGroup'] = KIND_MAP.get(it['kind'], it['kind'])

# شمارهٔ صفحهٔ معرفیِ هر کتاب. ترتیب از books/data.py می‌آید، نه از مرتب‌سازی این‌جا،
# چون دو کتاب هم‌سال داریم و ترتیبشان باید با نام فایل SecBookNN یکی بماند.
BOOK_NO = {'دیوارهای آتش و امنیت اینترنت': 1, 'رمزنگاری کاربردی': 2, 'امنیت شبکه: ارتباط خصوصی در دنیای عمومی': 3, 'امنیت شبکه و میان\u200cشبکه\u200cای: اصول و عمل': 4, 'مهندسی امنیت': 5, 'نوشتن کد امن (ویرایش دوم)': 6, 'امنیت رایانه: هنر و دانش': 7, 'هنر ارزیابی امنیت نرم\u200cافزار': 8, 'کتاب راهنمای هکر برنامه\u200cهای وب': 9, 'مهندسی رمزنگاری': 10, 'تار درهم': 11, 'مدل\u200cسازی تهدید: طراحی برای امنیت': 12, 'شبکه\u200cهای اعتماد صفر': 13, 'مهندسی امنیت، ویرایش سوم': 14, 'ساختن سامانه\u200cهای امن و قابل\u200cاتکا': 15}
for it in items:
    it['bookNo'] = BOOK_NO.get(it['fa'], 0) if it['kindGroup'] == 'کتاب' else 0
_books = [i for i in items if i['kindGroup'] == 'کتاب']
assert len(_books) == 15, len(_books)
assert sorted(i['bookNo'] for i in _books) == list(range(1, 16)), \
    'شمارهٔ کتاب‌ها با books/data.py نمی‌خواند: %s' % [(i['fa'], i['bookNo']) for i in _books]

SHORT = {'found': 'مبانی', 'crypto': 'رمزنگاری', 'net': 'شبکه', 'soft': 'نرم‌افزار',
         'ops': 'عملیات', 'ml': 'یادگیری ماشین'}
cats_js = [dict(key=c['key'], name=c['name'], short=SHORT[c['key']], color=c['color'], soft=c['soft'],
                blurb=c['blurb'], count=sum(1 for i in items if i['cat'] == c['key'])) for c in CATS]

events_js = [dict(y=y, m=m, fa=fa, en=en, note=note) for (y, m, fa, en, note) in sorted(EVENTS)]

J = lambda x: json.dumps(x, ensure_ascii=False)

LOGIC = '''
var CATS = %s;
var ITEMS = %s;
var EVENTS = %s;
var KINDS = %s;

function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}

var Y0 = 1973, Y1 = 2026;
var PLOT = { x0: 40, x1: 880, gutter: 992, evY: 18, sep: 36, y0: 42, laneH: 46 };

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { cat: 'all', kind: 'all', q: '' };
  }

  filtered() {
    var s = this.state;
    var q = s.q.trim().toLowerCase();
    return ITEMS.filter(function (it) {
      if (s.cat !== 'all' && it.cat !== s.cat) { return false; }
      if (s.kind !== 'all' && it.kindGroup !== s.kind) { return false; }
      if (q && it.hay.indexOf(q) === -1) { return false; }
      return true;
    });
  }

  chip(label, count, active, value, key, color, soft) {
    var self = this;
    var on = value === active;
    return {
      label: label, count: count === null ? '' : faNum(count),
      bg: on ? (soft || '#E7ECE4') : '#FFFFFF',
      fg: on ? (color || '#2F5233') : '#45494F',
      border: on ? (color || '#2F5233') : '#E4E1D6',
      pick: function () { var p = {}; p[key] = value; self.setState(p); }
    };
  }

  // قدیمی‌ترین سمت راست، تازه‌ترین سمت چپ — هم‌جهت با خواندن فارسی
  xOf(year) { return PLOT.x1 - ((year - Y0) / (Y1 - Y0)) * (PLOT.x1 - PLOT.x0); }

  // نقطه‌های خط زمان: هر دسته یک خط، و آثار هم‌سال روی هم چیده می‌شوند
  points(list) {
    var self = this;
    var out = [], seen = {};
    var byCat = {};
    for (var c = 0; c < CATS.length; c++) { byCat[CATS[c].key] = c; }
    var sorted = list.slice().sort(function (a, b) { return a.y - b.y; });
    for (var i = 0; i < sorted.length; i++) {
      var it = sorted[i];
      var lane = byCat[it.cat];
      var key = it.cat + ':' + it.y;
      var n = seen[key] || 0;
      seen[key] = n + 1;
      var cy = PLOT.y0 + lane * PLOT.laneH + 22 + (n === 0 ? 0 : (n === 1 ? -11 : 11));
      out.push({
        cx: self.xOf(it.y).toFixed(1), cy: cy.toFixed(1),
        r: (it.imp >= 5 ? 7 : (it.imp >= 4 ? 5.5 : 4)).toFixed(1),
        color: it.color,
        tip: faNum(it.y) + ' — ' + it.fa + ' · ' + it.who
      });
    }
    return out;
  }

  renderVals() {
    var self = this;
    var list = this.filtered();

    var lanes = CATS.map(function (c, i) {
      return {
        name: c.short, color: c.color,
        ly: (PLOT.y0 + i * PLOT.laneH + 26).toFixed(1),
        lineY: (PLOT.y0 + i * PLOT.laneH + 22).toFixed(1),
        x0: PLOT.x0, x1: PLOT.x1, lx: PLOT.gutter
      };
    });

    var ticks = [];
    for (var y = 1975; y <= 2025; y += 10) {
      var tx = self.xOf(y);
      ticks.push({ x: tx.toFixed(1), pct: (tx / 10).toFixed(1), label: faNum(y), y2: (PLOT.y0 + CATS.length * PLOT.laneH).toFixed(1) });
    }

    // رویدادها همیشه نشان داده می‌شوند — زمینه‌اند، نه داده‌ای که فیلتر شود
    var evSeen = {};
    var events = EVENTS.map(function (e) {
      var x = self.xOf(e.y);
      var n = evSeen[e.y] || 0;
      evSeen[e.y] = n + 1;
      var cy = PLOT.evY + (n === 0 ? 0 : (n === 1 ? -11 : 11));
      return {
        d: 'M ' + x.toFixed(1) + ' ' + (cy - 5.5) + ' L ' + (x + 5).toFixed(1) + ' ' + cy +
           ' L ' + x.toFixed(1) + ' ' + (cy + 5.5) + ' L ' + (x - 5).toFixed(1) + ' ' + cy + ' Z',
        tip: faNum(e.y) + ' ' + e.m + ' — ' + e.fa,
        yFa: faNum(e.y), fa: e.fa, en: e.en, m: e.m, note: e.note
      };
    });

    // شتاب: شمار آثار در هر بازهٔ پنج‌ساله
    var buckets = [];
    for (var b = 1970; b <= 2025; b += 5) {
      var n = 0;
      for (var k = 0; k < list.length; k++) { if (list[k].y >= b && list[k].y < b + 5) { n++; } }
      buckets.push({ from: b, n: n, label: faNum(b) });
    }
    var maxB = 1;
    for (var m = 0; m < buckets.length; m++) { if (buckets[m].n > maxB) { maxB = buckets[m].n; } }
    // روی صفحهٔ باریک، برچسب هر بازهٔ دوم کافی است تا ردیف سرریز نکند
    var bars = buckets.map(function (bk, bi) {
      return { label: bk.label, axis: bi %% 2 === 0 ? bk.label : '·', n: bk.n,
               nFa: bk.n ? faNum(bk.n) : '', h: Math.round((bk.n / maxB) * 100), show: bk.n > 0 };
    });

    var byDecadeNote = '';
    var mlCount = 0, mlRecent = 0;
    for (var z = 0; z < ITEMS.length; z++) {
      if (ITEMS[z].cat === 'ml') { mlCount++; if (ITEMS[z].y >= 2013) { mlRecent++; } }
    }

    return {
      totalFa: faNum(ITEMS.length),
      shownFa: faNum(list.length),
      bookFa: faNum(ITEMS.filter(function (i) { return i.kindGroup === 'کتاب'; }).length),
      spanFa: faNum(Y1 - 1 - Y0 + 1),
      mlFa: faNum(mlCount),
      mlRecentFa: faNum(mlRecent),
      q: this.state.q,
      onQuery: function (e) { self.setState({ q: e.target.value }); },
      catChips: [this.chip('همه', ITEMS.length, this.state.cat, 'all', 'cat', '#2F5233', '#E7ECE4')].concat(
        CATS.map(function (c) { return self.chip(c.name, c.count, self.state.cat, c.key, 'cat', c.color, c.soft); })),
      kindChips: [this.chip('همه', null, this.state.kind, 'all', 'kind', '#2F5233', '#E7ECE4')].concat(
        KINDS.map(function (k) {
          var n = ITEMS.filter(function (i) { return i.kindGroup === k; }).length;
          return self.chip(k, n, self.state.kind, k, 'kind', '#2F5233', '#E7ECE4');
        })),
      lanes: lanes,
      ticks: ticks,
      events: events,
      evCountFa: faNum(EVENTS.length),
      evLabelY: (PLOT.evY + 4).toFixed(1),
      sepY: PLOT.sep,
      gutter: PLOT.gutter,
      plotX0: PLOT.x0,
      plotX1: PLOT.x1,
      dots: this.points(list),
      plotH: (PLOT.y0 + CATS.length * PLOT.laneH + 26).toFixed(0),
      bars: bars,
      catCards: CATS.map(function (c) { return { name: c.name, blurb: c.blurb, color: c.color, soft: c.soft, countFa: faNum(c.count) }; }),
      list: list.map(function (it) {
        return {
          yFa: faNum(it.y), fa: it.fa, en: it.en, who: it.who, adv: it.adv, href: it.href,
          kind: it.kind, catName: it.catName, color: it.color, soft: it.soft,
          impFa: '★'.repeat(it.imp) + '☆'.repeat(5 - it.imp),
          isBook: it.kindGroup === 'کتاب',
          bookNo: it.bookNo || 0,
          b01: it.bookNo === 1, b02: it.bookNo === 2, b03: it.bookNo === 3,
          b04: it.bookNo === 4, b05: it.bookNo === 5, b06: it.bookNo === 6,
          b07: it.bookNo === 7, b08: it.bookNo === 8, b09: it.bookNo === 9,
          b10: it.bookNo === 10, b11: it.bookNo === 11, b12: it.bookNo === 12,
          b13: it.bookNo === 13, b14: it.bookNo === 14, b15: it.bookNo === 15
        };
      }),
      empty: list.length === 0
    };
  }
}
'''  % (J(cats_js), J(items), J(events_js), J(KINDS))

io.open(os.path.join(HERE, 'logic.js'), 'w', encoding='utf-8').write(LOGIC)
print('logic.js:', len(LOGIC), 'chars ·', len(items), 'items')
