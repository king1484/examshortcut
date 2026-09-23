import sympy as sp
from qa_common import Q, F, T, S, P, U, write_topic

# ---------------------------------------------------------------- sanity checks
# solved ds01: average production
assert sp.Rational(400 + 450 + 500 + 550, 4) == sp.Rational(475, 1)
# ds02: % increase 450 -> 500
assert sp.Rational(50, 450) * 100 == sp.Rational(100, 9)  # 11 1/9 %
# ds03: pie degrees to count
assert sp.Rational(144, 360) * 720 == 288
assert sp.Rational(90, 360) * 720 == 180
# ds04: pass ratios
assert sp.Rational(55, 60) > sp.Rational(63, 70) > sp.Rational(40, 50) > sp.Rational(45, 60)
assert sp.Rational(55, 60) == sp.Rational(11, 12)
# ds05: +20% then -10% => +8%
assert sp.Rational(12, 10) * sp.Rational(9, 10) == sp.Rational(108, 100)
# practice
assert 250 + 300 + 400 + 350 == 1300
assert sp.Rational(50, 200) * 100 == 25                      # 200 -> 250
assert sp.Rational(36, 360) * 7200 == 720                    # 36 deg sector
assert sp.Rational(320 + 280 + 360 + 300 + 340, 5) == 320    # row average
assert (60 + 70 + 80) - (50 + 60 + 90) == 10                 # column totals diff
assert sp.Rational(40, 100) * 4800 == 1920                   # 15% + 25%
assert sp.Rational(60, 480) * 100 == sp.Rational(25, 2)      # 480 -> 420: 12.5%
assert sp.Rational(450, 550) == sp.Rational(9, 11)           # ratio men:women
assert sp.Rational(630, 540) == sp.Rational(7, 6)            # 116 2/3 %
assert sp.Rational(60, 300) * 100 == 20 and sp.Rational(36, 360) * 100 == 10  # 20% vs 10%
assert 22 * sp.Rational(36, 10) == sp.Rational(396, 5)       # 79.2 deg
assert sp.Rational(25 + 30 + 20 + 35 + 40, 5) == 30          # per-day average
assert sp.Rational(33000, sp.Rational(11, 10) * sp.Rational(12, 10) * sp.Rational(5, 4)) == 20000
assert sp.Rational(660 - 550, 550) * 100 == 20               # profit %
assert sp.Rational(300 * 65 + 200 * 75, 500) == 69           # combined average

