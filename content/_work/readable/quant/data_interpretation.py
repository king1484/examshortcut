r"""Readable rewrite of Data Interpretation (data-interpretation) — all five subtopics.

Plain English, one idea per section. Every example embeds its data table in the
question text, and every computed answer is re-derived below with exact
Fraction arithmetic and asserted. Run with Python 3.12 from the repo root.
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "data-interpretation.json"


def pct(new, old):
    return F(new - old) * 100 / old


# ---------- shared datasets (mirrored in the question tables) ----------
CARS = {  # units produced by plant, 2019-2023
    "P": [120, 135, 150, 140, 165],
    "Q": [90, 110, 105, 125, 130],
    "R": [150, 145, 160, 170, 175],
    "S": [80, 95, 100, 110, 120],
}
YEARS = [2019, 2020, 2021, 2022, 2023]
SALES = [160, 200, 260, 250, 320]          # lakh rupees, 2019-2023
REV = [80, 96, 120, 144]                   # crore rupees, 2020-2023
DAYS = [480, 520, 460, 540, 500, 500]      # factory output, Mon-Sat
SAL = [(40, 25000), (30, 32000), (20, 28000), (30, 40000)]  # staff: (count, salary)
UNITS = [12000, 15000, 14000, 16000, 13000, 14000]          # six machines

# ---------- answer checks: di-table ----------
assert [sum(CARS[p][i] for p in "PQRS") for i in range(5)] == [440, 485, 515, 545, 590]
assert sum(CARS["R"]) == 800                                                 # tb p1: plant R total
assert F(CARS["Q"][2], CARS["R"][2]) == F(21, 32)                            # tb p2: 105:160
_pq = [CARS["P"][i] + CARS["Q"][i] for i in range(5)]
assert _pq == [210, 245, 255, 265, 295] and _pq.index(max(_pq)) == 4          # tb p3: best 2023
assert [y for y in YEARS if CARS["S"][YEARS.index(y)] >= 100] == [2021, 2022, 2023]  # tb p4: 3 years
assert sum(CARS["P"]) == 710 and F(710, 5) == 142                            # tb p5: P average
PASS = {("A", 2021): (50, 40), ("B", 2021): (60, 54), ("A", 2022): (64, 48), ("B", 2022): (70, 56)}
_rates = {k: F(p, a) for k, (a, p) in PASS.items()}
assert _rates[("B", 2021)] == F(9, 10) and max(_rates.values()) == F(9, 10)   # tb p6: B 2021 = 90%
assert _rates[("A", 2021)] == F(4, 5) and _rates[("A", 2022)] == F(3, 4) and _rates[("B", 2022)] == F(4, 5)
assert F(sum(CARS["S"]), 5) == 101                                           # notes: S average
_gap = [CARS["R"][i] - CARS["S"][i] for i in range(5)]
assert _gap == [70, 50, 60, 60, 55] and _gap.index(max(_gap)) == 0            # notes: gap widest 2019
# ---------- answer checks: di-percent ----------
assert pct(320, 250) == 28                                                   # pc p1: 2022->2023
assert pct(320, 160) == 100                                                  # pc p2: 2019->2023
assert 12000 + 15000 + 5000 + 4000 == 36000 and F(12000, 36000) == F(1, 3)   # pc p3: rent share
assert pct(72, 60) == 20 and pct(81, 72) == F(25, 2)                         # pc p4: points table
_rises = [pct(SALES[i + 1], SALES[i]) for i in range(4)]
assert _rises == [25, 30, F(-50, 13), 28] and _rises.index(max(_rises)) == 1  # pc p5: best 2021
assert F(15000, 36000) == F(5, 12) and F(4000, 36000) == F(1, 9)             # notes: other shares
assert F(200, 250) * 100 == 80 and F(250, 200) * 100 == 125                   # notes: A of B, B of A
# ---------- answer checks: di-pie ----------
assert F(108, 360) * 72000 == 21600                                          # pi p1: Food
assert F(15, 100) * 360 == 54                                                # pi p2: 15% -> 54 deg
assert F(90, 72) == F(5, 4) and F(108 - 72, 360) * 72000 == 7200             # pi p3: ratio + gap
assert pct(135, 120) == F(25, 2) and F(80, 90) == F(8, 9)                    # pi p4: two-pie growth
assert F(80 * 120, 360) == F(80, 3) and F(96 * 135, 360) == 36               # pi notes: Asia values
assert pct(36, F(80, 3)) == 35                                               # pi notes: value growth 35%
assert F(150, 500) * 360 == 108 and F(250, 500) * 360 == 180 and F(100, 500) * 360 == 72  # pie building
assert F(36, 360) * 72000 == 7200 and pct(200, 250) == -20                   # pie/misc notes
for _a, _f in [(90, 4), (120, 3), (60, 6), (45, 8), (36, 10), (180, 2)]:
    assert F(_a, 360) == F(1, _f)                                             # pie notes: fraction table
assert F(1600, 40) == 40 and F(40 * 360, 1) == 14400                         # pi p5: total from 40 deg
assert 108 + 90 + 72 + 54 + 36 == 360                                        # pie closes
# ---------- answer checks: di-average ----------
assert sum(DAYS) == 3000 and F(3000, 6) == 500                               # av p1: weekly average
_two = SAL[0][0] * SAL[0][1] + SAL[1][0] * SAL[1][1]
assert _two == 1960000 and F(_two, 70) == 28000                              # av p2: first two depts
_all = sum(n * s for n, s in SAL)
assert _all == 3720000 and sum(n for n, _ in SAL) == 120 and F(_all, 120) == 31000  # av p2: overall
assert sum(UNITS) == 84000 and F(84000, 6) == 14000                          # av p3: machines
assert sum(DAYS) - 460 == 2540 and F(2540, 5) == 508                         # av p4a: drop lowest
assert 7 * 520 - 3000 == 640                                                # av p4b: seventh day
assert 5 * 2560 == 12800 and 6 * 2500 - 12800 == 2200                        # av p5: bills
assert 40 * 25000 + 20 * 28000 == 1560000 and F(1560000, 60) == 26000        # av notes: clerks+guards
# ---------- answer checks: di-growth ----------
assert pct(96, 80) == 20                                                     # gr p1: 20%
assert F(110, 100) * F(110, 100) == F(121, 100)                              # gr p2: 21% total
assert F(45000, 150) * 100 == 30000 and F(14400) / F(72, 100) == 20000       # gr p3: reverse
_USERS = [40, 60, 96, 120]
_ur = [pct(_USERS[i + 1], _USERS[i]) for i in range(3)]
assert _ur == [50, 60, 25] and _ur.index(max(_ur)) == 1                      # gr p4: best 2022
assert pct(180, 100) == 80 and pct(100, 50) == 100 and 100 - 80 == 20        # gr p5: B by 20 points
assert 50000 * F(9, 10) ** 2 == 40500                                        # gr notes: depreciation
assert 8000 * F(11, 10) == 8800 and 8800 * F(21, 20) == 9240                 # gr notes: chained rates
assert pct(9240, 8000) == F(31, 2)                                           # gr notes: total 15.5%
print("all answer checks passed")


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


CARS_TABLE = ("| Plant | 2019 | 2020 | 2021 | 2022 | 2023 |\n|---|---|---|---|---|---|\n"
              "| P | 120 | 135 | 150 | 140 | 165 |\n| Q | 90 | 110 | 105 | 125 | 130 |\n"
              "| R | 150 | 145 | 160 | 170 | 175 |\n| S | 80 | 95 | 100 | 110 | 120 |")

# ============================================================ di-table
TABLE = dict(
    concept=(
        "A data table gives values for rows (plants, cities, shops) across columns (usually years).\n\n"
        "Read the row and column the question names, then do one small sum: a total, an average, a ratio "
        "or a count. Nothing more."
    ),
    notes=r"""### Read the table before the question
