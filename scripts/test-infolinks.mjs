import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { infolinksBootstrap } from '../src/lib/infolinks.ts';
import { isPublicAdPage } from '../src/lib/advertising.ts';

test('advertising excludes account, messages, personal inputs and active tests', () => {
  for (const url of [
    '', '/login/', '/dashboard/', '/revision/', '/feedback/', '/feature-requests/', '/contact/', '/privacy/',
    '/revision-planner/', '/exams/ssc-cgl/score-calculator/', '/exams/ssc-cgl/posts/',
    '/exams/ssc-cgl/mocks/', '/exams/ssc-cgl/mocks/tier-1-2025/', '/daily-quiz/',
    '/quant/percentage/practice/', '/quant/percentage/examples/', '/quant/percentage/formulas/',
  ]) assert.equal(isPublicAdPage(url), false, url);
  assert.equal(isPublicAdPage('/study-guides/revision-without-forgetting/'), true);
  assert.equal(isPublicAdPage('/exam-analysis/ssc-cgl-2026/'), true);
});

test('verification and development hosts never make advertising requests', () => {
  for (const hostname of ['localhost', '127.0.0.1', 'preview.examshortcut.pages.dev']) {
    vm.runInNewContext(infolinksBootstrap, { location: { hostname } });
  }
});

test('the issued account initializes once and requests the vendor only over HTTPS', () => {
  const scripts = [];
  const context = {
    location: { hostname: 'examshortcut.in' }, window: {},
    document: {
      getElementById: id => scripts.find(s => s.id === id),
      createElement: () => ({}), body: { appendChild: script => scripts.push(script) },
    },
  };
  vm.runInNewContext(infolinksBootstrap, context);
  vm.runInNewContext(infolinksBootstrap, context);
  assert.equal(scripts.length, 1);
  assert.equal(scripts[0].src, 'https://resources.infolinks.com/js/infolinks_main.js');
  assert.equal(context.window.infolinks_pid, 3448714);
  assert.equal(context.window.infolinks_wsid, 0);
});
