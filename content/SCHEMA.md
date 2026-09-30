# ExamShortcut content schema

ExamShortcut is a multi-exam platform (SSC, Railways, Banking, state PSCs, entrance exams).
Content is split in two layers:

- `content/core/` — **exam-agnostic** section content shared by every exam: `sections/<sectionId>.json`,
  `topics/<sectionId>/<topicId>.json`, `current-affairs/<year>.json`. Write it for any aspirant, not one exam.
- `content/exams/<examId>/` — exam-specific data: `exam.json`, `cutoffs.json`, `weightage.json`, `mocks/`.

(Older paths below that say `content/ssc-cgl/topics/...` now live at `content/core/topics/...`, and
`content/ssc-cgl/{exam,cutoffs,weightage}.json` + `mocks/` live at `content/exams/ssc-cgl/`.)

All content lives under `content/`. Every file is **UTF-8 JSON** and must parse with
`py -3 -c "import json,sys; json.load(open(sys.argv[1], encoding='utf-8'))" <file>`.
Validate every file you write. Invalid JSON breaks the site build.

## Writing rules (all agents)

- **Original content only.** Do NOT copy question text, explanations or notes verbatim from Testbook,
  Adda247, Oliveboard, BYJU'S, Kiran, Arihant, IndiaBix or any book/site. Facts, formulas, syllabus,
  official exam data and cutoffs are fine (cite the source). Write every question and explanation yourself.
- Questions should look and feel like real SSC CGL questions (same style, difficulty, option traps),
  modelled on actual recurring PYQ patterns — but freshly written with new numbers/words.
- **Correctness is the product.** Every Quant / numeric reasoning answer must be verified by running
  Python (`py -3`, sympy is fine: `py -3 -m pip install sympy` if missing) before you write it.
  Exactly one option must be correct; the other three must be plausible wrong answers (common mistakes).
  If you cannot verify a question, drop it.
- Math: write LaTeX inside `$...$` (inline) or `$$...$$` (display). In JSON every backslash is doubled:
  `"$\\frac{a}{b}$"`. Easiest safe path: build the data as Python dicts and `json.dump(..., ensure_ascii=False, indent=1)`
  from a script file (write the .py with the Write tool, not a bash heredoc — heredocs eat backslashes).
- Text fields are **Markdown** (bold, lists, tables allowed). Keep explanations tight, exam-oriented, Indian English.
- Shortcut/trick = the fast exam method (e.g. "use options", "digit sum check", "percentage fraction table",
  "assume LCM work"). Always show the standard method briefly and the shortcut clearly.
- Figure-based reasoning (mirror images, paper folding, embedded figures, cubes, counting figures):
  describe the technique in text; for questions use text/ASCII-describable variants or inline SVG in
  the `figure` field (a raw `<svg ...>...</svg>` string, viewBox based, stroke="currentColor", no external refs).
- IDs: lowercase kebab-case, stable, unique within the file (`percentage`, `pct-q07`).

## Question object (used everywhere)

```json
{
  "id": "pct-q01",
  "q": "Question text in Markdown, math in $...$",
  "figure": null,
  "options": ["...", "...", "...", "..."],
  "answer": 2,
  "solution": "Standard step-by-step solution (Markdown)",
  "shortcut": "Fast exam trick solution, or null",
  "difficulty": "easy | medium | hard",
  "subtopic": "subtopic-id this tests",
  "pattern": "short name of the recurring PYQ pattern this mirrors, e.g. 'successive discount equivalent'",
  "timeSec": 45
}
```
`answer` is the 0-based index into `options`. Always exactly 4 options.

## Topic file: `content/ssc-cgl/topics/<sectionId>/<topicId>.json`

sectionIds: `quant`, `reasoning`, `english`, `ga`, `computer`.

```json
{
  "id": "percentage",
  "sectionId": "quant",
  "title": "Percentage",
  "order": 4,
  "importance": "high | medium | low",
  "avgQuestions": { "tier1": 2, "tier2": 3 },
  "summary": "2-3 line overview: what it is and why it matters in CGL",
  "subtopics": [
    {
      "id": "pct-fraction-table",
      "title": "Percentage ↔ fraction conversion",
      "concept": "Markdown explanation of the concept",
      "formulas": [ { "name": "Successive change", "tex": "a+b+\\frac{ab}{100}", "note": "use signs for decrease" } ],
      "tricks": [ { "title": "Fraction table", "body": "Markdown", "example": { "q": "...", "solution": "..." } } ],
      "mistakes": [ "Common mistake 1" ]
    }
  ],
  "pyqPatterns": [
    { "pattern": "Successive discount", "frequency": "very common | common | occasional", "howToSpot": "...", "approach": "..." }
  ],
  "solvedExamples": [ Question, ... ],     // 3-5, fully worked, include shortcut
  "practice": [ Question, ... ]            // 12-15, mixed difficulty, topic-wise mock test
}
```
`formulas[].tex` is LaTeX WITHOUT surrounding `$` (the site wraps it). May be empty `[]` for non-math topics.
For GA/English, `formulas` can be `[]`; put facts/lists in `concept` (Markdown tables are great) and
mnemonics in `tricks`.

