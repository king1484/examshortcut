"""Readable rewrite of the Time & Work topic (4 subtopics; tw-pipes is the approved pilot and stays untouched).

Simple English, one idea per section, exact fraction checks for every number.
Run: python time_work.py  (patches content/core/topics/quant/time-work.json in place)
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "time-work.json"


def apply(data, sub_id, concept, notes, formulas, tricks, mistakes, revision, patterns):
    sub = next(s for s in data["subtopics"] if s["id"] == sub_id)
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sub_id}: never drop a pattern id"
    assert 2500 <= len(notes) <= 5000, (sub_id, len(notes))
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# =========================== tw-basics ===========================
# answer checks
assert 30 // 15 == 2 and 30 // 10 == 3 and 2 + 3 == 5 and 30 // 5 == 6              # p1: 6 days
assert F(1, 6) - F(1, 15) == F(1, 10)                                              # p1 reverse: B = 10
assert 36 // 9 == 4 and 36 // 12 == 3 and 36 // 18 == 2 and 4 + 3 + 2 == 9 and 36 // 9 == 4  # p2
assert F(1, 10) + F(1, 12) + F(1, 15) == F(1, 4) and F(1, 4) / 2 == F(1, 8)       # p3: trio 8 days
assert F(1, 8) - F(1, 12) == F(1, 24)                                              # p3: A alone 24
assert 10 * F(6, 5) == 12 and 9 * F(8, 3) == 24 and F(1, 12) + F(1, 24) == F(1, 8)  # p4: 8 days
assert 1 - F(5, 12) == F(7, 12) and F(7, 12) * 24 == 14                            # p25: left, C = 14
assert 20 // 10 == 2 and 20 // 20 == 1 and 2 + 1 == 3 and F(20, 3) == 6 + F(2, 3)  # trick 1
assert F(6 * 12, 6 + 12) == 4                                                      # trick 2
assert 36 // 6 == 6 and 36 // 12 == 3 and 36 // 18 == 2 and 6 + 3 + 2 == 11 and F(36, 11) == 3 + F(3, 11)  # trick 3
assert F(6 * 12, 6 + 12) == 4 and F(20, 10) == 2                                   # notes checks

b_concept = (
    r"Treat one whole job as the unit of work. A worker who finishes it in T days has a rate of $\dfrac{1}{T}$ per day, and rates add when people work together."
    "\n\n"
    r"The LCM method keeps everything in whole numbers: set the job to the LCM of the given days, so each rate becomes small units per day."
    "\n\n"
    r"Two workers who take $a$ and $b$ days alone finish together in $\dfrac{ab}{a+b}$ days."
)

b_notes = r"""### What rate means
A job is one whole thing — a wall, a tank, a batch of shirts. A worker's **rate** is the share of that job he finishes in one day.

If A finishes the whole job in T days, his rate is $\dfrac{1}{T}$ per day. Two facts run the whole topic:

$$\text{work} = \text{rate} \times \text{days}, \qquad \text{rates add when people work together}$$

Each worker keeps his own rate inside a team. So the combined time is always less than the fastest single time.

> **Rule:** If your combined answer came out larger than the fastest time, you added days instead of rates.

### The LCM method
Fractions invite slips. Give the job a size in units instead — the LCM of the given days.

A finishes in 15 days, B in 10. Job = 30 units. A does $30 \div 15 = 2$ units a day, B does 3. Together 5 units a day → $30 \div 5 = 6$ days. Every number stays a small whole number to the end.

> **Tip:** Convert every question here to units first. Rates, sums and remainders then stay integers.

### Two workers
For exactly two workers with times a and b:

$$T = \frac{ab}{a+b}$$

6 and 12 days → $\dfrac{72}{18} = 4$ days. This is the LCM method compressed into one line — use it when the numbers divide cleanly.

The reverse is just as common. A and B together take 6 days; A alone takes 15. Subtract rates, never days: $\dfrac{1}{6} - \dfrac{1}{15} = \dfrac{1}{10}$ → B alone takes 10 days.

### Three or more workers
Add all the rates in units. A, B and C take 9, 12 and 18 days: job = 36 units, rates $4 + 3 + 2 = 9$ a day → 4 days. As one formula:

$$T = \frac{abc}{ab + bc + ca}$$

> **Watch:** Do not fold three workers two at a time with $\dfrac{ab}{a+b}$. Add all three rates in a single line.

### Pairwise data
Sometimes the question gives A+B, B+C and A+C instead of single times. Add the three pair-rates: each person appears exactly twice, so halve the sum for the trio rate.

Pairs of 10, 12 and 15 days → $\dfrac{1}{10} + \dfrac{1}{12} + \dfrac{1}{15} = \dfrac{1}{4}$ → trio rate $\dfrac{1}{8}$ → 8 days together. For one person alone, subtract the pair that excludes him: A $= \dfrac{1}{8} - \dfrac{1}{12} = \dfrac{1}{24}$ → 24 days.

### Partial work statements
'A can do $\dfrac{5}{6}$ of the work in 10 days.' Scale to the whole job first: full time $= 10 \times \dfrac{6}{5} = 12$ days. Then combine as usual.

In units it is equally direct: a 24-unit job with 20 units done in 10 days gives a rate of $\dfrac{20}{10} = 2$ units a day. Small numbers, same answer.

> **Careful:** Multiply the days by the reciprocal of the fraction, not by the fraction itself.

### Fraction of work left
A team that takes T days together finishes $\dfrac{t}{T}$ of the job in t days, leaving $1 - \dfrac{t}{T}$.

A and B together take 12 days. After 5 days together, $\dfrac{5}{12}$ is done and $\dfrac{7}{12}$ is left. That remainder then belongs to whoever keeps working — usually the first step of a longer question.

