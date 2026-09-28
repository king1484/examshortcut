"""Phase-2 deep content for quant/data-interpretation — part 2: di-average, di-growth."""
from fractions import Fraction as F

from _lib import Sub, ind, rs, pct
from di_part1 import md_table


# ---------------- di-average ----------------

# weekly production (units), Mon-Sat
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
WEEK = [480, 520, 460, 540, 500, 500]
assert sum(WEEK) == 3000

# monthly production Jan-Jun
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
PROD = {"Jan": 2400, "Feb": 2600, "Mar": 2200, "Apr": 2800, "May": 2500, "Jun": 2500}
assert sum(PROD.values()) == 15000

# departments: (employees, average salary)
DEPT = {"A": (40, 25000), "B": (30, 32000), "C": (20, 28000), "D": (30, 40000)}


def week_table():
    return ("Production of a factory (in units):\n\n"
            + md_table(["Day"] + DAYS, [["Units"] + WEEK]))


def dept_table():
    rows = [[d, n, rs(s)] for d, (n, s) in DEPT.items()]
    return ("A company has four departments. The table shows the number of employees and their average salary:\n\n"
            + md_table(["Department", "Employees", "Average salary"], rows))


def build_average():
    S = Sub("di-average")
    S.notes = r"""### Averages inside a table
An average asks: "if everything were shared equally, how much would each get?" In DI the "things" are cells of a table — production of a factory across days, marks of students, salaries of departments. The rule never changes:
$$\text{average} = \frac{\text{sum of the cells}}{\text{number of cells}}$$
So every average question is really two questions: find the total, count the items, divide.

### Row or column average
A row (or column) average sums one row and divides by the count. Production over six days is 480, 520, 460, 540, 500, 500: the sum is 3,000, so the average is $3000 \div 6 = 500$ units. With friendly DI numbers the division is usually exact — if you get a messy decimal, recheck the cells you picked.

### Deviations: average without big sums
Instead of adding, pick any round number near the values and add the differences. For 480, 520, 460, 540, 500, 500 around 500: deviations $-20, +20, -40, +40, 0, 0$ add to $0$, so the average is exactly 500. This is fast and self-checking.

### Combined (weighted) average
Two groups with different sizes cannot be averaged plainly. Weight each group's average by its size:
$$\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2 + \dots}{n_1 + n_2 + \dots}$$
Department A: 40 employees at ₹25,000; department B: 30 at ₹32,000. Combined $= \frac{40 \times 25000 + 30 \times 32000}{70} = \frac{1960000}{70} = ₹28{,}000$ — closer to A's salary because A has more people. The plain average $\frac{25000 + 32000}{2} = 28{,}500$ is the planted trap.

### Per-period values
"Average sale per day" from a weekly total: divide the total by the number of periods, not by the number of rows of some other table. Total sales ₹84,000 in 6 days means ₹14,000 per day. Read the question: per day, per month, per employee — each divisor is different.

### Excluding or adding an item
- **Excluding**: new average $= \frac{\text{old total} - \text{removed value}}{\text{count} - 1}$. Dropping the lowest day (460) from our week: $\frac{3000 - 460}{5} = 508$.
- **Adding**: needed value $= \text{new average} \times (n+1) - \text{old total}$. To lift the 6-day average of 500 to 520 with a 7th day: $7 \times 520 - 3000 = 640$ units.

### Missing cell from an average
If the average is given, rebuild the total: total $= \text{average} \times n$. Then the missing cell is one subtraction. Six months average 2,500 units, so the half-year total is 15,000; if March is missing, March $= 15000 - (\text{other five})$.

### Quick revision
- average = total ÷ count; total = average × count.
- Deviation trick: pick a round base, add the differences, divide by n.
- Weighted average $\frac{\sum n_i \bar{x}_i}{\sum n_i}$ — plain average of the group means is the trap.
- Per day / per month: divide by periods, not rows.
- Exclude: $(T - x)/(n-1)$. Add: new avg × $(n+1) - T$.
- "More than the average" does not include cells equal to the average.
"""

    S.pattern("di-av-p1", "Average of a row / column", "very common",
      "'Average daily/monthly/annual production' — sum one row or column and divide.",
      r"\bar{x} = \frac{\sum \text{cells}}{n}",
      r"""1. Pick the cells (check the period count!).
2. Add in friendly pairs or use deviations from a round base.
3. Divide; a messy decimal usually means a wrong cell.

Why: an average is a total shared equally.""",
      week_table() + "\n\nThe average daily production (in units) is:",
      r"$3000 \div 6 = 500$ units.")

    S.pattern("di-av-p2", "Weighted / combined average of groups", "very common",
      "The table gives group sizes (employees, students) and each group's average; the overall average asked.",
      r"\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}",
      r"""1. Multiply each group's size by its average; add.
2. Divide by the total size.
3. Answer must sit between the group averages, nearer the bigger group.

Why: a bigger group pulls the combined average toward itself.""",
      dept_table() + "\n\nThe average salary of all employees of departments A and B together is:",
      r"$\frac{40 \times 25000 + 30 \times 32000}{70} = \frac{1960000}{70} = ₹28{,}000$.")

    S.pattern("di-av-p3", "Average per period from a total", "common",
      "'Average per day / per month / per worker' with a total given or summed.",
      r"\text{per period} = \frac{\text{total}}{\text{number of periods}}",
      r"""1. Build the total (add cells if needed).
2. Divide by the period count the question names.
3. Per worker = total ÷ workers; per day = total ÷ days — read the divisor.

Why: 'per' names the divisor.""",
      "A shop's sales in 6 days total ₹84,000. The average sale per day is:",
      r"$84000 \div 6 = ₹14{,}000$ per day.")

    S.pattern("di-av-p4", "Average after excluding or adding an item", "common",
      "'Excluding the least day…', 'with one more day the average becomes…'.",
      r"\text{exclude: } \frac{T - x}{n-1},\qquad \text{add: } x = \bar{x}_{new}(n+1) - T",
      r"""1. Old total $T = $ old average × n.
2. Excluding: subtract the item, divide by $n-1$.
3. Adding: new average × $(n+1)$ minus old total gives the needed value.

Why: the average always follows the total.""",
      week_table() + "\n\nIf the least productive day is excluded, the average production of the remaining days is:",
      r"$\frac{3000 - 460}{5} = \frac{2540}{5} = 508$ units.")

    S.pattern("di-av-p5", "Missing cell from a given average", "common",
      "An average is printed and one cell is missing; the missing cell asked.",
      r"x = n\bar{x} - \sum \text{known}",
      r"""1. Total = average × count.
2. Subtract the known cells.
3. Check the found cell fits the table's range.

Why: the average fixes the total, and the total fixes the missing cell.""",
      "Monthly production: Jan 2400, Feb 2600, Mar ?, Apr 2800, May 2500, Jun 2500; the six-month average is 2,500 units. March's production is:",
      r"Total $= 6 \times 2500 = 15000$; known $= 12800$; March $= 2200$.")

    # q1
    v = F(sum(WEEK), len(WEEK))
    assert v == 500
    S.q("di-av-p1", "easy", week_table() + "\n\nThe average daily production over the six days (in units) is:",
        ["500", "510", "490", "520"], str(v),
        r"Total $= 3000$; average $= \frac{3000}{6} = 500$ units.",
        r"Deviations from 500: $-20, +20, -40, +40, 0, 0$ — sum 0, so the average is 500.", 30)
    # q2
    q1 = sum(PROD[m] for m in ["Jan", "Feb", "Mar"])
    q2 = sum(PROD[m] for m in ["Apr", "May", "Jun"])
    a1, a2 = F(q1, 3), F(q2, 3)
    r = a1 / a2
    assert (q1, q2, a1, a2, r) == (7200, 7800, 2400, 2600, F(12, 13))
    mt = md_table(["Month"] + MONTHS, [["Production (units)"] + [PROD[m] for m in MONTHS]])
    S.q("di-av-p1", "medium", "Monthly production of a factory (in units):\n\n" + mt + "\n\nThe ratio of the average production of the first quarter (Jan–Mar) to that of the second quarter (Apr–Jun) is:",
        ["12 : 13", "13 : 12", "6 : 7", "11 : 12"], f"{r.numerator} : {r.denominator}",
        r"Q1 $= 7200$, average $2400$. Q2 $= 7800$, average $2600$. Ratio $2400 : 2600 = 12 : 13$.",
        r"Equal 3-month quarters: the ratio of totals works too (7200 : 7800).", 40)
    # q3
    ab = F(DEPT["A"][0] * DEPT["A"][1] + DEPT["B"][0] * DEPT["B"][1], DEPT["A"][0] + DEPT["B"][0])
    assert ab == 28000
    S.q("di-av-p2", "easy", dept_table() + "\n\nThe average salary of the employees of departments A and B together is:",
        [rs(28000), rs(28500), rs(27500), rs(29000)], rs(ab),
        r"$\frac{40 \times 25000 + 30 \times 32000}{40 + 30} = \frac{1960000}{70} = ₹28{,}000$.",
        r"₹28,500 is the plain average of 25,000 and 32,000 — wrong because the sizes differ.", 35)
    # q4
    tot_emp = sum(n for n, _ in DEPT.values())
    bill = sum(n * s for n, s in DEPT.values())
    allv = F(bill, tot_emp)
    assert (tot_emp, bill, allv) == (120, 3720000, 31000)
    S.q("di-av-p2", "hard", dept_table() + "\n\nThe average salary of all 120 employees of the company is:",
        [rs(31000), rs(31250), rs(30500), rs(31500)], rs(allv),
        r"Bill $= 40 \times 25000 + 30 \times 32000 + 20 \times 28000 + 30 \times 40000 = 37{,}20{,}000$. Average $= \frac{3720000}{120} = ₹31{,}000$.",
        r"Pair A+D: $1000000 + 1200000 = 2200000$; B+C: $960000 + 560000 = 1520000$; total 37,20,000.", 60)
    # q5
    v = F(sum(PROD.values()), 6)
    assert v == 2500
    mt = md_table(["Month"] + MONTHS, [["Production (units)"] + [PROD[m] for m in MONTHS]])
    S.q("di-av-p3", "easy", "Monthly production of a factory (in units):\n\n" + mt + "\n\nThe average monthly production (in units) is:",
        ["2,500", "2,600", "2,400", "2,550"], ind(v),
        r"Total $= 15000$ over 6 months: $\frac{15000}{6} = 2{,}500$.",
        r"Sum: $2400+2600+2200+2800+2500+2500 = 15000$.", 35)
    # q6
    v = F(84000, 6)
    assert v == 14000
    S.q("di-av-p3", "medium", "A shop sold goods worth ₹84,000 in 6 days. The average sale per day is:",
        [rs(14000), rs(12000), rs(16800), rs(12600)], rs(v),
        r"$\frac{84000}{6} = ₹14{,}000$ per day.",
        r"₹16,800 would be 5 days; ₹12,000 would be 7 — count the days.", 30)
    # q7
    w = sorted(WEEK)
    v = F(sum(WEEK) - w[0], 5)
    assert (w[0], v) == (460, 508)
    S.q("di-av-p4", "medium", week_table() + "\n\nIf the production of the least productive day is excluded, the average production of the remaining five days (in units) is:",
        ["508", "500", "510", "512"], str(v),
        r"Least day $= 460$. New average $= \frac{3000 - 460}{5} = 508$ units.",
        r"Divide by 5 (remaining days), not 6.", 40)
    # q8
    need = 7 * 520 - sum(WEEK)
    assert need == 640
    S.q("di-av-p4", "hard", week_table() + "\n\nThe factory works one more day (Sunday). What production on Sunday raises the seven-day average to 520 units?",
        ["640", "600", "660", "520"], str(need),
        r"Needed total $= 7 \times 520 = 3640$. Current $= 3000$. Sunday $= 640$ units.",
        r"$520 + 6 \times (520 - 500) = 520 + 120 = 640$.", 55)
    # q9
    miss = 6 * 2500 - (2400 + 2600 + 2800 + 2500 + 2500)
    assert miss == 2200
    mtq = md_table(["Month"] + MONTHS, [["Production (units)", 2400, 2600, "?", 2800, 2500, 2500]])
    S.q("di-av-p5", "easy", "Monthly production of a factory (in units):\n\n" + mtq + "\n\nIf the average monthly production is 2,500 units, the production in March is:",
        ["2,200", "2,300", "2,100", "2,400"], ind(miss),
        r"Total $= 6 \times 2500 = 15000$. Known $= 12800$. March $= 2200$ units.",
        r"Deviations from 2500: $-100, +100, ?, +300, 0, 0$ → ? $= -300$ → 2200.", 35)
    # q10
    tot = 24500
    miss = tot - (5200 + 4800 + 5100 + 4700)
    assert (tot / 5, miss) == (4900, 4700)
    vt = md_table(["Village", "P", "Q", "R", "S", "T"], [["Population", 5200, 4800, 5100, 4700, "?"]])
    S.q("di-av-p5", "medium", "Populations of five villages:\n\n" + vt + "\n\nIf the average population is 4,900, the population of village T is:",
        ["4,700", "4,600", "4,800", "4,900"], ind(miss),
        r"Total $= 5 \times 4900 = 24500$. Known $= 19800$. T $= 4700$.",
        r"Deviations from 4900: $+300, -100, +200, -200$ sum to $+200$, so T is $4900 - 200 = 4700$.", 40)
    return S