Scan the rows and columns first: what does each cell hold, in what unit?

| Plant | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|
| P | 120 | 135 | 150 | 140 | 165 |
| Q | 90 | 110 | 105 | 125 | 130 |
| R | 150 | 145 | 160 | 170 | 175 |
| S | 80 | 95 | 100 | 110 | 120 |

Cells are thousands of cars. Row totals compare plants; column totals compare years.

> **Tip:** Underline the row or column the question names before touching the numbers. Half the wrong answers in DI come from reading the wrong cell.

### Row and column totals
Add across a row to judge one plant over time; add down a column to judge one year.

Plant R total: $150 + 145 + 160 + 170 + 175 = 800$ thousand. Year 2023 total: $165 + 130 + 175 + 120 = 590$ thousand.

> **Watch:** Check unit words in the question ("thousands of cars"). A correct sum with the wrong unit is still a wrong answer.

### Comparing two cells
Questions love the ratio or difference of two named cells.

Q in 2021 against R in 2021: $105 : 160 = 21 : 32$ after dividing by 5.

> **Rule:** Reduce ratios fully. Options often keep the unreduced $105:160$ as a trap.

### A combined row pair
Add two rows, then compare the sums across columns.

$P + Q$ per year: 210, 245, 255, 265, 295. The biggest joint year is 2023.

> **Tip:** When sums are close, compute each and list them. Guessing "the last year" fails because 2021 dips for Q.

### Counting cells that meet a condition
"How many years did S cross 100?" Read one row and tick.

S row: 80, 95, 100, 110, 120. At or above 100 in 2021, 2022, 2023: three years.

> **Watch:** Decide once whether "cross 100" means above 100 or at least 100. Here 100 counts; the exam usually says "at least".

### The gap between two rows
"When was R ahead of S by the most?" Subtract the two rows column by column.

$R - S$ per year: 70, 50, 60, 60, 55. The widest gap is 70, in 2019. Note how R stays ahead every year even as S grows.

> **Tip:** Gap questions reward rough work: list the five differences, then compare. Doing each year in your head invites slips.

### The average of a row
One row, one sum, one divide.

Plant P average: $710 \div 5 = 142$ thousand cars a year.

### Percent tables
When a column already holds percentages, totals may be given separately. A pass-rate table reads the same way: appeared and passed columns give the rate by division.

City B, 2021: $54 \div 60 = 90\%$, the best rate in the table.

> **Example:** Appeared 50, passed 40 gives 80%. The same table for four city-year pairs is four one-line divisions.
""",
    formulas=[
        {"name": "Row total", "tex": r"\text{total} = \sum \text{row cells}"},
        {"name": "Row average", "tex": r"\bar{x} = \frac{\text{row total}}{\text{number of columns}}"},
        {"name": "Cell ratio", "tex": r"\text{ratio} = a : b \text{ (reduced)}"},
        {"name": "Rate from counts", "tex": r"\text{rate} = \frac{\text{passed}}{\text{appeared}} \times 100\%"},
    ],
    tricks=[
        {"title": "Sweep the row with tick marks",
         "body": "For count-type questions (how many years above a value), tick the qualifying cells while reading once. No rewriting, no calculator.",
         "example": {"q": "In how many years was Plant S's production at least 100 thousand?\n\n| Plant | 2019 | 2020 | 2021 | 2022 | 2023 |\n|---|---|---|---|---|---|\n| S | 80 | 95 | 100 | 110 | 120 |",
                     "steps": [r"S row: 80, 95, 100, 110, 120.",
                               r"At least 100: 2021, 2022, 2023.",
                               r"Count $= 3$."],
                     "answer": "3 years"}},
        {"title": "Column-first for year questions",
         "body": "Any question about one year (best year, total of a year) lives in a single column. Add that column alone; ignore the rest of the table.",
         "example": {"q": "Total production in 2023 was:\n\n| Plant | 2022 | 2023 |\n|---|---|---|\n| P | 140 | 165 |\n| Q | 125 | 130 |\n| R | 170 | 175 |\n| S | 110 | 120 |",
                     "steps": [r"2023 column: $165 + 130 + 175 + 120$.",
                               r"$= 590$ thousand."],
                     "answer": "590 thousand"}},
    ],
    mistakes=[
        {"wrong": "Adding the wrong row because two rows look similar.",
         "right": "Finger-point the row label, then read its cells."},
        {"wrong": "Answering in cars when the table says thousands of cars.",
         "right": "Carry the table's unit into the answer line."},
        {"wrong": "Leaving a ratio unreduced, such as 105:160.",
         "right": "Divide both terms by their common factor; options use reduced form."},
        {"wrong": "Counting a boundary value as a miss ('at least 100').",
         "right": "At least includes the boundary; above excludes it."},
        {"wrong": "Averaging two averages of different-sized groups.",
         "right": "Rebuild totals before dividing."},
    ],
    revision=[
        "Row questions read one row; year questions read one column.",
        "Totals first, ratio or average after.",
        "Reduce ratios fully; the unreduced pair is a planted option.",
        "Count questions: tick qualifying cells in one sweep.",
        "Rate = passed ÷ appeared, times 100.",
        "Carry the table's unit into the answer.",
    ],
    patterns=[
        pat("di-tb-p1", "Row total", "very common",
            "A table of items across years; the total for one item over all years is asked.",
            r"\text{total} = \sum \text{row cells}",
            ["Point at the named row.",
             "Add its cells across all columns.",
             "State the unit with the answer."],
            "One row, one addition: the simplest table question there is.",
            "Production of cars by four plants (in thousands):\n\n" + CARS_TABLE + "\n\nTotal production of Plant R over the five years was:",
            [r"R row: $150 + 145 + 160 + 170 + 175$.",
             r"$= 800$ thousand."],
            "800 thousand"),
        pat("di-tb-p2", "Ratio of two cells", "common",
            "Two entries are named (same year, different rows); their ratio is asked.",
            r"a : b \text{ reduced}",
            ["Pick the two cells named.",
             "Write them as a ratio.",
             "Divide both by their highest common factor."],
            "Ratios compare two cells without any totals.",
            "Production of cars by four plants (in thousands):\n\n" + CARS_TABLE + "\n\nThe ratio of production of Plant Q to Plant R in 2021 is:",
            [r"Q in 2021 $= 105$; R in 2021 $= 160$.",
             r"Ratio $= 105 : 160 = 21 : 32$."],
            "21 : 32"),
        pat("di-tb-p3", "Best year for a row pair", "common",
            "Two rows are combined and the year with the highest combined value is asked.",
            r"\text{best year} = \max_i (a_i + b_i)",
            ["Add the two rows column by column.",
             "List the five sums.",
             "Pick the largest and name its year."],
            "Combined strength can peak in a different year than either row alone.",
            "Production of cars by four plants (in thousands):\n\n" + CARS_TABLE + "\n\nIn which year was the combined production of Plants P and Q the highest?",
            [r"$P+Q$: 210, 245, 255, 265, 295 for 2019-2023.",
             r"Largest is 295.",
             r"Year 2023."],
            "2023"),
        pat("di-tb-p4", "Count the qualifying years", "common",
            "'For how many years was X at least / more than a value?'",
            r"\#\text{years} = \text{count of cells meeting the condition}",
            ["Read the named row once.",
             "Tick every cell meeting the condition.",
             "Count the ticks."],
            "It is a reading test, not a calculation.",
            "Production of cars by four plants (in thousands):\n\n" + CARS_TABLE + "\n\nFor how many years was the production of Plant S at least 100 thousand?",
            [r"S row: 80, 95, 100, 110, 120.",
             r"At least 100 in 2021, 2022, 2023.",
             r"Count $= 3$."],
            "3 years"),
        pat("di-tb-p5", "Average of a row", "very common",
            "The average of one item across all columns is asked.",
            r"\bar{x} = \frac{\text{row total}}{\text{columns}}",
            ["Add the row.",
             "Count the columns.",
             "Divide."],
            "An average is a row total shared over the years.",
            "Production of cars by four plants (in thousands):\n\n" + CARS_TABLE + "\n\nThe average production of Plant P over the five years is:",
            [r"P total $= 120 + 135 + 150 + 140 + 165 = 710$.",
             r"Average $= 710 \div 5 = 142$."],
            "142 thousand"),
        pat("di-tb-p6", "Rate table: appeared and passed", "common",
            "A table lists appeared and passed counts; the best or worst pass percentage is asked.",
            r"\text{rate} = \frac{\text{passed}}{\text{appeared}} \times 100\%",
            ["Divide passed by appeared for each row.",
             "Compare the rates.",
             "Name the row with the highest (or lowest)."],
            "Raw pass counts mislead; the rate per appeared candidate is the fair compare.",
            "Pass details of two coaching centres in two years:\n\n| Centre | Year | Appeared | Passed |\n|---|---|---|---|\n| A | 2021 | 50 | 40 |\n| B | 2021 | 60 | 54 |\n| A | 2022 | 64 | 48 |\n| B | 2022 | 70 | 56 |\n\nWhich centre-year pair shows the highest pass percentage?",
            [r"A 2021: $40/50 = 80\%$; B 2021: $54/60 = 90\%$.",
             r"A 2022: $48/64 = 75\%$; B 2022: $56/70 = 80\%$.",
             r"Highest: B in 2021."],
            "B in 2021 (90%)"),
    ],
)

# ============================================================ di-percent
PERCENT = dict(
    concept=(
        "Percentage questions on data compare one value with another: a rise, a share, or a gap in points.\n\n"
        "The base is everything. Ask first: percent of what? The number after 'of' is the base you divide by."
    ),
    notes=r"""### Percentage change: new against old
