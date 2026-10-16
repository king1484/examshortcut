import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { isPublicAdPage } from '../src/lib/advertising.ts';
import { monetagIssuedTag } from '../src/lib/monetag.ts';

const root = path.resolve('out');
let checked = 0;
let adPages = 0;
async function verify(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await verify(filename);
    } else if (entry.name.endsWith('.html')) {
      const relative = path.relative(root, filename).split(path.sep).join('/');
      const route = relative === 'index.html' ? '/' : `/${relative.replace(/(?:\/index)?\.html$/, '')}/`;
      const html = await readFile(filename, 'utf8');
      const head = html.match(/<head>([\s\S]*?)<\/head>/)?.[1] || '';
      const tag = /<script\b[^>]*\bid="monetag-vignette-bootstrap"[^>]*>/g;
      const count = [...html.matchAll(tag)].length;
      const eligible = isPublicAdPage(route);
      assert.equal(count, eligible ? 1 : 0, `Unexpected Monetag tag on ${route}`);
      if (eligible) {
        assert.match(head, /id="monetag-vignette-bootstrap"/, `Monetag must be in the head of ${route}`);
        assert.match(head, /<script\s+data-cfasync="false"[^>]*\bid="monetag-vignette-bootstrap"/, `Monetag must opt out of Rocket Loader on ${route}`);
        assert.match(head, /https:\/\/n6wxm\.com\/vignette\.min\.js/);
        assert.match(head, /12047445/);
        assert.ok(head.includes(monetagIssuedTag), `Issued Monetag embed changed on ${route}`);
        adPages++;
      }
      checked++;
    }
  }
}
await verify(root);
assert.ok(checked > 0 && adPages > 0, 'No exported ad pages were checked');
console.log(`Verified Monetag head tag and page exclusions across ${checked} pages (${adPages} reading pages).`);