> **Note:** The leftover fraction is itself a common exam answer. Compute it exactly; do not round it.
"""

b_formulas = [
    {"name": "One-day work", "tex": r"\frac{1}{T}"},
    {"name": "Combined time (two workers)", "tex": r"T = \frac{ab}{a + b}"},
    {"name": "Combined time (three workers)", "tex": r"T = \frac{abc}{ab + bc + ca}"},
    {"name": "Work done and left", "tex": r"\text{done} = \frac{t}{T}, \quad \text{left} = 1 - \frac{t}{T}"},
]

b_tricks = [
    {
        "title": "LCM units, not fractions",
        "body": "Set the job to the LCM of the individual times; every rate becomes a small whole number.",
        "example": {
            "q": "A finishes a job in 10 days and B in 20 days. Working together, they finish in:",
            "steps": [r"Work = LCM(10, 20) = $20$ units.", r"A: $2$/day, B: $1$/day → together $3$/day.", r"$20 \div 3 = 6\dfrac{2}{3}$ days."],
            "answer": "6 2/3 days",
        },
    },
    {
        "title": "The ab over a+b reflex",
        "body": "For exactly two workers, one formula — no fraction addition at all.",
        "example": {
            "q": "A does a job in 6 days, B in 12 days. Together they need:",
            "steps": [r"$T = \dfrac{6 \times 12}{6 + 12} = \dfrac{72}{18}$.", r"$= 4$ days — less than either alone."],
            "answer": "4 days",
        },
    },
    {
        "title": "Three workers through the LCM",
        "body": "Same method with three rates added in one line.",
        "example": {
            "q": "A, B and C take 6, 12 and 18 days respectively. Working together, they complete the work in:",
            "steps": [r"Work = LCM = $36$ units.", r"Rates: $6 + 3 + 2 = 11$ a day.", r"$36 \div 11 = 3\dfrac{3}{11}$ days."],
            "answer": "3 3/11 days",
        },
    },
]

b_mistakes = [
    {"wrong": "Adding the days (12 + 24 = 36) instead of adding the rates.", "right": "Rates add, days do not. The together time is ab/(a+b), and it must be less than the smaller time."},
    {"wrong": "For three workers, applying ab/(a+b) to a pair and merging again.", "right": "Add all three rates in one line, or use abc/(ab+bc+ca)."},
    {"wrong": "Accepting a combined time larger than the fastest worker's time.", "right": "The team must beat the best single time; if it does not, rates were not added."},
    {"wrong": "In reverse questions, subtracting the times instead of the rates.", "right": "B's rate = together rate − A's rate; then invert for B's days."},
    {"wrong": "Mixing units — one rate per day, another per hour.", "right": "Convert every rate to the same time unit before adding."},
]

b_revision = [
    "Rate = 1/time; rates add; work = rate × days.",
    "Two workers: T = ab/(a+b). Three: T = abc/(ab+bc+ca).",
    "Together minus one: subtract rates, never days.",
    "Pairwise times: add the three pair-rates, halve for the trio.",
    "Partial work: full time = days × reciprocal of the fraction.",
    "Work left after t days together: 1 − t/T.",
]

b_patterns = [
    pat("tw-p1", "Two workers together (or the reverse)", "very common",
        "Two individual times are given and the together time is asked — or the together time and one person's time are given and the other person is asked.",
        r"T = \frac{ab}{a + b}, \qquad \frac{1}{T_B} = \frac{1}{T_{A+B}} - \frac{1}{T_A}",
        ["Set the job to the LCM of the two times, in units.", "Add the two per-day rates; divide the job by the sum.", "Reverse question: subtract one rate from the together rate, then invert."],
        "Each worker carries his own share every day, so rates add or subtract — days never do.",
        "A finishes a job in 15 days and B in 10 days. Working together, in how many days do they finish it?",
        [r"Job = LCM(15, 10) = $30$ units.", r"A: $30 \div 15 = 2$/day; B: $30 \div 10 = 3$/day.", r"Together $5$/day → $30 \div 5 = 6$ days."],
        "6 days"),
    pat("tw-p2", "Three or more workers together", "very common",
        "Three individual times are given (or two times plus the trio time) and the combined time — or one missing individual time — is asked.",
        r"\frac{1}{T} = \frac{1}{T_A} + \frac{1}{T_B} + \frac{1}{T_C}, \qquad T = \frac{abc}{ab + bc + ca}",
        ["Take the job as the LCM of the given times.", "Write each rate in units per day and add them all in one line.", "Divide the job by the total rate; subtract rates from the trio rate if one is missing."],
        "The whole job is split among the workers, so the daily shares add up to the trio's share.",
        "A, B and C can do a piece of work in 9, 12 and 18 days respectively. In how many days will they finish it together?",
        [r"Job = LCM(9, 12, 18) = $36$ units.", r"Rates: $4 + 3 + 2 = 9$ a day.", r"$36 \div 9 = 4$ days."],
        "4 days"),
    pat("tw-p3", "Pairwise combination times", "common",
        "'A and B together take …, B and C together take …, A and C together take …' — the trio time or one person's time is asked.",
        r"\frac{1}{T_{ABC}} = \frac{1}{2}\left(\frac{1}{T_{AB}} + \frac{1}{T_{BC}} + \frac{1}{T_{AC}}\right)",
        ["Convert the three pair-times to pair-rates.", "Add all three: each worker is counted twice, so halve the sum for the trio rate.", "Any individual's rate = trio rate − the pair-rate that excludes him."],
        "In the sum of the three pair-rates, A appears in two pairs — and so do B and C.",
        "A and B can do a work in 10 days, B and C in 12 days, and A and C in 15 days. In how many days will all three finish it together?",
        [r"Pair rates: $\dfrac{1}{10} + \dfrac{1}{12} + \dfrac{1}{15} = \dfrac{1}{4}$.", r"Each person counted twice → trio rate $= \dfrac{1}{8}$.", r"$8$ days. A alone $= \dfrac{1}{8} - \dfrac{1}{12} = \dfrac{1}{24}$ → 24 days."],
        "8 days"),
    pat("tw-p4", "Fractional / partial work statements", "common",
        "'A can do 3/5 of the work in 12 days', 'B does 2/7 of the work in 8 days' — the full-work time, or the together time, is asked.",
        r"\text{full time} = \text{days} \times \frac{\text{denominator}}{\text{numerator}}",
        ["Scale each statement to the whole job: days × reciprocal of the fraction.", "Combine the full-work times like any other question.", "In LCM units the rate is simply (units done) ÷ (days taken)."],
        "A worker's rate is fixed, so a partial statement just describes a smaller stretch of the same job.",
        r"A can do $\dfrac{5}{6}$ of a work in 10 days and B can do $\dfrac{3}{8}$ of the same work in 9 days. Working together, in how many days will they complete the work?",
        [r"A's full time $= 10 \times \dfrac{6}{5} = 12$ days.", r"B's full time $= 9 \times \dfrac{8}{3} = 24$ days.", r"$\dfrac{1}{12} + \dfrac{1}{24} = \dfrac{1}{8}$ → $8$ days."],
        "8 days"),
    pat("tw-p25", "Fraction of work left after t days together", "very common",
        "A team's together time and the days they worked are given; the fraction of work left — or who finishes the rest — is asked.",
        r"\text{left} = 1 - \frac{t}{T_{together}}",
        [r"Read off the together time T of the team as it stood.", r"Work done in t days $= \dfrac{t}{T}$.", r"Left $= 1 - \dfrac{t}{T}$; if a new worker finishes the rest, multiply the leftover by his full time."],
        "A team working at its combined rate covers the whole job in T days, so t days deliver exactly t/T of it.",
        "A and B together can finish a work in 12 days. They work together for 5 days, after which B leaves. In how many days will C alone finish the remaining work if C alone can do the whole work in 24 days?",
        [r"Done in 5 days $= \dfrac{5}{12}$; left $= \dfrac{7}{12}$.", r"C needs $\dfrac{7}{12} \times 24 = 14$ days."],
        "14 days"),
]

# =========================== tw-efficiency ===========================
# answer checks
assert (2 + 1) * 18 == 54 and 54 // 2 == 27 and 54 // 1 == 54                       # p5: B 54, A 27
assert F(1, 30) / 2 == F(1, 60) and F(5, 60) == F(1, 12)                            # p6: 12 days
assert 2 * 12 - 12 == 12 and F(12 * 24, 12 + 24) == 8                               # p7: together 8
assert F(3, 2) * F(1, 27) == F(1, 18) and F(1, 18) + F(1, 27) == F(5, 54) and F(54, 5) * 10 == 108  # p8
assert (3 + 1) * 12 == 48 and 48 // 3 == 16 and 48 - 16 == 32                       # p26: diff 32
assert (2 + 1) * 12 == 36 and 36 // 2 == 18                                         # trick 1
assert (3 + 1) * 12 == 48 and 48 // 3 == 16                                         # trick 2
assert 3 * 12 - 12 == 24 and 2 * 12 == 24 and F(12 * 36, 12 + 36) == 9              # trick 3
assert (2 + 1) * 9 == 27 and F(27, 2) * 10 == 135                                   # notes: 27, 13.5

e_concept = (
    r"Efficiency is rate: the share of a job a person finishes per day. Efficiency and time are inversely proportional — twice as efficient means half the days."
    "\n\n"
    r"If A is k times as efficient as B and together they take T days, the job is $(k+1)T$ units: B alone needs $(k+1)T$ days and A alone $\dfrac{(k+1)T}{k}$ days."
    "\n\n"
    r"Convert every 'twice as good' or '50% more efficient' statement into a rate ratio before doing anything else."
)

e_notes = r"""### Efficiency is rate
'Efficient' here simply means faster. Efficiency is another word for rate, and it moves opposite to time:

