"""Phase-2 deep content for quant/time-work — pipes & cisterns + men-days modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, mixed


def build_pipes():
    S = Sub("tw-pipes")

    S.notes = r"""### Pipes are workers with signs
A pipe that fills a tank is an **inlet**; its rate is positive. A pipe (or a leak) that empties the tank is an **outlet**; its rate is negative. Measure the tank in LCM units — litres or just "units" — exactly as in work problems.
A fills in 12 hours → $+1$ tank per 12 h. B empties in 24 hours → $-\frac{1}{24}$ per hour. Everything else is bookkeeping:
$$\text{net rate} = (\text{sum of inlet rates}) - (\text{sum of outlet rates}), \qquad \text{time} = \frac{\text{tank}}{\text{net rate}}$$

### One inlet, one outlet
A fills in a hours, B empties in b hours ($b > a$). Net rate $= \frac1a - \frac1b$, so the tank fills in
$$T = \frac{ab}{b - a}$$
10 and 15 → $\frac{150}{5} = 30$ hours. Note the minus sign in the denominator — the two-inlet formula $\frac{ab}{a+b}$ is a different question.

### More than one of each
Add every inlet rate, subtract every outlet rate. 8 h and 12 h filling, 24 h emptying: take the tank as 24 units → $3 + 2 - 1 = 4$ units/h → 6 hours. Watch the sign of the net rate: if the outlets win, the tank never fills (some questions ask exactly this — the answer is "it will never fill").

### Staged problems (pipes opened or closed mid-way)
Work stage by stage:
1. Compute the work done in stage 1 = (stage-1 rate) × (stage-1 time).
2. Find what fraction of the tank is still empty.
3. Re-solve the remainder as a fresh, smaller tank with the new set of pipes.
A (10 h) and B (15 h) run 2 hours: 30-unit tank, rate 5 → 10 units done, 20 left. A drain C (30 h) now opens: net $5 - 1 = 4$ units/h → 5 hours more, 7 hours total. Always read carefully whether the question wants the **extra** time or the **total** time — both are asked.

### The reverse leak question
"A tank fills in 8 hours normally, but a leak at the bottom makes it take 8 hours 40 minutes. How long would the leak take to empty a full tank?" Treat the leak as an unknown outlet: its rate = normal fill rate − slow fill rate $= \frac18 - \frac{3}{26} = \frac{1}{104}$ → the leak empties the full tank in 104 hours.

### The empty tank with a leak from the start
Tank full, leak alone empties it in x hours, inlet alone fills the empty tank in y hours — with both acting from empty, fill time $= \frac{xy}{x - y}$ (same fill–drain formula; the leak must be slower than the inlet for filling to be possible at all).

### Common traps
- Adding an outlet's rate instead of subtracting it.
- Using $\frac{ab}{a+b}$ (two-inlets formula) for a fill–drain pair.
- Reporting the stage-1 time or the stage-2 time when the total was asked.
- Forgetting the tank may already be part-full when the new pipe opens.

### Quick revision
- Inlets +, outlets −; net rate = inlets − outlets.
- Fill–drain pair: $T = \frac{ab}{b-a}$.
- Stage it: work done in stage 1, then a fresh smaller tank.
- Reverse leak: leak rate = fast rate − slow rate; leak time = reciprocal.
- Net rate ≤ 0 → the tank never fills.
"""

    S.pattern("tw-p9", "Two or three inlets together", "very common",
        "Two or three pipes all filling the same tank, individual fill times given, combined fill time asked.",
        r"\frac{1}{T} = \frac{1}{T_1} + \frac{1}{T_2} + \cdots",
        r"""1. Tank = LCM of the fill times; rates in units/hour.
2. Add the rates; time = tank ÷ total rate.
3. Two inlets only: use $\frac{ab}{a+b}$ directly.

