import fs from 'node:fs';
import { ADSTERRA_ENABLED, ADSTERRA_CATEGORY_CONFIRMATION, ADSTERRA_SERVE_AFTER, ADSTERRA_UNITS } from '../src/lib/adsterra.ts';

// Codes copied from this site's publisher dashboard. They never execute in the app document.
const keys = {
  mobile: 'ad421e7c46979528e3db607ca2bb682e',
  desktop: '7e0573e36a571b0d145ab23096b1e4da',
  article: '59e3808cf2d39bca0ebc82811c6249ee',
};
export function buildAdDocument(enabled, confirmation) {
  const units = Object.fromEntries(Object.entries(ADSTERRA_UNITS).map(([name, unit]) => [name, { ...unit, key: keys[name] }]));
  const script = enabled && confirmation ? `
const units = ${JSON.stringify(units)};
const name = new URLSearchParams(location.search).get('unit');
let parentOrigin = '';
try { parentOrigin = new URL(document.referrer).origin; } catch {}
const unit = Object.hasOwn(units, name) ? units[name] : null;
if (unit && Date.now() >= ${Date.parse(ADSTERRA_SERVE_AFTER)} && location.hostname === 'examshortcut.pages.dev' &&
    ['https://examshortcut.in', 'https://www.examshortcut.in'].includes(parentOrigin)) {
  window.atOptions = { key: unit.key, format: 'iframe', width: unit.width, height: unit.height, params: {} };
  const script = document.createElement('script');
  script.src = 'https://bauval.org/22/' + unit.key;
  document.body.appendChild(script);
}` : '// Serving disabled until the requested category exclusions are confirmed.';
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Advertisement</title><style>html,body{margin:0;padding:0;overflow:hidden;background:transparent}</style></head><body><script>${script}</script></body></html>\n`;
}
if (process.argv[1]?.endsWith('generate-ad-documents.mjs')) {
  fs.mkdirSync('public/advertising', { recursive: true });
  fs.writeFileSync('public/advertising/display.html', buildAdDocument(ADSTERRA_ENABLED, ADSTERRA_CATEGORY_CONFIRMATION));
  console.log(`Adsterra frame: ${ADSTERRA_ENABLED && ADSTERRA_CATEGORY_CONFIRMATION ? 'enabled after category confirmation' : 'disabled; category confirmation pending'}.`);
}