$$\% \text{ change} = \frac{\text{new} - \text{old}}{\text{old}} \times 100$$

Sales of 250 rising to 320 grew by $\dfrac{70}{250} \times 100 = 28\%$.

> **Rule:** The base is the earlier (or original) value. Rise and fall use the same formula; a fall just gives a minus sign.

### Change over a long span
From 160 to 320 over five years: $\dfrac{320-160}{160} \times 100 = 100\%$. The value doubled.

> **Watch:** A question asking "by 2023 from 2019" wants one jump, not the sum of yearly rises. 25% then 30% is not 55%.

### Share of a total
One item as a percent of the whole table:

$$\text{share} = \frac{\text{item}}{\text{total}} \times 100$$

Spending table: Rent 12000, Food 15000, Travel 5000, Education 4000; total 36000. Rent's share $= \dfrac{12000}{36000} = 33\dfrac{1}{3}\%$.

> **Tip:** Add the full column first and keep the total visible. Every share question reuses it.

### Points versus percent
A rise from 60 points to 72 points is 12 points. As a percent it is $\dfrac{12}{60} \times 100 = 20\%$.

> **Watch:** Options offer both 12 and 20. Read whether the question says points or percent.

### Which year grew fastest?
Compute each year's rise on its own base, then compare.

Sales 160, 200, 260, 250, 320: rises are $25\%$, $30\%$, about $-3.8\%$, $28\%$. The fastest growth year is 2021, even though 2023 added more units.

> **Tip:** Fastest growth is about the rate, not the amount. A small base inflates the rate.

### Falls follow the same rule
A dip computes exactly like a rise. Sales slip from 260 to 250: $\dfrac{250-260}{260} \times 100 \approx -3.8\%$. The minus sign is the only difference.

> **Watch:** The base is still the earlier value, 260. Dividing 10 by 250 gives 4%, a planted wrong option.

### One item as percent of another
"A is what percent of B" divides A by B, no subtraction:

Sales of A are 200 when B sells 250. A is $\dfrac{200}{250} \times 100 = 80\%$ of B. Turned around, B is $\dfrac{250}{200} \times 100 = 125\%$ of A.

> **Tip:** The value after "of" is the base. Swapping the two swaps the answer between 80 and 125.

### Approximate, then aim
Ugly tables reward rough work. Round each value to one significant figure, compute, and match the closest option. Only compute exactly when two options sit close together.

> **Example:** A rise from 199 to 251 is about $50/200 = 25\%$; scan the options and only one will be near 25.

### Percentage of a percentage
"A's sales are 25% more than B's" does not make B 25% less than A. If B is 200, A is 250; then B is $\dfrac{200}{250} = 80\%$ of A, which is 20% less.

