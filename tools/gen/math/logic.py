# -*- coding: utf-8 -*-
"""خواننده خودش خط را جا می‌اندازد، و بعد می‌گذارد ماشین با سراشیبی پیدایش کند."""
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402

LOGIC = r'''
function faNum(x) {
  var m = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
  return String(x).replace(/[0-9]/g, function (c) { return m[c]; });
}
// جداکنندهٔ کسری در فارسی «٫» است، نه نقطهٔ لاتین؛ بقیهٔ متن سایت هم همین را دارد.
function fa1(v) { return faNum((Math.round(v * 10) / 10).toFixed(1)).replace('.', '٫'); }
function fa2(v) { return faNum((Math.round(v * 100) / 100).toFixed(2)).replace('.', '٫'); }

// شش کرت: چند پیمانه آب دادی، چند خروار برداشتی
var PTS = [{ x: 1, y: 3 }, { x: 2, y: 5 }, { x: 3, y: 4 },
           { x: 4, y: 8 }, { x: 5, y: 9 }, { x: 6, y: 11 }];
var BEST_A = 1.6, BEST_B = 16 / 15;   // جواب دقیقِ کمترین مربعات
var LR = 0.008, MAXRUN = 600;

// مختصات نقاشی
var X0 = 70, X1 = 480, Y0 = 232, Y1 = 26;
var XMIN = 0, XMAX = 7, YMIN = 0, YMAX = 12;
function px(x) { return X0 + (x - XMIN) / (XMAX - XMIN) * (X1 - X0); }
function py(y) { return Y0 + (y - YMIN) / (YMAX - YMIN) * (Y1 - Y0); }

function sse(a, b) {
  var s = 0;
  PTS.forEach(function (p) { var e = p.y - (a * p.x + b); s += e * e; });
  return s;
}
function grad(a, b) {
  var ga = 0, gb = 0;
  PTS.forEach(function (p) {
    var e = p.y - (a * p.x + b);
    ga += -2 * p.x * e; gb += -2 * e;
  });
  return [ga, gb];
}

class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { a: 0, b: 0, steps: 0 };
  }

  descend(s, n) {
    var a = s.a, b = s.b, k = 0;
    for (; k < n; k++) {
      var g = grad(a, b);
      a -= LR * g[0]; b -= LR * g[1];
      if (Math.abs(g[0]) + Math.abs(g[1]) < 0.0008) { k++; break; }
    }
    return { a: a, b: b, steps: s.steps + k };
  }

  btn(label, onClick, strong) {
    return {
      label: label,
      style: 'font-size: 13.5px; font-weight: ' + (strong ? '700' : '600') + '; padding: 10px 16px; '
        + 'border-radius: 10px; cursor: pointer; border: 1px solid '
        + (strong ? '#1E3A5F' : '#E4E1D6') + '; background: ' + (strong ? '#1E3A5F' : '#FFFFFF')
        + '; color: ' + (strong ? '#FFFFFF' : '#16181C') + ';',
      onClick: onClick
    };
  }

  renderVals() {
    var self = this;
    var s = this.state;
    var a = s.a, b = s.b;
    var err = sse(a, b);
    var best = sse(BEST_A, BEST_B);
    var close = Math.abs(a - BEST_A) < 0.02 && Math.abs(b - BEST_B) < 0.05;

    var dots = PTS.map(function (p) {
      var yh = a * p.x + b;
      var e = p.y - yh;
      return {
        cx: px(p.x).toFixed(1), cy: py(p.y).toFixed(1),
        ey: py(yh).toFixed(1),
        eCol: Math.abs(e) < 0.6 ? '#2F5233' : (Math.abs(e) < 1.6 ? '#8A8578' : '#B4530E'),
        label: faNum(p.x) + ' پیمانه، ' + faNum(p.y) + ' خروار'
      };
    });

    // خط در دو لبهٔ محور، بریده‌شده تا از کادر بیرون نزند
    var cl = function (x) { var y = a * x + b; return Math.max(YMIN, Math.min(YMAX, y)); };
    var xa = XMIN, xb = XMAX;
    var ya = cl(xa), yb = cl(xb);
    if (a !== 0) {
      if (a * xa + b < YMIN) { xa = (YMIN - b) / a; } else if (a * xa + b > YMAX) { xa = (YMAX - b) / a; }
      if (a * xb + b < YMIN) { xb = (YMIN - b) / a; } else if (a * xb + b > YMAX) { xb = (YMAX - b) / a; }
      xa = Math.max(XMIN, Math.min(XMAX, xa)); xb = Math.max(XMIN, Math.min(XMAX, xb));
      ya = a * xa + b; yb = a * xb + b;
    }

    var ticksX = [1, 2, 3, 4, 5, 6].map(function (v) {
      return { x: px(v).toFixed(1), y: (Y0 + 18).toFixed(1), t: faNum(v) };
    });
    var ticksY = [0, 3, 6, 9, 12].map(function (v) {
      return { x: (X0 - 12).toFixed(1), y: (py(v) + 4).toFixed(1), t: faNum(v),
               gx1: X0, gx2: X1, gy: py(v).toFixed(1) };
    });

    var set = function (da, db) {
      return function () {
        self.setState({ a: Math.max(-1, Math.min(4, self.state.a + da)),
                        b: Math.max(-4, Math.min(10, self.state.b + db)),
                        steps: self.state.steps });
      };
    };

    return {
      dots: dots, ticksX: ticksX, ticksY: ticksY,
      lx1: px(xa).toFixed(1), ly1: py(ya).toFixed(1),
      lx2: px(xb).toFixed(1), ly2: py(yb).toFixed(1),
      aFa: fa1(a), bFa: fa1(b),
      // نزدیک جواب، گردکردن به عدد صحیح خطا را ۵ نشان می‌داد در حالی که
      // کمترین خطای ممکن ۴٫۵۳ است و خواننده فکر می‌کرد هنوز جا دارد.
      errFa: err >= 20 ? faNum(Math.round(err)) : fa2(err), err2Fa: fa2(err),
      bestFa: fa2(best),
      barW: Math.max(1, Math.min(100, Math.round(err / 316 * 100))),
      stepsFa: faNum(s.steps),
      close: close, notClose: !close,
      verdict: close
        ? 'این همان کمترین خطای ممکن است. هیچ خط راستی نمی‌تواند از این بهتر باشد.'
        : (err < 20 ? 'نزدیک شدی. هنوز می‌شود کمترش کرد.'
                    : 'خطا هنوز بزرگ است؛ خط از نقطه‌ها دور است.'),
      vStyle: 'font-size: 13.5px; line-height: 1.95; font-weight: 600; margin: 0; color: '
        + (close ? '#2F5233' : (err < 20 ? '#8A8578' : '#B4530E')) + ';',
      btns: [
        self.btn('شیب بیشتر', set(0.2, 0)),
        self.btn('شیب کمتر', set(-0.2, 0)),
        self.btn('بالاتر', set(0, 0.5)),
        self.btn('پایین‌تر', set(0, -0.5))
      ],
      runs: [
        self.btn('یک گام سراشیبی', function () { self.setState(self.descend(self.state, 1)); }, true),
        self.btn('ده گام', function () { self.setState(self.descend(self.state, 10)); }, true),
        self.btn('تا ته برو', function () { self.setState(self.descend(self.state, MAXRUN)); }),
        self.btn('از نو', function () { self.setState({ a: 0, b: 0, steps: 0 }); })
      ]
    };
  }
}
'''

if __name__ == '__main__':
    io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logic.js'), 'w',
            encoding='utf-8').write(LOGIC)
    print('logic', len(LOGIC), 'chars')
