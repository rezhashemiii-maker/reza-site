#!/usr/bin/env node
// بررسی‌کنندهٔ خروجی استاتیک سایت؛ فقط از parser داخلی پروژه استفاده می‌کند.
// محدودیت parser: برای HTML تولیدشده مناسب است، نه HTML دلخواه با نحو بسیار نامعمول.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { find, parse, rawTextOf } from './parse.mjs';
import { getPages, STATIC_PAGES } from './pages.mjs';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const outputDir = path.resolve(process.cwd(), process.argv[2] || '.');
const issues = [];
const expectedPages = [...getPages(repoRoot), ...STATIC_PAGES].map((page) => page.out).sort();

function fail(message) {
  issues.push(message);
}

function attr(node, name) {
  const wanted = name.toLowerCase();
  for (const [key, value] of Object.entries(node.attrs || {})) {
    if (key.toLowerCase() === wanted) return value;
  }
  return undefined;
}

function hasToken(value, token) {
  return String(value || '').toLowerCase().split(/\s+/).includes(token.toLowerCase());
}

function walk(node, visitor) {
  visitor(node);
  for (const child of node.kids || []) walk(child, visitor);
}

function nodesByTag(tree, tag) {
  const nodes = [];
  walk(tree, (node) => {
    if (node.tag === tag) nodes.push(node);
  });
  return nodes;
}

function metaContent(tree, property, value) {
  for (const node of nodesByTag(tree, 'meta')) {
    if (attr(node, property) === value) return attr(node, 'content');
  }
  return undefined;
}

