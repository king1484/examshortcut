"""Phase-2 deep content for quant/ratio-proportion — money applications module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_money():
    S = Sub("rp-money-applications")
    S.notes = r"""### Income–expenditure–savings (two ratios)
Incomes in ratio $a : b$ and expenditures in ratio $p : q$ → write incomes $= ax, bx$ and expenditures $= py, qy$. **Two different multipliers** — that is the trap. Savings give one linear equation per person:
$$ax - py = s_1, \qquad bx - qy = s_2.$$
Subtract the equations (equal savings make the right sides cancel) or solve by elimination; then build any income, expenditure or saving.
Keep the arithmetic in fractions and it stays two lines. Always sanity-check both savings come out positive.

### Coin and denomination bags
Coins of denominations $d_1, d_2, d_3$ in ratio $n_1 : n_2 : n_3$: price ONE full set,
$$\text{set value} = n_1d_1 + n_2d_2 + n_3d_3,$$
then number of sets = total value ÷ set value. Count of a coin = its ratio term × sets. Convert everything to paise (or everything to rupees) first — ₹1 = 100 paise.

### Wages in proportion to work
Fair division follows work done. Days worked → shares ∝ days. Working together → shares ∝ **work rates** ($\frac{1}{\text{days}}$), not the days themselves: workers finishing alone in 6 and 9 days earn in ratio $\frac{1}{6} : \frac{1}{9} = 3 : 2$.

### Chained ratios on money
"A = 3/4 of B, B = 4/5 of C" → convert to a common base: $A : B : C = 3 : 4 : 5$. Then any total or share is plain part-division. Whenever two linked fractions appear, build the three-term ratio before touching the money.

### A complete income–expenditure walkthrough
"Incomes 5 : 4, expenditures 3 : 2, each saves ₹1,600."
1. Incomes $5x, 4x$; expenditures $3y, 2y$ — note the two different letters.
2. $5x - 3y = 1600$ and $4x - 2y = 1600$.
3. Equal savings → subtract the equations: $(5x - 4x) - (3y - 2y) = 0$, i.e. $x - y = 0$, so $x = y$.
4. Substitute: $5x - 3x = 1600$ → $x = 800$. Incomes ₹4,000 and ₹3,200; expenditures ₹2,400 and ₹1,600 — both savings check out at ₹1,600 ✓.
With equal savings, the subtraction step is what makes the question short; with unequal savings, eliminate y by cross-multiplying the two equations.

### Money-ratio hygiene
- Convert paise/rupees and hours/minutes before forming any ratio.
- Answer what is asked: coin COUNT vs coin VALUE, income vs expenditure — the options always carry both.
- Check plausibility: savings must come out positive for everyone; a negative y means the equations were set up with swapped multipliers.

### Quick revision
- Incomes and expenditures take different multipliers x and y.
- Subtract savings equations to eliminate.
- Coin bags: price one set, divide, multiply.
- Wages together ∝ 1/days each.
"""

    S.pattern("rp-c1", "Income–expenditure–savings ratios", "very common",
        "Two income ratios, two expenditure ratios, savings given — find an income or expenditure.",
        r"ax - py = s_1, \quad bx - qy = s_2",
        r"""1. Incomes = ax, bx; expenditures = py, qy (different letters!).
2. Write both savings equations.
3. Equal savings → subtract the equations to kill the constant; else eliminate y by cross-multiplying.

Why: two ratios plus two savings give exactly two linear equations in x and y.""",
        "The incomes of A and B are in the ratio 9 : 7 and their expenditures in the ratio 4 : 3. If each saves ₹2,000, A's income is:",
        r"$9x - 4y = 2000$, $7x - 3y = 2000$ → subtract: $2x = y$. Then $9x - 8x = 2000$ → x = 2000 → A $= ₹18{,}000$.")
    S.pattern("rp-c2", "Coin denominations in a ratio", "common",
        "Bags of ₹1/50p/25p (or ₹5/₹2/₹1) coins in a ratio with the total value given; find a coin count or the total.",
        r"\text{set value} = \sum n_i d_i, \quad \text{sets} = \frac{\text{total value}}{\text{set value}}",
        r"""1. Convert all values to ONE unit (paise or rupees).
2. Price one full set of coins in the given ratio.
3. Divide the total value by the set value → sets; multiply back for counts.

