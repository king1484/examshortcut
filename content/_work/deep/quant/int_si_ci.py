"""Phase-2 deep content for quant/interest — simple interest + compound interest modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed


def P(x):
    x = F(x)
    return (num(x) if x.denominator in (1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 100) else mixed(x)) + "%"


def build_si():
    S = Sub("int-si")
    S.notes = r"""### What interest is
When you borrow money, you pay a charge for using it; when you lend or deposit, you earn it. That charge is **interest**. The money borrowed or invested is the **principal (P)**, the charge is a per-cent per year called the **rate (R% per annum)**, and the period is the **time (T, in years)**.

### Simple interest — the formula and its four faces
In simple interest (SI) the interest each year is a fixed slice of the **original** principal only. The earlier interest earns nothing more.
$$SI = \frac{P \times R \times T}{100}$$
Keep the units straight: T in years (8 months $= \frac{8}{12} = \frac{2}{3}$ year), R per year. Any one of P, R, T, SI can be found from the other three:
$$P = \frac{100 \times SI}{RT}, \quad R = \frac{100 \times SI}{PT}, \quad T = \frac{100 \times SI}{PR}$$
SI on ₹6,500 at 8% for 3 years: $\frac{6500 \times 8 \times 3}{100} = ₹1{,}560$.

### Amount
**Amount (A)** = what you finally get back or owe: $A = P + SI$. Amount questions: first get SI $= A - P$, then use the formula.
A sum amounts to ₹1,560 in 2 years at 5%: SI $= 1560 - P$ and SI $= \frac{P \times 5 \times 2}{100} = 0.1P$ → $1.1P = 1560$ → P $= ₹1{,}418.18$ — exam numbers are chosen cleaner: A ₹1,540 → P ₹1,400.

### Growth is LINEAR at SI
The amount grows by the same rupee amount every year, so the yearly amounts form an arithmetic progression. Two consequences:
- **n times in T years**: if a sum becomes n times in T years, the interest earned is $(n-1)P$, so
$$R = \frac{100(n-1)}{T}$$
Doubles in 8 years → $\frac{100}{8} = 12.5\%$. Triples in 16 → $\frac{200}{16} = 12.5\%$.
- **T from n and R**: $T = \frac{100(n-1)}{R}$. "In what time will a sum become 5 times at 12%?" → $\frac{400}{12} = 33\frac{1}{3}$ years.
The word "amounts to n times" includes the principal, so the interest part is only $(n-1)$ times P — the classic trap is using n instead of n−1.

### Fraction-of-principal questions
"The SI is $\frac{1}{5}$ of the sum at 4% — find the time." Write $\frac{PRT}{100} = \frac{P}{5}$ → $T = \frac{100}{5 \times 4} = 5$ years. The P cancels; only the fraction, R and T matter.
Same shape: "In what time will the SI be $\frac{2}{9}$ of P at 8%?" → $T = \frac{200}{9 \times 8} = 2\frac{7}{9}$ years.

### Money scaling and comparison
SI is directly proportional to P, R and T. Doubling the sum doubles the interest; halving the rate halves it; the interest on 2P at half the rate equals the original interest.
Difference questions subtract two SI computations, or use ratios: SI on 3P at r% : SI on 2P at 2r% $= 3 : 4$.

### Where the marks are lost
- Mixing months and years (R is per annum; convert months to a fraction of a year).
- Using n instead of n−1 in n-times questions.
- Dividing by the amount when the question gives SI, or the reverse.

### Quick revision
- $SI = \frac{PRT}{100}$; $A = P + SI$; solve for any missing input.
- n times in T years at SI: $R = \frac{100(n-1)}{T}$, $T = \frac{100(n-1)}{R}$.
- Growth is linear: equal rupee growth every year.
- Fraction of P as SI: $T = \frac{100 \times \text{fraction}}{R}$.
- Months to years: divide by 12.
"""

    S.pattern("int-s1", "Direct simple interest", "very common",
        "P, R and T are given and the SI (or the amount) is asked directly.",
        r"SI = \frac{PRT}{100}, \qquad A = P + SI",
        r"""1. Convert T to years (months ÷ 12).
2. Multiply P × R × T and divide by 100.
3. For the amount, add P to the SI.