Why: every pipe pours its own share each hour, exactly like workers on a job.""",
        "Two pipes can fill a tank in 10 hours and 15 hours respectively. With both open together, the tank is filled in:",
        r"Tank $= 30$ units; rates 3 and 2 → 5/h → $30 \div 5 = 6$ hours.")
    S.pattern("tw-p10", "Inlets and outlets together (net rate)", "very common",
        "Filling pipes and an emptying pipe (or leak) are open at the same time; the fill time is asked.",
        r"\text{net rate} = \sum \frac{1}{T_{\text{in}}} - \sum \frac{1}{T_{\text{out}}}",
        r"""1. Mark each pipe + (fills) or − (empties) before any arithmetic.
2. Tank in LCM units; add inlets, subtract outlets.
3. Time = tank ÷ net rate. A fill–drain pair alone is $\frac{ab}{b-a}$.

Why: an outlet undoes work, so it must cancel part of the inlets' contribution.""",
        "Two pipes fill a tank in 8 hours and 12 hours, while a third pipe empties it in 24 hours. With all three open, the tank fills in:",
        r"Tank = 24 units → $3 + 2 - 1 = 4$ units/h → 6 hours.")
    S.pattern("tw-p11", "Reverse: find the leak / outlet from two fill times", "common",
        "'The tank fills in t hours normally but takes t′ hours because of a leak' — the leak's solo emptying time is asked.",
        r"\frac{1}{T_{\text{leak}}} = \frac{1}{t} - \frac{1}{t'}, \quad T_{\text{leak}} = \frac{t \cdot t'}{t' - t}",
        r"""1. Fast fill rate $= \frac1t$, slow (with leak) $= \frac{1}{t'}$.
2. Leak rate $=$ fast − slow; invert for the leak's own emptying time.
3. Put t′ in the same units as t (40 minutes = $\frac23$ hour).

Why: the only difference between the two runs is the leak, so the rate gap belongs to the leak alone.""",
        "A cistern normally fills in 8 hours, but a leak at the bottom makes it take 8 hours 40 minutes. The leak alone can empty the full cistern in:",
        r"Slow time $= \frac{26}{3}$ h. Leak rate $= \frac18 - \frac{3}{26} = \frac{13-12}{104} = \frac{1}{104}$ → 104 hours.")
    S.pattern("tw-p12", "Staged pipes — opened or closed mid-way", "common",
        "Pipes run for a few hours, then another pipe opens (or one closes); the remaining or total time is asked.",
        r"W_1 = \text{rate}_1 \times t_1, \qquad t_2 = \frac{1 - W_1}{\text{rate}_2}",
        r"""1. Stage 1: work done = rate × time; find the empty part left.
2. Stage 2: recompute the net rate with the new set of pipes.
3. Divide the remainder by the stage-2 rate; add stage times if the total is asked.

Why: the tank remembers only how much water is in it — stages are independent rate problems.""",
        "Pipes A and B fill a tank in 10 hours and 15 hours. Both run for 2 hours; then a drain pipe C, which can empty the full tank in 30 hours, is also opened. The total time to fill the tank is:",
        r"""Tank = 30 units; stage 1: $5 \times 2 = 10$ done, 20 left.
Stage 2: $5 - 1 = 4$ units/h → 5 h more → total **7 hours**.""")

    # ---- practice (tw-pipes) ----
    assert F(30, 3 + 2) == 6
    S.q("tw-p9", "easy",
        "Two pipes can fill a tank in 10 hours and 15 hours respectively. If both pipes are opened together, the tank will be filled in:",
        ["6 hours", "5 hours", "7 hours", "8 hours"], "6 hours",
        r"Tank $= 30$ units. Rates 3 and 2 units/h → $\frac{30}{5} = 6$ hours.",
        r"$\frac{10 \times 15}{10 + 15} = 6$ hours.", 25)
    assert F(60, 3 + 2 + 1) == 10
    S.q("tw-p9", "easy",
        "Three pipes can fill a tank in 20 hours, 30 hours and 60 hours respectively. Opening all three together, the tank is filled in:",
        ["10 hours", "8 hours", "12 hours", "15 hours"], "10 hours",
        r"Tank $= 60$ units. Rates $3 + 2 + 1 = 6$ units/h → 10 hours.",
        None, 30)
    assert F(12 * 24, 24 - 12) == 24
    S.q("tw-p10", "easy",
        "A pipe can fill a tank in 12 hours and another pipe can empty the full tank in 24 hours. If both are opened, the empty tank will be filled in:",
        ["24 hours", "18 hours", "36 hours", "12 hours"], "24 hours",
        r"Net rate $= \frac{1}{12} - \frac{1}{24} = \frac{1}{24}$ → 24 hours.",
        r"Fill–drain pair: $\frac{12 \times 24}{24 - 12} = 24$ hours.", 30)
    assert F(36, 4 + 3 - 2) == F(36, 5)
    S.q("tw-p10", "medium",
        "Two pipes fill a tank in 9 hours and 12 hours, while a third pipe empties it in 18 hours. With all three open, the empty tank is filled in:",
        ["7.2 hours", "7.5 hours", "8 hours", "6.5 hours"], "7.2 hours",
        r"Tank $= 36$ units. Net $= 4 + 3 - 2 = 5$ units/h → $\frac{36}{5} = 7.2$ hours.",
        None, 40)
    assert F(24, 3 + 2 - 1) == 6
    S.q("tw-p10", "medium",
        "Pipes A and B can fill a tank in 8 hours and 12 hours respectively, and pipe C can empty the full tank in 24 hours. All three are opened together. The tank will be full in:",
        ["6 hours", "8 hours", "5 hours", "10 hours"], "6 hours",
        r"Tank $= 24$ units. Net rate $= 3 + 2 - 1 = 4$ units/h → 6 hours.",
        None, 35)
    assert F(12 * 20, 20 - 12) == 30
    S.q("tw-p11", "medium",
        "With a leak at its bottom, a tank takes 20 hours to fill, while without the leak it fills in 12 hours. The leak alone can empty the full tank in:",
        ["30 hours", "24 hours", "32 hours", "26 hours"], "30 hours",
        r"Leak rate $= \frac{1}{12} - \frac{1}{20} = \frac{5-3}{60} = \frac{1}{30}$ → 30 hours.",
        r"$\frac{12 \times 20}{20 - 12} = 30$ hours.", 40)
    assert F(1) / (1 / F(8) - 3 / F(26)) == 104
    S.q("tw-p11", "medium",
        "A cistern is normally filled in 8 hours, but takes 8 hours 40 minutes to fill because of a leak in its bottom. In how many hours will the leak alone empty the full cistern?",
        ["104 hours", "96 hours", "110 hours", "120 hours"], "104 hours",
        r"Slow time $= 8\frac{2}{3} = \frac{26}{3}$ h. Leak rate $= \frac{1}{8} - \frac{3}{26} = \frac{13-12}{104} = \frac{1}{104}$ → 104 hours.",
        None, 45)
    total = 2 + F(20, 4)
    assert total == 7
    S.q("tw-p12", "medium",
        "Pipes A and B can fill a tank in 10 hours and 15 hours. Both are opened together for 2 hours; then a drain pipe C, which can empty the full tank in 30 hours, is also opened. The total time taken to fill the tank is:",
        ["7 hours", "6.5 hours", "8 hours", "7.5 hours"], "7 hours",
        r"""Tank = 30 units; stage 1: $5 \times 2 = 10$ units done, 20 left.
Stage 2: net $= 5 - 1 = 4$ units/h → 5 more hours. Total $= 2 + 5 = 7$ hours.""",
        None, 50)
    t2 = F(60 - 8 * 4, 5 - 2)
    assert F(4) + t2 == F(40, 3)
    S.q("tw-p12", "hard",
        "Pipes A and B can fill a tank in 12 hours and 20 hours respectively. Both are opened together for 4 hours; then B is closed and a drain pipe C, which can empty the full tank in 30 hours, is opened along with A. The total time taken to fill the tank is:",
        ["12 hours", "14 hours", "13 hours", "$13\\frac{1}{3}$ hours"], mixed(F(40, 3)) + " hours",
        r"""Tank = 60 units. Stage 1: $(5+3) \times 4 = 32$ units done, 28 left.
Stage 2: net $= 5 - 2 = 3$ units/h → $\frac{28}{3} = 9\frac{1}{3}$ h more. Total $= 13\frac{1}{3}$ hours.""",
        None, 60)
    return S


