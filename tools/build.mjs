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
  { file: 'Logic.dc.html', out: 'logic.html', nav: 'منطق برنامه‌نویسی' },
  { file: 'Foundations.dc.html', out: 'foundations.html', nav: 'مبانی ریاضی' },
  { file: 'Music.dc.html', out: 'music.html', nav: 'ریاضیات موسیقی' },
  { file: 'Sets.dc.html', out: 'sets.html', nav: 'نظریهٔ مجموعه‌ها' },
  { file: 'AgriInvest.dc.html', out: 'agri-invest.html', nav: 'سرمایه‌گذاری کشاورزی' },
  { file: 'Plain.dc.html', out: 'plain.html', nav: 'برنامه‌نویسی به زبان ساده' },
  { file: 'Watch.dc.html', out: 'watch.html', nav: 'رصدخانه' },
  { file: 'Workshop.dc.html', out: 'workshop.html', nav: 'کارگاه' },
  { file: 'Higgsfield.dc.html', out: 'higgsfield.html', nav: 'هیگزفیلد', sub: true },
  { file: 'Math.dc.html', out: 'math.html', nav: 'ریاضیات هوش مصنوعی' },
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
  { file: 'AiEngineer.dc.html', out: 'ai-engineer.html', nav: 'مهندس هوش مصنوعی' },
  { file: 'SecBook01.dc.html', out: 'sec-book-01.html', nav: 'کتاب 1', sub: true },
  { file: 'SecBook02.dc.html', out: 'sec-book-02.html', nav: 'کتاب 2', sub: true },
  { file: 'SecBook03.dc.html', out: 'sec-book-03.html', nav: 'کتاب 3', sub: true },
  { file: 'SecBook04.dc.html', out: 'sec-book-04.html', nav: 'کتاب 4', sub: true },
  { file: 'SecBook05.dc.html', out: 'sec-book-05.html', nav: 'کتاب 5', sub: true },
  { file: 'SecBook06.dc.html', out: 'sec-book-06.html', nav: 'کتاب 6', sub: true },
  { file: 'SecBook07.dc.html', out: 'sec-book-07.html', nav: 'کتاب 7', sub: true },
  { file: 'SecBook08.dc.html', out: 'sec-book-08.html', nav: 'کتاب 8', sub: true },
  { file: 'SecBook09.dc.html', out: 'sec-book-09.html', nav: 'کتاب 9', sub: true },
  { file: 'SecBook10.dc.html', out: 'sec-book-10.html', nav: 'کتاب 10', sub: true },
  { file: 'SecBook11.dc.html', out: 'sec-book-11.html', nav: 'کتاب 11', sub: true },
  { file: 'SecBook12.dc.html', out: 'sec-book-12.html', nav: 'کتاب 12', sub: true },
  { file: 'SecBook13.dc.html', out: 'sec-book-13.html', nav: 'کتاب 13', sub: true },
  { file: 'SecBook14.dc.html', out: 'sec-book-14.html', nav: 'کتاب 14', sub: true },
  { file: 'SecBook15.dc.html', out: 'sec-book-15.html', nav: 'کتاب 15', sub: true },
  { file: 'Aie101.dc.html', out: 'aie-101.html', nav: 'پروژهٔ 1.1', sub: true },
  { file: 'Aie102.dc.html', out: 'aie-102.html', nav: 'پروژهٔ 1.2', sub: true },
  { file: 'Aie103.dc.html', out: 'aie-103.html', nav: 'پروژهٔ 1.3', sub: true },
  { file: 'Aie104.dc.html', out: 'aie-104.html', nav: 'پروژهٔ 1.4', sub: true },
  { file: 'Aie105.dc.html', out: 'aie-105.html', nav: 'پروژهٔ 1.5', sub: true },
  { file: 'Aie106.dc.html', out: 'aie-106.html', nav: 'پروژهٔ 1.6', sub: true },
  { file: 'Aie107.dc.html', out: 'aie-107.html', nav: 'پروژهٔ 1.7', sub: true },
  { file: 'Aie108.dc.html', out: 'aie-108.html', nav: 'پروژهٔ 1.8', sub: true },
  { file: 'Aie109.dc.html', out: 'aie-109.html', nav: 'پروژهٔ 1.9', sub: true },
  { file: 'Aie110.dc.html', out: 'aie-110.html', nav: 'پروژهٔ 1.10', sub: true },
  { file: 'Aie201.dc.html', out: 'aie-201.html', nav: 'پروژهٔ 2.1', sub: true },
  { file: 'Aie202.dc.html', out: 'aie-202.html', nav: 'پروژهٔ 2.2', sub: true },
  { file: 'Aie203.dc.html', out: 'aie-203.html', nav: 'پروژهٔ 2.3', sub: true },
  { file: 'Aie204.dc.html', out: 'aie-204.html', nav: 'پروژهٔ 2.4', sub: true },
  { file: 'Aie205.dc.html', out: 'aie-205.html', nav: 'پروژهٔ 2.5', sub: true },
  { file: 'Aie206.dc.html', out: 'aie-206.html', nav: 'پروژهٔ 2.6', sub: true },
  { file: 'Aie207.dc.html', out: 'aie-207.html', nav: 'پروژهٔ 2.7', sub: true },
  { file: 'Aie208.dc.html', out: 'aie-208.html', nav: 'پروژهٔ 2.8', sub: true },
  { file: 'Aie209.dc.html', out: 'aie-209.html', nav: 'پروژهٔ 2.9', sub: true },
  { file: 'Aie210.dc.html', out: 'aie-210.html', nav: 'پروژهٔ 2.10', sub: true },
  { file: 'Aie301.dc.html', out: 'aie-301.html', nav: 'پروژهٔ 3.1', sub: true },
  { file: 'Aie302.dc.html', out: 'aie-302.html', nav: 'پروژهٔ 3.2', sub: true },
  { file: 'Aie303.dc.html', out: 'aie-303.html', nav: 'پروژهٔ 3.3', sub: true },
  { file: 'Aie304.dc.html', out: 'aie-304.html', nav: 'پروژهٔ 3.4', sub: true },
  { file: 'Aie305.dc.html', out: 'aie-305.html', nav: 'پروژهٔ 3.5', sub: true },
  { file: 'Aie306.dc.html', out: 'aie-306.html', nav: 'پروژهٔ 3.6', sub: true },
  { file: 'Aie307.dc.html', out: 'aie-307.html', nav: 'پروژهٔ 3.7', sub: true },
  { file: 'Aie308.dc.html', out: 'aie-308.html', nav: 'پروژهٔ 3.8', sub: true },
  { file: 'Aie309.dc.html', out: 'aie-309.html', nav: 'پروژهٔ 3.9', sub: true },
  { file: 'Aie310.dc.html', out: 'aie-310.html', nav: 'پروژهٔ 3.10', sub: true },
  { file: 'Aie401.dc.html', out: 'aie-401.html', nav: 'پروژهٔ 4.1', sub: true },
  { file: 'Aie402.dc.html', out: 'aie-402.html', nav: 'پروژهٔ 4.2', sub: true },
  { file: 'Aie403.dc.html', out: 'aie-403.html', nav: 'پروژهٔ 4.3', sub: true },
  { file: 'Aie404.dc.html', out: 'aie-404.html', nav: 'پروژهٔ 4.4', sub: true },
  { file: 'Aie405.dc.html', out: 'aie-405.html', nav: 'پروژهٔ 4.5', sub: true },
  { file: 'Aie406.dc.html', out: 'aie-406.html', nav: 'پروژهٔ 4.6', sub: true },
  { file: 'Aie407.dc.html', out: 'aie-407.html', nav: 'پروژهٔ 4.7', sub: true },
  { file: 'Aie408.dc.html', out: 'aie-408.html', nav: 'پروژهٔ 4.8', sub: true },
  { file: 'Aie409.dc.html', out: 'aie-409.html', nav: 'پروژهٔ 4.9', sub: true },
  { file: 'Aie410.dc.html', out: 'aie-410.html', nav: 'پروژهٔ 4.10', sub: true },
  { file: 'Aie501.dc.html', out: 'aie-501.html', nav: 'پروژهٔ 5.1', sub: true },
  { file: 'Aie502.dc.html', out: 'aie-502.html', nav: 'پروژهٔ 5.2', sub: true },
  { file: 'Aie503.dc.html', out: 'aie-503.html', nav: 'پروژهٔ 5.3', sub: true },
  { file: 'Aie504.dc.html', out: 'aie-504.html', nav: 'پروژهٔ 5.4', sub: true },
  { file: 'Aie505.dc.html', out: 'aie-505.html', nav: 'پروژهٔ 5.5', sub: true },
  { file: 'Aie506.dc.html', out: 'aie-506.html', nav: 'پروژهٔ 5.6', sub: true },
  { file: 'Aie507.dc.html', out: 'aie-507.html', nav: 'پروژهٔ 5.7', sub: true },
  { file: 'Aie508.dc.html', out: 'aie-508.html', nav: 'پروژهٔ 5.8', sub: true },
  { file: 'Aie509.dc.html', out: 'aie-509.html', nav: 'پروژهٔ 5.9', sub: true },
  { file: 'Aie510.dc.html', out: 'aie-510.html', nav: 'پروژهٔ 5.10', sub: true },
  { file: 'Aie601.dc.html', out: 'aie-601.html', nav: 'پروژهٔ 6.1', sub: true },
  { file: 'Aie602.dc.html', out: 'aie-602.html', nav: 'پروژهٔ 6.2', sub: true },
  { file: 'Aie603.dc.html', out: 'aie-603.html', nav: 'پروژهٔ 6.3', sub: true },
  { file: 'Aie604.dc.html', out: 'aie-604.html', nav: 'پروژهٔ 6.4', sub: true },
  { file: 'Aie605.dc.html', out: 'aie-605.html', nav: 'پروژهٔ 6.5', sub: true },
  { file: 'Aie606.dc.html', out: 'aie-606.html', nav: 'پروژهٔ 6.6', sub: true },
  { file: 'Aie607.dc.html', out: 'aie-607.html', nav: 'پروژهٔ 6.7', sub: true },
  { file: 'Aie608.dc.html', out: 'aie-608.html', nav: 'پروژهٔ 6.8', sub: true },
  { file: 'Aie609.dc.html', out: 'aie-609.html', nav: 'پروژهٔ 6.9', sub: true },
  { file: 'Aie610.dc.html', out: 'aie-610.html', nav: 'پروژهٔ 6.10', sub: true },
  // آینه‌های آرتیفکت: همان محتوای بخش‌های صفحهٔ اصلی، در قالب صفحهٔ جدا.
  // برای همگامی با آرتیفکت نگه داشته می‌شوند و noindex دارند تا با index.html رقابت نکنند.
  { file: 'Writing.dc.html', out: 'writing.html', nav: 'نوشته‌ها', mirror: true },
  { file: 'Books.dc.html', out: 'books.html', nav: 'کتاب‌ها' },
];
// صفحه‌های خودبسنده: HTML کاملی که از خط لولهٔ قالب رد نمی‌شود و همان‌طور که هست منتشر می‌شود.
// منبعشان src/standalone/ است و فقط در نقشهٔ سایت و ناوبری ۴۰۴ دیده می‌شوند.
const STANDALONE = [
  { file: 'iraq.html', out: 'iraq.html', nav: 'پروندهٔ عراق' },
];
const MAP = Object.fromEntries(PAGES.map((p) => [p.file, p.out]));
// آرتبوردهایی که در مخزن قالب دیگری دارند: «پروندهٔ عراق» این‌جا صفحهٔ خودبسنده است،
// پس پیوندهای Iraq.dc.html که از آرتیفکت آمده‌اند باید به همان فایل برسند.
for (const s of STANDALONE) MAP[s.file.replace(/\.html$/, '.dc.html').replace(/^./, (c) => c.toUpperCase())] = s.out;
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


