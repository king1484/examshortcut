"""Readable rewrite of Interest SI & CI (all five subtopics).

Simple English, one idea per section. Every number in every example is
recomputed below with exact fractions and asserted.
Run: python interest.py  (patches content/core/topics/quant/interest.json)
"""
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "interest.json"

# ---------- answer checks: int-si ----------
assert 5000 * 8 * 3 == 120000 and F(120000, 100) == 1200
assert 6500 * 8 * 3 == 156000 and F(156000, 100) == 1560 and 6500 + 1560 == 8060
assert 2000 - 1250 == 750 and F(750 * 100, 1250 * 12) == 5 and F(5 * 1250 * 12, 100) == 750
assert 1540 * F(10, 11) == 1400 and F(5 * 2, 100) == F(1, 10)
assert F(100 * 2, 16) == F(25, 2) and F(100 * 1, 8) == F(25, 2)
assert F(100 * 4, 12) == F(100, 3) == 33 + F(1, 3)
assert F(100, 5 * 4) == 5 and F(200, 9 * 8) == F(25, 9) == 2 + F(7, 9)
assert F(100 * 2, 5 * 4) == 10
assert 12000 * 8 * 3 == 288000 and F(288000, 100) == 2880
assert 10000 * F(15, 2) * 3 == 225000 and F(225000, 100) == 2250 and 2880 - 2250 == 630
assert 8 * 7800 == 62400 and 12 * 5200 == 62400 and 7800 + 5200 == 13000


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ================= int-si =================

SI_CONCEPT = (
    "Simple interest charges the same slice of the **original principal** every year. Old interest never earns more.\n\n"
    "Use $SI = \\dfrac{P \\times R \\times T}{100}$ and $A = P + SI$. If a sum becomes $n$ times in $T$ years, "
    "the interest part is only $(n-1)P$, so $R = \\dfrac{100(n-1)}{T}$."
)

SI_NOTES = r"""### The four words
- **Principal (P)**: the money lent, borrowed or invested.
- **Rate (R)**: the yearly charge, written as a per cent per annum.
- **Time (T)**: the period, always counted in years.
- **Interest (SI)**: the charge for the whole period.

Borrow Rs 100 for a year at 8% and you pay Rs 8 extra. Keep it three years and you pay Rs 24 — the same Rs 8 three times over.

> **Rule:** At simple interest, every year costs the same fixed slice of the original principal. Interest already paid never earns interest.

### The formula and its four faces
$$SI = \frac{P \times R \times T}{100}$$

Cover the one you want and the formula solves itself: $P = \dfrac{100 \times SI}{RT}$, $R = \dfrac{100 \times SI}{PT}$, $T = \dfrac{100 \times SI}{PR}$.

SI on Rs 6,500 at 8% for 3 years: $\dfrac{6500 \times 8 \times 3}{100} = 1560$.

> **Tip:** Keep T in years. Nine months is $\dfrac{9}{12} = \dfrac{3}{4}$ of a year, never 9.

### Amount questions
**Amount (A)** is the total handback: $A = P + SI$. When a question says "amounts to", strip the principal first: $SI = A - P$.

A sum amounts to Rs 1,540 in 2 years at 5%. Then $SI = 1540 - P$ and also $SI = \dfrac{P \times 5 \times 2}{100} = \dfrac{P}{10}$. So $1.1P = 1540$ and $P = 1400$.

### Growth is a straight line
The amount climbs by the same rupees every year, so the yearly amounts sit on a straight line. That single fact gives the n-times rule:

$$R = \frac{100(n-1)}{T}$$

"Becomes 3 times in 16 years" means interest $= 2P$ over 16 years: $R = \dfrac{200}{16} = 12.5\%$.

Check the same sum doubles in 8 years: $\dfrac{100}{8} = 12.5\%$. Same line, same slope. And "5 times at 12%" needs $T = \dfrac{400}{12} = 33\dfrac{1}{3}$ years.

> **Watch:** "Amounts to n times" includes the principal. Only $(n-1)P$ is interest. Using n instead of n−1 picks the trap option.

### Interest as a fraction of the sum
"The SI is $\dfrac{1}{5}$ of the sum at 4%." Write $\dfrac{P \times 4 \times T}{100} = \dfrac{P}{5}$ and cancel P: $T = \dfrac{100}{5 \times 4} = 5$ years.

The principal never enters the answer. Same shape: SI $= \dfrac{2}{9}$ of P at 8% gives $T = \dfrac{200}{9 \times 8} = 2\dfrac{7}{9}$ years.

### Comparing two situations
SI is proportional to each of P, R and T. Double the sum and the interest doubles; double the time and it doubles too. "Double P, half R" leaves SI unchanged.

For rupee answers, compute both and subtract: $\dfrac{12000 \times 8 \times 3}{100} - \dfrac{10000 \times 7.5 \times 3}{100} = 2880 - 2250 = 630$.

### One loan, two rates
A sum split into two parts at different rates is one linear equation. Split Rs 13,000 so both parts earn equal yearly interest, at 8% and 12%: $8a = 12(13000 - a)$, so $a = 7800$. Check: $8\%$ of 7,800 $= 624 = 12\%$ of 5,200.

> **Note:** Equal yearly interest means the smaller rate must hold the larger part.
"""

SI_FORMULAS = [
    {"name": "Simple interest", "tex": r"SI = \frac{PRT}{100}", "note": "Any one of the four recovers from the other three."},
    {"name": "Amount", "tex": r"A = P + SI = P\left(1 + \frac{RT}{100}\right)", "note": "'Amounts to' includes the principal."},
    {"name": "Recovering inputs", "tex": r"P = \frac{100\,SI}{RT},\quad R = \frac{100\,SI}{PT},\quad T = \frac{100\,SI}{PR}"},
    {"name": "n-times in T years", "tex": r"R = \frac{100(n-1)}{T}", "note": "Interest is only (n−1)P."},
    {"name": "Equal yearly interest", "tex": r"SI_{\text{per year}} = \frac{SI_{\text{total}}}{T}", "note": "Same rupees every year."},
]

SI_TRICKS = [
    {
        "title": "Cover the unknown",
        "body": "Write $SI = \\dfrac{PRT}{100}$ and cover the letter you want. That covered formula is the whole equation.",
        "example": {
            "q": "Find the simple interest on Rs 5,000 at 8% per annum for 3 years.",
            "steps": [r"$SI = \dfrac{5000 \times 8 \times 3}{100}$.", r"$= 1200$."],
            "answer": "Rs 1,200",
        },
    },
    {
        "title": "n-times to rate",
        "body": "'Becomes n times in T years' means the interest earned is $(n-1)P$. The P cancels.",
        "example": {
            "q": "At what rate per annum will a sum double itself in 10 years at simple interest?",
            "steps": [r"Interest $= (2-1)P = P$ in 10 years.", r"$R = \dfrac{100 \times 1}{10} = 10$."],
            "answer": "10% p.a.",
        },
    },
    {
        "title": "One year at a time",
        "body": "Divide the total interest by the years; every year carries exactly that much.",
        "example": {
            "q": "The simple interest on a sum at 4% per annum is two-fifths of the sum. Find the time.",
            "steps": [r"$\dfrac{P \times 4 \times T}{100} = \dfrac{2P}{5}$.", r"$T = \dfrac{100 \times 2}{5 \times 4} = 10$ years."],
            "answer": "10 years",
        },
    },
]

SI_MISTAKES = [
    {"wrong": "Plugging the amount A into the SI formula as the principal.",
     "right": "SI is always on the original P; from an amount take SI = A − P first."},
    {"wrong": "Using n instead of n − 1 in 'becomes n times'.",
     "right": "The interest part is only (n − 1)P, since n times includes the principal."},
    {"wrong": "Leaving months as months in T.",
     "right": "R is per annum, so T must be in years: 9 months = 3/4 year."},
    {"wrong": "Letting old interest earn interest.",
     "right": "At simple interest each year costs the same slice of the original principal only."},
    {"wrong": "Reporting the amount when the question asks for the interest.",
     "right": "A = P + SI; read which of the two the question wants."},
]