> **Example:** Reverse the sentence, reverse the base. 250 on base 200 is +25%; 200 on base 250 is −20%.
""",
    formulas=[
        {"name": "Percentage change", "tex": r"\frac{\text{new}-\text{old}}{\text{old}} \times 100\%",
         "note": "Base = the old / original value."},
        {"name": "Share", "tex": r"\frac{\text{part}}{\text{whole}} \times 100\%"},
        {"name": "Points vs percent", "tex": r"\text{points} = a - b; \quad \%\text{age} = \frac{a-b}{b} \times 100"},
    ],
    tricks=[
        {"title": "The 1% probe",
         "body": "Find 1% of the base first; then any percentage is that times n. 1% of 250 is 2.5, so 70 units is 28%.",
         "example": {"q": "Sales rose from 250 to 320. Find the percentage rise.",
                     "steps": [r"Rise $= 70$ units; $1\%$ of 250 $= 2.5$.",
                               r"$70 \div 2.5 = 28$."],
                     "answer": "28%"}},
        {"title": "Anchor on the double",
         "body": "A value that doubles is +100%; halves is −50%. Spot these before computing: they frame every other answer.",
         "example": {"q": "Sales went from 160 to 320 over five years. Total growth?",
                     "steps": [r"$320 = 2 \times 160$.",
                               r"Doubling is $+100\%$."],
                     "answer": "100%"}},
    ],
    mistakes=[
        {"wrong": "Dividing by the new value for a percentage rise.",
         "right": "Divide the rise by the old value."},
        {"wrong": "Adding yearly percentage rises for a span.",
         "right": "Use only the first and last values for a span."},
        {"wrong": "Reporting 12 when 20 is asked (points vs percent).",
         "right": "Check the unit the question wants."},
        {"wrong": "Calling +25% reversible, so a −25% fall returns the start.",
         "right": "Bases differ: +25% then −25% of the new value loses money."},
        {"wrong": "Using the largest rise in units as the fastest growth.",
         "right": "Growth rate divides by that year's own base."},
    ],
    revision=[
        r"$\%\text{ rise} = \dfrac{\text{rise}}{\text{old}} \times 100$.",
        "Span questions: first and last values only.",
        "Share: part over whole, after totalling the column.",
        "Points are differences; percent divides by the base.",
        "Fastest growth year = highest rate on its own base.",
        "Doubling is +100%; halving is −50%.",
    ],
    patterns=[
        pat("di-pc-p1", "Single-step percentage rise", "very common",
            "A table of yearly values; the percent change between two named years is asked.",
            r"\frac{\text{new}-\text{old}}{\text{old}} \times 100\%",
            ["Subtract the earlier year from the later one.",
             "Divide by the earlier year.",
             "Multiply by 100."],
            "Change only means something against its starting base.",
            "Sales of a store (in lakh rupees):\n\n| Year | 2019 | 2020 | 2021 | 2022 | 2023 |\n|---|---|---|---|---|---|\n| Sales | 160 | 200 | 260 | 250 | 320 |\n\nThe percentage increase in sales from 2022 to 2023 is:",
            [r"Rise $= 320 - 250 = 70$.",
             r"$\dfrac{70}{250} \times 100 = 28\%$."],
            "28%"),
        pat("di-pc-p2", "Percentage change over a span", "very common",
            "Growth from the first year to the last year is asked.",
            r"\frac{V_{last} - V_{first}}{V_{first}} \times 100\%",
            ["Take only the first and last values.",
             "Find the difference.",
             "Divide by the first value."],
            "A span has one start and one end; middle years are noise.",
            "Sales of a store (in lakh rupees):\n\n| Year | 2019 | 2020 | 2021 | 2022 | 2023 |\n|---|---|---|---|---|---|\n| Sales | 160 | 200 | 260 | 250 | 320 |\n\nThe percentage increase in sales from 2019 to 2023 is:",
            [r"Difference $= 320 - 160 = 160$.",
             r"$\dfrac{160}{160} \times 100 = 100\%$."],
            "100%"),
        pat("di-pc-p3", "Share of a total", "common",
            "One item of an expense or production table as a percent of the table's total.",
            r"\frac{\text{item}}{\text{total}} \times 100\%",
            ["Total the whole column.",
             "Place the item over the total.",
             "Multiply by 100."],
            "A share is a fraction of a fixed whole.",
            "Monthly expenses of a family:\n\n| Item | Rent | Food | Travel | Education |\n|---|---|---|---|---|\n| Amount (₹) | 12000 | 15000 | 5000 | 4000 |\n\nRent is what percent of total expenses?",
            [r"Total $= 12000 + 15000 + 5000 + 4000 = 36000$.",
             r"Rent share $= \dfrac{12000}{36000} \times 100 = 33\dfrac{1}{3}\%$."],
            r"33$\frac{1}{3}$%"),
        pat("di-pc-p4", "Points or percent", "common",
            "A table of scores or points; the question asks for the rise in points or in percent.",
            r"\text{points} = a-b; \quad \%\text{age} = \frac{a-b}{b} \times 100",
            ["Decide the unit asked: points or percent.",
             "Points: subtract.",
             "Percent: divide the difference by the earlier score."],
            "Same numbers, two answers; the unit decides.",
            "Points scored by a team across three seasons:\n\n| Season | 1st | 2nd | 3rd |\n|---|---|---|---|\n| Points | 60 | 72 | 81 |\n\nThe percentage increase in points from the 1st to the 2nd season is:",
            [r"Rise $= 72 - 60 = 12$ points.",
             r"$\dfrac{12}{60} \times 100 = 20\%$."],
            "20%"),
        pat("di-pc-p5", "Fastest growing year", "common",
            "Which year saw the highest percentage growth?",
            r"\max_i \frac{V_{i+1}-V_i}{V_i}",
            ["Compute each year's rise.",
             "Divide each by that year's base.",
             "Pick the largest rate."],
            "Growth speed is a rate on each year's own base.",
            "Sales of a store (in lakh rupees):\n\n| Year | 2019 | 2020 | 2021 | 2022 | 2023 |\n|---|---|---|---|---|---|\n| Sales | 160 | 200 | 260 | 250 | 320 |\n\nIn which year was the percentage growth in sales the highest?",
            [r"Rises: $40/160 = 25\%$, $60/200 = 30\%$, $-10/260 \approx -3.8\%$, $70/250 = 28\%$.",
             r"Largest rate is $30\%$.",
             r"Year 2021."],
            "2021"),
    ],
)

# ============================================================ di-pie
PIE = dict(
    concept=(
        "A pie chart splits a total into slices by angle: 360 degrees is the whole, so 1 degree is "
        "total ÷ 360.\n\n"
        "Two conversions answer everything: degrees to percent ($360° = 100\\%$) and degrees to value "
        "($1° =$ total ÷ $360$)."
    ),
    notes=r"""### Reading the slices
A family spends ₹72,000 a month:

| Head | Food | Rent | Education | Travel | Savings |
|---|---|---|---|---|---|
| Angle | 108° | 90° | 72° | 54° | 36° |

The angles must add to 360°: $108+90+72+54+36 = 360$. Check this before using any slice.

> **Rule:** One slice's value $= \dfrac{\text{angle}}{360} \times \text{total}$. Food $= \dfrac{108}{360} \times 72000 = ₹21,600$.

### Degrees into percent
$360°$ is the whole, so divide by 36: $108° \rightarrow 3 \rightarrow 30\%$. Each 3.6° is 1%.

Going the other way, $15\% = 15 \times 3.6 = 54°$.

> **Tip:** Memorise the pair: $25\% = 90°$, $50\% = 180°$. Halving and doubling gets the rest.

### Angles as simple fractions
Common slice angles are neat fractions of the whole. Learn the pairs once:

| Angle | 180° | 120° | 90° | 60° | 45° | 36° |
|---|---|---|---|---|---|---|
| Fraction | $\dfrac{1}{2}$ | $\dfrac{1}{3}$ | $\dfrac{1}{4}$ | $\dfrac{1}{6}$ | $\dfrac{1}{8}$ | $\dfrac{1}{10}$ |

A 90° slice of any total is a quarter of it; 120° is a third. Fractions beat decimal division under time pressure.

> **Tip:** Split odd angles into known pieces: 135° is 90° + 45°, so $\dfrac{1}{4} + \dfrac{1}{8} = \dfrac{3}{8}$.

### Comparing slices
Ratios and differences work directly in degrees.

