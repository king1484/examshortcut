# examshortcut.in: SSC CGL competitor gaps

Researched 2026-09-24. Web budget: 12 calls. The jagranjosh fetch was blocked, so its column is inferred from search listings and is **unverified**.
Timing matters: the **SSC CGL 2026 Tier 1 runs from 30 Sep to 30 Oct 2026**, admit cards come out from about 27 Sep, and more than 28 lakh candidates applied for 12,256 vacancies. The next 6 to 8 weeks bring the highest search demand of the year for "exam analysis", "answer key" and "marks calculator".

## What examshortcut has today (checked against `src/app`)
- Hub `/ssc-cgl` covers the pattern, eligibility, a posts table with pay levels and in-hand pay, a normalisation explainer, a year timeline, FAQs with FAQPage JSON-LD, and documents.
- `/cutoffs` (CutoffExplorer), `/weightage`, `/syllabus`, `/formula-sheet`, `/score-calculator` (manual counts per section compared with cutoffs), and `/ga/current-affairs` (Apr to Sep 2026 plus a quiz).
- Topic pages at `/[section]/[topic]` with overview, learn/[subtopic], formulas, examples and practice. There are 68 topic JSONs. GA has only ancient-history, polity, economy and current affairs.
- Mocks: T1 mock 1, T1 PYQ-2025 pattern, and T2 mock 1. There are also `/revision`, `/search` and `/dashboard` (localStorage progress).
- The site is English only (`lang="en-IN"`). The About page lists Hindi as "Later".

## 1. Comparison table

| Competitor | Free | Paid | UX strengths | SEO page types it ranks with |
|---|---|---|---|---|
| **Testbook** | 15 free CGL mocks, daily 10-question CA quizzes, 66 free CA tests, PYQ practice ("last 10 years"), rank predictor | Testbook Pass / SuperCoaching (about ₹649 for 90 days), 2,470+ tests, PDFs behind login | Live "mega" tests with All India Rank, **EN/HI toggle**, study plans | `/ssc-cgl-exam/{cut-off, previous-year-papers, rank-predictor, syllabus, eligibility, salary, answer-key, result, admit-card, exam-date}` plus `/news/` pages for exam dates and rank predictors |
| **Adda247 / sscadda** | Notification and PYQ PDFs, some mocks and quizzes | Mahapack, Test Prime, live classes | Dense hub: dates table, pattern table, **shift timings**, **region-wise centre list**, cutoff table, 10+ FAQs, WhatsApp alerts | `/jobs/ssc-cgl-*` (notification, exam date, admit card, **city intimation slip**, answer key, result, cutoff, PYQ PDF, eligibility, vacancy) and `/exams/ssc/…-out/` news pages |
| **Oliveboard** | Free mocks and live tests, some e-books, blog | Foundation, crash and practice courses; full mock series; AAO finance course | **Score calculator**, AI performance analysis, study plans, **English/Hinglish/Telugu/Tamil** batches | Syllabus, cutoff, salary, answer key, admit card, result, **post-specific (AAO)** pages |
| **BYJU'S Exam Prep (Gradeup)** | Free mocks and "mega mocks", free videos | Premium test series and classes | App-first, large community | `/ssc-exams/ssc-cgl-mock-test`, practice hubs |
| **Unacademy** | Limited free classes | Lite / Plus / Iconic subscriptions (all mocks and analysis on Plus) | Many educators per topic, live classes | Goal pages; ranks weakly for informational keywords |
| **PracticeMock** | **1 free mock** per tier, free topic tests, **800+ speed tests**, a free PYQ mock "challenge" | Full test series | AIR comparison, weak-area analysis, HI/EN, **DEST/typing practice** for Tier 2 | Blog: `ssc-cgl-salary`, `ssc-cgl-post-list` (post codes and job profile), `free-preparation-resources`, `english-mock-test (PYQ, PDF)` |
| **Jagranjosh / Careers360 / Shiksha / PW / CareerPower** (unverified) | Articles and PDFs | Little or none; these are ad-funded news sites | Speed on news: shift-wise analysis, "good attempts", day-of answer keys | cutoff (post-wise PDF), exam date, notification, PYQ PDF, salary, **exam calendar** (Careers360 news) |
| **Answer-key tools** (rankmitra, ranksetu, rankguruji, examrankcheck, clearrank) | Paste the **response-sheet URL**, get the score, normalised score and rank | None; ad-funded | Single-purpose, instant | "SSC CGL Tier-1 2025 marks calculator by answer key URL", "normalisation calculator", "rank predictor" |
| **Free mock sites** (karmsakha, mocktestzone, mockers, guidely) | Fully free PYQ-pattern mocks | None or a few | Thin, but rank for "free mock" keywords | "SSC CGL mock test 2026 free" |