Why: SI is a fixed fraction of the principal every year.""",
        "Find the simple interest on ₹6,500 at 8% per annum for 3 years.",
        r"$\frac{6500 \times 8 \times 3}{100} = ₹1{,}560$. Amount $= ₹8{,}060$.")
    S.pattern("int-s2", "Find P, R or T from the interest or amount", "very common",
        "Three of P, R, T, SI (or A) are given; the fourth is asked.",
        r"P = \frac{100 \times SI}{RT}, \quad R = \frac{100 \times SI}{PT}, \quad T = \frac{100 \times SI}{PR}",
        r"""1. If an amount is given, first take SI = A − P.
2. Rearrange $SI = \frac{PRT}{100}$ for the missing input.
3. Amount-only version: $A = P\left(1 + \frac{RT}{100}\right)$ — one linear equation.

Why: the four quantities are linked by one formula, so any three fix the fourth.""",
        "At what rate per cent per annum will ₹1,250 amount to ₹2,000 in 12 years at simple interest?",
        r"SI $= 750$ → $R = \frac{750 \times 100}{1250 \times 12} = 5\%$.")
    S.pattern("int-s3", "n times in T years (doubling, tripling)", "very common",
        "'A sum doubles / triples / becomes n times itself in T years — find the rate or time.'",
        r"R = \frac{100(n-1)}{T}, \qquad T = \frac{100(n-1)}{R}",
        r"""1. Interest earned = (n − 1) × P — subtract the principal once.
2. Rate: $\frac{100(n-1)}{T}$; Time: $\frac{100(n-1)}{R}$.
3. Chain: doubling in T means tripling in 2T, quadrupling in 3T (linear growth).

Why: 'becomes n times' gives SI = (n−1)P, and P cancels out.""",
        "A sum of money triples itself in 16 years at simple interest. The rate per annum is:",
        r"$R = \frac{100(3-1)}{16} = 12.5\%$. (Doubles in 8 years too.)")
    S.pattern("int-s4", "Interest as a fraction of the principal", "common",
        "'The SI is 1/5 (or 2/9 …) of the sum after T years at R%' — find T or R.",
        r"\frac{PRT}{100} = \frac{P}{k} \ \Rightarrow\ T = \frac{100}{kR}",
        r"""1. Set the fraction equal to $\frac{PRT}{100}$.
2. Cancel P from both sides.
3. Solve for the missing variable.

Why: the principal is common to both sides, so it never enters the answer.""",
        r"The simple interest on a sum at 4% per annum is $\frac{1}{5}$ of the sum. The number of years is:",
        r"$\frac{4T}{100} = \frac{1}{5}$ → $T = 5$ years.")
    S.pattern("int-s5", "Comparing two SI situations", "common",
        "Two principals, rates or times are compared — 'how much more interest', or SI on a scaled sum.",
        r"\frac{SI_1}{SI_2} = \frac{P_1 R_1 T_1}{P_2 R_2 T_2}",
        r"""1. SI is proportional to each of P, R, T — build the ratio.
2. For a difference, compute the two SIs and subtract.
3. 'Double P, half R' leaves SI unchanged (2 × ½ = 1).