$$\frac{\text{efficiency of A}}{\text{efficiency of B}} = \frac{\text{days of B}}{\text{days of A}}$$

Twice as efficient means half the days. Three times as efficient means one-third of the days. Write every comparison as a rate ratio before touching the numbers.

> **Rule:** Rate × days = one whole job. Multiply the rate by k and the days must divide by k.

### The unit trick
A is k times as good as B. Let B do 1 unit a day and A do k units a day — together $(k+1)$ units a day. If they finish in T days, the whole job is $(k+1)T$ units:

- weaker worker alone: $(k+1)T$ days
- stronger worker alone: $\dfrac{(k+1)T}{k}$ days

A is twice as good as B, and together they take 18 days → job $= 3 \times 18 = 54$ units → B alone 54 days, A alone 27. The weaker worker takes the longer time, always.

> **Watch:** If the stronger worker got the bigger number of days, the ratio was inverted.

### Ratios and per cents
'A and B are in efficiency ratio 3 : 2' is the same idea with both rates written at once: rates $3u$ and $2u$, together $5u$. If B alone takes 30 days, $2u = \dfrac{1}{30}$, so $u = \dfrac{1}{60}$ and together $5u = \dfrac{1}{12}$ → 12 days.

Per cents become ratios at sight. 50% more efficient → 3 : 2. 25% more → 5 : 4. 20% less → 4 : 5. Then continue exactly as with a plain ratio.

> **Tip:** '25% more efficient' is 125 : 100 = 5 : 4, never 25 : 100.

### Days-difference questions
'A is twice as fast as B and takes 12 days less.' Efficiency ratio 2 : 1 makes the times 1x and 2x. The gap $2x - x = 12$ gives x = 12: A takes 12 days, B takes 24. Together they need $\dfrac{12 \times 24}{36} = 8$ days.

In general, with efficiency ratio a : b, the times run b : a. Call them bx and ax, put the difference equal to the given gap, and solve for x.

### Difference of their times
Exams often ask for the difference of the two times instead of one of them. Price the job first, then subtract.

A is 3 times as efficient as B, and together they take 12 days → job $= 4 \times 12 = 48$ units. B alone 48 days, A alone 16 days, difference 32 days. One subtraction after the pricing step.

### Keep the direction honest
The strongest worker always takes the fewest days — and later, in wage questions, earns the bigger share. Run that check on every answer before choosing the option.

Recompute one full chain to stay safe: A is twice as good as B, together 9 days → job = 27 units → B alone 27 days, A alone 13.5. The weaker worker's days equal the job size in units — no accident, since the weaker worker sets the unit at 1 a day.

