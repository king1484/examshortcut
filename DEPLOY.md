# Configuration and hosting

This document describes the current configuration. Reading it or running repository checks does not deploy anything. Production service settings and the existing collector workflow are maintainer-controlled.

## Local preview

Use Node.js 24, run `npm ci`, then `npm run dev`. With no Firebase environment variables, public content and browser-local progress work in preview mode. Login and cloud sync are unavailable. Run the README's validation commands without production credentials.

## Optional Firebase accounts

Copy `.env.example` to ignored `.env.local` and supply the four `NEXT_PUBLIC_FIREBASE_*` values from **your own** Firebase web app. Enable the intended sign-in providers and configure authorized domains. Deploy reviewed Firestore rules to your own project for progress sync and the optional leaderboard. Never use the production project's accounts or request its private credentials for a fork.

The `NEXT_PUBLIC_*` settings identify a web application and are browser-visible. Service-account credentials and provider API keys are private and must not use that prefix or be committed.

## Current production build constraints

`npm run build` generates `out/`, but first calls `scripts/check-auth-config.mjs`. That script makes Firebase configuration requests and verifies the production `examshortcut.in` domains and Google provider. It rejects blank or mismatched settings. This protects the existing deployment from accidentally losing login.

A fresh clone can run development and repository checks without those settings; it cannot produce a successful production build with blank configuration. Self-hosting on a different domain currently requires adapting the production-specific checks and references. Also review canonical URLs, sitemap generation, redirects, service-worker behavior, analytics/advertising identifiers, feedback origin checks, and the scheduled workflow. Domain-neutral production builds are a future improvement, not an implemented feature.

## Hosting components

- **Study pages:** the generated `out/` directory is static.
- **Accounts/progress:** Firebase Auth and Firestore, with project-specific configuration and rules.
- **Feedback:** Cloudflare Pages Functions in `functions/`, a D1 database, and `migrations/feedback.sql`. A static-only host does not provide this endpoint.
- **Collector:** optional Python tooling with its own provider/network configuration. It is not necessary for ordinary development.

The checked-in `wrangler.jsonc`, `firebase.json`, and existing scheduled workflow describe the maintainer's deployment. Fork owners must create and bind their own resources. Do not run database migrations, publish to the production Cloudflare project, or deploy Firebase rules merely to verify a documentation or software contribution.

## Workflows

`checks.yml` validates contributions without production secrets or deployment. The existing `shift-analysis.yml` can collect sources, commit analysis updates, build, and deploy the production site; do not dispatch it for a documentation change. Fork owners should review and configure scheduled automation before enabling it in their own repository.

## Historical notes

`DEPLOY-HANDOFF.md` records an earlier import/deployment handoff. Its counts, validation results, local-server status, and deployment instructions are historical rather than current release guarantees. Follow the current README and package scripts for contributor checks.