SI_REVISION = [
    "SI $=$ PRT/100; A $=$ P $+$ SI.",
    "Any one of P, R, T, SI from the other three.",
    "n times in T years: R $= \\dfrac{100(n-1)}{T}$.",
    "Growth is linear: equal rupees every year.",
    "SI as a fraction of P: T $=$ 100 $\\times$ fraction $\\div$ R.",
    "Months to years: divide by 12.",
    "Split loan, equal interest: rate $\\times$ part equal on both sides.",
]

SI_PATTERNS = [
    pat("int-s1", "Direct simple interest", "very common",
        "P, R and T are given and the SI, or the amount, is asked straight out.",
        r"SI = \frac{PRT}{100}, \qquad A = P + SI",
        ["Convert T to years (months divided by 12).", "Multiply P, R, T and divide by 100.",
         "For the amount, add P back."],
        "Each year charges the same fixed slice of the principal.",
        "Find the simple interest on Rs 6,500 at 8% per annum for 3 years.",
        [r"$SI = \dfrac{6500 \times 8 \times 3}{100} = 1560$.", r"Amount $= 6500 + 1560 = 8060$."],
        "Rs 1,560"),
    pat("int-s2", "Find P, R or T from the interest or amount", "very common",
        "Three of P, R, T, SI (or the amount) are given; the fourth is asked.",
        r"P = \frac{100 \times SI}{RT}, \quad R = \frac{100 \times SI}{PT}, \quad T = \frac{100 \times SI}{PR}",
        ["If an amount is given, first take SI = A − P.", "Rearrange the formula for the missing letter.",
         "Sanity check the size: doubling money in 12 years is under 10%."],
        "One formula links all four quantities, so any three fix the fourth.",
        "At what rate per annum will Rs 1,250 amount to Rs 2,000 in 12 years at simple interest?",
        [r"$SI = 2000 - 1250 = 750$.", r"$R = \dfrac{750 \times 100}{1250 \times 12} = 5$."],
        "5% per annum"),
    pat("int-s3", "n times in T years", "very common",
        "'A sum doubles, triples or becomes n times itself in T years — find the rate or the time.'",
        r"R = \frac{100(n-1)}{T}, \qquad T = \frac{100(n-1)}{R}",
        ["Interest earned is (n − 1)P — subtract the principal once.", "Rate: 100(n−1) over T. Time: 100(n−1) over R.",
         "Chains stay linear: doubling in T years means tripling in 2T."],
        "'Becomes n times' fixes the interest as a multiple of P, and P cancels out.",
        "A sum of money triples itself in 16 years at simple interest. The rate per annum is:",
        [r"Interest $= (3-1)P = 2P$ in 16 years.", r"$R = \dfrac{100 \times 2}{16} = 12.5$."],
        "12.5%"),
    pat("int-s4", "Interest as a fraction of the principal", "common",
        "'The SI is 1/5 (or 2/9 ...) of the sum after T years at R% — find T or R.'",
        r"\frac{PRT}{100} = \frac{P}{k} \ \Rightarrow\ T = \frac{100}{kR}",
        ["Set the fraction equal to PRT over 100.", "Cancel P from both sides.",
         "Solve for the missing letter."],
        "The principal appears on both sides, so it never enters the answer.",
        "The simple interest on a sum at 4% per annum is one-fifth of the sum. The number of years is:",
        [r"$\dfrac{4T}{100} = \dfrac{1}{5}$.", r"$T = \dfrac{100}{5 \times 4} = 5$ years."],
        "5 years"),
    pat("int-s5", "Comparing two SI situations", "common",
        "Two principals, rates or times are compared — 'how much more interest', or interest on a scaled sum.",
        r"\frac{SI_1}{SI_2} = \frac{P_1 R_1 T_1}{P_2 R_2 T_2}",
        ["SI is proportional to each of P, R and T — build the ratio.", "For a rupee difference, compute both SIs and subtract.",
         "Scaling checks: double P and half R leaves SI unchanged."],
        "The formula is a product, so scaling factors multiply.",
        "The SI on Rs 12,000 at 8% for 3 years exceeds the SI on Rs 10,000 at 7.5% for 3 years by:",
        [r"$\dfrac{12000 \times 8 \times 3}{100} = 2880$.", r"$\dfrac{10000 \times 7.5 \times 3}{100} = 2250$.", r"$2880 - 2250 = 630$."],
        "Rs 630"),
    pat("int-s6", "One sum split at two rates", "common",
        "A sum is lent in two parts at different rates; the total or the equal yearly interest is given.",
        r"r_1 a = r_2 (P - a) \ \text{(equal interest)}, \quad \frac{r_1 a + r_2 (P-a)}{100} = \text{yearly interest}",
        ["Name the first part a and the second P − a.", "Write each part's yearly interest: part × rate ÷ 100.",
         "Equate to the given total, or to each other for equal interest.", "Solve and check the two interests."],
        "Yearly interest of each part is linear in its size, so the split solves one linear equation.",
        "Rs 13,000 is lent in two parts, one at 8% and the other at 12% simple interest. The yearly interest from the two parts is equal. Find the part lent at 8%.",
        [r"$8a = 12(13000 - a)$.", r"$20a = 156000$, so $a = 7800$.", r"Check: $8\%$ of $7800 = 624 = 12\%$ of $5200$."],
        "Rs 7,800"),
]

# ================= int-ci =================

# ---------- answer checks: int-ci ----------
assert 12000 * F(11, 10) ** 2 == 14520 and 14520 - 12000 == 2520 and F(12000 * 10 * 2, 100) == 2400
assert 10000 * F(11, 10) ** 2 == 12100 and 12100 - 10000 == 2100
assert F(11, 10) ** 2 == F(121, 100) and F(6, 5) ** 2 == F(36, 25) and F(5, 4) ** 2 == F(25, 16)
assert F(21, 20) ** 2 == F(441, 400) and F(11, 10) ** 3 == F(1331, 1000) and F(6, 5) ** 3 == F(216, 125)
assert F(9, 8) ** 2 == F(81, 64) and F(81, 64) - 1 == F(17, 64)
assert F(6, 5) ** 2 == F(36, 25) and F(3, 2) ** 2 == F(9, 4) and F(11, 10) ** 3 == F(1331, 1000)
assert 10000 * F(11, 10) ** 3 == 13310 and 13310 - 10000 == 3310
assert 25000 * F(11, 10) * F(6, 5) == 33000
assert 20000 * (F(121, 100) - 1) == 4200 and 4200 * F(3, 2) == 6300
assert 10000 * F(121, 100) == 12100 and 12100 * F(5, 100) == 605 and 12100 + 605 == 12705
assert 4840 * F(100, 121) == 4000 and 6655 * F(1000, 1331) == 5000

CI_CONCEPT = (
    "Compound interest adds each year's interest to the principal, so the next year charges more. "
    "The amount grows by the same **factor** every year, not the same rupees.\n\n"
    "Use $A = P\\left(1 + \\dfrac{R}{100}\\right)^T$ and $CI = A - P$. "
    "Write the rate as a chip fraction ($10\\% \\to \\dfrac{11}{10}$) and multiply one chip per year."
)