Why: the formula is a product, so scaling factors multiply.""",
        "The SI on ₹12,000 at 8% for 3 years exceeds the SI on ₹10,000 at 7.5% for 3 years by:",
        r"$2880 - 2250 = ₹630$.")

    si = 6500 * 8 * 3 / 100
    assert si == 1560
    S.q("int-s1", "easy", "What is the simple interest on ₹6,500 at 8% per annum for 3 years?",
        ["₹1,560", "₹1,500", "₹1,620", "₹1,440"], rs(si),
        r"$\frac{6500 \times 8 \times 3}{100} = ₹1{,}560$.",
        "₹520 per year × 3 = ₹1,560.", 25)
    si = 9000 * F(25, 4) * 2 / 100
    assert si == 1125
    S.q("int-s1", "easy", r"Find the simple interest on ₹9,000 at $6\frac{1}{4}$% per annum for 2 years.",
        ["₹1,125", "₹1,120", "₹1,150", "₹1,080"], rs(si),
        r"$6\frac{1}{4}\% = \frac{1}{16}$ → SI $= \frac{9000 \times 2}{16} = ₹1{,}125$.", None, 25)
    P_ = 5475 / F(3, 2)
    assert P_ == 3650
    S.q("int-s2", "medium",
        "A sum amounts to ₹5,475 in 4 years at 12.5% per annum simple interest. The sum is:",
        ["₹3,650", "₹3,750", "₹3,600", "₹4,380"], rs(P_),
        r"SI in 4 years $= \frac{12.5 \times 4}{100} = \frac{1}{2}$ of P → $1.5P = 5475$ → $P = ₹3{,}650$.",
        "₹4,380 divides by 1.25 — the rate acts for 4 years, so the factor is 1.5.", 35)
    R_ = 750 * 100 / (1250 * 12)
    assert R_ == 5
    S.q("int-s2", "easy",
        "At what rate of simple interest per annum will ₹1,250 amount to ₹2,000 in 12 years?",
        ["5%", "4%", "6%", "5.5%"], P(R_),
        r"SI $= 750$; $R = \frac{750 \times 100}{1250 \times 12} = 5\%$.",
        "₹62.50 per year on ₹1,250 = 5%.", 30)
    R_ = 100 * 2 / 16
    assert R_ == F(25, 2)
    S.q("int-s3", "easy",
        "A sum of money becomes three times itself in 16 years at simple interest. The rate of interest per annum is:",
        ["12.5%", "8.33%", "20%", "10%"], P(R_),
        r"$R = \frac{100(3-1)}{16} = 12.5\%$.",
        "20% uses n = 3 instead of n − 1 = 2 — the principal itself is not interest.", 25)
    T_ = F(400, 12)
    assert T_ == F(100, 3)
    S.q("int-s3", "medium",
        "In how many years will a sum of money become five times itself at 12% per annum simple interest?",
        [r"$33\frac{1}{3}$ years", "25 years", "40 years", "30 years"], f"{mixed(T_)} years",
        r"$T = \frac{100(5-1)}{12} = \frac{400}{12} = 33\frac{1}{3}$ years.",
        "25 years divides by 5 — the interest is only 4 times the principal.", 30)
    T_ = 100 / (5 * 4)
    assert T_ == 5
    S.q("int-s4", "easy",
        r"The simple interest on a sum at 4% per annum is $\frac{1}{5}$ of the sum. The number of years for which the sum is invested is:",
        ["5 years", "4 years", "8 years", "20 years"], f"{num(T_)} years",
        r"$\frac{4T}{100} = \frac{1}{5}$ → $T = 5$ years.",
        "20 years inverts the fraction (SI would be 5 times P).", 25)
    si = 15000 * 6 * F(2, 3) / 100
    assert si == 600
    S.q("int-s4", "medium",
        "The simple interest on ₹15,000 at 6% per annum for 8 months is:",
        ["₹600", "₹720", "₹540", "₹900"], rs(si),
        r"8 months $= \frac{2}{3}$ year → SI $= \frac{15000 \times 6 \times 2}{100 \times 3} = ₹600$.",
        "₹900 forgets to convert months to years.", 30)
    a, b = 12000 * 8 * 3 / 100, 10000 * F(15, 2) * 3 / 100
    assert a == 2880 and b == 2250 and a - b == 630
    S.q("int-s5", "medium",
        "The simple interest on ₹12,000 at 8% per annum for 3 years exceeds the simple interest on ₹10,000 at 7.5% per annum for 3 years by:",
        ["₹630", "₹450", "₹780", "₹300"], rs(a - b),
        r"$\frac{12000 \times 8 \times 3}{100} = 2880$ and $\frac{10000 \times 7.5 \times 3}{100} = 2250$. Difference $= ₹630$.", None, 35)
    x = 1680 * (2 * F(1, 2))
    assert x == 1680
    S.q("int-s5", "hard",
        "The simple interest on a certain sum at 6% per annum for 2 years is ₹1,680. The simple interest on double the sum at half the rate for the same time is:",
        ["₹1,680", "₹840", "₹3,360", "₹2,520"], rs(x),
        r"SI scales as P × R: $2 \times \frac{1}{2} = 1$ → the interest is unchanged, ₹1,680.",
        "₹3,360 doubles only the principal; the halved rate pulls it back.", 40)
    return S


def build_ci():
    S = Sub("int-ci")
    S.notes = r"""### What compounding means
