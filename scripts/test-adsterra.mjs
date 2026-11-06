import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { readFileSync } from 'node:fs';
import { isAdsterraReadingPage, canPlaceAdsterra, chooseAdsterraUnit, canServeAdsterra, ADSTERRA_SERVE_AFTER } from '../src/lib/adsterra.ts';
import { buildAdDocument } from './generate-ad-documents.mjs';

test('global reading placements exclude interactive tests, quizzes, forms, accounts and tools', () => {
  for (const route of ['/login/', '/dashboard/', '/contact/', '/feedback/', '/daily-quiz/', '/revision-planner/',
    '/exams/cat/mocks/real-paper/', '/exams/ssc-cgl/score-calculator/',
    '/exams/ssc-cgl/rank-estimator/', '/exams/cat/study-plan/', '/quant/percentage/practice/',
    '/current-affairs/2026/11/', '/exam-updates/example/extra/']) assert.equal(isAdsterraReadingPage(route), false, route);
  for (const route of ['/', '/quant/percentage/', '/exam-updates/example/', '/exams/ssc-cgl/guides/tier-2-strategy/', '/exams/ssc-cgl/mocks/']) assert(isAdsterraReadingPage(route), route);
});

test('fixed banners must fit the actual content width without scaling or clipping', () => {
  assert.equal(chooseAdsterraUnit(288, 'reading'), null);
  assert.equal(chooseAdsterraUnit(319, 'reading'), null);
  assert.equal(chooseAdsterraUnit(320, 'reading'), 'mobile');
  assert.equal(chooseAdsterraUnit(727, 'reading'), 'mobile');
  assert.equal(chooseAdsterraUnit(728, 'reading'), 'desktop');
  assert.equal(chooseAdsterraUnit(299, 'article'), null);
  assert.equal(chooseAdsterraUnit(300, 'article'), 'article');
});

test('pending category confirmation creates no advertising request, even with enable requested', () => {
  for (const [enabled, confirmation] of [[false, null], [true, null], [false, 'confirmed']]) {
    const html = buildAdDocument(enabled, confirmation);
    assert(!html.includes('bauval.org'));
    vm.runInNewContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], {});
  }
  for (const host of ['localhost', '127.0.0.1', 'preview.examshortcut.pages.dev']) assert.equal(canServeAdsterra(host), false);
});

test('the isolated document accepts only known units, official parents and the frame origin', () => {
  const script = buildAdDocument(true, 'reviewed').match(/<script>([\s\S]*?)<\/script>/)[1];
  for (const [hostname, referrer, query, expected] of [
    ['examshortcut.pages.dev', 'https://examshortcut.in/quant/percentage/', '?unit=mobile', 1],
    ['examshortcut.pages.dev', 'https://www.examshortcut.in/', '?unit=desktop', 1],
    ['examshortcut.in', 'https://examshortcut.in/', '?unit=mobile', 0],
    ['examshortcut.pages.dev', 'https://evil.example/', '?unit=mobile', 0],
    ['examshortcut.pages.dev', '', '?unit=mobile', 0],
    ['examshortcut.pages.dev', 'https://examshortcut.in/', '?unit=constructor', 0],
    ['examshortcut.pages.dev', 'https://examshortcut.in/', '?unit=https://evil.example/script.js', 0],
  ]) {
    const requests = [];
    vm.runInNewContext(script, { URL, URLSearchParams, Date: { now: () => Date.parse(ADSTERRA_SERVE_AFTER) }, location: { hostname, search: query }, window: {},
      document: { referrer, createElement: () => ({}), body: { appendChild: script => requests.push(script.src) } } });
    assert.equal(requests.length, expected);
    if (expected) assert.match(requests[0], /^https:\/\/bauval\.org\/22\/[a-f0-9]{32}$/);
  }
});

test('requests wait for the vendor category-block propagation period', () => {
  const deadline = Date.parse(ADSTERRA_SERVE_AFTER);
  assert.equal(canServeAdsterra('examshortcut.in', deadline - 1), false);
  assert.equal(canServeAdsterra('examshortcut.in', deadline), true);
  assert.equal(canServeAdsterra('www.examshortcut.in', deadline), true);
  assert.equal(canServeAdsterra('examshortcut.in.evil.example', deadline), false);
  const requests = [];
  const script = buildAdDocument(true, 'confirmed').match(/<script>([\s\S]*?)<\/script>/)[1];
  vm.runInNewContext(script, { URL, URLSearchParams, Date: { now: () => deadline - 1 }, window: {},
    location: { hostname: 'examshortcut.pages.dev', search: '?unit=mobile' },
    document: { referrer: 'https://examshortcut.in/', createElement: () => ({}), body: { appendChild: script => requests.push(script.src) } } });
  assert.equal(requests.length, 0);
});


test('interactive placements are opt-in and cannot leak across page types', () => {
  const examples = [
    ['/daily-quiz/', 'quiz'], ['/quant/percentage/practice/', 'quiz'],
    ['/current-affairs/2026/11/', 'quiz'], ['/english/verbs/learn/agreement/', 'quiz'],
    ['/exams/ssc-cgl/marks-calculator/', 'calculator'], ['/exams/cat/score-calculator/', 'calculator'],
    ['/exams/rrb-ntpc/salary-calculator/', 'calculator'], ['/exams/ssc-cgl/normalisation-calculator/', 'calculator'],
    ['/exams/ssc-cgl/mocks/tier-1-01/', 'mock-result'],
  ];
  for (const [path, context] of examples) {
    assert.equal(canPlaceAdsterra(path, context), true, path);
    assert.equal(canPlaceAdsterra(path, 'reading'), path.includes('/learn/'), path);
    for (const other of ['quiz', 'calculator', 'mock-result'].filter(c => c !== context)) {
      assert.equal(canPlaceAdsterra(path, other), false, `${path}: ${other}`);
    }
  }
  for (const path of ['/login/', '/dashboard/', '/feedback/', '/exams/ssc-cgl/typing-test/']) {
    for (const context of ['reading', 'quiz', 'calculator', 'mock-result']) assert.equal(canPlaceAdsterra(path, context), false);
  }
});

test('mock advertising exists only in its result component, and quizzes do not refresh ads per question', () => {
  const mock = readFileSync(new URL('../src/components/MockCBT.tsx', import.meta.url), 'utf8');
  const result = mock.indexOf('function MockResult(');
  assert(result > 0);
  assert(!mock.slice(0, result).includes('<AdsterraBanner'));
  assert.equal((mock.slice(result).match(/<AdsterraBanner/g) || []).length, 1);
  assert.match(mock, /if \(phase === 'result'\) return <MockResult/);
  const quiz = readFileSync(new URL('../src/components/TopicQuiz.tsx', import.meta.url), 'utf8');
  assert.equal((quiz.match(/<AdsterraBanner/g) || []).length, 1);
  assert(!quiz.slice(quiz.indexOf('function TopicQuizBody')).includes('<AdsterraBanner'));
  const banner = readFileSync(new URL('../src/components/AdsterraBanner.tsx', import.meta.url), 'utf8');
  assert(!banner.includes('sessionStorage'));
  assert(!banner.includes('Hide ads while studying'));
  assert(!banner.includes('setInterval'));
});