Why: the ratio fixes how many full sets the bag contains — the set is the repeating block.""",
        "A bag contains ₹1, 50-paise and 25-paise coins in the ratio 5 : 8 : 4, amounting to ₹210. The number of 50-paise coins is:",
        r"Set $= 500 + 400 + 100 = 1000$ paise = ₹10 → 21 sets → 50p coins $= 8 \times 21 = 168$.")
    S.pattern("rp-c3", "Money shared in proportion to work or linked ratios", "common",
        "Wages divided in proportion to work/days; or shares linked by 'A = 3/4 of B, B = 4/5 of C'.",
        r"\text{wage} \propto \text{work done}, \quad \text{together} \propto \frac{1}{\text{days alone}}",
        r"""1. Convert the story into one common ratio (days, or 1/days when working together).
2. Add the parts; one part = money ÷ parts.
3. For chains like A = (3/4)B = (3/4)(4/5)C, build A : B : C first.

Why: fair division always reduces to a three-term ratio on a common base.""",
        "Two workers, working alone, can finish a job in 6 days and 9 days. They work together and earn ₹1,500. The first worker's share is:",
        r"Rates: $\frac{1}{6} : \frac{1}{9} = 3 : 2$ → share $= \frac{3}{5} \times 1500 = ₹900$.")

    assert 18000 // 9 == 2000
    S.q("rp-c1", "medium",
        "The incomes of A and B are in the ratio 9 : 7 and their expenditures in the ratio 4 : 3. If each saves ₹2,000, then A's income is:",
        ["₹18,000", "₹14,000", "₹16,000", "₹20,000"], "₹18,000",
        r"""Incomes 9x, 7x; expenditures 4y, 3y.
