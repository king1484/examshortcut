"""Phase-2 deep content for quant/interest — CI−SI difference, instalments, rate/time case modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed


def P(x):
    x = F(x)
    return (num(x) if x.denominator in (1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 100) else mixed(x)) + "%"


def build_cisidiff():
    S = Sub("int-ci-si-diff")
    S.notes = r"""### Why CI and SI differ
For the **first** year, CI and SI on the same sum at the same rate are identical. They part ways from the second year: CI earns interest on the earlier interest, SI never does. So the gap is exactly the *interest earned on the accumulated interest*.

### Two years — the one-line formula
The difference is the first year's interest, re-earned once in the second year:
$$CI - SI = P\left(\frac{R}{100}\right)^2$$
₹12,500 at 12%: $12500 \times 0.12^2 = ₹180$.
Reverse: difference ₹50 at 10% → $P = \frac{50 \times 10000}{100} = ₹5{,}000$.
Notice the shape: P × rate-fraction × rate-fraction. The rate fraction $\frac{R}{100}$ appears once per extra year.

### Three years
The second year's interest also re-earns in the third, and the first year's interest re-earns twice:
$$CI - SI = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)$$
₹10,000 at 10%: $10000 \times 0.01 \times 3.1 = ₹310$.
At small rates the factor is roughly 3 (for 3 years) or 2 (for 2 years) times $\left(\frac{R}{100}\right)^2 P$.

### CI and SI both given
Given both figures for the same sum, the **difference isolates the rate**:
- 2 years: difference $= P\left(\frac{R}{100}\right)^2$ and SI $= \frac{2PR}{100}$ → divide: $\frac{R}{100} = \frac{\text{difference} \times 2}{SI}$ → $R = \frac{200 \times \text{difference}}{SI}$.
SI ₹800, CI ₹820 → $R = \frac{200 \times 20}{800} = 5\%$, then $P = \frac{800 \times 100}{2 \times 5} = ₹8{,}000$.
- Then the CI itself is just SI + difference.

### Doubling chains at CI
At CI a sum multiplies by the same factor every fixed period. If it **doubles in T years**:
- 4 times in 2T, 8 times in 3T — powers of 2.
- "16 times" = $2^4$ → 4T.
₹P doubling in 6 years → 8 times in 18 years. At SI this does **not** work (linear growth: 3 times takes 2T) — check which interest the question uses.

### Multiplier → rate
Amounts given as multiples: "becomes 1.44 times in 2 years at CI" → chip² $= 1.44$ → chip $= 1.2$ → 20%. Common squares: 1.21 → 10%, 1.44 → 20%, 2.25 → 50%; cubes: 1.728 → 20%, 1.331 → 10%.

### A quick worked case
₹8,000 at 5% for 2 years: SI $= 800$, CI $= 8000(1.05^2 - 1) = 820$ — difference ₹20, which is exactly $8000 \times 0.05^2$. Every 2-year question is this single multiplication in disguise; train yourself to see the rate fraction squared.

### Quick revision
- 2 years: $CI - SI = P\left(\frac{R}{100}\right)^2$.
- 3 years: $CI - SI = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)$.
- Difference and SI given: $R = \frac{200 \times \text{diff}}{SI}$ (2 years), then $P = \frac{100 \times SI}{2R}$.
- CI doubling chain: ×2 in T → ×$2^k$ in kT.
- Multiplier m in 2 years → rate $= 100(\sqrt{m} - 1)$.
"""

    S.pattern("int-x1", "CI − SI for 2 years", "very common",
              "Same sum at the same rate for exactly 2 years — find the difference, or the sum from the difference.",
              r"CI - SI = P\left(\frac{R}{100}\right)^2",
              r"""1. Apply the formula directly for the difference.
2. Reverse: $P = \frac{\text{difference} \times 10000}{R^2}$.
3. Check magnitude: at 10% the difference is only 1% of P.