CI_NOTES = r"""### What compounding means
In compound interest, each year's interest is added to the principal before the next year is charged. Interest starts earning interest, so the amount grows by the same factor every year.

Rs 10,000 at 10%: after one year 11,000, after two years 12,100. The second jump is Rs 1,100, not Rs 1,000 — the extra Rs 100 is interest on interest.

> **Rule:** One chip per year: $A = P \times \left(1 + \dfrac{R}{100}\right)^T$ and $CI = A - P$.

### Chips worth knowing by heart
| Rate | Chip | | Rate | Chip |
|---|---|---|---|---|
| 5% | 21/20 | | 8% | 27/25 |
| 10% | 11/10 | | 12.5% | 9/8 |
| 20% | 6/5 | | 25% | 5/4 |

CI on Rs 12,000 at 10% for 2 years: $12000 \times \dfrac{11}{10} \times \dfrac{11}{10} = 14520$, so CI $= 2520$. The same money at simple interest gives only 2,400.

> **Tip:** Keep chips as fractions. They stay exact, and exam numbers cancel cleanly.

### Net per cent for two and three years
Square the chip to read the two-year effect: 10% → 21% (not 20%), 20% → 44%, 25% → 56.25%, 5% → 10.25%.

Three years: 10% → 33.1%, 20% → 72.8%. Fraction rates stay clean: $12.5\%$ has chip $\dfrac{9}{8}$, so two years multiply the money by $\dfrac{81}{64}$ and CI $= \dfrac{17}{64}$ of P.

These small tables answer "the amount is what per cent of P" instantly.

### Compounding more often than once a year
- **Half-yearly**: rate halves, periods double — $A = P\left(1 + \dfrac{R}{200}\right)^{2T}$.
- **Quarterly**: rate quarters, periods quadruple — $A = P\left(1 + \dfrac{R}{400}\right)^{4T}$.

Rs 10,000 at 20% for $1\dfrac{1}{2}$ years compounded half-yearly is 3 periods at 10%: $10000 \times 1.1^3 = 13310$.

> **Careful:** $1\dfrac{1}{2}$ years half-yearly is 3 periods, not 2. Count periods before touching any chip.

More frequent compounding always gives more interest than yearly compounding at the same yearly rate.

### Broken years
$2\dfrac{1}{2}$ years at 10% compounded yearly: chips for the 2 full years, then simple interest for the half year on the amount.

$$10000 \times 1.1 \times 1.1 = 12100, \qquad 12100 \times \dfrac{5}{100} = 605, \qquad A = 12705$$

> **Watch:** The mixed rule (compound full years, simple the leftover fraction) is only for "compounded annually" questions. Half-yearly compounding handles the half year as its own full period.

### A different rate each year
Multiply each year's own chip. Rs 25,000 at 10% in year one and 20% in year two: $25000 \times \dfrac{11}{10} \times \dfrac{6}{5} = 33000$. A loss year simply uses a chip below 1.

### Scaling and going backwards
CI is proportional to P: at the same rate and time, CI on Rs 30,000 is 1.5 times CI on Rs 20,000.

From an amount back to P, divide by the chips: Rs 6,655 after 3 years at 10% is $\dfrac{6655}{1.331} = 5000$.

> **Note:** Know the powers cold: $1.1^2 = 1.21$, $1.1^3 = 1.331$, $1.2^2 = 1.44$, $1.25^2 = 1.5625$, $1.2^3 = 1.728$.
"""

CI_FORMULAS = [
    {"name": "Compound amount", "tex": r"A = P\left(1 + \frac{R}{100}\right)^T", "note": "One chip per year."},
    {"name": "Compound interest", "tex": r"CI = A - P = P\left[\left(1 + \frac{R}{100}\right)^T - 1\right]"},
    {"name": "Year-wise multipliers", "tex": r"A = P \times \frac{100 + r_1}{100} \times \frac{100 + r_2}{100} \times \cdots", "note": "For rates that change yearly."},
    {"name": "Half-yearly compounding", "tex": r"A = P\left(1 + \frac{R}{200}\right)^{2T}", "note": "Rate halves, periods double."},
    {"name": "Quarterly compounding", "tex": r"A = P\left(1 + \frac{R}{400}\right)^{4T}", "note": "Rate quarters, periods quadruple."},
]

CI_TRICKS = [
    {
        "title": "Multiply the chips",
        "body": "One chip per year, multiplied. Fraction chips cancel before you multiply.",
        "example": {
            "q": "Find the amount on Rs 10,000 at 10% per annum compound interest for 2 years.",
            "steps": [r"$10000 \times \dfrac{11}{10} \times \dfrac{11}{10} = 12100$.", r"CI $= 12100 - 10000 = 2100$."],
            "answer": "Rs 12,100 (CI Rs 2,100)",
        },
    },
    {
        "title": "Divide the chips to get P",
        "body": "An amount after T years walks back to the principal by dividing by the chip T times.",
        "example": {
            "q": "A sum amounts to Rs 4,840 in 2 years at 10% per annum CI. Find the sum.",
            "steps": [r"$P = 4840 \times \dfrac{10}{11} \times \dfrac{10}{11}$.", r"$= 4000$."],
            "answer": "Rs 4,000",
        },
    },
    {
        "title": "Half-yearly: halve rate, double count",
        "body": "Convert first, then run the chips on the periods.",
        "example": {
            "q": "Find the CI on Rs 10,000 at 20% per annum for 1.5 years, compounded half-yearly.",
            "steps": [r"3 half-years at $10\%$: chip $\dfrac{11}{10}$ cubed.", r"$10000 \times \dfrac{1331}{1000} = 13310$; CI $= 3310$."],
            "answer": "Rs 3,310",
        },
    },
]

CI_MISTAKES = [
    {"wrong": "Raising one chip to a power when rates change year to year.",
     "right": "Multiply each year's own chip separately."},
    {"wrong": "Halving the time instead of the rate for half-yearly compounding.",
     "right": "Rate halves (R/200) and the number of periods doubles (2T)."},
    {"wrong": "Reporting the amount A when the CI is asked.",
     "right": "CI = A − P; subtract the principal before answering."},
    {"wrong": "Using R/200 but keeping the exponent T.",
     "right": "The exponent must count periods: 2T for half-yearly, 4T for quarterly."},
    {"wrong": "Compounding the leftover fraction of a year.",
     "right": "Compound the full years; the leftover fraction earns simple interest."},
]

CI_REVISION = [
    "One chip per year; multiply; CI $=$ A $-$ P.",
    "Net two-year effects: 10 $\\to$ 21, 20 $\\to$ 44, 25 $\\to$ 56.25 per cent.",
    "Half-yearly: R/2 and 2T periods; quarterly: R/4 and 4T.",
    "Broken period: full years compound, leftover fraction simple.",
    "Different yearly rates: multiply the year-wise chips.",
    "P from A: divide by the chip power (1.21, 1.331, 1.44).",
]