# ---------------------------------------------------------------- subtopics
subtopics = [
S("di-table", "Reading tables: totals, differences, ratios",
r"""
DI starts with **reading discipline**: note what rows and columns are (units! years!), and only then look at
the question. Most Tier-1 table questions ask for a total, a difference of two cells, or a simple ratio —
the data hunting *is* the question.

Work cell-by-cell with running subtotals rather than reading values one by one for every sub-question.
""",
[
F("Total of a row/column", r"\text{total}=x_1+x_2+\cdots+x_k"),
F("Difference", r"\text{difference}=|A-B|"),
F("Ratio of cells", r"\text{ratio}=\frac{x_{ij}}{x_{kl}}\ \text{(simplify the fraction)}"),
],
[
T("Simplify the fraction before choosing",
r"""Ratios like $450:550$ reduce to $9:11$ — reduce before matching options, the unreduced pair is a common
distractor.""",
r"The table gives male and female employees (450 and 550). Find the ratio of males to females.",
r"$\frac{450}{550}=\frac{9}{11}$, i.e. $9:11$."),
T("Sums of friendly numbers",
r"""Group digits that make round numbers (e.g. $60+70+80$). DI tables are built so subtotals land on
round values.""",
r"Unit A produces 60, 70, 80 units in three years; Unit B produces 50, 60, 90. Whose total is larger and by how much?",
r"$A=210$, $B=200$; A leads by 10."),
],
[
"Mismatching units across columns (thousands vs units, lakh tonnes vs tonnes).",
"Adding percentages or ratios from different bases as if they were plain numbers.",
"Reading the wrong year's column after the question switches reference year.",
]),
S("di-percent", "Percentage change and comparisons",
r"""
$$\%\ \text{change}=\frac{\text{new}-\text{old}}{\text{old}}\times100$$

- The base is always the **earlier/older** value ("increase over 2020" divides by 2020).
- "X is what percent of Y" $\Rightarrow \frac{X}{Y}\times100$.
- Comparing two percentage changes: subtract them for percentage **points**, take a ratio for a relative
  comparison — the question says which it wants.
""",
[
F("Percentage change", r"\Delta\%=\frac{\text{new}-\text{old}}{\text{old}}\times100"),
F("Share of total", r"\text{share}=\frac{\text{part}}{\text{whole}}\times100\%"),
F("Percentage points", r"\text{pp difference}=\Delta\%_1-\Delta\%_2"),
],
[
T("Divide by the old value, always",
r"""Half of all DI percentage errors come from dividing by the new value. Anchor: "increase OVER X" uses X
as the denominator.""",
r"Sales fall from 480 units to 420 units. Find the percentage decrease.",
r"$\frac{480-420}{480}\times100=12.5\%$ — denominator is the starting 480."),
T("Compare percentages as fractions of friendly numbers",
r"""Convert $\frac{\text{change}}{\text{base}}$ to a fraction over a round base: $\frac{60}{300}=\frac15=20\%$
beats decimal division.""",
r"Output: 2021: 300, 2022: 360, 2023: 396. Which jump had the larger percentage increase?",
r"2021→22: $\frac{60}{300}=20\%$; 2022→23: $\frac{36}{360}=10\%$. The first, by 10 percentage points."),
],
[
"Dividing by the new value instead of the base.",
"Percentage points confused with percent (20% vs 10% is '10 points more', not 'twice as much' relative growth).",
"Ignoring 'approximately' and chasing exact decimals when the options are close but distinct.",
]),
S("di-pie", "Pie charts: degrees, shares and totals",
r"""
A pie's whole circle $=360^\circ=$ the stated total. Conversion chain:

$$\text{value}=\frac{\text{angle}}{360^\circ}\times\text{total},\qquad
\text{angle}=\text{share}\times360^\circ,\qquad 1\% = 3.6^\circ$$

CGL papers usually *print* the pie as a table of sector angles or percentages — read it exactly like a table.
""",
[
F("Angle to value", r"\text{value}=\frac{\theta}{360^\circ}\times\text{total}"),
F("Percent to angle", r"\theta=\text{share}\times3.6^\circ\ \text{per percent}"),
F("Share from angle", r"\text{share}=\frac{\theta}{3.6^\circ}\%"),
],
[
T("Memorise 3.6° per percent",
r"""Percent ↔ degree is one multiplication: 22% spans $79.2^\circ$; $36^\circ$ is 10% of the total. Most pie
questions are one such step plus a multiply.""",
r"A sector subtends $36^\circ$ in a pie chart of a budget of ₹7,200. What does the sector represent?",
r"$\frac{36}{360}=\frac{1}{10}$ of 7200 = ₹720."),
T("Two-sector combos first",
r"""When asked about two sectors together, add angles (or percentages) **before** converting to values — one
multiplication instead of two.""",
r"Two departments take 15% and 25% of a workforce of 4,800. How many together?",
r"$40\%$ of $4800=1920$."),
],
[
"Treating the printed angle as the value (or the value as a percentage).",
"Using 360° with a total that is itself a percentage share.",
"Degrees arithmetic off by the 3.6 factor ($1\\%\\neq1^\\circ$).",
]),
S("di-average", "Averages from data",
r"""
Two recurring asks:

- **Row/column average**: sum the cells, divide by the count — with clean DI numbers this is usually an
  integer.
- **Combined/weighted average** across two groups printed in the table (students × average marks, workers ×
  output):
  $$\bar{x}=\frac{n_1\bar{x}_1+n_2\bar{x}_2}{n_1+n_2}$$

For per-day/per-unit rates, the total over the period divided by the number of periods is the whole question.
""",
[
F("Average of cells", r"\bar{x}=\frac{\text{sum of cells}}{\text{number of cells}}"),
F("Weighted average", r"\bar{x}=\frac{n_1\bar{x}_1+n_2\bar{x}_2}{n_1+n_2}"),
F("Per-period value", r"\text{per period}=\frac{\text{total}}{\text{number of periods}}"),
],
[
T("Scan for the shortcut row",
r"""DI tables often hide symmetry: values around a central number (320, 280, 360, 300, 340 all deviate by
±20/40 around 320). Spotting the centre makes the average mental arithmetic.""",
r"A unit produces 320, 280, 360, 300 and 340 units over five days. Find the average daily production.",
r"Deviations $0,-40,+40,-20,+20$ cancel: average $=320$ units."),
T("Weight by the group sizes, not the marks",
r"""In combined-average tables the *count* is the weight. Multiply across each row, add, divide by total
count.""",
r"School A: 300 students averaging 65; School B: 200 students averaging 75. Find the combined average.",
r"$\frac{300\times65+200\times75}{500}=\frac{34500}{500}=69$."),
],
[
"Averaging group averages without weights (65 and 75 average to 70, not 69).",
"Dividing by the wrong count (summing 5 days but dividing by 7).",
"Mixing up which is the count column and which is the value column.",
]),
S("di-growth", "Growth rates and successive changes",
r"""
- **Growth rate**: $\frac{\text{new}-\text{old}}{\text{old}}\times100$ — same as percentage change.
- **Successive changes multiply**: $+a\%$ then $+b\%$ gives the factor $\left(1+\frac{a}{100}\right)\left(1+\frac{b}{100}\right)$.
  A $+20\%$ then $-10\%$ run nets $1.2\times0.9=1.08$, i.e. $+8\%$.
- **Running backwards**: earlier value $=\dfrac{\text{final value}}{\text{growth factor}}$ — divide, don't subtract.
""",
[
F("Growth rate", r"g=\frac{\text{new}-\text{old}}{\text{old}}\times100"),
F("Successive change", r"\text{factor}=\left(1+\frac{a}{100}\right)\left(1+\frac{b}{100}\right)"),
F("Reverse growth", r"\text{initial}=\frac{\text{final}}{\text{factor}}"),
F("Profit percent from table", r"\text{profit}\%=\frac{\text{income}-\text{expenditure}}{\text{expenditure}}\times100"),
],
[
T("Multiply factors, never add percentages",
r"""Convert each change to a factor ($+20\%\to1.2$), multiply, convert back. $+20\%+(-10\%)=+10\%$ is the
classic wrong shortcut — the true net is $+8\%$.""",
r"A price rises 20% and then falls 10%. What is the net change?",
r"$1.2\times0.9=1.08$ → net $+8\%$."),
T("Reverse-growth: divide by the factor",
r"""When the final value is given and the initial is asked, write the factor chain and divide once. Keep
factors as fractions ($1.65=\frac{33}{20}$) for clean division.""",
r"A town's population grew 10%, then 20%, then 25% over three years to reach 33,000. Find the initial population.",
r"Factor $=1.1\times1.2\times1.25=1.65$; initial $=\frac{33000}{1.65}=20{,}000$."),
],
[
"Adding successive percentages instead of multiplying factors.",
"Reversing growth by subtracting percentages (a 25% rise then 25% fall is not flat — it is $-6.25\\%$).",
"Profit percent computed on income instead of expenditure.",
]),
]