Rent : Education $= 90 : 72 = 5 : 4$. Food exceeds Education by $108 - 72 = 36°$, worth $\dfrac{36}{360} \times 72000 = ₹7,200$.

> **Watch:** A difference asked in rupees needs the degree gap converted through the total. Answering "36" alone is the planted option.

### Two pies side by side
Two pies show two totals. The same angle does not mean the same amount.

Company exports 2020: Asia 120° of ₹80 crore; 2021: Asia 135° of ₹96 crore. Asia's share rose from $33\dfrac{1}{3}\%$ to $37.5\%$. In value: 2020 gave $\dfrac{120}{360} \times 80 = 26\dfrac{2}{3}$ crore, 2021 gave $\dfrac{135}{360} \times 96 = 36$ crore. That is a $35\%$ rise, not the $12.5\%$ the angles alone suggest.

> **Note:** When only angles are given for both years, compare angles as ratios: Europe $80° : 90° = 8 : 9$.

### Building a pie from data
To draw or check a pie: each slice angle $= \dfrac{\text{part}}{\text{total}} \times 360°$.

Three items of 150, 250, 100 out of 500 take $108°$, $180°$, $72°$.

> **Example:** Savings at 36° is $\dfrac{36}{360} = 10\%$ of ₹72,000, i.e. ₹7,200.

### The one-degree value
Many questions hand you one slice value and ask for the total.

A 40° slice holds 1,600 units, so $1° = 40$ units and the whole pie is $360 \times 40 = 14,400$.

> **Tip:** Find the per-degree value first; every slice then costs one multiplication.
""",
    formulas=[
        {"name": "Slice value", "tex": r"\text{value} = \frac{\theta}{360} \times \text{total}",
         "note": "theta is the slice angle in degrees."},
        {"name": "Angle to percent", "tex": r"\% = \frac{\theta}{3.6}"},
        {"name": "Percent to angle", "tex": r"\theta = \% \times 3.6"},
        {"name": "Part to angle", "tex": r"\theta = \frac{\text{part}}{\text{total}} \times 360"},
        {"name": "Per-degree value", "tex": r"1° = \frac{\text{total}}{360}"},
    ],
    tricks=[
        {"title": "Divide by 36 for percent",
         "body": "Angle over 3.6 gives percent; angle over 36 gives percent over 10. 108° -> 30%, 54° -> 15%, 90° -> 25%.",
         "example": {"q": "A slice of 72° is what percent of the pie?",
                     "steps": [r"$72 \div 3.6 = 20$.",
                               r"So $72° = 20\%$."],
                     "answer": "20%"}},
        {"title": "Per-degree shortcut",
         "body": "Given one slice's value, find the value of 1 degree once, then price every other slice (and the whole pie) with one multiplication each.",
         "example": {"q": "A 40° slice of a pie is worth 1,600 units. Find the whole pie.",
                     "steps": [r"$1° = 1600 \div 40 = 40$ units.",
                               r"Whole $= 360 \times 40 = 14400$."],
                     "answer": "14,400"}},
    ],
    mistakes=[
        {"wrong": "Treating angles as values across two different pies.",
         "right": "Convert through each pie's own total first."},
        {"wrong": "Answering a rupee-difference question with the degree gap.",
         "right": "Convert the degree gap through total ÷ 360."},
        {"wrong": "Using 100° = 25% style conversions.",
         "right": "25% is 90°; 3.6° is 1%. Keep the pair exact."},
        {"wrong": "Forgetting to check that the angles add to 360°.",
         "right": "Add them first; a misprint or trap shows up immediately."},
        {"wrong": "Computing percent change in angles as percent change in value.",
         "right": "Growth in share (angle) and growth in value are different questions."},
    ],
    revision=[
        r"Slice value $= \dfrac{\theta}{360} \times$ total.",
        r"$\theta \to \%$: divide by 3.6. $\% \to \theta$: multiply by 3.6.",
        "25% = 90°, 50% = 180°, 10% = 36°.",
        "Compare slices in degrees; convert to money through the total.",
        "Two pies: same angle, different total, different value.",
        "One slice value gives the per-degree value for everything.",
    ],
    patterns=[
        pat("di-pi-p1", "Value of one slice", "very common",
            "A pie of known total; one slice's angle is given and its value asked.",
            r"\text{value} = \frac{\theta}{360} \times \text{total}",
            ["Write the total.",
             "Place the angle over 360.",
             "Multiply."],
            "A slice holds its fraction of the total, angle over 360.",
            "A family's monthly budget of ₹72,000 is shown as a pie:\n\n| Head | Food | Rent | Education | Travel | Savings |\n|---|---|---|---|---|---|\n| Angle | 108° | 90° | 72° | 54° | 36° |\n\nThe amount spent on Food is:",
            [r"Food angle $= 108°$.",
             r"$\dfrac{108}{360} \times 72000 = 21600$."],
            "₹21,600"),
        pat("di-pi-p2", "Percent into angle", "common",
            "A share is given as a percent and the slice angle is asked (or the reverse).",
            r"\theta = \% \times 3.6",
            ["Take the percentage.",
             "Multiply by 3.6.",
             "State the answer in degrees."],
            "The full circle, 360 degrees, carries the full 100 percent.",
            "In a pie chart of monthly expenses, Travel takes 15% of the budget. The central angle of the Travel slice is:",
            [r"$15\%$ of $360°$.",
             r"$0.15 \times 360 = 54°$."],
            "54°"),
        pat("di-pi-p3", "Ratio and difference of slices", "common",
            "Two slices are compared as a ratio, or their value gap is asked.",
            r"\frac{\theta_1}{\theta_2} : \text{ratio}; \quad \frac{\theta_1-\theta_2}{360}\times T : \text{gap}",
            ["Write both angles.",
             "Ratio: reduce the angles.",
             "Gap: convert the degree difference through the total."],
            "Angles carry both comparisons without touching the other slices.",
            "A family's monthly budget of ₹72,000 is shown as a pie:\n\n| Head | Food | Rent | Education | Travel | Savings |\n|---|---|---|---|---|---|\n| Angle | 108° | 90° | 72° | 54° | 36° |\n\nThe ratio of Rent to Education, and by how much amount Food exceeds Education, are:",
            [r"Rent : Education $= 90 : 72 = 5 : 4$.",
             r"Degree gap $= 108 - 72 = 36°$.",
             r"Amount gap $= \dfrac{36}{360} \times 72000 = ₹7,200$."],
            "5 : 4 and ₹7,200"),
        pat("di-pi-p4", "Two pies compared", "occasional",
            "The same category appears in two pies (two years, two companies).",
            r"\text{share} = \frac{\theta}{360}; \quad \text{value} = \text{share} \times \text{total}",
            ["Read each pie's total.",
             "Convert the slice to a share or value within its own pie.",
             "Compare the two results."],
            "The same angle of a bigger pie is more money; totals must enter.",
            "Angles of a company's export pie:\n\n| Region | 2020 | 2021 |\n|---|---|---|\n| Asia | 120° | 135° |\n| Europe | 80° | 90° |\n\nFor Europe, the ratio of the 2020 angle to the 2021 angle is:",
            [r"2020 angle $= 80°$; 2021 angle $= 90°$.",
             r"$80 : 90 = 8 : 9$."],
            "8 : 9"),
        pat("di-pi-p5", "Total from one slice", "common",
            "One slice's value is known; the whole pie (or another slice) is asked.",
            r"\text{total} = \frac{\text{slice value} \times 360}{\theta}",
            ["Find the per-degree value: slice value ÷ angle.",
             "Multiply by 360 for the total.",
             "Multiply by any other angle for its slice."],
            "One slice prices one degree, and one degree prices the pie.",
            "In a pie chart of production, a 40° sector represents 1,600 units. The total production of all sectors together is:",
            [r"$1° = 1600 \div 40 = 40$ units.",
             r"Total $= 40 \times 360 = 14400$ units."],
            "14,400 units"),
    ],
)

# ============================================================ di-average
AVERAGE = dict(
    concept=(
        "Table averages rebuild the total first: **average = total ÷ count**.\n\n"
        "Rows can carry their own counts (workers per salary band, machines per output), so weighted "
        "averages, not plain ones, are the default here."
    ),
    notes=r"""### Simple row average