function nonEmpty(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function parseSiteUrl(input) {
  const raw = String(input || '').trim();
  if (!raw) return null;
  try {
    const url = new URL(raw);
    if (!/^https?:$/.test(url.protocol) || url.username || url.password || url.search || url.hash) throw new Error('طرح یا جزء اضافی نامعتبر است');
    url.pathname = url.pathname.replace(/\/+$/, '');
    return {
      href: url.toString().replace(/\/$/, ''),
      origin: url.origin,
      basePath: `${url.pathname || ''}/`.replace(/^([^/])/, '/$1'),
    };
  } catch (error) {
    fail(`SITE_URL نامعتبر است: ${raw || '(خالی)'} (${error.message})`);
    return null;
  }
}

const indexPath = path.join(outputDir, 'index.html');
let inferredSite = '';
if (!Object.hasOwn(process.env, 'SITE_URL') && fs.existsSync(indexPath)) {
  const tree = parse(fs.readFileSync(indexPath, 'utf8'));
  const canonical = nodesByTag(tree, 'link').find((node) => hasToken(attr(node, 'rel'), 'canonical'));
  inferredSite = attr(canonical || { attrs: {} }, 'href') || '';
}
const site = parseSiteUrl(process.env.SITE_URL ?? inferredSite);
const basePath = site?.basePath || '/';

function expectedCanonical(file) {
  if (!site) return null;
  return `${site.href}/${file === 'index.html' ? '' : file}`;
}

function isExternalReference(ref) {
  return /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(ref);
}

function pageVirtualUrl(file) {
  const prefix = site?.basePath || '/';
  return new URL(`${prefix}${file}`, 'https://site-check.invalid');
}

function normalisePathname(pathname) {
  const decoded = decodeURIComponent(pathname);
  const normal = path.posix.normalize(decoded).replace(/^\/+/, '');
  if (!normal || normal === '.') return 'index.html';
  return normal.endsWith('/') ? `${normal}index.html` : normal;
}

// فقط ارجاع‌های واقعاً محلی را به نام فایل خروجی تبدیل می‌کند.
// undefined یعنی URL بیرونی یا scheme غیرقابل‌بررسی (mailto، data، javascript و ...).
function localTarget(ref, fromFile, label) {
  const value = String(ref || '').trim();
  if (!value || /^(?:data|javascript):/i.test(value)) return null;
  if (value.startsWith('#')) return { file: fromFile, fragment: value.slice(1) };

  let url;
  try {
    url = new URL(value, pageVirtualUrl(fromFile));
  } catch {
    fail(`${fromFile}: ${label} نشانی نامعتبر دارد: ${value}`);
    return null;
  }

  if (url.origin !== 'https://site-check.invalid') {
    if (site && url.origin === site.origin) {
      if (!url.pathname.startsWith(site.basePath)) {
        fail(`${fromFile}: ${label} باید با پیشوند ${site.basePath} شروع شود: ${value}`);
        return null;
      }
      return { file: normalisePathname(url.pathname.slice(site.basePath.length)), fragment: url.hash.slice(1) };
    }
    return null;
  }

  if (value.startsWith('/')) {
    if (site && !url.pathname.startsWith(site.basePath)) {
      fail(`${fromFile}: ${label} مسیر مطلق بدون پیشوند ${site.basePath} دارد: ${value}`);
      return null;
    }
    const relative = site ? url.pathname.slice(site.basePath.length) : url.pathname;
    return { file: normalisePathname(relative), fragment: url.hash.slice(1) };
  }

  return { file: normalisePathname(url.pathname.slice(basePath.length)), fragment: url.hash.slice(1) };
}

function readOutput(file) {
  const absolute = path.resolve(outputDir, file);
  if (absolute !== outputDir && !absolute.startsWith(`${outputDir}${path.sep}`)) return null;
  return fs.existsSync(absolute) && fs.statSync(absolute).isFile() ? absolute : null;
}

function checkLocalReference(ref, fromFile, label, pages) {
  if (String(ref || '').trim() === '#') {
    fail(`${fromFile}: ${label} لینک موقت # است؛ مقصد مشخص یا id واقعی ابتدای صفحه را استفاده کنید`);
    return;
  }
  const target = localTarget(ref, fromFile, label);
  if (!target) return;
  const targetPath = readOutput(target.file);
  if (!targetPath) {
    fail(`${fromFile}: ${label} به فایلِ موجود اشاره نمی‌کند: ${ref}`);
    return;
  }
  if (!target.fragment) return;

  const targetPage = pages.get(target.file);
  // لینک‌های HTML پیش‌رندرشده باید مقصد واقعی داشته باشند؛ متن JavaScript پارس نمی‌شود.
  if (!targetPage?.ids.has(decodeURIComponent(target.fragment))) {
    fail(`${fromFile}: fragment #${target.fragment} در ${target.file} پیدا نشد`);
  }
}

function checkDocumentStructure(page, pages) {
  const { file, tree } = page;
  const html = find(tree, 'html');
  if (!html) {
    fail(`${file}: عنصر html پیدا نشد`);
    return;
  }
  if (attr(html, 'lang') !== 'fa') fail(`${file}: lang باید fa باشد`);
  if (attr(html, 'dir') !== 'rtl') fail(`${file}: dir باید rtl باشد`);

  const title = rawTextOf(find(tree, 'title') || { kids: [] }).trim();
  if (!title) fail(`${file}: title خالی یا غایب است`);

  const description = metaContent(tree, 'name', 'description');
  if (!nonEmpty(description)) fail(`${file}: meta description خالی یا غایب است`);
  if (nodesByTag(tree, 'h1').length === 0) fail(`${file}: دست‌کم یک h1 لازم است`);

  if (site) {
    const canonical = nodesByTag(tree, 'link').find((node) => hasToken(attr(node, 'rel'), 'canonical'));
    const expected = expectedCanonical(file);
    if (!canonical || attr(canonical, 'href') !== expected) {
      fail(`${file}: canonical باید دقیقاً ${expected} باشد`);
    }
  }

  // بدون SITE_URL، build عمداً URL و تصویر مطلق اجتماعی تولید نمی‌کند تا نشانی ساختگی نسازد.
  const commonOg = ['og:type', 'og:locale', 'og:site_name', 'og:title', 'og:description'];
  const requiredOg = site ? [...commonOg, 'og:url', 'og:image'] : commonOg;
  for (const property of requiredOg) {
    if (!nonEmpty(metaContent(tree, 'property', property))) fail(`${file}: ${property} خالی یا غایب است`);
  }
  if (site && metaContent(tree, 'property', 'og:url') !== expectedCanonical(file)) {
    fail(`${file}: og:url باید دقیقاً ${expectedCanonical(file)} باشد`);
  }

  const requiredTwitter = site
    ? ['twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']
    : ['twitter:card', 'twitter:title', 'twitter:description'];
  for (const name of requiredTwitter) {
    if (!nonEmpty(metaContent(tree, 'name', name))) fail(`${file}: ${name} خالی یا غایب است`);
  }

  const image = metaContent(tree, 'property', 'og:image');
  if (site && nonEmpty(image)) checkLocalReference(image, file, 'og:image', pages);

  if (page.source.includes('[لینک GitHub]') || page.source.includes('[لینک LinkedIn]')) {
    fail(`${file}: placeholder شبکهٔ اجتماعی باقی مانده است`);
  }
}

function checkReferences(page, pages) {
  const { file, tree } = page;
  for (const node of nodesByTag(tree, 'a')) {
    const href = attr(node, 'href');
    if (href !== undefined) checkLocalReference(href, file, 'href', pages);
  }
  for (const node of nodesByTag(tree, 'script')) {
    const src = attr(node, 'src');
    if (src !== undefined) checkLocalReference(src, file, 'script src', pages);
  }
  for (const node of nodesByTag(tree, 'link')) {
    if (!hasToken(attr(node, 'rel'), 'stylesheet')) continue;
    const href = attr(node, 'href');
    if (href !== undefined) checkLocalReference(href, file, 'stylesheet href', pages);
  }
}

function check404(page, pages) {
  if (!page) {
    fail('404.html در خروجی وجود ندارد');
    return;
  }
  const robots = metaContent(page.tree, 'name', 'robots');
  if (!/\bnoindex\b/i.test(String(robots || ''))) fail('404.html باید meta robots با noindex داشته باشد');
  checkReferences(page, pages);
}

if (!fs.existsSync(outputDir) || !fs.statSync(outputDir).isDirectory()) {
  fail(`پوشهٔ خروجی پیدا نشد: ${outputDir}`);
} else {
  const htmlFiles = fs.readdirSync(outputDir)
    .filter((file) => file.endsWith('.html'))
    .sort();
  const publicFiles = htmlFiles.filter((file) => file !== '404.html');

  for (const file of expectedPages) {
    if (!publicFiles.includes(file)) fail(`صفحهٔ رسمی ${file} در خروجی پیدا نشد`);
  }
  for (const file of publicFiles) {
    if (!expectedPages.includes(file)) fail(`صفحهٔ ${file} خارج از فهرست رسمی ساخت است`);
  }

  const pages = new Map();
  for (const file of htmlFiles) {
    const source = fs.readFileSync(path.join(outputDir, file), 'utf8');
    const tree = parse(source);
    const ids = new Set();
    walk(tree, (node) => {
      const id = attr(node, 'id');
      if (nonEmpty(id)) ids.add(id);
    });
    pages.set(file, {
      file,
      source,
      tree,
      ids,
      hasScript: nodesByTag(tree, 'script').length > 0,
    });
  }

  for (const file of publicFiles) checkDocumentStructure(pages.get(file), pages);
  for (const file of publicFiles) checkReferences(pages.get(file), pages);
  check404(pages.get('404.html'), pages);

  if (site) {
    const sitemapPath = path.join(outputDir, 'sitemap.xml');
    const robotsPath = path.join(outputDir, 'robots.txt');
    if (!fs.existsSync(sitemapPath)) {
      fail('sitemap.xml در خروجی وجود ندارد');
    } else {
      const sitemap = fs.readFileSync(sitemapPath, 'utf8');
      for (const file of publicFiles) {
        const expected = expectedCanonical(file);
        if (!new RegExp(`<loc>\\s*${escapeRegExp(expected)}\\s*<\\/loc>`).test(sitemap)) {
          fail(`sitemap.xml شامل ${expected} نیست`);
        }
      }
    }
    if (!fs.existsSync(robotsPath)) {
      fail('robots.txt در خروجی وجود ندارد');
    } else {
      const robots = fs.readFileSync(robotsPath, 'utf8');
      if (!robots.includes(`Sitemap: ${site.href}/sitemap.xml`)) {
        fail(`robots.txt باید Sitemap: ${site.href}/sitemap.xml را داشته باشد`);
      }
    }
  }
}

if (issues.length) {
  console.error(`بررسی کیفیت سایت ناموفق بود (${issues.length} خطا):`);
  for (const issue of issues) console.error(`- ${issue}`);
  process.exitCode = 1;
} else {
  console.log(`بررسی کیفیت سایت موفق بود: ${expectedPages.length} صفحهٔ عمومی در ${path.relative(repoRoot, outputDir) || '.'}`);
}