patterns = [
P("Totals and differences from a table", "very common",
  r"Sum a row/column, or find the gap between two cells or two years.",
  r"Add friendly groups; keep subtotals; answer usually a round number — check against it."),
P("Percentage change between periods", "very common",
  r"'The percent increase from year A to year B', often with 'approximately' in the question.",
  r"$\frac{\text{new}-\text{old}}{\text{old}}\times100$; base is the earlier value; match the nearest option."),
P("Pie-chart sector values", "very common",
  r"Sectors printed as degrees or percentages with a stated total; a value, share or angle asked.",
  r"$\frac{\theta}{360}\times$total, or share$\times3.6^\circ$ for angles; combine sectors before converting."),
P("Ratios and shares", "common",
  r"'Ratio of X to Y in year Z' or 'X is what percent of Y'.",
  r"Reduce the fraction directly; convert to percent only at the end."),
P("Averages and weighted averages", "common",
  r"Row/column averages, or two groups with counts and averages to combine.",
  r"Simple mean of cells, or $\frac{n_1\bar x_1+n_2\bar x_2}{n_1+n_2}$ weighted by counts."),
P("Successive growth / reverse growth", "common",
  r"Multi-year growth rates with the final (or initial) value given.",
  r"Multiply factors to move forward, divide by the factor to move back; never add percentages."),
]

