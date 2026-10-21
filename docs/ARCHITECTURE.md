# Architecture notes

## Application and hosting

Next.js App Router exports the application as static HTML and assets (`output: 'export'`, trailing-slash routes). React and TypeScript implement interactive quizzes and progress views. Tailwind CSS supplies styles; Markdown, remark-math, rehype-katex, and KaTeX render educational content.

Most pages need no server runtime. Cloudflare Pages serves `out/`. The optional feedback API is a Pages Function backed by D1, so feedback requires more than uploading static files. Firebase supplies optional accounts and Firestore progress sync.

## Content model

- `content/core/`: shared sections, topics, notes, examples, practice sets, and current affairs.
- `content/exams/<examId>/`: exam metadata, cutoffs, weighting, mock definitions, and section files.
- `content/shift-analysis/`: dated analyses and the exam registry.
- `content/SCHEMA.md`: field contracts, mathematical-notation rules, and authoring requirements.
- `content/pyq-imports-2026-10-07.json`: provenance ledger for one batch of imports; it is not a license grant.

`src/lib/content.ts` reads JSON during the build. Client components must use client-safe constants and types rather than importing Node filesystem loaders. Keep stable IDs when correcting existing questions.

Most prose fields accept Markdown and inline/display math. Formula/TeX fields hold bare TeX. JSON requires escaped backslashes; current-affairs copy is rendered as plain text. Consult the schema for the particular field rather than assuming all strings use the same renderer.

## Interactive features

- `TopicTabs`, `Lesson`, `SolvedExample`, `PracticeSets`, `TopicQuiz`, and `QuestionView`: study and practice.
- `MockCBT`, `MockList`, `MockAccessGate`, and `DailyQuiz`: timed practice and test review.
- `src/lib/questionScore.ts`: question scoring, including numeric answers and question-specific penalties.
- `ScoreCalculator`, `RankEstimator`, `StudyPlanner`, `PostPlanner`, `DestTyping`, and `Search`: study tools.
- `Md.tsx`, `MathText.tsx`, and `LazyTex.tsx`: prose and mathematics rendering.

## Accounts and progress

`src/lib/store.ts` stores mistakes, bookmarks, scores, mock attempts, and drafts locally using `es-*` storage keys. Without Firebase configuration, development runs in local preview mode.

`src/lib/firebase.ts` initializes Firebase when all four public web configuration values are present. `src/lib/sync.ts` mirrors selected progress keys into `user_progress/{uid}` and merges progress on login. Firestore rules constrain access. Streaks use Indian calendar dates. The optional leaderboard stores client-computed scores; those scores are self-reported, not independently verified examination results.

`functions/api/feedback.js` accepts feedback and feature requests independently of Firebase login. D1 stores submissions privately. The public API has no feedback-listing endpoint. Treat email addresses and submission text as personal data and never attach real records to an issue.

## Build and verification

`npm run build` first validates production Firebase configuration, checks the advertising integration, generates daily quiz buckets, search data and pattern names, then runs the Next.js export. Post-build scripts verify the exported advertising/account setup, repair segment-prefetch paths, and generate the sitemap. Some generated source/public files can change when building; keep unrelated generated differences out of pull requests.

`npm run validate` checks JSON shape and question answer-field contracts. Import and scoring scripts check additional invariants. None of these replaces independent answer checking, source review, or browser testing.

## Optional analysis collector

`scripts/shift-collector/` collects external review sources, extracts structured facts using configured providers, checks evidence quality, and writes dated analysis. Network blocks and provider failures can leave analyses incomplete. Unsupported estimates should be withheld rather than invented. The collector is optional for local study-app development.

YouTube requests try up to three configured HTTP(S) proxies before direct access and the independent transcript fallback. Store one proxy per line in the optional `YT_PROXIES` Actions secret; the existing `YT_PROXY` single-endpoint secret still works. Locally, an ignored `scripts/shift-collector/proxy.txt` is used only when neither environment setting is present. Entries accept `http://user:password@host:port` or `host:port:user:password` (the latter safely encodes credential characters). An unavailable endpoint is skipped for later transcripts in the same run; a video with no captions does not disable other videos. Logs identify routes by number, never by address or credentials. A dead proxy still requires replacement; adding retries cannot make it reachable.

`.github/workflows/shift-analysis.yml` is the existing scheduled production collector/build/deployment workflow. `.github/workflows/checks.yml` runs contributor checks without production secrets, live collection, or deployment. Their responsibilities are separate.