# ---------------- di-growth ----------------

REV = {2020: 80, 2021: 96, 2022: 120, 2023: 144}  # firm A, ₹ crore
B_REV = {2020: 50, 2023: 100}
IE = {2021: (60, 40), 2022: (80, 50), 2023: (130, 90)}  # income, expenditure ₹ lakh


def rev_table():
    return ("Revenue of firm A (in ₹ crore):\n\n"
            + md_table(["Year"] + list(REV), [["Revenue"] + list(REV.values())]))


def ie_table():
    rows = [[y, rs(i), rs(e)] for y, (i, e) in sorted(IE.items())]
    return ("Income and expenditure of a firm (in ₹ lakh):\n\n"
            + md_table(["Year", "Income", "Expenditure"], rows))


def build_growth():
    S = Sub("di-growth")
    S.notes = r"""### Growth = percentage change with a direction
When a table shows how one quantity moves year after year, each year-on-year jump is a **growth rate**:
$$g = \frac{\text{new} - \text{old}}{\text{old}} \times 100$$
Revenue going 80 → 96 crore grows $\frac{16}{80} \times 100 = 20\%$. A negative $g$ is a decline. The base is always the **earlier** year.

### Successive changes multiply — never add
A rise of $a\%$ multiplies the value by $\left(1 + \frac{a}{100}\right)$; a fall of $b\%$ multiplies by $\left(1 - \frac{b}{100}\right)$. Two changes in a row multiply:
$$\text{net factor} = \left(1 + \frac{a}{100}\right)\left(1 + \frac{b}{100}\right)$$
- $+10\%$ then $+10\%$: $1.1 \times 1.1 = 1.21$ → net $+21\%$, not $+20\%$.
- $+25\%$ then $-20\%$: $1.25 \times 0.8 = 1.00$ → net **zero** — a fall of 20% exactly cancels a rise of 25%.
- Revenue 80 → 96 → 120 → 144: factors $1.2 \times 1.25 \times 1.2 = 1.8$, so the total growth is $+80\%$.

### Running backwards
If the final value is known and the initial is asked, **divide** by the factor — never subtract percentages.
$$\text{initial} = \frac{\text{final}}{\text{factor}}$$
A salary became ₹45,000 after raises of 20% and 25%: original $= \frac{45000}{1.2 \times 1.25} = \frac{45000}{1.5} = ₹30{,}000$. A population of 14,400 after falls of 20% and 10%: original $= \frac{14400}{0.8 \times 0.9} = \frac{14400}{0.72} = 20{,}000$.

### Profit percent from an income–expenditure table
$$\text{profit}\% = \frac{\text{income} - \text{expenditure}}{\text{expenditure}} \times 100$$
The base is **expenditure**, not income — dividing by income is a standard trap. Highest profit **percent** is not always the year with highest profit **amount**: a small year can be very profitable in percentage terms.

### Comparing two firms
Compare growth rates in percent, and remember a percent and a percentage point are different. Firm A grows 80% and firm B grows 100% — B is ahead **by 20 percentage points**, not "by 20%". Also, the bigger absolute increase can belong to the slower grower (a large base).

### Worked example: a three-year chain
Revenue goes 80 → 96 → 120 → 144 (₹ crore). Year-on-year: $\frac{16}{80} = 20\%$, $\frac{24}{96} = 25\%$, $\frac{24}{120} = 20\%$. Overall factor $= 1.2 \times 1.25 \times 1.2 = 1.8$, so revenue is up $80\%$ over the span — although the growth rates add to $65\%$. One multiplication settles what addition gets wrong.

### Two quick self-checks
- A rise of $a\%$ followed by a fall of $a\%$ always leaves a **loss** of $\frac{a^2}{100}\%$: 20% up then 20% down nets $-4\%$.
- If the factor chain multiplies to exactly 1, the net change is zero — the setter loves $+25\%$ with $-20\%$ and $+33\tfrac{1}{3}\%$ with $-25\%$.

### Quick revision
- $g = \frac{\text{new} - \text{old}}{\text{old}} \times 100$; base = earlier year.
- Chain of changes: multiply factors $(1 \pm \frac{a}{100})$.
- $+25\%$ then $-20\%$ (or $+20\%$ then $-25\%$) = no net change.
- Reverse: divide the final value by the factor.
- Profit% = profit ÷ expenditure × 100.
- Growth comparison in percentage points = subtract the two rates.
"""

    S.pattern("di-gr-p1", "Year-on-year growth rate", "very common",
      "'The percentage growth from year X to year Y' or 'in which year was growth highest'.",
      r"g = \frac{\text{new} - \text{old}}{\text{old}} \times 100",
      r"""1. Base = the earlier year.
2. Change ÷ base × 100.
3. For 'highest growth year', compute each rate — don't compare raw jumps.

Why: growth is relative to where the year started.""",
      rev_table() + "\n\nThe percentage growth in revenue from 2020 to 2021 is:",
      r"$\frac{96 - 80}{80} \times 100 = 20\%$.")

    S.pattern("di-gr-p2", "Net change over successive years", "very common",
      "'The overall increase from 2020 to 2023', or mixed rise/fall statements.",
      r"\text{factor} = \prod \left(1 \pm \frac{a_i}{100}\right)",
      r"""1. Convert each year's change to a factor.
2. Multiply the factors.
3. Net % = (factor − 1) × 100.

Why: each change acts on the already-changed value.""",
      "A price rises 10% and then another 10%. The net increase is:",
      r"$1.1 \times 1.1 = 1.21$ → net $+21\%$ (not 20%).")

    S.pattern("di-gr-p3", "Reverse growth: find the earlier value", "common",
      "The final value after two or three changes is given; the original is asked.",
      r"\text{initial} = \frac{\text{final}}{\prod \left(1 \pm \frac{a_i}{100}\right)}",
      r"""1. Build the factor chain (fall = minus).
2. Divide the final value by the product.
3. Keep factors as fractions for clean division.

Why: forward multiplies, backward divides.""",
      "After two successive raises of 20% and 25%, a salary is ₹45,000. The original salary was:",
      r"$\frac{45000}{1.2 \times 1.25} = \frac{45000}{1.5} = ₹30{,}000$.")

    S.pattern("di-gr-p4", "Profit percent from income and expenditure", "common",
      "An income–expenditure table; a profit percent asked, or the best year.",
      r"\text{profit}\% = \frac{I - E}{E} \times 100",
      r"""1. Profit = income − expenditure.
2. Divide by expenditure (not income).
3. For the best year, compute every profit percent — amounts mislead.

Why: profit percent measures return on money spent.""",
      ie_table() + "\n\nThe profit percent in 2022 is:",
      r"$\frac{80 - 50}{50} \times 100 = 60\%$.")

    S.pattern("di-gr-p5", "Comparing growth of two firms / periods", "common",
      "Two firms (or two spans) with start and end values; which grew faster, or by how many points.",
      r"\text{gap in points} = g_1 - g_2",
      r"""1. Compute each overall growth percent separately.
2. Compare; the gap is in percentage points.
3. Bigger absolute rise ≠ bigger percent growth.

Why: percent growth normalises for the base size.""",
      "Firm A: 80 → 144. Firm B: 50 → 100 (same span). Which grew faster in percent, and by how much?",
      r"A: 80%. B: 100%. B, by 20 percentage points.")

    T = rev_table()
    # q1
    v = F(REV[2021] - REV[2020], REV[2020]) * 100
    assert v == 20
    S.q("di-gr-p1", "easy", T + "\n\nThe percentage growth in revenue from 2020 to 2021 is:",
        ["20%", "16%", "25%", "12.5%"], pct(v),
        r"$\frac{96 - 80}{80} \times 100 = \frac{16}{80} \times 100 = 20\%$.",
        r"16% forgets to divide by the base; 25% divides by 96.", 30)
    # q2
    v = F(REV[2022] - REV[2021], REV[2021]) * 100
    assert v == 25
    S.q("di-gr-p1", "medium", T + "\n\nThe percentage growth in revenue from 2021 to 2022 is:",
        ["25%", "20%", "24%", "30%"], pct(v),
        r"$\frac{120 - 96}{96} \times 100 = \frac{24}{96} \times 100 = 25\%$.",
        r"$\frac{24}{96} = \frac{1}{4}$.", 35)
    # q3
    g = {y: F(REV[y] - REV[y - 1], REV[y - 1]) * 100 for y in (2021, 2022, 2023)}
    assert g == {2021: 20, 2022: 25, 2023: 20} and max(g, key=g.get) == 2022
    S.q("di-gr-p1", "medium", T + "\n\nIn which year was the percentage rise in revenue over the previous year the highest?",
        ["2022", "2021", "2023", "Equal in all"], str(max(g, key=g.get)),
        r"2021: $\frac{16}{80} = 20\%$; 2022: $\frac{24}{96} = 25\%$; 2023: $\frac{24}{120} = 20\%$ → **2022**.",
        r"The 24-crore jump happens twice but on different bases.", 45)
    # q4
    v = F(REV[2023], REV[2020])
    assert v == F(9, 5)
    S.q("di-gr-p2", "medium", T + "\n\nThe overall percentage increase in revenue from 2020 to 2023 is:",
        ["80%", "60%", "90%", "75%"], "80%",
        r"Factor $= \frac{144}{80} = \frac{9}{5} = 1.8$ → $+80\%$.",
        r"Adding 20 + 25 + 20 gives 65% — never add.", 45)
    # q5
    assert F(11, 10) ** 2 == F(121, 100)
    S.q("di-gr-p2", "easy", "The price of a commodity rises by 10% in one month and by another 10% in the next month. The net increase in price is:",
        ["21%", "20%", "121%", "19%"], "21%",
        r"$1.1 \times 1.1 = 1.21$ → net $+21\%$.",
        r"121% is the final value factor read as a percent.", 25)
    # q6
    assert F(125, 100) * F(80, 100) == 1
    S.q("di-gr-p2", "hard", "The output of a factory increases by 25% in the first year and decreases by 20% in the next year. The net change in output is:",
        ["No change", "5% increase", "5% decrease", "2.5% increase"], "No change",
        r"$1.25 \times 0.80 = 1.00$ → the output returns to its starting value.",
        r"$x + 25\%$ of it, minus 20% of the new value: $\frac{5}{4}x \times \frac{4}{5} = x$.", 40)
    # q7
    v = F(45000, F(6, 5) * F(5, 4))
    assert v == 30000
    S.q("di-gr-p3", "medium", "After two successive salary raises of 20% and 25%, a person's salary became ₹45,000. The salary before the raises was:",
        [rs(30000), rs(31500), rs(28800), rs(32500)], rs(v),
        r"Factor $= 1.2 \times 1.25 = 1.5$. Original $= \frac{45000}{1.5} = ₹30{,}000$.",
        r"Check: $30000 \to 36000 \to 45000$.", 40)
    # q8
    v = F(14400, F(4, 5) * F(9, 10))
    assert v == 20000
    S.q("di-gr-p3", "hard", "After two successive decreases of 20% and 10% in two years, the population of a town is 14,400. The population two years ago was:",
        ["20,000", "18,000", "19,200", "21,600"], ind(v),
        r"Factor $= 0.8 \times 0.9 = 0.72 = \frac{18}{25}$. Original $= 14400 \times \frac{25}{18} = 20{,}000$.",
        r"Check: $20000 \to 16000 \to 14400$.", 50)
    # q9
    i22, e22 = IE[2022]
    v = F(i22 - e22, e22) * 100
    assert v == 60
    S.q("di-gr-p4", "easy", ie_table() + "\n\nThe profit percent in 2022 is:",
        ["60%", "37.5%", "66.67%", "50%"], pct(v),
        r"$\frac{80 - 50}{50} \times 100 = 60\%$.",
        r"37.5% divides by income (80) — the standard trap.", 35)
    # q10
    pp = {y: F(i - e, e) * 100 for y, (i, e) in IE.items()}
    assert pp == {2021: F(50), 2022: F(60), 2023: F(40 * 100, 90)}
    assert max(pp, key=pp.get) == 2022
    assert max(IE, key=lambda y: IE[y][0] - IE[y][1]) == 2023  # absolute-profit trap
    S.q("di-gr-p4", "hard", ie_table() + "\n\nIn which year was the profit percentage the highest?",
        ["2022", "2023", "2021", "Same in all"], "2022",
        r"2021: $\frac{20}{40} = 50\%$; 2022: $\frac{30}{50} = 60\%$; 2023: $\frac{40}{90} \approx 44.4\%$ → **2022**.",
        r"2023 has the biggest profit amount (₹40 lakh) but a smaller percent — the base is bigger.", 60)
    # q11
    ga = F(REV[2023] - REV[2020], REV[2020]) * 100
    gb = F(B_REV[2023] - B_REV[2020], B_REV[2020]) * 100
    assert (ga, gb) == (80, 100) and gb > ga
    assert REV[2023] - REV[2020] > B_REV[2023] - B_REV[2020]  # absolute trap
    bt = md_table(["Firm", "Revenue 2020 (₹ cr)", "Revenue 2023 (₹ cr)"],
                  [["A", 80, 144], ["B", 50, 100]])
    S.q("di-gr-p5", "medium", "Revenues of two firms (in ₹ crore):\n\n" + bt + "\n\nWhich firm recorded the higher percentage growth over 2020–2023?",
        ["B", "A", "Both equal", "Cannot be determined"], "B",
        r"A: $\frac{64}{80} = 80\%$. B: $\frac{50}{50} = 100\%$. **B** grew faster.",
        r"A's absolute rise (64) is bigger, but B doubled its revenue.", 40)
    # q12
    assert gb - ga == 20
    S.q("di-gr-p5", "hard", "Revenues of two firms (in ₹ crore):\n\n" + bt + "\n\nBy how many percentage points does the growth of B exceed that of A?",
        ["20", "10", "25", "16"], str(gb - ga),
        r"B grows 100%, A grows 80%: gap $= 100 - 80 = 20$ percentage points.",
        r"'B grows 20% more than A' would need $\frac{20}{80} = 25\%$ — different question.", 50)
    return S