CI_PATTERNS = [
    pat("int-c1", "Amount or CI by chips", "very common",
        "P, R and whole-year T are given; the amount or CI is asked.",
        r"A = P\left(1 + \frac{R}{100}\right)^T",
        ["Write the chip 1 + R/100 as a small fraction.", "Multiply P by the chip T times.",
         "CI = A − P; check CI is more than SI."],
        "Each year scales the running amount by the same factor.",
        "Find the compound interest on Rs 12,000 at 10% per annum for 2 years.",
        [r"$12000 \times \dfrac{11}{10} \times \dfrac{11}{10} = 14520$.", r"CI $= 14520 - 12000 = 2520$ (SI would be 2400)."],
        "Rs 2,520"),
    pat("int-c2", "Net per cent or rate from a multiplier", "very common",
        "'Becomes 1.21 times in 2 years' or 'CI as a per cent of P' — the net compounding effect.",
        r"\text{net factor} = \left(1 + \frac{R}{100}\right)^T, \qquad R = 100(\sqrt[T]{m} - 1)",
        ["Square the chip for 2 years, cube it for 3.", "Read off the per cent: 1.21 → 21%, 1.44 → 44%.",
         "From a multiple, root it: m = 1.44 → chip 1.2 → 20%."],
        "Compounding applies the same growth twice, so effects multiply.",
        "A sum invested at compound interest becomes 1.44 times itself in 2 years. The annual rate is:",
        [r"Chip $= \sqrt{1.44} = 1.2$.", r"$R = (1.2 - 1) \times 100 = 20$."],
        "20% per annum"),
    pat("int-c3", "Half-yearly or quarterly compounding", "very common",
        "'Compounded half-yearly / quarterly' appears in the question, often with 1 or 1.5 years.",
        r"A = P\left(1 + \frac{R}{200}\right)^{2T} \quad \text{or} \quad P\left(1 + \frac{R}{400}\right)^{4T}",
        ["Halve (or quarter) the rate; double (quadruple) the periods.", "Run the chips on periods.",
         "1.5 years half-yearly is 3 periods."],
        "Each compounding period uses the rate for its own fraction of a year.",
        "Find the CI on Rs 10,000 at 20% per annum for 1.5 years, compounded half-yearly.",
        [r"Rate $10\%$ per half-year, 3 periods.", r"$10000 \times \left(\dfrac{11}{10}\right)^3 = 13310$.", r"CI $= 3310$."],
        "Rs 3,310"),
    pat("int-c4", "Different rates in different years", "common",
        "'10% in the first year and 20% in the second, compounded annually' — sometimes a loss year.",
        r"A = P\left(1+\frac{r_1}{100}\right)\left(1+\frac{r_2}{100}\right)\cdots",
        ["Write each year's own chip.", "Multiply them all with P.",
         "CI = A − P, or compare with another scenario."],
        "Each year compounds on the running amount at its own rate.",
        "Rs 25,000 is invested at 10% for the first year and 20% for the second, compounded annually. The amount is:",
        [r"$25000 \times \dfrac{11}{10} \times \dfrac{6}{5}$.", r"$= 33000$."],
        "Rs 33,000"),
    pat("int-c5", "Scaling the CI", "common",
        "The CI for one sum is given; the CI for another sum at the same rate and time is asked.",
        r"\frac{CI_2}{CI_1} = \frac{P_2}{P_1}",
        ["CI is proportional to P at a fixed rate and time.", "Scale by the ratio of the principals.",
         "For a changed time, use the net per cent of the new period instead."],
        "Every term of the CI formula is linear in P.",
        "The CI on Rs 20,000 for 2 years at 10% is Rs 4,200. The CI on Rs 30,000 for the same period and rate is:",
        [r"$CI_2 = 4200 \times \dfrac{30}{20}$.", r"$= 6300$."],
        "Rs 6,300"),
    pat("int-c6", "Broken period: full years plus a fraction", "common",
        "T is something like 2.5 years and the question says compounded annually.",
        r"A = P\left(1+\frac{R}{100}\right)^{\lfloor T \rfloor} \times \left(1 + \frac{R \times \text{fraction}}{100}\right)",
        ["Split T into whole years and the leftover fraction.", "Compound the whole years with chips.",
         "Charge simple interest on the result for the fraction.", "Add to finish."],
        "Banks compound full years and pay simple interest for the leftover part year.",
        "Find the compound interest on Rs 10,000 at 10% per annum for 2.5 years, compounded annually.",
        [r"$10000 \times \dfrac{11}{10} \times \dfrac{11}{10} = 12100$.", r"Half-year SI: $12100 \times \dfrac{5}{100} = 605$.", r"$A = 12705$, CI $= 2705$."],
        "Rs 2,705"),
]

# ================= int-ci-si-diff =================

# ---------- answer checks: int-ci-si-diff ----------
assert 12500 * F(12, 100) ** 2 == 180
assert F(50 * 10000, 100) == 5000 and 5000 * F(1, 10) ** 2 == 50
assert 10000 * F(1, 10) ** 2 * F(31, 10) == 310
assert F(200 * 20, 800) == 5 and F(800 * 100, 2 * 5) == 8000 and 8000 * F(5, 100) ** 2 == 20
assert 832 - 800 == 32 and F(800 * 100, 2) == 40000 and F(40000 * 8, 10000) == 32 and F(40000, 8) == 5000
assert 8000 * F(5, 100) * 2 == 800 and 8000 * F(21, 20) ** 2 == 8820 and 8820 - 8000 == 820 and 820 - 800 == 20 and 8000 * F(1, 20) ** 2 == 20
assert 8 == 2 ** 3 and 3 * 6 == 18
assert F(3, 2) ** 2 == F(9, 4)

X_CONCEPT = (
    "The gap between CI and SI is the **interest on earlier interest**.\n\n"
    "For 2 years: $CI - SI = P\\left(\\dfrac{R}{100}\\right)^2$. For 3 years: multiply that by $\\left(3 + \\dfrac{R}{100}\\right)$.\n\n"
    "At CI a sum doubles on a fixed schedule: 2 times in T years means $2^k$ times in kT years."
)

X_NOTES = r"""### Why CI and SI differ
For the first year, CI and SI on the same money at the same rate are equal. From year two they part ways: CI charges interest on the interest already earned; SI never does.

The whole gap between them is exactly this interest-on-interest.

> **Rule:** Two years: $CI - SI = P\left(\dfrac{R}{100}\right)^2$. Three years: multiply by $\left(3 + \dfrac{R}{100}\right)$.

### Two years in one line
Rs 12,500 at 12%: $12500 \times \dfrac{12}{100} \times \dfrac{12}{100} = 180$.

Run it backwards: a difference of Rs 50 at 10% means $P = \dfrac{50 \times 10000}{100} = 5000$.

At 10% the difference is only 1% of P. That gives a quick size check on every answer.

> **Watch:** CI is bigger than SI for 2 or more years, but the two are equal for a single year. Say which one is larger before computing.

### Three years
$$CI - SI = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)$$

Rs 10,000 at 10%: $10000 \times 0.01 \times 3.1 = 310$.

At small rates the bracket sits near 3, so the three-year gap runs about three times the two-year gap.

### Both figures handed to you
When a question gives both SI and CI for two years, the difference isolates the rate:

$$R = \frac{200 \times \text{difference}}{SI}$$

SI 800 and CI 820: $R = \dfrac{200 \times 20}{800} = 5\%$. Then $P = \dfrac{800 \times 100}{2 \times 5} = 8000$.

Another pair: SI 800, CI 832. Difference 32 $= P\left(\dfrac{R}{100}\right)^2$ and $PR = 40000$ from the SI. Divide: $R = 8\%$, P = 5,000.

> **Tip:** Two numbers in, two numbers out — rate first, then the principal.

### Doubling chains at CI
CI multiplies the money by the same factor every T years. So doubles in T years means 4 times in 2T, 8 times in 3T, 16 times in 4T.

A sum doubling in 6 years becomes 8 times in 18 years. Sixteen times is $2^4$, so it needs $4 \times 6 = 24$ years on the same clock.

> **Careful:** The chain belongs to CI only. At simple interest, doubling in T years means tripling in 2T — not quadrupling.

### From a multiplier to a rate
"Becomes 1.44 times in 2 years at CI" gives chip $= \sqrt{1.44} = 1.2$, so 20%. Know the squares: 1.21 → 10%, 1.44 → 20%, 2.25 → 50%. And the cubes: 1.331 → 10%, 1.728 → 20%.

### One pair, two laws
Rs 8,000 at 5% for 2 years: SI $= 800$, CI $= 8000 \times 1.05^2 - 8000 = 820$. The Rs 20 gap is exactly $8000 \times 0.05^2$.

The same pair of amounts read as SI growth would give yearly interest Rs 484, P = 4,356, rate $11\dfrac{1}{9}\%$ — a different law gives a different rate. Always check which interest the question means.
"""

X_FORMULAS = [
    {"name": "2-year difference", "tex": r"CI - SI = P\left(\frac{R}{100}\right)^2"},
    {"name": "3-year difference", "tex": r"CI - SI = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)"},
    {"name": "CI doubling chain", "tex": r"2\times \text{ in } T \Rightarrow 2^k\times \text{ in } kT"},
    {"name": "SI multiple pace", "tex": r"n\times \text{ in } T \Rightarrow n'\times \text{ in } T',\ (n'-1) = (n-1)\frac{T'}{T}", "note": "Linear, not powers."},
    {"name": "Rate from both figures", "tex": r"R = \frac{200 \times (CI_2 - SI_2)}{SI_2}", "note": "Two-year case."},
]

