"""Phase-2 deep content for quant/time-work — joining/leaving, alternate days, wages."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, mixed


def build_cases():
    S = Sub("tw-cases")

    S.notes = r"""### One method: count the work actually done
Every "twist" question in this family — someone leaves, someone joins late, people work on alternate days, wages are divided — is solved the same way. Put the job in LCM units, write each worker's rate per day, then **add up the work each worker actually did** and set the total equal to the whole job.

### A leaves after t days
A can do the job in $T_A$ days and works only t days: he completes $\frac{t}{T_A}$ of it. The rest, $1 - \frac{t}{T_A}$, is finished by whoever continues — alone or in a team — at their own rate. In units this is even simpler: job 30 units, A does 3/day, works 2 days → 6 units done, 24 left.
A (12 days) works 3 days, B (18 days) finishes alone: A did $\frac14$; B needs $\frac34 \times 18 = 13.5$ days.

### B joins after t days
A works alone first. Add his solo work to the team work: if A starts and B joins after t days,
$$\frac{t}{T_A} + \left(T_{\text{team}} - t\right)\left(\frac{1}{T_A} + \frac{1}{T_B}\right) = 1$$
A (20 days) starts; B (15 days) joins after 5 days. A alone did $\frac14$; the pair does $\frac{1}{20}+\frac{1}{15} = \frac{7}{60}$ per day → $\frac{45}{7}$ days more, about 14.4 total. Read carefully: the question may ask for the total days or the days after joining.

### Alternate days
Pair the days into a **cycle**. Working one day each, starting with A, one 2-day cycle does $\frac{1}{T_A} + \frac{1}{T_B}$ of the job. Divide the job by the cycle output to get the number of complete cycles, then walk the leftover days one at a time — **the next day is the other worker's turn**.
A = 8 days (3 units of 24), B = 12 days (2 units): cycle = 5 units per 2 days. Four cycles = 8 days, 20 units done, 4 left. Day 9 is A's: 3 units, 1 left. Day 10 is B's: 2 units/day → half a day. Total $9\frac12$ days. Never assume the leftover finishes inside the cycle pattern — check whose turn day 9 actually is.

### Wages follow work done
The wage is payment for work, so money splits in the ratio of the work each person actually did:
$$w_A : w_B = (\text{rate}_A \times \text{days}_A) : (\text{rate}_B \times \text{days}_B)$$
When everyone works the full time together, the days cancel and the wage ratio is just the **rate ratio**. A alone 10 days, B alone 15, together they earn ₹600: rates 3 : 2 → shares ₹360 and ₹240.
If one worker's time is unknown, first find his rate from the group rate (his rate = team rate − others). A (12 days), B (20 days) and C together finish in 5 days for ₹1200: team rate $\frac15$; C's rate $= \frac15 - \frac{1}{12} - \frac{1}{20} = \frac{1}{15}$; ratio $5:3:4$ → C gets ₹400.

### Reading the question twice
The same numbers support four different questions: how many days in total, how many days after the change, what fraction of work each did, and whose share is what. Mark the words *total*, *more*, *alone* and *remaining* before computing — most lost marks here are reading losses, not arithmetic ones.

### Quick revision
- Work done = rate × days worked; whoever continues inherits the remainder.
- Alternate days: count 2-day cycles, then hand the tail to the correct worker.
- Wages = work done ratio; equal days → rate ratio.
- Unknown member's rate = team rate − sum of known rates.
- Sanity: the stronger worker earns the bigger share.
"""

    S.pattern("tw-p17", "A leaves after t days", "very common",
        "A works a few days and leaves; B (or B and C, or the rest of the team) completes the remaining work; the remaining or total days are asked.",
        r"\text{remaining work} = 1 - \frac{t}{T_A}, \qquad \text{days} = \frac{\text{remaining}}{\text{continuing rate}}",
        r"""1. Job in units; find A's daily rate.
2. Work done by A in t days = rate × t; subtract from the job.
3. Divide the remainder by the daily rate of whoever continues.