In **compound interest (CI)**, each year's interest is added to the principal before the next year's interest is worked out. The interest earns interest, so the amount grows **geometrically** — by the same *factor* each year, not the same rupees.
$$A = P\left(1 + \frac{R}{100}\right)^T, \qquad CI = A - P$$

### Multipliers (chips) — the everyday method
Write $1 + \frac{R}{100}$ as a fraction and multiply it T times:
| Rate | Chip |
|---|---|
| 10% | $\frac{11}{10}$ |
| 20% | $\frac{6}{5}$ |
| $12\frac{1}{2}\%$ | $\frac{9}{8}$ |
| $6\frac{1}{4}\%$ | $\frac{17}{16}$ |
| 8% | $\frac{27}{25}$ |
CI on ₹12,000 at 10% for 2 years: $12000 \times \frac{11}{10} \times \frac{11}{10} = ₹14{,}520$ → CI $= ₹2{,}520$.

### The net-effect percentages
Two years at R% → net factor $\left(1+\frac{R}{100}\right)^2$: 10% → 21% (not 20%); 20% → 44%; 25% → 56.25%; 5% → 10.25%.
Three years at 10% → 33.1%; at 20% → 72.8%. These small tables answer "find the amount as % of P" questions instantly.
A 12.5% rate is $\frac{1}{8}$: two years multiply by $\frac{81}{64}$ → amount $= \frac{81}{64}P$, CI $= \frac{17}{64}P$. Fraction chips keep everything exact — prefer them to decimals.

### Fractional years and broken periods
$2\frac{1}{2}$ years at R% (annual compounding) = 2 full years by chips, then **simple interest for the half year** on the amount:
₹10,000 at 10% for $2\frac{1}{2}$ years → $10000 \times 1.1 \times 1.1 = 12{,}100$; half-year SI on it $= 12100 \times \frac{5}{100} = 605$ → ₹12,705.
(Compounded half-yearly instead? See the half-yearly pattern — different answer, different question.)

### Compounding more than once a year
- **Half-yearly**: rate halves, periods double: $A = P\left(1 + \frac{R}{200}\right)^{2T}$.
- **Quarterly**: rate quarters, periods quadruple: $A = P\left(1 + \frac{R}{400}\right)^{4T}$.
₹10,000 at 20% p.a. half-yearly for $1\frac{1}{2}$ years → 3 half-years at 10%: $10000 \times 1.1^3 = ₹13{,}310$.
More frequent compounding always gives more interest than annual compounding at the same nominal rate.

### Different rates in different years
Multiply the year-wise chips: $A = P\left(1+\frac{r_1}{100}\right)\left(1+\frac{r_2}{100}\right)\cdots$
₹25,000 with 10% then 20%: $25000 \times 1.1 \times 1.2 = ₹33{,}000$. A year of gain and a year of loss simply use their own chips.

### Scaling and finding P
CI is proportional to P (same rate and time): CI on ₹30,000 = 1.5 × CI on ₹20,000.
From an amount: divide by the chips. ₹6,655 after 3 years at 10% → $\frac{6655}{1.331} = ₹5{,}000$.

### Quick revision
- $A = P(1 + R/100)^T$; multiply chips T times.
- Net %: 2 years at 10% → 21%; at 20% → 44%; 3 years at 10% → 33.1%.
- Half-yearly: R/2, 2T. Quarterly: R/4, 4T.
- Broken period: full years by chips, then SI on the amount.
- Different yearly rates: multiply their chips.
"""

    S.pattern("int-c1", "Amount or CI by the multiplier method", "very common",
        "P, R and whole-year T are given; the amount or CI is asked.",
        r"A = P\left(1 + \frac{R}{100}\right)^T",
        r"""1. Write the chip $1 + \frac{R}{100}$ as a small fraction.
2. Multiply P by the chip T times.
3. CI = A − P.

Why: each year scales the running total by the same factor.""",
        "Find the compound interest on ₹12,000 at 10% per annum for 2 years.",
        r"$12000 \times \frac{11}{10} \times \frac{11}{10} = 14520$ → CI $= ₹2{,}520$. (SI would be ₹2,400.)")
    S.pattern("int-c2", "Net per cent / fraction-rate compounding", "very common",
        "'A sum becomes 1.21 times in 2 years' or 'CI as a per cent of P' — the net effect of compounding.",
        r"\text{net factor} = \left(1 + \frac{R}{100}\right)^2 = 1 + \frac{2R}{100} + \frac{R^2}{10000}",
        r"""1. Square the chip for 2 years, cube it for 3.