X_TRICKS = [
    {
        "title": "The rate-fraction squared gap",
        "body": "Two equations — the SI and the difference — hand you the rate and the principal.",
        "example": {
            "q": "The simple interest on a sum for 2 years is Rs 800 and the compound interest is Rs 832. Find the rate.",
            "steps": [r"Difference $32 = P\left(\dfrac{R}{100}\right)^2$ and $PR = 40000$.", r"$R = \dfrac{32 \times 10000}{40000} = 8$."],
            "answer": "8% (P = Rs 5,000)",
        },
    },
    {
        "title": "Count the doublings",
        "body": "Every T years at CI the money multiplies by the same factor, so count powers.",
        "example": {
            "q": "A sum doubles in 8 years at CI. In how many years will it become 8 times?",
            "steps": [r"$8 = 2^3$.", r"$3 \times 8 = 24$ years."],
            "answer": "24 years",
        },
    },
    {
        "title": "First-year interest lent again",
        "body": "For 2 years, think of the difference as the first year's interest earning R% once more.",
        "example": {
            "q": "The CI−SI difference on a sum for 2 years at 10% is Rs 50. Find the sum.",
            "steps": [r"$P \times 0.1^2 = 50$.", r"$P = 5000$."],
            "answer": "Rs 5,000",
        },
    },
]

X_MISTAKES = [
    {"wrong": "Using $P\\left(\\dfrac{R}{100}\\right)^2$ for 3 years.",
     "right": "Multiply by $\\left(3 + \\dfrac{R}{100}\\right)$ for the third year."},
    {"wrong": "Running the CI doubling chain on an SI question.",
     "right": "At SI, doubles in T means triples in 2T, not 4 times."},
    {"wrong": "Differencing two amounts without stripping the principal.",
     "right": "Differences live on interest: take SI = A − P first."},
    {"wrong": "Expecting a CI−SI gap within a single year.",
     "right": "Year one is identical; the gap starts with year two."},
]

X_REVISION = [
    "2 years: $CI - SI = P\\left(\\dfrac{R}{100}\\right)^2$.",
    "3 years: multiply by $\\left(3 + \\dfrac{R}{100}\\right)$.",
    "Both given: $R = \\dfrac{200 \\times \\text{diff}}{SI}$, then P.",
    "CI chain: $\\times 2$ in T $\\Rightarrow$ $\\times 2^k$ in kT.",
    "Multiplier m in 2 years: rate $= 100(\\sqrt{m} - 1)$.",
]

X_PATTERNS = [
    pat("int-x1", "CI minus SI for 2 years", "very common",
        "Same sum, same rate, exactly 2 years — the difference is asked, or the sum from the difference.",
        r"CI - SI = P\left(\frac{R}{100}\right)^2",
        ["Apply the formula directly for the difference.", "Reverse it: P = difference × 10000 ÷ R².",
         "Check size: at 10% the difference is 1% of P."],
        "Only the first year's interest gets re-earned, and only once.",
        "The difference between the compound and simple interest on a sum for 2 years at 10% per annum is Rs 50. Find the sum.",
        [r"$P = \dfrac{50 \times 10000}{100}$.", r"$= 5000$. Check: $5000 \times 0.01 = 50$."],
        "Rs 5,000"),
    pat("int-x2", "CI minus SI for 3 years", "very common",
        "'For 3 years' with the difference or a sum asked.",
        r"CI - SI = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)",
        ["Compute (R/100)² and multiply by (3 + R/100).", "Multiply by P, or divide the difference by the factor.",
         "At 10% the factor is 3.1."],
        "Two interest-on-interest effects stack by year three.",
        "The difference between CI and SI on Rs 10,000 for 3 years at 10% per annum is:",
        [r"$10000 \times (0.1)^2 \times 3.1$.", r"$= 310$."],
        "Rs 310"),
    pat("int-x3", "CI and SI both given", "common",
        "Both the SI and the CI for the same sum are stated; the rate or the sum is asked.",
        r"R = \frac{200 \times (CI - SI)}{SI} \quad \text{(2 years)}",
        ["Difference = interest-on-interest; SI = 2 × first-year interest.", "Divide: R/100 = difference × 2 ÷ SI.",
         "Then P = 100 × SI ÷ (2R)."],
        "Both figures share the same P and the same first-year interest.",
        "The simple interest on a sum for 2 years is Rs 800 and the compound interest is Rs 820. Find the rate per cent.",
        [r"Difference $= 20$.", r"$R = \dfrac{200 \times 20}{800} = 5$; P $= \dfrac{800 \times 100}{10} = 8000$."],
        "5% (P = Rs 8,000)"),
    pat("int-x4", "Doubling chain at CI", "common",
        "'A sum doubles in T years at CI — when is it 4, 8, 16 times?'",
        r"\times 2 \text{ in } T \ \Rightarrow\ \times 2^k \text{ in } kT",
        ["Write the target as a power of 2: 8 = 2³, 16 = 2⁴.", "Multiply T by that power.",
         "At SI the same question needs T × (n − 1) instead."],
        "CI multiplies by a constant factor per period.",
        "A sum doubles itself in 6 years at compound interest. In how many years will it become 8 times itself?",
        [r"$8 = 2^3$.", r"$3 \times 6 = 18$ years."],
        "18 years"),
    pat("int-x5", "Multiplier in 2 years — root the chip", "common",
        "'Becomes 2.25 times / 1.44 times itself in 2 years at CI' — find the rate.",
        r"R = 100\left(\sqrt{m} - 1\right)",
        ["Take the square root of the multiplier for 2 years, cube root for 3.",
         "Subtract 1 and convert to a per cent.", "Known pairs: 1.21 → 10%, 1.44 → 20%, 2.25 → 50%."],
        "The multiplier is the chip raised to the number of years.",
        "A sum becomes 2.25 times itself in 2 years at compound interest. The rate per annum is:",
        [r"$\sqrt{2.25} = 1.5$.", r"$R = 50$."],
        "50%"),
]

# ================= int-instalments =================

# ---------- answer checks: int-instalments ----------
assert F(10, 11) + F(100, 121) == F(210, 121)
assert 2520 * F(121, 210) == 1452
assert 2520 * F(11, 10) - 1452 == 1320 and (1320 * F(11, 10)) - 1452 == 0
assert 1050 * F(11, 10) == 1155 and F(1155 * 11, 21) == 605
assert F(10, 11) + F(100, 121) + F(1000, 1331) == F(3310, 1331) and 3310 * F(1331, 3310) == 1331
assert 1210 + 1100 + 1000 == 3310
assert F(5, 6) + F(25, 36) == F(55, 36) and F(5, 6) + F(25, 36) + F(125, 216) == F(455, 216)
assert F(4, 5) + F(16, 25) == F(36, 25) and F(4, 5) + F(16, 25) + F(64, 125) == F(244, 125)
assert 1200 == 5 * 300 - F(1, 10) * 300 * 10 and 1950 == F(39, 20) * 1000
assert 7200 - 1200 == 6000 and 6000 * F(12, 100) == 720 and F(6720, 12) == 560
assert 2100 * F(121, 210) == 1210
assert 1815 * F(100, 121) == 1500

T_CONCEPT = (
    "A loan is cleared by equal yearly payments; each payment covers part of the principal plus interest on the money still unpaid.\n\n"
    "Value every payment in today's money: $P = \\dfrac{x}{c} + \\dfrac{x}{c^2} + \\cdots + \\dfrac{x}{c^n}$ with $c = 1 + \\dfrac{R}{100}$.\n\n"
    "Check any answer by growing the debt year by year until it hits exactly zero."
)