**How we compare.** Our free depth is already stronger than every paid platform's free tier: full topic lessons, every mock free, and no login. We are behind in four areas:
- (a) time-sensitive exam-cycle pages
- (b) answer-key and response-sheet tooling
- (c) Hindi
- (d) GA breadth and Tier 2 extras such as DEST typing and more mocks

## 2. Top 10 gaps, ranked by impact and effort (all can be built statically)

| # | Gap | Impact | Effort | Notes / how to build statically |
|---|---|---|---|---|
| 1 | **Response-sheet marks calculator** (answer-key URL parser) | Very high (peaks in Oct 2026) | M | The SSC/digialm response sheet can't be fetched cross-origin. Two client-side options: (1) the user saves the page and uploads or pastes its HTML; (2) a bookmarklet that runs on the response-sheet page and posts counts to our `/score-calculator?c=…`. It parses the chosen and correct options per section and applies +2/−0.5. Show the raw score plus an **estimated normalised band**, reusing the existing normalisation copy. |
| 2 | **Shift-wise exam analysis and "good attempts" pages** for 30 Sep to 30 Oct | Very high (timely) | S per day | One static page per day, built from JSON: difficulty per section, good attempts, topics asked. Link it to our topic pages (for example "Geometry asked 3Q, so learn here"). Competitors rank with exactly this format. |
| 3 | **Exam calendar / notification tracker** (`/ssc-cgl/exam-date`, `/ssc/exam-calendar-2026`) | High (evergreen) | S | We already have `exam.timeline`; promote it to its own page. Add admit-card and city-slip dates, shift timings, a region list, a countdown, and an "Add to calendar" `.ics` download. `lastVerified` should be visible. |
| 4 | **Post preference and salary guide** (`/ssc-cgl/salary`, `/ssc-cgl/post-preference`) | High | S to M | The posts data already exists and is buried in the hub. Add post codes, the job profile, **physical and eligibility filters** (Inspector height and chest, JSO stats requirement, AAO desirable quals), an in-hand calculator by city class X/Y/Z, and a **drag-to-order preference builder** saved in localStorage. |
| 5 | **Hindi (bilingual) mode** | Very high (a large share of CGL aspirants study in Hindi) | L | Start with the highest-traffic pages (hub, cutoffs, syllabus, calculators, current affairs), then add Hindi question text for the mocks. Use `/hi/...` routes with `hreflang`. Testbook, Adda and PracticeMock all offer HI. |
| 6 | **DEST typing test and Tier 2 computer-module practice** | Medium to high | S to M | A pure client-side typing test: 2,000 key depressions in 15 min, with key-depression count, error %, and an SSC-style passage. PracticeMock and multityping rank with this. Add more Tier 2 mocks too, since we have only 1. |
| 7 | **GA coverage** (medieval and modern history, geography, physics, chemistry, biology, static GK, art and culture) | High (GA is 25% of Tier 1 and the weakest-served free area) | L | GA has only 3 topics plus CA. Reuse the topic JSON schema. Static GK (dances, stadiums, awards, firsts) makes good list pages that rank. |
| 8 | **Shift-wise PYQ practice library** (Tier 1 2019 to 2025, tagged by topic) | High ("previous year paper PDF" is a top query) | M to L | Only 1 PYQ-pattern mock exists. Build per-shift memory-based sets as interactive tests, with a **print-to-PDF stylesheet** so "PDF" intent is satisfied without hosting SSC's banned official files. Link each question to its topic page. |
| 9 | **Rank / percentile estimator** | Medium | S | Rough AIR from score, using published qualified counts (for example 1,86,509 qualified in 2024) and the cutoff distribution. It is static maths, clearly labelled as an estimate. Testbook ranks with this. |
| 10 | **Age-limit and eligibility checker, plus a day-countdown study plan generator** | Medium | S | DOB, category and post give eligibility, including relaxations and the cut-off date. Days left and weak topics from the dashboard give a day-by-day plan linking our pages. Both are client-only and both are shareable. |

