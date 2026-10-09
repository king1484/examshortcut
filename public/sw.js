/* ExamShortcut service worker — offline-first app shell + runtime cache.
   Static export: every page is a static file; cache-on-request keeps visited
   topics/mocks available offline. Content updates via network-first for pages,
   cache-first for static assets. */
const VERSION = 'es-v7';
const SHELL = ['/', '/exams/', '/exams/ssc-cgl/', '/learn/', '/daily-quiz/', '/exams/ssc-cgl/mocks/', '/formula-sheet/', '/revision/', '/about/', '/search/', '/manifest.webmanifest', '/icon.svg', '/search-index.json'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()).catch(() => {}));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  // Hashed build assets never change under the same URL: cache-first
  if (url.pathname.startsWith('/_next/static/')) {
    e.respondWith(
      caches.match(req).then((hit) => hit || fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(req, copy)).catch(() => {});
        return res;
      }))
    );
    return;
  }

  // Un-hashed assets (search-index.json, icons, manifest) change between deploys:
  // serve the cached copy instantly, refresh it in the background
  if (/\.(css|js|json|svg|png|woff2?|webmanifest)$/.test(url.pathname)) {
    e.respondWith(
      caches.open(VERSION).then((c) => c.match(req).then((hit) => {
        const fresh = fetch(req).then((res) => { if (res.ok) c.put(req, res.clone()).catch(() => {}); return res; });
        if (hit) { fresh.catch(() => {}); return hit; }
        return fresh;
      }))
    );
    return;
  }

  // Pages + RSC payloads: network-first, so a deploy is picked up at once and
  // payloads never point at chunk hashes from an older build; offline falls
  // back to cache, then the home shell. Speed comes from next/link prefetch.
  e.respondWith(
    fetch(req)
      .then((res) => {
        if (res.ok) { const copy = res.clone(); caches.open(VERSION).then((c) => c.put(req, copy)).catch(() => {}); }
        return res;
      })
      .catch(() => caches.match(req).then((hit) => hit || caches.match('/')))
  );
});