// ---------------------------------------------------------------- نوار تب‌های سراسری
// همان نوار بالای صفحهٔ اصلی، ولی روی هر صفحهٔ سایت. چون صفحه‌ها از ژنراتورهای
// مختلف می‌آیند، این‌جا موقع ساخت تزریق می‌شود نه در تک‌تک قالب‌ها.
const TABS = [
  { label: 'شروع',     href: 'index.html',         anchor: '#home' },
  { label: 'نوشته‌ها',  href: 'index.html#writing', anchor: '#writing' },
  { label: 'کتاب‌ها',   href: 'books.html',         anchor: null },
  { label: 'رصدخانه',  href: 'watch.html',         anchor: null },
];
// صفحه‌هایی که تب دیگری را روشن می‌کنند (آینه‌ها و زیرصفحه‌ها)
const TAB_ALIAS = {
  'writing.html': 'index.html#writing',
};
for (let i = 1; i <= 15; i++) TAB_ALIAS[`sec-book-${String(i).padStart(2, '0')}.html`] = 'books.html';

const TABS_CSS = [
  '.stabs{background:#FFFFFF;border-bottom:1px solid #E4E1D6}',
  '.stabs-in{max-width:1120px;margin:0 auto;padding:7px 16px;display:flex;align-items:center;gap:5px;flex-wrap:wrap}',
  '.stabs-brand{display:inline-flex;align-items:center;gap:8px;font-weight:800;font-size:14px;color:#16181C;margin-inline-end:8px;text-decoration:none}',
  '.stabs-brand span{width:9px;height:9px;border-radius:50%;background:#2F5233;flex-shrink:0}',
  '.stab{font-size:13px;color:#4A4F58;padding:6px 11px;border-radius:999px;text-decoration:none;white-space:nowrap}',
  '.stab:hover{background:#F0EEE7;color:#16181C;text-decoration:none}',
  '.stab[aria-current]{background:#2F5233;color:#FFFFFF;font-weight:700}',
  // روی دسکتاپ نوار می‌چسبد و هدرِ خودِ صفحه زیرش می‌نشیند؛ روی گوشی نمی‌چسبد
  // تا دو نوارِ چسبان نیمی از نما را نگیرند.
  '@media (min-width:861px){.stabs{position:sticky;top:0;z-index:60}body header{top:43px !important}[id]{scroll-margin-top:122px !important}}',
  '@media (max-width:860px){.stabs-in{padding:6px 12px;gap:3px}.stabs-brand{font-size:13px;margin-inline-end:5px}.stab{font-size:12.5px;padding:5px 9px}}',
];

