var ROOMS = [
  { name: 'سالن ۱', color: '#B4530E', soft: '#F4E3D3', scale: 0.92 },
  { name: 'سالن ۲', color: '#166534', soft: '#E3EEE1', scale: 1.08 },
  { name: 'سالن ۳', color: '#0E6FB4', soft: '#DCEBFA', scale: 1.0 }
];

var PHASES = {
  spawn:    { label: 'اسپان‌ران',         bg: '#F4E3D3', compost: [24, 26], room: [23, 26], rh: [92, 96], co2: [5000, 20000] },
  casing:   { label: 'کیسینگ‌ران',        bg: '#EBE3F5', compost: [23, 26], room: [22, 25], rh: [93, 97], co2: [4000, 12000] },
  pinning:  { label: 'ونتیلیشن و پین‌ست', bg: '#DCEBFA', compost: [18, 21], room: [16, 19], rh: [88, 93], co2: [800, 1500] },
  flush:    { label: 'فلاش و برداشت',     bg: '#BFDCBA', compost: [18, 21], room: [16, 19], rh: [85, 90], co2: [800, 1500] },
  rest:     { label: 'استراحت بین فلاش',  bg: '#F1EEE7', compost: [18, 21], room: [16, 19], rh: [85, 90], co2: [800, 1500] },
  cleanout: { label: 'تخلیه و ضدعفونی',   bg: '#E0DACB', compost: [18, 21], room: [16, 19], rh: [85, 90], co2: [800, 1500] }
};

var DEFAULTS = { price: '185000', compostCost: '12000', pickCost: '15000', fixedCost: '38000000' };
var YIELD = { 21: 62, 22: 148, 23: 124, 24: 71, 28: 47, 29: 88, 30: 72, 31: 36, 35: 26, 36: 47, 37: 36, 38: 19 };
var COMPOST_PER_ROOM = 2800;
var CASING_COST = 12000;

function phaseKey(d) {
  if (d < 14) { return 'spawn'; }
  if (d < 18) { return 'casing'; }
  if (d < 21) { return 'pinning'; }
  if (d < 25) { return 'flush'; }
  if (d < 28) { return 'rest'; }
  if (d < 32) { return 'flush'; }
  if (d < 35) { return 'rest'; }
  if (d < 39) { return 'flush'; }
  return 'cleanout';
}

function centers(d) {
  var compost, room, rh, co2;
  if (d <= 2) { compost = 27 - d * 0.5; } else if (d <= 14) { compost = 26 - (d - 2) * 0.1; }
  else if (d <= 18) { compost = 24.5; } else if (d <= 21) { compost = 24 - (d - 18) * 1.2; }
  else { compost = 19.6; }

  if (d <= 14) { room = 25 - d * 0.035; } else if (d <= 17) { room = 24.4; }
  else if (d <= 21) { room = 24 - (d - 17) * 1.55; } else { room = 17.7; }

  if (d <= 13) { rh = 94.8 - d * 0.07; } else if (d <= 17) { rh = 95.4; }
  else if (d <= 21) { rh = 94 - (d - 17) * 1.5; }
  else { rh = (phaseKey(d) === 'rest') ? 89.5 : 87.2; }

  if (d <= 10) { co2 = 3000 + d * 1500; } else if (d <= 14) { co2 = 18000 - (d - 10) * 750; }
  else if (d <= 18) { co2 = 15000 - (d - 14) * 2000; } else if (d <= 21) { co2 = 7000 - (d - 18) * 2000; }
  else { co2 = (phaseKey(d) === 'flush') ? 1450 : 1050; }
  if (co2 < 800) { co2 = 800; }

  return { compost: compost, room: room, rh: rh, co2: co2 };
}

function yieldOf(d, scale) {
  var b = YIELD[d] || 0;
  return b ? Math.round(b * scale) : 0;
}

function cycleTotal(scale) {
  var s = 0;
  for (var k in YIELD) { s += YIELD[k]; }
  return Math.round(s * scale);
}

function harvestedSoFar(day, scale) {
  var s = 0;
  for (var k in YIELD) { if (Number(k) <= day) { s += YIELD[k]; } }
  return Math.round(s * scale);
}

// مولد شبه‌تصادفیِ بذردار. دمو باید عددهای ثابتی داشته باشد، وگرنه:
// ۱) خروجی ساخت در هر بار اجرا فرق می‌کند و مخزن بی‌دلیل کثیف می‌شود،
// ۲) پیش‌رندر و مرورگر دو دنیای متفاوت می‌سازند و صفحه موقع بارگذاری می‌پرد.
var SEED0 = 20261010;
var _seed = SEED0;
var _firstBuild = true;
function rnd() {
  _seed = (_seed * 1664525 + 1013904223) % 4294967296;
  return _seed / 4294967296;
}

function jitter(v, a) { return v + (rnd() * 2 - 1) * a; }
function r1(v) { return Math.round(v * 10) / 10; }

class Component extends DCLogic {
  constructor(props) {
    super(props);
    var days = [9, 30, 20];
    this.state = {
      days: days, active: 1, tick: 0,
      price: DEFAULTS.price, compostCost: DEFAULTS.compostCost,
      pickCost: DEFAULTS.pickCost, fixedCost: DEFAULTS.fixedCost,
      sim: this.build(days)
    };
  }

  fa(str) {
    var map = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹' };
    return String(str).replace(/[0-9]/g, function (d) { return map[d]; });
  }
  num(n) { return Number(n).toLocaleString('fa-IR'); }
  mt(n) { return this.num(Math.round(n / 100000) / 10); }

  build(days) {
    // فقط اولین دنیا بذر ثابت دارد تا پیش‌رندر و مرورگر یکی باشند؛
    // «نمونهٔ تازه» و جلو بردن روز باید واقعاً عددهای تازه بدهند.
    if (_firstBuild) { _seed = SEED0; _firstBuild = false; }
    var self = this;
    var rooms = days.map(function (day, i) {
      var cfg = ROOMS[i];
      var key = phaseKey(day);
      var rng = PHASES[key];
      var env = [];
      for (var k = 13; k >= 0; k--) {
        var d = day - k;
        if (d < 0) { d = 0; }
        var c = centers(d);
        env.push({
          compost: r1(jitter(c.compost, 0.3)), room: r1(jitter(c.room, 0.3)),
          rh: r1(jitter(c.rh, 1)), co2: Math.round(jitter(c.co2, c.co2 * 0.07))
        });
      }
      var today = env[13];
      if (rnd() < 0.3) {
        var pick = ['compost', 'room', 'rh', 'co2'][Math.floor(rnd() * 4)];
        var band = rng[pick];
        var span = band[1] - band[0];
        var below = rnd() < 0.5;
        var v = below ? band[0] - span * (0.08 + rnd() * 0.2) : band[1] + span * (0.08 + rnd() * 0.2);
        today[pick] = pick === 'co2' ? Math.round(v) : r1(v);
        env[13] = today;
      }
      var gradeA = Math.round(60 + rnd() * 24);
      var restPct = 100 - gradeA;
      var gradeC = Math.round(restPct * (0.12 + rnd() * 0.2));
      var gradeB = restPct - gradeC;

      return {
        name: cfg.name, color: cfg.color, soft: cfg.soft, scale: cfg.scale,
        compostKg: Math.round(COMPOST_PER_ROOM * cfg.scale),
        day: day, phaseKey: key, phase: rng.label, env: env, today: today,
        produced: yieldOf(day, cfg.scale),
        gradeA: gradeA, gradeB: gradeB, gradeC: gradeC,
        prevTotal: Math.round(cycleTotal(cfg.scale) * (0.86 + rnd() * 0.26))
      };
    });

    var bars = [];
    for (var k2 = 6; k2 >= 0; k2--) {
      var segs = rooms.map(function (r) {
        var d = r.day - k2;
        if (d < 0) { d += 42; }
        return yieldOf(d, r.scale);
      });
      bars.push({ offset: k2, segs: segs, total: segs[0] + segs[1] + segs[2] });
    }

    var forecast = [];
    for (var k3 = 1; k3 <= 14; k3++) {
      var t = 0;
      rooms.forEach(function (r) { t += yieldOf((r.day + k3) % 42, r.scale); });
      forecast.push(t);
    }

    var names = ['میدان مرکزی — غرفه ۱۲', 'هایپر شهر', 'صنایع غذایی آریان', 'رستوران‌های زنجیره‌ای پیوند'];
    var offsets = [2, 5, 9, 13];
    var commitments = offsets.map(function (o, i) {
      return { inDays: o, customer: names[i], kg: Math.round((150 + rnd() * 190) / 10) * 10 };
    });

    var receivables = names.map(function (n, i) {
      return {
        name: n,
        amount: Math.round((8 + rnd() * 34) * 10) / 10,
        days: Math.round(2 + rnd() * 36)
      };
    });

    return {
      rooms: rooms, bars: bars, forecast: forecast, commitments: commitments,
      receivables: receivables, logs: this.buildLogs(rooms),
      kwhPerKg: r1(2.0 + rnd() * 1.2),
      wastePct: r1(3 + rnd() * 6),
      cashBalance: Math.round((60 + rnd() * 120) * 10) / 10
    };
  }

  buildLogs(rooms) {
    var self = this;
    var T = {
      visit: { type: 'بازدید سالن', bg: '#F4E3D3', color: '#8A5410' },
      harvest: { type: 'برداشت', bg: '#E3EEE1', color: '#166534' },
      water: { type: 'آبیاری', bg: '#DCEBFA', color: '#0E6FB4' },
      disease: { type: 'مشاهده بیماری', bg: '#F5E1DF', color: '#A32222' },
      sale: { type: 'فروش', bg: '#F5E9D6', color: '#8A5410' },
      compost: { type: 'کمپوست', bg: '#EBE3F5', color: '#5B3F92' }
    };
    var out = [];
    rooms.forEach(function (r) {
      out.push({ t: T.visit, room: r.name, text: 'دمای کمپوست ' + self.num(r.today.compost) + ' °C · رطوبت ' + self.num(r.today.rh) + '٪ · CO₂ ' + self.num(r.today.co2) + ' ppm' });
      if (r.produced > 0) {
        out.push({ t: T.harvest, room: r.name, text: 'قارچ دکمه‌ای ' + self.num(r.produced) + ' کیلو · Flush ' + self.fa(r.day < 28 ? 1 : (r.day < 35 ? 2 : 3)) + ' · ' + (rnd() < 0.7 ? 'درجه یک' : 'درجه دو') });
      }
      if (r.phaseKey === 'casing' || r.phaseKey === 'flush') {
        out.push({ t: T.water, room: r.name, text: self.num(80 + Math.round(rnd() * 90)) + ' لیتر آبیاری سطحی' });
      }
      if (r.phaseKey === 'spawn' && r.day < 2) {
        out.push({ t: T.compost, room: r.name, text: 'ورود ' + self.num(r.compostKg) + ' کیلو کمپوست · Batch ' + self.fa('A-' + (100 + Math.floor(rnd() * 90))) });
      }
    });
    if (rnd() < 0.5) {
      var rr = rooms[Math.floor(rnd() * 3)];
      out.push({ t: T.disease, room: rr.name, text: 'لکه‌های قهوه‌ای پراکنده · شدت ' + (rnd() < 0.6 ? 'کم' : 'متوسط') });
    }
    var sold = rooms.reduce(function (s, r) { return s + r.produced; }, 0);
    if (sold > 0) {
      out.push({ t: T.sale, room: '—', text: self.num(sold) + ' کیلو قارچ دکمه‌ای به میدان مرکزی' });
    }
    var hours = [];
    for (var i = 0; i < out.length; i++) { hours.push(6 + Math.floor(rnd() * 13)); }
    hours.sort(function (a, b) { return b - a; });
    return out.map(function (o, i) {
      var mm = Math.floor(rnd() * 6) * 10;
      return {
        type: o.t.type, bg: o.t.bg, color: o.t.color, room: o.room, text: o.text,
        time: self.fa((hours[i] < 10 ? '0' : '') + hours[i] + ':' + (mm < 10 ? '0' : '') + mm)
      };
    });
  }

