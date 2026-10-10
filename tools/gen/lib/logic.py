# -*- coding: utf-8 -*-
import json, io, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = json.load(io.open(os.path.join(HERE, 'refs.json'), encoding='utf-8'))

DOMS = [
    ('امنیت',              'sec',   '#C2410C', '#F7E3D6'),
    ('یادگیری ماشین',      'learn', '#2F5233', '#E7ECE4'),
    ('سواد هوش مصنوعی',    'ai',    '#7E22CE', '#EEE2F9'),
    ('شطرنج',              'chess', '#8A1538', '#F3E3E7'),
    ('نظریهٔ بازی',         'game',  '#0E6FB4', '#DCEBFA'),
]
DOMKEY = {d[0]: d[1] for d in DOMS}
DOMCOL = {d[0]: (d[2], d[3]) for d in DOMS}

KIND_GROUP = {'استاندارد': 'استاندارد و چارچوب', 'چارچوب': 'استاندارد و چارچوب',
              'فهرست': 'استاندارد و چارچوب', 'مقررات': 'استاندارد و چارچوب',
              'بیانیه': 'استاندارد و چارچوب'}
KINDS = ['مقاله', 'کتاب', 'استاندارد و چارچوب', 'گزارش']

FAD = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return ''.join(FAD[int(c)] for c in str(n))

items = []
for r in ROWS:
    kg = KIND_GROUP.get(r['kind'], r['kind'])
    doms = [dict(name=d, key=DOMKEY[d], color=DOMCOL[d][0], soft=DOMCOL[d][1],
                 sec=DOMKEY[d] == 'sec', learn=DOMKEY[d] == 'learn', ai=DOMKEY[d] == 'ai',
                 chess=DOMKEY[d] == 'chess', game=DOMKEY[d] == 'game') for d in r['domains']]
    hay = ' '.join(filter(None, [r['titleEn'], r['titleFa'], r['who'], r['note'],
                                 r['kind'], str(r['year']), ' '.join(r['domains'])])).lower()
    items.append(dict(
        y=r['year'], yFa=fa(r['year']), en=r['titleEn'], fa=r['titleFa'] or '',
        hasFa=bool(r['titleFa']), who=r['who'], kind=r['kind'], kindGroup=kg,
        note=r['note'], hasNote=bool(r['note']), topic=r.get('topic') or '',
        link=r['link'] or '', hasLink=bool(r['link']),
        doms=doms, domKeys=[DOMKEY[d] for d in r['domains']],
        cross=len(doms) > 1, crossFa=fa(len(doms)),
        color=doms[0]['color'], hay=hay))

counts_dom = collections.Counter(k for it in items for k in it['domKeys'])
counts_kind = collections.Counter(it['kindGroup'] for it in items)

doms_js = [dict(name=n, key=k, color=c, soft=s, count=counts_dom[k]) for (n, k, c, s) in DOMS]
kinds_js = [dict(name=k, count=counts_kind.get(k, 0)) for k in KINDS]

J = lambda x: json.dumps(x, ensure_ascii=False)

LOGIC = '''
var ITEMS = %s;
var DOMS = %s;
var KINDS = %s;

function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { q: '', dom: 'all', kind: 'all', sort: 'asc' };
  }

  filtered() {
    var s = this.state;
    var q = s.q.trim().toLowerCase();
    var out = ITEMS.filter(function (it) {
      if (s.dom !== 'all' && it.domKeys.indexOf(s.dom) === -1) { return false; }
      if (s.kind !== 'all' && it.kindGroup !== s.kind) { return false; }
      if (q && it.hay.indexOf(q) === -1) { return false; }
      return true;
    });
    out = out.slice();
    out.sort(function (a, b) {
      return s.sort === 'asc' ? a.y - b.y : b.y - a.y;
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
        + 'border: 1px solid ' + (on ? (color || '#1F4E5F') : '#E4E1D6') + '; '
        + 'background: ' + (on ? (soft || '#E2EDF1') : '#FFFFFF') + '; '
        + 'color: ' + (on ? (color || '#1F4E5F') : '#45494F') + ';',
      onClick: onClick
    };
  }

  renderVals() {
    var self = this;
    var s = this.state;
    var rows = this.filtered();

    var domChips = [this.chip('همه', ITEMS.length, s.dom === 'all', function () { self.setState({ dom: 'all' }); })];
    DOMS.forEach(function (d) {
      domChips.push(self.chip(d.name, d.count, s.dom === d.key,
        function () { self.setState({ dom: d.key }); }, d.color, d.soft));
    });

    var kindChips = [this.chip('هر نوع', null, s.kind === 'all', function () { self.setState({ kind: 'all' }); })];
    KINDS.forEach(function (k) {
      kindChips.push(self.chip(k.name, k.count, s.kind === k.name,
        function () { self.setState({ kind: k.name }); }));
    });

    var sortChips = [
      this.chip('قدیمی‌ترین اول', null, s.sort === 'asc', function () { self.setState({ sort: 'asc' }); }),
      this.chip('تازه‌ترین اول', null, s.sort === 'desc', function () { self.setState({ sort: 'desc' }); })
    ];

    return {
      q: s.q,
      onQ: function (e) { self.setState({ q: e.target.value }); },
      onClear: function () { self.setState({ q: '', dom: 'all', kind: 'all' }); },
      rows: rows,
      countFa: faNum(rows.length),
      empty: rows.length === 0,
      filtered: rows.length !== ITEMS.length,
      domChips: domChips,
      kindChips: kindChips,
      sortChips: sortChips
    };
  }
}
''' % (J(items), J(doms_js), J(kinds_js))

if __name__ == '__main__':
    io.open(os.path.join(HERE, 'logic.js'), 'w', encoding='utf-8').write(LOGIC)
    print('logic', len(LOGIC), 'chars ·', len(items), 'items')
