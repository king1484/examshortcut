"""Phase-2 deep content for quant/data-interpretation — part 1: di-table, di-percent, di-pie."""
from fractions import Fraction as F

from _lib import Sub, ind, rs, num, pct, pick, nearest


def md_table(headers, rows):
    """Markdown table. rows: list of lists (any values)."""
    out = ["| " + " | ".join(str(h) for h in headers) + " |",
           "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


# shared table: car production (thousand units) of four companies
YEARS = [2019, 2020, 2021, 2022, 2023]
CARS = {
    "P": [120, 135, 150, 140, 165],
    "Q": [90, 110, 105, 125, 130],
    "R": [150, 145, 160, 170, 175],
    "S": [80, 95, 100, 110, 120],
}


def cars_table():
    rows = [[y] + [CARS[c][i] for c in "PQRS"] for i, y in enumerate(YEARS)]
    return ("Production of cars (in thousands) by four companies:\n\n"
            + md_table(["Year", "P", "Q", "R", "S"], rows))


# ---------------- di-table ----------------

def build_table():
    S = Sub("di-table")
    S.notes = r"""### What a DI table is
A table is data arranged in **rows** (going across) and **columns** (going down). Think of a school marks register: each row is a student, each column is a subject. In competitive exams a table usually shows years down the side and companies, states or products across the top. Every question is a small calculation on a few cells, so the real skill is **reading the right cells quickly and correctly**.

### Step 1: read the frame before the numbers
Before touching any question, spend 15 seconds on the frame:
- **Title and units.** "Production (in thousand tonnes)" means a cell showing 45 is really 45,000 tonnes. Options are often written in the same unit, but sometimes they convert — check.
- **Row and column labels.** Is the year down the side or across the top? Mixing up a row and a column is the most common silly error.
- **Totals row or column.** If the table already has a total, use it instead of adding again.

### Step 2: the five things tables ask
1. **Total and difference.** Add a row or a column; or find the gap between two cells or two totals. Add in friendly pairs: $120 + 150 + 135 + 165 + 140$ becomes $(120+150+140) + (135+165) = 410 + 300 = 710$.
2. **Ratio.** "Ratio of A to B" means $\frac{A}{B}$ reduced to lowest terms. Cancel the common factor first: $255 : 230$, both divide by 5, gives $51 : 46$. Keep the order the question uses — $A : B$ is not $B : A$.
3. **Maximum / minimum.** "In which year was the gap between R and S the least?" Write the small list of gaps (70, 50, 60, 60, 55) in the margin and pick. Do not compute more than the question needs.
4. **Counting years that satisfy a condition.** "In how many years was P above its own average?" Find the average once, then tick cells. Watch "more than" versus "at least": a cell equal to the average is **not** more than it.
5. **Missing value.** If a total or an average is given, the missing cell is $\text{total} - \text{sum of the known cells}$; with an average, first make the total $= \text{average} \times \text{count}$.

### Worked example
A table shows sales (in ₹ lakh) of four shops: A 240, B ?, C 310, D 185, with a total of 990. Missing B $= 990 - (240 + 310 + 185) = 990 - 735 = 255$.

### Speed habits that save marks
- **Round only at the end.** DI tables are built with friendly numbers, so exact answers usually come out whole.
- **Use the options.** If the options are 540, 550, 560, 570 and your unit digits add to 0, only 550 and 570 survive. The last digit of a sum is a free check.
- **One table, many questions.** In Tier-2 style sets, 4 or 5 questions use one table. Write column totals once in the margin and reuse them.
- **Equal is a trap.** In "more than" counting questions, the setter often places one cell exactly equal to the benchmark.

### Common mistakes
- Reading 2021's row when the question says 2020.
- Reporting the ratio upside down.
- Forgetting the unit (thousands, lakh, crore) when options are in full numbers.
- Adding every cell when only two were needed.

### Quick revision
| Ask | Method |
|---|---|
| Total | Add in friendly pairs; check the last digit |
| Difference | Subtract the two totals, not every cell pair |
| Ratio | $A : B$, cancel common factors, keep the order |
| Max / min | List the small derived numbers, then pick |
| Count years | Benchmark once; "more than" excludes equal |
| Missing cell | Total − known sum; total = average × count |
"""

    S.pattern("di-tb-p1", "Total or difference of rows / columns", "very common",
      "'Total production of Q over the years', 'by how much does 2023 exceed 2019' — plain addition or subtraction of cells.",
      r"\text{Difference} = \sum \text{row}_1 - \sum \text{row}_2",
      r"""1. Locate the row/column (check the unit).
2. Add in friendly pairs; keep running subtotals.
3. For a difference of totals, subtract totals once instead of cell by cell.

Why: every total question is only addition — speed comes from grouping.""",
      cars_table() + "\n\nThe total production of company R over the five years is:",
      r"$150 + 145 + 160 + 170 + 175 = 800$ thousand.")

    S.pattern("di-tb-p2", "Ratio of cells or of sums", "very common",
      "'The ratio of X to Y', often of sums of two cells each.",
      r"A : B = \frac{A}{B}\ \text{in lowest terms}",
      r"""1. Build each side (a cell or a sum of cells).
2. Cancel the HCF.
3. Keep the order asked; the reversed ratio is always an option.

Why: a ratio is just a fraction written with a colon.""",
      cars_table() + "\n\nThe ratio of production of Q in 2021 to that of R in 2021 is:",
      r"$105 : 160$; divide by 5 → $21 : 32$.")

    S.pattern("di-tb-p3", "Which year / item is the maximum or minimum", "common",
      "'In which year was the difference / total / growth the highest (or least)?'",
      None,
      r"""1. Compute the small derived number for each year (gap, total or % rise).
2. Write them in a row in the margin.
3. Pick the extreme; check that the question asked least or most.

Why: the setter hides the answer behind one derived number — never guess from raw cells.""",
      cars_table() + "\n\nIn which year was the total production of P and Q together the highest?",
      r"Totals: 210, 245, 255, 265, 295 → **2023**.")

    S.pattern("di-tb-p4", "Count the years meeting a condition", "common",
      "'In how many years was …more than / less than…'",
      None,
      r"""1. Fix the benchmark (an average, another row, a stated number).
2. Tick each year that strictly meets the condition.
3. Equal values do not count for 'more than'.

Why: counting is easy; the traps are the benchmark and the tie.""",
      cars_table() + "\n\nIn how many years was the production of S at least 100 thousand?",
      r"100, 110, 120 → **3** years (2021, 2022, 2023). 'At least' includes the equal value.")

    S.pattern("di-tb-p5", "Missing value from a given total or average", "occasional",
      "A cell is blank or marked '?', and a total or an average is printed.",
      r"x = \text{total} - \sum \text{known} = n\bar{x} - \sum \text{known}",
      r"""1. Make the total (multiply the average by the count if needed).
2. Subtract the known cells.

Why: the total is the only thing that ties the cells together.""",
      "Sales (₹ lakh): A 240, B ?, C 310, D 185; total 990. Sales of B are:",
      r"$990 - 735 = 255$ lakh.")

    T = cars_table()
    # q1
    v = sum(CARS["Q"])
    assert v == 560
    S.q("di-tb-p1", "easy", T + "\n\nThe total production of company Q over the five years (in thousands) is:",
        ["560", "550", "570", "540"], str(v),
        r"$90 + 110 + 105 + 125 + 130 = 560$ thousand.",
        r"Pairs: $(90+110) + (105+125) + 130 = 200 + 230 + 130 = 560$.", 35)
    # q2
    t23 = sum(CARS[c][4] for c in "PQRS")
    t19 = sum(CARS[c][0] for c in "PQRS")
    d = t23 - t19
    assert (t23, t19, d) == (590, 440, 150)
    S.q("di-tb-p1", "medium", T + "\n\nBy how much (in thousands) does the total production of all four companies in 2023 exceed that in 2019?",
        ["150", "140", "160", "130"], str(d),
        r"2023: $165 + 130 + 175 + 120 = 590$. 2019: $120 + 90 + 150 + 80 = 440$. Difference $= 150$ thousand.",
        r"Cell-wise gaps: $45 + 40 + 25 + 40 = 150$ — no need for full totals.", 45)
    # q3
    a = CARS["P"][0] + CARS["P"][1]
    b = CARS["S"][3] + CARS["S"][4]
    r = F(a, b)
    assert (a, b, r) == (255, 230, F(51, 46))
    S.q("di-tb-p2", "medium", T + "\n\nThe ratio of the total production of P in 2019 and 2020 to the total production of S in 2022 and 2023 is:",
        ["51 : 46", "46 : 51", "17 : 15", "51 : 44"], f"{r.numerator} : {r.denominator}",
        r"P: $120 + 135 = 255$. S: $110 + 120 = 230$. $255 : 230 = 51 : 46$ (divide by 5).",
        r"Divide both sums by 5 at once.", 45)
    # q4
    gaps = [CARS["R"][i] - CARS["S"][i] for i in range(5)]
    assert gaps == [70, 50, 60, 60, 55]
    yr = YEARS[gaps.index(min(gaps))]
    assert gaps.count(min(gaps)) == 1 and yr == 2020
    S.q("di-tb-p3", "medium", T + "\n\nIn which year was the difference between the production of R and S the least?",
        ["2020", "2023", "2021", "2019"], str(yr),
        r"Gaps R − S: 70, 50, 60, 60, 55. Least is 50 in **2020**.",
        r"List the five gaps in the margin; don't compare raw cells.", 40)
    # q5
    avgP = F(sum(CARS["P"]), 5)
    cnt = sum(1 for x in CARS["P"] if x > avgP)
    assert avgP == 142 and cnt == 2
    S.q("di-tb-p4", "medium", T + "\n\nIn how many years was the production of P more than its own five-year average?",
        ["1", "2", "3", "4"], str(cnt),
        r"Average of P $= \frac{710}{5} = 142$. Years above 142: 150 (2021) and 165 (2023) → **2**. 140 is just below.",
        r"Deviation check from 140: $-20, -5, +10, 0, +25$ sum to $+10$, so average $= 142$.", 45)
    # q6
    miss = 1250 - (240 + 310 + 185 + 260)
    assert miss == 255
    tb = md_table(["Product", "A", "B", "C", "D", "E", "Total"], [["Sales (units)", 240, "?", 310, 185, 260, "1,250"]])
    S.q("di-tb-p5", "easy", "Sales of five products in a month:\n\n" + tb + "\n\nThe sales of product B are:",
        ["255", "245", "265", "250"], str(miss),
        r"Known sum $= 240 + 310 + 185 + 260 = 995$. B $= 1250 - 995 = 255$.",
        r"Last digits: known cells end in 0+0+5+0 = 5, total ends in 0 → B ends in 5: only 255 or 245 or 265 — then compute.", 35)
    # q7
    r = F(CARS["R"][2], CARS["Q"][2])
    assert r == F(32, 21)
    S.q("di-tb-p2", "easy", T + "\n\nThe ratio of production of R to that of Q in 2021 is:",
        ["32 : 21", "21 : 32", "16 : 11", "30 : 21"], "32 : 21",
        r"$160 : 105$; divide by 5 → $32 : 21$.",
        r"Order: R first, Q second.", 30)
    # q8
    rise = {c: F(CARS[c][4] - CARS[c][0], CARS[c][0]) * 100 for c in "PQRS"}
    best = max(rise, key=rise.get)
    assert best == "S" and rise["S"] == 50 and sorted(rise.values())[-2] < 50
    # absolute rise tie check: P rose 45 (largest absolute) - the trap
    assert max("PQRS", key=lambda c: CARS[c][4] - CARS[c][0]) == "P"
    S.q("di-tb-p3", "hard", T + "\n\nWhich company showed the highest percentage increase in production from 2019 to 2023?",
        ["P", "Q", "R", "S"], best,
        r"Rises: P $\frac{45}{120} = 37.5\%$, Q $\frac{40}{90} \approx 44.4\%$, R $\frac{25}{150} \approx 16.7\%$, S $\frac{40}{80} = 50\%$ → **S**.",
        r"P has the biggest absolute rise (45) but the biggest base too; S doubles half-way (40 on 80).", 60)
    # q9
    wins = [i for i in range(5) if CARS["P"][i] + CARS["Q"][i] > CARS["R"][i] + CARS["S"][i]]
    assert [CARS["P"][i] + CARS["Q"][i] for i in range(5)] == [210, 245, 255, 265, 295]
    assert [CARS["R"][i] + CARS["S"][i] for i in range(5)] == [230, 240, 260, 280, 295]
    assert len(wins) == 1
    S.q("di-tb-p4", "hard", T + "\n\nIn how many years was the combined production of P and Q more than the combined production of R and S?",
        ["1", "2", "0", "3"], str(len(wins)),
        r"P+Q: 210, 245, 255, 265, 295. R+S: 230, 240, 260, 280, 295. Only 2020 (245 > 240) → **1**. 2023 is a tie (295 = 295), which does not count.",
        r"Compare the gap $(P - R) + (Q - S)$ per year: $-20, +5, -5, -15, 0$.", 60)
    # q10
    tot = 5 * 48
    miss = tot - (42 + 55 + 38 + 50)
    assert miss == 55
    tb = md_table(["Year", 2019, 2020, 2021, 2022, 2023], [["Exports (₹ crore)", 42, 55, 38, 50, "?"]])
    S.q("di-tb-p5", "medium", "Exports of a firm:\n\n" + tb + "\n\nIf the average export over the five years is ₹48 crore, the export in 2023 is:",
        ["₹55 crore", "₹48 crore", "₹52 crore", "₹60 crore"], "₹55 crore",
        r"Total $= 5 \times 48 = 240$. Known $= 42 + 55 + 38 + 50 = 185$. 2023 $= 240 - 185 = 55$.",
        r"Deviations from 48: $-6, +7, -10, +2$ sum to $-7$, so the last must be $48 + 7 = 55$.", 40)
    return S


# ---------------- di-percent ----------------

SALES = {2019: 160, 2020: 200, 2021: 260, 2022: 250, 2023: 320}


def sales_table():
    return ("Annual sales of a company (₹ crore):\n\n"
            + md_table(["Year"] + list(SALES), [["Sales"] + list(SALES.values())]))


def build_percent():
    S = Sub("di-percent")
    S.notes = r"""### Why percentages rule DI
Raw numbers are hard to compare. A shop that grows from ₹100 to ₹150 and a factory that grows from ₹1,000 to ₹1,100 both "increased", but by very different amounts relative to their size. Percentages put everything on a scale of 100, so that fair comparison is possible. Almost every DI set has at least one percentage question.

### Percentage change — the base is the OLD value
$$\%\ \text{change} = \frac{\text{new} - \text{old}}{\text{old}} \times 100$$
- Sales go from 160 to 200: change $= 40$, base $= 160$, so $\frac{40}{160} \times 100 = 25\%$.
- Sales go from 260 to 250: change $= -10$, base $= 260$, so a fall of $\frac{10}{260} \times 100 \approx 3.85\%$.
The "old" value is the **earlier year** or the value the question says "over" or "compared with". Dividing by the new value is the number-one trap, and its result is always among the options.

### "X is what percent of Y"
$$\frac{X}{Y} \times 100$$
The value after "of" is the base. ₹200 as a percent of ₹320 is $\frac{200}{320} = 62.5\%$.

### "X is what percent more than Y"
$$\frac{X - Y}{Y} \times 100$$
₹320 is $\frac{120}{200} = 60\%$ more than ₹200. But ₹200 is $\frac{120}{320} = 37.5\%$ **less** than ₹320. The same gap gives different percentages because the base changes.

### Share of a total
A part as a percent of the whole: $\frac{\text{part}}{\text{total}} \times 100$. If a family spends ₹12,000 of ₹36,000 on food, the food share is $33\tfrac{1}{3}\%$. Add parts first when two items are asked together.

### Percentage points versus percent
If a school's pass rate rises from 60% to 72%:
- The rise is **12 percentage points** (simple subtraction of two percentages).
- The rise is **20 percent** in relative terms ($\frac{12}{60} \times 100$).
Read which one is asked. "By how many percentage points" means subtract; "by what percent" means divide by the old rate.

### Largest percentage rise — do not trust the biggest jump
In a series 160, 200, 260, 250, 320 the biggest **absolute** rise is 2023 (+70), but the biggest **percentage** rise is 2021 ($\frac{60}{200} = 30\%$ against $\frac{70}{250} = 28\%$). A small base makes a small jump look big in percent terms.

### Useful fraction table
| Fraction | % | Fraction | % |
|---|---|---|---|
| $\frac{1}{8}$ | 12.5 | $\frac{1}{3}$ | 33.33 |
| $\frac{1}{6}$ | 16.67 | $\frac{3}{8}$ | 37.5 |
| $\frac{1}{5}$ | 20 | $\frac{5}{8}$ | 62.5 |
| $\frac{1}{4}$ | 25 | $\frac{2}{3}$ | 66.67 |

### Quick revision
- % change $= \frac{\text{new} - \text{old}}{\text{old}} \times 100$ — base is the earlier value.
- "What percent of Y" → base Y. "More than Y" → base Y.
- Same gap, different base: 60% more ≠ 37.5% less.
- Percentage points = subtract rates; percent change of a rate = divide by old rate.
- Biggest absolute jump is not always the biggest % jump.
"""

    S.pattern("di-pc-p1", "Percentage increase / decrease between two periods", "very common",
      "'The percentage increase (or decrease) in sales from 2021 to 2022'.",
      r"\frac{\text{new} - \text{old}}{\text{old}} \times 100",
      r"""1. Old = the earlier year; new = the later year.
2. Change ÷ old × 100.
3. For 'approximately', match the nearest option.

Why: a change is measured against where you started.""",
      sales_table() + "\n\nThe percentage increase in sales from 2022 to 2023 is:",
      r"$\frac{320 - 250}{250} \times 100 = 28\%$.")

    S.pattern("di-pc-p2", "X as a percent of Y / percent more or less than", "very common",
      "'2020 sales are what percent of 2023 sales?', 'By what percent is A more than B?'",
      r"\frac{X}{Y} \times 100,\qquad \frac{X - Y}{Y} \times 100",
      r"""1. The word 'of' or 'than' points to the base Y.
2. Divide by the base, multiply by 100.
3. More-than and less-than answers differ — check direction.

Why: every percent is a fraction of one chosen base.""",
      sales_table() + "\n\nBy what percent are the 2023 sales more than the 2019 sales?",
      r"$\frac{320 - 160}{160} \times 100 = 100\%$.")

    S.pattern("di-pc-p3", "Share of a total", "common",
      "A breakdown of a total (expenses, votes, students) and 'what percent of the total is…'.",
      r"\frac{\text{part}}{\text{total}} \times 100",
      r"""1. Find the total (add cells if not printed).
2. Add the parts asked together.
3. Divide and convert with the fraction table.

Why: a share is a part over the whole.""",
      "A family spends ₹12,000 on food out of a total of ₹36,000. Food's share is:",
      r"$\frac{12000}{36000} = \frac{1}{3} = 33\tfrac{1}{3}\%$.")

    S.pattern("di-pc-p4", "Percentage points vs percent change of a rate", "common",
      "The data itself is in percent (pass rate, literacy rate, market share) and the question asks how much it changed.",
      r"\text{points} = r_2 - r_1,\qquad \%\ \text{change} = \frac{r_2 - r_1}{r_1} \times 100",
      r"""1. 'Percentage points' → subtract the two rates.
2. 'By what percent' → divide the gap by the old rate.
3. Both answers usually appear as options.

Why: a rate is already a percent — changing it can be read two ways.""",
      "A pass rate rises from 60% to 72%. By what percent did it rise?",
      r"Points $= 12$; percent $= \frac{12}{60} \times 100 = 20\%$.")

    S.pattern("di-pc-p5", "Year with the highest / lowest percentage change", "common",
      "'In which year was the percentage increase over the previous year maximum?'",
      None,
      r"""1. For each year compute change ÷ previous value (fractions are enough).
2. Compare the fractions, not the raw jumps.
3. Ignore years with a fall when a rise is asked.

Why: a small base inflates the percent — the biggest raw jump often loses.""",
      sales_table() + "\n\nIn which year was the lowest percentage increase over the previous year (ignore falls)?",
      r"Rises: 2020 25%, 2021 30%, 2023 28% → **2020**.")

    T = sales_table()
    # q1
    v = F(SALES[2020] - SALES[2019], SALES[2019]) * 100
    assert v == 25
    S.q("di-pc-p1", "easy", T + "\n\nThe percentage increase in sales from 2019 to 2020 is:",
        ["25%", "20%", "40%", "30%"], pct(v),
        r"$\frac{200 - 160}{160} \times 100 = \frac{40}{160} \times 100 = 25\%$.",
        r"Wrong base: $\frac{40}{200} = 20\%$ is the trap.", 30)
    # q2
    ch = {y: F(SALES[y] - SALES[y - 1], SALES[y - 1]) * 100 for y in range(2020, 2024)}
    assert ch == {2020: 25, 2021: 30, 2022: F(-10 * 100, 260), 2023: 28}
    best = max(ch, key=ch.get)
    assert best == 2021
    assert max(range(2020, 2024), key=lambda y: SALES[y] - SALES[y - 1]) == 2023  # absolute trap
    S.q("di-pc-p5", "medium", T + "\n\nIn which year was the percentage increase in sales over the previous year the highest?",
        ["2021", "2023", "2020", "2022"], str(best),
        r"2020: $\frac{40}{160} = 25\%$; 2021: $\frac{60}{200} = 30\%$; 2022: fall; 2023: $\frac{70}{250} = 28\%$ → **2021**.",
        r"2023 has the largest jump (70) but on a larger base — 28% < 30%.", 55)
    # q3
    ex = float(F(10, 260) * 100)
    opts, a = nearest([("3.85%", 3.85), ("4.17%", 4.17), ("3.33%", 3.33), ("4.5%", 4.5)], ex)
    S.q("di-pc-p1", "medium", T + "\n\nThe percentage decrease in sales from 2021 to 2022 is approximately:",
        opts, a,
        r"$\frac{260 - 250}{260} \times 100 = \frac{1000}{260} \approx 3.85\%$.",
        r"Base is 260 (the earlier year). $\frac{10}{250} = 4\%$ and $\frac{10}{240}$ are wrong-base traps.", 40)
    # q4
    v = F(SALES[2020], SALES[2023]) * 100
    assert v == F(125, 2)
    S.q("di-pc-p2", "medium", T + "\n\nThe sales in 2020 are what percent of the sales in 2023?",
        ["62.5%", "160%", "37.5%", "60%"], pct(v),
        r"$\frac{200}{320} \times 100 = 62.5\%$.",
        r"$\frac{200}{320} = \frac{5}{8} = 62.5\%$ from the fraction table.", 35)
    # q5
    v = F(SALES[2023] - SALES[2020], SALES[2020]) * 100
    assert v == 60
    S.q("di-pc-p2", "medium", T + "\n\nBy what percent are the sales in 2023 more than the sales in 2020?",
        ["60%", "37.5%", "62.5%", "120%"], pct(v),
        r"Gap $= 120$; base $= 200$ (the 'than' year). $\frac{120}{200} \times 100 = 60\%$.",
        r"37.5% is the gap over 320 — that answers 'less than', not 'more than'.", 35)
    # q6 share
    exp = {"Food": 12000, "Rent": 9000, "Education": 6000, "Transport": 3000, "Others": 6000}
    tot = sum(exp.values())
    assert tot == 36000
    tb = md_table(["Head", "Food", "Rent", "Education", "Transport", "Others"], [["Amount (₹)"] + [ind(v) for v in exp.values()]])
    v = F(exp["Education"] + exp["Transport"], tot) * 100
    assert v == 25
    S.q("di-pc-p3", "easy", "Monthly expenses of a family:\n\n" + tb + "\n\nEducation and Transport together make up what percent of the total expenses?",
        ["25%", "20%", "30%", "16.67%"], pct(v),
        r"Total $= ₹36{,}000$. Education + Transport $= ₹9{,}000$. $\frac{9000}{36000} = 25\%$.",
        r"9,000 is a quarter of 36,000.", 35)
    v2 = F(exp["Rent"], tot) * 100
    assert v2 == 25
    v3 = F(exp["Food"] - exp["Rent"], exp["Rent"]) * 100
    assert v3 == F(100, 3)
    S.q("di-pc-p3", "medium", "Monthly expenses of a family:\n\n" + tb + "\n\nWhat percent of the total expenses is spent on heads other than Food and Rent?",
        ["41.67%", "58.33%", "33.33%", "45%"], "41.67%",
        r"Other heads $= 6000 + 3000 + 6000 = ₹15{,}000$. $\frac{15000}{36000} = \frac{5}{12} \approx 41.67\%$.",
        r"Food + Rent $= 21000 = \frac{7}{12}$ of total, so the rest is $\frac{5}{12}$.", 45)
    assert round(float(F(15000, 36000) * 100), 2) == 41.67
    # q8 points
    r1, r2 = 60, 72
    S.q("di-pc-p4", "easy", "The pass percentage of a school was 60% in 2022 and 72% in 2023. By how many **percentage points** did it rise?",
        ["12", "20", "6", "16.67"], str(r2 - r1),
        r"Percentage points = simple difference of the two rates: $72 - 60 = 12$.",
        r"20 is the percent change ($\frac{12}{60}$), not the points.", 25)
    v = F(r2 - r1, r1) * 100
    assert v == 20
    S.q("di-pc-p4", "medium", "The pass percentage of a school was 60% in 2022 and 72% in 2023. By what **percent** did the pass percentage increase?",
        ["20%", "12%", "16.67%", "72%"], pct(v),
        r"Change $= 12$ points on a base of 60: $\frac{12}{60} \times 100 = 20\%$.",
        r"12% is the points answer; 16.67% divides by 72 (wrong base).", 30)
    # q10 compare changes
    g1 = F(SALES[2020] - SALES[2019], SALES[2019]) * 100
    g2 = F(SALES[2023] - SALES[2022], SALES[2022]) * 100
    assert g2 - g1 == 3
    S.q("di-pc-p5", "hard", T + "\n\nBy how many percentage points is the growth rate of 2022–23 more than that of 2019–20?",
        ["3", "30", "12", "5"], str(g2 - g1),
        r"2019–20: $\frac{40}{160} = 25\%$. 2022–23: $\frac{70}{250} = 28\%$. Difference $= 3$ percentage points.",
        r"Compare rates, not raw jumps (40 vs 70 would suggest 30).", 55)
    return S


# ---------------- di-pie ----------------

BUDGET = 72000
ANG = {"Food": 108, "Rent": 72, "Education": 54, "Transport": 36, "Savings": 45, "Others": 45}
assert sum(ANG.values()) == 360


def budget_pie():
    return (f"A pie chart shows a family's monthly budget of ₹{ind(BUDGET)}. The central angles are:\n\n"
            + md_table(["Head"] + list(ANG), [["Angle"] + [f"{v}°" for v in ANG.values()]]))


def build_pie():
    S = Sub("di-pie")
    S.notes = r"""### What a pie chart shows
A pie chart is a circle cut into slices (sectors). The whole circle stands for the **total** — the whole budget, all students, all sales. Each slice is one part. A bigger slice means a bigger share. Since a circle has $360^\circ$ at its centre, the total is spread over $360^\circ$.

In competitive exams the pie is often printed as a list of angles or percentages — read it exactly like a table.

### The three conversions
$$\text{value} = \frac{\text{angle}}{360^\circ} \times \text{total}$$
$$\text{angle} = \frac{\text{percent}}{100} \times 360^\circ = \text{percent} \times 3.6^\circ$$
$$\text{percent} = \frac{\text{angle}}{360^\circ} \times 100 = \frac{\text{angle}}{3.6}$$
Remember: **1% = 3.6°** and **1° = total ÷ 360**.

### Worked example: value of one degree
Budget ₹72,000, so $1^\circ = \frac{72000}{360} = ₹200$. Rent at $72^\circ$ is $72 \times 200 = ₹14{,}400$. Food at $108^\circ$ is $108 \times 200 = ₹21{,}600$. Finding "one degree" once turns every later question into one multiplication.

### Difference and ratio of two slices
- Difference: subtract the **angles** first, then convert once. Food − Education $= 108^\circ - 54^\circ = 54^\circ = 54 \times 200 = ₹10{,}800$.
- Ratio: the ratio of values equals the ratio of angles — the total cancels. Savings : Transport $= 45 : 36 = 5 : 4$.

### When the total is not given
If one slice's value is known, use proportion. Transport ($36^\circ$) is ₹9,000, so Food ($108^\circ$) is $\frac{108}{36} \times 9000 = ₹27{,}000$, and the total is $\frac{360}{36} \times 9000 = ₹90{,}000$.

### Two pie charts
Two years (or two companies) each with its own total. The same slice size does **not** mean the same value if the totals differ. Export share of Asia 30% of ₹400 crore = ₹120 crore; 27% of ₹500 crore = ₹135 crore. The share fell but the amount **rose** by 12.5%. Always convert each pie to values before comparing.

### Common mistakes
- Adding the angles of two sectors and expecting the percent of the **sum** to equal the sum of the percents — that one is true, but only because both share the same total of $360^\circ$.
- Using 100 instead of 360 when converting an angle to a value.
- Forgetting that two $45^\circ$ sectors of **different** pies can be different amounts.
- Reporting the angle when the value was asked (the question says "amount" or "degrees" — underline which).

### Handy angle table
| Percent | Angle | Percent | Angle |
|---|---|---|---|
| 5% | 18° | 25% | 90° |
| 10% | 36° | 30% | 108° |
| 12.5% | 45° | 50% | 180° |
| 20% | 72° | 75% | 270° |

### Quick revision
- Whole circle $= 360^\circ =$ total $= 100\%$.
- value $= \frac{\theta}{360} \times$ total; angle $= \% \times 3.6$.
- Find the value of $1^\circ$ once and reuse it.
- Differences and ratios: work with angles, convert at the end.
- Two pies: convert each to values; shares alone mislead.
"""

    S.pattern("di-pi-p1", "Angle → value", "very common",
      "Central angles and a total are given; the amount of one or two sectors asked.",
      r"\text{value} = \frac{\theta}{360^\circ} \times \text{total}",
      r"""1. Find the value of one degree: total ÷ 360.
2. Multiply by the sector's angle (add angles first for two sectors).

Why: the circle's 360 degrees are the total, shared in proportion.""",
      budget_pie() + "\n\nThe amount spent on Food is:",
      r"$1^\circ = ₹200$; Food $= 108 \times 200 = ₹21{,}600$.")

    S.pattern("di-pi-p2", "Percent ↔ angle conversion", "very common",
      "A sector given in % with the angle asked, or an angle with the % asked.",
      r"\theta = p \times 3.6^\circ,\qquad p = \frac{\theta}{3.6}",
      r"""1. Percent to angle: multiply by 3.6.
2. Angle to percent: divide by 3.6 (or by 360 then ×100).

Why: 100% is 360°, so 1% is 3.6°.""",
      "A sector is 15% of a pie chart. Its central angle is:",
      r"$15 \times 3.6 = 54^\circ$.")

    S.pattern("di-pi-p3", "Difference or ratio of two sectors", "common",
      "'How much more is spent on A than on B?' or 'ratio of A to B'.",
      r"A - B = \frac{\theta_A - \theta_B}{360} \times \text{total},\quad A : B = \theta_A : \theta_B",
      r"""1. Work with the angles (or percents) directly.
2. For a difference, convert the angle gap once.
3. For a ratio, the total cancels — reduce the angles.

Why: all sectors share the same total, so it is a common factor.""",
      budget_pie() + "\n\nThe ratio of the amount on Rent to that on Education is:",
      r"$72 : 54 = 4 : 3$.")

    S.pattern("di-pi-p4", "Two pie charts with different totals", "common",
      "Two pies (two years, two firms) with different totals; the change in one item is asked.",
      r"\text{value}_i = \frac{p_i}{100} \times T_i",
      r"""1. Convert the item to a value in each pie using its own total.
2. Then find the change or ratio of the values.
3. Never compare shares directly when totals differ.

Why: a smaller slice of a bigger pie can be more money.""",
      "Exports: 2022 total ₹400 crore, Asia 30%; 2023 total ₹500 crore, Asia 27%. The change in exports to Asia is:",
      r"$120 \to 135$: a rise of ₹15 crore.")

    S.pattern("di-pi-p5", "One sector known → total or another sector", "common",
      "No total is printed; the value of one sector is given.",
      r"\text{total} = \frac{360}{\theta_k} \times V_k,\qquad V_x = \frac{\theta_x}{\theta_k} \times V_k",
      r"""1. Value per degree $= V_k \div \theta_k$.
2. Multiply by 360 for the total, or by $\theta_x$ for another sector.

Why: every sector gets the same value per degree.""",
      "A sector of 40° stands for 1,600 students. The total number of students is:",
      r"$\frac{360}{40} \times 1600 = 14{,}400$.")

    T = budget_pie()
    per = F(BUDGET, 360)
    assert per == 200
    v = ANG["Rent"] * per
    assert v == 14400
    S.q("di-pi-p1", "easy", T + "\n\nThe amount spent on Rent is:",
        [rs(14400), rs(12000), rs(14000), rs(18000)], rs(v),
        r"$\frac{72}{360} \times 72000 = \frac{1}{5} \times 72000 = ₹14{,}400$.",
        r"$1^\circ = ₹200$; $72 \times 200$.", 30)
    v = F(ANG["Food"], 360) * 100
    assert v == 30
    S.q("di-pi-p2", "easy", T + "\n\nWhat percent of the budget is spent on Food?",
        ["30%", "36%", "25%", "108%"], pct(v),
        r"$\frac{108}{360} \times 100 = 30\%$.",
        r"Angle ÷ 3.6: $108 \div 3.6 = 30$.", 25)
    v = (ANG["Food"] - ANG["Education"]) * per
    assert v == 10800
    S.q("di-pi-p3", "medium", T + "\n\nHow much more is spent on Food than on Education?",
        [rs(10800), rs(21600), rs(5400), rs(12600)], rs(v),
        r"Angle gap $= 108^\circ - 54^\circ = 54^\circ$. $54 \times 200 = ₹10{,}800$.",
        r"Subtract angles, convert once.", 35)
    r = F(ANG["Savings"], ANG["Transport"])
    assert r == F(5, 4)
    S.q("di-pi-p3", "medium", T + "\n\nThe ratio of Savings to Transport is:",
        ["5 : 4", "4 : 5", "5 : 3", "9 : 8"], "5 : 4",
        r"Ratio of values = ratio of angles: $45 : 36 = 5 : 4$.",
        r"The total cancels — no need to find amounts.", 25)
    # p5: transport value known, no total
    v = F(ANG["Food"], ANG["Transport"]) * 9000
    assert v == 27000
    tb = md_table(["Head"] + list(ANG), [["Angle"] + [f"{a}°" for a in ANG.values()]])
    S.q("di-pi-p5", "medium", "A pie chart shows a family's monthly spending:\n\n" + tb + "\n\nIf the family spends ₹9,000 on Transport, how much does it spend on Food?",
        [rs(27000), rs(21600), rs(24000), rs(30000)], rs(v),
        r"Food is $\frac{108}{36} = 3$ times Transport: $3 \times 9000 = ₹27{,}000$.",
        r"Angle ratio 108 : 36 = 3 : 1.", 40)
    # p2 percent pie -> angle
    v = F(12 * 36, 10)
    assert v == F(216, 5)
    tb = md_table(["Subject", "Maths", "Science", "English", "Hindi", "Social Sc."], [["Share", "25%", "18%", "12%", "20%", "25%"]])
    S.q("di-pi-p2", "medium", "A pie chart shows the share of marks-weight given to five subjects:\n\n" + tb + "\n\nThe central angle of the English sector is:",
        ["43.2°", "12°", "36°", "48.6°"], f"{num(v)}°",
        r"$12 \times 3.6^\circ = 43.2^\circ$.",
        r"10% = 36°, 2% = 7.2° → 43.2°.", 30)
    # p5 total from sector
    v = F(360, 81) * 2700
    assert v == 12000
    S.q("di-pi-p5", "hard", "In a pie chart of students by stream, the Commerce sector has a central angle of 81° and represents 2,700 students. The total number of students is:",
        ["12,000", "10,800", "13,500", "9,000"], ind(v),
        r"Per degree $= \frac{2700}{81} = \frac{100}{3}$. Total $= 360 \times \frac{100}{3} = 12{,}000$.",
        r"$\frac{360}{81} = \frac{40}{9}$; $2700 \times \frac{40}{9} = 300 \times 40$.", 45)
    # p4 two pies
    a22 = F(30, 100) * 400
    a23 = F(27, 100) * 500
    v = (a23 - a22) / a22 * 100
    assert (a22, a23, v) == (120, 135, F(25, 2))
    tb = md_table(["Region", "Asia", "Europe", "Africa", "America", "Others"],
                  [["2022 (total ₹400 cr)", "30%", "20%", "10%", "25%", "15%"],
                   ["2023 (total ₹500 cr)", "27%", "18%", "15%", "24%", "16%"]])
    S.q("di-pi-p4", "hard", "Two pie charts show a company's exports by region:\n\n" + tb + "\n\nBy what percent did exports to Asia increase from 2022 to 2023?",
        ["12.5%", "−3%", "10%", "25%"], pct(v),
        r"2022: $30\% \times 400 = ₹120$ cr. 2023: $27\% \times 500 = ₹135$ cr. Rise $= \frac{15}{120} \times 100 = 12.5\%$.",
        r"The share fell (30 → 27) but the pie grew 25% — convert to values first.", 60)
    e22 = F(20, 100) * 400
    e23 = F(18, 100) * 500
    r = e22 / e23
    assert (e22, e23, r) == (80, 90, F(8, 9))
    S.q("di-pi-p4", "medium", "Two pie charts show a company's exports by region:\n\n" + tb + "\n\nThe ratio of exports to Europe in 2022 to that in 2023 is:",
        ["8 : 9", "10 : 9", "9 : 8", "4 : 5"], "8 : 9",
        r"2022: $20\% \times 400 = 80$. 2023: $18\% \times 500 = 90$. Ratio $= 8 : 9$.",
        r"10 : 9 compares the shares only — wrong when totals differ.", 45)
    # p1 two sectors
    angs = {"Sports": 70, "Music": 56, "Drama": 90, "Art": 64, "Science club": 80}
    assert sum(angs.values()) == 360
    v = F(angs["Sports"] + angs["Music"], 360) * 7200
    assert v == 2520
    tb = md_table(["Activity"] + list(angs), [["Angle"] + [f"{a}°" for a in angs.values()]])
    S.q("di-pi-p1", "medium", "7,200 students of a school each chose one activity. A pie chart shows:\n\n" + tb + "\n\nHow many students chose Sports or Music?",
        ["2,520", "2,400", "2,160", "2,880"], ind(v),
        r"Angles $70 + 56 = 126^\circ$. $1^\circ = \frac{7200}{360} = 20$ students. $126 \times 20 = 2{,}520$.",
        r"Add the angles first, then one multiplication.", 35)
    return S
