// AST + مقادیر → رشتهٔ HTML (پیش‌رندر در زمان ساخت)
import { isVoid, encodeText, encodeAttr } from './parse.mjs';

export function resolve(path, scopes) {
  const p = String(path).trim();
  if (p === 'true') return true;
  if (p === 'false') return false;
  if (p === 'null') return null;
  if (/^-?\d+(\.\d+)?$/.test(p)) return Number(p);
  const bits = p.split('.');
  for (let i = scopes.length - 1; i >= 0; i--) {
    const s = scopes[i];
    if (s && Object.prototype.hasOwnProperty.call(s, bits[0])) {
      let v = s[bits[0]];
      for (let j = 1; j < bits.length && v != null; j++) v = v[bits[j]];
      return v;
    }
  }
  return undefined;
}

const txt = (v) => (v == null || v === false ? '' : String(v));

function attrString(v, scopes) {
  if (v === null) return null;
  if (typeof v === 'string') return v;
  if (v.h !== undefined) {
    const r = resolve(v.h, scopes);
    return r === undefined || r === null || typeof r === 'function' ? null : String(r);
  }
  return v.p.map((x) => (typeof x === 'string' ? x : txt(resolve(x.h, scopes)))).join('');
}

export function renderToString(ast, scopes, selectValue) {
  let out = '';
  for (const node of ast) {
    if (typeof node === 'string') {
      out += encodeText(node.replace(/[ \t\r\n]*\n[ \t\r\n]*/g, '\n'));
      continue;
    }
    if (node.h !== undefined) { out += encodeText(txt(resolve(node.h, scopes))); continue; }
    if (node.f !== undefined) {
      const list = resolve(node.f, scopes) || [];
      list.forEach((item, idx) => {
        out += renderToString(node.k || [], [...scopes, { [node.as]: item, $index: idx }]);
      });
      continue;
    }
    if (node.i !== undefined) {
      if (resolve(node.i, scopes)) out += renderToString(node.k || [], scopes);
      continue;
    }

    // عنصر
    let attrs = '';
    const cls = node.c ? node.c : null;
    let ownValue;
    if (cls) attrs += ` class="${cls}"`;
    for (const [k, v] of Object.entries(node.a || {})) {
      const s = attrString(v, scopes);
      if (s === null) { if (v === null) attrs += ` ${k}`; continue; }
      if (k === 'value') {
        ownValue = s;
        // `value` روی <select> اتریبیوت معتبری نیست؛ به جایش <option selected> علامت می‌خورد
        if (node.n === 'select') continue;
      }
      if (k === 'class' && cls) { attrs = attrs.replace(`class="${cls}"`, `class="${cls} ${s}"`); continue; }
      attrs += ` ${k}="${encodeAttr(s)}"`;
    }
    if (node.n === 'option' && selectValue !== undefined && ownValue === selectValue) attrs += ' selected';

    out += `<${node.n}${attrs}>`;
    if (isVoid(node.n)) continue;
    const nextSelect = node.n === 'select' ? (ownValue ?? '') : undefined;
    if (node.r) out += (node.k || []).map((x) => (typeof x === 'string' ? x : '')).join('');
    else out += renderToString(node.k || [], scopes, nextSelect);
    out += `</${node.n}>`;
  }
  return out;
}