## Section index: `content/ssc-cgl/sections/<sectionId>.json`

```json
{
  "id": "quant",
  "name": "Quantitative Aptitude",
  "short": "Quant",
  "tier1": { "questions": 25, "marks": 50 },
  "tier2": { "questions": 30, "marks": 90 },
  "overview": "Markdown",
  "strategy": "Markdown: how to prepare this section, order of topics, time plan, attempt strategy",
  "topics": ["number-system", "percentage", "..."]   // topic ids in study order (only ones whose files exist)
}
```
(Quant has two topic agents — the section file for quant is written by the Quant-Advanced agent after
the arithmetic list is known: arithmetic topic ids are listed in this schema below.)

Quant arithmetic topic ids: `number-system`, `simplification`, `hcf-lcm`, `percentage`, `ratio-proportion`,
`average`, `interest`, `profit-loss-discount`, `mixture-alligation`, `time-work`, `time-speed-distance`.
Quant advanced topic ids: `algebra`, `geometry`, `mensuration-2d`, `mensuration-3d`, `trigonometry`,
`heights-distances`, `statistics`, `data-interpretation`.

Reasoning topic ids: `analogy`, `classification`, `series`, `coding-decoding`, `mathematical-operations`,
`missing-number`, `blood-relations`, `direction-distance`, `order-ranking`, `seating-arrangement`, `syllogism`,
`venn-diagrams`, `dictionary-order`, `statement-conclusion`, `counting-figures`, `mirror-water-image`,
`paper-folding-cutting`, `embedded-figures`, `cube-dice`, `figure-series`.

English topic ids: `reading-comprehension`, `cloze-test`, `error-spotting`, `sentence-improvement`,
`fill-in-the-blanks`, `synonyms-antonyms`, `one-word-substitution`, `idioms-phrases`, `spelling`,
`active-passive`, `direct-indirect`, `sentence-rearrangement`, `grammar-essentials`.

GA topic ids: `ancient-history`, `medieval-history`, `modern-history`, `art-culture`, `polity`,
`indian-geography`, `world-geography`, `economy`, `physics`, `chemistry`, `biology`, `static-gk`, `current-affairs`.

Computer topic ids: `computer-fundamentals`, `hardware-memory`, `software-os`, `ms-word`, `ms-excel`,
`ms-powerpoint`, `internet-email`, `networking`, `cyber-security`, `keyboard-shortcuts`.

## Mock section sets: `content/ssc-cgl/mocks/parts/<mockId>--<sectionId>.json`

```json
{ "mockId": "t1-mock-1", "sectionId": "quant", "questions": [ Question, ... ] }
```
Mock ids and sizes:
- `t1-mock-1` — Tier 1 full mock. quant 25, reasoning 25, english 25, ga 25.
- `t1-pyq-2025` — Tier 1 "PYQ-pattern" paper: same topic distribution and difficulty as the
  actual CGL 2025 Tier 1 shifts (use published exam analyses for the topic-wise count), but original questions.
  quant 25, reasoning 25, english 25, ga 25.
- `t2-mock-1` — Tier 2 Paper 1 mock. quant 30, reasoning 30, english 45, ga 25, computer 20.
Mock questions must NOT duplicate topic practice questions. Spread topics like the real paper.
English sets must include 1 reading comprehension passage (5 Qs) and 1 cloze test (5 Qs) for Tier 1
(Tier 2: 2 RC + 1 cloze); put the passage text in each question's `q` via a shared lead-in
(`"passage"` field allowed: `"passage": "Markdown passage"` on the first question of the group and
`"group": "rc1"` on all questions in the group).


---

## Phase 2: deep subtopic content (added 2026-09-24)

Every subtopic gains detailed notes and a catalogue of question types; every subtopic gets its own practice set.
**Existing fields and ids stay** (URLs are indexed): never rename or delete a topic/subtopic id or an existing
question. You may ADD new subtopics where the topic is missing an important sub-area (e.g. HCF/LCM of fractions).

### Writing style (Phase 2)
- **Simple English.** Short sentences, everyday words, explain every term the first time. Write for a
  first-time aspirant from a Hindi/regional-medium school. No jargon without a one-line meaning.
- Exam-neutral: say "competitive exams" / "SSC, Railway, Banking exams", not "SSC CGL" only.
- **No links, URLs, "Source:" lines, book or website names.** Original writing only.
- Markdown; headings inside `notes` use `###` only (the page already uses h2 for the subtopic title).
- Math in `$...$` / `$$...$$`, backslashes doubled in JSON (build via a Python script + json.dump).

