# ExamShortcut

Free exam-prep site for Indian competitive exams — **SSC · Railways · Banking · CAT** (live at <https://examshortcut.in>).
Notes, formula sheets, shortcut tricks, topic tests, a daily quiz, full CBT-style mock tests, shift-wise exam analysis,
cutoffs and calculators. Public content needs no login; an optional free account syncs progress across devices.

- **Stack:** Next.js (App Router, `output: 'export'` → fully static) · React 19 · Tailwind CSS 4 · TypeScript ·
  react-markdown + remark-math + rehype-katex · Firebase (Auth + Firestore, Spark free tier).
- **Hosting:** Cloudflare Pages, project `examshortcut`. There is no server: `out/` is the whole site.
- **Next.js is non-standard here.** `AGENTS.md` says to read `node_modules/next/dist/docs/` before writing framework code.

## Quick start

```bash
npm ci
cp .env.example .env.local     # fill the 4 NEXT_PUBLIC_FIREBASE_* values (optional, see "Accounts")
npm run dev                    # http://localhost:3000
npm run validate               # parse + schema-check every content JSON
npm run build                  # full production build → out/
```

`npm run build` is a pipeline, not just `next build`:

| Step | Script | What it does |
|---|---|---|
| 1 | `scripts/generate-daily-quiz.mjs` | Builds `public/data/daily/<n>.json` — 30 rotating buckets mixing every subject's practice questions |
| 2 | `scripts/generate-search-index.mjs` | Builds `public/search-index.json` (topics, pages) used by Search and the Dashboard |
| 3 | `scripts/generate-pattern-names.mjs` | Builds `src/data/pattern-names.json` (pattern id → human name) used by the Explanation chip in `QuestionView` |
| 4 | `next build` | Static export to `out/` |
| 5 | `scripts/fix-segment-prefetch.mjs` | Writes the flat `__next.a.b.__PAGE__.txt` copies the client router asks for (otherwise every link prefetch 404s) |
| 6 | `scripts/generate-sitemap.mjs` | `out/sitemap.xml` (skips `noindex` pages) and adds canonical tags |

If the build fails with `EBUSY` on `out/`, a local static server (e.g. `python -m http.server`) is holding that folder — stop it.

## Repository layout

```
content/            ALL site content as JSON (see "Content model")
  SCHEMA.md           authoring rules + the Question/Topic JSON contract — read before writing content
  core/               exam-agnostic subject content shared by every exam
    sections/<section>.json         quant | reasoning | english | ga | computer
    topics/<section>/<topic>.json   notes, patterns, formulas, solved examples, practice set
    current-affairs/<year>.json     monthly current-affairs items (rendered as plain text, not Markdown)
    blurbs.json
  exams/<examId>/     exam-specific data: exam.json, cutoffs.json, weightage.json, mocks/
    mocks/parts/<mockId>--<sectionId>.json   one file per section of a mock paper
  shift-analysis/     per-exam-day analysis: <examSlug>/<YYYY-MM-DD>.json + exams.json registry
  research/, _work/   scratch/research — ignored by build and scans (_work is git-ignored)
public/             static assets copied to out/ root
  _headers, _redirects  Cloudflare Pages caching/security headers and old-URL 301s
  sw.js               service worker (bump VERSION when shipping changed shells)
  manifest.webmanifest, icons, og.png, robots.txt, ads.txt (AdSense pub id)
  data/daily/         GENERATED daily-quiz buckets      search-index.json  GENERATED
scripts/            build-time Node scripts (above) + validate-content.mjs + icon/OG image helpers (Python)
src/
  app/                routes (App Router) — see "Routes"
  components/         UI; subfolders: cat/ (CAT tools), di/ (data-interpretation charts), exam-subpages/ (pattern/eligibility/salary/age pages)
  lib/                data access + shared logic — see "Libraries"
firestore.rules     Firestore security rules (deployed separately, see "Accounts")
firebase.json, firestore.indexes.json
supabase/schema.sql legacy, unused (the app uses Firebase)
DEPLOY.md           hosting notes (partly outdated: it predates Firebase accounts)
```

## Content model

Two layers (details and writing rules in `content/SCHEMA.md`):

1. **Core** (`content/core`) — subjects are shared by every exam. A *topic* file carries notes/subtopics, pattern
   cards (`patterns[].formula` is bare TeX), `pyqPatterns`, `solvedExamples`, a `practice` set and `revision` bullets.
2. **Exam** (`content/exams/<id>`) — an exam only decides which subjects matter and adds its own pattern, cutoffs,
   weightage and mocks. Exams: `ssc-cgl`, `ssc-chsl`, `ssc-cpo`, `ssc-gd`, `ssc-mts`, `ibps-po`, `ibps-clerk`,
   `rrb-ntpc`, `rrb-group-d`, `cat`.

**Rules that matter**
- Content is read at build time by `src/lib/content.ts` (Node `fs`). Client components must import only the
  client-safe modules (`sections.ts`, `exams.ts`, `types.ts`).
- Every string field is **Markdown with `$…$` / `$$…$$` math**, except fields named `.tex` / `.formula`, which are
  bare TeX. Current-affairs text is plain text (no Markdown, so never add `\$` there).
- Math gotchas (all were real bugs): JSON needs doubled backslashes (`"\\frac"`, never a bare `\f`/`\t`/`\b`);
  a literal dollar sign is `\$` in prose, and inside inline math use `\mathdollar` (remark-math closes math at any `$`);
  don't put a space-led `$ … $` pair around symbols.
- Only real, verified questions and answers. Quant answers are checked with Python before being written.

## Routes (`src/app`)

| Route | What |
|---|---|
| `/` | Home: exam picker, daily quiz teaser, tools |
| `/[section]/` · `/[section]/[topic]/` | Subject and topic hub (tabs: overview, `learn/[subtopic]`, `formulas`, `examples`, `practice`) |
| `/learn/`, `/formula-sheet/`, `/quant-formulas/`, `/shortcut-tricks/`, `/vocab/`, `/static-gk/`, `/data-interpretation/` | Cross-subject study pages |
| `/daily-quiz/` | Today's mix (`public/data/daily`, bucket = day-number % 30, IST rollover) |
| `/exams/` · `/exams/[exam]/…` | Exam hubs: `exam-pattern`, `eligibility`, `salary-and-posts`, `cutoffs`, `mocks/[id]` (CBT) |
| `/exams/ssc-cgl/…` | CGL has its own richer pages (posts, calendar, admit-card, rank-estimator, typing test, weightage, syllabus, study-plan, score-calculator) |
| `/exams/cat/…` | CAT syllabus, score calculator, study planner |
| `/exam-analysis/[exam]/[slug]/` | Shift-wise analysis from `content/shift-analysis` |
| `/current-affairs/[year]/[month]/` | Current affairs archive |
| `/dashboard/`, `/revision/` | Personal progress and mistake notebook (behind `AuthGate`) |
| `/leaderboard/` | Opt-in public leaderboard (points only) |
| `/login/`, `/search/`, `/about`, `/contact`, `/privacy`, `/terms`, `/disclaimer` | Utility/legal pages |

`src/app/layout.tsx` holds the head (metadata, AdSense snippet), `AuthProvider`, header, footer (Telegram button,
links) and the service-worker registration.

## Libraries (`src/lib`)

| File | Role |
|---|---|
| `content.ts` | Build-time (Node) loaders for sections, topics, mocks; the only place that reads `content/` |
| `sections.ts`, `exams.ts`, `types.ts` | Client-safe constants: section meta/colours, exam registry, `Question`/`Topic` types |
| `shifts.ts` | Shift-analysis loaders |
| `catSyllabus.ts`, `postDetails.ts`, `destPassages.ts` | Static reference data for CAT, SSC post pages, typing-test passages |
| `store.ts` | **Local-first progress** in `localStorage` (`es-*` keys): mistakes, bookmarks, topic scores, studied, mock attempts, drafts. `useStore()` re-renders on any write |
| `useExam.ts` | Selected exam (`es-exam`) |
| `firebase.ts` | Firebase init; exports `authConfigured`, `auth`, `db`. Without env vars the site runs in "preview mode" (no accounts, everything local) |
| `sync.ts` | When logged in, mirrors the `SYNC_KEYS` store keys to Firestore `user_progress/{uid}`; merges cloud + local on login |
| `streak.ts` | Streak and points maths (`computeStreak`, `computeStats`, `useProgress`). IST calendar days |
| `leaderboard.ts` | Opt-in public leaderboard reads/writes (`leaderboard/{uid}`) |

## Components worth knowing (`src/components`)

- **Rendering:** `Md.tsx` (Markdown + KaTeX pipeline), `MathText.tsx`, `LazyTex.tsx` (client-side KaTeX for `Tex` blocks).
- **Learning flow:** `TopicTabs`, `Lesson`, `SolvedExample`, `PracticeSets`, `TopicQuiz`, `QuestionView`, `StudiedToggle`.
- **Tests:** `MockCBT` (full CBT interface + analysis), `MockList`, `MockAccessGate`, `DailyQuiz`.
- **Account/progress:** `Auth.tsx` (`AuthProvider`, `useAuth`, `AuthGate`, `AccountButton`), `LoginForm`, `Dashboard`,
  `Streak.tsx` (`StreakChip`, `StreakCard`), `Leaderboard.tsx`.
- **Tools:** `ScoreCalculator`, `RankEstimator`, `StudyPlanner`, `PostPlanner`, `DestTyping`, `ExamCutoffs`, `CutoffExplorer`, `ExamCalendar`, `Search`.
- **Chrome:** `SiteHeader` (nav + streak chip + account), `ThemeToggle`, `NavLoader`, `SwRegister`.

Styling: Tailwind 4 plus design tokens and component classes (`.card`, `.btn`, `.btn-brand`, `.chip`, `.tbl`) in
`src/app/globals.css`, with light/dark themes via CSS variables. Keep CTAs calm — no gradients or glow on login prompts.

## Accounts, streak and leaderboard

- **Auth:** Firebase Auth (Google + email link). Optional; everything public works without it.
- **Progress sync:** Firestore `user_progress/{uid}` — private to the owner.
- **Streak:** personal motivation only — never published or ranked. Any studied topic, topic/daily test, mock attempt or
  logged mistake marks that IST day active. Shown in the header chip (links to the daily quiz) and the dashboard; works
  for logged-out visitors from local data.
- **Points:** 10 per studied topic · up to 30 per test (best score) · 25 + best-score% per mock paper. Streak does not count.
- **Leaderboard:** strictly **opt-in** and **real users only** (no seeded/fake entries). Joining writes
  `leaderboard/{uid}` = `{name, points, studied, tests, mocks, updatedAt}`; leaving deletes it.
  Anyone can read the collection, only the owner can write their row (validated shapes in `firestore.rules`).
  Scores are computed client-side, so they are self-reported.
- **Deploying Firestore rules** (needed whenever `firestore.rules` changes; the site deploy does not do this):
  ```bash
  npx firebase-tools login
  npx firebase-tools deploy --only firestore:rules --project examshortcut-app
  ```
  Until the rules are live the leaderboard shows "couldn't be loaded"; nothing else is affected.

Environment variables (`.env.local`, not committed): `NEXT_PUBLIC_FIREBASE_API_KEY`, `_AUTH_DOMAIN`, `_PROJECT_ID`, `_APP_ID`.

## Deploying the site

Cloudflare Pages, static upload of `out/`:

```bash
npm run build
npx wrangler pages deploy out --project-name examshortcut --branch main --commit-dirty=true
```

Verify on the live URL with a cache-buster (`?cb=<random>`). `public/_headers` sets long-cache for `/_next/static/*`
and no-cache for `sw.js`; bump `VERSION` in `public/sw.js` when shell assets change.

## Conventions

- Prefer editing JSON in place; keep CRLF/LF as the file already has. Validate with `npm run validate` after content edits.
- Don't put Node imports in files that client components import.
- New pages that are personal/thin should set `robots: { index: false }` (dashboard, leaderboard do).
- Ads: AdSense publisher snippet is in `layout.tsx` `<head>`; `public/ads.txt` carries the publisher line.
