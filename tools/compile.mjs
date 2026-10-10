// قالب پارس‌شده را به یک AST فشرده تبدیل می‌کند و استایل‌های ثابت را به کلاس می‌برد.
import { isVoid, isRaw } from './parse.mjs';

const EVENTS = { onclick: 'click', oninput: 'input', onchange: 'input', onsubmit: 'submit' };
const HOLE = /\{\{\s*([^}]+?)\s*\}\}/g;

// «{{a}} b {{c}}» → لیست تکه‌ها؛ متن خالی → رشته
function parts(str) {
  const out = [];
  let last = 0;
  for (const m of str.matchAll(HOLE)) {
    if (m.index > last) out.push(str.slice(last, m.index));
    out.push({ h: m[1] });
    last = m.index + m[0].length;
  }
  if (last < str.length) out.push(str.slice(last));
  return out;
}

const hasHole = (s) => typeof s === 'string' && HOLE.test(s.replace(HOLE, (x) => x));

function attrValue(str) {
  const ps = parts(str);
  if (ps.length === 0) return '';
  if (ps.length === 1) return ps[0];               // رشته یا یک حفرهٔ تنها
  return { p: ps };
}

// استایل را به دو بخش می‌شکند: اعلان‌های ثابت (کلاس‌پذیر) و اعلان‌های حفره‌دار.
function splitStyle(style) {
  const fixed = [];
  const dyn = [];
  for (const decl of style.split(';')) {
    const d = decl.trim();
    if (!d) continue;
    (d.includes('{{') ? dyn : fixed).push(d);
  }
  return { fixed: fixed.join(';'), dyn: dyn.join(';') };
}

export function compile(templateRoot, ctx) {
  // ctx: { styleUse: Map<cssText, {count, pages:Set}>, page }
  let loopDepth = 0;                                // گره‌های داخل حلقه بارها تکرار می‌شوند
  const walk = (node) => {
    if (node.tag === '#text' || node.tag === '#raw') {
      const t = node.text;
      if (!t) return [];
      if (node.tag === '#raw') return [t];
      const ps = parts(t);
      return ps.length ? ps : [];
    }

    if (node.tag === 'sc-for') {
      const list = (node.attrs.list || '').replace(HOLE, '$1').trim();
      loopDepth++;
      const body = kids(node);
      loopDepth--;
      return [{ f: list, as: node.attrs.as || 'item', k: body }];
    }
    if (node.tag === 'sc-if') {
      const v = (node.attrs.value || '').replace(HOLE, '$1').trim();
      return [{ i: v, k: kids(node) }];
    }

    const a = {};
    const ev = {};
    let cls = null;
    for (const name of node.order || Object.keys(node.attrs)) {
      if (name.startsWith('hint-')) continue;
      const lower = name.toLowerCase();
      const raw = node.attrs[name];
      if (lower in EVENTS && typeof raw === 'string' && raw.trim().startsWith('{{')) {
        ev[EVENTS[lower]] = raw.replace(HOLE, '$1').trim();
        continue;
      }
      // نام اتریبیوت با همان حروف اصلی نگه داشته می‌شود: در SVG بزرگ و کوچک فرق دارد
      // (viewBox ≠ viewbox). در HTML نام‌ها بی‌تفاوت‌اند، پس این برای هر دو درست است.
      if (raw === null) { a[name] = null; continue; }

      if (lower === 'style') {
        const { fixed, dyn } = splitStyle(raw);
        if (fixed) {
          const key = fixed;
          let rec = ctx.styleUse.get(key);
          if (!rec) { rec = { count: 0, pages: new Set(), cls: null }; ctx.styleUse.set(key, rec); }
          rec.count += loopDepth ? 8 : 1;
          rec.pages.add(ctx.page);
          cls = key;                                // در پاس دوم به نام کلاس بدل می‌شود
        }
        if (dyn) a.style = attrValue(dyn);
        continue;
      }
      a[name] = attrValue(raw);
    }

    const out = { n: node.tag };
    if (cls !== null) out.s = cls;
    if (Object.keys(a).length) out.a = a;
    if (Object.keys(ev).length) out.e = ev;
    if (node.self) out.sf = 1;
    if (!isVoid(node.tag) && !node.self) {
      const k = kids(node);
      if (k.length) out.k = k;
    }
    if (isRaw(node.tag)) out.r = 1;
    return [out];
  };

  const kids = (node) => (node.kids || []).flatMap(walk);
  return kids(templateRoot);
}

// پاس دوم: کلید استایل را با نام کلاس (یا استایل درجا، اگر یکتاست) جا‌به‌جا می‌کند
export function applyClasses(ast, styleUse) {
  const visit = (n) => {
    if (typeof n === 'string' || n.h) return;
    if (n.k) n.k.forEach(visit);
    if (!n.s) return;
    const rec = styleUse.get(n.s);
    if (rec && rec.cls) {
      n.c = rec.cls;
      delete n.s;
    } else {
      // یکتا — همان‌جا می‌ماند و با بخش پویا ادغام می‌شود
      const fixed = n.s;
      delete n.s;
      n.a = n.a || {};
      const dynamic = n.a.style;
      if (dynamic === undefined) n.a.style = fixed;
      else if (typeof dynamic === 'string') n.a.style = `${fixed};${dynamic}`;
      else n.a.style = { p: [`${fixed};`, ...(dynamic.p || [dynamic])] };
    }
  };
  ast.forEach(visit);
}