  params() {
    return {
      price: parseFloat(this.state.price) || 0,
      compostCost: parseFloat(this.state.compostCost) || 0,
      pickCost: parseFloat(this.state.pickCost) || 0,
      fixedCost: parseFloat(this.state.fixedCost) || 0
    };
  }

  econ(room, P) {
    var expected = cycleTotal(room.scale);
    var soFar = harvestedSoFar(room.day, room.scale);
    var casingKg = Math.round(room.compostKg * 0.15);
    var fixedPart = room.compostKg * P.compostCost + casingKg * CASING_COST + P.fixedCost;
    var labor = expected * P.pickCost;
    var cost = fixedPart + labor;
    // قیمت مؤثر: درجه دو ۷۲٪ و ریز ۴۵٪ قیمت درجه یک به فروش می‌رود
    var effPrice = P.price * (room.gradeA + 0.72 * room.gradeB + 0.45 * room.gradeC) / 100;
    var revenue = expected * effPrice;
    return {
      expected: expected, soFar: soFar, compostKg: room.compostKg, casingKg: casingKg,
      compostCost: room.compostKg * P.compostCost, casingCost: casingKg * CASING_COST,
      labor: labor, fixedPart: fixedPart, cost: cost, revenue: revenue, effPrice: effPrice,
      profit: revenue - cost,
      costPerKg: expected > 0 ? cost / expected : 0,
      margin: revenue > 0 ? ((revenue - cost) / revenue) * 100 : 0,
      be: (expected / room.compostKg) * 100,
      beKg: (effPrice - P.pickCost) > 0 ? fixedPart / (effPrice - P.pickCost) : 0
    };
  }

  nextDay() {
    var days = this.state.days.map(function (d) { return (d + 1) % 42; });
    this.setState({ days: days, tick: this.state.tick + 1, sim: this.build(days) });
  }
  week() {
    var days = this.state.days.map(function (d) { return (d + 7) % 42; });
    this.setState({ days: days, tick: this.state.tick + 7, sim: this.build(days) });
  }
  reshuffle() { this.setState({ sim: this.build(this.state.days) }); }
  reset() {
    var days = [9, 30, 20];
    this.setState({
      days: days, active: 1, tick: 0,
      price: DEFAULTS.price, compostCost: DEFAULTS.compostCost,
      pickCost: DEFAULTS.pickCost, fixedCost: DEFAULTS.fixedCost,
      sim: this.build(days)
    });
  }
  set(key) {
    var self = this;
    return function (e) {
      var p = {};
      p[key] = e.target.value;
      self.setState(p);
    };
  }

  spark(values, min, max, band, color) {
    var pts = [];
    for (var i = 0; i < values.length; i++) {
      var x = 8 + i * (264 / (values.length - 1));
      var v = values[i];
      if (v < min) { v = min; }
      if (v > max) { v = max; }
      pts.push(x.toFixed(1) + ',' + (64 - ((v - min) / (max - min)) * 54).toFixed(1));
    }
    var yTop = 64 - ((Math.min(band[1], max) - min) / (max - min)) * 54;
    var yBot = 64 - ((Math.max(band[0], min) - min) / (max - min)) * 54;
    return { pts: pts.join(' '), bandY: yTop.toFixed(1), bandH: Math.max(2, yBot - yTop).toFixed(1) };
  }

  metricOf(label, unit, values, current, min, max, band, color, soft) {
    var s = this.spark(values, min, max, band, color);
    var ok = current >= band[0] && current <= band[1];
    return {
      label: label, unit: unit, value: this.num(current), pts: s.pts, bandY: s.bandY, bandH: s.bandH,
      color: color, soft: soft,
      chip: (ok ? 'در بازه · ' : 'خارج از بازه · ') + this.num(band[0]) + ' تا ' + this.num(band[1]),
      chipBg: ok ? '#E3EEE1' : '#F5E9D6', chipColor: ok ? '#166534' : '#8A5410'
    };
  }

  signed(v, unit) {
    var n = Math.round(v);
    if (n === 0) { n = 0; }
    return (n > 0 ? '+' : '') + this.num(n) + (unit ? ' ' + unit : '');
  }

  kpi(label, value, target, ok, delta) {
    return {
      label: label, value: value, target: target, delta: delta,
      bg: ok ? '#E3EEE1' : '#F5E9D6', color: ok ? '#166534' : '#8A5410'
    };
  }