Why: each worker is only paid in work-units — when A stops, his units stop flowing.""",
        "A can do a work in 12 days and B in 18 days. A works for 3 days and then leaves. In how many days will B alone finish the remaining work?",
        r"A does $\frac{3}{12} = \frac14$. Remaining $= \frac34$ → B needs $\frac34 \times 18 = 13.5$ days.")
    S.pattern("tw-p18", "B joins after t days", "common",
        "A starts alone; after some days B (or a team) joins and the rest is done together; the total time or the after-joining time is asked.",
        r"\frac{t}{T_A} + (T - t)\left(\frac{1}{T_A} + \frac{1}{T_B}\right) = 1",
        r"""1. Work done by A alone = rate × t.
2. Remaining work ÷ combined daily rate = days after joining.
3. Add the solo days for the total time.

Why: the job has two phases with different daily rates; each phase is a rate × time sum.""",
        "A can finish a work in 20 days and B in 15 days. A works alone for 5 days, after which B joins him. In how many days is the whole work finished?",
        r"A did $\frac14$. Remaining $\frac34$ at $\frac{1}{20}+\frac{1}{15} = \frac{7}{60}$/day → $\frac{45}{7} = 6\frac37$ days more → about $11\frac37$ total.")
    S.pattern("tw-p19", "Alternate days (A one day, B next)", "common",
        "'A and B work on alternate days, A starting' — find the total time, or which day the work ends.",
        r"\text{per 2-day cycle} = \frac{1}{T_A} + \frac{1}{T_B}",
        r"""1. One 2-day cycle does $\frac{1}{T_A} + \frac{1}{T_B}$ of the job (use units).
2. Complete as many full cycles as fit; note the work left.
3. Walk the leftover one day at a time — the next day belongs to the OTHER worker. A partial last day counts as a fraction of a day.

Why: pairing the days turns a jumpy schedule into a smooth repeated cycle.""",
        "A can finish a work in 8 days and B in 12 days. Working on alternate days beginning with A, in how many days is the work finished?",
        r"""Job 24 units; A 3/day, B 2/day. Cycle = 5 units. 4 cycles (8 days) → 20 done.
Day 9 (A): 3 → 1 left. Day 10 (B): half a day. Total $9\frac12$ days.""")
    S.pattern("tw-p20", "Wages split by work done", "very common",
        "A total wage for a joint job is given; find one person's share — sometimes with unequal days worked or an unknown member.",
        r"w_A : w_B = (\text{rate}_A \times d_A) : (\text{rate}_B \times d_B)",
        r"""1. Write each worker's rate (in units/day) and multiply by his own days.
2. The wage ratio is the ratio of those products.
3. Give each worker his fraction of the total money.

Why: wages pay for work delivered, and work = rate × days.""",
        "A and B together earn ₹600 for a job. A alone can do the job in 10 days and B alone in 15 days. A's share is:",
        r"Rates 3 : 2 → A gets $\frac{3}{5} \times 600 = ₹360$ (B: ₹240).")

    # ---- practice (tw-cases) ----
    assert F(3, 4) * 18 == F(27, 2)
    S.q("tw-p17", "easy",
        "A can do a piece of work in 12 days and B can do it in 18 days. A works for 3 days and then leaves. B alone will finish the remaining work in:",
        ["13.5 days", "12 days", "15 days", "12.5 days"], "13.5 days",
        r"A did $\frac{3}{12} = \frac14$; remaining $= \frac34$. B's time $= \frac34 \times 18 = 13.5$ days.",
        None, 30)
    assert 600 * F(3, 5) == 360
    S.q("tw-p20", "easy",
        "A and B together receive ₹600 for completing a job. A alone can do the job in 10 days and B alone in 15 days. A's share is:",
        ["₹360", "₹300", "₹240", "₹400"], "₹360",
        r"$A : B = \frac{1}{10} : \frac{1}{15} = 3 : 2$ → A gets $\frac35 \times 600 = ₹360$.",
        None, 30)
    after = F(3, 4) / (1 / F(20) + 1 / F(15))
    assert after == F(45, 7) and 5 + after == F(80, 7)
    S.q("tw-p18", "easy",
        "A can complete a work in 20 days and B in 15 days. A works alone for 5 days, after which B joins him. In how many days in total is the work completed?",
        ["$10\\frac{3}{7}$ days", "12 days", "$11\\frac{1}{2}$ days", "$11\\frac{3}{7}$ days"], mixed(F(80, 7)) + " days",
        r"""A alone did $\frac{5}{20} = \frac14$. Remaining $\frac34$ at $\frac{7}{60}$/day → $\frac{45}{7} = 6\frac37$ days.
