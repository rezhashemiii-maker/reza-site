// یک پارسر کوچک HTML برای فایل‌های .dc.html — بدون هیچ وابستگی بیرونی.
// خروجی: درختی از گره‌ها که ساخت‌های قالب (sc-for / sc-if / {{hole}}) را می‌شناسد.

const VOID = new Set(['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
  'link', 'meta', 'param', 'source', 'track', 'wbr']);
const RAW = new Set(['script', 'style', 'textarea']);

export const isVoid = (t) => VOID.has(t);
export const isRaw = (t) => RAW.has(t);

export function decode(s) {
  return s.replace(/&(amp|lt|gt|quot|apos|nbsp|#39|#x27|#160);/g, (m, k) => ({
    amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ',
    '#39': "'", '#x27': "'", '#160': ' ',
  })[k]);
}

export const encodeText = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
export const encodeAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');

// ---------------------------------------------------------------- tokenizer

export function parse(src) {
  let i = 0;
  const root = { tag: '#root', attrs: {}, kids: [] };
  const stack = [root];
  const top = () => stack[stack.length - 1];

  const pushText = (raw) => {
    if (!raw) return;
    top().kids.push({ tag: '#text', text: decode(raw) });
  };

  while (i < src.length) {
    const lt = src.indexOf('<', i);
    if (lt === -1) { pushText(src.slice(i)); break; }
    pushText(src.slice(i, lt));

    if (src.startsWith('<!--', lt)) {
      const end = src.indexOf('-->', lt);
      i = end === -1 ? src.length : end + 3;
      continue;                                    // کامنت‌ها حذف می‌شوند
    }
    if (src.startsWith('<!', lt)) {
      const end = src.indexOf('>', lt);
      i = end === -1 ? src.length : end + 1;
      continue;                                    // doctype
    }
    if (src.startsWith('</', lt)) {
      const end = src.indexOf('>', lt);
      const name = src.slice(lt + 2, end).trim().toLowerCase();
      for (let s = stack.length - 1; s > 0; s--) {
        if (stack[s].tag === name) { stack.length = s; break; }
      }
      i = end + 1;
      continue;
    }

    // تگ باز
    const m = /^<([a-zA-Z][a-zA-Z0-9:-]*)/.exec(src.slice(lt));
    if (!m) { pushText('<'); i = lt + 1; continue; }
    const tag = m[1].toLowerCase();
    let p = lt + m[0].length;
    const attrs = {};
    const order = [];
    let selfClosed = false;
    for (;;) {
      while (p < src.length && /\s/.test(src[p])) p++;
      if (p >= src.length) break;
      if (src[p] === '>') { p++; break; }
      if (src.startsWith('/>', p)) { p += 2; selfClosed = true; break; }
      const am = /^([^\s=/>]+)/.exec(src.slice(p));
      if (!am) { p++; continue; }
      const name = am[1];
      p += am[1].length;
      let value = '';
      while (p < src.length && /\s/.test(src[p])) p++;
      if (src[p] === '=') {
        p++;
        while (p < src.length && /\s/.test(src[p])) p++;
        const q = src[p];
        if (q === '"' || q === "'") {
          const end = src.indexOf(q, p + 1);
          value = src.slice(p + 1, end);
          p = end + 1;
        } else {
          const em = /^[^\s>]*/.exec(src.slice(p));
          value = em[0];
          p += em[0].length;
        }
      } else {
        value = null;                              // اتریبیوت بولین
      }
      if (!(name in attrs)) order.push(name);
      attrs[name] = value === null ? null : decode(value);
    }

    const node = { tag, attrs, order, kids: [] };
    if (selfClosed) node.self = true;
    top().kids.push(node);
    i = p;

    if (VOID.has(tag)) continue;
    // `<rect …/>` در SVG واقعاً خودبسته است. اگر نادیده بگیریم، همهٔ
    // هم‌نیاهای بعدی فرزندش می‌شوند و تصویر از هم می‌پاشد.
    if (selfClosed) continue;
    if (RAW.has(tag)) {
      const close = src.toLowerCase().indexOf(`</${tag}`, i);
      const end = close === -1 ? src.length : close;
      node.kids.push({ tag: '#raw', text: src.slice(i, end) });
      i = end === src.length ? end : src.indexOf('>', end) + 1;
      continue;
    }
    stack.push(node);
  }
  return root;
}

export function find(node, tag) {
  if (node.tag === tag) return node;
  for (const k of node.kids || []) {
    const hit = find(k, tag);
    if (hit) return hit;
  }
  return null;
}

export function rawTextOf(node) {
  return (node.kids || []).map((k) => k.text || '').join('');
}
