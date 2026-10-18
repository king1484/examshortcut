import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';

const root = path.resolve('out');
let checked = 0;
async function verify(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await verify(filename);
    } else if (entry.name.endsWith('.html')) {
      const html = await readFile(filename, 'utf8');
      const route = path.relative(root, filename);
      assert.doesNotMatch(html, /bauval\.org|araplhn\.org|data-adsterra|quge5\.com|n6wxm\.com|al5sm\.com|resources\.infolinks\.com|acscdn\.com\/script\/aclib\.js/, `Old advertising integration on ${route}`);
      if (/^yandex_[\da-f]+\.html$/.test(route)) continue;
      const head = html.match(/<head>([\s\S]*?)<\/head>/)?.[1];
      assert.ok(head, `Missing head on ${route}`);
      for (const url of ['https://cmp.gatekeeperconsent.com/min.js', 'https://the.gatekeeperconsent.com/cmp.min.js', 'https://www.ezojs.com/ezoic/sa.min.js', 'https://ezoicanalytics.com/analytics.js']) {
        assert.ok(head.includes(url), `Ezoic connection script missing from ${route}`);
      }
      assert.doesNotMatch(html, /ezoic-pub-ad-placeholder-|showAds\s*\(/, `Ads must wait for review and category configuration: ${route}`);
      checked++;
    }
  }
}

await verify(root);
assert.ok(checked > 0, 'No exported application pages checked');
const redirects = await readFile(path.join(root, '_redirects'), 'utf8');
assert.match(redirects, /^\/ads\.txt\s+https:\/\/srv\.adstxtmanager\.com\/19390\/examshortcut\.in\s+301$/m);
console.log(`Verified Ezoic connection scripts on ${checked} pages, managed ads.txt, no old ad tags, and no ad placements before approval.`);
