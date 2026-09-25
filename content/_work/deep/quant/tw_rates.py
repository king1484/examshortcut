"""Phase-2 deep content for quant/time-work — work rates + efficiency modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, mixed


def build_basics():
    S = Sub("tw-basics")

    S.notes = r"""### Work, time and rate
In these questions "work" means one whole job — building a wall, filling a tank, stitching shirts. The **rate** of a worker is the part of the job he finishes in one day (or one hour). If A finishes the whole job in T days, his rate is $\frac{1}{T}$ of the job per day. Two rules run the whole topic:

$$\text{Work done} = \text{rate} \times \text{time}, \qquad \text{rates add when people work together}$$

When two people work together, their rates simply add — each does his own bit every day. So the combined time is always **less than the fastest individual time**. If your answer is bigger, you added days instead of rates.

### The LCM method — whole numbers, no fractions
Fractions slow you down and cause sign slips. Instead, give the job a size in **units**: take the LCM of all the individual times.
A finishes in 15 days, B in 10 days. Let the job = 30 units (LCM of 15 and 10). A does $30 \div 15 = 2$ units a day, B does 3 units a day. Together $5$ units a day → $30 \div 5 = 6$ days. Every number here is a small whole number — that is the whole point of the method.

### Combining two workers
For exactly two workers with times a and b:
$$T = \frac{ab}{a + b}$$
Example: 6 and 12 days → $\frac{6 \times 12}{18} = 4$ days. This is the same as the LCM method — try it once to convince yourself, then use whichever is faster.
The reverse question is just as common: "A and B together take 6 days, A alone takes 10 — find B alone." Subtract the rates: $\frac{1}{6} - \frac{1}{10} = \frac{1}{15}$ → 15 days.

### Three or more workers
Add all three rates. A, B, C take 9, 12, 18 days: job = 36 units, rates $4 + 3 + 2 = 9$ a day → 4 days. As a formula, three workers take
$$T = \frac{abc}{ab + bc + ca}$$

### Pairwise data (A+B, B+C, A+C)
When the three pair-times are given, add the three pair-rates — each person's rate now appears **twice** — and halve:
$$\frac{1}{T_{AB}} + \frac{1}{T_{BC}} + \frac{1}{T_{AC}} = 2\left(\frac{1}{T_A} + \frac{1}{T_B} + \frac{1}{T_C}\right)$$
Pairs take 10, 12 and 15 days: sum of pair rates $= \frac{15}{60} = \frac14$ → trio rate $\frac18$ → all three together take 8 days. To find one person alone, subtract a pair from the trio: A = trio − (B+C).

### Partial work statements
"A can do $\frac{3}{5}$ of a work in 12 days." Scale to the whole job: full time $= 12 \times \frac{5}{3} = 20$ days. Convert every worker to a full-work time first, then combine as usual. With the LCM method this is equally quick: if the job is 35 units and A does 21 units in 12 days, his rate is $\frac{21}{12} = \frac74$ units a day.

### Common traps
- Adding the individual days (15 + 10 = 25) instead of the rates.
- In "together minus one" questions, subtracting the times instead of the rates.
- Partial work: scaling the days by the given fraction instead of its reciprocal.
- Forgetting the sanity check — a combined time must beat the best single time.

### Quick revision
- Rate = 1/time; rates add; Work = rate × time.
- Two workers: $T = \frac{ab}{a+b}$. Three: $T = \frac{abc}{ab+bc+ca}$.
- Together − A = B: subtract rates, never days.
- Pairwise times: add the three pair-rates, halve → trio rate.
- Partial work: full time = days × (reciprocal of fraction).
"""

    S.pattern("tw-p1", "Two workers together (or the reverse)", "very common",
        "Two individual completion times are given and the time together is asked — or the together time and one person's time are given and the other person's time is asked.",
        r"T = \frac{ab}{a + b}, \qquad \frac{1}{T_B} = \frac{1}{T_{A+B}} - \frac{1}{T_A}",
        r"""1. Take the job as LCM units, or write each rate as $\frac{1}{T}$.
