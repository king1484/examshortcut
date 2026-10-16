import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { isPublicAdPage } from '../src/lib/advertising.ts';
import { MONETAG_MULTITAG_SRC, MONETAG_MULTITAG_ZONE } from '../src/lib/monetag.ts';

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
      const bootstraps = html.match(/<script[^>]*id="monetag-multitag-bootstrap"[^>]*>[\s\S]*?<\/script>/g) || [];
      if (isPublicAdPage(route)) {
        assert.equal(bootstraps.length, 1, `Expected one MultiTag bootstrap on ${route}`);
        assert.ok(html.indexOf(bootstraps[0]) < html.indexOf('</head>'), `MultiTag must be in the head on ${route}`);
        assert.ok(bootstraps[0].includes(MONETAG_MULTITAG_SRC) && bootstraps[0].includes(MONETAG_MULTITAG_ZONE), `Wrong MultiTag embed on ${route}`);
        assert.match(bootstraps[0], /data-cfasync="false"/);
        adPages++;
      } else {
        assert.equal(bootstraps.length, 0, `MultiTag must stay off private pages, forms and tests: ${route}`);
      }
      // The replaced standalone Vignette and Infolinks integrations stay disabled.
      assert.doesNotMatch(html, /monetag-vignette-(?:bootstrap|sdk)|n6wxm\.com\/vignette\.min\.js/, `Vignette tag still present on ${route}`);
      assert.doesNotMatch(html, /infolinks-(?:bootstrap|sdk)|resources\.infolinks\.com\/js\/infolinks_main\.js/, `Infolinks tag still present on ${route}`);
      checked++;
    }
  }
}
await verify(root);
assert.ok(checked > 0, 'No exported pages were checked');
console.log(`Verified MultiTag on ${adPages} public reading pages and exclusions across ${checked} pages.`);