> **Note:** '30% more efficient' means 13 : 10, not 30 : 100. Convert the wording to a ratio before any arithmetic.
"""

e_formulas = [
    {"name": "Efficiency and time", "tex": r"\frac{E_A}{E_B} = \frac{T_B}{T_A}"},
    {"name": "k-times worker", "tex": r"T_B = (k+1)T, \quad T_A = \frac{(k+1)T}{k}"},
    {"name": "Times from an efficiency ratio", "tex": r"E_A : E_B = a : b \Rightarrow T_A : T_B = b : a"},
    {"name": "Per cent more efficient", "tex": r"a\% \text{ more} \Rightarrow E_A : E_B = (100 + a) : 100"},
]

e_tricks = [
    {
        "title": "Rate units from the efficiency ratio",
        "body": "Let B = 1 unit/day, A = k units/day; together (k+1) per day prices the job.",
        "example": {
            "q": "A is twice as efficient as B, and together they finish a job in 12 days. B alone would take:",
            "steps": [r"Units: $2 + 1 = 3$/day → job $= 3 \times 12 = 36$ units.", r"B alone $= 36 \div 1 = 36$ days (A: $18$)."],
            "answer": "36 days",
        },
    },
    {
        "title": "Invert, never scale",
        "body": "'A is 3 times as good' means A's days = B's days ÷ 3.",
        "example": {
            "q": "A is 3 times as efficient as B and together they complete the work in 12 days. A alone takes:",
            "steps": [r"Job $= 4 \times 12 = 48$ units.", r"A $= 48 \div 3 = 16$ days (B: $48$)."],
            "answer": "16 days",
        },
    },
    {
        "title": "Days-difference cases",
        "body": "'B takes 24 days more than A' plus an efficiency ratio pins both times.",
        "example": {
            "q": "A is 3 times as fast as B and takes 24 days less than B. Together they would finish the work in:",
            "steps": [r"Times $x$ and $3x$ with $3x - x = 24$ → $x = 12$: A $= 12$, B $= 36$ days.", r"Together $= \dfrac{12 \times 36}{48} = 9$ days."],
            "answer": "9 days",
        },
    },
]

e_mistakes = [
    {"wrong": "Reading 'twice as efficient' as twice the days.", "right": "Efficiency up means days down — half the days, not double."},
    {"wrong": "Giving the k-times worker $(k+1)T$ days.", "right": "That is the weaker worker's time. The stronger takes (k+1)T/k."},
    {"wrong": "Treating '25% more efficient' as 25 : 100.", "right": "It is 125 : 100 = 5 : 4. Add the per cent to 100 first."},
    {"wrong": "Adding efficiencies as if they were days.", "right": "Efficiencies are rates; invert to times (or price in units) before combining."},
    {"wrong": "Mixing up whose time is longer in days-difference questions.", "right": "The weaker worker takes the longer time. Check the direction before answering."},
]

e_revision = [
    "Efficiency ratio = rate ratio = inverse time ratio.",
    "k-times worker, together T days: weaker (k+1)T, stronger (k+1)T/k.",
    "50% / 25% / 30% more efficient → 3:2 / 5:4 / 13:10.",
    "Efficiency a : b makes times b : a; gap = (b − a)x.",
    "Difference of times: price the job in units, then subtract.",
    "Sanity check: faster worker, fewer days — always.",
]

e_patterns = [
    pat("tw-p5", "'k times as efficient', together time given", "very common",
        "'A is twice/thrice as efficient as B and together they finish in T days' — the individual times are asked.",
        r"T_B = (k+1)T, \qquad T_A = \frac{(k+1)T}{k}",
        ["Let the weaker worker do 1 unit/day, the stronger k units/day.", r"Together $(k+1)$ units/day → job $= (k+1) \times T$ units.", "Divide the job by each worker's own rate for his days."],
        "The together time prices the job in units; each worker then spends those units at his own speed.",
        "A is twice as efficient as B and together they complete a work in 18 days. B alone can complete it in:",
        [r"Rates: A $= 2$, B $= 1$ → $3$/day.", r"Job $= 3 \times 18 = 54$ units.", r"B alone $= 54 \div 1 = 54$ days (A alone $27$)."],
        "54 days"),
    pat("tw-p6", "Efficiency ratio given as a : b", "common",
        "An explicit ratio like 3 : 2 is given for the efficiencies, with either the together time or one person's time.",
        r"\text{job} = (a + b) \times T \text{ units}, \qquad T_{\text{weak}} = \frac{(a+b)T}{b}",
        [r"Fix rates $au$ and $bu$ per day.", "From the given time, price the job in units.", "Divide the job by the rate whose time is asked."],
        "A ratio is only a k-times statement written for both workers at once.",
        "The efficiencies of A and B are in the ratio 3 : 2. B alone can finish the work in 30 days. Working together, they will finish it in:",
        [r"B: $2u = \dfrac{1}{30}$ → $u = \dfrac{1}{60}$.", r"Together $5u = \dfrac{5}{60} = \dfrac{1}{12}$ per day.", r"$12$ days."],
        "12 days"),
    pat("tw-p7", "Efficiency ratio plus a gap of days", "common",
        "'A is twice as fast as B and takes 12 days less' — find either individual time or the together time.",
        r"bx - ax = \text{gap}, \text{ where the times are } bx \text{ and } ax",
        [r"With efficiency ratio $a : b$, the times are in $b : a$ — call them $bx$ and $ax$.", "Put the difference equal to the given gap and solve for x.", r"Combine the two times with $\dfrac{ab}{a+b}$ if the together time is asked."],
        "The gap is a difference of two numbers in a known ratio, so one bracket pins both.",
        "A is twice as fast a worker as B and takes 12 days less than B to finish a piece of work. Working together, they will finish it in:",
        [r"Times $x$ and $2x$: $2x - x = 12$ → A $= 12$ days, B $= 24$ days.", r"Together $= \dfrac{12 \times 24}{36} = 8$ days."],
        "8 days"),
    pat("tw-p8", "Percent more / less efficient", "occasional",
        "'A is 50% more efficient than B', 'A works 20% faster' — percentages of efficiency instead of a ratio.",
        r"a\% \text{ more efficient} \Rightarrow E_A : E_B = (100 + a) : 100",
        ["Convert to a ratio: 50% more → 3 : 2; 25% more → 5 : 4; 20% less → 4 : 5.", "Continue with the unit method — price the job, then divide.", "Keep fractions; answers like 10.8 days are legitimate."],
        "'a% more efficient' means the rate is multiplied by one plus a hundredth.",
        "A is 50% more efficient than B. B alone can finish a work in 27 days. Working together, they will finish it in:",
        [r"A's rate $= \dfrac{3}{2} \times \dfrac{1}{27} = \dfrac{1}{18}$.", r"Sum $= \dfrac{1}{18} + \dfrac{1}{27} = \dfrac{5}{54}$ per day.", r"$\dfrac{54}{5} = 10.8$ days."],
        "10.8 days"),
    pat("tw-p26", "Difference of the two individual times", "common",
        "'A is k times as efficient as B and together they take T days' — the difference between their individual times is asked.",
        r"T_B - T_A = (k+1)T - \frac{(k+1)T}{k}",
        ["Let the weaker worker do 1 unit a day, the stronger k units.", r"Job $= (k+1)T$ units; weaker alone $(k+1)T$ days, stronger $\dfrac{(k+1)T}{k}$ days.", "Subtract the two times."],
        "Both times come from the same priced job, so one subtraction finishes the question.",
        "A is 3 times as efficient as B and together they complete a work in 12 days. Find the difference between the times A and B alone would take.",
        [r"Job $= 4 \times 12 = 48$ units.", r"B alone $= 48$ days; A alone $= 48 \div 3 = 16$ days.", r"Difference $= 48 - 16 = 32$ days."],
        "32 days"),
]

# =========================== tw-man-days ===========================
# answer checks
assert 12 * 15 * 8 == 1440 and 18 * 10 == 180 and 1440 // 180 == 8                 # p13
assert 400 * (25 - 5) == 8000 and 8000 // 500 == 16                                # p14
assert 60 * 40 == 2400 and 60 * 10 == 600 and 2400 - 600 == 1800 and 1800 // 50 == 36  # p15
assert F(1, 3 * 12) == F(1, 36) and F(1, 5 * 12) == F(1, 60) and F(6, 36) + F(5, 60) == F(1, 4)  # p16
assert F(20 * 20 * 9, 8 * 12) == F(75, 2)                                          # p27: 37.5
assert 15 * 20 == 300 and 300 // 25 == 12                                          # trick 1
assert 500 * 24 == 12000 and 500 + 300 == 800 and 12000 // 800 == 15               # trick 2
assert 45 * 16 == 720 and 45 * 4 == 180 and 720 - 180 == 540 and F(540, 81) == F(20, 3)  # trick 3
assert 18 * 25 == 450 and 450 // 30 == 15                                          # notes
assert 3 * 2 + 2 == 8                                                              # notes: boy-units

m_concept = (
    r"Total work is the product of the resources: $W = M \times D \times H \times E$ — men, days, hours per day, efficiency."
    "\n\n"
    r"For the same job, $M_1 D_1 H_1 E_1 = M_2 D_2 H_2 E_2$: more men means fewer days."
    "\n\n"
    r"Provisions are the same arithmetic: stock = men × days, and after t days the remaining stock feeds the new headcount for $\dfrac{M_1(D - t)}{M_2}$ days."
)

m_notes = r"""### Work is a product
Many men in few days or few men in many days — the job keeps the same size. Total work is the product of every resource:

$$W = M \times D \times H \times E$$

men × days × hours a day × efficiency. For the same job, equate two situations: $M_1 D_1 H_1 E_1 = M_2 D_2 H_2 E_2$. 18 men × 25 days = 450 man-days; with 30 men the same job needs $\dfrac{450}{30} = 15$ days.

> **Rule:** For a fixed job, more men means fewer days. Men and days are inversely proportional.

### Hours join the chain
Hours a day behave exactly like men. 12 men working 8 hours a day for 15 days put in $12 \times 15 \times 8 = 1440$ man-hours. With 18 men at 10 hours a day the job takes $\dfrac{1440}{180} = 8$ days.

Write the missing quantity last, then divide. No proportion table is needed.

> **Tip:** Convert the whole job to one labour unit first — man-days or man-hours. The answer is then a single division.

### Provisions
Food 'for M men for D days' is $M \times D$ man-days of stock. After t days the stock left is $M(D - t)$, and the new headcount consumes it:

$$\text{days left} = \frac{M_1(D - t)}{M_2}$$

400 men hold 25 days of food. After 5 days, 100 more men arrive: $400 \times 20 = 8000$ man-days ÷ 500 men = 16 days. Men leaving works the same way, and then the stock lasts longer.

> **Watch:** Subtract the elapsed days before anything else. Feeding the new headcount from the full D is the standard error.

### Mid-work changes
A team works for a while, then men join or leave. Convert the whole job to man-days, subtract what is already done, and hand the remainder to the new team.

60 men need 40 days → 2400 man-days. After 10 days, 600 are done. Ten men leave, and the remaining 1800 man-days need $\dfrac{1800}{50} = 36$ days more.

> **Careful:** Apply the chain to the remaining work only. Restarting from the full job double-counts the finished part.

### Men, women and boys
'3 men or 5 women can do it in 12 days' fixes both unit rates, because both teams finish equal work. So one man does $\dfrac{1}{36}$ per day and one woman $\dfrac{1}{60}$ per day.

Price any mixed team by adding rates: 6 men + 5 women $= \dfrac{6}{36} + \dfrac{5}{60} = \dfrac{1}{4}$ → 4 days.

> **Tip:** Read 'or' as 'the two teams are equal in work terms'. The two unit rates then fall out together.

### Scaling the work itself
Sometimes the work grows instead of the crew. Work then scales directly with men and days:

$$W_2 = W_1 \times \frac{M_2}{M_1} \times \frac{D_2}{D_1}$$

8 men reap 20 hectares in 12 days. In 9 days, 20 men reap $20 \times \dfrac{20}{8} \times \dfrac{9}{12} = 37.5$ hectares. Multiply for resources that grew, divide for those that shrank.