### Subtopic additions
```json
{
  "id": "...", "title": "...", "concept": "(keep — short intro)", "formulas": [...], "tricks": [...], "mistakes": [...],

  "notes": "Markdown, 2500-5000 characters. The full lesson: what it is (with an everyday example),
            the basic idea step by step, every rule/formula explained in words with a small worked number,
            special cases, a quick-revision table or bullet list at the end (### Quick revision).",

  "patterns": [                      // 4-8 question TYPES asked from this subtopic, most common first
    {
      "id": "hl-p1",                  // unique within the topic file
      "name": "Largest number dividing a, b, c leaving the same remainder r",
      "frequency": "very common | common | occasional",
      "howToSpot": "Plain words: the words/shape of the question that tell you it is this type",
      "formula": "LaTeX without $ (the dedicated formula for this type), or null for non-math types",
      "logic": "Markdown: numbered steps to solve + one line on WHY it works",
      "example": { "q": "Markdown question", "solution": "Markdown step-by-step solution, ending with the answer" }
    }
  ]
}
```

### Topic-level `pyqPatterns` (rewrite richer, simple English)
Keep the same keys, make each 2-4 sentences, add `example` and `subtopic`:
`{ "pattern", "frequency", "howToSpot", "approach", "subtopic": "<subtopic id>", "example": { "q", "solution" } | null }`
6-10 per topic, covering the whole topic.

### Practice (per subtopic)
Append new questions to the topic's `practice` array. Target **>= 12 practice questions per subtopic**
(existing ones count) and **every pattern covered by >= 2 questions**. Each new question sets
`"subtopic"` to its subtopic id and `"pattern"` to the pattern **id** (e.g. `"hl-p1"`). Mixed difficulty
(~30% easy, 50% medium, 20% hard). New question ids: `<subtopicId>-pNN`, unique in the file.
Same Question contract as above (4 unique options, 0-based answer, solution, shortcut when there is one).
Quant/numeric answers MUST be computed by Python in your build script (assert the stored answer equals the
computed value); if a question can't be verified, drop it.

## Phase 3: readable lessons (added 2026-09-29)

The subtopic page now renders each `###` of `notes` as its own numbered section, lifts traps and recaps
into dedicated blocks, and shows every worked example as "try it first, then reveal the steps".
Reference implementation: `content/_work/readable/quant/tw_pipes.py` (Time & Work > Pipes & Cisterns).

### Writing rules (stricter than Phase 2)
- One idea per sentence, **20 words or fewer**. Active voice. Everyday words ("speed", not "efficiency rate").
  Define a term in plain words the first time it appears. No filler ("bookkeeping", "note that", "it is worth").
- Open every notes section with the idea in one sentence, then a small worked number. Show, then tell.
- Teach the **one fastest reliable method** first (e.g. LCM units in time & work), then the formula shortcut.
- Original writing only. Never copy wording from any website, book or app. No links or sources.

### Subtopic fields
- `concept`: 2-4 short sentences, plain words, **no display math**. "The idea in one minute".
- `notes`: 2500-5000 chars, 4-8 `###` sections. Headings are plain phrases, no numbers (the page numbers them).
  **No "Common traps" / "Quick revision" sections** — those go in `mistakes` / `revision`.
  Callouts: a blockquote starting with a bold label, e.g. `> **Rule:** …`, `> **Tip:** …`, `> **Watch:** …`,
  `> **Note:** …`, `> **Example:** …`. Use 2-5 per subtopic. Put `$$…$$` on its own line.
  In running text use `\dfrac` for fractions (plain `\frac` renders tiny inline).
- `patterns`: 5-8 question types where the subtopic really has them (never pad), most common first.
  Keep every existing pattern id (practice questions point to them); new ids continue the topic's sequence.
  Each: `name`, `frequency`, `howToSpot` (the words in the question that give it away), `formula` (or null),
  `steps` (3-5 short imperative steps), `why` (one sentence),
  `example`: `{ "q", "steps": [2-5 short lines], "answer": "short final answer" }`. Drop `logic`/`solution`.
- `mistakes`: 4-6 `{ "wrong": "what students do", "right": "what to do instead" }`.
- `revision`: 4-8 one-line takeaways (formulas allowed).
- `tricks`: keep useful ones, rewrite in the same plain style; `example` uses `steps` + `answer`.
- `formulas`: keep; add a `note` in words where the symbol meaning is not obvious.
- Quant/reasoning numbers: every number in every example is recomputed in the build script with
  `fractions.Fraction` / asserts. GA/English/computer: keep facts exactly as they are; do not add new facts
  you cannot state with certainty.
- Validate with `python content/_work/readable/validate.py <topic json files…>` before finishing.
