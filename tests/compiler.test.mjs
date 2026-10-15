import assert from 'node:assert/strict';
import test from 'node:test';

import { compile, applyClasses } from '../tools/compile.mjs';
import { parse } from '../tools/parse.mjs';
import { renderToString } from '../tools/render.mjs';

function compileTemplate(source, page = 'test.html') {
  const styleUse = new Map();
  const ast = compile(parse(source), { styleUse, page });
  return { ast, styleUse };
}

test('متن و attributeهای قالب به‌درستی escape می‌شوند و مقدار گمشده attribute نمی‌سازد', () => {
  const { ast } = compileTemplate(`
    <div title='نقل‌قول: {{ quote }} &amp; بیشتر' data-missing='{{ missing }}'>
      متن {{ message }}
    </div>
  `);

  const html = renderToString(ast, [{ quote: '"دوگانه"', message: '<بازه & امن>' }]);

  assert.match(html, /title="نقل‌قول: &quot;دوگانه&quot; &amp; بیشتر"/);
  assert.match(html, /متن &lt;بازه &amp; امن&gt;/);
  assert.doesNotMatch(html, /data-missing=/);
  assert.doesNotMatch(html, /<بازه/);
});

test('sc-if و sc-for با scope تو در تو، $index و مسیرهای dotted رندر می‌شوند', () => {
  const { ast } = compileTemplate(`
    <section>
      <sc-if value="{{ state.visible }}"><h1>{{ state.title }}</h1></sc-if>
      <sc-for list="{{ items }}" as="item"><p>{{ $index }}: {{ item.label }}</p></sc-for>
    </section>
  `);

  const shown = renderToString(ast, [{
    state: { visible: true, title: 'فهرست' },
    items: [{ label: 'اول' }, { label: 'دوم' }],
  }]);
  assert.match(shown, /<h1>فهرست<\/h1>/);
  assert.match(shown, /<p>0: اول<\/p>/);
  assert.match(shown, /<p>1: دوم<\/p>/);

  const hidden = renderToString(ast, [{
    state: { visible: false, title: 'نباید دیده شود' },
    items: [],
  }]);
  assert.doesNotMatch(hidden, /نباید دیده شود/);
  assert.doesNotMatch(hidden, /<h1>/);
});

test('styleهای تکراری با نام کلاس امن و قابل ترکیب اعمال می‌شوند', () => {
  const { ast, styleUse } = compileTemplate(`
    <main>
      <div class="author" style="color: red; padding: 4px">A</div>
      <div style="color: red; padding: 4px">B</div>
      <p style="margin: 0">C</p>
    </main>
  `);

  const shared = styleUse.get('color: red;padding: 4px');
  assert.ok(shared, 'استایل تکراری باید در styleUse ثبت شود');
  shared.cls = 'sharedStyle';
  applyClasses(ast, styleUse);

  const html = renderToString(ast, [{}]);
  assert.match(html, /<div class="sharedStyle author">A<\/div>/);
  assert.match(html, /<div class="sharedStyle">B<\/div>/);
  assert.match(html, /<p style="margin: 0">C<\/p>/);
  assert.doesNotMatch(html, /style="color: red; padding: 4px"/);
});

test('محتوای raw در script دست‌نخورده می‌ماند، اما متن عادی escape می‌شود', () => {
  const { ast } = compileTemplate('<script>const markup = "<x>&";</script><p>{{ value }}</p>');
  const html = renderToString(ast, [{ value: '<x>&' }]);

  assert.match(html, /<script>const markup = "<x>&";<\/script>/);
  assert.match(html, /<p>&lt;x&gt;&amp;<\/p>/);
});