### Efficiency inside the product
A worker twice as efficient counts as two men. A team of 3 men and 2 boys, where one man equals 2 boys in output, is $3 \times 2 + 2 = 8$ boy-units. Convert everyone to one standard unit before multiplying — never mix raw headcounts with a separate efficiency factor.
"""

m_formulas = [
    {"name": "MDH chain", "tex": r"M_1 D_1 H_1 E_1 = M_2 D_2 H_2 E_2 \quad (W_1 = W_2)"},
    {"name": "Men and days constant", "tex": r"M_1 D_1 = M_2 D_2"},
    {"name": "Provisions remaining", "tex": r"\text{days} = \frac{M_1 (D_{total} - t)}{M_2}"},
    {"name": "Work scaling", "tex": r"W_2 = W_1 \times \frac{M_2}{M_1} \times \frac{D_2}{D_1}"},
]

m_tricks = [
    {
        "title": "Multiply resources, equate products",
        "body": "Everything that grows the work sits beside M; the missing quantity lands alone.",
        "example": {
            "q": "15 men complete a work in 20 days. In how many days will 25 men complete the same work?",
            "steps": [r"$15 \times 20 = 25 \times D$.", r"$D = 300 \div 25 = 12$ days."],
            "answer": "12 days",
        },
    },
    {
        "title": "Provisions after reinforcement",
        "body": "Stock left = original men × days left; then divide by the new headcount.",
        "example": {
            "q": "A garrison of 500 men has provisions for 27 days. After 3 days, 300 more men join. The provisions will now last:",
            "steps": [r"Stock left $= 500 \times 24 = 12000$ man-days.", r"$12000 \div 800 = 15$ days."],
            "answer": "15 days",
        },
    },
    {
        "title": "Work left after a share is done",
        "body": "First find the remaining man-days, then apply them to the new team.",
        "example": {
            "q": "45 men start a job they would finish in 16 days. After 4 days, 36 more men join. The remaining work now takes:",
            "steps": [r"Job $= 720$ man-days; done $= 180$; left $= 540$.", r"$540 \div 81 = 6\dfrac{2}{3}$ days."],
            "answer": "6 2/3 days",
        },
    },
]

m_mistakes = [
    {"wrong": "Writing more men on the wrong side (more men, more days).", "right": "For a fixed job men and days are inverse: M₁D₁ = M₂D₂."},
    {"wrong": "Forgetting to subtract the elapsed days in provisions.", "right": "Stock left = M(D − t); only that feeds the new headcount."},
    {"wrong": "Applying the chain to the whole work after a mid-work change.", "right": "Subtract the man-days already done; chain only the remainder."},
    {"wrong": "Counting efficiency twice.", "right": "E enters the product once. Convert everyone to one standard unit first."},
    {"wrong": "Using two different labour units in one chain.", "right": "Convert boys and women to man-equivalents (or one common unit) before multiplying."},
]

m_revision = [
    "M₁D₁H₁E₁ = M₂D₂H₂E₂ for the same work.",
    "Provisions: stock left = M(D − t) man-days ÷ new headcount.",
    "Mid-work: remaining = total man-days − done; chain only the remainder.",
    "Equivalence: one person's rate = 1/(group size × days).",
    "Work scaling: W₂ = W₁ × (M₂/M₁) × (D₂/D₁).",
    "Sanity: more men, more hours, higher efficiency → fewer days.",
]

m_patterns = [
    pat("tw-p13", "Men–days–hours chain", "very common",
        "One scenario of men, days and (maybe) hours per day is given; a second scenario changes some of them and one value is asked.",
        r"M_1 D_1 H_1 E_1 = M_2 D_2 H_2 E_2",
        [r"Compute the work as $M \times D \times H \times E$ for the given scenario.", "Divide by the new men, hours and efficiency.", "The unknown lands alone on one side."],
        "The total job is a fixed number of man-hours, so the two products must be equal.",
        "If 12 men working 8 hours a day can complete a work in 15 days, in how many days will 18 men working 10 hours a day complete it?",
        [r"Work $= 12 \times 15 \times 8 = 1440$ man-hours.", r"New crew supplies $18 \times 10 = 180$ man-hours a day.", r"$1440 \div 180 = 8$ days."],
        "8 days"),
    pat("tw-p14", "Provisions of a garrison / hostel", "very common",
        "Food or fodder for M men for D days; after t days some men join or leave; how much longer the stock lasts is asked.",
        r"\text{days} = \frac{M_1 (D - t)}{M_2}",
        ["Total stock = M × D man-days; each man eats one unit a day.", r"After t days, stock left $= M(D - t)$.", "Divide by the new headcount for the remaining days."],
        "The stock is simply a number of man-days, whoever eats them.",
        "A garrison of 400 men has provisions for 25 days. After 5 days, 100 more men join. The provisions will now last:",
        [r"Stock left $= 400 \times (25 - 5) = 8000$ man-days.", r"New headcount $= 500$.", r"$8000 \div 500 = 16$ days."],
        "16 days"),
    pat("tw-p15", "Reinforcement / men leaving mid-work", "common",
        "A team works for some days, then men join or leave; the extra days needed for the remaining work are asked.",
        r"\text{extra days} = \frac{\text{remaining man-days}}{\text{new team size}}",
        ["Whole job in man-days = M × D.", "Subtract the man-days already done (M × days worked).", "Divide the remainder by the new number of men."],
        "Only the unfinished man-days remain to be shared among whoever is still on the job.",
        "60 men can complete a piece of work in 40 days. They work for 10 days, after which 10 men leave. In how many days will the remaining work be completed?",
        [r"Job $= 60 \times 40 = 2400$ man-days.", r"Done $= 60 \times 10 = 600$; left $= 1800$ for $50$ men.", r"$1800 \div 50 = 36$ days."],
        "36 days"),
    pat("tw-p16", "Men, women and boys equivalence", "common",
        "'3 men or 5 women can do a work in 12 days' — a mixed team of men and women (or boys) is asked about.",
        r"\text{rate of one} = \frac{1}{\text{group size} \times \text{days}}",
        [r"From each 'or' statement, write one person's rate: $\dfrac{1}{\text{count} \times \text{days}}$.", "Price the asked team as a sum of unit rates.", "Invert for the days."],
        "'3 men or 5 women in 12 days' means the two teams do equal work per day, fixing both unit rates.",
        "If 3 men or 5 women can do a piece of work in 12 days, in how many days will 6 men and 5 women together do it?",
        [r"1 man: $\dfrac{1}{36}$/day; 1 woman: $\dfrac{1}{60}$/day.", r"Team rate $= \dfrac{6}{36} + \dfrac{5}{60} = \dfrac{1}{4}$ per day.", r"$4$ days."],
        "4 days"),
    pat("tw-p27", "Scaling the work itself", "common",
        "A crew produces a measured output — hectares, chairs, kilometres of road; a new crew and time give a new output.",
        r"W_2 = W_1 \times \frac{M_2}{M_1} \times \frac{D_2}{D_1}",
        ["Put each change as a fraction: new ÷ old.", "Multiply the old output by both fractions.", "Reduce the fractions first to keep the arithmetic small."],
        "Output grows in direct proportion to men and to days — the chain equation read forward.",
        "If 8 men can reap 20 hectares in 12 days, how many hectares can 20 men reap in 9 days?",
        [r"Men factor $= \dfrac{20}{8}$; days factor $= \dfrac{9}{12}$.", r"$20 \times \dfrac{20}{8} \times \dfrac{9}{12} = 37.5$ hectares."],
        "37.5 hectares"),
]

# =========================== tw-cases ===========================
# answer checks
assert F(3, 12) == F(1, 4) and (1 - F(1, 4)) * 18 == F(27, 2)                      # p17: 13.5
assert F(1, 20) + F(1, 15) == F(7, 60) and F(3, 4) / F(7, 60) == F(45, 7) and F(45, 7) + 5 == F(80, 7)  # p18
assert 24 // 8 == 3 and 24 // 12 == 2 and 3 + 2 == 5 and 4 * 5 == 20               # p19
assert 24 - 20 == 4 and 4 - 3 == 1 and 9 + F(1, 2) == F(19, 2)                     # p19: 9.5
assert 30 // 10 == 3 and 30 // 15 == 2 and F(3, 5) * 600 == 360                    # p20
assert 3 * (9 - 3) + 2 * 9 == 36 and F(9 - 3, 12) + F(9, 18) == 1                  # p28: T = 9
assert F(4, 15) + F(11, 15) == 1 and 20 * F(11, 15) == F(44, 3)                    # trick 1
assert F(1, 6) + F(1, 12) == F(1, 4) and F(1, 4) * 4 == 1                          # trick 2
assert F(1, 12) / F(1, 18) == F(3, 2) and F(3, 5) * 840 == 504                     # trick 3
assert F(1, 5) - F(1, 12) - F(1, 20) == F(1, 15)                                   # notes: C

c_concept = (
    r"Every twist here — leaving, joining, alternating, wages — uses one method: count the work each person actually did."
    "\n\n"
    r"A leaving after t days finishes $\dfrac{t}{T_A}$ of the job; whoever continues inherits the rest. Alternate days pair into a 2-day cycle of $\dfrac{1}{T_A} + \dfrac{1}{T_B}$."
    "\n\n"
    r"Wages split in the ratio of work done — which equals the rate ratio when everyone works the same days."
)

c_notes = r"""### Count the work actually done
Someone leaves, someone joins late, people alternate days, wages get split — one method answers all of it. Put the job in LCM units, write each worker's daily rate, then add up the work each person actually did. Set the total equal to the whole job.

