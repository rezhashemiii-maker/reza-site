import fs from 'node:fs';
import path from 'node:path';

const NAMES = new Set(['header', 'footer']);

export function expandPartials(source, pageFile, root) {
  return source.replace(/<dc-include\s+name="([a-z-]+)"\s*><\/dc-include>/g, (_, name) => {
    if (!NAMES.has(name)) throw new Error(`جزء مشترک ناشناخته: ${name}`);
    let html = fs.readFileSync(path.join(root, 'src', 'partials', `${name}.html`), 'utf8').trim();
    if (name === 'header') {
      html = html.replace(/<a\b[^>]*>/g, (tag) => {
        if (!tag.includes(`href="${pageFile}"`)) return tag;
        if (tag.includes('class="tab"')) {
          return tag.replace('class="tab"', 'class="tab on" aria-current="page"');
        }
        if (tag.includes('class="navcta"')) return tag.replace('class="navcta"', 'class="navcta" aria-current="page"');
        return tag;
      });
    }
    return html;
  });
}
