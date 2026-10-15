import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const site = 'https://rezhashemiii-maker.github.io/reza-site';

test('کنترل کیفیت دامنه را از خروجی تشخیص می‌دهد و نقص واقعی را رد می‌کند', (t) => {
  const output = fs.mkdtempSync(path.join(os.tmpdir(), 'reza-site-quality-'));
  t.after(() => fs.rmSync(output, { recursive: true, force: true }));
  const built = spawnSync(process.execPath, ['tools/build.mjs'], {
    cwd: root, encoding: 'utf8', env: { ...process.env, SITE_URL: site, OUTPUT_DIR: output },
  });
  assert.equal(built.status, 0, built.stderr);
  const env = { ...process.env };
  delete env.SITE_URL;
  const check = () => spawnSync(process.execPath, ['tools/check-site.mjs', output], {
    cwd: root, encoding: 'utf8', env,
  });
  assert.equal(check().status, 0, 'دستور بدون SITE_URL باید canonical موجود را تشخیص دهد');
  const index = path.join(output, 'index.html');
  const html = fs.readFileSync(index, 'utf8');

  fs.writeFileSync(index, html.replace('</body>', '<a href="#quality-missing-anchor">پیوند معیوب</a></body>'));
  let result = check();
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /quality-missing-anchor/);

  fs.writeFileSync(index, html.replace('</body>', '<a href="#">پیوند موقت</a></body>'));
  result = check();
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /لینک موقت #/);

  fs.writeFileSync(index, html.replace(/<meta name="description"[^>]*>/, '<meta name="description" content="">'));
  result = check();
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /description/);

  fs.writeFileSync(index, html);
  fs.writeFileSync(path.join(output, 'unexpected.html'), html);
  result = check();
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /unexpected\.html/);
});