### Leaving after t days
A works t of his $T_A$ days and stops. He finished $\dfrac{t}{T_A}$ of the job; the rest, $1 - \dfrac{t}{T_A}$, belongs to whoever continues.

A (12 days) works 3 days → $\dfrac{1}{4}$ done. B (18 days) alone needs $\dfrac{3}{4} \times 18 = 13.5$ days.

> **Rule:** Work done = rate × days worked. Whoever continues inherits only the remainder.

### Leaving before the end
'A leaves 3 days before the work finishes' hides the total time T. Write both stints against T: A works $T - 3$ days, B works all T days.

$$\frac{T - t}{T_A} + \frac{T}{T_B} = 1$$

With $T_A = 12$, $T_B = 18$, $t = 3$: $\dfrac{T-3}{12} + \dfrac{T}{18} = 1$ → $3(T-3) + 2T = 36$ → T = 9 days.

> **Tip:** One unknown T, one linear equation. Multiply through by the LCM of the two times.

### Joining after t days
A starts alone; B joins later. Add the solo stint to the team stint:

$$\frac{t}{T_A} + (\text{days together}) \times \left(\frac{1}{T_A} + \frac{1}{T_B}\right) = 1$$

A (20 days) works 5 days → $\dfrac{1}{4}$. The pair then does $\dfrac{1}{20} + \dfrac{1}{15} = \dfrac{7}{60}$ a day → $\dfrac{45}{7} = 6\dfrac{3}{7}$ days more, $11\dfrac{3}{7}$ in total.

> **Watch:** 'In how many days is the work finished?' can mean the total or the extra days after the change. Underline which one is asked.

### Alternate days
Pair the days into one cycle of two days: A's day plus B's day $= \dfrac{1}{T_A} + \dfrac{1}{T_B}$ of the job. Count whole cycles, then walk the leftover day by day — the next day is the other worker's turn.

A = 8 days (3 units of 24), B = 12 days (2 units). A cycle = 5 units. Four cycles = 8 days, 20 units done. Day 9 is A's: 3 more, 1 left. Day 10 is B's at 2 a day: half a day. Total $9\dfrac{1}{2}$ days.

> **Careful:** The tail does not always fit the pattern. Check whose turn the next day really is.

### Wages follow work
Money splits in the ratio of work actually delivered: rate × days for each person. When everyone works the full time, the days cancel and the wage ratio is just the rate ratio.

A alone 10 days, B alone 15, ₹600 earned together → rates 3 : 2 → ₹360 and ₹240. An unknown member: his rate = team rate − the known rates. A (12 days), B (20 days) and C finish in 5 days → C $= \dfrac{1}{5} - \dfrac{1}{12} - \dfrac{1}{20} = \dfrac{1}{15}$; the shares run 5 : 3 : 4.

