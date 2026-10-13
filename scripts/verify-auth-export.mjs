import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import nextEnv from '@next/env';
const { loadEnvConfig } = nextEnv;
import { validateAuthConfig } from './check-auth-config.mjs';

loadEnvConfig(process.cwd());
const config = validateAuthConfig(process.env);
const html = fs.readFileSync('out/login/index.html', 'utf8');
assert(html.includes('data-auth-ready="true"'), 'Export disabled accounts: deployment stopped.');
assert(!html.includes('Accounts are being switched on shortly'), 'Export contains disabled login.');
const walk = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(path.join(dir, e.name)) : [path.join(dir, e.name)]);
const bundle = walk('out/_next/static').filter(p => p.endsWith('.js')).map(p => fs.readFileSync(p, 'utf8')).join('\n');
for (const [name, value] of Object.entries(config)) assert(bundle.includes(value), `${name} was not bundled: deployment stopped.`);
assert(bundle.includes('google.com'), 'Google authentication provider missing from export.');
console.log('Login export passed: accounts enabled and all four Firebase values bundled.');
