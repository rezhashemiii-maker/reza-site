#!/usr/bin/env node
// ساخت سایت استاتیک از آرتبوردهای src/*.dc.html
//  · قالب‌ها در زمان ساخت پیش‌رندر می‌شوند (محتوا بدون جاوااسکریپت هم خوانا است)
//  · استایل‌های تکراری درجا به کلاس‌های CSS مشترک تبدیل می‌شوند
//  · صفحه‌های تعاملی همان منطق اصلی را با یک رانتایم ~۳ کیلوبایتی اجرا می‌کنند
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { parse, find, rawTextOf } from './parse.mjs';
import { compile, applyClasses } from './compile.mjs';
import { renderToString } from './render.mjs';
import { getPages, STATIC_PAGES } from './pages.mjs';
import { expandPartials } from './partials.mjs';
import { normalizeSiteUrl, metadataTags, withStaticMetadata, encodeText, encodeAttr } from './metadata.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SRC = path.join(root, 'src');
const OUT = process.env.OUTPUT_DIR ? path.resolve(root, process.env.OUTPUT_DIR) : root;
// خروجی جدا نباید پوشهٔ منبع، ابزار یا والد مخزن را بازنویسی کند.
if (OUT !== root) {
  const rel = path.relative(root, OUT);
  const protectedDirs = ['src', 'tools', 'public', '.git', 'assets', 'tests'];
  if (!path.relative(OUT, root).startsWith('..') || protectedDirs.some((name) => rel === name || rel.startsWith(name + path.sep))) {
    throw new Error('OUTPUT_DIR نباید روی منبع یا والد مخزن باشد');
  }
}
fs.mkdirSync(OUT, { recursive: true });

const PAGES = getPages(root);
const PUBLIC_PAGES = [...PAGES, ...STATIC_PAGES];
const MAP = Object.fromEntries(PAGES.map((p) => [p.file, p.out]));
const SITE = normalizeSiteUrl(process.env.SITE_URL || '');
// پیشوند مسیر سایت (برای Pagesِ پروژه‌ای مثل /reza-site/) — فقط در صفحهٔ ۴۰۴ لازم است
const BASE = SITE ? new URL(SITE + '/').pathname : '/';

const FAVICON =
  'data:image/svg+xml,' +
  encodeURIComponent(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">' +
      '<rect width="32" height="32" rx="8" fill="#2F5233"/>' +
      '<text x="16" y="23" font-family="sans-serif" font-size="19" font-weight="bold" ' +
      'fill="#F5F3EE" text-anchor="middle">ر</text></svg>'
  );

// ---------------------------------------------------------------- پاس ۱: پارس و کمپایل

const styleUse = new Map();
const docs = [];

for (const page of PAGES) {
  const src = expandPartials(fs.readFileSync(path.join(SRC, page.file), 'utf8'), page.file, root);
  const tree = parse(src);

  const htmlEl = find(tree, 'html');
  const lang = htmlEl?.attrs.lang || 'fa';
  const dir = htmlEl?.attrs.dir || 'rtl';
  const title = rawTextOf(find(tree, 'title') || { kids: [] }).trim();

  const xdc = find(tree, 'x-dc');
  if (!xdc) throw new Error(`${page.file}: <x-dc> پیدا نشد`);
  const helmet = find(xdc, 'helmet');
  const body = { tag: '#frag', attrs: {}, kids: xdc.kids.filter((k) => k !== helmet) };

  // اسکریپت منطق (اگر باشد)
  let logic = null;
  const findScript = (node) => {
    if (node.tag === 'script' && 'data-dc-script' in node.attrs) return node;
    for (const k of node.kids || []) { const hit = findScript(k); if (hit) return hit; }
    return null;
  };
  const scriptEl = findScript(tree);
  if (scriptEl) logic = rawTextOf(scriptEl).trim();

  // سرِ helmet: لینک‌های فونت جدا، قواعد CSS جدا
  const headLinks = (helmet?.kids || []).filter((k) => k.tag === 'link');
  const helmetCss = (helmet?.kids || [])
    .filter((k) => k.tag === 'style')
    .map(rawTextOf)
    .join('\n')
    .trim();

  const ctx = { styleUse, page: page.out };
  const ast = compile(body, ctx);
  docs.push({ ...page, lang, dir, title, ast, logic, headLinks, helmetCss });
}