### Read the question twice
The same numbers support four different asks: total days, days after the change, each person's share of work, each person's share of money. Mark the words *total*, *more*, *alone* and *remaining* before computing. Most lost marks here are reading losses, not arithmetic ones.
"""

c_formulas = [
    {"name": "Work done by A in t days", "tex": r"\frac{t}{T_A}"},
    {"name": "Leaves t days before the end", "tex": r"\frac{T - t}{T_A} + \frac{T}{T_B} = 1"},
    {"name": "Two-day cycle", "tex": r"\frac{1}{T_A} + \frac{1}{T_B} \text{ per 2 days}"},
    {"name": "Wage split", "tex": r"w_A = \text{total} \times \frac{1/T_A}{1/T_A + 1/T_B}"},
]

c_tricks = [
    {
        "title": "Subtract the finished part",
        "body": "Whoever continues inherits only the remainder.",
        "example": {
            "q": "A can do a work in 15 days and B in 20 days. A works for 4 days and leaves. B alone finishes the rest in:",
            "steps": [r"A did $\dfrac{4}{15}$; left $= \dfrac{11}{15}$.", r"B needs $20 \times \dfrac{11}{15} = 14\dfrac{2}{3}$ days."],
            "answer": "14 2/3 days",
        },
    },
    {
        "title": "Count full cycles, then the tail",
        "body": "Alternate days: measure progress per 2-day cycle.",
        "example": {
            "q": "A takes 6 days and B takes 12 days for a job. They work on alternate days, A starting. The job is finished in:",
            "steps": [r"Per 2 days: $\dfrac{1}{6} + \dfrac{1}{12} = \dfrac{1}{4}$.", r"4 cycles = 8 days, exactly the whole job."],
            "answer": "8 days",
        },
    },
    {
        "title": "Wages follow work, not days alone",
        "body": "Rate ratio × equal days = work ratio.",
        "example": {
            "q": "A alone does a work in 12 days, B in 18 days. They work together and earn ₹840. A's share is:",
            "steps": [r"$A : B = \dfrac{1}{12} : \dfrac{1}{18} = 3 : 2$.", r"A gets $840 \times \dfrac{3}{5} = ₹504$."],
            "answer": "₹504",
        },
    },
]

c_mistakes = [
    {"wrong": "Splitting wages by days alone when efficiencies differ.", "right": "Wages follow work done: rate × days for each person."},
    {"wrong": "In alternate-day problems, forgetting who works the final partial day.", "right": "Walk the tail day by day; the next day is the other worker's turn."},
    {"wrong": "Applying the remaining work to both workers.", "right": "Only whoever continues inherits the remainder; A has stopped."},
    {"wrong": "Counting a 2-day cycle as one day.", "right": "One cycle = one day of A plus one day of B = two calendar days."},
    {"wrong": "Reading 'leaves 3 days before completion' as 'works 3 days'.", "right": "A works T − 3 of the T total days; set up the equation in T."},
]

c_revision = [
    "Work done = rate × days worked; the rest inherits the remainder.",
    "Leaves t days before the end: (T−t)/T_A + T/T_B = 1.",
    "Alternate days: count 2-day cycles, then hand the tail to the right worker.",
    "Wages split by work done; equal days → rate ratio.",
    "Unknown member: rate = team rate − sum of known rates.",
    "Mark total / more / alone / remaining before computing.",
]

c_patterns = [
    pat("tw-p17", "A leaves after t days", "very common",
        "A works a few days and leaves; B (or B and C, or the rest of the team) completes the remaining work; the remaining or total days are asked.",
        r"\text{remaining work} = 1 - \frac{t}{T_A}, \qquad \text{days} = \frac{\text{remaining}}{\text{continuing rate}}",
        ["Put the job in units; find A's daily rate.", "Work done by A in t days = rate × t; subtract from the job.", "Divide the remainder by the daily rate of whoever continues."],
        "When A stops, his units stop flowing — only the finished units leave the pool.",
        "A can do a work in 12 days and B in 18 days. A works for 3 days and then leaves. In how many days will B alone finish the remaining work?",
        [r"A does $\dfrac{3}{12} = \dfrac{1}{4}$.", r"Remaining $= \dfrac{3}{4}$.", r"B needs $\dfrac{3}{4} \times 18 = 13.5$ days."],
        "13.5 days"),
    pat("tw-p18", "B joins after t days", "common",
        "A starts alone; after some days B (or a team) joins and the rest is done together; the total time or the after-joining time is asked.",
        r"\frac{t}{T_A} + (T - t)\left(\frac{1}{T_A} + \frac{1}{T_B}\right) = 1",
        ["Work done by A alone = rate × t.", "Remaining work ÷ combined daily rate = days after joining.", "Add the solo days for the total time."],
        "The job has two phases with different daily rates; each phase is a rate × time sum.",
        "A can finish a work in 20 days and B in 15 days. A works alone for 5 days, after which B joins him. In how many days is the whole work finished?",
        [r"A did $\dfrac{5}{20} = \dfrac{1}{4}$.", r"Pair rate $= \dfrac{1}{20} + \dfrac{1}{15} = \dfrac{7}{60}$ a day.", r"$\dfrac{3}{4} \div \dfrac{7}{60} = 6\dfrac{3}{7}$ more → $11\dfrac{3}{7}$ total."],
        "11 3/7 days in total (6 3/7 more)"),
    pat("tw-p19", "Alternate days (A one day, B next)", "common",
        "'A and B work on alternate days, A starting' — find the total time, or which day the work ends.",
        r"\text{per 2-day cycle} = \frac{1}{T_A} + \frac{1}{T_B}",
        [r"One 2-day cycle does $\dfrac{1}{T_A} + \dfrac{1}{T_B}$ of the job (use units).", "Complete as many full cycles as fit; note the work left.", "Walk the leftover one day at a time — the next day belongs to the other worker. A partial last day counts as a fraction."],
        "Pairing the days turns a jumpy schedule into a smooth repeated cycle.",
        "A can finish a work in 8 days and B in 12 days. Working on alternate days beginning with A, in how many days is the work finished?",
        [r"Job $= 24$ units; A $3$/day, B $2$/day → cycle $= 5$ units.", r"4 cycles $= 8$ days → $20$ units done, $4$ left.", r"Day 9 (A): $3$ → $1$ left. Day 10 (B): half a day. Total $9\dfrac{1}{2}$ days."],
        "9.5 days"),
    pat("tw-p20", "Wages split by work done", "very common",
        "A total wage for a joint job is given; find one person's share — sometimes with unequal days worked or an unknown member.",
        r"w_A : w_B = (\text{rate}_A \times d_A) : (\text{rate}_B \times d_B)",
        ["Write each worker's rate in units/day and multiply by his own days.", "The wage ratio is the ratio of those products.", "Give each worker his fraction of the total money."],
        "Wages pay for work delivered, and work = rate × days.",
        "A and B together earn ₹600 for a job. A alone can do the job in 10 days and B alone in 15 days. A's share is:",
        [r"Job $= 30$ units: rates $3 : 2$.", r"A gets $\dfrac{3}{5} \times 600 = ₹360$ (B: $₹240$)."],
        "₹360"),
    pat("tw-p28", "A leaves t days before the work finishes", "common",
        "'A and B start together; A leaves t days before the work is completed' — the total time is asked.",
        r"\frac{T - t}{T_A} + \frac{T}{T_B} = 1",
        [r"Let the total time be T; A works $T - t$ days, B works all $T$ days.", "Write A's share plus B's share equal to 1; multiply by the LCM of the times.", "Solve the linear equation for T."],
        "Both stints are measured against the same unknown finish line, so one equation closes the question.",
        "A can do a work in 12 days and B in 18 days. They begin together, but A leaves 3 days before the work is finished. Find the total time taken.",
        [r"$\dfrac{T-3}{12} + \dfrac{T}{18} = 1$; multiply by $36$.", r"$3(T-3) + 2T = 36$, so $5T = 45$.", r"$T = 9$ days (A worked $6$, B worked $9$)."],
        "9 days"),
]

# =========================== apply ===========================
data = json.loads(TOPIC.read_text(encoding="utf-8"))
apply(data, "tw-basics", b_concept, b_notes, b_formulas, b_tricks, b_mistakes, b_revision, b_patterns)
apply(data, "tw-efficiency", e_concept, e_notes, e_formulas, e_tricks, e_mistakes, e_revision, e_patterns)
apply(data, "tw-man-days", m_concept, m_notes, m_formulas, m_tricks, m_mistakes, m_revision, m_patterns)
apply(data, "tw-cases", c_concept, c_notes, c_formulas, c_tricks, c_mistakes, c_revision, c_patterns)

ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]
assert len(ids) == len(set(ids)), "duplicate pattern ids in topic"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("time-work updated:", ", ".join(f"{s['id']}: {len(s['patterns'])} patterns" for s in data["subtopics"]))