T_NOTES = r"""### What an instalment does
A loan of P is cleared by **n equal yearly payments** of Rs x, each paid at the **end** of a year. Each payment must cover its share of the principal plus interest for the years that share stayed unpaid.

> **Rule:** The loan equals the value **today** of all the instalments. Money paid later is worth less today.

### Present value — the working rule
An instalment x paid after k years is worth only its discounted value today. With chip $c = 1 + \dfrac{R}{100}$:

$$P = \frac{x}{c} + \frac{x}{c^2} + \cdots + \frac{x}{c^n}$$

At 10% for 2 years: $P = x\left(\dfrac{10}{11} + \dfrac{100}{121}\right) = \dfrac{210x}{121}$.

So a loan of Rs 2,520 needs $x = 2520 \times \dfrac{121}{210} = 1452$.

### The table that checks everything
Grow the debt one year, subtract the instalment, repeat:

| Year | Debt × 1.1 − instalment |
|---|---|
| 1 | $2520 \times 1.1 - 1452 = 1320$ |
| 2 | $1320 \times 1.1 - 1452 = 0$ |

> **Tip:** The final row must land exactly on zero. A miss of even Rs 1 means the instalment is wrong.

### Ready-made loan factors
| Rate | 2 instalments | 3 instalments |
|---|---|---|
| 10% | P = 210x/121 | P = 3310x/1331 |
| 20% | P = 55x/36 | P = 455x/216 |
| 25% | P = 36x/25 | P = 244x/125 |

Every entry is just the discounted fractions added. So Rs 3,310 at 10% over 3 years needs $x = 3310 \times \dfrac{1331}{3310} = 1331$ — and indeed $1210 + 1100 + 1000 = 3310$.

### Instalments at simple interest
The exam shortcut subtracts the interest the early payments save:

$$P = nx - \frac{r}{100} \cdot x \cdot \frac{n(n-1)}{2}$$

Rs 1,200 at 10% in 5 yearly payments: $1200 = 5x - 0.1x \times 10 = 4x$, so x = 300. Two payments at 5%: $1950 = 2x - 0.05x$, so x = 1,000.

> **Careful:** The deduction uses n(n−1)/2, one per pair of years the later instalments save. Writing n(n+1)/2 is the standard slip.

### Hire purchase and down payments
Cash price minus down payment gives the balance; only the balance carries interest.

Flat interest shape: add balance × R × T/100 and split evenly. Balance 6,000 at 12% for 1 year in 12 monthly parts: $\dfrac{6000 + 720}{12} = 560$ per month.

Compounding shape: apply the present-value rule to the balance. Rs 2,100 at 10% in 2 yearly payments: $\dfrac{210x}{121} = 2100$, so x = 1,210.

### Present worth of one future payment
The same rule with a single term. Rs 1,815 due after 2 years at 10% CI is worth $\dfrac{1815}{1.21} = 1500$ today.

> **Note:** Discounting is compounding run backwards: divide by the chip once per year of delay.
"""

T_FORMULAS = [
    {"name": "Present value (CI)", "tex": r"P = \sum_{k=1}^{n} \frac{x}{\left(1 + \frac{r}{100}\right)^k}", "note": "One term per instalment."},
    {"name": "Simple interest instalment", "tex": r"P = nx - \frac{x\,r}{100} \cdot \frac{n(n-1)}{2}", "note": "Interest the early payments save."},
    {"name": "Tabular step", "tex": r"\text{debt}_{k+1} = \text{debt}_k\left(1 + \frac{r}{100}\right) - x", "note": "Must end at zero."},
]

T_TRICKS = [
    {
        "title": "Grow, subtract, repeat",
        "body": "Two or three rows of the debt table finish any small question.",
        "example": {
            "q": "A man borrows Rs 1,050 at 10% per annum compound interest and repays it in two equal annual instalments. Find each instalment.",
            "steps": [r"Year 1: $1050 \times 1.1 = 1155$; debt $= 1155 - x$.", r"Year 2: $(1155 - x) \times 1.1 = x$.", r"$1270.5 = 2.1x$, so $x = 605$."],
            "answer": "Rs 605",
        },
    },
    {
        "title": "Present-value one-liner",
        "body": "Discount each instalment by the chip power for its year and add.",
        "example": {
            "q": "A loan of Rs 2,520 at 10% CI is repaid in 2 equal annual instalments. Find each instalment.",
            "steps": [r"$2520 = x\left(\dfrac{10}{11} + \dfrac{100}{121}\right) = \dfrac{210x}{121}$.", r"$x = 2520 \times \dfrac{121}{210} = 1452$."],
            "answer": "Rs 1,452",
        },
    },
    {
        "title": "SI instalment shortcut",
        "body": "Use $P = nx - \\dfrac{xr}{100} \\cdot \\dfrac{n(n-1)}{2}$ straight off for simple-interest loans.",
        "example": {
            "q": "Rs 1,950 is repaid in two equal annual instalments at 5% per annum simple interest. Find each instalment.",
            "steps": [r"$1950 = 2x - \dfrac{5x}{100} \times 1$.", r"$1950 = 1.95x$, so $x = 1000$."],
            "answer": "Rs 1,000",
        },
    },
]

T_MISTAKES = [
    {"wrong": "Charging a full year's interest on money already repaid.",
     "right": "Interest accrues on the outstanding balance only."},
    {"wrong": "Discounting every instalment by the same chip power.",
     "right": "The instalment after k years divides by the k-th power of the chip."},
    {"wrong": "Taking n(n+1)/2 in the SI shortcut.",
     "right": "The bracket is n(n−1)/2."},
    {"wrong": "Stopping the table one row early.",
     "right": "The debt must read exactly zero after the last instalment."},
    {"wrong": "Applying interest to the full cash price in hire purchase.",
     "right": "Only the balance after the down payment carries interest."},
]

T_REVISION = [
    "Loan $=$ sum of instalments discounted to today.",
    "10%, 2 years: $P = \\dfrac{210x}{121}$; 20%: $\\dfrac{55x}{36}$.",
    "Always verify with the zero-balance table.",
    "SI shortcut: $P = nx - \\dfrac{xr}{100} \\cdot \\dfrac{n(n-1)}{2}$.",
    "Hire purchase: interest on the balance only.",
    "Present worth $=$ future value $\\div$ chip power.",
]

T_PATTERNS = [
    pat("int-t1", "Two equal annual instalments at CI", "very common",
        "'A loan is returned in 2 equal annual instalments at R% CI' — find the instalment, or the loan from it.",
        r"P = \frac{x}{1+r} + \frac{x}{(1+r)^2}",
        ["Set the chips: 10% → 10/11 and 100/121; 20% → 5/6 and 25/36; 25% → 4/5 and 16/25.",
         "Add the two fractions; P = x times their sum.", "Divide P by the sum to get x; verify with the debt table."],
        "Each instalment is discounted for the years it is delayed.",
        "A borrows Rs 2,520 from B at 10% CI and returns it in 2 equal annual instalments. Find each instalment.",
        [r"$P = x\left(\dfrac{10}{11} + \dfrac{100}{121}\right) = \dfrac{210x}{121}$.", r"$x = 2520 \times \dfrac{121}{210} = 1452$.", r"Check: $2520 \times 1.1 - 1452 = 1320$; $1320 \times 1.1 - 1452 = 0$."],
        "Rs 1,452"),
    pat("int-t2", "Three equal annual instalments at CI", "common",
        "'Cleared in 3 equal annual instalments' — same rule, one more term.",
        r"P = x\left(\frac{1}{1+r} + \frac{1}{(1+r)^2} + \frac{1}{(1+r)^3}\right)",
        ["Build the three discounted fractions.", "At 10% they add to 3310x/1331.",
         "Divide P by the factor; check the three present values."],
        "One extra year of delay means one more discount factor.",
        "A loan of Rs 3,310 at 10% CI is repaid in 3 equal annual instalments. Each instalment is:",
        [r"$x = 3310 \times \dfrac{1331}{3310} = 1331$.", r"Present values: $1210 + 1100 + 1000 = 3310$."],
        "Rs 1,331"),
    pat("int-t3", "Instalments with simple interest", "common",
        "'Repaid in n equal annual instalments at R% simple interest.'",
        r"P = nx - \frac{r}{100}\,x\,\frac{n(n-1)}{2}",
        ["Compute the bracket n(n−1)/2.", "Write P = x times (n − r·bracket/100) and divide.",
         "Cross-check small cases with a balance table."],
        "Instalments paid early save part of the interest.",
        "A man borrows Rs 1,200 at 10% simple interest and pays it in 5 equal annual instalments. Each instalment is:",
        [r"$1200 = 5x - \dfrac{10x}{100} \times 10 = 5x - x$.", r"$1200 = 4x$, so $x = 300$."],
        "Rs 300"),
    pat("int-t4", "Hire purchase with a down payment", "common",
        "'Cash price Rs C, Rs D paid down, the balance with interest in equal instalments.'",
        r"\text{instalment} = \frac{\text{balance}(1 + RT/100)}{n} \ \text{(flat)} \quad \text{or PV on the balance}",
        ["Balance = cash price − down payment; work only with the balance.",
         "Flat interest: add balance × R × T/100 and split evenly.", "At a compounding rate, use present value on the balance."],
        "The down payment is settled today, so it never earns interest.",
        "A TV costs Rs 7,200 cash. A buyer pays Rs 1,200 down and the balance with 12% per annum interest for 1 year, in 12 equal monthly instalments (interest on the full balance). Find the monthly instalment.",
        [r"Balance $= 6000$; interest $= 6000 \times \dfrac{12}{100} = 720$.", r"$\dfrac{6000 + 720}{12} = 560$."],
        "Rs 560"),
    pat("int-t5", "Present worth of a future payment", "occasional",
        "'What is the present value of Rs A due in T years at R%?'",
        r"\text{PW} = \frac{A}{(1 + r)^T}",
        ["Divide the future amount by the chip, T times.", "For a stream of payments, do it term by term and add.",
         "Recognise it as the instalment formula with a single term."],
        "Discounting is compounding in reverse.",
        "Find the present worth of Rs 1,815 due 2 years hence at 10% per annum compound interest.",
        [r"$\dfrac{1815}{1.1 \times 1.1} = \dfrac{1815}{1.21}$.", r"$= 1500$."],
        "Rs 1,500"),
]

