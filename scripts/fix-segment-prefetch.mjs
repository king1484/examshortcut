#!/usr/bin/env node
/* Static export writes each page's prefetch segment as a nested file
     out/exams/ssc-cgl/mocks/__next.exams/ssc-cgl/mocks/__PAGE__.txt
   but the client router requests the flat name
     out/exams/ssc-cgl/mocks/__next.exams.ssc-cgl.mocks.__PAGE__.txt
   so every link prefetch 404s. Write the flat copy next to each nested one.
   Run after `next build`: node scripts/fix-segment-prefetch.mjs */
import fs from 'node:fs';
import path from 'node:path';

const OUT = path.join(process.cwd(), 'out');
let copied = 0;

function walk(dir) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (!fs.statSync(p).isDirectory()) continue;
    if (f === '_next') continue;
    if (f.startsWith('__next.')) flatten(dir, p);
    else walk(p);
  }
}

function flatten(routeDir, segDir) {
  const files = [];
  const collect = (d) => {
    for (const f of fs.readdirSync(d)) {
      const p = path.join(d, f);
      if (fs.statSync(p).isDirectory()) collect(p);
      else files.push(p);
    }
  };
  collect(segDir);
  for (const file of files) {
    const flat = path.basename(segDir) + '.' + path.relative(segDir, file).split(path.sep).join('.');
    const dest = path.join(routeDir, flat);
    if (!fs.existsSync(dest)) {
      fs.copyFileSync(file, dest);
      copied++;
    }
  }
}

if (fs.existsSync(OUT)) walk(OUT);
console.log(`segment prefetch: ${copied} flat copies written`);
