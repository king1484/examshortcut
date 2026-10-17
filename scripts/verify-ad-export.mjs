import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { isPublicAdPage } from '../src/lib/advertising.ts';

const root = path.resolve('out');
let checked = 0;
let banners = 0;
async function verify(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await verify(filename);
    } else if (entry.name.endsWith('.html')) {
      const relative = path.relative(root, filename).split(path.sep).join('/');
      const route = relative === 'index.html' ? '/' : `/${relative.replace(/(?:\/index)?\.html$/, '')}/`;
      const html = await readFile(filename, 'utf8');
      // Only the issued manual display zone is permitted; bundled formats stay out.
      assert.doesNotMatch(html, /monetag-(?:multitag|vignette)-(?:bootstrap|sdk)|quge5\.com\/88\/tag\.min\.js|n6wxm\.com\/vignette\.min\.js/, `Monetag tag still present on ${route}`);
      assert.doesNotMatch(html, /infolinks-(?:bootstrap|sdk)|resources\.infolinks\.com\/js\/infolinks_main\.js/, `Infolinks tag still present on ${route}`);
      assert.doesNotMatch(html, /runAutoTag|runPop|runInterstitial|runInPagePush|1wj8naoruw/, `Non-display Adcash integration on ${route}`);
      const slots = [...html.matchAll(/data-adcash-zone="([^"]+)"/g)];
      assert.ok(slots.length <= 1, `Duplicate advertising slots on ${route}`);
      for (const [, zone] of slots) {
        assert.equal(zone, '12327298', `Unrecognised display zone on ${route}`);
        assert.ok(isPublicAdPage(route), `Advertising reached a protected route: ${route}`);
        banners++;
      }
      checked++;
    }
  }
}
await verify(root);
assert.ok(checked > 0, 'No exported pages were checked');
assert.ok(banners > 0, 'Display advertising placements missing from export');
console.log(`Verified ${banners} manual display slots across ${checked} pages; no advertising on protected routes or bundled SDKs.`);
