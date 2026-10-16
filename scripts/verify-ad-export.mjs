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
      const relative = path.relative(root, filename).split(path.sep).join('/');
      const route = relative === 'index.html' ? '/' : `/${relative.replace(/(?:\/index)?\.html$/, '')}/`;
      const html = await readFile(filename, 'utf8');
      // Advertising stays off while a regular display provider reviews the site.
      assert.doesNotMatch(html, /monetag-(?:multitag|vignette)-(?:bootstrap|sdk)|quge5\.com\/88\/tag\.min\.js|n6wxm\.com\/vignette\.min\.js/, `Monetag tag still present on ${route}`);
      assert.doesNotMatch(html, /infolinks-(?:bootstrap|sdk)|resources\.infolinks\.com\/js\/infolinks_main\.js/, `Infolinks tag still present on ${route}`);
      checked++;
    }
  }
}
await verify(root);
assert.ok(checked > 0, 'No exported pages were checked');
console.log(`Verified no Monetag or Infolinks advertising SDK across ${checked} pages.`);
