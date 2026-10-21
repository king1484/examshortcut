import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

test('declared dates survive fresh checkouts and removed legacy mock pages retain redirects', () => {
  const output = fs.mkdtempSync(path.join(os.tmpdir(), 'examshortcut-seo-'));
  try {
    function page(route, metadata = '') {
      const directory = path.join(output, route);
      fs.mkdirSync(directory, { recursive: true });
      fs.writeFileSync(path.join(directory, 'index.html'), `<html><head><title>Fixture</title><meta name="description" content="Fixture"/>${metadata}</head><body>Fixture</body></html>`);
    }
    // Content source mtime is later than this declared date on both a developer
    // machine and a fresh CI checkout; the author-supplied date must win.
    page('study-guides/explicit-date-test', '<meta property="article:modified_time" content="2020-01-02"/>');
    page('exams/cat/mocks/available');
    page('exams/cat/mocks/held', '<meta name="robots" content="noindex, follow"/>');
    fs.writeFileSync(path.join(output, '_redirects'), '# Existing rules\n/old/ /new/ 301\n');
    function generate() {
      const result = spawnSync(process.execPath, ['scripts/generate-sitemap.mjs'], {
        cwd: process.cwd(), env: { ...process.env, SITEMAP_OUT: output }, encoding: 'utf8',
      });
      assert.equal(result.status, 0, result.stderr);
    }
    generate();
    const map = fs.readFileSync(path.join(output, 'sitemap.xml'), 'utf8');
    assert(map.includes('<loc>https://examshortcut.in/study-guides/explicit-date-test/</loc><lastmod>2020-01-02</lastmod>'));
    assert(!map.includes('/exams/cat/mocks/held/'));
    const redirects = fs.readFileSync(path.join(output, '_redirects'), 'utf8');
    for (const id of ['available', 'held']) {
      for (const slash of ['', '/']) {
        assert(redirects.includes(`/exams/ssc-cgl/mocks/${id}${slash} /exams/cat/mocks/${id}/ 301`));
      }
    }
    assert(redirects.includes('/old/ /new/ 301'));
    generate();
    assert.equal(fs.readFileSync(path.join(output, '_redirects'), 'utf8'), redirects);
    assert.equal(fs.readFileSync(path.join(output, 'sitemap.xml'), 'utf8'), map);
  } finally {
    assert.equal(path.dirname(path.resolve(output)), path.resolve(os.tmpdir()));
    assert(path.basename(output).startsWith('examshortcut-seo-'));
    fs.rmSync(output, { recursive: true, force: true });
  }
});
