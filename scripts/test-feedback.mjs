import test from 'node:test';
import assert from 'node:assert/strict';
import { validateSubmission, onRequest } from '../functions/api/feedback.js';

const data = { id: '12345678-1234-4234-8234-123456789abc', kind: 'feedback', title: 'Missing explanation', message: 'Please explain the base value in this solution.', email: '', page: 'https://examshortcut.in/quant/' };
test('accepts anonymous feedback and feature requests', () => {
  assert.equal(validateSubmission(data).email, '');
  assert.equal(validateSubmission({ ...data, kind: 'feature' }).kind, 'feature');
});
test('rejects bad fields, spam, oversized messages and unrelated links', () => {
  for (const change of [{ kind: 'spam' }, { title: 'x' }, { message: 'short' }, { message: 'x'.repeat(3001) }, { email: 'invalid' }, { website: 'spam' }, { id: '../' }, { page: 'https://evil.example/' }, { page: 'https://user:password@examshortcut.in/' }]) {
    assert.throws(() => validateSubmission({ ...data, ...change }));
  }
});
test('endpoint refuses reads and cross-site posts without exposing saved feedback', async () => {
  const url = 'https://examshortcut.in/api/feedback';
  const get = await onRequest({ request: new Request(url), env: {} });
  assert.equal(get.status, 405);
  const cross = await onRequest({ request: new Request(url, { method: 'POST', headers: { Origin: 'https://evil.example' } }), env: {} });
  assert.equal(cross.status, 403);
});
test('missing storage returns an error instead of pretending to save', async () => {
  const response = await onRequest({ request: new Request('https://examshortcut.in/api/feedback', {
    method: 'POST', headers: { Origin: 'https://examshortcut.in', 'Content-Type': 'application/json' }, body: JSON.stringify(data),
  }), env: {} });
  assert.equal(response.status, 503);
  assert((await response.json()).error);
});