Honourable mentions: a daily 10-question quiz with a streak (Testbook's daily hook); a "report error" button on each question (already on the About roadmap); a WhatsApp/Telegram alert link on the exam-date page.

## 3. SEO page types we are missing

Each item gives the target URL, then the query it targets.

- **Exam-cycle news:** `/ssc-cgl/exam-date`, `/admit-card`, `/city-intimation-slip`, `/answer-key`, `/result`, `/notification`, `/vacancy` (post- and state-wise). Queries: "SSC CGL admit card 2026", "SSC CGL answer key 2026".
- **Exam analysis:** `/ssc-cgl/exam-analysis/2026-10-01-shift-1` and a `/exam-analysis` index. Queries: "SSC CGL exam analysis today", "good attempts".
- **Calendar:** `/ssc/exam-calendar-2026` (all SSC exams, so it also catches CHSL, MTS and CPO traffic).
- **Tools as landing pages:** `/ssc-cgl/marks-calculator-answer-key`, `/normalisation-calculator`, `/rank-predictor`, `/age-limit-calculator`, `/typing-test-dest`.
- **Career:** `/ssc-cgl/salary`, `/post-preference`, `/post-list` (post codes), and per-post pages such as `/ssc-cgl/posts/income-tax-inspector` and `/aao`. Queries: "SSC CGL ASO salary", "excise inspector job profile".
- **Eligibility:** `/ssc-cgl/eligibility`, `/age-limit`, `/physical-requirements` (these are only sections in the hub today, so they cannot rank separately).
- **Cutoffs, split out:** `/ssc-cgl/cutoff/2025`, `/cutoff/tier-2`, `/cutoff/post-wise`, `/expected-cutoff-2026`. The current single `/cutoffs` page cannot capture year- and tier-specific queries.
- **PYQ:** `/ssc-cgl/previous-year-papers`, `/pyq/2025/tier-1/shift-…`, and topic-wise PYQ pages such as `/ssc-cgl/quant/geometry/pyq`.
- **"PDF"-intent pages:** syllabus PDF, formula sheet PDF, and current affairs PDF by month. Use print CSS plus a "Download PDF" (print) button, because that query modifier is everywhere in competitor titles.
- **Month-wise current affairs:** `/ga/current-affairs/2026-09` instead of one long page. This gives fresh URLs every month.
- **Strategy content:** `/ssc-cgl/preparation-strategy`, `/study-plan-{30,60,90}-days`, `/best-books`, `/tier-2-strategy`, `/cgl-vs-chsl`.
- **Hindi mirrors:** `/hi/ssc-cgl/...` for all of the above, with `hreflang`.
- **Schema:** add `Quiz` / `Question` markup to practice pages, `Event` markup to the exam dates, and `BreadcrumbList` sitewide. FAQPage is currently only on the hub.

## Sources
- testbook.com/ssc-cgl-exam; adda247.com/jobs/ssc-cgl; oliveboard.in/ssc-cgl
- practicemock.com/blog/ssc-cgl-salary, /ssc-cgl-post-list, /ssc-cgl-previous-year-free-mock-test-challenge
- rankmitra.in/ssc/cgl/pre/score-calculator.php; examrankcheck.in/ssc-cgl-marks-calculator; testbook.com/ssc-cgl-exam/rank-predictor
- adda247.com/exams/ssc/ssc-cgl-exam-date-2026-out; news.careers360.com (SSC exam calendar 2026)
- pw.live/ssc/exams/ssc-cgl-2025-tier-1-cut-off; unacademy.com/goal/ssc-cgl; byjusexamprep.com