Six days of factory output:

| Day | Mon | Tue | Wed | Thu | Fri | Sat |
|---|---|---|---|---|---|---|
| Units | 480 | 520 | 460 | 540 | 500 | 500 |

Total $= 3000$, average $= 3000 \div 6 = 500$ units a day.

> **Rule:** Total first, divide second. An average of a table row is one sum and one division.

### Weighted average: counts differ
A plain average works only when every value has the same count. Salary bands do not:

| Band | Staff | Salary (₹) |
|---|---|---|
| Clerks | 40 | 25,000 |
| Typists | 30 | 32,000 |
| Guards | 20 | 28,000 |
| Managers | 30 | 40,000 |

$$\bar{x} = \frac{\sum (\text{count} \times \text{value})}{\sum \text{count}}$$

Clerks and typists alone: $\dfrac{40 \times 25000 + 30 \times 32000}{70} = \dfrac{1960000}{70} = ₹28,000$. All four bands: $\dfrac{3720000}{120} = ₹31,000$.

> **Watch:** The unweighted mean of 25000, 32000, 28000, 40000 is 31,250 — close, and wrong. Options love it.

### Where the weighted average sits
The weighted average always sits between the smallest and largest band values, pulled toward the biggest band.

Clerks (40 at ₹25,000) with guards (20 at ₹28,000): $\dfrac{40 \times 25000 + 20 \times 28000}{60} = ₹26,000$. It leans toward ₹25,000 because clerks are the bigger band.

> **Tip:** Use this to reject options before computing: an answer outside the band range is always wrong.

### Drop one entry, add one entry
Removing a day changes both the total and the count.

Drop Wednesday's 460: new total $2540$, new count 5, average $508$. A Sunday of 520-average over 7 days needs $7 \times 520 = 3640$, so Sunday's output $= 3640 - 3000 = 640$.

> **Tip:** Any average question with a change is two totals and one subtraction.

### The sixth value that fixes the average
Five electricity bills average ₹2,560 (total ₹12,800). A sixth bill drops the average to ₹2,500, so the new total is $6 \times 2500 = 15000$. The sixth bill is $15000 - 12800 = ₹2,200$.

> **Example:** Bill below the new average pulls it down; the size of the pull shows in the difference of totals.

### Machine tables
Machines with one output each are plain rows:

| Machine | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| Units | 12000 | 15000 | 14000 | 16000 | 13000 | 14000 |

Total $= 84,000$ units, so the average is $84000 \div 6 = 14,000$ units per machine.

> **Watch:** Keep the unit name (units, rupees, thousands) straight from the header row; two unit columns in one table is a classic DI setup.

### Average of averages fails
Two shifts, averages 400 and 500, do not average to 450 unless the shifts are equal. If 10 workers and 20 workers produced those averages, the combined average is $\dfrac{10 \times 400 + 20 \times 500}{30} = 466.67$.