2. Read the percentage: 10% → 21%, 20% → 44%, 12.5% → 26.5625% ($\frac{81}{64}$).
3. For a given multiple, take the square root: 1.44 → chip 1.2 → 20%.

Why: compounding applies the same growth twice, so the effects multiply.""",
        "A sum invested at compound interest becomes 1.44 times itself in 2 years. The annual rate is:",
        r"Chip $= \sqrt{1.44} = 1.2$ → 20% per annum.")
    S.pattern("int-c3", "Half-yearly or quarterly compounding", "very common",
        "'Compounded half-yearly / quarterly' appears in the question — usually for $1$ to $2$ years.",
        r"A = P\left(1 + \frac{R}{200}\right)^{2T} = P\left(1 + \frac{R}{400}\right)^{4T}",
        r"""1. Halve (or quarter) the rate and double (quadruple) the number of periods.
2. Work the periods with chips as usual.
3. Watch $1\frac{1}{2}$ years: half-yearly means 3 periods.

Why: each compounding period uses the rate for that fraction of a year.""",
        "Find the CI on ₹10,000 at 20% per annum for 1½ years, compounded half-yearly.",
        r"3 half-years at 10%: $10000 \times 1.1^3 = 13310$ → CI $= ₹3{,}310$.")
    S.pattern("int-c4", "Different rates in different years", "common",
        "'8% in the first year and 10% in the second, compounded annually' — sometimes a loss year too.",
        r"A = P\left(1+\frac{r_1}{100}\right)\left(1+\frac{r_2}{100}\right)\cdots",
        r"""1. Write each year's own chip.
2. Multiply them all with P.
3. CI = A − P (or compare with another scenario).

Why: each year compounds on the running amount at its own rate.""",
        "₹25,000 is invested at 10% for the first year and 20% for the second, compounded annually. The amount is:",
        r"$25000 \times 1.1 \times 1.2 = ₹33{,}000$.")
    S.pattern("int-c5", "Scaling the CI (same rate, proportional principal)", "common",
        "The CI for one sum is given; the CI for another sum at the same rate and time is asked.",
        r"\frac{CI_2}{CI_1} = \frac{P_2}{P_1}",
        r"""1. CI is proportional to P at fixed rate and time.
2. Ratio the principals; scale the CI.
3. For a changed time, apply the net-per-cent of the new period instead.

