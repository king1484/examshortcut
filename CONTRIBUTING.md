# Contributing to ExamShortcut

Thanks for helping improve the study platform. Small, focused changes are easiest to review.

## Start here

1. Check existing issues for the same bug or correction. Open an issue before a substantial feature or architectural change.
2. Fork the repository and create a branch for one change.
3. Follow the README's local setup. You do not need the maintainer's Firebase, Cloudflare, or LLM credentials to run the basic app and repository checks.
4. Read `AGENTS.md` before framework changes and `content/SCHEMA.md` before content changes.

## What makes a useful contribution

- A bug report with a URL, browser/device details, reproduction steps, and expected versus actual behavior.
- A question correction with its stable ID and a worked derivation or authoritative reference.
- A focused accessibility or usability improvement.
- A regression test for a real scoring, storage, account-configuration, or collector failure.
- Documentation that matches the behavior of a fresh clone.

Never submit user progress exports, real student feedback, email addresses, transcripts containing personal information, credentials, or local environment files. Use synthetic examples.

## Content changes

Read `content/SCHEMA.md` and `CONTENT_RIGHTS.md`. Keep question IDs stable. Provide original wording and explanations for new practice material, with exactly one valid MCQ answer. Verify numeric answers with a reproducible calculation; schema validation alone does not verify correctness. Identify recalled questions and estimates as such. Preserve source links and state redistribution permissions for imported material. Do not copy a commercial preparation site's questions or explanations without permission.

## Before opening a pull request

Run:

```bash
npm run validate
node --experimental-strip-types --test scripts/test-auth-config.mjs scripts/test-feedback.mjs scripts/test-infolinks.mjs scripts/test-score-calculator.mjs
python scripts/test-statistics.py
node scripts/verify-pyq-imports.mjs
node scripts/verify-pyq-runtime.mjs
```

For collector changes, install its requirements and run:

```bash
python -m unittest discover -s scripts/shift-collector -p "test_*.py"
```

Describe the problem, the resulting behavior, and what you checked. Include screenshots for visible UI changes, with personal information removed. Explain any test you could not run. Keep generated builds, scratch data, and unrelated formatting out of the change.

## Production boundaries

Repository checks do not deploy the website or collect live data. Do not run the production workflow, publish a deployment, alter Firebase rules, or write to the production feedback database as part of a contribution. Fork owners need their own service accounts and must review domain-specific configuration before hosting.

## Review and conduct

The primary maintainer reviews changes and may request revisions or decline changes outside the project scope. Feedback should be respectful, specific, and directed at the work. Harassment, discrimination, doxxing, and unsolicited promotion are not welcome. Report conduct concerns through the private contact route in `SECURITY.md`.

Software contributions are offered under the project's MIT license. Educational material and third-party assets follow the separate rules in `CONTENT_RIGHTS.md`.