> **Tip:** Whenever group sizes differ, multiply each average by its size before adding.
""",
    formulas=[
        {"name": "Simple average", "tex": r"\bar{x} = \frac{\sum x}{n}"},
        {"name": "Weighted average", "tex": r"\bar{x} = \frac{\sum n_i x_i}{\sum n_i}",
         "note": "n_i is the count in each band or row."},
        {"name": "Entry to hit a target average", "tex": r"x = (n+1)\bar{x}_{new} - n\bar{x}_{old}"},
    ],
    tricks=[
        {"title": "Deviations from a round base",
         "body": "Table values near a round number: average = base + (sum of differences ÷ count). 480, 520, 460, 540, 500, 500 around 500: deviations sum to 0, average exactly 500.",
         "example": {"q": "Find the average of 480, 520, 460, 540, 500, 500.",
                     "steps": [r"Base 500: deviations $-20, +20, -40, +40, 0, 0$.",
                               r"Sum of deviations $= 0$.",
                               r"Average $= 500$."],
                     "answer": "500"}},
        {"title": "Balance around the new average",
         "body": "If an added value lowers the average, each old entry gains (old avg − new avg); the new entry supplies all of it.",
         "example": {"q": "Five bills average 2,560. A sixth brings the average to 2,500. Find the sixth bill.",
                     "steps": [r"Old total $= 5 \times 2560 = 12800$.",
                               r"New total $= 6 \times 2500 = 15000$.",
                               r"Sixth bill $= 15000 - 12800 = 2200$."],
                     "answer": "₹2,200"}},
    ],
    mistakes=[
        {"wrong": "Averaging band values without their counts.",
         "right": "Weight by the staff or count column first."},
        {"wrong": "Averaging two group averages when groups differ in size.",
         "right": "Rebuild both totals and both counts."},
        {"wrong": "Dropping an entry but dividing by the old count.",
         "right": "The count falls by one with the entry."},
        {"wrong": "Mixing units from two different header rows.",
         "right": "Read the header of the exact row you use."},
        {"wrong": "Rounding mid-way and carrying the rounded value.",
         "right": "Keep fractions until the final line."},
    ],
    revision=[
        r"Simple: $\dfrac{\sum x}{n}$; weighted: $\dfrac{\sum n_i x_i}{\sum n_i}$.",
        "Band tables: multiply count by value before adding.",
        "Removed entry: new total ÷ new count.",
        "Added entry: $(n+1)\\times$new average $-$ old total.",
        "Average of averages is valid only for equal group sizes.",
        "Deviations from a round base beat long addition.",
    ],
    patterns=[
        pat("di-av-p1", "Average of a row", "very common",
            "A table of daily or yearly values; the overall average is asked.",
            r"\bar{x} = \frac{\sum x}{n}",
            ["Add the row or column.",
             "Count the entries.",
             "Divide."],
            "One row, one total, one count.",
            "Units produced by a factory on six days of a week:\n\n| Day | Mon | Tue | Wed | Thu | Fri | Sat |\n|---|---|---|---|---|---|---|\n| Units | 480 | 520 | 460 | 540 | 500 | 500 |\n\nThe average daily production is:",
            [r"Total $= 480+520+460+540+500+500 = 3000$.",
             r"Average $= 3000 \div 6 = 500$."],
            "500 units"),
        pat("di-av-p2", "Weighted average from bands", "very common",
            "A table pairs counts with values (staff per salary, students per mark); one average asked.",
            r"\bar{x} = \frac{\sum n_i x_i}{\sum n_i}",
            ["Multiply each count by its value.",
             "Add the products.",
             "Divide by the total count."],
            "Bigger bands must pull the average harder.",
            "Salary structure of a company:\n\n| Band | Clerks | Typists | Guards | Managers |\n|---|---|---|---|---|\n| Staff | 40 | 30 | 20 | 30 |\n| Salary (₹) | 25,000 | 32,000 | 28,000 | 40,000 |\n\nThe average salary of all 120 employees is:",
            [r"$\sum n x = 40 \times 25000 + 30 \times 32000 + 20 \times 28000 + 30 \times 40000$.",
             r"$= 1000000 + 960000 + 560000 + 1200000 = 3720000$.",
             r"Average $= 3720000 \div 120 = 31,000$."],
            "₹31,000"),
        pat("di-av-p3", "Average of a machine row", "common",
            "Machines or branches each give one output; the average output is asked.",
            r"\bar{x} = \frac{\sum x}{n}",
            ["Add the outputs.",
             "Divide by the number of machines.",
             "Keep the unit from the header."],
            "It is still a row average; the row is just machines.",
            "Output of six machines in a month:\n\n| Machine | M1 | M2 | M3 | M4 | M5 | M6 |\n|---|---|---|---|---|---|---|\n| Units | 12,000 | 15,000 | 14,000 | 16,000 | 13,000 | 14,000 |\n\nThe average output per machine is:",
            [r"Total $= 12000+15000+14000+16000+13000+14000 = 84000$.",
             r"Average $= 84000 \div 6 = 14,000$."],
            "14,000 units"),
        pat("di-av-p4", "Drop an entry, extend the week", "common",
            "An entry is removed (lowest day) or added (seventh day) and the new average is asked.",
            r"\bar{x}_{new} = \frac{\text{total} \mp \text{entry}}{n \mp 1}",
            ["Write the current total.",
             "Remove or add the entry.",
             "Divide by the new count."],
            "Both the total and the count move together.",
            "Units produced by a factory on six days:\n\n| Day | Mon | Tue | Wed | Thu | Fri | Sat |\n|---|---|---|---|---|---|---|\n| Units | 480 | 520 | 460 | 540 | 500 | 500 |\n\nIf Wednesday is excluded, the average of the remaining days is:",
            [r"Total without Wednesday $= 3000 - 460 = 2540$.",
             r"Days left $= 5$.",
             r"Average $= 2540 \div 5 = 508$."],
            "508 units"),
        pat("di-av-p5", "The value that sets a target average", "common",
            "A new reading must bring the average to a stated level.",
            r"x = (n+1)\bar{x}_{target} - \text{old total}",
            ["Old total: old average times old count.",
             "New total: target average times new count.",
             "Subtract."],
            "The new total must cover every old value plus the newcomer.",
            "The average of five electricity bills is ₹2,560. After a sixth bill arrives, the average of all six becomes ₹2,500.\n\n| Bills | Count | Average (₹) |\n|---|---|---|\n| First five | 5 | 2,560 |\n| All six | 6 | 2,500 |\n\nThe sixth bill is:",
            [r"Old total $= 5 \times 2560 = 12800$.",
             r"New total $= 6 \times 2500 = 15000$.",
             r"Sixth bill $= 15000 - 12800 = 2200$."],
            "₹2,200"),
    ],
)

# ============================================================ di-growth
GROWTH = dict(
    concept=(
        "Growth questions track a value rising year after year: one year's rate, the total rate over "
        "several years, or the starting value when only the end is known.\n\n"
        "Every version still rests on one line: new value $=$ old value $\\times$ growth multiplier."
    ),
    notes=r"""### The growth multiplier
Growth of $r\%$ multiplies by $\left(1 + \dfrac{r}{100}\right)$.

Revenue 80 crore grows 20%: $80 \times \dfrac{120}{100} = 96$ crore. A 20% fall would multiply by $\dfrac{80}{100}$.

> **Rule:** Never add percentages of different bases. Convert each to a multiplier and multiply.

### Two rises in a row
10% growth twice is not 20%.

$$\left(\frac{110}{100}\right)^2 = \frac{121}{100} = 1.21 \Rightarrow 21\%$$

The extra 1% comes from the first rise earning the second year's growth.

> **Watch:** Successive changes of +10% and −10% end below the start: $1.1 \times 0.9 = 0.99$.

### Rate over several years
Over two years, the total growth multiplier is the ratio of end to start: $\dfrac{144}{80} = 1.8$, so 80% in two years. If asked for the yearly rate assuming equal years, take the square root — but most exam questions want the total rate only.

> **Tip:** End ÷ start gives the total multiplier instantly. 144/80 = 1.8 means +80%.

### Working backwards
A value after 50% growth is 45,000. Before the growth it was $\dfrac{45000}{1.5} = 30,000$.

Divide by the multiplier; never subtract 50% of 45,000.

> **Example:** If 14,400 is 72% of a number, the number is $14400 \div 0.72 = 20,000$. Same reversal, percentage base.

### Which year grew fastest?
App users (thousands): 40, 60, 96, 120.

| Year | 2021 | 2022 | 2023 |
|---|---|---|---|
| Growth | $\dfrac{20}{40} = 50\%$ | $\dfrac{36}{60} = 60\%$ | $\dfrac{24}{96} = 25\%$ |

2022 grew fastest even though 2023 added 24k users, more than 2021's 20k.

> **Watch:** Rate divides by that year's own base; each year has its own.

### Depreciation: growth in reverse
Falling values follow the same multiplier idea with a number below 1.

A machine worth ₹50,000 loses 10% each year. After two years: $50000 \times 0.9 \times 0.9 = ₹40,500$. The loss is $19\%$, not $20\%$, because the second year's 10% acts on a smaller value.

> **Watch:** Straight-line thinking (50,000 − 5,000 − 5,000 = 40,000) is the planted option. Percent decay always shrinks the base.

### Chained different rates
A town of 8,000 grows 10% one year, then 5% the next: $8000 \times 1.1 = 8800$, then $8800 \times 1.05 = 9240$. The total growth is $\dfrac{9240}{8000} - 1 = 15.5\%$, and $10\% + 5\% = 15\%$ is close but wrong.

> **Tip:** Multiply step by step in the order the years come; each rate feeds on the previous result.

### Comparing two growers
Plant A: 100 → 180, up 80%. Plant B: 50 → 100, up 100%. B grew faster by 20 percentage points, though A added more units.

