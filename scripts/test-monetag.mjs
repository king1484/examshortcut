import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { readFile } from 'node:fs/promises';
import { monetagBootstrap } from '../src/lib/monetag.ts';

test('Monetag never requests ads on development or preview hosts', () => {
  for (const hostname of ['localhost', '127.0.0.1', 'preview.examshortcut.pages.dev']) {
    vm.runInNewContext(monetagBootstrap, { location: { hostname } });
  }
});

test('the issued MultiTag initializes once with its Cloudflare attribute on both public hosts', () => {
  for (const hostname of ['examshortcut.in', 'www.examshortcut.in']) {
    const scripts = [];
    const context = {
      location: { hostname },
      document: {
        readyState: 'complete',
        getElementById: id => scripts.find(s => s.id === id),
        createElement: () => ({ dataset: {}, attrs: {}, setAttribute(name, value) { this.attrs[name] = value; } }),
        head: { appendChild: script => { scripts.push(script); return script; } },
      },
    };
    vm.runInNewContext(monetagBootstrap, context);
    vm.runInNewContext(monetagBootstrap, context);
    assert.equal(scripts.length, 1);
    assert.equal(scripts[0].dataset.zone, '296822');
    assert.equal(scripts[0].src, 'https://quge5.com/88/tag.min.js');
    assert.equal(scripts[0].attrs['data-cfasync'], 'false');
    assert.equal(scripts[0].async, true);
    assert.equal(scripts[0].dataset.loadState, 'loading');
    scripts[0].onload();
    assert.equal(scripts[0].dataset.loadState, 'loaded');
    scripts[0].onerror();
    assert.equal(scripts[0].dataset.loadState, 'error');
  }
});

test('the issued tag starts in the head before body exists without waiting for page load', () => {
  const scripts = [];
  const context = {
    location: { hostname: 'examshortcut.in' },
    document: {
      readyState: 'loading',
      getElementById: id => scripts.find(s => s.id === id),
      createElement: () => ({ dataset: {}, setAttribute() {} }),
      head: { appendChild: script => { scripts.push(script); return script; } },
    },
  };
  vm.runInNewContext(monetagBootstrap, context);
  assert.equal(scripts.length, 1);
  assert.equal(scripts[0].dataset.zone, '296822');
  assert.equal(scripts[0].src, 'https://quge5.com/88/tag.min.js');
});

test('offline handlers remain available when the vendor worker import is blocked', async () => {
  const imported = [];
  const worker = await readFile(new URL('../public/sw.js', import.meta.url), 'utf8');
  vm.runInNewContext(worker, {
    self: { location: { hostname: 'examshortcut.in' } }, console: { warn() {} },
    importScripts(url) {
      imported.push(url);
      if (url.startsWith('https://')) throw new Error('blocked');
    },
  });
  assert.equal(imported[0], '/offline-sw.js');
  assert.equal(imported[1], 'https://3nbf4.com/act/files/service-worker.min.js?r=sw');
});

test('preview service workers only load the site offline handlers', async () => {
  const imported = [];
  const worker = await readFile(new URL('../public/sw.js', import.meta.url), 'utf8');
  vm.runInNewContext(worker, {
    self: { location: { hostname: 'preview.examshortcut.pages.dev' } },
    importScripts: url => imported.push(url),
  });
  assert.deepEqual(imported, ['/offline-sw.js']);
});

test('offline cache updates preserve caches belonging to the advertising worker', async () => {
  const handlers = {};
  const deleted = [];
  const worker = await readFile(new URL('../public/offline-sw.js', import.meta.url), 'utf8');
  vm.runInNewContext(worker, {
    self: { addEventListener: (event, handler) => { handlers[event] = handler; }, clients: { claim() {} } },
    caches: { keys: async () => ['es-v9', 'es-v10', 'monetag-push'], delete: async name => deleted.push(name) },
  });
  let completion;
  handlers.activate({ waitUntil: promise => { completion = promise; } });
  await completion;
  assert.deepEqual(deleted, ['es-v9']);
});
