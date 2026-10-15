import test from 'node:test';
import assert from 'node:assert/strict';
import { normalizeSiteUrl, metadataTags, withStaticMetadata } from '../tools/metadata.mjs';
import { parse, find } from '../tools/parse.mjs';

const site = 'https://rezhashemiii-maker.github.io/reza-site';
const page = { title: 'عنوان "آزمایشی" <A&B>', description: 'متن "روشن" & اختصاصی', out: 'sample.html' };
const nodes = (tree, tag) => {
  const out = [];
  const visit = (node) => {
    if (node.tag === tag) out.push(node);
    (node.kids || []).forEach(visit);
  };
  visit(tree);
  return out;
};

test('نشانی سایت واقعی است و credentials، query، fragment و protocol نامعتبر پذیرفته نمی‌شوند', () => {
  assert.equal(normalizeSiteUrl('  '), '');
  assert.equal(normalizeSiteUrl(site + '/'), site);
  for (const bad of ['javascript:alert(1)', 'ftp://example.com', 'https://user:pass@example.com', site + '?x=1', site + '#fragment']) {
    assert.throws(() => normalizeSiteUrl(bad));
  }
});

test('متادیتا مقدارها را escape می‌کند و canonical و تصویر را با prefix سایت می‌سازد', () => {
  const html = metadataTags(page, site);
  const tree = parse(html);
  const metas = Object.fromEntries(nodes(tree, 'meta').map((n) => [n.attrs.name || n.attrs.property, n.attrs.content]));
  assert.equal(metas.description, page.description);
  assert.equal(metas['og:title'], page.title);
  assert.equal(metas['og:url'], site + '/sample.html');
  assert.equal(metas['og:image'], site + '/assets/social-preview.png');
  assert.equal(metas['twitter:card'], 'summary_large_image');
  assert.equal(find(tree, 'link').attrs.href, site + '/sample.html');
  assert.match(html, /&quot;/);
  assert.match(html, /&amp;/);
  assert.equal(metadataTags({ ...page, out: 'index.html' }, site).includes(`href="${site}/"`), true);
});

test('پیش‌نمایش بدون دامنه URL ساختگی یا canonical تولید نمی‌کند', () => {
  const html = metadataTags(page, '');
  assert.doesNotMatch(html, /rel="canonical"|property="og:url"|property="og:image"|name="twitter:image"/);
  assert.match(html, /name="twitter:card" content="summary"/);
  assert.throws(() => metadataTags({ ...page, description: '' }, site));
});

test('بازنویسی head مستقل بدنه و اسکریپت‌ها را تغییر نمی‌دهد و تگ‌های تکراری نمی‌سازد', () => {
  const body = '</head><body><h1>محتوا</h1><script>const data = "<meta name=\\"description\\" content=\\"unchanged\\">";</script></body></html>';
  const source = '<!doctype html><html lang="fa" dir="rtl"><head><title>صفحهٔ مستقل</title><meta name="description" content="توضیح مستقل"><meta property="og:title" content="قدیمی"><meta name="theme-color" content="#F5F3EE"><link rel="canonical" href="https://old.invalid"><script type="application/ld+json">{"@type":"Article"}</script>' + body;
  const result = withStaticMetadata(source, { file: 'sample.html', out: 'sample.html', type: 'article' }, site);
  assert.equal(result.slice(result.indexOf('</head>')), body);
  const head = parse(result.slice(0, result.indexOf('</head>')));
  const meta = nodes(head, 'meta');
  assert.equal(meta.filter((n) => n.attrs.name === 'description').length, 1);
  assert.equal(meta.filter((n) => n.attrs.property === 'og:title').length, 1);
  assert.equal(meta.find((n) => n.attrs.name === 'theme-color').attrs.content, '#F5F3EE');
  assert.match(result, /"@type":"Article"/);
  assert.equal(nodes(head, 'link').filter((n) => n.attrs.rel === 'canonical').length, 1);
  assert.throws(() => withStaticMetadata('<html>', { file: 'invalid.html' }, site));
});
