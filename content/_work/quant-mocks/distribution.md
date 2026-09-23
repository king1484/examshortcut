# Quant mock distributions (t1-mock-1, t1-pyq-2025, t2-mock-1)

All 80 questions are original (fresh scenarios and numbers, modelled on recurring SSC CGL
patterns). Every answer was re-derived and asserted with `py -3` (arithmetic + sympy) inside
the build scripts `build_t1_mock1.py`, `build_t1_pyq2025.py`, `build_t2_mock1.py` before the
JSON was written. None of the questions duplicate any practice/solved question in
`content/ssc-cgl/topics/quant/` (checked question-by-question against all 19 topic files;
near-collisions found during authoring — tangent-secant PT=12/PA=8 solved example, the
"2x+3y=12, xy=6" algebra item, "walking 40 m, 30°→60°" solved example — were rewritten with
different numbers and asks). Correct-option positions are balanced across a/b/c/d by the
shared finalizer (`verify_common.finalize`, rotate-to-target).

## t1-mock-1 (25 Qs, 10 easy / 11 medium / 4 hard) — typical Tier 1 mix

| Topic | Qs | | Topic | Qs |
|---|---|---|---|---|
| data-interpretation | 3 (1 table set) | | algebra | 2 |
| geometry | 3 | | trigonometry | 2 |
| profit-loss-discount | 2 | | percentage | 2 |
| simplification | 2 | | ratio-proportion (partnership) | 1 |
| average, interest, time-work, time-speed-distance | 1 each | | heights-distances, statistics | 1 each |
| mensuration-2d, mensuration-3d | 1 each | | | |

Arithmetic 11 / advanced 14 — matches the `weightage.json` quant averages (arithmetic backbone
with geometry + DI as the biggest advanced blocks).

## t1-pyq-2025 (25 Qs, 9 easy / 14 medium / 2 hard) — mirrors a real 2025 Tier 1 shift

Topic counts taken from the 2025 column of `content/ssc-cgl/weightage.json`
(DI 3, geometry 3, P&L 2, algebra 2, trigonometry 2, and 1 each of percentage, number-system,
simplification, ratio-proportion, average, interest, time-work, time-speed-distance,
mensuration-2d, mensuration-3d, heights-distances, statistics, mixture-alligation).
Difficulty skews moderate (only 2 hard) to match the reported 2025 shift difficulty.
Each question's `pattern` field names the actual 2025 PYQ type it mirrors (types observed in
the official 12 Sep S1, 13 Sep S2 and 23 Sep S1 2025 question papers): fraction comparison,
rational-irrational classification, partnership with mid-year change, average of an arithmetic
list, savings after income-expenditure change, CI given find SI, markup with successive
discounts, discount with embedded profit, remove-and-replace, pairwise work rates, two speeds
early-late, concentric ring area, sphere inscribed in cube, angle at centre and circumference,
parallel chords radius, common tangents count, sum-zero cube identity, line from two points,
ratio conversion via triplet, sec-tan reciprocal pair, walking towards tower, grouped median,
table DI (percent-of-total / average / growth ranking).

## t2-mock-1 (30 Qs, 6 easy / 15 medium / 9 hard) — Tier 2 Paper 1 feel (+3/−1)

| Topic | Qs | | Topic | Qs |
|---|---|---|---|---|
| data-interpretation | 4 (one 4-Q table block) | | geometry | 4 |
| algebra | 3 | | trigonometry | 3 |
| mensuration-2d, mensuration-3d | 2 + 2 | | profit-loss-discount | 2 |
| simplification, percentage, ratio, average, interest | 1 each | | mixture, T&W, TSD, H&D, statistics | 1 each |

Advanced maths 19 / arithmetic 11 (20%/50%/30% difficulty), matching published Tier 2
analyses: %-Ratio-P&L block ≈ 8–10, Algebra 3–4, Geometry 4–5, Trig+H&D 4–5, Data 3–5,
multi-question DI blocks.

## Sources (distribution only — no question text copied)

- StudyIQ, "SSC CGL Exam Analysis 2025" — aggregate Tier 1 topic counts, moderate difficulty.
- EduRev, "SSC CGL Tier 1 Previous Year Analysis 2022–2025" — per-topic counts by year.
- StudyIQ, "SSC CGL Exam Analysis 9th September 2024 (All Shifts)" — 2024 shift-wise tables.
- Adda247, "SSC CGL Exam Analysis 2024, 9 September Shift 1" — tabular DI set, good attempts.
- T.I.M.E., "SSC CGL 2024 Tier II Analysis" — Tier 2 topic spread, no quadratic/progressions.
- Class24, "SSC CGL Tier 2 Exam Analysis 2024" — %-Ratio-P&L 8–10, Algebra 3–4, Data 3–4.
- Collegedekho, "SSC CGL Paper Analysis" — Tier 2 2023 topic table.
- Official CGL 2025 Tier 1 question papers (12 Sep Shift 1, 13 Sep Shift 2, 23 Sep Shift 1,
  prepp.in PDFs) — read directly to catalogue the 2025 question TYPES only (types listed
  above; all numbers, names and scenarios in the mocks are newly invented).
- `content/ssc-cgl/weightage.json` and `content/ssc-cgl/sections/quant.json` — final counts.