  renderVals() {
    var self = this;
    var sim = this.state.sim;
    var rooms = sim.rooms;
    var P = this.params();
    var active = rooms[this.state.active];
    var rng = PHASES[active.phaseKey];

    var metricDefs = [
      { key: 'compost', label: 'دمای کمپوست', unit: '°C' },
      { key: 'room', label: 'دمای سالن', unit: '°C' },
      { key: 'rh', label: 'رطوبت RH', unit: '٪' },
      { key: 'co2', label: 'CO₂', unit: 'ppm' }
    ];

    // ---- اقتصاد ----
    var econs = rooms.map(function (r) { return self.econ(r, P); });
    var econRows = rooms.map(function (r, i) {
      var e = econs[i];
      return {
        name: r.name, color: r.color, phase: r.phase, day: self.num(r.day),
        compost: self.num(e.compostKg), soFar: self.num(e.soFar), expected: self.num(e.expected),
        be: self.num(Math.round(e.be)), beColor: e.be >= 28 ? '#166534' : '#8A5410',
        costPerKg: self.num(Math.round(e.costPerKg / 1000) * 1000),
        profit: self.mt(e.profit), margin: self.num(Math.round(e.margin)),
        profitColor: e.profit > 0 ? '#166534' : '#A32222'
      };
    });

    var sum = function (f) { return econs.reduce(function (s, e) { return s + f(e); }, 0); };
    var tCost = sum(function (e) { return e.cost; });
    var tRev = sum(function (e) { return e.revenue; });
    var tExpected = sum(function (e) { return e.expected; });
    var tCompost = sum(function (e) { return e.compostKg; });
    var tProfit = tRev - tCost;
    var tMargin = tRev > 0 ? (tProfit / tRev) * 100 : 0;
    var tCostPerKg = tExpected > 0 ? tCost / tExpected : 0;
    var tBe = tCompost > 0 ? (tExpected / tCompost) * 100 : 0;

    var total = {
      compost: this.num(tCompost), soFar: this.num(sum(function (e) { return e.soFar; })),
      expected: this.num(tExpected), be: this.num(Math.round(tBe)),
      costPerKg: this.num(Math.round(tCostPerKg / 1000) * 1000),
      profit: this.mt(tProfit), margin: this.num(Math.round(tMargin)),
      profitColor: tProfit > 0 ? '#166534' : '#A32222'
    };

    var e1 = econs[1];
    var safety = e1.beKg > 0 ? Math.round(((e1.expected - e1.beKg) / e1.beKg) * 100) : 0;
    var breakEven = {
      kg: this.num(Math.round(e1.beKg)), expected: this.num(e1.expected),
      safety: this.num(safety)
    };

    var mixTotal = sum(function (e) { return e.cost; }) || 1;
    var costMix = {
      compostPct: Math.round((sum(function (e) { return e.compostCost; }) / mixTotal) * 100),
      casingPct: Math.round((sum(function (e) { return e.casingCost; }) / mixTotal) * 100),
      laborPct: Math.round((sum(function (e) { return e.labor; }) / mixTotal) * 100),
      fixedPct: Math.round((P.fixedCost * 3 / mixTotal) * 100)
    };

    var lowRev = tRev * 0.9;
    var lowMargin = lowRev > 0 ? ((lowRev - tCost) / lowRev) * 100 : 0;
    var sensitivity = {
      margin: this.num(Math.round(lowMargin)),
      color: lowMargin > 20 ? '#166534' : (lowMargin > 0 ? '#8A5410' : '#A32222')
    };

    // ---- ترکیب گرید و قیمت مؤثر ----
    var gradeRows = rooms.map(function (r, i) {
      var e = econs[i];
      var disc = P.price > 0 ? (1 - e.effPrice / P.price) * 100 : 0;
      var healthy = r.gradeA >= 70;
      return {
        name: r.name, color: r.color,
        a: r.gradeA, b: r.gradeB, c: r.gradeC,
        aLabel: self.num(r.gradeA) + '٪', bLabel: self.num(r.gradeB) + '٪', cLabel: self.num(r.gradeC) + '٪',
        effPrice: self.num(Math.round(e.effPrice / 1000) * 1000),
        discount: self.num(Math.round(disc)),
        chip: healthy ? 'ترکیب سالم' : 'سهم درجه یک پایین',
        chipBg: healthy ? '#E3EEE1' : '#F5E9D6',
        chipColor: healthy ? '#166534' : '#8A5410'
      };
    });

    // ---- مقایسه با سیکل قبل ----
    var cycleCompare = rooms.map(function (r, i) {
      var cur = econs[i].expected;
      var prev = r.prevTotal;
      var d = prev > 0 ? ((cur - prev) / prev) * 100 : 0;
      var maxv = Math.max(cur, prev) || 1;
      var up = d >= 0;
      return {
        name: r.name, color: r.color, delta: d,
        prev: self.num(prev), cur: self.num(cur),
        prevW: Math.round((prev / maxv) * 100), curW: Math.round((cur / maxv) * 100),
        deltaLabel: self.signed(d, '') + '٪',
        deltaColor: up ? '#166534' : '#A32222',
        deltaBg: up ? '#E3EEE1' : '#F5E1DF',
        note: up ? 'هم‌تراز یا بهتر از سیکل قبل' : 'افت نسبت به سیکل قبل همین سالن'
      };
    });

    // ---- پیش‌بینی و تعهدها ----
    var maxF = 1;
    sim.forecast.forEach(function (v) { if (v > maxF) { maxF = v; } });
    var commitDays = {};
    sim.commitments.forEach(function (c) { commitDays[c.inDays] = true; });
    var forecast = sim.forecast.map(function (v, i) {
      var d = i + 1;
      return {
        day: '+' + self.fa(d), label: v > 0 ? self.num(v) : '—',
        h: Math.max(2, Math.round((v / maxF) * 74)),
        color: v > 0 ? '#166534' : '#D9D5C9',
        mark: commitDays[d] ? '▾' : ''
      };
    });

    var cum = [];
    var run = 0;
    for (var i2 = 0; i2 < sim.forecast.length; i2++) { run += sim.forecast[i2]; cum.push(run); }
    var commitRun = 0;
    var firstGap = null;
    var commitments = sim.commitments.map(function (c) {
      commitRun += c.kg;
      var avail = cum[c.inDays - 1] || 0;
      var covered = avail >= commitRun;
      if (!covered && firstGap === null) { firstGap = { c: c, gap: Math.round(commitRun - avail) }; }
      return {
        when: 'تا ' + self.fa(c.inDays) + ' روز دیگر', customer: c.customer,
        kg: self.num(c.kg), cumForecast: self.num(avail),
        status: covered ? 'پوشش داده می‌شود' : 'کسری',
        bg: covered ? '#E3EEE1' : '#F5E1DF', color: covered ? '#166534' : '#A32222'
      };
    });

    // ---- برنامهٔ نیروی کار ----
    var laborDays = [];
    for (var li = 0; li < 7; li++) {
      var lkg = sim.forecast[li];
      laborDays.push({
        day: '+' + self.fa(li + 1),
        kg: lkg > 0 ? self.num(lkg) : '—',
        hours: lkg > 0 ? self.num(Math.round((lkg / 20) * 10) / 10) : '—',
        workers: lkg > 0 ? self.num(Math.ceil(lkg / 100)) : '—',
        bg: lkg > 400 ? '#F5E9D6' : '#FFFFFF'
      });
    }
    var next7 = sim.forecast.slice(0, 7);
    var peakKg = Math.max.apply(null, next7);
    var peakIdx = next7.indexOf(peakKg);
    var peakWorkers = Math.ceil(peakKg / 100);
    var weekHours = Math.round(next7.reduce(function (s, v) { return s + v; }, 0) / 20);

    var week7 = cum[6] || 0;
    var commit7 = sim.commitments.reduce(function (s, c) { return s + (c.inDays <= 7 ? c.kg : 0); }, 0);
    var gap7 = commit7 - week7;
    var coverage = gap7 > 0
      ? { title: 'کسری ' + this.num(Math.round(gap7)) + ' کیلویی در هفت روز آینده',
          detail: 'تعهد ثبت‌شده ' + this.num(commit7) + ' کیلو در برابر پیش‌بینی برداشت ' + this.num(week7) + ' کیلو. یا تحویل یکی از سفارش‌ها را جابه‌جا کن، یا فروش آزاد این هفته را متوقف کن.',
          bg: '#F5E1DF', color: '#A32222' }
      : { title: 'تعهدهای هفت روز آینده پوشش داده می‌شوند',
          detail: 'پیش‌بینی برداشت ' + this.num(week7) + ' کیلو در برابر تعهد ' + this.num(commit7) + ' کیلو — مازاد ' + this.num(Math.round(-gap7)) + ' کیلو برای فروش آزاد.',
          bg: '#E3EEE1', color: '#166534' };

    // ---- برنامهٔ سالن‌ها ----
    var gantt = rooms.map(function (r) {
      var segs = [];
      var last = null;
      for (var k = 0; k < 45; k++) {
        var key = phaseKey((r.day + k) % 42);
        if (last && last.key === key) { last.len++; }
        else { last = { key: key, len: 1 }; segs.push(last); }
      }
      return {
        name: r.name,
        segs: segs.map(function (s) {
          return { w: Math.round((s.len / 45) * 1000) / 10, bg: PHASES[s.key].bg };
        })
      };
    });

    var idleDays = 0;
    rooms.forEach(function (r) {
      for (var k = 0; k < 30; k++) { if (phaseKey((r.day + k) % 42) === 'cleanout') { idleDays++; } }
    });

    // ---- هشدارها و تصمیم‌ها ----
    var alerts = [];
    metricDefs.forEach(function (d) {
      var v = active.today[d.key];
      var band = rng[d.key];
      if (v < band[0] || v > band[1]) {
        var span = band[1] - band[0];
        var dist = v < band[0] ? band[0] - v : v - band[1];
        var hard = dist > span * 0.15;
        alerts.push({
          severity: hard ? 'شدید' : 'متوسط',
          bg: hard ? '#F5E1DF' : '#F5E9D6', pillBg: hard ? '#EDCECB' : '#EBDBC0',
          color: hard ? '#A32222' : '#8A5410',
          title: d.label + ' ' + (v < band[0] ? 'پایین‌تر از بازه' : 'بالاتر از بازه'),
          detail: 'ثبت‌شده ' + self.num(v) + ' ' + d.unit + ' · بازهٔ مرجع ' + self.num(band[0]) + ' تا ' + self.num(band[1]) + ' در مرحلهٔ ' + rng.label
        });
      }
    });

    var decisions = [];
    var SEV = {
      crit: { severity: 'فوری', color: '#A32222', pillBg: '#EDCECB' },
      warn: { severity: 'این هفته', color: '#8A5410', pillBg: '#EBDBC0' },
      ok: { severity: 'پایش', color: '#166534', pillBg: '#CFE3CC' }
    };

    if (gap7 > 0) {
      decisions.push({
        severity: SEV.crit.severity, color: SEV.crit.color, pillBg: SEV.crit.pillBg,
        title: 'کسری ' + this.num(Math.round(gap7)) + ' کیلو در برابر تعهد فروش',
        detail: 'تعهد هفت روز آینده ' + this.num(commit7) + ' کیلو است و پیش‌بینی برداشت ' + this.num(week7) + ' کیلو.',
        action: 'تحویل ' + (firstGap ? firstGap.c.customer : 'یکی از سفارش‌ها') + ' را جابه‌جا کن یا فروش آزاد را ببند.'
      });
    }

    rooms.forEach(function (r) {
      if (r.day >= 36) {
        decisions.push({
          severity: SEV.crit.severity, color: SEV.crit.color, pillBg: SEV.crit.pillBg,
          title: 'سفارش کمپوست ' + r.name,
          detail: r.name + ' در روز ' + self.num(r.day) + ' است و تا ' + self.num(42 - r.day) + ' روز دیگر تخلیه می‌شود.',
          action: 'ثبت خرید ' + self.num(r.compostKg) + ' کیلو کمپوست برای پرکردن بعدی.'
        });
      }
    });

    rooms.forEach(function (r, i) {
      var rr = PHASES[r.phaseKey];
      metricDefs.forEach(function (d) {
        var v = r.today[d.key];
        var band = rr[d.key];
        var span = band[1] - band[0];
        var dist = v < band[0] ? band[0] - v : (v > band[1] ? v - band[1] : 0);
        if (dist > span * 0.15) {
          decisions.push({
            severity: SEV.crit.severity, color: SEV.crit.color, pillBg: SEV.crit.pillBg,
            title: 'انحراف شدید ' + d.label + ' در ' + r.name,
            detail: self.num(v) + ' ' + d.unit + ' در برابر بازهٔ ' + self.num(band[0]) + ' تا ' + self.num(band[1]) + ' مرحلهٔ ' + rr.label + '.',
            action: 'اصلاح امروز و ثبت اقدام؛ اثرش دو هفتهٔ دیگر روی برداشت دیده می‌شود.'
          });
        }
      });
      if (econs[i].margin < 25) {
        decisions.push({
          severity: SEV.warn.severity, color: SEV.warn.color, pillBg: SEV.warn.pillBg,
          title: 'حاشیهٔ سود ' + r.name + ' باریک شده',
          detail: 'حاشیهٔ این سیکل ' + self.num(Math.round(econs[i].margin)) + '٪ و بهای تمام‌شده ' + self.num(Math.round(econs[i].costPerKg / 1000) * 1000) + ' تومان بر کیلو است.',
          action: 'قیمت کمپوست را مذاکره کن یا قیمت فروش را بازبینی کن.'
        });
      }
    });

    cycleCompare.forEach(function (cc) {
      if (cc.delta < -5) {
        decisions.push({
          severity: SEV.warn.severity, color: SEV.warn.color, pillBg: SEV.warn.pillBg,
          title: 'افت ' + cc.deltaLabel + ' در ' + cc.name + ' نسبت به سیکل قبل',
          detail: 'برآورد این سیکل ' + cc.cur + ' کیلو در برابر ' + cc.prev + ' کیلو سیکل قبلِ همین سالن.',
          action: 'کیفیت کمپوست این Batch و تاریخچهٔ محیطی روزهای اسپان‌ران را با سیکل قبل مقایسه کن.'
        });
      }
    });

    rooms.forEach(function (r, i) {
      if (r.gradeA < 65) {
        decisions.push({
          severity: SEV.warn.severity, color: SEV.warn.color, pillBg: SEV.warn.pillBg,
          title: 'سهم درجه یک ' + r.name + ' فقط ' + self.num(r.gradeA) + '٪ است',
          detail: 'قیمت مؤثر این سالن ' + self.num(Math.round(econs[i].effPrice / 1000) * 1000) + ' تومان بر کیلو شده، نه قیمت درجه یک.',
          action: 'فاصلهٔ چیدن را کوتاه‌تر کن؛ قارچ دیر چیده‌شده به درجه دو می‌افتد.'
        });
      }
    });

    if (peakWorkers > 4) {
      decisions.push({
        severity: SEV.warn.severity, color: SEV.warn.color, pillBg: SEV.warn.pillBg,
        title: 'اوج برداشت ' + this.num(peakKg) + ' کیلو در روز +' + this.fa(peakIdx + 1),
        detail: 'آن روز حدود ' + this.num(peakWorkers) + ' نفر کارگر برداشت لازم است؛ روزهای دیگر هفته کمتر.',
        action: 'نیروی روزمزد را از الان برای همان روز هماهنگ کن.'
      });
    }

    if (sim.wastePct > 7) {
      decisions.push({
        severity: SEV.warn.severity, color: SEV.warn.color, pillBg: SEV.warn.pillBg,
        title: 'ضایعات ' + this.num(sim.wastePct) + '٪ — بالاتر از هدف ۵٪',
        detail: 'هر یک درصد ضایعات روی کل مزرعه حدود ' + this.mt(tExpected * 0.01 * P.price) + ' میلیون تومان در سیکل است.',
        action: 'زمان‌بندی چیدن و آموزش کارگر برداشت را بازبینی کن.'
      });
    }

    var overdue = sim.receivables.filter(function (r) { return r.days > 21; });
    if (overdue.length > 0) {
      var od = overdue.reduce(function (s, r) { return s + r.amount; }, 0);
      decisions.push({
        severity: SEV.warn.severity, color: SEV.warn.color, pillBg: SEV.warn.pillBg,
        title: 'وصول ' + this.num(Math.round(od * 10) / 10) + ' میلیون تومان مطالبات معوق',
        detail: overdue.length + ' مشتری بیش از ۲۱ روز از تحویل گذشته‌اند و هنوز تسویه نکرده‌اند.',
        action: 'پیش از سفارش کمپوست بعدی، تسویه را پیگیری کن.'
      });
    }

    if (idleDays > 6) {
      decisions.push({
        severity: SEV.warn.severity, color: SEV.warn.color, pillBg: SEV.warn.pillBg,
        title: this.num(idleDays) + ' روز سالن خالی در ۳۰ روز آینده',
        detail: 'سربار ثابت در روزهای خالی هم پرداخت می‌شود.',
        action: 'برنامهٔ پرکردن را جلو بینداز تا فاصلهٔ سیکل‌ها کوتاه‌تر شود.'
      });
    }

    if (decisions.length === 0) {
      decisions.push({
        severity: SEV.ok.severity, color: SEV.ok.color, pillBg: SEV.ok.pillBg,
        title: 'امروز تصمیم فوری‌ای لازم نیست',
        detail: 'محیط هر سه سالن در بازهٔ مرحله است، تعهدها پوشش داده می‌شوند و مطالبات معوق نداری.',
        action: 'ادامهٔ پایش روزانه.'
      });
    }

    // ---- شاخص‌ها ----
    var kpis = [
      this.kpi('بازده بیولوژیک', this.num(Math.round(tBe)) + '٪', '۲۸٪ یا بالاتر', tBe >= 28,
        this.signed(tBe - 28, 'واحد')),
      this.kpi('بهای تمام‌شدهٔ هر کیلو', this.num(Math.round(tCostPerKg / 1000) * 1000), 'زیر ۱۱۰٬۰۰۰ تومان', tCostPerKg <= 110000,
        tCostPerKg <= 110000 ? 'زیر هدف' : 'بالای هدف'),
      this.kpi('حاشیهٔ سود', this.num(Math.round(tMargin)) + '٪', '۳۵٪ یا بالاتر', tMargin >= 35,
        this.signed(tMargin - 35, 'واحد')),
      this.kpi('سهم ضایعات', this.num(sim.wastePct) + '٪', 'زیر ۵٪', sim.wastePct <= 5,
        sim.wastePct <= 5 ? 'زیر هدف' : 'بالای هدف'),
      this.kpi('روز خالی سالن (۳۰ روز)', this.num(idleDays) + ' روز', 'زیر ۶ روز', idleDays <= 6,
        idleDays <= 6 ? 'زیر هدف' : 'بالای هدف'),
      this.kpi('برق هر کیلو', this.num(sim.kwhPerKg) + ' kWh', 'زیر ۲٫۵ kWh', sim.kwhPerKg <= 2.5,
        sim.kwhPerKg <= 2.5 ? 'زیر هدف' : 'بالای هدف')
    ];

    // ---- نقدینگی ----
    var recTotal = sim.receivables.reduce(function (s, r) { return s + r.amount; }, 0);
    var upcoming = Math.round((tCompost * P.compostCost / 3 + P.fixedCost) / 100000) / 10;
    var netCash = Math.round((sim.cashBalance + recTotal - upcoming) * 10) / 10;
    var cash = {
      balance: this.num(sim.cashBalance), receivable: this.num(Math.round(recTotal * 10) / 10),
      upcoming: this.num(upcoming), net: this.num(netCash),
      netColor: netCash > 0 ? '#166534' : '#A32222'
    };

    var receivables = sim.receivables.map(function (r) {
      var late = r.days > 21;
      var mid = r.days > 10 && r.days <= 21;
      return {
        name: r.name, amount: self.num(r.amount), days: self.num(r.days),
        status: late ? 'معوق' : (mid ? 'نزدیک سررسید' : 'جاری'),
        bg: late ? '#F5E1DF' : (mid ? '#F5E9D6' : '#E3EEE1'),
        color: late ? '#A32222' : (mid ? '#8A5410' : '#166534')
      };
    });

    // ---- نوارهای گذشته و سالن فعال ----
    var maxTotal = 1;
    sim.bars.forEach(function (b) { if (b.total > maxTotal) { maxTotal = b.total; } });
    var bars = sim.bars.map(function (b) {
      var t = b.total || 1;
      return {
        label: b.offset === 0 ? 'امروز' : self.fa(b.offset) + ' روز',
        total: b.total > 0 ? self.num(b.total) : '—',
        h: Math.max(2, Math.round((b.total / maxTotal) * 76)),
        s1: Math.round((b.segs[0] / t) * 100),
        s2: Math.round((b.segs[1] / t) * 100),
        s3: Math.round((b.segs[2] / t) * 100)
      };
    });

    var tabs = rooms.map(function (r, i) {
      var on = i === self.state.active;
      return {
        name: r.name, phase: r.phase, day: self.num(r.day), color: r.color, soft: r.soft,
        bg: on ? r.soft : '#FFFFFF', border: on ? r.color : '#E4E1D6',
        yieldLabel: r.produced > 0 ? ('برداشت امروز ' + self.num(r.produced) + ' کیلو') : 'امروز برداشتی ندارد',
        pick: function () { self.setState({ active: i }); }
      };
    });

    var env = active.env;
    var metrics = [
      this.metricOf('دمای کمپوست', '°C', env.map(function (e) { return e.compost; }), active.today.compost, 14, 30, rng.compost, '#B4530E', '#F4E3D3'),
      this.metricOf('دمای سالن', '°C', env.map(function (e) { return e.room; }), active.today.room, 14, 30, rng.room, '#0E6FB4', '#DCEBFA'),
      this.metricOf('رطوبت RH', '٪', env.map(function (e) { return e.rh; }), active.today.rh, 80, 100, rng.rh, '#2A6F51', '#E3EEE1'),
      this.metricOf('دی‌اکسید کربن', 'ppm', env.map(function (e) { return e.co2; }), active.today.co2, 0, 20000, rng.co2, '#5B3F92', '#EBE3F5')
    ];

    return {
      tick: this.num(this.state.tick),
      nextDay: function () { self.nextDay(); },
      week: function () { self.week(); },
      reshuffle: function () { self.reshuffle(); },
      reset: function () { self.reset(); },
      f: this.state,
      h: {
        price: this.set('price'), compostCost: this.set('compostCost'),
        pickCost: this.set('pickCost'), fixedCost: this.set('fixedCost')
      },
      decisions: decisions, kpis: kpis, econRows: econRows, total: total,
      breakEven: breakEven, costMix: costMix, sensitivity: sensitivity,
      gradeRows: gradeRows, cycleCompare: cycleCompare,
      labor: {
        days: laborDays,
        weekHours: this.num(weekHours),
        peakKg: this.num(peakKg),
        peakDay: '+' + this.fa(peakIdx + 1),
        peakWorkers: this.num(peakWorkers)
      },
      forecast: forecast, commitments: commitments, coverage: coverage, gantt: gantt,
      bars: bars, tabs: tabs, metrics: metrics, logs: sim.logs,
      cash: cash, receivables: receivables,
      room: {
        name: active.name, color: active.color, soft: active.soft, phase: active.phase,
        day: this.num(active.day), remain: this.num(42 - active.day),
        dayPct: Math.round((active.day / 42) * 100),
        alerts: alerts, noAlerts: alerts.length === 0
      }
    };
  }
}
dcMount(["\n","\n\n",{"n":"div","k":["\n\n  ","\n  ",{"n":"header","k":["\n    ",{"n":"div","k":["\n      ",{"n":"a","a":{"href":"dorrin.html"},"k":["← مطالعهٔ موردی دُرّین"],"c":"ce"},"\n      ",{"n":"nav","k":["\n        ",{"n":"a","a":{"href":"#decisions"},"k":["تصمیم‌ها"],"c":"c4z"},"\n        ",{"n":"a","a":{"href":"#economics"},"k":["اقتصاد"],"c":"c4z"},"\n        ",{"n":"a","a":{"href":"#plan"},"k":["برنامه"],"c":"c4z"},"\n        ",{"n":"a","a":{"href":"#ops"},"k":["عملیات"],"c":"c4z"},"\n        ",{"n":"a","a":{"href":"#cash"},"k":["نقدینگی"],"c":"c4z"},"\n        ",{"n":"a","a":{"href":"./#gallery"},"k":["کارها"],"c":"c4z"},"\n      "],"c":"c8s"},"\n    "],"a":{"style":"max-width: 1180px;margin: 0 auto;padding: 14px 24px;display: flex;align-items: center;gap: 16px;flex-wrap: wrap"}},"\n  "],"c":"cyn"},"\n\n  ",{"n":"main","k":["\n\n    ","\n    ",{"n":"span","k":["Sandbox · همهٔ عددها شبیه‌سازی‌شده‌اند"],"c":"cyo"},"\n    ",{"n":"h1","k":["پل فرماندهی کارخانهٔ قارچ دکمه‌ای"],"a":{"style":"font-size: clamp(26px, 3.6vw, 38px);font-weight: 800;line-height: 1.45;margin: 0 0 14px"}},"\n    ",{"n":"p","k":["این صفحه از نگاه کسی ساخته شده که باید ",{"n":"b","k":["تصمیم بگیرد"]},"، نه کسی که فقط گزارش می‌خواند: سه سالن تولید قارچ دکمه‌ای، هر کدام در نقطهٔ متفاوتی از سیکل ۴۲ روزه، با اقتصاد هر سیکل، تعهدهای فروش، برنامهٔ پرکردن سالن‌ها و وضعیت نقدینگی — همه روی یک صفحه."],"a":{"style":"font-size: 16px;line-height: 2;color: #45494F;max-width: 68ch;margin: 0 0 12px"}},"\n    ",{"n":"p","k":[{"n":"b","k":["«روز بعد»"]}," را بزن تا مزرعه جلو برود؛ در بخش «اقتصاد» هم می‌توانی قیمت فروش و بهای کمپوست را عوض کنی و همان لحظه ببینی حاشیهٔ سود و نقطهٔ سربه‌سر کجا می‌رود."],"c":"cy3"},"\n\n    ","\n    ",{"n":"div","k":["\n      ",{"n":"button","e":{"click":"nextDay"},"k":["روز بعد ←"],"a":{"style":"font-size: 14px;font-weight: 700;color: #FFFFFF;background: #B4530E;padding: 12px 24px;border-radius: 10px"}},"\n      ",{"n":"button","e":{"click":"week"},"k":["یک هفته جلو"],"c":"cz3"},"\n      ",{"n":"button","e":{"click":"reshuffle"},"k":["داده تصادفی جدید"],"c":"cz3"},"\n      ",{"n":"button","e":{"click":"reset"},"k":["بازنشانی"],"a":{"style":"font-size: 13.5px;font-weight: 600;color: #666158;background: transparent;padding: 12px 8px"}},"\n      ",{"n":"div","k":["روز شبیه‌سازی: ",{"n":"b","k":[{"h":"tick"}],"c":"c4x"}],"c":"cxe"},"\n    "],"a":{"style":"display: flex;gap: 12px;flex-wrap: wrap;align-items: center;background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 14px;padding: 16px 20px;margin-bottom: 34px"}},"\n\n    ","\n    ",{"n":"section","a":{"id":"decisions"},"k":["\n      ",{"n":"p","k":["۰۱ — تصمیم"],"c":"cl7"},"\n      ",{"n":"h2","k":["امروز باید دربارهٔ چه چیزی تصمیم بگیری"],"c":"cl8"},"\n      ",{"n":"p","k":["سیستم از داده‌های خام، فهرست کوتاهی از تصمیم‌های امروز می‌سازد. هر کارت، عددی که تصمیم را ایجاب کرده و اقدام پیشنهادی را کنار هم می‌گذارد."],"c":"cof"},"\n\n      ",{"n":"div","k":["\n        ",{"f":"decisions","as":"d","k":["\n          ",{"n":"div","a":{"style":{"p":["border-inline-start: 4px solid ",{"h":"d.color"}]}},"k":["\n            ",{"n":"span","a":{"style":{"p":["background: ",{"h":"d.pillBg"},";color: ",{"h":"d.color"}]}},"k":[{"h":"d.severity"}],"c":"cev"},"\n            ",{"n":"div","k":["\n              ",{"n":"div","k":[{"h":"d.title"}],"c":"cex"},"\n              ",{"n":"div","k":[{"h":"d.detail"}],"c":"cai"},"\n            "],"c":"cew"},"\n            ",{"n":"div","k":[{"h":"d.action"}],"c":"cey"},"\n          "],"c":"ceu"},"\n        "]},"\n      "],"c":"c2k"},"\n    "],"c":"cl6"},"\n\n    ","\n    ",{"n":"section","k":["\n      ",{"n":"h2","k":["شاخص‌های کلیدی در برابر هدف"],"c":"cog"},"\n      ",{"n":"p","k":["عدد خام به‌تنهایی تصمیم نمی‌سازد؛ فاصله‌اش با هدف می‌سازد. هر شاخص با هدف مزرعه و اختلافش نشان داده می‌شود."],"c":"cs4"},"\n      ",{"n":"div","k":["\n        ",{"f":"kpis","as":"k","k":["\n          ",{"n":"div","k":["\n            ",{"n":"div","k":["\n              ",{"n":"span","k":[{"h":"k.label"}],"c":"cq"},"\n              ",{"n":"span","a":{"style":{"p":["background: ",{"h":"k.bg"},";color: ",{"h":"k.color"}]}},"k":[{"h":"k.delta"}],"c":"cf0"},"\n            "],"c":"cez"},"\n            ",{"n":"div","k":[{"h":"k.value"}],"c":"cf1"},"\n            ",{"n":"div","k":["هدف: ",{"h":"k.target"}],"c":"co"},"\n          "],"c":"ci"},"\n        "]},"\n      "],"a":{"style":"display: grid;grid-template-columns: repeat(auto-fit, minmax(235px, 1fr));gap: 12px"}},"\n    "],"c":"cid"},"\n\n    ","\n    ",{"n":"section","a":{"id":"economics"},"k":["\n      ",{"n":"p","k":["۰۲ — اقتصاد"],"c":"cl7"},"\n      ",{"n":"h2","k":["اقتصاد هر سیکل تولید"],"c":"cl8"},"\n      ",{"n":"p","k":["مهم‌ترین عدد یک کارخانهٔ قارچ، برداشت نیست — ",{"n":"b","k":["بهای تمام‌شدهٔ هر کیلو"]}," است. این جدول، اقتصاد کامل سیکل جاری هر سالن را بر اساس فرض‌های قابل‌تغییر زیر حساب می‌کند."],"a":{"style":"font-size: 14px;line-height: 1.95;color: #666158;max-width: 68ch;margin: 0 0 20px"}},"\n\n      ",{"n":"div","k":["\n        ",{"n":"h3","k":["سناریو — این عددها را عوض کن"],"a":{"style":"font-size: 14.5px;font-weight: 700;margin: 0 0 4px"}},"\n        ",{"n":"p","k":["هر تغییری بزنی، کل جدول، حاشیهٔ سود، نقطهٔ سربه‌سر و تصمیم‌های بالای صفحه همان لحظه دوباره حساب می‌شوند."],"c":"cz4"},"\n        ",{"n":"div","k":["\n          ",{"n":"div","k":["\n            ",{"n":"label","a":{"for":"p-price"},"k":["قیمت فروش (تومان/کیلو)"],"c":"c3r"},"\n            ",{"n":"input","a":{"id":"p-price","type":"number","step":"5000","value":{"h":"f.price"}},"e":{"input":"h.price"}},"\n          "]},"\n          ",{"n":"div","k":["\n            ",{"n":"label","a":{"for":"p-comp"},"k":["کمپوست (تومان/کیلو)"],"c":"c3r"},"\n            ",{"n":"input","a":{"id":"p-comp","type":"number","step":"500","value":{"h":"f.compostCost"}},"e":{"input":"h.compostCost"}},"\n          "]},"\n          ",{"n":"div","k":["\n            ",{"n":"label","a":{"for":"p-pick"},"k":["دستمزد برداشت (تومان/کیلو)"],"c":"c3r"},"\n            ",{"n":"input","a":{"id":"p-pick","type":"number","step":"1000","value":{"h":"f.pickCost"}},"e":{"input":"h.pickCost"}},"\n          "]},"\n          ",{"n":"div","k":["\n            ",{"n":"label","a":{"for":"p-fix"},"k":["سربار ثابت هر سیکل (تومان)"],"c":"c3r"},"\n            ",{"n":"input","a":{"id":"p-fix","type":"number","step":"1000000","value":{"h":"f.fixedCost"}},"e":{"input":"h.fixedCost"}},"\n          "]},"\n        "],"a":{"style":"display: grid;grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));gap: 12px"}},"\n      "],"a":{"style":"background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 16px;padding: 20px 22px;margin-bottom: 16px"}},"\n\n      ",{"n":"div","k":["\n        ",{"n":"table","k":["\n          ",{"n":"thead","k":["\n            ",{"n":"tr","k":["\n              ",{"n":"th","k":["سالن"],"c":"caj"},"\n              ",{"n":"th","k":["مرحله"],"c":"caj"},"\n              ",{"n":"th","k":["کمپوست (کیلو)"],"c":"caj"},"\n              ",{"n":"th","k":["برداشت تاکنون"],"c":"caj"},"\n              ",{"n":"th","k":["برآورد کل سیکل"],"c":"caj"},"\n              ",{"n":"th","k":["بازده بیولوژیک"],"c":"caj"},"\n              ",{"n":"th","k":["بهای تمام‌شده/کیلو"],"c":"caj"},"\n              ",{"n":"th","k":["سود سیکل"],"c":"caj"},"\n              ",{"n":"th","k":["حاشیه"],"c":"caj"},"\n            "]},"\n          "]},"\n          ",{"n":"tbody","k":["\n            ",{"f":"econRows","as":"e","k":["\n              ",{"n":"tr","k":["\n                ",{"n":"td","k":[{"n":"span","a":{"style":{"p":["background: ",{"h":"e.color"}]}},"c":"cf3"},{"h":"e.name"}],"c":"cf2"},"\n                ",{"n":"td","k":[{"h":"e.phase"}," · روز ",{"h":"e.day"}],"c":"cf4"},"\n                ",{"n":"td","k":[{"h":"e.compost"}],"c":"c2r"},"\n                ",{"n":"td","k":[{"h":"e.soFar"}],"c":"c2r"},"\n                ",{"n":"td","k":[{"h":"e.expected"}],"c":"c2r"},"\n                ",{"n":"td","a":{"style":{"p":["color: ",{"h":"e.beColor"}]}},"k":[{"h":"e.be"},"٪"],"c":"c3y"},"\n                ",{"n":"td","k":[{"h":"e.costPerKg"}],"c":"c2r"},"\n                ",{"n":"td","a":{"style":{"p":["color: ",{"h":"e.profitColor"}]}},"k":[{"h":"e.profit"}],"c":"c3y"},"\n                ",{"n":"td","a":{"style":{"p":["color: ",{"h":"e.profitColor"}]}},"k":[{"h":"e.margin"},"٪"],"c":"c3y"},"\n              "]},"\n            "]},"\n            ",{"n":"tr","k":["\n              ",{"n":"td","k":["کل مزرعه"],"a":{"style":"padding: 12px 14px;font-weight: 800;background: #FAFAF7"}},"\n              ",{"n":"td","k":["۳ سالن فعال"],"a":{"style":"padding: 12px 14px;background: #FAFAF7;color: #666158"}},"\n              ",{"n":"td","k":[{"h":"total.compost"}],"c":"coh"},"\n              ",{"n":"td","k":[{"h":"total.soFar"}],"c":"coh"},"\n              ",{"n":"td","k":[{"h":"total.expected"}],"c":"coh"},"\n              ",{"n":"td","k":[{"h":"total.be"},"٪"],"c":"cs5"},"\n              ",{"n":"td","k":[{"h":"total.costPerKg"}],"c":"coh"},"\n              ",{"n":"td","a":{"style":{"p":["color: ",{"h":"total.profitColor"}]}},"k":[{"h":"total.profit"}],"c":"cs5"},"\n              ",{"n":"td","a":{"style":{"p":["color: ",{"h":"total.profitColor"}]}},"k":[{"h":"total.margin"},"٪"],"c":"cs5"},"\n            "]},"\n          "]},"\n        "],"a":{"style":"width: 100%;min-width: 860px;font-size: 13px"}},"\n      "],"a":{"style":"overflow-x: auto;background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 16px;margin-bottom: 14px"}},"\n      ",{"n":"p","k":["مبالغ سود بر حسب میلیون تومان. بازده بیولوژیک = کیلو قارچ برداشت‌شده به ازای هر ۱۰۰ کیلو کمپوست؛ استاندارد خوب برای قارچ دکمه‌ای حدود ۲۸ تا ۳۵ درصد است."],"a":{"style":"font-size: 12px;color: #666158;margin: 0 0 20px"}},"\n\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"n":"h4","k":["نقطهٔ سربه‌سر هر سالن"],"c":"cs6"},"\n          ",{"n":"div","k":[{"h":"breakEven.kg"}," ",{"n":"span","k":["کیلو"],"a":{"style":"font-size: 13px;font-weight: 600;color: #666158"}}],"a":{"style":"font-size: 24px;font-weight: 800;margin-bottom: 4px"}},"\n          ",{"n":"p","k":["زیر این عدد، سیکل ضرر می‌دهد. برآورد فعلی ",{"n":"b","k":[{"h":"breakEven.expected"}," کیلو"]}," است — یعنی ",{"h":"breakEven.safety"},"٪ حاشیهٔ اطمینان."],"c":"cyx"},"\n        "],"c":"ci"},"\n        ",{"n":"div","k":["\n          ",{"n":"h4","k":["ترکیب هزینهٔ هر سیکل"],"c":"cs6"},"\n          ",{"n":"div","k":["\n            ",{"n":"div","a":{"style":{"p":["width: ",{"h":"costMix.compostPct"},"%"]}},"c":"cak"},"\n            ",{"n":"div","a":{"style":{"p":["background: #5B3F92;","width: ",{"h":"costMix.casingPct"},"%"]}}},"\n            ",{"n":"div","a":{"style":{"p":["width: ",{"h":"costMix.laborPct"},"%"]}},"c":"c50"},"\n            ",{"n":"div","a":{"style":{"p":["width: ",{"h":"costMix.fixedPct"},"%"]}},"c":"cal"},"\n          "],"a":{"style":"display: flex;height: 22px;border-radius: 6px;overflow: hidden;margin-bottom: 10px"}},"\n          ",{"n":"div","k":["\n            ",{"n":"span","k":[{"n":"span","a":{"style":"width: 9px;height: 9px;background: #B4530E;border-radius: 2px"}},"کمپوست ",{"h":"costMix.compostPct"},"٪"],"c":"c3a"},"\n            ",{"n":"span","k":[{"n":"span","a":{"style":"width: 9px;height: 9px;background: #5B3F92;border-radius: 2px"}},"کیسینگ ",{"h":"costMix.casingPct"},"٪"],"c":"c3a"},"\n            ",{"n":"span","k":[{"n":"span","c":"cam"},"دستمزد ",{"h":"costMix.laborPct"},"٪"],"c":"c3a"},"\n            ",{"n":"span","k":[{"n":"span","a":{"style":"width: 9px;height: 9px;background: #0E6FB4;border-radius: 2px"}},"سربار ",{"h":"costMix.fixedPct"},"٪"],"c":"c3a"},"\n          "],"a":{"style":"display: flex;gap: 10px;flex-wrap: wrap;font-size: 11.5px;color: #45494F"}},"\n        "],"c":"ci"},"\n        ",{"n":"div","k":["\n          ",{"n":"h4","k":["حساسیت به قیمت"],"c":"cs6"},"\n          ",{"n":"p","k":["اگر قیمت فروش ۱۰٪ افت کند:"],"a":{"style":"font-size: 12.5px;line-height: 1.85;color: #45494F;margin: 0 0 10px"}},"\n          ",{"n":"div","a":{"style":{"p":["font-size: 20px;font-weight: 800;","color: ",{"h":"sensitivity.color"}]}},"k":[{"h":"sensitivity.margin"},"٪"]},"\n          ",{"n":"p","k":["حاشیهٔ سود جدید (اکنون ",{"h":"total.margin"},"٪)"],"a":{"style":"font-size: 12px;color: #666158;margin: 4px 0 0"}},"\n        "],"c":"ci"},"\n      "],"c":"cjb"},"\n\n      ",{"n":"h3","k":["ترکیب گرید و قیمت مؤثر"],"c":"cz5"},"\n      ",{"n":"p","k":["قیمت درجه یک، قیمت کل محصول نیست. قارچ دکمه‌ای که دیر چیده شود کلاهکش باز می‌شود و به درجه دو می‌افتد؛ درجه دو حدود ۷۲٪ و ریز حدود ۴۵٪ قیمت درجه یک به فروش می‌رود. ",{"n":"b","k":["قیمت مؤثر"]}," همان عددی است که واقعاً در محاسبهٔ سود بالا نشسته."],"c":"coi"},"\n      ",{"n":"div","k":["\n        ",{"f":"gradeRows","as":"g","k":["\n          ",{"n":"div","k":["\n            ",{"n":"div","k":["\n              ",{"n":"span","a":{"style":{"p":["background: ",{"h":"g.color"}]}},"c":"c67"},"\n              ",{"n":"span","k":[{"h":"g.name"}],"c":"c68"},"\n              ",{"n":"span","a":{"style":{"p":["background: ",{"h":"g.chipBg"},";color: ",{"h":"g.chipColor"}]}},"k":[{"h":"g.chip"}],"c":"c65"},"\n            "],"c":"cf5"},"\n            ",{"n":"div","k":["\n              ",{"n":"div","a":{"style":{"p":["width: ",{"h":"g.a"},"%"]}},"c":"c50"},"\n              ",{"n":"div","a":{"style":{"p":["width: ",{"h":"g.b"},"%"]}},"c":"cf7"},"\n              ",{"n":"div","a":{"style":{"p":["width: ",{"h":"g.c"},"%"]}},"c":"cf8"},"\n            "],"c":"cf6"},"\n            ",{"n":"div","k":["\n              ",{"n":"span","k":[{"n":"span","c":"cam"},"درجه یک ",{"h":"g.aLabel"}],"c":"c3a"},"\n              ",{"n":"span","k":[{"n":"span","c":"cfa"},"درجه دو ",{"h":"g.bLabel"}],"c":"c3a"},"\n              ",{"n":"span","k":[{"n":"span","c":"cfb"},"ریز ",{"h":"g.cLabel"}],"c":"c3a"},"\n            "],"c":"cf9"},"\n            ",{"n":"div","k":["\n              ",{"n":"div","k":["قیمت مؤثر هر کیلو"],"c":"co"},"\n              ",{"n":"div","k":[{"h":"g.effPrice"}],"c":"cfc"},"\n              ",{"n":"div","k":[{"h":"g.discount"},"٪ کمتر از قیمت درجه یک"],"c":"cfd"},"\n            "],"c":"c1e"},"\n          "],"c":"ci"},"\n        "]},"\n      "],"a":{"style":"display: grid;grid-template-columns: repeat(auto-fit, minmax(235px, 1fr));gap: 14px;margin-bottom: 10px"}},"\n\n      ",{"n":"h3","k":["مقایسه با سیکل قبلِ همین سالن"],"c":"cz5"},"\n      ",{"n":"p","k":["عدد امروز به‌تنهایی چیزی نمی‌گوید؛ افت تدریجی را فقط مقایسهٔ سیکل‌ها نشان می‌دهد. اگر یک سالن دو سیکل پشت‌سرهم افت کند، معمولاً مسئله از کیفیت کمپوست یا ضدعفونی ناقص سیکل قبل است، نه از تنظیمات امروز."],"c":"coi"},"\n      ",{"n":"div","k":["\n        ",{"f":"cycleCompare","as":"c","k":["\n          ",{"n":"div","k":["\n            ",{"n":"div","k":["\n              ",{"n":"span","a":{"style":{"p":["background: ",{"h":"c.color"}]}},"c":"c67"},"\n              ",{"n":"span","k":[{"h":"c.name"}],"c":"c68"},"\n              ",{"n":"span","a":{"style":{"p":["background: ",{"h":"c.deltaBg"},";color: ",{"h":"c.deltaColor"}]}},"k":[{"h":"c.deltaLabel"}],"c":"cff"},"\n            "],"c":"cfe"},"\n            ",{"n":"div","k":["\n              ",{"n":"span","k":["سیکل قبل"],"c":"c69"},"\n              ",{"n":"div","k":["\n                ",{"n":"div","a":{"style":{"p":["width: ",{"h":"c.prevW"},"%"]}},"c":"cfg"},"\n              "],"c":"c6a"},"\n              ",{"n":"span","k":[{"h":"c.prev"}],"c":"c6b"},"\n            "],"c":"c29"},"\n            ",{"n":"div","k":["\n              ",{"n":"span","k":["این سیکل"],"c":"c69"},"\n              ",{"n":"div","k":["\n                ",{"n":"div","a":{"style":{"p":["width: ",{"h":"c.curW"},"%;background: ",{"h":"c.color"}]}},"c":"cfi"},"\n              "],"c":"c6a"},"\n              ",{"n":"span","k":[{"h":"c.cur"}],"c":"c6b"},"\n            "],"c":"cfh"},"\n            ",{"n":"div","k":[{"h":"c.note"}],"c":"cfj"},"\n          "],"c":"ci"},"\n        "]},"\n      "],"c":"cjb"},"\n    "],"c":"cl6"},"\n\n    ","\n    ",{"n":"section","a":{"id":"plan"},"k":["\n      ",{"n":"p","k":["۰۳ — برنامه"],"c":"cl7"},"\n      ",{"n":"h2","k":["پیش‌بینی برداشت در برابر تعهدهای فروش"],"c":"cl8"},"\n      ",{"n":"p","k":["فروش قارچ دکمه‌ای پیش‌فروش می‌شود، ولی موج برداشت را نمی‌شود جابه‌جا کرد. این نمودار، برداشت ۱۴ روز آیندهٔ هر سه سالن را کنار تعهدهای ثبت‌شده می‌گذارد تا کسری پیش از وقوع دیده شود."],"c":"cof"},"\n\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"f":"forecast","as":"d","k":["\n            ",{"n":"div","k":["\n              ",{"n":"span","k":[{"h":"d.label"}],"c":"cfl"},"\n              ",{"n":"div","a":{"style":{"p":["height: ",{"h":"d.h"},"%;background: ",{"h":"d.color"}]}},"c":"cfm"},"\n              ",{"n":"span","k":[{"h":"d.day"}],"c":"cfn"},"\n              ",{"n":"span","k":[{"h":"d.mark"}],"c":"cfo"},"\n            "],"c":"cfk"},"\n          "]},"\n        "],"a":{"style":"display: flex;align-items: flex-end;gap: 4px;height: 180px;direction: ltr"}},"\n        ",{"n":"div","k":["\n          ",{"n":"span","k":[{"n":"span","c":"cz6"},"روز برداشت"],"c":"can"},"\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 10px;height: 10px;background: #D9D5C9;border-radius: 3px"}},"بدون برداشت"],"c":"can"},"\n          ",{"n":"span","k":[{"n":"span","k":["▾"],"a":{"style":"color: #A32222;font-weight: 700"}},"روز تحویل سفارش"],"c":"can"},"\n        "],"a":{"style":"display: flex;gap: 16px;flex-wrap: wrap;border-top: 1px solid #E4E1D6;margin-top: 14px;padding-top: 12px;font-size: 11.5px;color: #45494F"}},"\n      "],"c":"cqe"},"\n\n      ",{"n":"div","a":{"style":{"p":["padding: 16px 20px;border-radius: 12px;margin-bottom: 16px;","background: ",{"h":"coverage.bg"}]}},"k":["\n        ",{"n":"div","a":{"style":{"p":["font-size: 14.5px;font-weight: 700;margin-bottom: 4px;","color: ",{"h":"coverage.color"}]}},"k":[{"h":"coverage.title"}]},"\n        ",{"n":"div","k":[{"h":"coverage.detail"}],"c":"cai"},"\n      "]},"\n\n      ",{"n":"div","k":["\n        ",{"n":"table","k":["\n          ",{"n":"thead","k":["\n            ",{"n":"tr","k":["\n              ",{"n":"th","k":["تحویل"],"c":"cao"},"\n              ",{"n":"th","k":["مشتری"],"c":"cao"},"\n              ",{"n":"th","k":["مقدار"],"c":"cao"},"\n              ",{"n":"th","k":["برداشت تجمعی تا آن روز"],"c":"cao"},"\n              ",{"n":"th","k":["وضعیت"],"c":"cao"},"\n            "]},"\n          "]},"\n          ",{"n":"tbody","k":["\n            ",{"f":"commitments","as":"c","k":["\n              ",{"n":"tr","k":["\n                ",{"n":"td","k":[{"h":"c.when"}],"c":"c6c"},"\n                ",{"n":"td","k":[{"h":"c.customer"}],"c":"cfp"},"\n                ",{"n":"td","k":[{"h":"c.kg"}," کیلو"],"c":"c2s"},"\n                ",{"n":"td","k":[{"h":"c.cumForecast"}," کیلو"],"c":"c2s"},"\n                ",{"n":"td","k":[{"n":"span","a":{"style":{"p":["background: ",{"h":"c.bg"},";color: ",{"h":"c.color"}]}},"k":[{"h":"c.status"}],"c":"c3e"}],"c":"c6d"},"\n              "]},"\n            "]},"\n          "]},"\n        "],"a":{"style":"width: 100%;min-width: 620px;font-size: 13px"}},"\n      "],"a":{"style":"overflow-x: auto;background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 16px;margin-bottom: 30px"}},"\n\n      ",{"n":"h3","k":["برنامهٔ نیروی کار برداشت"],"c":"co9"},"\n      ",{"n":"p","k":["برداشت قارچ دکمه‌ای موجی است، پس نیاز به کارگر هم موجی است — و کارگر روزمزد را باید از قبل هماهنگ کرد. فرض محاسبه: هر کارگر ماهر حدود ۲۰ کیلو در ساعت می‌چیند و پنجرهٔ چیدن هر روز حدود ۵ ساعت صبح است."],"c":"coi"},"\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"n":"div","k":["\n            ",{"n":"div","k":["کل هفته"],"c":"c1k"},"\n            ",{"n":"div","k":[{"h":"labor.weekHours"}," ",{"n":"span","k":["نفر-ساعت"],"c":"c90"}],"c":"cs7"},"\n          "]},"\n          ",{"n":"div","k":["\n            ",{"n":"div","k":["اوج برداشت"],"c":"c1k"},"\n            ",{"n":"div","k":[{"h":"labor.peakKg"}," ",{"n":"span","k":["کیلو در روز ",{"h":"labor.peakDay"}],"c":"c90"}],"c":"cs7"},"\n          "]},"\n          ",{"n":"div","k":["\n            ",{"n":"div","k":["کارگر لازم در روز اوج"],"c":"c1k"},"\n            ",{"n":"div","k":[{"h":"labor.peakWorkers"}," ",{"n":"span","k":["نفر"],"c":"c90"}],"c":"cs7"},"\n          "]},"\n        "],"a":{"style":"display: flex;gap: 20px;flex-wrap: wrap;padding-bottom: 14px;margin-bottom: 14px;border-bottom: 1px solid #E4E1D6"}},"\n        ",{"n":"table","k":["\n          ",{"n":"thead","k":["\n            ",{"n":"tr","k":["\n              ",{"n":"th","k":["روز"],"c":"coj"},"\n              ",{"n":"th","k":["برداشت پیش‌بینی"],"c":"coj"},"\n              ",{"n":"th","k":["نفر-ساعت"],"c":"coj"},"\n              ",{"n":"th","k":["کارگر لازم"],"c":"coj"},"\n            "]},"\n          "]},"\n          ",{"n":"tbody","k":["\n            ",{"f":"labor.days","as":"d","k":["\n              ",{"n":"tr","k":["\n                ",{"n":"td","a":{"style":{"p":["background: ",{"h":"d.bg"}]}},"k":[{"h":"d.day"}],"c":"cfq"},"\n                ",{"n":"td","a":{"style":{"p":["background: ",{"h":"d.bg"}]}},"k":[{"h":"d.kg"}," کیلو"],"c":"c6e"},"\n                ",{"n":"td","a":{"style":{"p":["background: ",{"h":"d.bg"}]}},"k":[{"h":"d.hours"}],"c":"c6e"},"\n                ",{"n":"td","a":{"style":{"p":["background: ",{"h":"d.bg"}]}},"k":[{"h":"d.workers"}],"c":"cfr"},"\n              "]},"\n            "]},"\n          "]},"\n        "],"a":{"style":"width: 100%;font-size: 13px"}},"\n      "],"a":{"style":"background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 16px;padding: 20px 22px;margin-bottom: 30px"}},"\n\n      ",{"n":"h3","k":["برنامهٔ سالن‌ها — ۴۵ روز آینده"],"c":"co9"},"\n      ",{"n":"p","k":["هر روزی که یک سالن خالی بماند، هزینهٔ ثابتش را می‌پردازی بدون اینکه چیزی تولید کند. این نوار نشان می‌دهد سالن‌ها کِی خالی می‌شوند و سفارش کمپوست بعدی باید کِی ثبت شود."],"c":"coi"},"\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"n":"span","k":["امروز"]},{"n":"span","k":["+۱۵ روز"]},{"n":"span","k":["+۳۰ روز"]},{"n":"span","k":["+۴۵ روز"]},"\n        "],"a":{"style":"direction: ltr;display: flex;justify-content: space-between;font-size: 10.5px;color: #666158;margin-bottom: 8px;padding-inline-start: 78px"}},"\n        ",{"f":"gantt","as":"g","k":["\n          ",{"n":"div","k":["\n            ",{"n":"span","k":[{"h":"g.name"}],"c":"cfs"},"\n            ",{"n":"div","k":["\n              ",{"f":"g.segs","as":"s","k":["\n                ",{"n":"div","a":{"style":{"p":["width: ",{"h":"s.w"},"%;background: ",{"h":"s.bg"}]}}},"\n              "]},"\n            "],"c":"cft"},"\n          "],"c":"c3k"},"\n        "]},"\n        ",{"n":"div","k":["\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 11px;height: 11px;background: #F4E3D3;border-radius: 3px"}},"اسپان‌ران"],"c":"can"},"\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 11px;height: 11px;background: #EBE3F5;border-radius: 3px"}},"کیسینگ"],"c":"can"},"\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 11px;height: 11px;background: #DCEBFA;border-radius: 3px"}},"پین‌ست"],"c":"can"},"\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 11px;height: 11px;background: #BFDCBA;border-radius: 3px"}},"فلاش"],"c":"can"},"\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 11px;height: 11px;background: #F1EEE7;border-radius: 3px"}},"استراحت"],"c":"can"},"\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 11px;height: 11px;background: #E0DACB;border-radius: 3px"}},"تخلیه و ضدعفونی"],"c":"can"},"\n        "],"a":{"style":"display: flex;gap: 12px;flex-wrap: wrap;border-top: 1px solid #E4E1D6;margin-top: 14px;padding-top: 12px;font-size: 11.5px;color: #45494F"}},"\n      "],"c":"cqe"},"\n    "],"c":"cl6"},"\n\n    ","\n    ",{"n":"section","k":["\n      ",{"n":"h2","k":["برداشت هفت روز گذشته"],"c":"cog"},"\n      ",{"n":"p","k":["تفکیک به سالن نشان می‌دهد کدام سالن الان بار مزرعه را می‌کشد — و اگر موج‌ها روی هم بیفتند، جای برنامه‌ریزی پرکردن ایراد دارد."],"c":"cs4"},"\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"f":"bars","as":"b","k":["\n            ",{"n":"div","k":["\n              ",{"n":"span","k":[{"h":"b.total"}],"c":"cfv"},"\n              ",{"n":"div","a":{"style":{"p":["height: ",{"h":"b.h"},"%"]}},"k":["\n                ",{"n":"div","a":{"style":{"p":["height: ",{"h":"b.s3"},"%"]}},"c":"cal"},"\n                ",{"n":"div","a":{"style":{"p":["height: ",{"h":"b.s2"},"%"]}},"c":"c50"},"\n                ",{"n":"div","a":{"style":{"p":["height: ",{"h":"b.s1"},"%"]}},"c":"cak"},"\n              "],"c":"cfw"},"\n              ",{"n":"span","k":[{"h":"b.label"}],"c":"c5x"},"\n            "],"c":"cfu"},"\n          "]},"\n        "],"a":{"style":"display: flex;align-items: flex-end;gap: 12px;height: 180px;direction: ltr"}},"\n        ",{"n":"div","k":["\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 10px;height: 10px;background: #B4530E;border-radius: 3px"}},"سالن ۱"],"c":"c28"},"\n          ",{"n":"span","k":[{"n":"span","c":"cz6"},"سالن ۲"],"c":"c28"},"\n          ",{"n":"span","k":[{"n":"span","a":{"style":"width: 10px;height: 10px;background: #0E6FB4;border-radius: 3px"}},"سالن ۳"],"c":"c28"},"\n        "],"a":{"style":"display: flex;gap: 14px;flex-wrap: wrap;border-top: 1px solid #E4E1D6;margin-top: 14px;padding-top: 12px"}},"\n      "],"c":"ch"},"\n    "],"c":"cid"},"\n\n    ","\n    ",{"n":"section","a":{"id":"ops"},"k":["\n      ",{"n":"p","k":["۰۴ — عملیات"],"c":"cl7"},"\n      ",{"n":"h2","k":["وضعیت محیطی سالن‌ها"],"c":"cl8"},"\n      ",{"n":"p","k":["لایهٔ زیرین تصمیم‌ها. اگر این چهار عدد در بازهٔ مرحله بمانند، برداشت سیکل بعد قابل پیش‌بینی می‌شود؛ اگر نمانند، دو هفته بعد در جدول اقتصاد بالا خودش را نشان می‌دهد."],"c":"cof"},"\n\n      ",{"n":"div","k":["\n        ",{"f":"tabs","as":"t","k":["\n          ",{"n":"button","a":{"style":{"p":["background: ",{"h":"t.bg"},";border: 1.5px solid ",{"h":"t.border"}]}},"e":{"click":"t.pick"},"k":["\n            ",{"n":"div","k":["\n              ",{"n":"span","k":[{"h":"t.name"}],"c":"cfz"},"\n              ",{"n":"span","a":{"style":{"p":["color: ",{"h":"t.color"},";background: ",{"h":"t.soft"}]}},"k":[{"h":"t.phase"}],"c":"cg0"},"\n            "],"c":"cfy"},"\n            ",{"n":"div","k":["روز ",{"h":"t.day"}," از ۴۲ · ",{"h":"t.yieldLabel"}],"c":"co"},"\n          "],"c":"cfx"},"\n        "]},"\n      "],"a":{"style":"display: flex;gap: 10px;flex-wrap: wrap;margin-bottom: 18px"}},"\n\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"n":"h3","k":[{"h":"room.name"}],"c":"c4o"},"\n          ",{"n":"span","a":{"style":{"p":["color: ",{"h":"room.color"},";background: ",{"h":"room.soft"}]}},"k":[{"h":"room.phase"}],"c":"c3e"},"\n          ",{"n":"span","k":["روز ",{"h":"room.day"}," از ۴۲ · ",{"h":"room.remain"}," روز تا پایان سیکل"],"c":"c80"},"\n        "],"a":{"style":"display: flex;align-items: baseline;gap: 12px;flex-wrap: wrap;margin-bottom: 18px"}},"\n\n        ",{"n":"div","k":["\n          ",{"n":"div","k":["\n            ",{"n":"div","a":{"style":"width: 33.3%;background: #F4E3D3"}},"\n            ",{"n":"div","a":{"style":"width: 9.5%;background: #EBE3F5"}},"\n            ",{"n":"div","a":{"style":"width: 7.1%;background: #DCEBFA"}},"\n            ",{"n":"div","c":"cs8"},"\n            ",{"n":"div","c":"cz7"},"\n            ",{"n":"div","c":"cs8"},"\n            ",{"n":"div","c":"cz7"},"\n            ",{"n":"div","c":"cs8"},"\n            ",{"n":"div","a":{"style":"width: 7.1%;background: #E0DACB"}},"\n          "],"a":{"style":"display: flex;height: 14px;border-radius: 7px;overflow: hidden"}},"\n          ",{"n":"div","a":{"style":{"p":["position: absolute;top: -4px;width: 3px;height: 22px;background: #16181C;border-radius: 2px;","left: ",{"h":"room.dayPct"},"%"]}}},"\n        "],"a":{"style":"direction: ltr;position: relative;margin-bottom: 8px"}},"\n        ",{"n":"div","k":["\n          ",{"n":"span","k":["اسپان‌ران"]},{"n":"span","k":["کیسینگ"]},{"n":"span","k":["پین‌ست"]},{"n":"span","k":["فلاش ۱"]},{"n":"span","k":["فلاش ۲"]},{"n":"span","k":["فلاش ۳"]},{"n":"span","k":["تخلیه"]},"\n        "],"a":{"style":"direction: ltr;display: flex;justify-content: space-between;font-size: 10.5px;color: #666158;margin-bottom: 22px"}},"\n\n        ",{"n":"div","k":["\n          ",{"f":"metrics","as":"m","k":["\n            ",{"n":"div","k":["\n              ",{"n":"div","k":[{"h":"m.label"}],"c":"cg2"},"\n              ",{"n":"div","k":[{"h":"m.value"},{"n":"span","k":[" ",{"h":"m.unit"}],"c":"c90"}],"c":"cg3"},"\n              ",{"n":"svg","a":{"viewBox":"0 0 280 72","role":"img","aria-label":"روند ۱۴ روز اخیر"},"k":["\n                ",{"n":"rect","a":{"x":"8","y":{"h":"m.bandY"},"width":"264","height":{"h":"m.bandH"},"fill":{"h":"m.soft"}}},"\n                ",{"n":"polyline","a":{"points":{"h":"m.pts"},"fill":"none","stroke":{"h":"m.color"},"stroke-width":"2.2","stroke-linejoin":"round","stroke-linecap":"round"}},"\n              "],"c":"cg4"},"\n              ",{"n":"div","a":{"style":{"p":["background: ",{"h":"m.chipBg"},";color: ",{"h":"m.chipColor"}]}},"k":[{"h":"m.chip"}],"c":"cg5"},"\n            "],"c":"cg1"},"\n          "]},"\n        "],"c":"cz8"},"\n        ",{"n":"p","k":["خط، روند ۱۴ روز اخیر است و نوار رنگی، بازهٔ مرجع ",{"n":"b","k":["مرحلهٔ فعلی"]},". وقتی سالن مرحله عوض می‌کند، نوار جابه‌جا می‌شود و بخشی از خط بیرون می‌افتد — این طبیعی است، نه خطا."],"a":{"style":"font-size: 12px;color: #666158;margin: 12px 0 0"}},"\n      "],"c":"cpd"},"\n\n      ",{"n":"div","k":["\n        ",{"n":"h3","k":["هشدارهای ",{"h":"room.name"}],"c":"cz2"},"\n        ",{"n":"p","k":["هشدار نسبت به مرحله ساخته می‌شود، نه با یک عدد ثابت: CO₂ برابر ۱۵٬۰۰۰ در اسپان‌ران طبیعی است و در فلاش فاجعه."],"c":"cz4"},"\n        ",{"n":"div","k":["\n          ",{"f":"room.alerts","as":"a","k":["\n            ",{"n":"div","a":{"style":{"p":["background: ",{"h":"a.bg"}]}},"k":["\n              ",{"n":"span","a":{"style":{"p":["background: ",{"h":"a.pillBg"},";color: ",{"h":"a.color"}]}},"k":[{"h":"a.severity"}],"c":"c3e"},"\n              ",{"n":"span","k":[{"h":"a.title"}],"c":"c4j"},"\n              ",{"n":"span","k":[{"h":"a.detail"}],"c":"c63"},"\n            "],"c":"cg6"},"\n          "]},"\n          ",{"i":"room.noAlerts","k":["\n            ",{"n":"div","k":["همهٔ مقادیر این سالن در بازهٔ مرجع مرحله‌اند — هیچ هشدار بازی وجود ندارد."],"a":{"style":"padding: 14px;border-radius: 10px;background: #E3EEE1;color: #166534;font-size: 13.5px;font-weight: 600"}},"\n          "]},"\n        "],"c":"c3d"},"\n      "],"c":"ch"},"\n    "],"c":"cl6"},"\n\n    ","\n    ",{"n":"section","a":{"id":"cash"},"k":["\n      ",{"n":"p","k":["۰۵ — نقدینگی"],"c":"cl7"},"\n      ",{"n":"h2","k":["پول کجاست"],"c":"cl8"},"\n      ",{"n":"p","k":["کارخانهٔ سودده هم اگر طلبش وصول نشود، برای خرید کمپوست سیکل بعد پول کم می‌آورد. این بخش، سود روی کاغذ را از پول در دسترس جدا می‌کند."],"c":"cof"},"\n\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"n":"div","k":[{"h":"cash.balance"}],"c":"cin"},"\n          ",{"n":"div","k":["موجودی صندوق (م.ت)"],"c":"c31"},"\n        "],"c":"cah"},"\n        ",{"n":"div","k":["\n          ",{"n":"div","k":[{"h":"cash.receivable"}],"a":{"style":"font-size: 21px;font-weight: 800;color: #8A5410"}},"\n          ",{"n":"div","k":["مطالبات وصول‌نشده (م.ت)"],"c":"c31"},"\n        "],"c":"cah"},"\n        ",{"n":"div","k":["\n          ",{"n":"div","k":[{"h":"cash.upcoming"}],"c":"cz1"},"\n          ",{"n":"div","k":["پرداختی ۱۴ روز آینده (م.ت)"],"c":"c31"},"\n        "],"c":"cah"},"\n        ",{"n":"div","k":["\n          ",{"n":"div","a":{"style":{"p":["color: ",{"h":"cash.netColor"}]}},"k":[{"h":"cash.net"}],"c":"cin"},"\n          ",{"n":"div","k":["مانده پس از تعهدها (م.ت)"],"c":"c31"},"\n        "],"c":"cah"},"\n      "],"a":{"style":"display: grid;grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));gap: 12px;margin-bottom: 16px"}},"\n\n      ",{"n":"div","k":["\n        ",{"n":"table","k":["\n          ",{"n":"thead","k":["\n            ",{"n":"tr","k":["\n              ",{"n":"th","k":["مشتری"],"c":"cao"},"\n              ",{"n":"th","k":["مبلغ (م.ت)"],"c":"cao"},"\n              ",{"n":"th","k":["روز از تحویل"],"c":"cao"},"\n              ",{"n":"th","k":["وضعیت"],"c":"cao"},"\n            "]},"\n          "]},"\n          ",{"n":"tbody","k":["\n            ",{"f":"receivables","as":"r","k":["\n              ",{"n":"tr","k":["\n                ",{"n":"td","k":[{"h":"r.name"}],"c":"c6c"},"\n                ",{"n":"td","k":[{"h":"r.amount"}],"c":"c2s"},"\n                ",{"n":"td","k":[{"h":"r.days"}],"c":"c2s"},"\n                ",{"n":"td","k":[{"n":"span","a":{"style":{"p":["background: ",{"h":"r.bg"},";color: ",{"h":"r.color"}]}},"k":[{"h":"r.status"}],"c":"c3e"}],"c":"c6d"},"\n              "]},"\n            "]},"\n          "]},"\n        "],"a":{"style":"width: 100%;min-width: 560px;font-size: 13px"}},"\n      "],"a":{"style":"overflow-x: auto;background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 16px"}},"\n    "],"c":"cl6"},"\n\n    ","\n    ",{"n":"section","k":["\n      ",{"n":"h2","k":["ثبت‌های امروز"],"c":"cog"},"\n      ",{"n":"p","k":["همهٔ عددهای بالای این صفحه از همین سطرها ساخته شده‌اند. در سیستم واقعی، هر سطر را یک نفر از موبایل داخل سالن ثبت کرده است."],"c":"cs4"},"\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"f":"logs","as":"l","k":["\n            ",{"n":"div","k":["\n              ",{"n":"span","a":{"style":{"p":["background: ",{"h":"l.bg"},";color: ",{"h":"l.color"}]}},"k":[{"h":"l.type"}],"c":"cg8"},"\n              ",{"n":"span","k":[{"h":"l.text"}],"c":"cg9"},"\n              ",{"n":"span","k":[{"h":"l.room"}],"c":"co"},"\n              ",{"n":"span","k":[{"h":"l.time"}],"c":"c4e"},"\n            "],"c":"cg7"},"\n          "]},"\n        "],"c":"c3d"},"\n      "],"c":"c46"},"\n    "],"c":"cid"},"\n\n    ","\n    ",{"n":"section","k":["\n      ",{"n":"h2","k":["داده از کجا به تصمیم می‌رسد"],"c":"cog"},"\n      ",{"n":"p","k":["ارزش سیستم در فرم‌ها نیست؛ در سه مرحلهٔ بعدی است."],"a":{"style":"font-size: 13.5px;color: #666158;margin: 0 0 18px;max-width: 68ch"}},"\n      ",{"n":"div","k":["\n        ",{"n":"div","k":["\n          ",{"n":"div","k":["۱"],"c":"c24"},"\n          ",{"n":"h4","k":["ثبت در سالن"],"c":"c81"},"\n          ",{"n":"p","k":["اپراتور با موبایل، در کمتر از ۳۰ ثانیه فرم کوتاه را پر می‌کند."],"c":"c34"},"\n        "],"a":{"style":"background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 14px;padding: 18px 20px;border-top: 3px solid #B4530E"}},"\n        ",{"n":"div","k":["\n          ",{"n":"div","k":["۲"],"c":"c24"},"\n          ",{"n":"h4","k":["سنجش با مرحله"],"c":"c81"},"\n          ",{"n":"p","k":["سیستم می‌داند سالن در کدام روز سیکل است و عدد را با بازهٔ همان مرحله می‌سنجد."],"c":"c34"},"\n        "],"a":{"style":"background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 14px;padding: 18px 20px;border-top: 3px solid #5B3F92"}},"\n        ",{"n":"div","k":["\n          ",{"n":"div","k":["۳"],"c":"c24"},"\n          ",{"n":"h4","k":["تبدیل به پول"],"c":"c81"},"\n          ",{"n":"p","k":["هر کیلو برداشت و هر کیلو کمپوست به بهای تمام‌شده و حاشیهٔ سود همان سیکل تبدیل می‌شود."],"c":"c34"},"\n        "],"a":{"style":"background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 14px;padding: 18px 20px;border-top: 3px solid #166534"}},"\n        ",{"n":"div","k":["\n          ",{"n":"div","k":["۴"],"c":"c24"},"\n          ",{"n":"h4","k":["تصمیم امروز"],"c":"c81"},"\n          ",{"n":"p","k":["آنچه از آستانه رد شده، بالای صفحه به‌صورت یک تصمیم با اقدام مشخص می‌نشیند."],"c":"c34"},"\n        "],"a":{"style":"background: #FFFFFF;border: 1px solid #E4E1D6;border-radius: 14px;padding: 18px 20px;border-top: 3px solid #A32222"}},"\n      "],"c":"cz8"},"\n    "],"a":{"style":"margin-bottom: 34px"}},"\n\n    ",{"n":"div","k":["\n      ",{"n":"p","k":["همهٔ عددهای این صفحه شبیه‌سازی‌شده‌اند و هیچ ارتباطی با داده واقعی مزرعهٔ دُرّین ندارند. محصول در همهٔ محاسبات ",{"n":"b","k":["قارچ دکمه‌ای"]}," است و منحنی‌ها، بازه‌های مرجع و نسبت‌های اقتصادی بر پایهٔ الگوی رایج همین محصول ساخته شده‌اند."],"a":{"style":"font-size: 13px;line-height: 1.95;color: #45494F;max-width: 66ch;margin: 0 auto"}},"\n    "],"a":{"style":"background: #FAFAF7;border: 1px dashed #D9D5C9;border-radius: 14px;padding: 20px 24px;text-align: center"}},"\n\n  "],"a":{"style":"max-width: 1180px;margin: 0 auto;padding: 46px 24px 80px"}},"\n\n  ",{"n":"footer","k":["\n    ",{"n":"div","k":["\n      ",{"n":"a","a":{"href":"dorrin.html"},"k":["← مطالعهٔ موردی کامل"],"c":"c2j"},"\n      ",{"n":"span","k":["رضا هاشمی · پل فرماندهی شبیه‌سازی‌شده"],"c":"cq"},"\n    "],"a":{"style":"max-width: 1180px;margin: 0 auto;padding: 24px;display: flex;justify-content: space-between;flex-wrap: wrap;gap: 10px"}},"\n  "],"c":"c1p"},"\n\n"],"c":"cb"},"\n"],Component);