def build_mandays():
    S = Sub("tw-man-days")

    S.notes = r"""### Work as a product of resources
The same job can be finished by many men in few days or few men in many days. The bridge between the two situations is that the **total work stays the same**, and total work is the product of every resource:
$$\text{Work} = M \times D \times H \times E$$
(men × days × hours per day × efficiency). Equating the products of two situations:
$$\frac{M_1 D_1 H_1 E_1}{W_1} = \frac{M_2 D_2 H_2 E_2}{W_2}$$
For the same work, drop the W's. Quantities that grow with days (men, hours, efficiency) sit beside M; write the missing quantity last and solve. 18 men × 25 days = 450 man-days; with 30 men, $\frac{450}{30} = 15$ days. More men → fewer days: men and days are inversely proportional.

### Hours per day in the chain
12 men working 8 hours a day finish in 15 days: work $= 12 \times 15 \times 8 = 1440$ man-hours. How long for 18 men at 10 hours a day? $\frac{1440}{18 \times 10} = 8$ days. Hours behave exactly like days — more hours a day, fewer days needed.

### Provisions (garrison, hostel, fodder)
A stock of food "for M men for D days" is $M \times D$ man-days of food. After t days the stock left is $M(D - t)$ man-days, to be shared by the new headcount:
$$\text{days left} = \frac{M_1 (D - t)}{M_2}$$
400 men have food for 25 days; after 5 days 100 more men arrive → stock left $= 400 \times 20 = 8000$ man-days ÷ 500 = 16 days. If men leave instead, the headcount drops and the stock lasts longer. If nobody joins or leaves, the remaining days are simply $D - t$.

### Work left after some days / reinforcement mid-work
Convert the whole job into man-days first. 60 men need 40 days → job = 2400 man-days. After 10 days they have done 600, leaving 1800 for the new team. If 10 men leave, the remaining 50 need $\frac{1800}{50} = 36$ days more. Always apply the chain to the **remaining** work, never to the whole job again.

### Men, women and boys (efficiency equivalence)
"3 men or 5 women can do a work in 12 days" pins the unit rates: one man does $\frac{1}{3 \times 12} = \frac{1}{36}$ per day, one woman $\frac{1}{60}$ per day. Any team can then be priced: 6 men + 5 women $= \frac{6}{36} + \frac{5}{60} = \frac14$ per day → 4 days. Read "or" as "the two teams are equally big in work terms".

### Efficiency inside the chain
If one person is twice as efficient, count him as 2 men. A team of 3 men and 2 boys, where a man = 2 boys, is $3 \times 2 + 2 = 8$ boy-units. Converting everyone to one standard unit before multiplying avoids all confusion.

### Common traps
- Writing more men in the numerator (more men → FEWER days).
- Forgetting to subtract the elapsed days from the provisions.
- Applying the chain to the full job instead of the remaining job.
- Counting a man's efficiency twice — E enters the product once.

### Quick revision
- $M_1D_1H_1E_1 = M_2D_2H_2E_2$ for the same work.
- Provisions: stock $= M(D-t)$ man-days ÷ new headcount.
- Mid-work: remaining work = total − (rate × days gone).
- Equivalence: rate of one man = $\frac{1}{\text{men} \times \text{days}}$; price every team this way.
- Sanity: more men / more hours / higher efficiency → fewer days.
"""

    S.pattern("tw-p13", "Men–days–hours chain", "very common",
        "One scenario of men, days and (maybe) hours per day is given; a second scenario changes some of them and one value is asked.",
        r"M_1 D_1 H_1 E_1 = M_2 D_2 H_2 E_2",
        r"""1. Compute the work as $M \times D \times H \times E$ for the given scenario.
2. Divide by the new men, hours and efficiency.
3. Everything that grows with time stays on the left; the unknown lands alone.

Why: the total job is a fixed number of man-hours, so the two products must be equal.""",
        "If 12 men working 8 hours a day can complete a work in 15 days, in how many days will 18 men working 10 hours a day complete it?",
        r"$12 \times 15 \times 8 = 1440$ man-hours; $\frac{1440}{18 \times 10} = 8$ days.")
    S.pattern("tw-p14", "Provisions of a garrison / hostel", "very common",
        "Food or fodder for M men for D days; after t days some men join or leave; how much longer the stock lasts is asked.",
        r"\text{days} = \frac{M_1 (D - t)}{M_2}",
        r"""1. Stock consumed per day = M units; total stock $= M \times D$ man-days.
2. After t days, stock left $= M(D-t)$.
3. Divide by the new headcount for the number of remaining days.

Why: each man eats one unit a day, so the stock is simply a number of man-days.""",
        "A garrison of 400 men has provisions for 25 days. After 5 days, 100 more men join. The provisions will now last:",
        r"Stock left $= 400 \times 20 = 8000$ man-days → $\frac{8000}{500} = 16$ days.")
    S.pattern("tw-p15", "Reinforcement / men leaving mid-work", "common",
        "A team works for some days, then men join or leave; the extra days needed for the remaining work are asked.",
        r"\text{extra days} = \frac{\text{remaining work (man-days)}}{\text{new team size}}",
        r"""1. Whole job in man-days = M × D.
2. Subtract the man-days already done (M × days worked).
3. Divide the remainder by the new number of men.

Why: only the unfinished man-days remain to be shared among whoever is still on the job.""",
        "60 men can complete a piece of work in 40 days. They work for 10 days, after which 10 men leave. In how many days will the remaining work be completed?",
        r"Job $= 2400$ man-days; done $= 600$; left $= 1800$ for 50 men → $\frac{1800}{50} = 36$ days.")
    S.pattern("tw-p16", "Men ↔ women ↔ boys equivalence", "common",
        "'3 men or 5 women can do a work in 12 days' — a mixed team of men and women (or boys) is asked about.",
        r"\text{rate of one} = \frac{1}{\text{(group size)} \times \text{days}}",
        r"""1. From each 'or' statement, write the rate of one person: $\frac{1}{(\text{count})(\text{days})}$.
2. Price the asked team as a sum of unit rates.
3. Invert for the days.

Why: '3 men or 5 women in 12 days' means the two teams do equal work per day, fixing both unit rates.""",
        "If 3 men or 5 women can do a piece of work in 12 days, in how many days will 6 men and 5 women together do it?",
        r"""1 man: $\frac{1}{36}$/day; 1 woman: $\frac{1}{60}$/day.
Team rate $= \frac{6}{36} + \frac{5}{60} = \frac{1}{4}$ → 4 days.""")

    # ---- practice (tw-man-days) ----
    assert F(18 * 25, 30) == 15
    S.q("tw-p13", "easy",
        "If 18 men can complete a piece of work in 25 days, in how many days will 30 men complete the same work?",
        ["15 days", "12 days", "18 days", "20 days"], "15 days",
        r"Work $= 18 \times 25 = 450$ man-days. $\frac{450}{30} = 15$ days.",
        "Men × days constant: 450 ÷ 30.", 25)
    assert F(12 * 15 * 8, 18 * 10) == 8
    S.q("tw-p13", "easy",
        "12 men working 8 hours a day can complete a work in 15 days. In how many days will 18 men working 10 hours a day complete the same work?",
        ["8 days", "9 days", "10 days", "7 days"], "8 days",
        r"Work $= 12 \times 15 \times 8 = 1440$ man-hours → $\frac{1440}{18 \times 10} = 8$ days.",
        None, 30)
    assert F(400 * 20, 500) == 16
    S.q("tw-p14", "easy",
        "A garrison of 400 men has provisions for 25 days. After 5 days, 100 more men join the garrison. The provisions will now last for:",
        ["16 days", "18 days", "15 days", "20 days"], "16 days",
        r"Stock left $= 400 \times (25-5) = 8000$ man-days → $\frac{8000}{500} = 16$ days.",
        None, 30)
    assert F(20 * 24 * 9, 8 * 15) == 36
    S.q("tw-p13", "medium",
        "20 men working 9 hours a day complete a piece of work in 24 days. How many men working 8 hours a day will complete it in 15 days?",
        ["36 men", "30 men", "40 men", "32 men"], "36 men",
        r"Work $= 20 \times 24 \times 9 = 4320$ man-hours. $\frac{4320}{15 \times 8} = 36$ men.",
        None, 40)
    assert F(300 * 35, 200) == F(105, 2)
    S.q("tw-p14", "medium",
        "A fort has provisions for 300 men for 45 days. After 10 days, 100 men leave the fort. For how many more days will the provisions last?",
        ["52.5 days", "45 days", "50 days", "55 days"], "52.5 days",
        r"Stock left $= 300 \times 35 = 10500$ man-days → $\frac{10500}{200} = 52.5$ days.",
        "Fewer men → the stock lasts longer than the original 35 remaining days.", 40)
    assert F(60 * 40 - 60 * 10, 50) == 36
    S.q("tw-p15", "medium",
        "60 men can complete a piece of work in 40 days. They start together and work for 10 days, after which 10 men leave. In how many days will the remaining work be finished?",
        ["36 days", "30 days", "32 days", "40 days"], "36 days",
        r"Job $= 2400$ man-days; done $= 600$; left $= 1800$ with 50 men → 36 days.",
        None, 45)
    assert F(1) / (6 / F(36) + 5 / F(60)) == 4
    S.q("tw-p16", "medium",
        "If 3 men or 5 women can complete a piece of work in 12 days, then 6 men and 5 women together will complete it in:",
        ["4 days", "5 days", "6 days", "3 days"], "4 days",
        r"""1 man $= \frac{1}{36}$/day, 1 woman $= \frac{1}{60}$/day.
$\frac{6}{36} + \frac{5}{60} = \frac{1}{6} + \frac{1}{12} = \frac{1}{4}$ → 4 days.""",
        None, 45)
    assert F(1) / (8 / F(80) + 8 / F(120)) == 6
    S.q("tw-p16", "medium",
        "8 men or 12 boys can finish a piece of work in 10 days. 8 men and 8 boys together will finish it in:",
        ["6 days", "8 days", "5 days", "7 days"], "6 days",
        r"""1 man $= \frac{1}{80}$/day, 1 boy $= \frac{1}{120}$/day.
$\frac{8}{80} + \frac{8}{120} = \frac{1}{10} + \frac{1}{15} = \frac{1}{6}$ → 6 days.""",
        None, 45)
    assert F(120 * 60 - 120 * 12, 72) == 80
    S.q("tw-p15", "hard",
        "120 men can complete a piece of work in 60 days. They work together for the first 12 days; after that some men leave, and the remaining men complete the rest of the work in 72 days. How many men left after the 12th day?",
        ["40 men", "30 men", "50 men", "45 men"], "40 men",
        r"""Job $= 7200$ man-days; done $= 1440$; left $= 5760$.
Men needed $= \frac{5760}{72} = 80$ → $120 - 80 = 40$ men must leave.""",
        None, 60)
    return S
