# -*- coding: utf-8 -*-
"""فیلتر و جست‌وجوی «رصدخانه».

دفترها بر اساس تاریخ گروه می‌شوند. چون فیلتر ممکن است همهٔ خبرهای یک روز را
بردارد، سرصفحهٔ تاریخ در خودِ فهرستِ فیلترشده ساخته می‌شود نه در قالب.
"""
import io, json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data as D  # noqa: E402

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] if c.isdigit() else c for c in str(n))

# نام محصول‌ها لاتین‌اند و از متن فارسی درنمی‌آیند. بدون جداسازی، الگوریتم دوجهته
# نقطه و پرانتزِ کنارشان را می‌قاپد و جمله به‌هم می‌ریزد — «ChatGPT.» می‌شود «.ChatGPT».
# LRI/PDI همان کاری را می‌کند که unicode-bidi: isolate می‌کند، ولی در متن ساده،
# پس داخل {{...}} هم که HTML تزریق نمی‌شود کار می‌کند.
LRI, PDI = '\u2066', '\u2069'
# با شروعِ فقط حرفی، «9to5Mac» رقمِ اولش بیرون می‌ماند و «to5Mac9» خوانده می‌شود.
LAT = re.compile(r'[A-Za-z0-9][A-Za-z0-9._+\-/]*(?:[ ][A-Za-z0-9][A-Za-z0-9._+\-/]*)*')
HASLAT = re.compile(r'[A-Za-z]')

def iso(t):
    def rep(m):
        run = m.group(0)
        if not HASLAT.search(run):      # عددِ تنها، نه نامِ لاتین
            return run
        tail = ''
        while run and run[-1] in '._+-/':
            tail = run[-1] + tail
            run = run[:-1]
        return LRI + run + PDI + tail
    return LAT.sub(rep, t)

CATC = {k: (lab, col, soft) for (k, lab, col, soft) in D.CATS}
CONFC = {k: (lab, col, soft, _) for (k, lab, col, soft, _) in D.CONF}

items = []
for ed in D.EDITIONS:
    for it in ed['items']:
        clab, ccol, csoft = CATC[it['cat']]
        flab, fcol, fsoft, _ = CONFC[it['conf']]
        body = [iso(x) for x in it['body']]
        code = it.get('code', '')
        note = iso(it.get('note', ''))
        srcs = [dict(label=iso(s[0]), url=s[1]) for s in it.get('sources', [])]
        # متن جست‌وجو بدون نشانه‌های جداسازی می‌ماند تا تایپِ «mistral» هم بگیرد
        hay = ' '.join([it['title'], ' '.join(it['body']), it.get('why', ''),
                        it.get('note', ''), code, clab, flab, ed['fa'], ed['greg'],
                        it.get('tags', ''),   # نام‌های لاتین و مترادف‌ها، فقط برای جست‌وجو
                        ' '.join(x[0] for x in it.get('sources', []))]).lower()
        items.append(dict(
            ed=ed['iso'], edFa=ed['fa'], edGreg=ed['greg'], edIntro=ed['intro'],
            cat=it['cat'], catLabel=clab, catColor=ccol, catSoft=csoft,
            conf=it['conf'], confLabel=flab, confColor=fcol, confSoft=fsoft,
            date=it['date'], title=iso(it['title']),
            body=[dict(t=p) for p in body],
            code=code, hasCode=bool(code),
            why=iso(it.get('why', '')), hasWhy=bool(it.get('why')),
            note=note, hasNote=bool(note),
            srcs=srcs, nSrc=fa(len(srcs)),
            hay=hay))

cat_n = collections.Counter(i['cat'] for i in items)
conf_n = collections.Counter(i['conf'] for i in items)

cats_js = [dict(key=k, name=lab, color=c, soft=s, count=cat_n.get(k, 0))
           for (k, lab, c, s) in D.CATS]
confs_js = [dict(key=k, name=lab, color=c, soft=s, count=conf_n.get(k, 0))
            for (k, lab, c, s, _) in D.CONF]

J = lambda x: json.dumps(x, ensure_ascii=False)

LOGIC = '''
var ITEMS = %s;
var CATS = %s;
var CONFS = %s;

function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { q: '', cat: 'all', conf: 'all' };
  }

  chip(label, count, on, onClick, color, soft) {
    return {
      label: label,
      count: count === null ? '' : faNum(count),
      hasCount: count !== null,
      style: 'display: inline-flex; align-items: center; gap: 7px; font-size: 13px; font-weight: '
        + (on ? '700' : '500') + '; padding: 8px 14px; border-radius: 999px; cursor: pointer; '
        + 'border: 1px solid ' + (on ? (color || '#16494D') : '#E4E1D6') + '; '
        + 'background: ' + (on ? (soft || '#E2EDEC') : '#FFFFFF') + '; '
        + 'color: ' + (on ? (color || '#16494D') : '#45494F') + ';',
      onClick: onClick
    };
  }

  renderVals() {
    var self = this;
    var s = this.state;
    var q = s.q.trim().toLowerCase();

    var rows = ITEMS.filter(function (it) {
      if (s.cat !== 'all' && it.cat !== s.cat) { return false; }
      if (s.conf !== 'all' && it.conf !== s.conf) { return false; }
      if (q && it.hay.indexOf(q) === -1) { return false; }
      return true;
    }).map(function (it) {
      var o = {}; for (var k in it) { o[k] = it[k]; } return o;
    });

    // سرصفحهٔ تاریخ روی نخستین خبرِ هر روز که از فیلتر رد شده، نه روی روزِ خالی
    var seen = '';
    rows.forEach(function (r) {
      r.newDay = r.ed !== seen;
      seen = r.ed;
    });

    var catChips = [this.chip('همه', ITEMS.length, s.cat === 'all',
      function () { self.setState({ cat: 'all' }); })];
    CATS.forEach(function (c) {
      catChips.push(self.chip(c.name, c.count, s.cat === c.key,
        function () { self.setState({ cat: c.key }); }, c.color, c.soft));
    });

    var confChips = [this.chip('هر اعتباری', null, s.conf === 'all',
      function () { self.setState({ conf: 'all' }); })];
    CONFS.forEach(function (c) {
      confChips.push(self.chip(c.name, c.count, s.conf === c.key,
        function () { self.setState({ conf: c.key }); }, c.color, c.soft));
    });

    return {
      q: s.q,
      onQ: function (e) { self.setState({ q: e.target.value }); },
      onClear: function () { self.setState({ q: '', cat: 'all', conf: 'all' }); },
      rows: rows,
      countFa: faNum(rows.length),
      empty: rows.length === 0,
      filtered: rows.length !== ITEMS.length,
      catChips: catChips,
      confChips: confChips
    };
  }
}
''' % (J(items), J(cats_js), J(confs_js))

if __name__ == '__main__':
    io.open(os.path.join(HERE, 'logic.js'), 'w', encoding='utf-8').write(LOGIC)
    print('logic', len(LOGIC), 'chars ·', len(items), 'items')
