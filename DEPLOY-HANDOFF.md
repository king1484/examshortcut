# ExamShortcut deployment handoff

## State

- Branch: `master`
- Final commit: current `HEAD` (`Add deployment handoff summary`), containing the verified import commit `36f885f`.
- Working tree was clean after the final commit.
- Deployment has **not** been run. Deploy only after the owner reviews the local build and approves it.

## What was delivered

- 38 complete timed tests with 3,226 imported questions.
- SSC, Railway, UP Police, IBPS PO, IBPS Clerk, SBI Clerk, SBI PO, and CAT imports.
- CAT 2025 Slots 2 and 3 include VARC, DILR, QA, and TITA numeric questions.
- Five-option MCQ rendering and CAT numeric-answer input support.
- MTS per-question negative-marking support.
- Provenance ledger: `content/pyq-imports-2026-10-07.json`.

## Verification

These checks passed:

```text
node scripts/verify-pyq-imports.mjs
  Verified 38 registered imports: 3226 questions, complete sections, unique IDs, valid keys and MTS penalties.

node scripts/verify-pyq-runtime.mjs
  PYQ scoring checks passed.

npx tsc --noEmit
  passed

npm run build
  passed; 1,282 static pages generated
```

The content validator still reports the repository's pre-existing 1,901 errors in legacy `mistakes` fields under `content/core/topics`; the new PYQ files add no validator errors.

## Local review

The static output is served at `http://localhost:4173`.

Useful routes:

- `/exams/cat/mocks/cat-real-2025-1130-s2`
- `/exams/cat/mocks/cat-real-2025-1130-s3`
- `/exams/sbi-clerk/mocks/sbi-clerk-real-2025-0920-s1`
- `/exams/ibps-clerk/mocks/ibps-clerk-pattern-2024-0824-s1`
- `/exams/sbi-po/mocks/sbi-po-pattern-2025-0804-s1`

## Deploy instruction

After owner approval, deploy the current `master` `HEAD` using the project's normal hosting workflow. Do not deploy an older commit or any uncommitted local state.