Why: only the first year's interest is re-earned, once.""",
              "The difference between the compound and simple interest on a sum for 2 years at 10% per annum is ₹50. Find the sum.",
              r"$P = \frac{50 \times 10000}{100} = ₹5{,}000$. Check: $5000 \times 0.01 = 50$.")
    S.pattern("int-x2", "CI − SI for 3 years", "very common",
              "'For 3 years' with both interests asked or their difference.",
              r"CI - SI = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)",
              r"""1. Compute $\left(\frac{R}{100}\right)^2$ and multiply by $\left(3 + \frac{R}{100}\right)$.
2. Multiply by P (or divide the difference by this factor to get P).
3. At 10% the factor is 3.1; the difference is 3.1% of P.

Why: two extra 'interest-on-interest' effects stack up in year three.""",
              "The difference between CI and SI on ₹10,000 for 3 years at 10% per annum is:",
              r"$10000 \times (0.1)^2 \times 3.1 = ₹310$.")
    S.pattern("int-x3", "CI and SI both given — find rate and sum", "common",
              "Both the SI and the CI (2 or 3 years) are given for the same sum; the rate or the sum is asked.",
              r"\frac{CI - SI}{SI} = \frac{\frac{R}{100}}{n}\ \ (n \text{ years}) \Rightarrow R = \frac{200\,(CI-SI)}{SI}\ \text{for 2 years}",
              r"""1. Difference = interest-on-interest; SI = n × first-year interest.
2. Divide difference by SI to get $\frac{R}{100n}$; find R.
3. Then $P = \frac{100 \times SI}{nR}$; CI = SI + difference if asked.

Why: both quantities share the same P and first-year interest.""",
              "The simple interest on a sum for 2 years is ₹800 and the compound interest is ₹820. Find the rate per cent.",
              r"$R = \frac{200 \times 20}{800} = 5\%$; P $= ₹8{,}000$.")
    S.pattern("int-x4", "Doubling chain at CI (powers)", "common",
              "'A sum doubles in T years at CI — when is it 4, 8, 16 times?'",
              r"\times 2 \text{ in } T \ \Rightarrow\ \times 2^k \text{ in } kT",
              r"""1. Write the target as a power of 2: 8 = 2³, 16 = 2⁴.
2. Multiply T by that power.
3. At SI the same question gives T × (n − 1) — don't mix the two.

Why: CI multiplies by a constant factor per period.""",
              "A sum doubles itself in 6 years at compound interest. In how many years will it become 8 times itself?",
              r"$8 = 2^3$ → $3 \times 6 = 18$ years.")
    S.pattern("int-x5", "Multiplier in 2 years — root the chip", "common",
              "'Becomes 2.25 times / 1.69 times itself in 2 years at CI' — find the rate.",
              r"R = 100\left(\sqrt{m} - 1\right)",
              r"""1. Take the square root of the multiplier (2 years) or cube root (3 years).
2. Subtract 1 and convert to a per cent.
3. Known pairs: 1.21 → 10%, 1.44 → 20%, 2.25 → 50%; 1.728 → 20% (3 years).

Why: the multiplier is the chip raised to the number of years.""",
              "A sum becomes 2.25 times itself in 2 years at compound interest. The rate per annum is:",
              r"$\sqrt{2.25} = 1.5$ → $R = 50\%$.")

    d = 12500 * F(12, 100) ** 2
    assert d == 180
    S.q("int-x1", "easy",
        "The difference between the compound interest and the simple interest on ₹12,500 at 12% per annum for 2 years is:",
        ["₹180", "₹150", "₹200", "₹160"], rs(d),
        r"$12500 \times \left(\frac{12}{100}\right)^2 = ₹180$.",
        "₹150 scales linearly with the rate; the difference grows as the square.", 25)
    P_ = 50 * 10000 / (10 * 10)
    assert P_ == 5000
    S.q("int-x1", "medium",
        "The difference between the compound interest and the simple interest on a sum for 2 years at 10% per annum is ₹50. The sum is:",
        ["₹5,000", "₹4,500", "₹5,500", "₹6,000"], rs(P_),
        r"$P = \frac{50 \times 10000}{10^2} = ₹5{,}000$.",
        "₹500 divides by 10 — the difference uses the rate squared.", 30)
    d = 10000 * F(1, 10) ** 2 * F(31, 10)
    assert d == 310
    S.q("int-x2", "medium",
        "The difference between the compound interest and the simple interest on ₹10,000 for 3 years at 10% per annum is:",
        ["₹310", "₹300", "₹331", "₹210"], rs(d),
        r"$10000 \times (0.1)^2 \times (3 + 0.1) = 10000 \times 0.031 = ₹310$.",
        "₹331 is the full third-year CI on 10,000, not the difference.", 30)
    P_ = 310 / (F(1, 10) ** 2 * F(31, 10))
    assert P_ == 10000
    S.q("int-x2", "hard",
        "The difference between the compound interest and the simple interest on a sum for 3 years at 10% per annum is ₹310. The sum is:",
        ["₹10,000", "₹9,000", "₹12,000", "₹10,500"], rs(P_),
        r"Factor $= (0.1)^2 \times 3.1 = 0.031$ → $P = \frac{310}{0.031} = ₹10{,}000$.",
        "Using the 2-year formula gives ₹31,000 — count 3 years here.", 40)
    R_ = 200 * 20 / 800
    assert R_ == 5
    S.q("int-x3", "medium",
        "The simple interest on a certain sum for 2 years at the same rate is ₹800 and the compound interest is ₹820. The rate of interest per annum is:",
        ["5%", "4%", "2.5%", "6.25%"], P(R_),
        r"$R = \frac{200 \times (820-800)}{800} = 5\%$.",
        "2.5% halves where it should double: difference = P(R/100)², SI = 2PR/100.", 35)
    R_ = 100 * 38.4 / 480
    assert R_ == 8
    S.q("int-x3", "hard",
        "The simple interest on a sum for 2 years is ₹960 and the compound interest is ₹998.40. The rate of interest per annum is:",
        ["8%", "5%", "4%", "10%"], P(R_),
        r"Difference $= 38.40 = P\left(\frac{R}{100}\right)^2$ and $\frac{2PR}{100} = 960$ → $PR = 48000$. So $48000 \times \frac{R}{10000} = 38.40$ → $R = 8\%$.",
        "Then P = 6,000; the CI checks as 998.40.", 45)
    S.q("int-x4", "easy",
        "A sum of money doubles itself in 6 years at compound interest. In how many years will it become 8 times itself?",
        ["18 years", "12 years", "24 years", "21 years"], "18 years",
        r"$8 = 2^3$ → $3 \times 6 = 18$ years.",
        "24 years is the SI-style chain (1 + 3 × 6 used loosely) — powers, not multiples, at CI.", 25)
    S.q("int-x4", "medium",
        "A sum becomes four times itself in 10 years at compound interest. In how many years will the same sum become 32 times itself?",
        ["25 years", "40 years", "30 years", "50 years"], "25 years",
        r"$4 = 2^2$ → doubling time 5 years; $32 = 2^5$ → $5 \times 5 = 25$ years.",
        "The doubling time is 5, not 10 — 4 times needs only two doublings.", 30)
    R_ = (F(225, 100) ** F(1, 2) - 1) * 100
    assert R_ == 50
    S.q("int-x5", "medium",
        "A sum invested at compound interest becomes 2.25 times itself in 2 years. The rate of interest per annum is:",
        ["50%", "25%", "60%", "45%"], P(R_),
        r"Chip $= \sqrt{2.25} = 1.5$ → $R = 50\%$.",
        "25% would compound to only 1.5625 times.", 30)
    R_ = (F(1728, 1000) ** F(1, 3) - 1) * 100
    assert F(12, 10) ** 3 == F(1728, 1000)
    S.q("int-x5", "hard",
        "A sum becomes 1.728 times itself in 3 years at compound interest, compounded annually. The rate of interest per annum is:",
        ["20%", "12%", "24%", "18%"], "20%",
        r"Cube root: $1.2^3 = 1.728$ → $R = 20\%$.",
        r"24% would give $1.24^3 \approx 1.907$ — test the known cube 1.728 = 1.2³.", 40)
    return S