Total $= 5 + 6\frac37 = 11\frac37$ days.""",
        None, 40)
    assert F(1) / (1 / F(3) + 1 / F(6)) * 2 == 4
    S.q("tw-p19", "easy",
        "A can complete a job in 3 days and B in 6 days. They work on alternate days, A starting on day 1. The job is finished in:",
        ["4 days", "5 days", "3.5 days", "4.5 days"], "4 days",
        r"Per 2-day cycle: $\frac13 + \frac16 = \frac12$. Two cycles = 4 days complete the job exactly.",
        None, 30)
    left = F(30 - 2 * (3 + 2 + 1), 3)
    assert left == 6
    S.q("tw-p17", "medium",
        "A can do a work in 10 days, B in 15 days and C in 30 days. All three start together, but A leaves after 2 days. For how many more days will B and C work to finish the job?",
        ["6 days", "7 days", "5 days", "8 days"], "6 days",
        r"""Job = 30 units; rates 3, 2, 1. In 2 days all three did 12 units; 18 left.
B + C = 3 units/day → $18 \div 3 = 6$ days.""",
        None, 45)
    total = 6 + F(6, 12 + 24) * 24
    assert total == 10
    S.q("tw-p18", "medium",
        "A can finish a piece of work in 12 days and B in 24 days. A starts the work and B joins him after 6 days. The whole work is finished in:",
        ["10 days", "9 days", "11 days", "12 days"], "10 days",
        r"""A alone: $\frac{6}{12} = \frac12$ done. Remaining $\frac12$ at $\frac{1}{12}+\frac{1}{24} = \frac18$/day → 4 days.
Total $= 6 + 4 = 10$ days.""",
        None, 45)
    assert 4500 * F(5, 15) == 1500
    S.q("tw-p20", "medium",
        "A, B and C together complete a job for ₹4,500. A alone can do it in 10 days, B in 12 days and C in 15 days. B's share is:",
        ["₹1,500", "₹1,800", "₹1,200", "₹1,350"], "₹1,500",
        r"Rates (LCM 60): 6 : 5 : 4 → B gets $\frac{5}{15} \times 4500 = ₹1{,}500$.",
        None, 40)
    assert F(1, 2) * 1 + 1 == F(3, 2)
    S.q("tw-p19", "hard",
        "A can finish a work in 8 days and B in 12 days. They work on alternate days, starting with A. The work is finished in:",
        ["9 days", "10 days", "$8\\frac{1}{2}$ days", "$9\\frac{1}{2}$ days"], mixed(F(19, 2)) + " days",
        r"""Job 24 units; A 3/day, B 2/day; cycle = 5 units per 2 days.
4 cycles = 8 days → 20 done. Day 9 (A): 3 → 1 left. Day 10 (B, 2/day): $\frac12$ day.
Total $= 9\frac12$ days.""",
        "Day 9 belongs to A, not B — the turns alternate every single day.", 55)
    c_rate = 1 / F(5) - 1 / F(12) - 1 / F(20)
    assert F(1) / c_rate == 15 and 1200 * F(4, 12) == 400
    S.q("tw-p20", "hard",
        "A and B undertake to complete a piece of work for ₹1,200. A can do it in 12 days and B in 20 days. With the help of C, they complete it in 5 days. C's share is:",
        ["₹400", "₹300", "₹500", "₹450"], "₹400",
        r"""Team rate $= \frac15$. C's rate $= \frac15 - \frac{1}{12} - \frac{1}{20} = \frac{1}{15}$.
Ratio $= \frac{1}{12} : \frac{1}{20} : \frac{1}{15} = 5 : 3 : 4$ → C gets $\frac{4}{12} \times 1200 = ₹400$.""",
        None, 60)
    return S