# ---------------------------------------------------------------- solved examples
solved = []

solved.append(Q("di-s01",
r"""Production of a factory (in thousand units):

| Year | 2019 | 2020 | 2021 | 2022 |
|---|---|---|---|---|
| Production | 400 | 450 | 500 | 550 |

Find the average production over the four years (in thousand units).""",
U("", 475, 470, 480, 465), 475,
r"Total $=400+450+500+550=1900$; average $=\frac{1900}{4}=475$ thousand units.",
r"Deviations around 475 are $-75,-25,+25,+75$ — they cancel, so the average is 475 without summing.",
"easy", "di-average", "row average", 35))

solved.append(Q("di-s02",
r"""Using the same data,

| Year | 2019 | 2020 | 2021 | 2022 |
|---|---|---|---|---|
| Production | 400 | 450 | 500 | 550 |

the percentage increase in production from 2020 to 2021 was approximately:""",
[(r"$11\tfrac{1}{9}\%$", "11 1/9%"), ("10%", "10%"), (r"$12\tfrac{1}{2}\%$", "12.5%"), ("12%", "12%")], "11 1/9%",
r"$\frac{500-450}{450}\times100=\frac{50}{450}\times100=\frac{100}{9}=11\tfrac19\%$.",
r"$\frac{50}{450}=\frac19\to11\tfrac19\%$. Base is 2020 (the earlier year).",
"medium", "di-percent", "percent increase", 40))

solved.append(Q("di-s03",
r"""Employees of a company by department (pie-chart sectors given as angles):

| Department | Engineering | Sales | HR | Admin | Support |
|---|---|---|---|---|---|
| Angle | 144° | 90° | 36° | 54° | 36° |

If the company has 720 employees, how many work in Engineering?""",
U("", 288, 216, 180, 252), 288,
r"$\frac{144}{360}\times720=\frac{2}{5}\times720=288$.",
r"$\frac{144}{360}=\frac25$ of 720 = 288. (Check: Sales $\frac{90}{360}\times720=180$.)",
"easy", "di-pie", "pie angle to value", 40))

solved.append(Q("di-s04",
r"""Students who appeared ($A$) and passed ($P$) in a board exam:

| | City A (App) | City A (Pass) | City B (App) | City B (Pass) |
|---|---|---|---|---|
| 2020 | 50 | 40 | 60 | 55 |
| 2021 | 60 | 45 | 70 | 63 |

(In hundreds.) Which city-year pair had the highest pass percentage?""",
[("City B, 2020", sp.Rational(55, 60)), ("City B, 2021", sp.Rational(63, 70)), ("City A, 2021", sp.Rational(45, 60)), ("City A, 2020", sp.Rational(40, 50))], sp.Rational(55, 60),
r"""
Pass percentages: A-2020 $\frac45=80\%$, B-2020 $\frac{55}{60}=91\tfrac23\%$, A-2021 $75\%$, B-2021 $90\%$.

Highest: City B in 2020.
""",
r"Compare fractions: $\frac{55}{60}=\frac{11}{12}\approx91.7\%$ beats $\frac{9}{10}$ and the two $\frac45$s. Cross-multiply to compare — don't decimalise.",
"medium", "di-table", "max ratio cell", 55))

solved.append(Q("di-s05",
r"The price of a commodity rose by 20% in the first year and fell by 10% in the next year. The net change over the two years is:",
U("", "8% increase", "10% increase", "8% decrease", "10% decrease"), "8% increase",
r"Factor $=1.20\times0.90=1.08$ — a net increase of 8%.",
r"Multiply the factors $1.2\times0.9=1.08$: net $+8\%$. (Adding $+20-10=+10\%$ is the classic trap.)",
"medium", "di-growth", "successive change", 40))

# ---------------------------------------------------------------- practice
pr = []

pr.append(Q("di-q01",
r"""Sales (in ₹ hundreds) of four shops in a month:

| Shop | A | B | C | D |
|---|---|---|---|---|
| Sales | 250 | 300 | 400 | 350 |

The total sales of all four shops (in ₹) is:""",
U("", 130000, 125000, 135000, 120000), 130000,
r"Total $=250+300+400+350=1300$ hundreds $=$ ₹1,30,000.",
r"Sum 1300, remember the ×100 unit: ₹1,30,000. Trap: 1300 (forgot the unit).",
"easy", "di-table", "column total", 35))

