#!/usr/bin/env node
// ساخت سایت استاتیک از آرتبوردهای src/*.dc.html
//  · قالب‌ها در زمان ساخت پیش‌رندر می‌شوند (محتوا بدون جاوااسکریپت هم خوانا است)
//  · استایل‌های تکراری درجا به کلاس‌های CSS مشترک تبدیل می‌شوند
//  · صفحه‌های تعاملی همان منطق اصلی را با یک رانتایم ~۳ کیلوبایتی اجرا می‌کنند
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
import { parse, find, rawTextOf } from './parse.mjs';
import { compile, applyClasses } from './compile.mjs';
import { renderToString } from './render.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SRC = path.join(root, 'src');
const OUT = root;

const PAGES = [
  { file: 'Main.dc.html', out: 'index.html', nav: 'خانه' },
  { file: 'Services.dc.html', out: 'services.html', nav: 'سرویس‌های فروشنی' },
  { file: 'Library.dc.html', out: 'library.html', nav: 'کتابخانه' },
  { file: 'Chess.dc.html', out: 'chess.html', nav: 'شطرنج' },
  { file: 'AILiteracy.dc.html', out: 'ai-literacy.html', nav: 'سواد هوش مصنوعی' },
  { file: 'Security.dc.html', out: 'security.html', nav: 'کتاب‌های امنیت' },
  { file: 'Literacy.dc.html', out: 'literacy.html', nav: 'سنجش سواد' },
  { file: 'Pattern.dc.html', out: 'pattern.html', nav: 'الگوی پیشرفت' },
  { file: 'Glossary.dc.html', out: 'glossary.html', nav: 'واژه‌نامه' },
  { file: 'Learn.dc.html', out: 'learn.html', nav: 'مسیر یادگیری' },
  { file: 'Ideas.dc.html', out: 'ideas.html', nav: 'ایده‌ها' },
  { file: 'GameTheory.dc.html', out: 'game-theory.html', nav: 'نظریهٔ بازی' },
  { file: 'Patents.dc.html', out: 'patents.html', nav: 'ثبت اختراع' },
  { file: 'Dorrin.dc.html', out: 'dorrin.html', nav: 'مطالعهٔ موردی' },
  { file: 'Demo.dc.html', out: 'demo.html', nav: 'دموی زنده' },
];
// صفحه‌های خودبسنده: HTML کاملی که از خط لولهٔ قالب رد نمی‌شود و همان‌طور که هست منتشر می‌شود.
// منبعشان src/standalone/ است و فقط در نقشهٔ سایت و ناوبری ۴۰۴ دیده می‌شوند.
const STANDALONE = [
  { file: 'iraq.html', out: 'iraq.html', nav: 'پروندهٔ عراق' },
];
const MAP = Object.fromEntries(PAGES.map((p) => [p.file, p.out]));
const SITE = (process.env.SITE_URL || '').replace(/\/$/, '');
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
  const src = fs.readFileSync(path.join(SRC, page.file), 'utf8');
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
// پیشوند ثابت `c`: بدون آن، نامِ عددیِ پیشوندگرفته (۳ → s3) با نامِ پایهٔ ۳۶ِ
// شمارندهٔ ۱۰۱۱ (که خودش «s3» می‌شود) یکی می‌شد و استایل دو عنصر بی‌ربط قاتی می‌شد.
const shortName = (n) => {
  let s = '';
  do { s = NAME[n % 36] + s; n = Math.floor(n / 36); } while (n > 0);
  return `c${s}`;
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
{
  // نگهبان: هیچ دو کلاسی نباید نام یکسان بگیرد
  const names = [...styleUse.values()].filter((r) => r.cls).map((r) => r.cls);
  const dup = names.filter((n, i) => names.indexOf(n) !== i);
  if (dup.length) throw new Error(`نام کلاس تکراری: ${[...new Set(dup)].join(', ')}`);
}

for (const d of docs) applyClasses(d.ast, styleUse);

// ---------------------------------------------------------------- بازنویسی لینک‌ها

const rewriteLinks = (ast) => {
  const visit = (n) => {
    if (typeof n === 'string' || n.h !== undefined) return;
    if (n.a && typeof n.a.href === 'string') {
      // «Foo.dc.html» و «./Foo.dc.html#bookmark» هر دو باید بازنویسی شوند
      const m = /^\.?\/?([A-Za-z0-9_.-]+\.dc\.html)(#.*)?$/.exec(n.a.href);
      if (m && MAP[m[1]]) {
        const target = MAP[m[1]] === 'index.html' ? './' : MAP[m[1]];
        n.a.href = target + (m[2] || '');
      }
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
for (const f of fs.readdirSync(path.join(OUT, 'assets'))) fs.unlinkSync(path.join(OUT, 'assets', f));
fs.copyFileSync(path.join(root, 'tools/dc.js'), path.join(OUT, 'assets/dc.js'));
fs.writeFileSync(
  path.join(OUT, 'assets/site.css'),
  [...baseCssRules, ...RESPONSIVE, ...shared].join('\n') + '\n'
);

// ---------------------------------------------------------------- پاس ۳: رندر و نوشتن

const DESCRIPTIONS = {
  'index.html':
    'رضا هاشمی — یادگیری ماشین را به فارسی می‌نویسم و برای کسب‌وکارها سیستم ثبت داده و تصمیم می‌سازم. هر مفهوم با ارجاع به مقالهٔ اصلی‌اش.',
  'services.html':
    'هفتادوپنج سرویسی که با ابزارهای هوش مصنوعی و بدون دانش کدنویسی زیاد می‌شود ساخت و فروخت — با شش سنجه برای هر سرویس، انتخابگر پنج‌سؤالی، ماشین‌حساب درآمد و ضدفهرست ده چیزی که نباید ساخت.',
  'library.html':
    'کتابخانهٔ یکپارچهٔ منابع سایت: ۱۶۸ کتاب، مقاله، استاندارد و گزارش از ۱۹۱۳ تا ۲۰۲۵، قابل جست‌وجو و فیلتر بر اساس بخش و نوع — با ۱۲۵ پیوند مستقیم به متن اصلی.',
  'chess.html':
    'شطرنج، یادگیری ماشین و نظریهٔ بازی‌ها: از قضیهٔ زرملو (۱۹۱۳) تا ترنسفورمر بدون جست‌وجو (۲۰۲۴) — ۲۵ ایستگاه تاریخی، ۱۴ ارتباط میان شطرنج و یادگیری ماشین، و ۸ ایدهٔ تازه.',
  'ai-literacy.html':
    'معماری سواد هوش مصنوعی در ۱۶ ستون و ۵ لایه: همهٔ آن چیزی که باید بدانی، با ۲۲۰ مفهوم، تقدم یادگیری، خط زمان ۱۲ هفته‌ای و سه سطح عمق برای هر ستون.',
  'security.html':
    'نقشهٔ ۶۱ کتاب، مقاله و استاندارد که معماری امنیت شبکه و اطلاعات را ساختند، کنار ۱۹ حمله و افشاگری که باعثشان شد — از ۱۹۷۳ تا امروز روی یک خط زمان مشترک.',
  'literacy.html':
    'سنجش سواد هوش مصنوعی در ۳۰ سؤال و ۱۰ دقیقه: نیمرخ شش‌بعدی، کارهایی که با دانش امروزت می‌توانی بکنی، و دو قدم بعدی‌ات. بر پایهٔ چارچوب‌های یونسکو، Long و Magerko، و Ng و همکاران.',
  'pattern.html':
    'پروژهٔ تحقیقاتی: الگوی پیشرفت سیندره سورهوس در عدد و نمودار — ۱٬۱۰۰ بستهٔ npm، ۲ میلیارد دانلود در ماه، و شش قاعده‌ای که از داده بیرون آمد.',
  'glossary.html':
    'واژه‌نامهٔ فارسی یادگیری ماشین: ۲۸۵ اصطلاح با معادل انگلیسی، توضیح ساده، مترادف‌های رایج و هشدار اشتباه‌های پرتکرار. قابل جست‌وجو و فیلتر.',
  'learn.html':
    'مسیر یادگیری ماشین در هشت ایستگاه؛ هر ایستگاه فقط به ایستگاه قبلی تکیه می‌کند و مقالهٔ مرجع و تمرین خودش را دارد.',
  'ideas.html':
    'صد ایدهٔ کاربردی یادگیری ماشین در ده حوزه، و کنار هر ایده دقیقاً همان داده‌ای که لازم دارد. قابل جست‌وجو و فیلتر.',
  'game-theory.html':
    'نظریهٔ بازی برای کسی که مدل می‌سازد: تعادل، انگیزه و بازی‌های تکرارشونده، با ارجاع به مقاله‌های اصلی.',
  'patents.html':
    'ثبت اختراع در ایران و بیرون از ایران، از نگاه کسی که سیستم می‌سازد: چه چیزی ثبت‌شدنی است، چه مسیری دارد و چه هزینه‌ای.',
  'dorrin.html':
    'مطالعهٔ موردی دُرّین: سیستم ثبت و تصمیم برای یک واحد پرورش قارچ — از ثبت دمای کمپوست تا سود هر سالن.',
  'demo.html':
    'دموی زندهٔ سامانهٔ پایش سالن‌های پرورش قارچ: فاز رشد، دما، رطوبت، دی‌اکسید کربن، برداشت و اقتصاد هر فلاش.',
};

const escapeAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
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
    }).runInContext(context);
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

  const canonical = SITE ? `\n<link rel="canonical" href="${SITE}/${d.out === 'index.html' ? '' : d.out}">` : '';
  const desc = DESCRIPTIONS[d.out] || '';

  const html = `<!doctype html>
<html lang="${d.lang}" dir="${d.dir}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${d.title}</title>
<meta name="description" content="${escapeAttr(desc)}">
<meta name="author" content="رضا هاشمی">
<meta property="og:type" content="website">
<meta property="og:locale" content="fa_IR">
<meta property="og:title" content="${escapeAttr(d.title)}">
<meta property="og:description" content="${escapeAttr(desc)}">
<link rel="icon" href="${FAVICON}">${canonical}
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

// ---------------------------------------------------------------- نقشهٔ سایت و خروجی گزارش

if (SITE) {
  const today = new Date().toISOString().slice(0, 10);
  fs.writeFileSync(
    path.join(OUT, 'sitemap.xml'),
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
      [...PAGES, ...STANDALONE].map(
        (p) =>
          `  <url><loc>${SITE}/${p.out === 'index.html' ? '' : p.out}</loc><lastmod>${today}</lastmod></url>`
      ).join('\n') +
      `\n</urlset>\n`
  );
  fs.writeFileSync(path.join(OUT, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${SITE}/sitemap.xml\n`);
}
// ---------------------------------------------------------------- صفحه‌های خودبسنده
for (const sa of STANDALONE) {
  fs.copyFileSync(path.join(SRC, 'standalone', sa.file), path.join(OUT, sa.out));
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
${[...PAGES, ...STANDALONE].map((p) => `<a href="${BASE}${p.out === 'index.html' ? '' : p.out}" style="font-size:14px;font-weight:600;color:#16181C;background:#FFFFFF;border:1px solid #E4E1D6;padding:11px 18px;border-radius:999px">${p.nav}</a>`).join('\n')}
</nav>
</main>
</body>
</html>
`
);

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