def build_instalments():
    S = Sub("int-instalments")
    S.notes = r"""### The idea: instalments repay principal plus interest
A loan of P is cleared by **n equal annual instalments** of ₹x paid at the **end** of each year. Each instalment must cover (a) its share of the principal and (b) interest for the time the money stayed with the borrower.

### Present value — the one rule
The instalment paid after k years is worth only $\frac{x}{(1+r)^k}$ **today**, where $r = \frac{R}{100}$. The loan equals the present values of all instalments:
$$P = \frac{x}{1+r} + \frac{x}{(1+r)^2} + \cdots + \frac{x}{(1+r)^n}$$
Take the common denominator and solve for x. At 10% for 2 years:
$$P = x\left(\frac{10}{11} + \frac{100}{121}\right) = \frac{210x}{121}$$
so P = 2,520 → $x = \frac{2520 \times 121}{210} = ₹1{,}452$.
The tabular check: year 1 debt $= 2520 \times 1.1 - 1452 = 1320$; year 2: $1320 \times 1.1 - 1452 = 0$. Zero after the last instalment confirms the answer.

### Ready denominators
| Rate | 2 instalments | 3 instalments |
|---|---|---|
| 10% | $\frac{210}{121}x$ | $\frac{3310}{1331}x$ |
| 20% | $\frac{55}{36}x$ | $\frac{455}{216}x$ |
| 25% | $\frac{36}{25}x$ | $\frac{244}{125}x$ |
Each entry: P = factor × x, so $x = P \div$ factor. Every fraction comes from chips: $\frac{10}{11} + \frac{100}{121}$ etc.

### Simple-interest instalments
Here interest accrues on the **outstanding principal**, but the standard exam shortcut (which is exact for the usual 'interest on whole period deducted' reading) is:
$$P = nx - \frac{r}{100}\,x\,\frac{n(n-1)}{2}$$
The second term knocks off the interest not payable because later instalments return their money earlier. ₹1,200 at 10% in 5 annual instalments: $1200 = 5x - 0.1x \times 10 = 4x$ → x = ₹300.
A tabular SI walk (add interest on the balance, subtract the instalment) must end at zero; use it to verify small cases.

### Hire purchase / down payment
Two shapes:
1. **Balance carried at a rate, cleared by equal instalments** — apply the present-value rule to the *balance*, not the cash price. Cash price 2,500, down 400, balance 2,100 at 10% in 2 instalments: $\frac{210x}{121} = 2100$ → x = ₹1{,}210.
2. **Flat interest on the whole balance**: instalment $= \frac{\text{balance} + \text{balance} \times R \times T/100}{\text{number of instalments}}$. Balance 6,000 at 12% for 1 year in 12 monthly pieces: $\frac{6000 + 720}{12} = ₹560$.

### Present worth of a future payment
The same rule with one term: ₹1,815 due 2 years from now at 10% CI is worth $\frac{1815}{1.21} = ₹1{,}500$ today. Discounting is the reverse of compounding.

### Quick revision
- $P = \sum \frac{x}{(1+r)^k}$ — one equation, one unknown x.
- 10%, 2 years: $P = \frac{210x}{121}$; 20%: $\frac{55x}{36}$; 25%: $\frac{36x}{25}$.
- Verify by the zero-balance table.
- SI shortcut: $P = nx - \frac{rx}{100} \cdot \frac{n(n-1)}{2}$.
- H.P. flat rate: (balance + flat interest) ÷ instalments.
- Present worth = future value ÷ chip.
"""

    S.pattern("int-t1", "Two equal annual instalments (CI)", "very common",
              "'A loan is returned in 2 equal annual instalments of ₹x at R% CI' — find x, or the loan from x.",
              r"P = \frac{x}{1+r} + \frac{x}{(1+r)^2}",
              r"""1. Set chips: 10% → $\frac{10}{11}, \frac{100}{121}$; 20% → $\frac{5}{6}, \frac{25}{36}$; 25% → $\frac{4}{5}, \frac{16}{25}$.
2. Add the two fractions; P = x × their sum.
3. $x = P \times \frac{\text{denominator}}{\text{numerator}}$. Verify with the zero-balance table.

Why: each instalment is discounted for the years it is delayed.""",
              "A borrows ₹2,520 from B at 10% CI and returns it in 2 equal annual instalments. Find each instalment.",
              r"$x = 2520 \times \frac{121}{210} = ₹1{,}452$. Table: 2520×1.1 − 1452 = 1320; 1320×1.1 − 1452 = 0.")
    S.pattern("int-t2", "Three equal annual instalments (CI)", "common",
              "'Cleared in 3 equal annual instalments' — same rule, one more term.",
              r"P = x\left(\frac{1}{1+r} + \frac{1}{(1+r)^2} + \frac{1}{(1+r)^3}\right)",
              r"""1. Build the three discounted fractions.
2. 10%: $\frac{13310 + 12100 + 11000}{14641}x = \frac{36410x}{14641} = \frac{3310x}{1331}$.
3. $x = P \times \frac{1331}{3310}$ at 10% (for P = 3,310 → x = 1,331).

Why: one extra year means one extra discount factor.""",
              "A loan of ₹3,310 at 10% CI is to be repaid in 3 equal annual instalments. The value of each instalment is:",
              r"$x = 3310 \times \frac{1331}{3310} = ₹1{,}331$. (1210 + 1100 + 1000 = 3310.)")
    S.pattern("int-t3", "Instalments with simple interest", "common",
              "'Repaid in n equal annual instalments at R% simple interest.'",
              r"P = nx - \frac{r}{100}\,x\,\frac{n(n-1)}{2}",
              r"""1. Compute the deduction term $\frac{n(n-1)}{2}$.
2. Write $P = x\left[n - \frac{r}{100}\cdot\frac{n(n-1)}{2}\right]$ and divide.
3. Cross-check small cases with a balance table.

Why: instalments paid earlier save part of the interest.""",
              "A man borrows ₹1,200 at 10% simple interest and agrees to pay it in 5 equal annual instalments. Each instalment is:",
              r"$1200 = 5x - 0.1x(10) = 4x$ → x = ₹300.")
    S.pattern("int-t4", "Hire purchase with a down payment", "common",
              "'Cash price ₹C, ₹D paid down, the balance with interest in equal instalments.'",
              r"\text{instalment} = \frac{\text{balance}(1 + RT/100)}{n}\ \ \text{(flat) or PV on the balance}",
              r"""1. Balance = cash price − down payment; work only with the balance.
2. Flat interest: add balance × R × T/100 and split into instalments.
3. Rate on balance: use the present-value rule with P = balance.

Why: the down payment never earns interest for the seller.""",
              "A TV costs ₹7,200 cash. A buyer pays ₹1,200 down and the balance with 12% per annum interest for 1 year in 12 equal monthly instalments (interest on the full balance). Find the monthly instalment.",
              r"Balance 6,000; interest $= 6000 \times \frac{12}{100} = 720$; total 6,720 → ₹560 per month.")
    S.pattern("int-t5", "Present worth of a future payment", "occasional",
              "'What is the present value of ₹A due in T years at R%?'",
              r"\text{PW} = \frac{A}{(1 + r)^T}",
              r"""1. Divide the future amount by the chip T times.
2. For instalment streams, do it term by term and add.
3. Recognise it as the instalment formula with a single term.

Why: discounting is compounding in reverse.""",
              "Find the present worth of ₹1,815 due 2 years hence at 10% per annum compound interest.",
              r"$\frac{1815}{1.1 \times 1.1} = ₹1{,}500$.")

    x = 2520 * F(121, 210)
    assert x == 1452
    S.q("int-t1", "medium",
        "A borrows ₹2,520 from B at 10% per annum compound interest and agrees to return the whole amount in 2 equal annual instalments. The value of each instalment is:",
        ["₹1,452", "₹1,260", "₹1,386", "₹1,500"], rs(x),
        r"$2520 = x\left(\frac{10}{11} + \frac{100}{121}\right) = \frac{210x}{121}$ → x = ₹1,452.",
        "₹1,260 is just half the loan — interest is still due on the unpaid half.", 35)
    x = 660 * F(36, 55)
    assert x == 432
    S.q("int-t1", "hard",
        "A sum of ₹660 is borrowed at 20% per annum compound interest and repaid in 2 equal annual instalments. Each instalment is:",
        ["₹432", "₹330", "₹400", "₹450"], rs(x),
        r"$660 = x\left(\frac{5}{6} + \frac{25}{36}\right) = \frac{55x}{36}$ → x = ₹432.",
        "Table check: 660×1.2 − 432 = 360; 360×1.2 − 432 = 0.", 40)
    x = 900 * F(25, 36)
    assert x == 625
    S.q("int-t1", "hard",
        "A man takes a loan of ₹900 at 25% per annum compound interest and clears it in two equal annual instalments. The amount of each instalment is:",
        ["₹625", "₹450", "₹562.50", "₹700"], rs(x),
        r"$900 = x\left(\frac{4}{5} + \frac{16}{25}\right) = \frac{36x}{25}$ → x = ₹625.",
        "Check: 900×1.25 − 625 = 500; 500×1.25 − 625 = 0.", 40)
    x = 3310 * F(1331, 3310)
    assert x == 1331
    S.q("int-t2", "medium",
        "A loan of ₹3,310 is to be repaid in 3 equal annual instalments at 10% per annum compound interest. Each instalment is:",
        ["₹1,331", "₹1,210", "₹1,100", "₹1,440"], rs(x),
        r"$3310 = x\left(\frac{10}{11} + \frac{100}{121} + \frac{1000}{1331}\right) = \frac{3310x}{1331}$ → x = ₹1,331.",
        "The present values 1,210 + 1,100 + 1,000 add back to 3,310.", 35)
    x = 910 * F(216, 455)
    assert x == 432
    S.q("int-t2", "hard",
        "A debt of ₹910 at 20% per annum compound interest is discharged in 3 equal annual instalments. The value of each instalment is:",
        ["₹432", "₹350", "₹400", "₹455"], rs(x),
        r"$910 = x\left(\frac{5}{6} + \frac{25}{36} + \frac{125}{216}\right) = \frac{455x}{216}$ → x = ₹432.",
        r"Fractions $\frac{180 + 150 + 125}{216}$ share the denominator $6^3$.", 45)
    x = 488 * F(125, 244)
    assert x == 250
    S.q("int-t2", "hard",
        "A man borrows ₹488 at 25% per annum compound interest and repays it in 3 equal annual instalments. Each instalment is:",
        ["₹250", "₹200", "₹300", "₹244"], rs(x),
        r"$488 = x\left(\frac{4}{5} + \frac{16}{25} + \frac{64}{125}\right) = \frac{244x}{125}$ → x = ₹250.",
        r"Sum of fractions $\frac{100 + 80 + 64}{125} = \frac{244}{125}$.", 45)
    x = 1200 / (5 - F(10, 100) * 10)
    assert x == 300
    S.q("int-t3", "medium",
        "A man borrows ₹1,200 at 10% per annum simple interest and agrees to repay it in 5 equal annual instalments. The value of each instalment is:",
        ["₹300", "₹240", "₹320", "₹360"], rs(x),
        r"$1200 = 5x - \frac{10}{100}x \times 10 = 4x$ → x = ₹300.",
        "₹240 ignores the interest; ₹360 adds it the wrong way.", 35)
    x = 740 / (4 - F(5, 100) * 6)
    assert x == 200
    S.q("int-t3", "hard",
        "A sum of ₹740 is lent at 5% per annum simple interest and is to be paid back in 4 equal annual instalments. Each instalment is:",
        ["₹200", "₹185", "₹210", "₹222"], rs(x),
        r"$740 = 4x - \frac{5}{100}x \times 6 = 3.7x$ → x = ₹200.",
        r"The deduction $\frac{n(n-1)}{2} = 6$ instalment-years of interest.", 40)
    x = 2100 * F(121, 210)
    assert x == 1210
    S.q("int-t4", "hard",
        "The cash price of a scooter is ₹2,500. A buyer pays ₹400 down and agrees to pay the balance with interest at 10% per annum compound interest in 2 equal annual instalments. The value of each instalment is:",
        ["₹1,210", "₹1,100", "₹1,155", "₹1,260"], rs(x),
        r"Balance $= 2100 = \frac{210x}{121}$ → x = ₹1,210.",
        "Table check: 2100×1.1 − 1210 = 1100; 1100×1.1 − 1210 = 0.", 40)
    x = (6000 + 6000 * F(12, 100)) / 12
    assert x == 560
    S.q("int-t4", "medium",
        "A television costs ₹7,200 in cash. A customer pays ₹1,200 as down payment and the balance with 12% per annum simple interest for 1 year in 12 equal monthly instalments, the interest being charged on the full balance. The monthly instalment is:",
        ["₹560", "₹500", "₹600", "₹620"], rs(x),
        r"Balance 6,000 + interest 720 = 6,720 → $\frac{6720}{12} = ₹560$ per month.",
        "₹500 ignores interest; ₹600 charges interest on the cash price.", 30)
    pw = 1815 / F(121, 100)
    assert pw == 1500
    S.q("int-t5", "easy",
        "Find the present worth of ₹1,815 due 2 years hence at 10% per annum compound interest.",
        ["₹1,500", "₹1,650", "₹1,480", "₹1,550"], rs(pw),
        r"$\frac{1815}{1.1^2} = \frac{1815}{1.21} = ₹1{,}500$.",
        "₹1,650 discounts only one year.", 25)
    pw = 1331 / F(1331, 1000)
    assert pw == 1000
    S.q("int-t5", "medium",
        "What sum of money today is equivalent to ₹1,331 payable 3 years from now, compound interest being 10% per annum?",
        ["₹1,000", "₹1,100", "₹1,210", "₹900"], rs(pw),
        r"$\frac{1331}{1.1^3} = ₹1{,}000$.",
        "₹1,210 uses $1.1^2$ — three years need three chips.", 30)
    return S