// ---------------------------------------------------------------- پاس ۲: نام‌گذاری کلاس‌ها

const NAME = '0123456789abcdefghijklmnopqrstuvwxyz';
const shortName = (n) => {
  let s = '';
  do { s = NAME[n % 36] + s; n = Math.floor(n / 36); } while (n > 0);
  return /^[0-9]/.test(s) ? `s${s}` : s;
};

let counter = 0;
const shared = [];
const perPage = new Map();
const ordered = [...styleUse.entries()].sort((a, b) => b[1].count - a[1].count);
for (const [css, rec] of ordered) {
  if (rec.count < 2) continue;                      // یک‌بارمصرف — درجا می‌ماند
  rec.cls = shortName(counter++);
  // `.x.x` تا ویژگی قاعده از استایل درجای قبلی کم‌تر نشود (مثلاً a:hover)
  const rule = `.${rec.cls}.${rec.cls}{${css}}`;
  if (rec.pages.size > 1) shared.push(rule);
  else {
    const only = [...rec.pages][0];
    if (!perPage.has(only)) perPage.set(only, []);
    perPage.get(only).push(rule);
  }
}
for (const d of docs) applyClasses(d.ast, styleUse);

// ---------------------------------------------------------------- بازنویسی لینک‌ها

const rewriteLinks = (ast) => {
  const visit = (n) => {
    if (typeof n === 'string' || n.h !== undefined) return;
    if (n.a && typeof n.a.href === 'string' && /\.dc\.html(#.*)?$/.test(n.a.href)) {
      const [file, hash = ''] = n.a.href.replace(/^\.?\//, '').split(/(?=#)/);
      if (MAP[file]) n.a.href = (MAP[file] === 'index.html' ? './' : MAP[file]) + hash;
    }
    (n.k || []).forEach(visit);
  };
  ast.forEach(visit);
};
docs.forEach((d) => rewriteLinks(d.ast));

// ---------------------------------------------------------------- CSS مشترک

const baseCssRules = (() => {
  // قواعدی که در همهٔ صفحه‌ها یکسان‌اند → فایل مشترک؛ بقیه → CSS خود صفحه
  const split = (css) => css.split('\n').map((l) => l.trim()).filter(Boolean);
  const counts = new Map();
  for (const d of docs) for (const r of split(d.helmetCss)) counts.set(r, (counts.get(r) || 0) + 1);
  const common = [...counts.entries()].filter(([, c]) => c === docs.length).map(([r]) => r);
  const commonSet = new Set(common);
  for (const d of docs) d.ownCss = split(d.helmetCss).filter((r) => !commonSet.has(r));
  return common;
})();

const RESPONSIVE = [
  '@media (max-width:640px){body{font-size:15px}}',
  'img,svg{max-width:100%}',
  '*{-webkit-tap-highlight-color:rgba(47,82,51,.15)}',
  ':focus-visible{outline:2px solid #2F5233;outline-offset:2px}',
];

fs.mkdirSync(path.join(OUT, 'assets'), { recursive: true });
// خروجی‌های ساخت پیشین پاک می‌شوند تا فایل مرده جا نماند
for (const f of fs.readdirSync(path.join(OUT, 'assets'))) fs.rmSync(path.join(OUT, 'assets', f), { recursive: true });
// فایل‌های دست‌نویس خارج از assets تولیدشده نگه‌داری می‌شوند.
fs.cpSync(path.join(root, 'public/assets'), path.join(OUT, 'assets'), { recursive: true });
fs.copyFileSync(path.join(root, 'tools/dc.js'), path.join(OUT, 'assets/dc.js'));
fs.writeFileSync(
  path.join(OUT, 'assets/site.css'),
  [...baseCssRules, ...RESPONSIVE, ...shared].join('\n') + '\n'
);

// ---------------------------------------------------------------- پاس ۳: رندر و نوشتن

const escapeAttr = encodeAttr;
let report = [];

for (const d of docs) {
  const scopes = [{}];
  let vals = {};
  if (d.logic) {
    const sandbox = {
      console,
      DCLogic: class {
        constructor(props) { this.props = props || {}; this.state = {}; }
        setState() {}
        forceUpdate() {}
      },
    };
    const context = vm.createContext(sandbox);
    new vm.Script(`${d.logic}\n;globalThis.__vals = new Component({}).renderVals();`, {
      filename: d.file,
    }).runInContext(context, { timeout: 5000 });
    vals = context.__vals || {};
  }
  scopes[0] = vals;

  const bodyHtml = renderToString(d.ast, scopes);
  // فقط صفحه‌ای که قالبش واقعاً پویاست به رانتایم نیاز دارد
  const isDynamic = (list) => list.some((n) => {
    if (typeof n === 'string') return false;
    if (n.h !== undefined || n.f !== undefined || n.i !== undefined || n.e) return true;
    if (n.a && Object.values(n.a).some((v) => v && typeof v === 'object')) return true;
    return isDynamic(n.k || []);
  });
  const interactive = Boolean(d.logic) && isDynamic(d.ast);
  const pageCss = [...(perPage.get(d.out) || []), ...d.ownCss];
  const cssFile = pageCss.length ? `assets/${d.out.replace(/\.html$/, '')}.css` : null;
  if (cssFile) fs.writeFileSync(path.join(OUT, cssFile), pageCss.join('\n') + '\n');

  let jsFile = null;
  if (interactive) {
    jsFile = `assets/${d.out.replace(/\.html$/, '')}.js`;
    const ast = JSON.stringify(d.ast);
    fs.writeFileSync(
      path.join(OUT, jsFile),
      `${d.logic}\ndcMount(${ast},Component);\n`
    );
  }

  const links = d.headLinks
    .map((l) => {
      const attrs = (l.order || Object.keys(l.attrs))
        .map((k) => (l.attrs[k] === null || l.attrs[k] === '' ? ` ${k}` : ` ${k}="${escapeAttr(l.attrs[k])}"`))
        .join('');
      return `<link${attrs}>`;
    })
    .join('\n');

  const meta = metadataTags(d, SITE);

  const html = `<!doctype html>
<html lang="${d.lang}" dir="${d.dir}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${encodeText(d.title)}</title>
<meta name="author" content="رضا هاشمی">
${meta}
<link rel="icon" href="${FAVICON}">
${links}
<link rel="stylesheet" href="assets/site.css">${cssFile ? `\n<link rel="stylesheet" href="${cssFile}">` : ''}
</head>
<body>
${interactive ? `<div id="dc-root">${bodyHtml}</div>` : bodyHtml}
${interactive ? `<script src="assets/dc.js" defer></script>\n<script src="${jsFile}" defer></script>` : ''}
</body>
</html>
`;
  fs.writeFileSync(path.join(OUT, d.out), html);
  report.push([d.out, html.length, cssFile ? fs.statSync(path.join(OUT, cssFile)).size : 0, jsFile ? fs.statSync(path.join(OUT, jsFile)).size : 0]);
}

// صفحات مستقل نیز از همان مسیر انتشار و متادیتا عبور می‌کنند.
for (const page of STATIC_PAGES) {
  const source = fs.readFileSync(path.join(root, 'public/pages', page.file), 'utf8');
  fs.writeFileSync(path.join(OUT, page.out), withStaticMetadata(source, page, SITE));
}

const lastModified = (page) => {
  const source = page.file.endsWith('.dc.html') ? `src/${page.file}` : `public/pages/${page.file}`;
  const sources = [source];
  if (page.file.endsWith('.dc.html') && fs.readFileSync(path.join(root, source), 'utf8').includes('<dc-include')) {
    sources.push('src/partials');
  }
  try {
    // تاریخ تغییر منبع، نه تاریخ هر بار ساخت؛ در archive بدون Git، lastmod حذف می‌شود.
    const gitDate = (paths) => execFileSync('git', ['log', '-1', '--format=%cs', '--', ...paths], {
      cwd: root,
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    // برای اولین مهاجرت صفحهٔ مستقل، تاریخ منبع قبلی در ریشه معتبر است.
    const date = gitDate(sources) || (!page.file.endsWith('.dc.html') ? gitDate([page.file]) : '');
    return /^\d{4}-\d{2}-\d{2}$/.test(date) ? `<lastmod>${date}</lastmod>` : '';
  } catch { return ''; }
};

// ---------------------------------------------------------------- نقشهٔ سایت و خروجی گزارش

if (SITE) {
  fs.writeFileSync(
    path.join(OUT, 'sitemap.xml'),
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
      PUBLIC_PAGES.map(
        (p) =>
          `  <url><loc>${encodeText(SITE + '/' + (p.out === 'index.html' ? '' : p.out))}</loc>${lastModified(p)}</url>`
      ).join('\n') +
      `\n</urlset>\n`
  );
  fs.writeFileSync(path.join(OUT, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${SITE}/sitemap.xml\n`);
} else {
  for (const name of ['sitemap.xml', 'robots.txt']) fs.rmSync(path.join(OUT, name), { force: true });
}
fs.writeFileSync(path.join(OUT, '.nojekyll'), '');

// ---------------------------------------------------------------- صفحهٔ ۴۰۴
fs.writeFileSync(
  path.join(OUT, '404.html'),
  `<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>صفحه پیدا نشد — رضا هاشمی</title>
<meta name="robots" content="noindex">
<link rel="icon" href="${FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800&amp;display=swap">
<link rel="stylesheet" href="${BASE}assets/site.css">
</head>
<body>
<main style="max-width:640px;margin:0 auto;padding:22vh 24px;text-align:center">
<p style="font-size:12px;letter-spacing:.12em;font-weight:700;color:#2F5233;margin:0 0 16px">خطای ۴۰۴</p>
<h1 style="font-size:clamp(26px,5vw,40px);font-weight:800;line-height:1.5;margin:0 0 18px">این صفحه این‌جا نیست</h1>
<p style="font-size:16px;line-height:2;color:#4A4F58;margin:0 0 30px">شاید نشانی را اشتباه وارد کرده‌اید یا صفحه جابه‌جا شده است.</p>
<nav style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center">
${PUBLIC_PAGES.map((p) => `<a href="${BASE}${p.out === 'index.html' ? '' : p.out}" style="font-size:14px;font-weight:600;color:#16181C;background:#FFFFFF;border:1px solid #E4E1D6;padding:11px 18px;border-radius:999px">${p.nav}</a>`).join('\n')}
</nav>
</main>
</body>
</html>
`
);

fs.writeFileSync(path.join(OUT, 'manus-routes.json'), JSON.stringify({ routes: PUBLIC_PAGES.map((p) => ({ path: p.out === 'index.html' ? '/' : '/' + p.out, title: p.nav })) }, null, 2) + '\n');

const srcTotal = PAGES.reduce((n, p) => n + fs.statSync(path.join(SRC, p.file)).size, 0);
const outTotal = report.reduce((n, r) => n + r[1] + r[2] + r[3], 0)
  + fs.statSync(path.join(OUT, 'assets/site.css')).size
  + fs.statSync(path.join(OUT, 'assets/dc.js')).size;

console.log('صفحه'.padEnd(18), 'HTML'.padStart(9), 'CSS'.padStart(8), 'JS'.padStart(9));
for (const [name, h, c, j] of report) {
  console.log(name.padEnd(18), String(h).padStart(9), String(c).padStart(8), String(j).padStart(9));
}
console.log('—'.repeat(48));
console.log('site.css'.padEnd(18), String(fs.statSync(path.join(OUT, 'assets/site.css')).size).padStart(9));
console.log('dc.js'.padEnd(18), String(fs.statSync(path.join(OUT, 'assets/dc.js')).size).padStart(9));
console.log(`\nمنبع: ${srcTotal} بایت  →  خروجی: ${outTotal} بایت  (${Math.round((outTotal / srcTotal) * 100)}%)`);
console.log(`کلاس‌های استخراج‌شده: ${counter}  (مشترک ${shared.length})`);
