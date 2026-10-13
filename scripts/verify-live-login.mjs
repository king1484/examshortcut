import nextEnv from '@next/env';
import { validateAuthConfig } from './check-auth-config.mjs';

nextEnv.loadEnvConfig(process.cwd());
const config = validateAuthConfig(process.env);
async function verify() {
  const response = await fetch('https://examshortcut.in/login/', { cache: 'no-store', signal: AbortSignal.timeout(15000) });
  if (!response.ok) throw new Error(`Live login returned HTTP ${response.status}.`);
  const html = await response.text();
  if (!html.includes('data-auth-ready="true"')) throw new Error('Live login does not have accounts enabled.');
  const scripts = [...html.matchAll(/<script[^>]+src="([^"]+)"/g)].map(m => m[1]).filter(p => p.startsWith('/_next/static/'));
  const chunks = await Promise.all(scripts.map(async p => {
    const res = await fetch(new URL(p, 'https://examshortcut.in'), { signal: AbortSignal.timeout(15000) });
    if (!res.ok) throw new Error(`Live login asset returned HTTP ${res.status}.`);
    return res.text();
  }));
  const bundle = chunks.join('\n');
  for (const [name, value] of Object.entries(config)) if (!bundle.includes(value)) throw new Error(`${name} missing from live login assets.`);
  console.log('Live login smoke check passed: HTTP 200, accounts enabled, matching Firebase settings in served JavaScript.');
}
let failure;
for (let attempt = 1; attempt <= 7; attempt++) {
  try { await verify(); failure = null; break; } catch (e) {
    failure = e;
    console.log(`Login propagation check ${attempt}/7: ${e.message}`);
    if (attempt < 7) await new Promise(resolve => setTimeout(resolve, 10000));
  }
}
if (failure) { console.error(failure.message); process.exitCode = 1; }
