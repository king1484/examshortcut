# Current-affairs research brief — read fully before starting

Project: ExamShortcut, a free multi-exam prep website (SSC, Railways, Banking, state exams...).
Repo root: `C:\Users\Vinay Singirikonda\Desktop\examshortcut` (Windows; Git Bash + PowerShell available).

Goal: exam-relevant current affairs, month by month, for the months you are assigned, as one JSON file
per calendar year: `content/core/current-affairs/<year>.json`.

## Research rules (strict)
- **Research, don't recall.** Every item must come from a page you actually fetched with WebFetch in this
  task (Wikipedia "<Year> in India", "<Month> <Year>" / "Portal:Current events/<Month> <Year>",
  award pages (Padma, Bharat Ratna, Nobel, Oscars, Booker, Jnanpith, Dadasaheb Phalke, national sports awards),
  sports event pages (Olympics, Asian Games, Commonwealth Games, cricket World Cups, Thomas Cup, chess),
  Union Budget pages, ISRO mission pages, G20/BRICS/SCO/QUAD summit pages, appointment pages (CJI, CEC,
  RBI Governor, Chief of Army/Navy/Air Staff, President/VP), government scheme pages, index/report rankings).
  If you can't confirm a date or number, leave it out. No guessing.
- Exam relevance only: appointments, awards, sports, summits & international relations, schemes & policy,
  economy & banking (RBI, budget, GDP), defence & exercises, science & space, environment, reports &
  indices (India's rank), books & authors, important days (themes), obituaries of major figures, states.
  Skip crime, gossip, stock tips, celebrity news.
- Write in **simple English**, original sentences (do not copy text). NO URLs, NO "Source:" lines,
  NO website names in the output.

## Output format (per year file)
```json
{
  "year": 2025,
  "months": [
    {
      "month": "2025-01",
      "label": "January 2025",
      "items": [
        {
          "date": "2025-01-13",            // "YYYY-MM-DD", or "YYYY-MM" if the exact day is unknown
          "category": "sports",            // one of: national, international, economy, sports, awards,
                                           // appointments, science, defence, environment, schemes,
                                           // reports, days, obituaries, books, states
          "headline": "Short headline, max ~12 words",
          "detail": "1-3 simple sentences with the exam facts: who, what, where, numbers.",
          "examFacts": ["Crisp one-line fact an exam could ask", "..."]   // 1-3
        }
      ],
      "quiz": [ Question, ... ]            // 6-10 MCQs per month built ONLY from that month's items
    }
  ]
}
```
Question contract: `{ "id": "ca-2025-01-q01", "q": "...", "options": [4 unique strings], "answer": 0-3,
"solution": "1-2 sentences", "shortcut": null, "difficulty": "easy|medium|hard", "subtopic": "2025-01",
"pattern": "<category>", "timeSec": 20 }`.

Target: 15-30 items per month (big months more), spread across categories. Months in chronological order.
Build the file with a Python script (`content/_work/deep/ca/<year>.py`, written with the Write tool,
`json.dump(..., ensure_ascii=False, indent=1)`), run with `py -3`. Validate it parses. If a year file
already exists (another agent may own other months of the same year), merge by month — never delete
months you don't own.

Save after each month or two so progress survives. Do NOT touch any other files, no git, no build, no deploy.
Final reply: months done, item + quiz counts per month, anything you couldn't verify.