const siteTabs = (out, base = '') => {
  const active = TAB_ALIAS[out] || out;
  const items = TABS.map((t) => {
    const self = out === 'index.html' && t.anchor;
    const href = self ? t.anchor : base + t.href;
    const on = self ? t.href === 'index.html' : active === t.href || (out === 'index.html' && t.href === 'index.html');
    return `<a class="stab" href="${href}"${on ? ' aria-current="page"' : ''}>${t.label}</a>`;
  }).join('');
  return `<nav class="stabs" aria-label="منوی اصلی"><div class="stabs-in"><a class="stabs-brand" href="${base}index.html"><span></span>رضا هاشمی</a>${items}</div></nav>`;
};

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
  [...baseCssRules, ...RESPONSIVE, ...TABS_CSS, ...shared].join('\n') + '\n'
);

// ---------------------------------------------------------------- پاس ۳: رندر و نوشتن

// توضیح متای صفحه‌های منتقل‌شده از آرتیفکت، تولیدشده با tools/port (اگر بود)
const AUTO_DESC = (() => {
  const out = {};
  for (const n of ['descriptions.auto.json', 'descriptions.books.json']) {
    const f = path.join(SRC, n);
    if (fs.existsSync(f)) Object.assign(out, JSON.parse(fs.readFileSync(f, 'utf8')));
  }
  return out;
})();

