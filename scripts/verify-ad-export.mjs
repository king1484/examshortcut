import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';

const root = path.resolve('out');
let checked = 0;
let monetagBundles = 0;
async function verify(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await verify(filename);
    } else if (entry.name.endsWith('.js')) {
      const javascript = await readFile(filename, 'utf8');
      assert.doesNotMatch(javascript, /quge5\.com\/88\/tag\.min\.js|n6wxm\.com\/vignette\.min\.js|bauval\.org|araplhn\.org/, `Unapproved ad SDK in ${filename}`);
      if (javascript.includes('https://al5sm.com/tag.min.js')) {
        assert.ok(javascript.includes('12061370') && javascript.includes('monetag-onclick-sdk'), 'Unexpected Monetag zone');
        monetagBundles++;
      }
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
assert.equal(monetagBundles, 1, 'Expected one shared standalone Monetag SDK loader');
const redirects = await readFile(path.join(root, '_redirects'), 'utf8');
assert.match(redirects, /^\/ads\.txt\s+https:\/\/srv\.adstxtmanager\.com\/19390\/examshortcut\.in\s+301$/m);
console.log(`Verified Ezoic connection on ${checked} pages, managed ads.txt, one approved standalone Monetag loader, and no Ezoic placements or other ad SDKs.`);
