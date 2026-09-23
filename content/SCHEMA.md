# ExamShortcut content schema (SSC CGL, Phase 1)

All content lives under `content/ssc-cgl/`. Every file is **UTF-8 JSON** and must parse with
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
