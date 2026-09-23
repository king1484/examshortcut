/* ExamShortcut service worker — offline-first app shell + runtime cache.
   Static export: every page is a static file; cache-on-request keeps visited
   topics/mocks available offline. Content updates via network-first for pages,
   cache-first for static assets. */
const VERSION = 'es-v1';
const SHELL = ['/', '/ssc-cgl/', '/ssc-cgl/syllabus/', '/ssc-cgl/mocks/', '/ssc-cgl/formula-sheet/', '/revision/', '/about/', '/manifest.webmanifest', '/icon.svg'];

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

  // Static assets: cache-first
  if (url.pathname.startsWith('/_next/static/') || /\.(css|js|svg|png|woff2?|webmanifest)$/.test(url.pathname)) {
    e.respondWith(
      caches.match(req).then((hit) => hit || fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(req, copy)).catch(() => {});
        return res;
      }))
    );
    return;
  }

  // Pages: network-first with cache fallback (so content updates land, offline still works)
  e.respondWith(
    fetch(req)
      .then((res) => {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(req, copy)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(req).then((hit) => hit || caches.match('/')))
  );
});
