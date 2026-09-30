# Readable-lessons rewrite: agent brief

Repo: `C:\Users\Vinay Singirikonda\Desktop\examshortcut` (Next.js static site, exam prep for SSC/Railway/banking).
Feedback from a real student: the subtopic lessons are "clumsy, not readable, not user friendly, the English is not good,
not understandable". Your job: rewrite the lesson content of your assigned topics so a 12th-pass student reading
in their second language understands it on the first read. Also add more question types (patterns) and clear
step-by-step solution methods.

## Read first (in this order)
1. `content/SCHEMA.md`, especially the **Phase 3: readable lessons** section at the end. It is the spec. Follow it exactly.
2. `content/_work/readable/quant/tw_pipes.py`: the finished reference rewrite (Time & Work > Pipes & Cisterns).
   Copy its *structure and tone*, not its topic. Note how it:
   - opens every section with one plain sentence and then a tiny worked number
   - uses `> **Rule:** / **Tip:** / **Watch:** / **Example:**` callouts
   - keeps every old pattern id and adds new ones
   - gives every pattern a `howToSpot`, 3-5 imperative `steps`, a one-line `why`, and an `example` with `q`, `steps` and `answer`
   - moves traps into `mistakes` ({wrong, right}) and the recap into `revision`
   - asserts every number
3. Your topic JSON files at `content/core/topics/<section>/<topic>.json` (current content: the facts are your source material).
4. `src/lib/types.ts` (Subtopic, QuestionPattern, WorkedExample, Mistake, Trick) for the exact field shapes.

## What to produce
For each assigned topic, write `content/_work/readable/<section>/<topic_id_with_underscores>.py` that loads the topic
JSON, replaces these fields on **every** subtopic: `concept`, `notes`, `patterns`, `mistakes`, `revision`,
and `tricks` / `formulas` where they need a plain-English rewrite. It then writes the JSON back
(`json.dump(t, f, ensure_ascii=False, indent=1)`, utf-8, newline='\n'), then run it.
Do NOT change `id`, `title`, `practice`, `solvedExamples`, `pyqPatterns` or any other top-level field.
One script per topic, so a mistake only reruns one topic. Use the **Write tool** to create scripts (Bash heredocs eat
backslashes in LaTeX). Use raw strings `r"..."` for anything containing LaTeX.

Python: `"C:/Users/Vinay Singirikonda/AppData/Local/Programs/Python/Python312/python.exe"` (bare `python` is the wrong env).
Validate: `<python> content/_work/readable/validate.py content/core/topics/<section>/<topic>.json` from the repo root.
Finish only when every one of your files shows **0 errors**. Fix warnings about long sentences and missing callouts too.

## Quality bar (the whole point)
- Short sentences (max ~20 words), active voice, common words. Say "speed", not "rate of efficiency".
  Explain every term the first time. No filler: "bookkeeping", "sign discipline", "it is worth noting", "leverage", "robust".
- Structure beats prose: small tables, numbered steps and bullets are fine inside sections. Walls of text are not.
- Teach the single most reliable method first, then shortcuts.
- Questions in pattern examples must look like real exam questions (SSC CGL/CHSL, RRB NTPC, IBPS PO level), be original
  (never copied from any website, book or app), and be solvable in under 90 seconds.
- 5-8 patterns where the subtopic genuinely has that many question types; 3-4 is fine for narrow subtopics. **Never pad.**
  Keep all existing pattern ids (practice questions link to them). New ids continue the topic's numbering
  (check the max existing id across the whole topic file first; ids must be unique within the file).
- **Quant/reasoning:** compute every number in every example inside the script (Fraction, integer math, small
  simulations) and `assert` it equals the answer text you wrote. A wrong answer is the worst possible bug.
- **GA/computer/english:** keep every fact that is in the current notes (reorganise it, tables are good) and keep facts exactly
  as stated. Do not add a new fact, date, number or name unless you are certain of it. When in doubt, leave it out.
  English examples: grammar must be correct and uncontroversial (standard Indian exam grammar conventions).
- Math: `$…$` inline, `$$…$$` on its own line; `\dfrac` inside sentences; balanced `$`. No HTML. No links. No emojis.
- Headings: `###` only, plain phrases, no numbers, never "traps/mistakes/revision/summary" (those have their own fields).

## Rules
- Only edit the topic JSON files assigned to you, plus your own scripts in `content/_work/readable/<section>/`.
  Never touch `src/`, other topics, `package.json`, or git (no commits, no stash, no checkout).
- Do not run `npm`, `next build` or the dev server (another process owns it).
- Work topic by topic: write the script, run it, validate, fix, then move on. If you run long, finish whole
  topics rather than leaving one half-done.
- Final reply (short): per topic, the number of subtopics rewritten, the patterns before → after, the validator result,
  and anything you were unsure about (e.g. a fact you left out).
