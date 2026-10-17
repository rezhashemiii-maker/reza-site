
function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}

// هشت دستور. هیچ‌کدام چیزی «نمی‌فهمد» — هر کدام یک کار یکتا و بی‌ابهام می‌کند.
var PROGRAM = [
  { t: 'در کوزهٔ «شمار» بگذار: هیچ', k: 'set', jar: 'شمار', v: 0 },
  { t: 'در کوزهٔ «کیسه» بگذار: آنچه شمردی', k: 'setn', jar: 'کیسه' },
  { t: 'اگر کوزهٔ «کیسه» خالی است، برو به دستور ۸', k: 'ifzero', jar: 'کیسه', to: 7 },
  { t: 'یکی به کوزهٔ «شمار» بیفزا', k: 'inc', jar: 'شمار' },
  { t: 'یکی از کوزهٔ «کیسه» بردار', k: 'dec', jar: 'کیسه' },
  { t: 'بنویس: «یک کیسه شمرده شد»', k: 'say', s: 'یک کیسه شمرده شد' },
  { t: 'برو به دستور ۳', k: 'goto', to: 2 },
  { t: 'بنویس: «جمع کیسه‌ها» و آنچه در کوزهٔ «شمار» است', k: 'sayjar', s: 'جمع کیسه‌ها: ', jar: 'شمار' }
];

var MAXSTEPS = 400;

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = this.fresh(5);
  }

  fresh(n) {
    return { n: n, pc: 0, jars: { 'شمار': null, 'کیسه': null }, out: [], steps: 0, done: false };
  }

  // یک گام: دقیقاً همان کاری که دستور می‌گوید، نه یک ذره بیشتر
  step(s) {
    if (s.done) { return s; }
    var ins = PROGRAM[s.pc];
    var jars = { 'شمار': s.jars['شمار'], 'کیسه': s.jars['کیسه'] };
    var out = s.out.slice();
    var pc = s.pc + 1;

    if (ins.k === 'set') { jars[ins.jar] = ins.v; }
    else if (ins.k === 'setn') { jars[ins.jar] = s.n; }
    else if (ins.k === 'inc') { jars[ins.jar] = (jars[ins.jar] || 0) + 1; }
    else if (ins.k === 'dec') { jars[ins.jar] = (jars[ins.jar] || 0) - 1; }
    else if (ins.k === 'say') { out.push(ins.s); }
    else if (ins.k === 'sayjar') { out.push(ins.s + faNum(jars[ins.jar])); }
    else if (ins.k === 'goto') { pc = ins.to; }
    else if (ins.k === 'ifzero') { if (jars[ins.jar] === 0) { pc = ins.to; } }

    var steps = s.steps + 1;
    var done = pc >= PROGRAM.length || steps >= MAXSTEPS;
    return { n: s.n, pc: done ? PROGRAM.length - 1 : pc, jars: jars, out: out, steps: steps, done: done };
  }

  chip(label, on, onClick) {
    return {
      label: label,
      style: 'font-size: 13px; font-weight: ' + (on ? '700' : '500') + '; padding: 7px 14px; '
        + 'border-radius: 999px; cursor: pointer; border: 1px solid ' + (on ? '#6B4226' : '#E4E1D6') + '; '
        + 'background: ' + (on ? '#F3E8DE' : '#FFFFFF') + '; color: ' + (on ? '#6B4226' : '#45494F') + ';',
      onClick: onClick
    };
  }

  renderVals() {
    var self = this;
    var s = this.state;

    var lines = PROGRAM.map(function (ins, i) {
      var here = i === s.pc && !s.done;
      var fin = i === s.pc && s.done;
      return {
        noFa: faNum(i + 1),
        t: ins.t,
        style: 'display: flex; gap: 12px; align-items: flex-start; padding: 10px 13px; border-radius: 9px; '
          + 'background: ' + (here ? '#F3E8DE' : (fin ? '#E7ECE4' : 'transparent')) + '; '
          + 'border: 1px solid ' + (here ? '#6B4226' : (fin ? '#2F5233' : 'transparent')) + ';',
        noStyle: 'flex-shrink: 0; width: 20px; font-size: 12px; font-weight: 700; font-variant-numeric: tabular-nums; '
          + 'color: ' + (here ? '#6B4226' : (fin ? '#2F5233' : '#A8A296')) + ';',
        tStyle: 'font-size: 13.5px; line-height: 1.9; color: ' + (here || fin ? '#16181C' : '#45494F') + ';'
      };
    });

    var jar = function (name) {
      var v = s.jars[name];
      return {
        name: name,
        val: v === null ? '—' : faNum(v),
        empty: v === null,
        note: v === null ? 'هنوز چیزی در آن نگذاشته‌ایم' : (v === 0 ? 'خالی است' : 'در آن ' + faNum(v) + ' تا هست'),
        valStyle: 'font-size: 34px; font-weight: 800; line-height: 1; color: ' + (v === null ? '#C8C2B6' : '#6B4226') + ';'
      };
    };

    return {
      nChips: [3, 5, 8].map(function (k) {
        return self.chip(faNum(k) + ' کیسه', s.n === k, function () { self.setState(self.fresh(k)); });
      }),
      lines: lines,
      jars: [jar('شمار'), jar('کیسه')],
      out: s.out.map(function (x) { return { t: x }; }),
      hasOut: s.out.length > 0,
      stepsFa: faNum(s.steps),
      done: s.done,
      running: !s.done,
      nextStyle: 'font-size: 14px; font-weight: 700; color: #FFFFFF; background: '
        + (s.done ? '#C8C2B6' : '#6B4226') + '; padding: 11px 22px; border-radius: 10px; cursor: '
        + (s.done ? 'default' : 'pointer') + ';',
      onStep: function () { if (!self.state.done) { self.setState(self.step(self.state)); } },
      onRun: function () {
        var st = self.state;
        var guard = 0;
        while (!st.done && guard < MAXSTEPS) { st = self.step(st); guard++; }
        self.setState(st);
      },
      onReset: function () { self.setState(self.fresh(self.state.n)); }
    };
  }
}
