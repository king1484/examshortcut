# Deploying ExamShortcut

The site is a fully static Next.js export (`out/`). No server, no database —
all user state (mistakes, bookmarks, mock attempts) lives in the visitor's
localStorage. Any static host works; **Cloudflare Pages** is the recommended
default (free, unlimited bandwidth on static, Indian edge presence, custom
domain + free SSL).

## Build

```bash
npm ci
npm run build        # next build && node scripts/generate-sitemap.mjs
```

Deployable artifact: `out/` (index.html + trailingSlash directory routes +
sitemap.xml + PWA assets).

## Cloudflare Pages (recommended)

1. Push the repo to GitHub.
2. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git.
3. Build settings:
   - Framework preset: **None**
   - Build command: `npm run build`
   - Build output directory: `out`
   - Node version: add environment variable `NODE_VERSION` = `22`
4. Custom domain: add `examshortcut.in` (and `www`), then at the domain
   registrar point nameservers to Cloudflare (or CNAME `www` →
   `<project>.pages.dev`).

Notes:
- TrailingSlash routes (`/ssc-cgl/quant/` → `/ssc-cgl/quant/index.html`) are
  served natively by Pages — no `_redirects` needed.
- `sw.js` is served with the right scope automatically. Bump `VERSION` in
  `public/sw.js` when shipping changed shells so clients refresh.
- `manifest.webmanifest`, `icon.svg`, `icon-maskable.svg`, `robots.txt` are
  already in `public/` and land in `out/` root.

## Domain

- Primary: `examshortcut.in` (Cloudflare registrar or any registrar).
- `examshortcut.com` → 301 redirect to `.in` (Cloudflare Redirect Rule:
  `http.host eq "examshortcut.com"` → 301 `https://examshortcut.in{uri}`).

## Post-deploy checklist

- [ ] Lighthouse: PWA installable, ≥90 on all four scores for the homepage.
- [ ] Offline check: load homepage, go offline, reload → shell renders from SW.
- [ ] `https://examshortcut.in/sitemap.xml` lists the topic pages.
- [ ] Google Search Console: submit sitemap, request indexing for `/ssc-cgl/`.
- [ ] Install prompt on Android Chrome works (manifest + SW + icons).

## Play Store TWA (later phase)

Once deployed, a Trusted Web Activity wrapper publishes the same site as an
Android app using Bubblewrap:

```bash
npm i -g @bubblewrap/cli
bubblewrap init --manifest https://examshortcut.in/manifest.webmanifest
bubblewrap build
```

Requires: hosted `assetlinks.json` (Cloudflare Pages `public/.well-known/`)
and a keystore. Only do this after the web version is stable.