> **Tip:** "By how many percentage points" subtracts the two rates; "by how much percent more" divides the rates. The exam usually wants the points.
""",
    formulas=[
        {"name": "Growth multiplier", "tex": r"\text{new} = \text{old}\left(1+\frac{r}{100}\right)"},
        {"name": "Successive growth", "tex": r"r_{total} = \left(1+\frac{a}{100}\right)\left(1+\frac{b}{100}\right)-1"},
        {"name": "Reverse to original", "tex": r"\text{old} = \frac{\text{new}}{1+\frac{r}{100}}"},
        {"name": "Total multiplier", "tex": r"\frac{\text{end}}{\text{start}} = 1 + \frac{r_{total}}{100}"},
    ],
    tricks=[
        {"title": "Multipliers beat repeated percenting",
         "body": "Chain growth as multipliers: +10% then +10% is 1.1 x 1.1 = 1.21. One multiplication, no compounding errors.",
         "example": {"q": "A value rises 10% each year for 2 years. Total growth?",
                     "steps": [r"$1.10 \times 1.10 = 1.21$.",
                               r"Total growth $= 21\%$."],
                     "answer": "21%"}},
        {"title": "End over start",
         "body": "The total growth multiplier over any span is just the last value divided by the first. 144/80 = 1.8 → +80%.",
         "example": {"q": "Revenue went from 80 crore to 144 crore in two years. Total growth?",
                     "steps": [r"$144 \div 80 = 1.8$.",
                               r"Total growth $= 80\%$."],
                     "answer": "80%"}},
    ],
    mistakes=[
        {"wrong": "Adding two successive rates: 10% + 10% = 20%.",
         "right": "Multiply the multipliers: 1.1 x 1.1 = 1.21."},
        {"wrong": "Subtracting the percent of the final value to reverse a rise.",
         "right": "Divide by the multiplier: 45000 ÷ 1.5."},
        {"wrong": "Mixing 'percentage points' with 'percent more'.",
         "right": "Points subtract rates; percent more divides them."},
        {"wrong": "Judging the fastest year by units added.",
         "right": "Divide each rise by that year's own base."},
        {"wrong": "Averaging yearly rates for the span rate.",
         "right": "Use end ÷ start for the true span multiplier."},
    ],
    revision=[
        r"new $=$ old $\times \left(1+\dfrac{r}{100}\right)$.",
        r"Successive: multiply multipliers; $+10\%,+10\% \to +21\%$.",
        r"$+10\%$ then $-10\%$ ends $1\%$ below the start.",
        r"Reverse: divide by the multiplier.",
        r"Span rate: end $\div$ start.",
        "Fastest year: each rise over its own base.",
    ],
    patterns=[
        pat("di-gr-p1", "One year's growth rate", "very common",
            "A table of yearly values; one year's percent growth is asked.",
            r"\frac{V_2 - V_1}{V_1} \times 100\%",
            ["Take the two values around that year.",
             "Divide the rise by the earlier value.",
             "Multiply by 100."],
            "A rate needs its own base year.",
            "Revenue of a company (in ₹ crore):\n\n| Year | 2020 | 2021 | 2022 | 2023 |\n|---|---|---|---|---|\n| Revenue | 80 | 96 | 120 | 144 |\n\nThe growth rate in 2021 over 2020 is:",
            [r"Rise $= 96 - 80 = 16$.",
             r"$\dfrac{16}{80} \times 100 = 20\%$."],
            "20%"),
        pat("di-gr-p2", "Growth over two years", "common",
            "The total percentage change after two successive rises is asked.",
            r"\left(1+\frac{a}{100}\right)\left(1+\frac{b}{100}\right)-1",
            ["Write each rise as a multiplier.",
             "Multiply the multipliers.",
             "Subtract 1 for the total rate."],
            "Each rise compounds on the one before it.",
            "An item's price rises 10% in the first year and 10% again in the second year. The total percentage rise is:\n\n| Year | Rise |\n|---|---|\n| 1st | 10% |\n| 2nd | 10% |",
            [r"$1.10 \times 1.10 = 1.21$.",
             r"Total rise $= 21\%$."],
            "21%"),
        pat("di-gr-p3", "Value before the growth", "common",
            "The end value and the growth rate are known; the start is asked.",
            r"\text{old} = \frac{\text{new}}{1+\frac{r}{100}}",
            ["Turn the rate into a multiplier.",
             "Divide the end value by it.",
             "Check by growing the answer back up."],
            "Growth multiplies, so reversal divides.",
            "A company's revenue grew 50% this year and reached ₹45,000 crore. The revenue before the growth was:\n\n| Quantity | Value |\n|---|---|\n| Revenue after growth | ₹45,000 crore |\n| Growth during the year | +50% |",
            [r"Multiplier $= 1.5$.",
             r"$45000 \div 1.5 = 30000$."],
            "₹30,000 crore"),
        pat("di-gr-p4", "Fastest growing year in a table", "common",
            "A value table across years; which year grew at the highest rate.",
            r"\max_i \frac{V_{i+1}-V_i}{V_i}",
            ["Compute each year's rise.",
             "Divide each by its own base.",
             "Name the year with the top rate."],
            "Equal units added can hide very different rates.",
            "Users of an app (in thousands):\n\n| Year | 2020 | 2021 | 2022 | 2023 |\n|---|---|---|---|---|\n| Users | 40 | 60 | 96 | 120 |\n\nIn which year was the growth rate the highest?",
            [r"2021: $20/40 = 50\%$.",
             r"2022: $36/60 = 60\%$; 2023: $24/96 = 25\%$.",
             r"Highest: 2022."],
            "2022"),
        pat("di-gr-p5", "Two entities compared", "common",
            "Two plants, shops or teams; whose growth was faster, and by how much.",
            r"\frac{N_2 - N_1}{N_1} \times 100\% \text{ for each}",
            ["Compute each grower's rate.",
             "Compare the two rates.",
             "Points: subtract; percent more: divide."],
            "A bigger absolute gain can still be a smaller rate.",
            "Production of two plants (in tonnes):\n\n| Plant | 2022 | 2023 |\n|---|---|---|\n| A | 100 | 180 |\n| B | 50 | 100 |\n\nB's growth rate exceeds A's by how many percentage points?",
            [r"A: $\dfrac{80}{100} = 80\%$.",
             r"B: $\dfrac{50}{50} = 100\%$.",
             r"$100 - 80 = 20$ points."],
            "20 percentage points"),
    ],
)

# ============================================================ patch
PATCHES = {
    "di-table": TABLE,
    "di-percent": PERCENT,
    "di-pie": PIE,
    "di-average": AVERAGE,
    "di-growth": GROWTH,
}

data = json.loads(TOPIC.read_text(encoding="utf-8"))
for sid, patch in PATCHES.items():
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = {p["id"] for p in patch["patterns"]}
    assert old_ids <= new_ids, f"{sid}: dropped ids {old_ids - new_ids}"
    others = {p["id"] for s in data["subtopics"] for p in s.get("patterns", []) if s["id"] != sid}
    assert not (others & new_ids), f"{sid}: clash {others & new_ids}"
    notes = patch["notes"]
    assert 2500 <= len(notes) <= 5000, f"{sid}: notes {len(notes)} chars"
    n_old = len(sub.get("patterns", []))
    sub.update(concept=patch["concept"], notes=notes.strip() + "\n",
               formulas=patch.get("formulas", sub.get("formulas", [])),
               tricks=patch.get("tricks", sub.get("tricks", [])),
               mistakes=patch["mistakes"], revision=patch["revision"],
               patterns=patch["patterns"])
    print(f"{sid}: notes {len(notes)} chars, patterns {n_old} -> {len(patch['patterns'])}")

with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("data-interpretation.json updated")
