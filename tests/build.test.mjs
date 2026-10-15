import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const buildScript = path.join(repoRoot, 'tools', 'build.mjs');
const checkScript = path.join(repoRoot, 'tools', 'check-site.mjs');
const productionUrl = 'https://rezhashemiii-maker.github.io/reza-site';
const expectedStandalonePages = ['agri-invest.html', 'iraq.html'];

function run(command, args, env = {}) {
  return spawnSync(command, args, {
    cwd: repoRoot,
    encoding: 'utf8',
    env: { ...process.env, ...env },
  });
}

function build(env) {
  return run(process.execPath, [buildScript], env);
}

function outputHtmlFiles(directory) {
  return fs.readdirSync(directory).filter((name) => name.endsWith('.html')).sort();
}

function filesRecursively(directory, prefix = '') {
  if (!fs.existsSync(directory)) return [];
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const relative = path.posix.join(prefix, entry.name);
    const absolute = path.join(directory, entry.name);
    return entry.isDirectory() ? filesRecursively(absolute, relative) : [relative];
  });
}

function diagnostic(result) {
  return `status=${result.status}\nstdout:\n${result.stdout}\nstderr:\n${result.stderr}`;
}

test('build با SITE_URL و OUTPUT_DIR مستقل، تمام خروجی‌های عمومی و دارایی‌های دستی را می‌سازد', (t) => {
  const output = fs.mkdtempSync(path.join(os.tmpdir(), 'reza-site-build-'));
  t.after(() => fs.rmSync(output, { recursive: true, force: true }));

  const result = build({ SITE_URL: productionUrl, OUTPUT_DIR: output });
  assert.equal(result.status, 0, diagnostic(result));

  const htmlFiles = outputHtmlFiles(output);
  const publicFiles = htmlFiles.filter((name) => name !== '404.html');
  assert.equal(publicFiles.length, 84, '۸۲ قالب و ۲ صفحهٔ مستقل باید تولید شوند');
  assert.equal(htmlFiles.length, 85, 'به‌علاوهٔ 404.html باید تولید شود');
  for (const file of expectedStandalonePages) assert.ok(publicFiles.includes(file), `${file} باید در خروجی باشد`);
  assert.ok(fs.existsSync(path.join(output, '404.html')));
  assert.ok(fs.existsSync(path.join(output, 'sitemap.xml')));
  assert.ok(fs.existsSync(path.join(output, 'robots.txt')));

  const sourceAssets = filesRecursively(path.join(repoRoot, 'public', 'assets'));
  assert.ok(sourceAssets.length > 0, 'public/assets باید دست‌کم یک دارایی دستی داشته باشد');
  for (const asset of sourceAssets) {
    assert.ok(fs.existsSync(path.join(output, 'assets', asset)), `دارایی دستی ${asset} باید کپی شود`);
  }

  const index = fs.readFileSync(path.join(output, 'index.html'), 'utf8');
  assert.match(index, new RegExp(`<link rel="canonical" href="${productionUrl}/">`));
  assert.match(index, new RegExp(`<meta property="og:url" content="${productionUrl}/">`));

  const checked = run(process.execPath, [checkScript, output], { SITE_URL: productionUrl });
  assert.equal(checked.status, 0, diagnostic(checked));
});

test('build بدون SITE_URL خروجی جدا می‌سازد و metadata نسبیِ مطلقِ نادرست یا sitemap ندارد', (t) => {
  const output = fs.mkdtempSync(path.join(os.tmpdir(), 'reza-site-no-site-url-'));
  t.after(() => fs.rmSync(output, { recursive: true, force: true }));

  const result = build({ OUTPUT_DIR: output, SITE_URL: '' });
  assert.equal(result.status, 0, diagnostic(result));
  assert.equal(outputHtmlFiles(output).filter((name) => name !== '404.html').length, 84);
  assert.ok(!fs.existsSync(path.join(output, 'sitemap.xml')));
  assert.ok(!fs.existsSync(path.join(output, 'robots.txt')));

  const index = fs.readFileSync(path.join(output, 'index.html'), 'utf8');
  assert.doesNotMatch(index, /<link rel="canonical"/);
  assert.doesNotMatch(index, /<meta property="og:url" content="\/(?!\/)/);
});

test('OUTPUT_DIR نسبی نیز نسبت به ریشهٔ مخزن به‌عنوان خروجی جدا پذیرفته می‌شود', (t) => {
  const relative = `.tmp-build-test-${process.pid}-${Date.now()}`;
  const output = path.join(repoRoot, relative);
  t.after(() => fs.rmSync(output, { recursive: true, force: true }));

  const result = build({ OUTPUT_DIR: relative, SITE_URL: productionUrl });
  assert.equal(result.status, 0, diagnostic(result));
  assert.ok(fs.existsSync(path.join(output, 'index.html')));
  assert.ok(fs.existsSync(path.join(output, '404.html')));
});

test('مقادیر نامعتبر SITE_URL و OUTPUT_DIR با خطای روشن رد می‌شوند', (t) => {
  const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'reza-site-invalid-env-'));
  const outputFile = path.join(temporary, 'not-a-directory');
  fs.writeFileSync(outputFile, 'file');
  t.after(() => fs.rmSync(temporary, { recursive: true, force: true }));

  const invalidSite = build({ SITE_URL: 'not a URL', OUTPUT_DIR: path.join(temporary, 'out') });
  assert.notEqual(invalidSite.status, 0, 'SITE_URL نامعتبر باید build را متوقف کند');
  assert.match(`${invalidSite.stdout}\n${invalidSite.stderr}`, /SITE_URL|URL/i);

  const invalidOutput = build({ SITE_URL: productionUrl, OUTPUT_DIR: outputFile });
  assert.notEqual(invalidOutput.status, 0, 'OUTPUT_DIR که فایل است نباید پذیرفته شود');
});