# ================= int-rate-time-cases =================

# ---------- answer checks: int-rate-time-cases ----------
assert 6655 * F(1000, 1331) == 5000 and 1331 * F(1000, 1331) == 1000
assert 5324 * 10 == 4840 * 11 and F(5324, 4840) == F(11, 10) and 4840 * F(100, 121) == 4000
assert 2662 * 10 == 2420 * 11 and F(2662, 2420) == F(11, 10)
assert 5000 - 4500 == 500 and 4500 - 500 == 4000 and F(500 * 100, 4000) == F(25, 2)
assert 6750 - 6000 == 750 and 6000 - 2 * 750 == 4500 and F(750 * 100, 4500) == F(50, 3)
assert F(8000 - 6800, 2) == 600 and 6800 - 3 * 600 == 5000 and F(600 * 100, 5000) == 12
assert 5600 - 5200 == 400 and 5200 - 3 * 400 == 4000 and F(400 * 100, 4000) == 10
assert 1800 - 1200 == 600 and F(600 * 100, 10000) == 6
assert 5324 - 4840 == 484 and 4840 - 484 == 4356 and F(484 * 100, 4356) == F(100, 9) == 11 + F(1, 9)
assert 5600 - 5200 == 400 and 5200 - 3 * 400 == 4000 and F(400 * 100, 4000) == 10
assert 5600 - 5200 == 400 and 5600 - 400 == 5200

R_CONCEPT = (
    "Given amounts, work backwards to the inputs.\n\n"
    "At CI, consecutive amounts **divide**: $\\dfrac{A_{T+1}}{A_T} = 1 + \\dfrac{R}{100}$. "
    "At SI they **subtract**: the gap is one year's interest.\n\n"
    "For P, divide a CI amount by the chip power, or subtract the accrued interest from an SI amount."
)

R_NOTES = r"""### Amounts tell the story
Reverse questions hand you the amounts after whole years and ask for the principal or the rate. Everything lives in the gap between two amounts.

> **Rule:** At CI divide consecutive amounts; at SI subtract them. Match the operation to the growth law.

### CI: the ratio trick
$$\frac{A_{T+1}}{A_T} = 1 + \frac{R}{100}$$

Amounts Rs 4,840 (2 years) and Rs 5,324 (3 years): $\dfrac{5324}{4840} = 1.1$, so the rate is 10%. The principal never entered. Walk back for it: $\dfrac{4840}{1.21} = 4000$.

Another pair, smaller money: Rs 2,420 then Rs 2,662. The ratio $\dfrac{2662}{2420} = \dfrac{11}{10}$ again — 10%. The ratio never cares how large the sum is.

> **Watch:** The ratio gives the chip 1.1; the rate is 10%. Reporting 1.1 as the rate is a real trap option.

### SI: the constant gap
SI adds the same rupees every year, so consecutive amounts differ by exactly one year's interest:

$$A_{T+1} - A_T = \frac{P \times R}{100}$$

Amounts Rs 4,500 then Rs 5,000: yearly interest 500; P = 4500 − 500 = 4000; rate $= \dfrac{500 \times 100}{4000} = 12.5\%$.

One more: Rs 6,000 then Rs 6,750 gives a gap of 750. If the question adds P = 4,500, the rate is $\dfrac{750 \times 100}{4500} = 16\dfrac{2}{3}\%$.

### Gaps wider than one year
Non-consecutive amounts: divide the rupee gap by the year gap first.

Rs 6,800 after 3 years and Rs 8,000 after 5 years: $\dfrac{8000 - 6800}{2} = 600$ per year. Then P = 6800 − 3 × 600 = 5000 and the rate is 12%.

> **Careful:** 3 → 5 years is two years of interest. Dividing by 2 is the step students forget.

### Two SIs on one sum
SI 1,200 for 2 years and 1,800 for 3 years: the Rs 600 difference is one year's interest, so $\dfrac{PR}{100} = 600$.

That is one equation in two unknowns, so the question must supply P or R. With P = 10,000 the rate is 6%; with rate 6% the sum is 10,000. The two SIs alone never fix both.

### The classic 2-year / 3-year pair at SI
"A sum amounts to A in 2 years and B in 3 years at SI." Yearly interest is B − A. Then P = A − 2(B − A) = 3A − 2B. The rate is $\dfrac{(B-A) \times 100}{P}$.

Rs 5,200 after 3 years and Rs 5,600 after 4 years: yearly 400, P = 5200 − 3 × 400 = 4000, rate 10%.

### Going back at CI
From a single amount, divide by the chip power: Rs 6,655 after 3 years at 10% → $\dfrac{6655}{1.331} = 5000$.

And Rs 4,840 after 2 years at 10% is $\dfrac{4840}{1.21} = 4000$ — the same 4,000 the ratio walk gave above.

> **Note:** Know the powers cold: 1.21, 1.331, 1.44, 1.5625, 1.728. They turn divisions into one step.
"""

R_FORMULAS = [
    {"name": "Principal from amount", "tex": r"P = \frac{A}{\left(1 + \frac{r}{100}\right)^T}", "note": "CI: divide by the chip power."},
    {"name": "Rate from consecutive amounts", "tex": r"1 + \frac{r}{100} = \frac{A_{t+1}}{A_t} \quad (\text{CI})", "note": "Divide at CI."},
    {"name": "Yearly SI from amounts", "tex": r"SI_{\text{year}} = A_{t+1} - A_t \quad (\text{SI})", "note": "Subtract at SI."},
    {"name": "Two-amount system", "tex": r"\frac{A_2}{A_1} = 1 + \frac{r}{100} \Rightarrow P = \frac{A_1}{1 + r/100}"},
]

R_TRICKS = [
    {
        "title": "Ratio first, then walk back",
        "body": "The ratio of consecutive CI amounts exposes the chip; divide once more for P.",
        "example": {
            "q": "A sum amounts to Rs 1,331 in 3 years at 10% per annum CI. Find the sum.",
            "steps": [r"$P = 1331 \times \dfrac{10}{11} \times \dfrac{10}{11} \times \dfrac{10}{11}$.", r"$= 1000$."],
            "answer": "Rs 1,000",
        },
    },
    {
        "title": "Equal yearly steps at SI",
        "body": "Check the amounts differ by a constant — that constant is the yearly interest.",
        "example": {
            "q": "A sum amounts to Rs 6,000 in 2 years and Rs 6,750 in 3 years at SI. Find the rate if P = Rs 4,500.",
            "steps": [r"Yearly SI $= 6750 - 6000 = 750$.", r"Check: $4500 + 2 \times 750 = 6000$.", r"$R = \dfrac{750 \times 100}{4500} = 16\dfrac{2}{3}\%$."],
            "answer": "16 2/3% p.a.",
        },
    },
    {
        "title": "Two amounts, two unknowns",
        "body": "Dividing the amounts kills P and hands you the chip.",
        "example": {
            "q": "A sum amounts to Rs 4,840 in 2 years and Rs 5,324 in 3 years at CI. Find the rate.",
            "steps": [r"$\dfrac{5324}{4840} = \dfrac{11}{10}$.", r"$R = 10$."],
            "answer": "10% p.a.",
        },
    },
]