Why: every term of the CI formula is linear in P.""",
        "The CI on ₹20,000 for 2 years at 10% is ₹4,200. The CI on ₹30,000 for the same period and rate is:",
        r"$4200 \times \frac{30}{20} = ₹6{,}300$.")

    A = 12000 * F(11, 10) ** 2
    assert A == 14520
    S.q("int-c1", "easy", "The compound interest on ₹12,000 at 10% per annum for 2 years, compounded annually, is:",
        ["₹2,520", "₹2,400", "₹2,640", "₹2,200"], rs(A - 12000),
        r"$12000 \times \frac{11}{10} \times \frac{11}{10} = 14520$ → CI $= 14520 - 12000 = ₹2{,}520$.",
        "₹2,400 is the simple interest — compounding adds ₹120 more.", 25)
    A = 8000 * F(23, 20) ** 2
    assert A == 10580
    S.q("int-c1", "medium", "Find the compound interest on ₹8,000 at 15% per annum for 2 years.",
        ["₹2,580", "₹2,400", "₹2,500", "₹2,700"], rs(A - 8000),
        r"$8000 \times \frac{23}{20} \times \frac{23}{20} = 10580$ → CI $= ₹2{,}580$.",
        r"Net $= 32.25\%$ (not 30%): $15 + 15 + 2.25$.", 30)
    A = 6250 * F(26, 25) ** 2
    assert A == 6760
    S.q("int-c2", "medium", "Find the compound interest on ₹6,250 at 4% per annum for 2 years.",
        ["₹510", "₹500", "₹525", "₹520"], rs(A - 6250),
        r"$4\% = \frac{1}{25}$ → $6250 \times \frac{26}{25} \times \frac{26}{25} = 6760$. CI $= ₹510$.",
        "₹500 is SI; the extra ₹10 is interest on the first year's interest.", 30)
    A = 20000 * F(9, 8) ** 2
    assert A - 20000 == F(10625, 2)
    ans = "₹5,312.50"
    S.q("int-c2", "hard", r"Find the compound interest on ₹20,000 at $12\frac{1}{2}\%$ per annum for 2 years.",
        [ans, "₹5,000", "₹5,400", "₹5,250"], ans,
        r"$12\frac{1}{2}\% = \frac{1}{8}$ → $20000 \times \frac{81}{64} = ₹25{,}312.50$. CI $= ₹5{,}312.50$.",
        r"Net factor $\frac{81}{64} = 1.265625$ → 26.5625% of 20,000.", 40)
    A = 10000 * F(11, 10) ** 3
    assert A == 13310
    S.q("int-c3", "easy",
        "Find the compound interest on ₹10,000 at 20% per annum for 1½ years, interest compounded half-yearly.",
        ["₹3,310", "₹3,200", "₹3,000", "₹3,410"], rs(A - 10000),
        r"Rate per half-year $= 10\%$, 3 periods → $10000 \times 1.1^3 = 13310$. CI $= ₹3{,}310$.",
        "₹3,000 treats it as one year at 20% plus simple half-year.", 30)
    A = 4000 * F(41, 40) ** 4
    assert abs(float(A - 4000) - 415.25) < 0.005
    ans = "₹415.25"
    S.q("int-c3", "hard",
        "Find the compound interest on ₹4,000 at 10% per annum for 1 year, compounded quarterly.",
        [ans, "₹400", "₹410", "₹420.50"], ans,
        r"4 quarters at $2.5\%$: $4000 \times \left(\frac{41}{40}\right)^4 = ₹4{,}415.25$. CI $= ₹415.25$.",
        "₹400 is the annual-compounding figure; quarterly always beats it.", 45)
    A = 25000 * F(11, 10) * F(6, 5)
    assert A == 33000
    S.q("int-c4", "easy",
        "A man invests ₹25,000 for two years, compounded annually. The rate is 10% for the first year and 20% for the second year. The amount he receives is:",
        ["₹33,000", "₹32,500", "₹30,250", "₹33,750"], rs(A),
        r"$25000 \times \frac{11}{10} \times \frac{6}{5} = ₹33{,}000$.",
        "₹32,500 averages the two rates — multiply the chips instead.", 30)
    A = 40000 * F(21, 20) * F(27, 25)
    assert A == 45360
    S.q("int-c4", "hard",
        "₹40,000 is invested at compound interest: 5% in the first year and 8% in the second year. The compound interest earned is:",
        ["₹5,360", "₹5,200", "₹5,600", "₹5,408"], rs(A - 40000),
        r"$40000 \times \frac{21}{20} \times \frac{27}{25} = ₹45{,}360$ → CI $= ₹5{,}360$.",
        "₹5,408 wrongly applies 8% to the interest earned in year one.", 40)
    S.q("int-c5", "medium",
        "The compound interest on ₹20,000 for 2 years at 10% per annum is ₹4,200. The compound interest on ₹30,000 for the same period at the same rate is:",
        ["₹6,300", "₹6,200", "₹6,600", "₹6,000"], "₹6,300",
        r"CI is proportional to P: $4200 \times \frac{30}{20} = ₹6{,}300$.",
        "₹6,600 would follow 3 × 2,200 (SI scaling) — keep the CI base 4,200.", 30)
    ci = 880 / F(44, 100) * F(3) * F(1, 5)
    assert ci == 1200
    S.q("int-c5", "hard",
        "The compound interest on a certain sum for 2 years at 20% per annum is ₹880. The compound interest on triple the sum for 1 year at the same rate is:",
        ["₹1,200", "₹1,320", "₹1,100", "₹1,440"], rs(ci),
        r"$CI = 44\%$ of P → $P = \frac{880}{0.44} = ₹2{,}000$. Triple sum $= ₹6{,}000$; 1 year at 20% → CI $= ₹1{,}200$.",
        "₹1,320 scales the 2-year figure — the new period is only 1 year.", 45)
    return S
