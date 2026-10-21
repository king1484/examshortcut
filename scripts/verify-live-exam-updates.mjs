import fs from 'node:fs';
import assert from 'node:assert/strict';
const items = JSON.parse(fs.readFileSync('content/exam-updates.json', 'utf8')).filter(item => item.published);
const routes = ['/exam-updates/', '/results/', '/answer-keys/', ...items.map(item => `/exam-updates/${item.slug}/`)];
for (let attempt = 0; attempt < 8; attempt++) {
  const results = await Promise.all(routes.map(async route => {
    try {
      const response = await fetch(`https://examshortcut.in${route}`, { headers: { 'Cache-Control': 'no-cache' }, signal: AbortSignal.timeout(20000) });
      const html = await response.text();
      const item = items.find(item => route === `/exam-updates/${item.slug}/`);
      return response.ok && html.includes('<h1') && (!item || html.includes(`property="article:modified_time" content="${item.updatedAt}"`));
    } catch { return false; }
  }));
  if (results.every(Boolean)) { console.log(`Live exam updates: ${routes.length} routes and article versions verified.`); process.exit(0); }
  if (attempt === 7) assert.fail('Live exam update pages did not propagate: ' + routes.filter((_, i) => !results[i]).join(', '));
  await new Promise(resolve => setTimeout(resolve, 10000));
}