R_MISTAKES = [
    {"wrong": "Dividing SI amounts to get the rate.",
     "right": "SI amounts grow by equal rupees; subtract them. Divide only at CI."},
    {"wrong": "Subtracting CI amounts to get the yearly interest.",
     "right": "CI growth is multiplicative; the ratio of consecutive amounts is the chip."},
    {"wrong": "Reporting the chip 1.1 as the rate.",
     "right": "Rate = (chip − 1) × 100 = 10%."},
    {"wrong": "Using the whole rupee gap when the years skip.",
     "right": "Divide the gap by the year gap first: 3 → 5 years is 2 years."},
    {"wrong": "Feeding SI amounts into a CI formula.",
     "right": "Check the growth law first: equal gaps mean SI."},
]

R_REVISION = [
    "CI: $\\dfrac{A_{T+1}}{A_T}$ is the chip; subtract 1 for the rate.",
    "SI: $A_{T+1} - A_T$ is one year's interest, constant.",
    "Year-skipping gaps: divide by the year gap.",
    "SI amounts: P = amount $-$ years $\\times$ yearly interest.",
    "CI amounts: P = amount $\\div$ chip power.",
]

R_PATTERNS = [
    pat("int-r1", "Principal from an amount at CI", "very common",
        "An amount after 2 or 3 whole years at a known CI rate is given; the original sum is asked.",
        r"P = \frac{A}{\left(1 + \frac{R}{100}\right)^T}",
        ["Recall the chip powers: 1.21, 1.331, 1.44.", "Divide the amount by the right power.",
         "P must come out smaller than the amount."],
        "Discounting undoes compounding exactly.",
        "A sum amounts to Rs 6,655 in 3 years at 10% per annum compound interest. The sum is:",
        [r"$1.1^3 = 1.331$.", r"$\dfrac{6655}{1.331} = 5000$."],
        "Rs 5,000"),
    pat("int-r2", "Rate from consecutive CI amounts", "very common",
        "Amounts after T and T+1 years are given at CI; the rate is asked.",
        r"1 + \frac{R}{100} = \frac{A_{T+1}}{A_T}",
        ["Divide the later amount by the earlier one.", "Subtract 1 and read the rate.",
         "For P, discount the given amount by the chips."],
        "One year of growth is exactly one chip.",
        "A sum amounts to Rs 4,840 in 2 years and to Rs 5,324 in 3 years at compound interest. The rate per annum is:",
        [r"$\dfrac{5324}{4840} = \dfrac{11}{10}$.", r"$R = 10$."],
        "10%"),
    pat("int-r3", "Rate from consecutive SI amounts", "very common",
        "Amounts after T and T+1 years at SI; the rate or the sum is asked.",
        r"A_{T+1} - A_T = \frac{PR}{100}, \qquad P = A_T - (A_{T+1} - A_T)",
        ["The difference is one year's interest — constant at SI.", "Subtract it from the earlier amount for P.",
         "Rate = difference ÷ P × 100."],
        "SI growth is arithmetic, so equal gaps carry equal interest.",
        "A sum amounts to Rs 4,500 in 1 year and Rs 5,000 in 2 years at simple interest. Find the rate per annum.",
        [r"Yearly interest $= 500$; P $= 4000$.", r"Rate $= \dfrac{500 \times 100}{4000} = 12.5$."],
        "12.5%"),
    pat("int-r4", "Amounts spanning several years at SI", "common",
        "'Amounts to A in m years and B in n years' with m and n not adjacent.",
        r"\text{yearly interest} = \frac{B - A}{n - m}",
        ["Divide the amount gap by the year gap.", "P = A − m × yearly interest.",
         "Rate = yearly ÷ P × 100."],
        "Linear growth means any two points fix the line.",
        "A sum amounts to Rs 6,800 in 3 years and Rs 8,000 in 5 years at simple interest. Find the rate per annum.",
        [r"Yearly $= \dfrac{8000 - 6800}{2} = 600$.", r"P $= 6800 - 1800 = 5000$.", r"Rate $= \dfrac{600 \times 100}{5000} = 12$."],
        "12%"),
    pat("int-r5", "Two SIs on the same sum", "common",
        "'SI for 2 years is x, for 3 years is y' — the difference pins the yearly interest.",
        r"\text{yearly interest} = \frac{y - x}{\Delta n}, \quad R = \frac{100 \times \text{yearly}}{P}",
        ["Yearly interest = difference of the SIs ÷ year gap.", "The yearly figure equals PR/100 — one equation.",
         "Use the P or R the question supplies; recompute both SIs to check."],
        "Same sum, same rate: every extra year adds the same rupees.",
        "The simple interest on a sum of Rs 10,000 for 2 years is Rs 1,200 and for 3 years is Rs 1,800. The rate per annum is:",
        [r"Yearly $= 1800 - 1200 = 600$.", r"$R = \dfrac{600 \times 100}{10000} = 6$."],
        "6%"),
]

# ================= write back =================

dfrac = lambda x: x.replace(r"\frac", r"\dfrac")

BLOCKS = [
    ("int-si", dict(concept=SI_CONCEPT, notes=SI_NOTES, formulas=SI_FORMULAS,
                    tricks=SI_TRICKS, mistakes=SI_MISTAKES, revision=SI_REVISION, patterns=SI_PATTERNS)),
    ("int-ci", dict(concept=CI_CONCEPT, notes=CI_NOTES, formulas=CI_FORMULAS,
                    tricks=CI_TRICKS, mistakes=CI_MISTAKES, revision=CI_REVISION, patterns=CI_PATTERNS)),
    ("int-ci-si-diff", dict(concept=X_CONCEPT, notes=X_NOTES, formulas=X_FORMULAS,
                            tricks=X_TRICKS, mistakes=X_MISTAKES, revision=X_REVISION, patterns=X_PATTERNS)),
    ("int-instalments", dict(concept=T_CONCEPT, notes=T_NOTES, formulas=T_FORMULAS,
                             tricks=T_TRICKS, mistakes=T_MISTAKES, revision=T_REVISION, patterns=T_PATTERNS)),
    ("int-rate-time-cases", dict(concept=R_CONCEPT, notes=R_NOTES, formulas=R_FORMULAS,
                                 tricks=R_TRICKS, mistakes=R_MISTAKES, revision=R_REVISION, patterns=R_PATTERNS)),
]

data = json.loads(TOPIC.read_text(encoding="utf-8"))
for sid, block in BLOCKS:
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    patterns = block["patterns"]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = {p["id"] for p in patterns}
    assert old_ids <= new_ids, (sid, old_ids - new_ids)
    all_other = {p["id"] for s in data["subtopics"] if s["id"] != sid for p in s.get("patterns", [])}
    assert not (all_other & new_ids), (sid, all_other & new_ids)
    notes = block["notes"].strip() + "\n"
    assert 2500 <= len(notes) <= 5000, (sid, len(notes))
    assert 4 <= len(re.findall(r"^### ", notes, re.M)) <= 8, sid
    block.update(notes=notes, mistakes=[{k: dfrac(v) for k, v in m.items()} for m in block["mistakes"]],
                 revision=[dfrac(r) for r in block["revision"]])
    sub.update(**block)
    print(f"{sid}: notes {len(notes)} chars, {len(patterns)} patterns (was {len(old_ids)})")

file_ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]
assert len(file_ids) == len(set(file_ids)), "duplicate pattern ids in file"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("interest.json updated")