2. Together: add the rates, then time = work ÷ combined rate.
3. Reverse: subtract one rate from the together rate to get the missing worker.

Why: each worker carries his own share of work every day, so rates add (or subtract).""",
        "A finishes a job in 15 days and B in 10 days. Working together, in how many days do they finish it?",
        r"Job = 30 units; rates 2 and 3 → 5/day → $30 \div 5 = 6$ days.")
    S.pattern("tw-p2", "Three or more workers together", "very common",
        "Three individual times are given (or two times plus the trio time) and the combined time — or one missing individual time — is asked.",
        r"\frac{1}{T} = \frac{1}{T_A} + \frac{1}{T_B} + \frac{1}{T_C}, \qquad T = \frac{abc}{ab+bc+ca}",
        r"""1. Job = LCM of the given times; find each rate in units per day.
2. Add the rates; divide the job by the total rate.
3. To find a missing rate, subtract the known rates from the trio rate.

Why: the whole job is split among the workers, so the daily shares add up to the trio's share.""",
        "A, B and C can do a piece of work in 9, 12 and 18 days respectively. In how many days will they finish it together?",
        r"Job = 36 units; rates $4 + 3 + 2 = 9$ a day → $36 \div 9 = 4$ days.")
    S.pattern("tw-p3", "Pairwise combination times", "common",
        "'A and B together take …, B and C together take …, A and C together take …' — the trio time or one person's time is asked.",
        r"\frac{1}{T_{ABC}} = \frac{1}{2}\left(\frac{1}{T_{AB}} + \frac{1}{T_{BC}} + \frac{1}{T_{AC}}\right)",
        r"""1. Convert the three pair-times to pair-rates.
2. Add all three: each worker's rate is counted twice, so halve the sum for the trio rate.
3. Any individual's rate = trio rate − the pair-rate not containing him.

Why: in the sum of the three pair-rates, A appears in two pairs, and so do B and C.""",
        "A and B can do a work in 10 days, B and C in 12 days, A and C in 15 days. In how many days will all three finish it together?",
        r"Pair rates: $\frac1{10}+\frac1{12}+\frac1{15} = \frac14$ → trio rate $\frac18$ → 8 days.")
    S.pattern("tw-p4", "Fractional / partial work statements", "common",
        "'A can do 3/5 of the work in 12 days', 'B does 2/7 of the work in 8 days' — the full-work time, or the together time, is asked.",
        r"\text{full time} = \text{days} \times \frac{\text{denominator}}{\text{numerator}}",
        r"""1. Scale each statement to the whole job: full time = days given × reciprocal of the fraction.
2. Combine the full-work times like any other question.
3. In LCM units, the rate is simply (units done) ÷ (days taken).

Why: a worker's rate is fixed, so completing only a fraction just means he worked on a smaller job for the given days.""",
        "A can do $\\frac{5}{6}$ of a work in 10 days and B can do $\\frac{3}{8}$ of the same work in 9 days. Working together, in how many days will they complete the work?",
        r"""A's full time $= 10 \times \frac65 = 12$ days; B's $= 9 \times \frac83 = 24$ days.
Together: $\frac1{12}+\frac1{24} = \frac18$ → 8 days.""")

    # ---- practice (tw-basics) ----
    assert F(30, 2 + 3) == 6
    S.q("tw-p1", "easy", "A can complete a piece of work in 15 days and B can complete it in 10 days. Working together, they will complete it in:",
        ["6 days", "5 days", "7 days", "8 days"], "6 days",
        r"LCM method: job $= 30$ units. A: 2 units/day, B: 3 units/day → 5 units/day → $\frac{30}{5} = 6$ days.",
        r"$\frac{15 \times 10}{15+10} = 6$ days.", 25)
    b = 1 / F(6) - 1 / F(10)
    assert F(1) / b == 15
    S.q("tw-p1", "easy",
        "A and B together can finish a work in 6 days. A alone can finish it in 10 days. B alone will finish it in:",
        ["15 days", "16 days", "12 days", "18 days"], "15 days",
        r"B's rate $= \frac{1}{6} - \frac{1}{10} = \frac{4}{60} = \frac{1}{15}$ → 15 days.",
        None, 30)
    assert F(36, 4 + 3 + 2) == 4
    S.q("tw-p2", "medium",
        "A, B and C can complete a piece of work in 9 days, 12 days and 18 days respectively. Working together, they will complete it in:",
        ["4 days", "5 days", "3 days", "$4\\frac{1}{2}$ days"], "4 days",
        r"Job $= 36$ units (LCM of 9, 12, 18). Rates: $4 + 3 + 2 = 9$ units/day → $\frac{36}{9} = 4$ days.",
        None, 35)
    c = 1 / F(6) - 1 / F(15) - 1 / F(20)
    assert F(1) / c == 20
    S.q("tw-p2", "hard",
        "A, B and C together can finish a work in 6 days. A alone can finish it in 15 days and B alone in 20 days. C alone will finish it in:",
        ["20 days", "25 days", "30 days", "40 days"], "20 days",
        r"C's rate $= \frac{1}{6} - \frac{1}{15} - \frac{1}{20} = \frac{10 - 4 - 3}{60} = \frac{3}{60} = \frac{1}{20}$ → 20 days.",
        "All three pair-numbers share LCM 60 — put everything over 60 in one line.", 45)
    assert 2 / (1 / F(10) + 1 / F(12) + 1 / F(15)) == 8
    S.q("tw-p3", "medium",
        "A and B together can do a piece of work in 10 days, B and C together in 12 days, and A and C together in 15 days. All three working together will finish it in:",
        ["8 days", "6 days", "9 days", "10 days"], "8 days",
        r"""Sum of pair rates $= \frac{1}{10} + \frac{1}{12} + \frac{1}{15} = \frac{6+5+4}{60} = \frac{1}{4}$.
Trio rate $= \frac{1}{2} \times \frac{1}{4} = \frac{1}{8}$ → 8 days.""",
        None, 45)
    a = 1 / F(10) - 1 / F(15)
    assert F(1) / a == 30
    S.q("tw-p3", "hard",
        "A and B together take 12 days, B and C together 15 days, and A and C together 20 days for the same work. A alone can do it in:",
        ["30 days", "24 days", "36 days", "20 days"], "30 days",
        r"""Trio rate $= \frac12\left(\frac1{12}+\frac1{15}+\frac1{20}\right) = \frac12 \times \frac{5+4+3}{60} = \frac{1}{10}$.
A $=$ trio $-(B+C) = \frac{1}{10} - \frac{1}{15} = \frac{1}{30}$ → 30 days.""",
        None, 55)
    t = F(1) / (1 / F(20) + 1 / F(28))
    assert t == F(35, 3)
    S.q("tw-p4", "medium",
        "A can do $\\frac{3}{5}$ of a work in 12 days and B can do $\\frac{2}{7}$ of the same work in 8 days. Working together, they will complete the work in:",
        ["12 days", "$10\\frac{2}{3}$ days", "13 days", "$11\\frac{2}{3}$ days"], mixed(t) + " days",
        r"""A's full-work time $= 12 \times \frac{5}{3} = 20$ days; B's $= 8 \times \frac{7}{2} = 28$ days.
Together: $\frac{1}{20} + \frac{1}{28} = \frac{7+5}{140} = \frac{3}{35}$ → $\frac{35}{3} = 11\frac{2}{3}$ days.""",
        None, 45)
    assert F(1) / (1 / F(12) + 1 / F(24)) == 8
    S.q("tw-p4", "medium",
        "A does $\\frac{5}{6}$ of a piece of work in 10 days, and B does $\\frac{3}{8}$ of the same work in 9 days. Working together, they finish the whole work in:",
        ["8 days", "9 days", "6 days", "10 days"], "8 days",
        r"""A's full-work time $= 10 \times \frac{6}{5} = 12$ days; B's $= 9 \times \frac{8}{3} = 24$ days.
Together: $\frac{1}{12} + \frac{1}{24} = \frac{1}{8}$ → 8 days.""",
        "Multiply the days by the reciprocal of the fraction — not by the fraction itself.", 40)
    return S


