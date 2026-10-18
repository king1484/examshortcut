import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import vm from 'node:vm';

const root = path.resolve('out');
let checked = 0;
let banners = 0;
const zones = ['31786624', '31792395', '31792396', '31792397', '31792398', '31792399', '31792392'];
const issued = {
  '300x250': '59e3808cf2d39bca0ebc82811c6249ee',
  '468x60': '20450e07856c27fb0dbc5aa6013720ac',
  '160x300': '8daf048adbebe221d752a368db3181ab',
  '160x600': '230ad824659625c6badc44597930e2c3',
  '320x50': 'ad421e7c46979528e3db607ca2bb682e',
  '728x90': '7e0573e36a571b0d145ab23096b1e4da',
};
const smartlink = 'https://araplhn.org/4/2030aeb2a6b6a453f627153d8cb02b50';
async function verify(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await verify(filename);
    } else if (entry.name.endsWith('.html')) {
      const relative = path.relative(root, filename).split(path.sep).join('/');
      const route = relative === 'index.html' ? '/' : `/${relative.replace(/(?:\/index)?\.html$/, '')}/`;
      const html = await readFile(filename, 'utf8');
      // The live Social Bar test still showed a notification-style card.
      assert.doesNotMatch(html, /31792391|31792394|fddeed3afc5be59e6049e19c4d7ffb40|bauval\.org\/14\//, `Unapproved Adsterra format on ${route}`);
      assert.doesNotMatch(html, /monetag-(?:multitag|vignette)-(?:bootstrap|sdk)|quge5\.com\/88\/tag\.min\.js|n6wxm\.com\/vignette\.min\.js/, `Monetag tag still present on ${route}`);
      assert.doesNotMatch(html, /infolinks-(?:bootstrap|sdk)|resources\.infolinks\.com\/js\/infolinks_main\.js/, `Infolinks tag still present on ${route}`);
      assert.doesNotMatch(html, /runAutoTag|runPop|runInterstitial|runInPagePush|1wj8naoruw/, `Non-display Adcash integration on ${route}`);
      assert.doesNotMatch(html, /data-adcash-zone|acscdn\.com\/script\/aclib\.js/, `Old Adcash integration on ${route}`);
      const slots = [...html.matchAll(/data-adsterra-zone="([^"]+)"/g)];
      // The isolated vendor document is an asset, not another application page.
      if (relative === 'advertising/display.html') {
        assert.doesNotMatch(html, /format['"]?\s*:\s*['"](?:popunder|social|push)/);
        assert.match(html, /59e3808cf2d39bca0ebc82811c6249ee/);
        assert.match(html, /noindex, nofollow/);
        continue;
      }
      if (relative === 'advertising/native.html') {
        assert.match(html, /bauval\.org\/21\/843472de0df6800e210bdae1ed686f7a/);
        assert.match(html, /id="container-843472de0df6800e210bdae1ed686f7a"/);
        assert.match(html, /noindex, nofollow/);
        continue;
      }
      if (/^yandex_[\da-f]+\.html$/.test(relative)) {
        assert.equal(slots.length, 0, 'Search verification documents must stay unchanged');
        continue;
      }
      assert.deepEqual(slots.map(([, zone]) => zone).sort(), [...zones].sort(), `Expected each responsive advertising slot once on ${route}`);
      const link = html.match(/<a\b[^>]*data-adsterra-smartlink="31792393"[^>]*>/)?.[0];
      assert.ok(link, `Sponsored offers missing on ${route}`);
      assert.ok(link.includes(`href="${smartlink}"`), `Wrong Smartlink on ${route}`);
      assert.match(link, /rel="sponsored noopener noreferrer"/);
      assert.match(link, /target="_blank"/);
      for (const [, zone] of slots) {
        assert.ok(zones.includes(zone), `Unrecognised display zone on ${route}`);
        banners++;
      }
      checked++;
    }
  }
}
await verify(root);
// Exercise the real exported loader: local/preview/unknown inputs cannot load ads,
// and every allowed size selects exactly its issued code and dimensions.
const display = await readFile(path.join(root, 'advertising/display.html'), 'utf8');
const loader = display.match(/<script>([\s\S]*?)<\/script>/)[1];
for (const hostname of ['localhost', 'preview.examshortcut.pages.dev', 'examshortcut.in', 'examshortcut.pages.dev']) {
 for (const referrer of ['', 'https://example.com/', 'https://examshortcut.in/', 'https://www.examshortcut.in/']) {
  for (const size of [...Object.keys(issued), '__proto__', 'constructor', 'https://example.com/unsafe.js']) {
    const requests = [];
    const context = { location: { hostname, search: `?size=${encodeURIComponent(size)}` }, URLSearchParams, URL,
      document: { referrer, body: { style: {}, appendChild: (node) => requests.push(node.src) }, createElement: () => ({}) } };
    vm.runInNewContext(loader, context);
    const allowed = hostname === 'examshortcut.pages.dev' && ['https://examshortcut.in/', 'https://www.examshortcut.in/'].includes(referrer) && Object.hasOwn(issued, size);
    assert.deepEqual(requests, allowed ? [`https://bauval.org/22/${issued[size]}`] : [], `Unexpected request for ${hostname}/${size}`);
    if (allowed) {
      const [width, height] = size.split('x').map(Number);
      assert.equal(context.atOptions.width, width);
      assert.equal(context.atOptions.height, height);
      assert.equal(context.atOptions.format, 'iframe');
    }
  }
 }
}
// Allowing vendor storage is safe only on a separate origin, never on the
// account origin. Catch accidental relative iframe URLs before deployment.
const component = await readFile('src/components/DisplayBanner.tsx', 'utf8');
assert.match(component, /const AD_DOCUMENT_ORIGIN = 'https:\/\/examshortcut\.pages\.dev'/);
assert.equal((component.match(/src=\{`\$\{AD_DOCUMENT_ORIGIN\}/g) || []).length, 2);
assert.doesNotMatch(component, /allow-top-navigation/);
assert.ok(checked > 0, 'No exported pages were checked');
assert.ok(banners > 0, 'Display advertising placements missing from export');
console.log(`Verified seven responsive Adsterra slots and a labelled Smartlink on each of ${checked} pages (${banners} total); loader guards passed; no Social Bar, Popunder or old SDKs.`);
