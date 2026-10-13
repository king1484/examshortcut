import nextEnv from '@next/env';
const { loadEnvConfig } = nextEnv;
import { pathToFileURL } from 'node:url';

export function validateAuthConfig(env) {
  const names = ['API_KEY', 'AUTH_DOMAIN', 'PROJECT_ID', 'APP_ID'].map(n => `NEXT_PUBLIC_FIREBASE_${n}`);
  const missing = names.filter(n => !env[n]?.trim());
  if (missing.length) throw new Error(`Login configuration missing: ${missing.join(', ')}. Build stopped to protect the deployed login.`);
  const config = Object.fromEntries(names.map(n => [n, env[n].trim()]));
  if (!/^AIza[\w-]{30,}$/.test(config.NEXT_PUBLIC_FIREBASE_API_KEY)) throw new Error('Invalid Firebase web API key.');
  if (!/^[a-z\d-]+\.firebaseapp\.com$/.test(config.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN)) throw new Error('Invalid Firebase authentication domain.');
  if (!/^1:\d+:web:[a-f\d]+$/.test(config.NEXT_PUBLIC_FIREBASE_APP_ID)) throw new Error('Invalid Firebase web app ID.');
  if (config.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN !== `${config.NEXT_PUBLIC_FIREBASE_PROJECT_ID}.firebaseapp.com`) throw new Error('Firebase project and authentication domain do not match.');
  return config;
}

export async function checkAuthConfig() {
  loadEnvConfig(process.cwd());
  const config = validateAuthConfig(process.env);
  const base = 'https://identitytoolkit.googleapis.com/v1';
  const key = config.NEXT_PUBLIC_FIREBASE_API_KEY;
  const read = async (url, options) => {
    const res = await fetch(url, { ...options, signal: AbortSignal.timeout(20000) });
    if (!res.ok) throw new Error(`Firebase configuration check failed (HTTP ${res.status}). Deployment stopped.`);
    return res.json();
  };
  const project = await read(`${base}/projects?key=${key}`);
  if (config.NEXT_PUBLIC_FIREBASE_APP_ID.split(':')[1] !== String(project.projectId)) throw new Error('Firebase API key and web app belong to different projects. Deployment stopped.');
  for (const domain of ['examshortcut.in', 'www.examshortcut.in']) {
    if (!project.authorizedDomains?.includes(domain)) throw new Error(`Firebase does not authorize ${domain}. Deployment stopped.`);
  }
  const google = await read(`${base}/accounts:createAuthUri?key=${key}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ providerId: 'google.com', continueUri: 'https://examshortcut.in/login/' }),
  });
  if (google.providerId !== 'google.com' || new URL(google.authUri).hostname !== 'accounts.google.com') throw new Error('Google sign-in provider is unavailable. Deployment stopped.');
  console.log('Login preflight passed: complete Firebase config, production domains authorized, Google provider enabled.');
  return config;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  checkAuthConfig().catch(e => { console.error(e.message); process.exitCode = 1; });
}