pr.append(Q("di-q02",
r"""Output of a unit (in tonnes):

| Year | 2020 | 2021 |
|---|---|---|
| Output | 200 | 250 |

The percentage increase in output from 2020 to 2021 is:""",
U("", "25%", "20%", r"$22\tfrac12\%$", "30%"), "25%",
r"$\frac{250-200}{200}\times100=25\%$.",
r"$\frac{50}{200}=\frac14\to25\%$. Trap: 20% (divided by 250).",
"easy", "di-percent", "percent increase", 30))

pr.append(Q("di-q03",
r"""In a pie chart of a yearly budget of ₹7,200 (in hundreds), one sector subtends an angle of 36° at the centre. The amount represented by this sector (in ₹) is:""",
U("", 72000, 36000, 720000, 216000), 72000,
r"$\frac{36}{360}\times7200=720$ hundreds $=$ ₹72,000.",
r"36° is $\frac{1}{10}$ of the circle: one tenth of 7200 hundreds = ₹72,000.",
"easy", "di-pie", "pie sector value", 35))

pr.append(Q("di-q04",
r"""Daily production of a factory (in units): 320, 280, 360, 300, 340 over five days. The average daily production (in units) is:""",
U("", 320, 315, 325, 310), 320,
r"Total $=1600$; average $=\frac{1600}{5}=320$ units.",
r"Deviations $0,-40,+40,-20,+20$ cancel around 320 — the average is the centre value itself.",
"easy", "di-average", "row average", 30))

pr.append(Q("di-q05",
r"""Production (in units) of two units of a plant:

| Year | Unit A | Unit B |
|---|---|---|
| 2020 | 60 | 50 |
| 2021 | 70 | 60 |
| 2022 | 80 | 90 |

Over the three years, the total production of Unit A exceeds that of Unit B by:""",
U("", "10 units", "20 units", "5 units", "15 units"), "10 units",
r"$A=60+70+80=210$; $B=50+60+90=200$; difference $=10$ units.",
r"Tally each column: 210 vs 200 → 10. ($60+70+80$: pair 60+80=140 first.)",
"easy", "di-table", "column totals difference", 40))

pr.append(Q("di-q06",
r"""In a workforce of 4,800, the pie chart shows two departments occupying 15% and 25% of the circle. The number of employees in these two departments together is:""",
U("", 1920, 1680, 2400, 1440), 1920,
r"Together $15\%+25\%=40\%$; $0.40\times4800=1920$.",
r"Add the shares first: 40% of 4800 = 1920. One multiplication, not two.",
"medium", "di-pie", "pie combined sectors", 35))

pr.append(Q("di-q07",
r"The readership of a magazine fell from 4.8 lakh to 4.2 lakh. The percentage decrease is:",
U("", "12.5%", "12%", "10%", "15%"), "12.5%",
r"$\frac{4.8-4.2}{4.8}\times100=\frac{0.6}{4.8}\times100=12.5\%$.",
r"$\frac{0.6}{4.8}=\frac18\to12.5\%$. Base is the original 4.8 lakh.",
"medium", "di-percent", "percent decrease", 35))

pr.append(Q("di-q08",
r"""In a college in 2022 there were 450 male and 550 female students. The ratio of male to female students is:""",
[("9 : 11", sp.Rational(9, 11)), ("11 : 9", sp.Rational(11, 9)), ("4 : 5", sp.Rational(4, 5)), ("5 : 6", sp.Rational(5, 6))], sp.Rational(9, 11),
r"$\frac{450}{550}=\frac{9}{11}$, i.e. $9:11$.",
r"Divide both by 50: 9 : 11. Trap: 11 : 9 (reversed order — the question asks male : female).",
"medium", "di-table", "ratio of cells", 30))

pr.append(Q("di-q09",
r"""Monthly incomes (in ₹): Aman 54,000; Bina 63,000. Bina's income is what percent of Aman's income?""",
[(r"$116\tfrac{2}{3}\%$", sp.Rational(350, 3)), (r"$86\tfrac{2}{3}\%$", sp.Rational(260, 3)), ("120%", "120%"), (r"$116\tfrac{1}{4}\%$", sp.Rational(465, 4))], sp.Rational(350, 3),
r"$\frac{63000}{54000}\times100=\frac{7}{6}\times100=116\tfrac23\%$.",
r"$\frac{63}{54}=\frac76\to116\tfrac23\%$. Trap: $86\tfrac23\%$ is Aman as a percent of Bina (the inverse).",
"medium", "di-percent", "share as percent", 35))

