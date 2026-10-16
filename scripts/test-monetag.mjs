import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { monetagBootstrap } from '../src/lib/monetag.ts';

test('Monetag never requests ads on development or preview hosts', () => {
  for (const hostname of ['localhost', '127.0.0.1', 'preview.examshortcut.pages.dev']) {
    vm.runInNewContext(monetagBootstrap, { location: { hostname } });
  }
});

test('the issued Vignette zone initializes once over HTTPS on both public hosts', () => {
  for (const hostname of ['examshortcut.in', 'www.examshortcut.in']) {
    const scripts = [];
    const context = {
      location: { hostname },
      document: {
        readyState: 'complete',
        getElementById: id => scripts.find(s => s.id === id),
        createElement: () => ({ dataset: {}, async: true }),
        querySelector: () => scripts.find(s => s.dataset.zone === '12047445'),
        body: { appendChild: script => { scripts.push(script); return script; } },
      },
    };
    vm.runInNewContext(monetagBootstrap, context);
    vm.runInNewContext(monetagBootstrap, context);
    assert.equal(scripts.length, 1);
    assert.equal(scripts[0].dataset.zone, '12047445');
    assert.equal(scripts[0].src, 'https://n6wxm.com/vignette.min.js');
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
      createElement: () => ({ dataset: {}, async: true }),
      querySelector: () => scripts.find(s => s.dataset.zone === '12047445'),
      documentElement: { appendChild: script => { scripts.push(script); return script; } },
    },
  };
  vm.runInNewContext(monetagBootstrap, context);
  assert.equal(scripts.length, 1);
  assert.equal(scripts[0].dataset.zone, '12047445');
  assert.equal(scripts[0].src, 'https://n6wxm.com/vignette.min.js');
});