def build_ratetime():
    S = Sub("int-rate-time-cases")
    S.notes = r"""### Reading rates out of amounts
When a sum **amounts** to given figures after whole years, the *growth between consecutive years* tells the story.

### At compound interest — the ratio trick
Consecutive yearly amounts differ by the year's interest, and
$$\frac{A_{T+1}}{A_T} = 1 + \frac{R}{100}$$
Amounts ₹4,840 (after 2 years) and ₹5,324 (after 3 years): $\frac{5324}{4840} = 1.1$ → 10%. The principal itself is not needed. From the rate, walk back to P: $\frac{4840}{1.21} = ₹4{,}000$.

### At simple interest — the constant difference
SI adds the **same rupees** every year, so consecutive amounts differ by exactly one year's interest:
$$A_{T+1} - A_T = \frac{PR}{100}$$
₹4,500 and ₹5,000: yearly interest ₹500; the sum at the start $= 4500 - 500 = ₹4{,}000$; rate $= \frac{500 \times 100}{4000} = 12.5\%$.
Non-consecutive years: divide the amount gap by the year gap first. ₹6,800 in 3 years and ₹8,000 in 5 years → $\frac{8000 - 6800}{2} = ₹600$ per year.

### Two SIs on one sum
If the SI for 2 years is 1,200 and for 3 years 1,800, the difference (₹600) is one year's interest — and $\frac{PR}{100} = 600$. That is one equation in two unknowns, so the question must supply P or R as well: P ₹10,000 → rate 6%; rate 6% → P ₹10,000. The two SIs together never determine both by themselves.

### Amounts spanning 2y and 3y at SI — the classic pair
'A sum amounts to A in 2 years and B in 3 years at SI':
yearly interest $= B - A$; P $= A - 2(B - A) = 3A - 2B$; rate $= \frac{(B-A) \times 100}{P}$.
₹5,200 (3 years) and ₹5,600 (4 years): yearly ₹400, P $= 5200 - 3 \times 400 = ₹4{,}000$, rate 10%.

### Finding P from an amount at CI
Divide by the chips: amount ₹6,655 after 3 years at 10% → $\frac{6655}{1.331} = ₹5{,}000$. Recognise $1.1^3 = 1.331$, $1.1^2 = 1.21$, $1.2^2 = 1.44$, $1.25^2 = 1.5625$.

### A quick worked case
CI, amounts 4,840 → 5,324: ratio 1.1, so 10% — and P $= \frac{4840}{1.21} = ₹4{,}000$ if asked. The same pair at SI would mean yearly interest ₹484, P $= 4356$, rate $= \frac{48400}{4356} = 11\frac{1}{9}\%$ — different answers from the same numbers, because the growth laws differ. Decide CI or SI first; the reading of the gap depends on it.

### Where the marks go
- Reading a CI gap as a rupee amount (it grows every year) or an SI gap as a ratio (it is constant) — the two standard swaps.
- Forgetting to divide non-consecutive gaps by the year count: 3 → 5 years is TWO years of interest.
- Discounting only once from a 3-year amount, or compounding when the question says simple.

### Quick revision
- CI: $\frac{A_{T+1}}{A_T} = 1 + \frac{R}{100}$ — rate needs no P.
- SI: $A_{T+1} - A_T = $ one year's interest, constant every year.
- Non-consecutive: divide the gap by the year gap.
- P from SI amounts: subtract the accrued interest years × yearly interest.
- P from CI amounts: divide by the chip power.
"""

    S.pattern("int-r1", "Principal from an amount at CI", "very common",
              "An amount after 2 or 3 whole years at a known CI rate is given; the original sum is asked.",
              r"P = \frac{A}{\left(1 + \frac{R}{100}\right)^T}",
              r"""1. Recall the chip powers: $1.1^2 = 1.21$, $1.1^3 = 1.331$, $1.2^2 = 1.44$.
2. Divide the amount by the right power.
3. Sanity check: P must be smaller than the amount.

Why: discounting undoes the compounding exactly.""",
              "A sum amounts to ₹6,655 in 3 years at 10% per annum compound interest. The sum is:",
              r"$\frac{6655}{1.331} = ₹5{,}000$. (1.331 = 1.1³.)")
    S.pattern("int-r2", "Rate from consecutive CI amounts", "very common",
              "Amounts after T and T+1 years are given at CI; the rate is asked.",
              r"1 + \frac{R}{100} = \frac{A_{T+1}}{A_T}",
              r"""1. Divide the later amount by the earlier one.
2. Subtract 1 and read the rate.
3. If P is asked, discount the given amount by the chips.

Why: one year of growth is exactly one chip.""",
              "A sum amounts to ₹4,840 in 2 years and to ₹5,324 in 3 years at compound interest. The rate per annum is:",
              r"$\frac{5324}{4840} = 1.1$ → 10%.")
    S.pattern("int-r3", "Rate from consecutive SI amounts", "very common",
              "Amounts after T and T+1 years at SI; the rate (or the sum) is asked.",
              r"A_{T+1} - A_T = \frac{PR}{100}, \qquad P = A_T - (A_{T+1} - A_T)",
              r"""1. The difference is one year's interest — constant at SI.
2. Subtract it from the earlier amount to get P.
3. Rate = difference ÷ P × 100.

Why: SI growth is arithmetic, so equal gaps hold equal interest.""",
              "A sum amounts to ₹4,500 in 1 year and ₹5,000 in 2 years at simple interest. Find the rate per annum.",
              r"Yearly interest $= 500$; P $= 4000$; rate $= \frac{500 \times 100}{4000} = 12.5\%$.")
    S.pattern("int-r4", "Amounts spanning several years at SI", "common",
              "'Amounts to A in m years and B in n years (m ≠ n ± 1)' — or two SIs over different periods.",
              r"\text{yearly interest} = \frac{B - A}{n - m}",
              r"""1. Divide the amount gap by the year gap.
2. P = A − m × yearly interest.
3. Rate = yearly ÷ P × 100. For two plain SIs, the difference of the SIs over 1 year is the yearly interest.

Why: the linear growth makes any two points fix the line.""",
              "A sum amounts to ₹6,800 in 3 years and ₹8,000 in 5 years at simple interest. Find the rate per annum.",
              r"Yearly $= \frac{1200}{2} = 600$; P $= 6800 - 1800 = ₹5{,}000$; rate 12%.")
    S.pattern("int-r5", "Two SIs on the same sum", "common",
              "'SI for 2 years is x, for 3 years is y' — the difference pins the yearly interest; P or R comes from the question.",
              r"\text{yearly interest} = \frac{y - x}{\Delta n}, \quad R = \frac{100 \times \text{yearly}}{P}, \quad P = \frac{100 \times \text{yearly}}{R}",
              r"""1. Yearly interest = difference of the two SIs ÷ year gap.
2. The yearly figure equals $\frac{PR}{100}$ — one equation. If the question gives P, get R; if it gives R, get P.
3. Check by recomputing both SIs.

Why: same sum, same rate — every extra year adds the same rupees.""",
              "The simple interest on a sum of ₹10,000 for 2 years is ₹1,200 and for 3 years is ₹1,800. The rate per annum is:",
              r"Yearly $= 1800 - 1200 = 600$; $R = \frac{600 \times 100}{10000} = 6\%$.")

    P_ = 6655 / F(1331, 1000)
    assert P_ == 5000
    S.q("int-r1", "easy",
        "A sum amounts to ₹6,655 in 3 years at 10% per annum compound interest. The original sum is:",
        ["₹5,000", "₹4,800", "₹5,200", "₹4,500"], rs(P_),
        r"$\frac{6655}{1.331} = ₹5{,}000$.",
        "₹6,000 forgets that 6,655 already includes three years of growth.", 25)
    P_ = 24200 / F(121, 100)
    assert P_ == 20000
    S.q("int-r1", "medium",
        "What sum will amount to ₹24,200 in 2 years at 10% per annum compound interest?",
        ["₹20,000", "₹19,800", "₹21,000", "₹22,000"], rs(P_),
        r"$\frac{24200}{1.21} = ₹20{,}000$.",
        "₹22,000 divides only one chip (1.1).", 30)
    R_ = (F(5324, 4840) - 1) * 100
    assert R_ == 10
    S.q("int-r2", "easy",
        "A sum amounts to ₹4,840 in 2 years and ₹5,324 in 3 years at compound interest. The rate of interest per annum is:",
        ["10%", "5%", "11%", "12.5%"], P(R_),
        r"$\frac{5324}{4840} = 1.1$ → 10%.",
        "The gap ₹484 is one year's interest on 4,840 — no principal needed.", 25)
    R_ = (F(2120, 2000) - 1) * 100
    assert R_ == 6
    S.q("int-r2", "medium",
        "A sum amounts to ₹2,000 in 1 year and ₹2,120 in 2 years at compound interest. The rate per annum is:",
        ["6%", "6.5%", "5%", "7%"], P(R_),
        r"$\frac{2120}{2000} = 1.06$ → 6%.",
        "6.5% assumes simple-interest scaling.", 25)
    R_ = 500 * 100 / 4000
    assert R_ == F(25, 2)
    S.q("int-r3", "easy",
        "A sum amounts to ₹4,500 in 1 year and ₹5,000 in 2 years at simple interest. The rate of interest per annum is:",
        ["12.5%", "10%", "11%", "15%"], P(R_),
        r"Yearly interest $= 500$; P $= 4500 - 500 = 4000$; rate $= 12.5\%$.",
        "10% would need yearly interest 450, but the amounts differ by 500.", 25)
    R_ = 500 * 100 / 5000
    assert R_ == 10
    S.q("int-r3", "medium",
        "A sum amounts to ₹5,500 in 2 years and ₹6,000 in 3 years at simple interest. The rate of interest per annum is:",
        ["10%", "9.09%", "12%", "11%"], P(R_),
        r"Yearly interest $= 500$; P $= 5500 - 1000 = 5000$; rate 10%.",
        "₹500 is one year's interest; subtract two of them for P.", 30)
    R_ = 600 * 100 / 5000
    assert R_ == 12
    S.q("int-r4", "medium",
        "A sum amounts to ₹6,800 in 3 years and ₹8,000 in 5 years at simple interest. The rate of interest per annum is:",
        ["12%", "11.76%", "10%", "15%"], P(R_),
        r"Yearly $= \frac{8000 - 6800}{2} = 600$; P $= 6800 - 3(600) = 5000$; rate 12%.",
        "₹600 per year, not 1,200 — the years 3 → 5 span two years.", 35)
    R_ = 400 * 100 / 4000
    assert R_ == 10
    S.q("int-r4", "hard",
        "A sum amounts to ₹5,200 in 3 years and ₹5,600 in 4 years at simple interest. The sum and the rate are:",
        ["₹4,000 at 10%", "₹4,400 at 9.09%", "₹3,600 at 11.1%", "₹4,800 at 8.33%"], "₹4,000 at 10%",
        r"Yearly interest $= 400$; P $= 5200 - 1200 = ₹4{,}000$; rate $= \frac{400 \times 100}{4000} = 10\%$.",
        "Divide the ₹400 gap by 1 year here; check P = 4000 + 1200 = 5200.", 40)
    R_ = 600 * 100 / 10000
    assert R_ == 6 and 10000 * 6 * 2 / 100 == 1200 and 10000 * 6 * 3 / 100 == 1800
    S.q("int-r5", "easy",
        "The simple interest on a sum of ₹10,000 is ₹1,200 for 2 years and ₹1,800 for 3 years. The rate of interest per annum is:",
        ["6%", "5%", "7.5%", "8%"], P(R_),
        r"Yearly interest $= 1800 - 1200 = 600$; rate $= \frac{600 \times 100}{10000} = 6\%$.",
        "The two SIs must differ by exactly one year's interest — ₹600.", 30)
    P_ = 600 * 100 / 10
    assert P_ == 6000 and 6000 * 10 * 4 / 100 == 2400 and 6000 * 10 * 6 / 100 == 3600
    S.q("int-r5", "medium",
        "The simple interest on a certain sum is ₹2,400 in 4 years and ₹3,600 in 6 years. If the rate is 10% per annum, the sum is:",
        ["₹6,000", "₹5,400", "₹6,600", "₹4,800"], rs(P_),
        r"Yearly interest $= \frac{3600 - 2400}{2} = 600$; P $= \frac{600 \times 100}{10} = ₹6{,}000$.",
        r"Check: $6000 \times 10 \times 4/100 = 2400$ and $\times 6 = 3600$.", 35)
    R_ = (F(169, 100) ** F(1, 2) - 1) * 100
    assert F(13, 10) ** 2 == F(169, 100)
    S.q("int-r5", "hard",
        "A sum becomes 1.69 times itself in 2 years at compound interest. The rate of interest per annum is:",
        ["30%", "34.5%", "25%", "32%"], "30%",
        r"$\sqrt{1.69} = 1.3$ → 30% per annum.",
        "34.5% divides the total growth by 2 — compounding needs the root.", 35)
    return S
