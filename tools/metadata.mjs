import { parse, find, rawTextOf, encodeText, encodeAttr } from './parse.mjs';

export function normalizeSiteUrl(value = '') {
  if (!value.trim()) return '';
  const url = new URL(value.trim());
  if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password || url.search || url.hash) {
    throw new Error('SITE_URL باید نشانی عمومی http/https بدون اطلاعات ورود، query یا fragment باشد');
  }
  return url.href.replace(/\/+$/, '');
}

export function metadataTags({ title, description, out, type = 'website' }, siteUrl) {
  if (!title?.trim() || !description?.trim()) throw new Error(`${out}: عنوان و توضیح صفحه نباید خالی باشد`);
  const tags = [
    `<meta name="description" content="${encodeAttr(description)}">`,
    `<meta property="og:type" content="${encodeAttr(type)}">`,
    '<meta property="og:locale" content="fa_IR">',
    '<meta property="og:site_name" content="رضا هاشمی">',
    `<meta property="og:title" content="${encodeAttr(title)}">`,
    `<meta property="og:description" content="${encodeAttr(description)}">`,
    `<meta name="twitter:card" content="${siteUrl ? 'summary_large_image' : 'summary'}">`,
    `<meta name="twitter:title" content="${encodeAttr(title)}">`,
    `<meta name="twitter:description" content="${encodeAttr(description)}">`,
  ];
  // پیش‌نمایش بدون دامنهٔ مشخص نباید canonical یا تصویر با نشانی ساختگی بسازد.
  if (siteUrl) {
    const canonical = `${siteUrl}/${out === 'index.html' ? '' : out}`;
    const image = `${siteUrl}/assets/social-preview.png`;
    tags.push(
      `<link rel="canonical" href="${encodeAttr(canonical)}">`,
      `<meta property="og:url" content="${encodeAttr(canonical)}">`,
      `<meta property="og:image" content="${encodeAttr(image)}">`,
      '<meta property="og:image:width" content="1200">',
      '<meta property="og:image:height" content="675">',
      '<meta property="og:image:alt" content="رضا هاشمی — یادگیری ماشین و سیستم‌های داده">',
      `<meta name="twitter:image" content="${encodeAttr(image)}">`,
      '<meta name="twitter:image:alt" content="رضا هاشمی — یادگیری ماشین و سیستم‌های داده">',
    );
  }
  return tags.join('\n');
}

const OWNED_META = new Set([
  'description', 'og:type', 'og:locale', 'og:site_name', 'og:title', 'og:description',
  'og:url', 'og:image', 'og:image:width', 'og:image:height', 'og:image:alt',
  'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image', 'twitter:image:alt',
]);

// فقط head بازنویسی می‌شود؛ بدنه، داده‌ها و اسکریپت‌های صفحهٔ مستقل دست‌نخورده می‌مانند.
export function withStaticMetadata(html, page, siteUrl) {
  const end = html.toLowerCase().indexOf('</head>');
  if (end < 0) throw new Error(`${page.file}: head معتبر پیدا نشد`);
  const tree = parse(html.slice(0, end) + '</head>');
  const title = rawTextOf(find(tree, 'title') || { kids: [] }).trim();
  let description = '';
  const visit = (node) => {
    if (node.tag === 'meta' && node.attrs.name === 'description') description = node.attrs.content || '';
    (node.kids || []).forEach(visit);
  };
  visit(tree);
  const head = html.slice(0, end).replace(/<(meta|link)\b[^>]*>/gi, (tag) => {
    const node = find(parse(tag), /^<meta\b/i.test(tag) ? 'meta' : 'link');
    if (node?.tag === 'meta' && OWNED_META.has(node.attrs.name || node.attrs.property)) return '';
    if (node?.tag === 'link' && node.attrs.rel === 'canonical') return '';
    return tag;
  });
  return `${head}\n${metadataTags({ ...page, title, description }, siteUrl)}\n${html.slice(end)}`;
}

export { encodeText, encodeAttr };
