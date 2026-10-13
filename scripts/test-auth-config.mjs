import test from 'node:test';
import assert from 'node:assert/strict';
import { validateAuthConfig } from './check-auth-config.mjs';

const env = {
  NEXT_PUBLIC_FIREBASE_API_KEY: `AIza${'a'.repeat(35)}`,
  NEXT_PUBLIC_FIREBASE_PROJECT_ID: 'example-project',
  NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN: 'example-project.firebaseapp.com',
  NEXT_PUBLIC_FIREBASE_APP_ID: '1:12345:web:abcdef',
};
test('accepts a complete coherent web configuration', () => assert.deepEqual(validateAuthConfig(env), env));
test('rejects every missing setting, including the CI regression', () => {
  assert.throws(() => validateAuthConfig({}), /Login configuration missing/);
  for (const key of Object.keys(env)) assert.throws(() => validateAuthConfig({ ...env, [key]: '' }), /Login configuration missing/);
});
test('rejects mixed projects and malformed values', () => {
  assert.throws(() => validateAuthConfig({ ...env, NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN: 'other-project.firebaseapp.com' }), /do not match/);
  assert.throws(() => validateAuthConfig({ ...env, NEXT_PUBLIC_FIREBASE_API_KEY: 'placeholder' }), /Invalid/);
});