def build_eff():
    S = Sub("tw-efficiency")

    S.notes = r"""### Efficiency is rate with a comparison
"Efficient" here does not mean clever — it means **works faster**. Efficiency is another name for rate. The one relation to remember:

$$\frac{\text{efficiency of A}}{\text{efficiency of B}} = \frac{\text{time of B}}{\text{time of A}}$$

Efficiency and time are **inversely proportional**: twice as efficient → half the days. Three times as efficient → one-third of the days. Write every statement as a rate ratio before doing anything else.

### The unit trick for "k times as good"
If A is k times as efficient as B, let B do 1 unit a day and A do k units a day. Together $(k+1)$ units a day. If together they take T days, the whole job is $(k+1)T$ units, so:
$$\text{B alone} = (k+1)T \text{ days}, \qquad \text{A alone} = \frac{(k+1)T}{k} \text{ days}$$
A is twice as efficient as B; together 18 days → job $= 3 \times 18 = 54$ units → B alone 54 days, A alone 27. Notice B (the weaker worker) takes the longer time — if you assign 54 to A, you inverted the ratio.

### Efficiency given as a ratio
"A and B work in the ratio 3 : 2" — same idea. Rates $3u$ and $2u$; together $5u$. If the together time is 15 days, the job is $75u$, so B alone takes $\frac{75u}{2u} = 37.5$ days. If B's own time is given instead, first get u from it.

### "50% more efficient" and friends
Percentages become ratios at sight: 50% more efficient → ratio $3 : 2$; 25% more efficient → $5 : 4$; 20% less efficient → $4 : 5$. Then continue exactly as above. A is 50% more efficient than B and B takes 27 days → A's rate $= \frac{3}{2} \times \frac{1}{27} = \frac{1}{18}$; together $\frac{1}{18} + \frac{1}{27} = \frac{5}{54}$ → $10.8$ days.

### Days-difference questions
"A is twice as fast as B and finishes 12 days earlier." Times are $x$ and $2x$, and $2x - x = 12$, so A = 12, B = 24; together $\frac{12 \times 24}{36} = 8$ days. With ratio $a : b$ for A : B efficiency, times are in $b : a$ — set the difference equal to the given gap and everything falls out.

### Why the inverse rule never fails
Rate × time = 1 whole job (constant). If the rate is multiplied by k, the time must be divided by k for the product to stay 1. That is all "inversely proportional" means, and it is why scaling days in the wrong direction gives an impossible answer — the strongest worker always takes the fewest days.

### Common traps
- Reading "twice as efficient" as "twice the days" — efficiency and time move opposite ways.
- Giving the k-times worker $(k+1)T$ instead of $\frac{(k+1)T}{k}$ — that belongs to the weaker worker.
- Treating "25% more efficient" as a ratio of 25 : 100; it is 125 : 100 = 5 : 4.
- Mixing up whose time is longer in days-difference questions.

### Quick revision
- Efficiency ratio = rate ratio = inverse time ratio.
- k-times worker, together T days: weaker $(k+1)T$, stronger $\frac{(k+1)T}{k}$.
- 50% / 25% / 20% more efficient → 3:2 / 5:4 / 6:5.
- Days gap with times $bx$ and $ax$: $(b-a)x =$ gap.
- Sanity check: faster worker → fewer days, always.
"""

    S.pattern("tw-p5", "'k times as efficient', together time given", "very common",
        "'A is twice/thrice as efficient as B and together they finish in T days' — the individual times are asked.",
        r"T_B = (k+1)T, \qquad T_A = \frac{(k+1)T}{k}",
        r"""1. Let the weaker worker do 1 unit/day, the stronger k units/day.
2. Together $(k+1)$ units/day → whole job $= (k+1) \times T$ units.
3. Divide by each worker's own rate to get his days.

Why: the together time prices the job in units; each worker then spends those units at his own speed.""",
        "A is twice as efficient as B and together they complete a work in 18 days. B alone can complete it in:",
        r"Job $= (2+1) \times 18 = 54$ units → B alone 54 days (A alone 27 days).")
    S.pattern("tw-p6", "Efficiency ratio given as a : b", "common",
        "An explicit ratio like 3 : 2 or 4 : 5 is given for the efficiencies, with either the together time or one person's time.",
        r"\text{job} = (a + b) \times T \ (u), \quad T_{\text{weak}} = \frac{(a+b)T}{b}",
        r"""1. Fix rates $au$ and $bu$ per day.
2. From the given time, price the job in units.
3. Divide the job by the rate whose time is asked.

Why: a ratio is only a k-times statement written for both workers at once.""",
        "The efficiencies of A and B are in the ratio 3 : 2. B alone can finish the work in 30 days. Working together, they will finish it in:",
        r"B's rate $= \frac{1}{30} = 2u$ → $u = \frac{1}{60}$. Together $5u = \frac{5}{60} = \frac{1}{12}$ → 12 days.")
    S.pattern("tw-p7", "Efficiency ratio plus a gap of days", "common",
        "'A is twice as fast as B and takes 12 days less' — find either individual time or the together time.",
        r"b x - a x = \text{gap}, \text{ where times are } bx \text{ and } ax",
        r"""1. With efficiency ratio $a:b$, the times are in $b:a$ — call them $bx$ and $ax$.
2. Put the difference equal to the given gap and solve for x.
3. Now combine the two times with $\frac{ab}{a+b}$ if the together time is asked.

Why: the gap is a difference of two numbers in a known ratio, so one bracket pins both.""",
        "A is twice as fast a worker as B and takes 12 days less than B to finish a piece of work. Working together, they will finish it in:",
        r"""Times $x$ and $2x$: $2x - x = 12$ → A 12 days, B 24 days.
Together $= \frac{12 \times 24}{36} = 8$ days.""")
    S.pattern("tw-p8", "Percent more / less efficient", "occasional",
        "'A is 50% more efficient than B', 'A works 20% faster' — percentages of efficiency instead of a ratio.",
        r"a\% \text{ more efficient} \Rightarrow E_A : E_B = (100+a) : 100",
        r"""1. Convert to a ratio: 50% more → 3 : 2; 25% more → 5 : 4; 20% less → 4 : 5.
2. Continue with the unit method (price the job, then divide).

Why: "a% more efficient" means rate $= \left(1 + \frac{a}{100}\right) \times$ the other's rate.""",
        "A is 50% more efficient than B. B alone can finish a work in 27 days. Working together, they will finish it in about:",
        r"A's rate $= \frac{3}{2} \times \frac{1}{27} = \frac{1}{18}$. Sum $= \frac{1}{18} + \frac{1}{27} = \frac{5}{54}$ → $10.8$ days.")

    # ---- practice (tw-efficiency) ----
    assert 3 * 18 == 54 and (3 * 18) / 2 == 27
    S.q("tw-p5", "easy",
        "A is twice as efficient as B, and together they complete a work in 18 days. B alone can complete it in:",
        ["54 days", "36 days", "27 days", "72 days"], "54 days",
        r"Job $= (2+1) \times 18 = 54$ units → B alone $= 54$ days. (A alone $= 27$ days.)",
        "Weaker worker gets the LONGER time — $(k+1)T$ belongs to B.", 30)
    assert (4 * 12) / 3 == 16
    S.q("tw-p5", "easy",
        "A is thrice as efficient as B, and together they finish a work in 12 days. A alone will finish it in:",
        ["16 days", "48 days", "36 days", "24 days"], "16 days",
        r"Job $= (3+1) \times 12 = 48$ units. A alone $= \frac{48}{3} = 16$ days.",
        r"$\frac{(k+1)T}{k} = \frac{4 \times 12}{3} = 16$.", 30)
    assert 5 * 10 == 50
    S.q("tw-p5", "easy",
        "A is 4 times as efficient as B, and working together they complete a job in 10 days. B alone will complete it in:",
        ["50 days", "40 days", "12.5 days", "60 days"], "50 days",
        r"Job $= 5 \times 10 = 50$ units → B alone 50 days (A alone 12.5 days).",
        None, 30)
    assert F(75, 2) == F(75, 2)
    S.q("tw-p6", "medium",
        "The efficiencies of A and B are in the ratio 3 : 2, and together they finish a work in 15 days. B alone will finish it in:",
        ["37.5 days", "25 days", "22.5 days", "45 days"], "37.5 days",
        r"Rates $3u$ and $2u$ → job $= 5u \times 15 = 75u$. B alone $= \frac{75u}{2u} = 37.5$ days.",
        None, 40)
    assert F(1) / (3 / F(60) + 2 / F(60)) == 12
    S.q("tw-p6", "medium",
        "A and B work with efficiencies in the ratio 3 : 2. B alone can complete the work in 30 days. Working together, they will complete it in:",
        ["12 days", "18 days", "10 days", "15 days"], "12 days",
        r"B's rate $= \frac{1}{30} = 2u$ → $u = \frac{1}{60}$. Together $= 5u = \frac{1}{12}$ → 12 days.",
        None, 40)
    assert F(1) / (3 / F(80) + 2 / F(80)) == 16
    S.q("tw-p6", "medium",
        "The efficiencies of A and B are in the ratio 3 : 2. B alone takes 40 days for a piece of work. Working together, A and B will take:",
        ["16 days", "24 days", "20 days", "25 days"], "16 days",
        r"$2u = \frac{1}{40}$ → $u = \frac{1}{80}$; together rate $5u = \frac{5}{80} = \frac{1}{16}$ → 16 days.",
        None, 40)
    assert F(12 * 24, 36) == 8
    S.q("tw-p7", "medium",
        "A is twice as fast a worker as B and takes 12 days less than B for the same work. Working together, they will finish the work in:",
        ["8 days", "6 days", "9 days", "12 days"], "8 days",
        r"""Times: $x$ and $2x$ with $2x - x = 12$ → A = 12, B = 24.
Together $= \frac{12 \times 24}{12 + 24} = 8$ days.""",
        None, 45)
    assert F(100, 2) == 50
    S.q("tw-p7", "medium",
        "A works 1.5 times as fast as B (efficiencies 3 : 2). Together they finish a job in 20 days. B alone will finish it in:",
        ["50 days", "$33\\frac{1}{3}$ days", "30 days", "60 days"], "50 days",
        r"Together rate $= 5u = \frac{1}{20}$ → $u = \frac{1}{100}$. B's rate $= 2u = \frac{1}{50}$ → 50 days.",
        None, 45)
    assert F(1) / (1 / F(18) + 1 / F(54)) == F(27, 2)
    S.q("tw-p7", "medium",
        "A is thrice as fast as B, and B takes 36 days more than A to complete a piece of work. Working together, they will complete it in:",
        ["13.5 days", "12 days", "15 days", "18 days"], "13.5 days",
        r"""Times $x$ and $3x$: $3x - x = 36$ → $x = 18$ (A = 18, B = 54).
Together: $\frac{1}{18} + \frac{1}{54} = \frac{2}{27}$ → $13.5$ days.""",
        None, 50)
    assert F(54, 5) == F(54, 5)
    S.q("tw-p8", "medium",
        "A is 50% more efficient than B. B alone can complete a work in 27 days. Working together, they will complete it in:",
        ["10.8 days", "13.5 days", "12 days", "16.2 days"], "10.8 days",
        r"Ratio $3:2$. A's rate $= \frac{3}{2} \times \frac{1}{27} = \frac{1}{18}$; sum $= \frac{1}{18} + \frac{1}{27} = \frac{5}{54}$ → $10.8$ days.",
        None, 45)
    assert F(80, 3) == F(80, 3)
    S.q("tw-p8", "hard",
        "A is 25% more efficient than B and therefore takes 12 days less than B for the same work. Working together, they will finish the work in:",
        ["$26\\frac{2}{3}$ days", "30 days", "24 days", "28 days"], mixed(F(80, 3)) + " days",
        r"""Ratio $5:4$ → times $4x$ and $5x$ with $5x - 4x = 12$ → B = 60, A = 48.
Together: $\frac{48 \times 60}{108} = \frac{80}{3} = 26\frac{2}{3}$ days.""",
        None, 55)
    return S
