<p align="center">
  <img src="public/icon.svg" alt="ExamShortcut" width="72" height="72">
</p>

<h1 align="center">ExamShortcut</h1>

<p align="center">An open-source study platform for Indian competitive exams.<br>Learn the concept. Practise the shortcut. Review your mistakes.</p>

<p align="center">
  <a href="https://examshortcut.in">Use ExamShortcut</a> ·
  <a href="#run-locally">Run locally</a> ·
  <a href="CONTRIBUTING.md">Contribute</a> ·
  <a href="https://github.com/king1484/examshortcut/issues/new/choose">Report an issue</a>
</p>

<p align="center">
  <a href="https://github.com/king1484/examshortcut/actions/workflows/checks.yml"><img src="https://github.com/king1484/examshortcut/actions/workflows/checks.yml/badge.svg?branch=master" alt="Repository checks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Software_license-MIT-blue.svg" alt="Software license: MIT"></a>
</p>

## Why this project exists

Preparing for an exam involves more than collecting questions. Students need clear explanations, timed practice, a way to revisit mistakes, and a study history that stays useful across sessions. ExamShortcut brings those workflows together in a free web app, with structured content that contributors can inspect and improve in Git.

The platform covers SSC, Railways, Banking, and CAT. Public lessons can be read without an account. Progress is stored locally; an optional Firebase account adds cross-device sync. The source is published so developers and educators can improve the software, report incorrect answers, and extend its exam coverage.

## What you can do

- **Learn:** subject notes, worked examples, formula sheets, and shortcut techniques with Markdown and mathematical notation.
- **Practise:** topic quizzes, a rotating daily quiz, and timed computer-based mock tests, including numeric-answer and five-option questions where supported.
- **Review:** bookmarks, mistake tracking, revision tools, scores, and study progress.
- **Plan:** exam hubs, syllabus and cutoff references, study planners, typing practice, and score calculators.
- **Stay informed:** dated exam-shift analysis with source references and checks that withhold unsupported attempt estimates.
- **Use it on different devices:** responsive pages, light/dark themes, and a service worker for the app shell. Offline coverage depends on what has been cached.

ExamShortcut is an independent study aid, not an official examination authority. Check exam notices, dates, and eligibility against the relevant official source. Estimates and recalled questions are not official results or answer keys.

## Run locally

Use **Node.js 24** and npm. Python **3.12** is needed only for the optional analysis collector and its tests.

```bash
git clone https://github.com/king1484/examshortcut.git
cd examshortcut
npm ci
npm run dev
```

Open [localhost:3000](http://localhost:3000). Leave Firebase settings unset for local preview: public study content and local progress work without a cloud account. Login and cloud sync require your own Firebase project.

To configure accounts, copy `.env.example` to `.env.local` (`Copy-Item .env.example .env.local` in PowerShell, or `cp .env.example .env.local` on macOS/Linux), then fill in its four `NEXT_PUBLIC_FIREBASE_*` web-app settings. These are public client configuration, not service-account credentials. Never add private keys or production secrets to Git. See [configuration and hosting](DEPLOY.md).

### Validate your changes

```bash
npm run validate
node --experimental-strip-types --test scripts/test-auth-config.mjs scripts/test-feedback.mjs scripts/test-infolinks.mjs
node scripts/verify-pyq-imports.mjs
node scripts/verify-pyq-runtime.mjs
```

Optional collector checks:

```bash
python -m pip install -r scripts/shift-collector/requirements.txt
python -m unittest discover -s scripts/shift-collector -p "test_*.py"
```

These checks run without production credentials. The content validator checks JSON structure and answer-field contracts; it does **not** prove that every explanation or answer is factually correct. Collector tests use mocked sources rather than running a live collection.

`npm run build` creates the static export in `out/`. Its production preflight currently verifies the maintainer's Firebase domains and Google sign-in provider, so a fresh clone cannot run a production build with blank settings. Local development and repository checks do not need that configuration. Fork owners must adapt the production-specific settings before deploying their own instance; see [DEPLOY.md](DEPLOY.md).

## How it fits together

The application uses Next.js App Router, React, TypeScript, Tailwind CSS, Markdown, and KaTeX. Lessons and questions are loaded from JSON at build time. Firebase supplies optional authentication and progress sync. Cloudflare Pages serves the static export; a Pages Function and D1 handle private student feedback. The optional Python collector produces source-backed shift-analysis data.

```text
content/                  Subject material, exam data, mocks, shift analysis
src/app/                  Pages and routes
src/components/           Lessons, quizzes, mock tests, progress, study tools
src/lib/                  Content loaders, scoring, local storage, Firebase sync
functions/api/            Student feedback endpoint
migrations/               Feedback database schema
scripts/                  Validation, generation, verification, optional collector
public/                   Static assets and service worker
.github/                  Repository checks and contribution templates
```

Read the [architecture notes](docs/ARCHITECTURE.md) for the content model and component map, and [content/SCHEMA.md](content/SCHEMA.md) before editing questions.

## Contributing

Useful contributions include reproducible bug reports, corrected explanations with worked evidence, accessibility improvements, scoring tests, and better contributor setup. Start with [CONTRIBUTING.md](CONTRIBUTING.md). Please check existing issues before beginning a large change.

For an answer correction, include the exam/topic, question ID or URL, the incorrect result, and your derivation or authoritative source. For a security issue, follow [SECURITY.md](SECURITY.md) instead of posting sensitive details in a public issue.

## Maintenance and near-term priorities

[Vinay Singirikonda (@king1484)](https://github.com/king1484) is the primary maintainer. Maintenance includes reviewing content corrections, fixing scoring and interface regressions, validating imported papers, reviewing changes from the analysis collector, and maintaining the hosted app. Repository checks validate contributions; the existing scheduled collector has a separate production workflow.

Current priorities are to improve answer-verification coverage, make self-hosting less coupled to the production domain, expand accessibility checks, and document content provenance and redistribution permissions. These are areas for contribution, not promises of a delivery date. The project has no guaranteed response time.

## License and content rights

The original **software** is available under the [MIT License](LICENSE). See [CONTENT_RIGHTS.md](CONTENT_RIGHTS.md) for the scope and exclusions.

Past-paper questions, source excerpts, third-party images, and other external material are **not automatically licensed under MIT**. Source links and import records document provenance, not permission to redistribute. Check the applicable rights before reusing content or publishing a fork's question bank. No blanket open-content license is granted for `content/` or third-party assets.
