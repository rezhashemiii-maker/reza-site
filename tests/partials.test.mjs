import test from 'node:test';
import assert from 'node:assert/strict';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import { expandPartials } from '../tools/partials.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

test('هدر و فوتر در زمان ساخت وارد می‌شوند و صفحهٔ جاری مشخص می‌شود', () => {
  const source = fs.readFileSync(path.join(root, 'src', 'Writing.dc.html'), 'utf8');
  const result = expandPartials(source, 'Writing.dc.html', root);
  assert.doesNotMatch(result, /<dc-include/);
  assert.match(result, /class="tab on" aria-current="page" href="Writing\.dc\.html"/);
  assert.equal((result.match(/class="tab on"/g) || []).length, 1);
  assert.match(result, /href="https:\/\/github\.com\/rezhashemiii-maker"/);
  assert.doesNotMatch(result, /\[لینک GitHub\]|\[لینک LinkedIn\]/);
});

test('تماس aria-current دارد و جزء ناشناخته پذیرفته نمی‌شود', () => {
  const result = expandPartials('<dc-include name="header"></dc-include>', 'Contact.dc.html', root);
  assert.match(result, /class="navcta" aria-current="page"/);
  assert.throws(() => expandPartials('<dc-include name="unknown"></dc-include>', 'Main.dc.html', root));
});