const DESCRIPTIONS = {
  'index.html':
    'رضا هاشمی — یادگیری ماشین را به فارسی می‌نویسم و برای کسب‌وکارها سیستم ثبت داده و تصمیم می‌سازم. هر مفهوم با ارجاع به مقالهٔ اصلی‌اش.',
  'books.html':
    'پانزده کتاب امنیت که معماری این رشته را ساختند، از ۱۹۹۴ تا ۲۰۲۰. برای هر کتاب: چرا مهم است، داخلش چیست، چه چیزی کهنه شده و چه چیزی نشده.',
  'logic.html':
    'اصول و منطق برنامه‌نویسی از صفر، در قالب نامه‌ای به ابوریحان بیرونی: متغیر، شرط، حلقه، تابع، داده‌ساختار، دودویی و بازگشت — با تمثیل‌های هزار سال پیش و بدون واژهٔ تخصصی.',
  'watch.html':
    'رصدخانه — دفترِ روزانهٔ آنچه در هوش مصنوعی اتفاق می‌افتد: مدل تازه، قابلیت تازه، پرونده، عدد و حاشیه. بالای هر رصد نوشته شده از کجا آمده و چقدر می‌شود باورش کرد.',
  'foundations.html':
    'مبانی ریاضی از راهی دیگر: هر مفهوم وقتی ساخته شد که چیزی شکست. ده قاعدهٔ بی‌دلیل، فرمول‌خوانی، بی‌نهایت، احتمال، تمرین انتزاع، و ۳۱ کتاب به ترتیبِ خواندن.',
  'music.html':
    'ریاضیاتِ موسیقی در دو قصه و دوازده شب، برای بلند خواندن پیش از خواب: از لرزش تا اکتاو، پنجم، کمای فیثاغورسی و دروغِ کوچکِ پیانو، و بعد ضرب‌آهنگ، نصف‌کردنِ وقت و سه روی دو — با صدا.',
  'sets.html':
    'نظریهٔ مجموعه‌ها در ده پرده: چه چیزی کانتور را مجبور کرد واردِ بی‌نهایت شود، چطور پارادوکسِ راسل ریاضی را تا یک قدمِ فروپاشی برد، و چرا دیتابیس و احتمال روی همین قصه ایستاده‌اند.',
  'agri-invest.html':
    'داشبورد تعاملی سرمایه‌گذاری در کشاورزی: بازده، دورهٔ بازگشت و حساسیت به قیمت در ۱۹ فعالیت، با مدل وام ده‌ساله که نشان می‌دهد تورم معادلهٔ سود را چطور عوض می‌کند.',
  'plain.html':
    'منطق برنامه‌نویسی به زبان امروز و برای آدم معمولی: برنامه، متغیر، شرط، حلقه، تابع، فهرست و خطا — با مثال گوشی و آسانسور و سبد خرید، و یک برنامهٔ کامل خط‌به‌خط.',
  'workshop.html':
    'کارگاه — راهنمای کاملِ ابزارهای کاربردی، از صفر. نه معرفی و نه فهرست قابلیت‌ها: وارد که شدی، این دکمه‌ای که جلویت است برای چیست.',
  'higgsfield.html':
    'راهنمای کامل هیگزفیلد از صفر: نقشهٔ کاملِ رابط، هر بخش و هر دکمه، اعتبار و جایی که هدر می‌رود، تصویر و ویدئو و سینما و بازاریابی، و دستور کارِ روز اول.',
  'math.html':
    'مبانی ریاضی و آماری هوش مصنوعی از صفر، در نامهٔ دومی به ابوریحان بیرونی: شمردن، احتمال، قضیهٔ بیز، کمترین مربعات، سراشیبی و آنتروپی — از الکندی و خوارزمی تا پرسپترون.',
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
  // تخته‌هایی مثل داشبورد کشاورزی حفرهٔ {{...}} ندارند و همهٔ کارشان را در
  // componentDidMount با DOM انجام می‌دهند؛ این‌ها هم به زمان اجرا نیاز دارند.
  const domDriven = /componentDidMount\s*\(/.test(d.logic || '');
  const interactive = Boolean(d.logic) && (isDynamic(d.ast) || domDriven);
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
  const desc = DESCRIPTIONS[d.out] || AUTO_DESC[d.out] || '';
  // صفحه‌های آینه همان محتوای بخش‌های index.html را دارند؛ ایندکس‌شدنشان
  // یعنی دو نشانی برای یک متن. پیوندهایشان دنبال می‌شود، خودشان نه.
  const robots = d.mirror ? '\n<meta name="robots" content="noindex,follow">' : '';

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
<link rel="icon" href="${FAVICON}">${canonical}${robots}
${links}
<link rel="stylesheet" href="assets/site.css">${cssFile ? `\n<link rel="stylesheet" href="${cssFile}">` : ''}
</head>
<body>
${bodyHtml.includes('class="navbar"') ? '' : siteTabs(d.out)}
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
      [...PAGES.filter((p) => !p.mirror), ...STANDALONE].map(
        (p) =>
          `  <url><loc>${SITE}/${p.out === 'index.html' ? '' : p.out}</loc><lastmod>${today}</lastmod></url>`
      ).join('\n') +
      `\n</urlset>\n`
  );
  fs.writeFileSync(path.join(OUT, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${SITE}/sitemap.xml\n`);
}
// ---------------------------------------------------------------- صفحه‌های خودبسنده
for (const sa of STANDALONE) {
  let raw = fs.readFileSync(path.join(SRC, 'standalone', sa.file), 'utf8');
  // این صفحه از خط لولهٔ قالب رد نمی‌شود، پس CSS نوار را هم باید همراهش برد
  // قاعدهٔ چسبندگیِ دسکتاپ بازنویسی می‌شود: این صفحه هدرِ چسبانِ خودش را ندارد
  const tabCss = `<style>${TABS_CSS.filter((r) => !r.startsWith('@media (min-width')).join('')}`
    + '@media (min-width:861px){.stabs{position:sticky;top:0;z-index:60}}</style>';
  raw = raw.replace('</head>', `${tabCss}</head>`).replace('<body>', `<body>\n${siteTabs(sa.out)}`);
  fs.writeFileSync(path.join(OUT, sa.out), raw);
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
${[...PAGES.filter((p) => !p.sub), ...STANDALONE].map((p) => `<a href="${BASE}${p.out === 'index.html' ? '' : p.out}" style="font-size:14px;font-weight:600;color:#16181C;background:#FFFFFF;border:1px solid #E4E1D6;padding:11px 18px;border-radius:999px">${p.nav}</a>`).join('\n')}
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
