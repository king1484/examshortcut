# Deep-content brief (Phase 2) — read fully before starting

Project: ExamShortcut, a free multi-exam prep website (SSC, Railways, Banking, state exams...).
Repo root: `C:\Users\Vinay Singirikonda\Desktop\examshortcut` (Windows; Git Bash + PowerShell available).

Goal: make every subtopic of your assigned topics a complete lesson that an aspirant can learn from
without any other website or book: detailed simple-English notes, every question TYPE asked from it
(with its own formula / logic and a worked example), and a practice set per subtopic.

1. Read `content/SCHEMA.md` fully — especially "Phase 2: deep subtopic content" at the bottom. It is the contract.
2. Topic files: `content/core/topics/<section>/<topic>.json`. Read the existing file first; keep every
   existing id, field and question. Only ADD: `notes` + `patterns` on each subtopic, richer `pyqPatterns`
   (rewrite allowed, same keys + `subtopic` + `example`), new `practice` questions. You may add missing
   subtopics (full content: concept, formulas, tricks, mistakes, notes, patterns, practice) if the topic
   clearly lacks a commonly-asked sub-area — keep new subtopic ids short kebab-case.
3. Work method: for each topic, write a Python build script `content/_work/deep/<section>/<topic>.py`
   (use the Write tool, never a bash heredoc — heredocs eat backslashes). It loads the JSON, adds content
   from Python dicts, runs checks, and writes back with
   `json.dump(data, f, ensure_ascii=False, indent=1)` (UTF-8). Splitting one topic into several scripts
   (e.g. one per subtopic, merged by id so re-running is idempotent) is fine. Run with `py -3 <script>`.
   Make scripts idempotent: re-running must not duplicate questions/patterns (upsert by id).
4. Correctness is the product:
   - Quant / numeric reasoning: compute every answer in Python inside the script and `assert` that
     `options[answer]` equals the computed value. Distractors = realistic mistakes. Drop anything you can't verify.
   - Verbal/GA/computer: exactly one defensible answer; no "all of the above" tricks with two right options.
   - GA facts: only facts you are sure of; if unsure, check with WebFetch (Wikipedia is fine to READ) or skip.
     Avoid office-holders and anything that changes often.
   - After writing, scan string fields for accidental control characters from bad escapes
     (`\f`, `\t`, `\b`, `\r` inside LaTeX like `\frac` written with a single backslash in a non-raw string).
     Use raw strings `r"..."` for LaTeX in Python.
5. Validate after every topic: `node scripts/validate-content.mjs` must print "All content valid".
   Also check your own targets: every subtopic has `notes` (2500-5000 chars) and 4-8 `patterns`;
   every subtopic has >= 12 practice questions; every pattern id is used by >= 2 practice questions.
   Print a small table per topic from your script to prove it.
6. Style: simple English, short sentences, explain terms, Indian context and ₹ in examples. Exam-neutral
   wording ("in competitive exams", "SSC, Railway and Banking papers ask..."). NO URLs, NO "Source:" lines,
   NO names of books, coaching sites or apps. Original writing only — do not copy from any website.
7. Do NOT touch anything outside your assigned topic files and your `content/_work/deep/<section>/` folder.
   Do NOT run git commands, npm build, or deploy. Other agents are editing other topic files in parallel.
8. Finish topic by topic (save + validate each before starting the next) so partial progress survives.
   Final reply: a short table per topic — subtopics (before→after), patterns, practice (before→after),
   notes avg chars, anything you skipped or couldn't verify.