$9x - 4y = 2000$ and $7x - 3y = 2000$ → subtract: $2x - y = 0$ → $y = 2x$.
Then $9x - 8x = 2000$ → x = 2000 → A's income $= ₹18{,}000$.""",
        None, 55)
    assert 5 * 800 - 3 * 800 == 1600 and 4 * 800 - 2 * 800 == 1600
    S.q("rp-c1", "hard",
        "The incomes of A and B are in the ratio 5 : 4 and their expenditures in the ratio 3 : 2. If each saves ₹1,600, then B's expenditure is:",
        ["₹1,600", "₹2,400", "₹1,200", "₹3,200"], "₹1,600",
        r"""$5x - 3y = 1600$ and $4x - 2y = 1600$ → from the second, $y = 2x - 800$.
Substitute: $5x - 6x + 2400 = 1600$ → $x = 800$ → $y = 800$.
B's expenditure $= 2y = ₹1{,}600$.""",
        None, 60)
    assert 3 * 12000 - 2 * 15000 == 6000 and 4 * 12000 - 3 * 15000 == 3000
    S.q("rp-c1", "hard",
        "The incomes of A and B are in the ratio 3 : 4 and their expenditures in the ratio 2 : 3. If A saves ₹6,000 and B saves ₹3,000, then A's income is:",
        ["₹36,000", "₹30,000", "₹42,000", "₹24,000"], "₹36,000",
        r"""$3x - 2y = 6000$ and $4x - 3y = 3000$.
Multiply the first by 3 and the second by 2: $9x - 6y = 18000$, $8x - 6y = 6000$ → subtract: $x = 12000$.
A's income $= 3 \times 12000 = ₹36{,}000$.""",
        None, 60)
    assert 210 // 10 == 21 and 8 * 21 == 168
    S.q("rp-c2", "easy",
        "A bag contains ₹1, 50-paise and 25-paise coins in the ratio 5 : 8 : 4, amounting to ₹210 in all. The number of 50-paise coins is:",
        ["168", "140", "105", "84"], "168",
        r"""One set $= 500 + 400 + 100 = 1000$ paise $= ₹10$.
Sets $= \frac{210}{10} = 21$ → 50-paise coins $= 8 \times 21 = 168$.""",
        None, 40)
    assert 882 != 32 * 27 and 512 // 32 == 16 and (3 + 5 + 7) * 16 == 240
    S.q("rp-c2", "medium",
        "A box contains ₹5, ₹2 and ₹1 coins in the ratio 3 : 5 : 7, amounting to ₹512 in all. The total number of coins is:",
        ["240", "220", "256", "208"], "240",
        r"""One set $= 15 + 10 + 7 = ₹32$ → sets $= \frac{512}{32} = 16$.
Coins per set $= 3 + 5 + 7 = 15$ → total $= 15 \times 16 = 240$.""",
        None, 45)
    assert round(103 / 5.15, 6) == 20.0 and 4 * 20 == 80
    S.q("rp-c2", "hard",
        "A bag contains 50-paise, 25-paise and 10-paise coins in the ratio 5 : 9 : 4, amounting to ₹103 in all. The number of 10-paise coins is:",
        ["80", "100", "60", "90"], "80",
        r"""One set $= 250 + 225 + 40 = 515$ paise $= ₹5.15$.
Sets $= \frac{103}{5.15} = 20$ → 10-paise coins $= 4 \times 20 = 80$.""",
        None, 55)
    assert 1200 // 10 == 120 and 5 * 120 == 600
    S.q("rp-c3", "easy",
        "₹1,200 is divided among three workers in proportion to the number of days each worked: 2 days, 3 days and 5 days. The share of the third worker is:",
        ["₹600", "₹480", "₹360", "₹540"], "₹600",
        r"""Ratio $= 2 : 3 : 5$ (10 parts) → 1 part $= ₹120$.
Third worker $= 5 \times 120 = ₹600$.""",
        None, 30)
    assert abs((1 / 6) / (1 / 9) - 1.5) < 1e-9 and 1500 // 5 == 300
    S.q("rp-c3", "medium",
        "Working alone, two workers can finish a job in 6 days and 9 days respectively. They work together and receive ₹1,500 for the job. The first worker's share is:",
        ["₹900", "₹750", "₹600", "₹1,000"], "₹900",
        r"""Shares follow work rate: $\frac{1}{6} : \frac{1}{9} = 3 : 2$.
First worker $= \frac{3}{5} \times 1500 = ₹900$.""",
        None, 45)
    assert 2550 // 17 == 150 and 10 * 150 == 1500
    S.q("rp-c3", "medium",
        "A sum of ₹2,550 is divided among A, B and C such that A : B = 3 : 4 and B : C = 2 : 5. C's share is:",
        ["₹1,500", "₹1,200", "₹600", "₹750"], "₹1,500",
        r"""Bridge B: A : B = 3 : 4, B : C = 2 : 5 → A : B : C $= 3 : 4 : 10$ (17 parts).
C $= \frac{10}{17} \times 2550 = ₹1{,}500$.""",
        None, 45)
    S.q("rp-c3", "hard",
        "A's salary is three-fourths of B's salary, and B's salary is four-fifths of C's. If the total salary of the three is ₹7,200, then C's salary is:",
        ["₹3,000", "₹2,400", "₹2,880", "₹3,200"], "₹3,000",
        r"""Let C = 20 → B = 16 → A = 12 → $A : B : C = 12 : 16 : 20 = 3 : 4 : 5$.
C $= \frac{5}{12} \times 7200 = ₹3{,}000$.""",
        None, 50)
    S.pattern("rp-c4", "Condition-driven division ('half of', 'twice of')", "common",
        "'A gets twice as much as B', 'the first gets half of the second' — shares defined by statements, not by a stated ratio.",
        r"\text{translate each statement into a multiple}, \ \text{then read off } A : B : C",
        r"""1. Let the LAST person hold x (or 1 part).
2. Translate each statement into multiples of that part.
3. Read the ratio, add parts, divide the total.

Why: chain statements fix the mutual multiples; taking the last person as the base untangles them in one pass.""",
        "₹918 is divided among three friends such that the first gets half of the second and the second gets two-thirds of the third. The first friend's share is:",
        r"Let the third = 3 → second = 2 → first = 1 → ratio $1 : 2 : 3$ → first $= \frac{918}{6} = ₹153$.")

    assert 1400 // 7 == 200
    S.q("rp-c4", "easy",
        "₹1,400 is divided among A, B and C such that A gets twice as much as B, and B gets twice as much as C. C's share is:",
        ["₹200", "₹400", "₹100", "₹350"], "₹200",
        r"""$A : B : C = 4 : 2 : 1$ (7 parts) → C $= \frac{1400}{7} = ₹200$.""",
        None, 35)
    assert 918 // 6 == 153
    S.q("rp-c4", "medium",
        "A sum of ₹918 is divided among three friends such that the first gets half of what the second gets, and the second gets two-thirds of what the third gets. The first friend's share is:",
        ["₹153", "₹306", "₹459", "₹102"], "₹153",
        r"""Take the third = 3 → second $= \frac{2}{3} \times 3 = 2$ → first $= 1$.
Ratio $1 : 2 : 3$ → first $= \frac{1}{6} \times 918 = ₹153$.""",
        None, 45)
    return S
