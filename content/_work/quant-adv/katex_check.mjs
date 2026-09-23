// KaTeX validation for content JSON files. Usage: node katex_check.mjs f1.json [f2.json ...]
import fs from 'fs';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const katex = require('katex');
let bad = 0, count = 0;
function render(tex, where) {
  count++;
  try { katex.renderToString(tex, { throwOnError: true, strict: 'ignore' }); }
  catch (e) { bad++; console.log(`KATEX ERR ${where}: ${e.message.split('\n')[0]}  <<${tex}>>`); }
}
function segs(s) {
  const out = []; const re = /\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g; let m;
  while ((m = re.exec(s))) out.push(m[1] !== undefined ? m[1] : m[2]);
  return out;
}
function walk(o, p) {
  if (typeof o === 'string') {
    if (o.trimStart().startsWith('<svg')) return;
    if (p.endsWith('.tex')) render(o, p); else segs(o).forEach((t) => render(t, p));
  } else if (Array.isArray(o)) o.forEach((v, i) => walk(v, `${p}[${i}]`));
  else if (o && typeof o === 'object') for (const k of Object.keys(o)) walk(o[k], `${p}.${k}`);
}
for (const f of process.argv.slice(2)) walk(JSON.parse(fs.readFileSync(f, 'utf8')), f.split(/[\\/]/).pop());
console.log(`katex: ${count} math segments, ${bad} errors`);
process.exit(bad ? 1 : 0);
