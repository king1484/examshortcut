from fractions import Fraction as F
from _lib import Sub, fr, rs


def rec(s):
    """'3.1(45)' -> Fraction for 3.1454545..."""
    whole, dec = s.split(".")
    if "(" in dec:
        pre, rep = dec.rstrip(")").split("(")
    else:
        pre, rep = dec, ""
    val = F(int(whole))
    if pre:
        val += F(int(pre), 10 ** len(pre))
    if rep:
        val += F(int(rep), (10 ** len(rep) - 1) * 10 ** len(pre))
    return val


def rtex(s):
    """'3.1(45)' -> $3.1\\overline{45}$"""
    if "(" in s:
        a, b = s.rstrip(")").split("(")
        return f"${a}\\overline{{{b}}}$"
    return f"${s}$"


def terminates(x):
    d = F(x).denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


def build():
    S = Sub("ns-fractions-decimals")
    S.notes = r"""### Fractions in one line
A **fraction** $\frac{p}{q}$ means $p$ parts out of $q$ equal parts. $p$ is the numerator (top), $q$ the denominator (bottom, never 0). $\frac{3}{4}$ of ₹200 is ₹150.
- **Proper fraction**: top < bottom ($\frac{3}{7}$). **Improper**: top ≥ bottom ($\frac{9}{4}$). **Mixed**: $2\frac{1}{4} = \frac{9}{4}$.
- **Lowest terms**: divide top and bottom by their HCF. $\frac{21}{168} = \frac{1}{8}$.

### Decimals: terminating and recurring
Divide the top by the bottom. Two things can happen:
- The division **stops**: $\frac{7}{80} = 0.0875$ → a **terminating** decimal.
- The digits **repeat forever**: $\frac{1}{3} = 0.333\dots = 0.\overline{3}$ → a **recurring** decimal. The bar shows the repeating block.

**Terminating test.** First reduce the fraction to lowest terms. It terminates only if the denominator has **no prime factor other than 2 and 5**.
- $\frac{7}{80}$: $80 = 2^4 \times 5$ → terminates.
- $\frac{11}{48}$: $48 = 2^4 \times 3$ → recurring (because of 3).
- $\frac{21}{168}$ looks like it has 3 and 7 in the bottom, but it reduces to $\frac{1}{8}$ → terminates. Always reduce first!

### Recurring decimal to fraction
**Pure recurring** (repeats right after the point): write the repeating digits over as many 9s.
$0.\overline{7} = \frac{7}{9}$, $0.\overline{72} = \frac{72}{99} = \frac{8}{11}$, $0.\overline{142857} = \frac{142857}{999999} = \frac{1}{7}$.

**Mixed recurring** (some digits do not repeat): numerator = (all digits after the point) − (non-repeating digits); denominator = one 9 for each repeating digit, then one 0 for each non-repeating digit.
$0.4\overline{7} = \frac{47 - 4}{90} = \frac{43}{90}$, $0.2\overline{45} = \frac{245 - 2}{990} = \frac{243}{990}$.

**With a whole number**: handle the whole part separately. $3.1\overline{45} = 3 + \frac{145 - 1}{990} = 3 + \frac{8}{55} = \frac{173}{55}$.

Why the 9s? $x = 0.\overline{7}$ → $10x = 7.\overline{7}$ → $10x - x = 7$ → $x = \frac{7}{9}$.

### Adding recurring decimals
Convert each to a fraction, add, and convert back if the options are decimals. $0.\overline{6} + 0.\overline{7} + 0.\overline{8} = \frac{6+7+8}{9} = \frac{21}{9} = 2.\overline{3}$ — not 2.1! Adding digits directly is the classic trap.

### Comparing fractions
- **Cross-multiplication** for two fractions: $\frac{5}{8}$ vs $\frac{7}{11}$ → $5 \times 11 = 55$ vs $8 \times 7 = 56$ → $\frac{7}{11}$ is bigger.
- **Decimal method**: convert each to 3 decimal places.
- **Complement method**: when all fractions are close to 1, compare the gap from 1. $\frac{13}{17}$ is $\frac{4}{17}$ short of 1; $\frac{9}{11}$ is $\frac{2}{11}$ short. The bigger the gap, the smaller the fraction.
- Same numerators: the smaller denominator gives the bigger fraction.

### Fraction word problems
"$\frac{3}{5}$ of a number is 63 more than $\frac{1}{4}$ of it" → $(\frac{3}{5} - \frac{1}{4})x = 63$ → $\frac{7}{20}x = 63$ → $x = 180$.
For "spends $\frac{1}{3}$, then $\frac{1}{4}$ of the **remaining**" questions, take fractions of what is left, not of the whole.

### Quick revision
- Terminating ⇔ reduced denominator has only 2s and 5s.
- Pure recurring: digits / 9s. Mixed: (all − non-repeating) / (9s then 0s).
- Convert to fractions before adding recurring decimals.
- Compare by cross-multiplying, decimals or complements.
- "Of the remaining" → multiply fractions step by step.
"""

    S.pattern("ns-fd-p1", "Recurring decimal to fraction", "very common",
        r"A decimal with a bar, like $0.\overline{72}$ or $3.1\overline{45}$, and fractions in the options.",
        r"0.a\overline{bc} = \frac{abc - a}{990}",
        r"""1. Separate the whole number part.
2. Numerator: all digits after the point minus the non-repeating digits.
3. Denominator: one 9 per repeating digit, then one 0 per non-repeating digit.
4. Simplify and add the whole part back.

Why: multiplying by powers of 10 and subtracting cancels the endless repeating tail.""",
        r"Write $0.3\overline{8}$ as a fraction.",
        r"$\frac{38 - 3}{90} = \frac{35}{90} = \frac{7}{18}$.")
    S.pattern("ns-fd-p2", "Sum or difference of recurring decimals", "common",
        r"Two or three barred decimals added or subtracted, e.g. $0.\overline{6} + 0.\overline{7} + 0.\overline{8}$.",
        None,
        r"""1. Convert each decimal to a fraction (use a common denominator like 9, 90, 99).
2. Add or subtract the fractions.
3. Convert back to the form used in the options.

Why: recurring decimals cannot be added digit by digit because the carry keeps coming from the endless tail.""",
        r"Find $0.\overline{5} + 0.\overline{4}$.",
        r"$\frac{5}{9} + \frac{4}{9} = \frac{9}{9} = 1$. (Not 0.9!)")
    S.pattern("ns-fd-p3", "Terminating or non-terminating decimal test", "common",
        "'Which of the following fractions will give a terminating decimal?' (or non-terminating).",
        r"\frac{p}{q} \text{ (lowest terms) terminates} \iff q = 2^m 5^n",
        r"""1. Reduce every fraction to lowest terms.
2. Factorise the denominator.
3. Only 2s and 5s → terminating; any other prime → recurring.

Why: $10 = 2 \times 5$, so only such denominators can be turned into a power of 10.""",
        r"Does $\frac{27}{120}$ terminate?",
        r"$\frac{27}{120} = \frac{9}{40}$ and $40 = 2^3 \times 5$ → yes, it terminates ($0.225$).")
    S.pattern("ns-fd-p4", "Comparing and ordering fractions", "very common",
        "'Which is the largest/smallest fraction?' or 'arrange in ascending order'.",
        r"\frac{a}{b} > \frac{c}{d} \iff ad > bc \ (b, d > 0)",
        r"""1. Two at a time: cross-multiply.
2. Many fractions: convert to decimals (3 places) or use the complement from 1 when all are close to 1.
3. Check the order asked (ascending = smallest first).

Why: cross-multiplying is the same as putting both fractions over the common denominator $bd$.""",
        r"Which is larger: $\frac{7}{9}$ or $\frac{11}{14}$?",
        r"$7 \times 14 = 98$, $9 \times 11 = 99$. $98 < 99$ → $\frac{11}{14}$ is larger.")
    S.pattern("ns-fd-p5", "Fraction of a quantity (word problems)", "common",
        "'3/5 of a number exceeds 1/4 of it by 63', 'spends 1/3 on rent and 1/4 of the remaining on food …'.",
        r"\text{part} = \text{fraction} \times \text{whole}",
        r"""1. Let the whole be $x$.
2. Translate each sentence into a fraction of $x$ (fractions of the **remaining** are multiplied).
3. Equate the known part to its value and solve.

Why: every part is a fixed fraction of the whole, so one known part fixes the whole.""",
        r"$\frac{2}{3}$ of a number is 48. What is $\frac{3}{4}$ of the number?",
        r"Number $= 48 \times \frac{3}{2} = 72$. $\frac{3}{4} \times 72 = 54$.")

    # p1
    v = rec("0.(72)")
    assert v == F(8, 11)
    S.q("ns-fd-p1", "easy", r"The value of $0.\overline{72}$ as a fraction in lowest terms is:",
        [fr(F(8, 11)), fr(F(18, 25)), fr(F(7, 9)), fr(F(73, 99))], fr(v),
        r"$0.\overline{72} = \frac{72}{99} = \frac{8}{11}$ (divide top and bottom by 9).",
        r"$\frac{18}{25} = 0.72$ exactly — that is the non-recurring trap.", 30)
    v = rec("3.1(45)")
    assert v == F(173, 55) and rec("3.(14)") == F(311, 99)
    S.q("ns-fd-p1", "medium", r"Express $3.1\overline{45}$ as a fraction.",
        [fr(F(173, 55)), fr(F(311, 99)), fr(F(3113, 990)), fr(F(157, 50))], fr(v),
        r"""Whole part 3. Decimal part $0.1\overline{45}$: numerator $= 145 - 1 = 144$, denominator $= 990$ (two 9s for '45', one 0 for '1').
$\frac{144}{990} = \frac{8}{55}$. So $3.1\overline{45} = 3 + \frac{8}{55} = \frac{173}{55}$.""",
        None, 50)

    # p2
    v = rec("0.(6)") + rec("0.(7)") + rec("0.(8)")
    assert v == F(7, 3) == rec("2.(3)")
    opts = ["2.(3)", "2.1", "2.(1)", "2.(2)"]
    assert [o for o in opts if rec(o) == v] == ["2.(3)"]
    S.q("ns-fd-p2", "easy", r"What is the value of $0.\overline{6} + 0.\overline{7} + 0.\overline{8}$?",
        [rtex(o) for o in opts], rtex("2.(3)"),
        r"$\frac{6}{9} + \frac{7}{9} + \frac{8}{9} = \frac{21}{9} = \frac{7}{3} = 2.\overline{3}$.",
        "Adding digits (6 + 7 + 8 = 21 → 2.1) ignores the carries from the endless tail.", 35)
    v = rec("0.4(7)") + rec("0.3(5)")
    assert v == F(5, 6)
    opts = [fr(F(5, 6)), rtex("0.8(2)"), fr(F(82, 99)), fr(F(83, 90))]
    assert rec("0.8(2)") != v and F(82, 99) != v and F(83, 90) != v
    S.q("ns-fd-p2", "hard", r"What is the value of $0.4\overline{7} + 0.3\overline{5}$?",
        opts, fr(v),
        r"""$0.4\overline{7} = \frac{47 - 4}{90} = \frac{43}{90}$ and $0.3\overline{5} = \frac{35 - 3}{90} = \frac{32}{90}$.
Sum $= \frac{75}{90} = \frac{5}{6}$ ($= 0.8\overline{3}$).""",
        None, 60)

    # p3
    cands = [F(7, 80), F(3, 14), F(11, 45), F(13, 24)]
    assert [c for c in cands if terminates(c)] == [F(7, 80)]
    S.q("ns-fd-p3", "easy", "Which of the following fractions can be written as a terminating decimal?",
        [fr(c) for c in cands], fr(F(7, 80)),
        r"$80 = 2^4 \times 5$ has only 2s and 5s, so $\frac{7}{80} = 0.0875$ terminates. The others have 7 ($14$), 3 ($45$, $24$) in the denominator.",
        None, 30)
    labels = [(r"$\frac{21}{168}$", F(21, 168)), (r"$\frac{33}{60}$", F(33, 60)), (r"$\frac{17}{125}$", F(17, 125)), (r"$\frac{11}{48}$", F(11, 48))]
    nonterm = [l for l, x in labels if not terminates(x)]
    assert nonterm == [r"$\frac{11}{48}$"]
    S.q("ns-fd-p3", "medium", "Which of the following fractions gives a NON-terminating (recurring) decimal?",
        [l for l, _ in labels], nonterm[0],
        r"""Reduce first:
- $\frac{21}{168} = \frac{1}{8}$ → terminates.
- $\frac{33}{60} = \frac{11}{20}$ → terminates.
- $\frac{17}{125}$, $125 = 5^3$ → terminates.
- $\frac{11}{48}$, $48 = 2^4 \times 3$ → **recurring** (factor 3).""",
        "Reduce before judging: 168 contains 3 and 7, but 21/168 = 1/8.", 45)

    # p4
    c = [F(3, 5), F(5, 8), F(7, 11), F(9, 14)]
    assert max(c) == F(9, 14)
    S.q("ns-fd-p4", "easy", "Which of the following fractions is the largest?",
        [fr(x) for x in c], fr(max(c)),
        r"Decimals: $\frac{3}{5} = 0.600$, $\frac{5}{8} = 0.625$, $\frac{7}{11} \approx 0.636$, $\frac{9}{14} \approx 0.643$. Largest $= \frac{9}{14}$.",
        r"Complements: $\frac{2}{5}, \frac{3}{8}, \frac{4}{11}, \frac{5}{14}$ = 0.40, 0.375, 0.364, 0.357. Smallest gap → largest fraction → $\frac{9}{14}$.", 45)
    c = [F(2, 3), F(5, 7), F(7, 10), F(11, 15)]
    order = sorted(c)
    assert order == [F(2, 3), F(7, 10), F(5, 7), F(11, 15)]
    txt = lambda seq: " < ".join(fr(x).strip("$") for x in seq)
    right = "$" + txt(order) + "$"
    wrongs = ["$" + txt([F(2, 3), F(5, 7), F(7, 10), F(11, 15)]) + "$",
              "$" + txt([F(7, 10), F(2, 3), F(5, 7), F(11, 15)]) + "$",
              "$" + txt([F(2, 3), F(7, 10), F(11, 15), F(5, 7)]) + "$"]
    S.q("ns-fd-p4", "medium", r"Arrange in ascending order: $\frac{2}{3}, \frac{5}{7}, \frac{7}{10}, \frac{11}{15}$.",
        [right] + wrongs, right,
        r"Decimals: $\frac{2}{3} \approx 0.667$, $\frac{7}{10} = 0.700$, $\frac{5}{7} \approx 0.714$, $\frac{11}{15} \approx 0.733$. Ascending: $\frac{2}{3} < \frac{7}{10} < \frac{5}{7} < \frac{11}{15}$.",
        None, 60)
    c = [F(13, 17), F(11, 14), F(15, 19), F(9, 11)]
    assert min(c) == F(13, 17)
    S.q("ns-fd-p4", "medium", "Which of the following fractions is the smallest?",
        [fr(x) for x in c], fr(min(c)),
        r"Gaps from 1: $\frac{4}{17} \approx 0.235$, $\frac{3}{14} \approx 0.214$, $\frac{4}{19} \approx 0.211$, $\frac{2}{11} \approx 0.182$. The biggest gap belongs to $\frac{13}{17}$, so it is the smallest.",
        "Complement method: biggest shortfall from 1 = smallest fraction.", 45)

    # p5
    x = F(63) / (F(3, 5) - F(1, 4))
    assert x == 180
    S.q("ns-fd-p5", "easy", r"$\frac{3}{5}$ of a number is 63 more than $\frac{1}{4}$ of the number. What is the number?",
        ["180", "150", "210", "240"], str(x),
        r"$\left(\frac{3}{5} - \frac{1}{4}\right)x = 63 \Rightarrow \frac{7}{20}x = 63 \Rightarrow x = 180$.",
        r"Check: $\frac{3}{5} \times 180 = 108$, $\frac{1}{4} \times 180 = 45$, difference 63 ✓.", 40)
    rest = 1 - F(1, 3) - F(1, 4) * (1 - F(1, 3))
    sal = F(9000) / rest
    assert rest == F(1, 2) and sal == 18000
    S.q("ns-fd-p5", "medium", r"Ravi spends $\frac{1}{3}$ of his salary on rent and $\frac{1}{4}$ of the remaining on food. He saves the rest, which is ₹9,000. What is his salary?",
        [rs(18000), rs(21600), rs(15000), rs(24000)], rs(int(sal)),
        r"""After rent, $\frac{2}{3}$ is left. Food $= \frac{1}{4} \times \frac{2}{3} = \frac{1}{6}$ of the salary.
Savings $= 1 - \frac{1}{3} - \frac{1}{6} = \frac{1}{2}$ of the salary $= ₹9,000$.
Salary $= ₹18,000$.""",
        r"Trap ₹21,600: taking $\frac{1}{4}$ of the whole salary gives savings $\frac{5}{12}$.", 50)
    return S