pr.append(Q("di-q10",
r"""Production (in tonnes): 2021: 300, 2022: 360, 2023: 396. The percentage increase in 2021-22 exceeds that in 2022-23 by:""",
U("", "10 percentage points", "20 percentage points", "30 percentage points", "5 percentage points"), "10 percentage points",
r"""2021-22: $\frac{60}{300}\times100=20\%$. 2022-23: $\frac{36}{360}\times100=10\%$.

Difference $=20-10=10$ percentage points.""",
r"$\frac{60}{300}=20\%$, $\frac{36}{360}=10\%$ → 10 points. (Bases differ: 300 then 360.)",
"medium", "di-percent", "compare percent changes", 45))

pr.append(Q("di-q11",
r"""In a pie chart of family expenditure, rent takes 22% of the total. The central angle of the rent sector is:""",
[(r"$79.2^\circ$", sp.Rational(396, 5)), (r"$72^\circ$", 72), (r"$80.5^\circ$", sp.Rational(161, 2)), (r"$88^\circ$", 88)], sp.Rational(396, 5),
r"$22\times3.6^\circ=79.2^\circ$.",
r"Percent to angle: multiply by 3.6. $22\times3.6=79.2^\circ$. Trap: $72^\circ$ (used 3° per percent... or mixed up with 20%).",
"medium", "di-pie", "percent to angle", 30))

pr.append(Q("di-q12",
r"""Units assembled by a worker over a week (5 working days): 25, 30, 20, 35, 40. The average daily output is:""",
U("", 30, 28, 32, 26), 30,
r"Total $=25+30+20+35+40=150$; average $=\frac{150}{5}=30$ units.",
r"Pair to round numbers: $25+35=60$, $30+20=50$, $+40$ → 150 over 5 days → 30.",
"medium", "di-average", "per-day average", 30))

pr.append(Q("di-q13",
r"""The population of a town grew by 10%, 20% and 25% in three successive years and stood at 33,000 at the end. The population at the beginning was:""",
U("", 20000, 22000, 24000, 19800), 20000,
r"""
Factor $=1.1\times1.2\times1.25=1.65$.

Initial $=\frac{33000}{1.65}=20{,}000$.
""",
r"Divide by the product of factors $1.65$: $33000/1.65=20000$. ($1.65=\frac{33}{20}$ makes the division clean.)",
"hard", "di-growth", "reverse successive growth", 60))

pr.append(Q("di-q14",
r"""For a firm in 2022, income was ₹6.6 crore and expenditure ₹5.5 crore. The profit percentage is:""",
U("", "20%", "18%", "22%", "25%"), "20%",
r"$\frac{6.6-5.5}{5.5}\times100=\frac{1.1}{5.5}\times100=20\%$.",
r"$\frac{1.1}{5.5}=\frac15\to20\%$. Profit percent is always on **expenditure**.",
"hard", "di-growth", "profit percent", 45))

pr.append(Q("di-q15",
r"""Two schools:

| School | Students | Average marks |
|---|---|---|
| A | 300 | 65 |
| B | 200 | 75 |

The average marks of all 500 students of the two schools together is:""",
U("", 69, 70, 68, 71), 69,
r"$\frac{300\times65+200\times75}{500}=\frac{19500+15000}{500}=\frac{34500}{500}=69$.",
r"Weighted by students, not the plain 70: $\frac{34500}{500}=69$. Trap: 70 (equal-weight average).",
"hard", "di-average", "weighted average", 50))

topic = {
    "id": "data-interpretation",
    "sectionId": "quant",
    "title": "Data Interpretation",
    "order": 19,
    "importance": "medium",
    "avgQuestions": {"tier1": 2, "tier2": 5},
    "summary": "Reading tables and charts: totals, percentage change, pie-chart angles and shares, row averages, weighted averages and successive growth. "
               "DI rewards calm reading more than calculation — every question is one fraction or one product away, and the data is given in clean, round numbers by design. Tier 2 sets often attach a 5-question block to one table, so per-table setup pays twice.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
