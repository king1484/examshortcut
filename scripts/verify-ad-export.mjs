import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';

const root = path.resolve('out');
const adsenseLine = 'google.com, pub-1700177065699672, DIRECT, f08c47fec0942fa0';
const blockedSdk = /al5sm\.com\/tag\.min\.js|ezojs\.com\/ezoic|ezoicanalytics\.com|gatekeeperconsent\.com|resources\.infolinks\.com|acscdn\.com\/script\/aclib\.js|quge5\.com|n6wxm\.com|bauval\.org|araplhn\.org|data-adsterra/i;
let checked = 0;

async function verify(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await verify(filename);
    } else if (entry.name.endsWith('.js')) {
      const javascript = await readFile(filename, 'utf8');
      assert.doesNotMatch(javascript, blockedSdk, `Unapproved ad SDK in ${filename}`);
    } else if (entry.name.endsWith('.html')) {
      const html = await readFile(filename, 'utf8');
      const route = path.relative(root, filename);
      assert.doesNotMatch(html, blockedSdk, `Old advertising integration on ${route}`);
      if (/^yandex_[\da-f]+\.html$/.test(route)) continue;
      const head = html.match(/<head>([\s\S]*?)<\/head>/)?.[1];
      assert.ok(head, `Missing head on ${route}`);
      assert.match(
        head,
        /<meta name="google-adsense-account" content="ca-pub-1700177065699672"\/?>/,
        `AdSense account meta missing from ${route}`,
      );
      assert.doesNotMatch(html, /ezoic-pub-ad-placeholder-|showAds\s*\(/, `Legacy ad placeholder on ${route}`);
      checked++;
    }
  }
}

await verify(root);
assert.ok(checked > 0, 'No exported application pages checked');

const ads = await readFile(path.join(root, 'ads.txt'), 'utf8');
assert.ok(ads.includes(adsenseLine), 'ads.txt must authorize the AdSense publisher');
assert.doesNotMatch(ads, /infolinks|ezoic|adsterra|adcash/i, 'ads.txt still authorizes a removed ad network');

const redirects = await readFile(path.join(root, '_redirects'), 'utf8');
assert.doesNotMatch(redirects, /^\/ads\.txt\s/m, 'ads.txt must be served locally, not redirected to Ezoic');

console.log(`Verified AdSense-only export: ${checked} pages, local ads.txt, no Monetag/Ezoic/Infolinks/Adsterra SDKs.`);
