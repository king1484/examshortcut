"""Phase-2 deep content for quant/time-speed-distance — races module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F

from _lib import Sub


def build_races():
    S = Sub("tsd-races")

    S.notes = r"""### The language of races
Every race question uses one of four phrases. Decode them first, then it is plain arithmetic:

- "**A beats B by x metres**" — when A finishes the race (covers the full distance D), B is still x m from the finish, having run $D - x$.
- "**A beats B by t seconds**" — A finishes, and B needs t more seconds to finish.
- "**A gives B a start of x metres**" — B starts x m ahead of the common start line, so B runs only $D - x$.
- "**A gives B a start of t seconds**" — B starts running t seconds before A does.
A "**dead heat**" means both finish together.

### Beats by x metres → the speed ratio
When A finishes, B has covered $D - x$. Both ran for the same time, so
$$\frac{S_A}{S_B} = \frac{D}{D - x}$$
In a 100 m race A beats B by 10 m → $S_A : S_B = 100 : 90 = 10:9$. That ratio answers most follow-ups directly (who wins a longer race, by how much, start needed for a dead heat, and so on).

### Beats by t seconds / by both
- Beaten by t s: B covers D in $t_A + t$. If B's time is given, A's time is $t_B - t$; if A's time is given, B's is $t_A + t$.
- "**A beats B by 20 m or 5 s**" links them: B runs the final 20 m in 5 s → $S_B = \frac{20}{5} = 4$ m/s. Then A's time over D follows at once (200 m race: A runs 200 m while B runs 180 m, taking 45 s → $t_A = 45$ s, $S_A = \frac{40}{9}$ m/s).
- Race scores may quote the winner's time: A runs 100 m in 12 s while B takes 15 s → when A finishes, B has covered $\frac{100}{15} \times 12 = 80$ m → beaten by 20 m.

### Starts and handicaps
A start of x m to B in a race of D: B runs $D - x$ while A runs D. If the result is a dead heat, $\frac{S_A}{S_B} = \frac{D}{D-x}$ exactly as in a "beats by x" race — a start problem and a beats problem are the same arithmetic read in opposite directions. If A gives a start and still WINS by y m, B effectively ran $D - x - y$: e.g. A gives B 30 m in a 300 m race and wins by 45 m → $S_A : S_B = 300 : 225 = 4:3$.

### Games of 100 (chain rule)
"A can give B 20 points in a game of 100" means $S_A : S_B = 100 : 80$. Chain two such statements by multiplying:
A gives B 20 (in 100) and B gives C 10 (in 100): $\frac{A}{B} = \frac{100}{80}$, $\frac{B}{C} = \frac{100}{90}$ → when A scores 100, C scores $80 \times \frac{90}{100} = 72$ → A can give C 28 points.

### Chained races
"A beats B by 5 m in 100 m; B beats C by 8 m in 100 m" does NOT give A beats C by 13 m. Convert to ratios and multiply: $\frac{A}{B} = \frac{100}{95}$, $\frac{B}{C} = \frac{100}{92}$ → when A runs 100, C runs $95 \times \frac{92}{100} = 87.4$ → A beats C by 12.6 m.

### Common traps
- Adding the two margins in a chained race (13 instead of 12.6 m).
- Forgetting that a beaten runner still has to run the remaining x m in "or t seconds" statements.
- Treating a start of x m as if B ran the full distance.
- Comparing speeds before both runners have run for the SAME time.

### Quick revision
- Beats by x m → $S_A:S_B = D : (D-x)$.
- Beats by t s → $t_B = t_A + t$; "by x m or t s" → $S_B = \frac{x}{t}$.
- Start x m → B runs $D - x$; wins by y m after a start → B ran $D - x - y$.
- Chain margins through ratios, never by addition.
"""

    S.pattern("tsd-p17", "Race won by x metres", "very common",
        "'A beats B by x metres in a D-metre race' — the ratio of speeds, the margin in a different-length race, or the winner's speed is asked.",
        r"\frac{S_A}{S_B} = \frac{D}{D - x}",
        r"""1. At the moment A finishes, B has covered exactly $D - x$ in the same time.
2. Equal times cancel: the speeds are in the ratio $D : (D-x)$.
3. Use the ratio for any follow-up (B's speed from A's, new margins, dead-heat starts).

Why: 'beats by x' is just two runners observed over one common time interval.""",
        "In a 1 km race A beats B by 100 m. If A runs at 11 m/s, B's speed is:",
        r"$\frac{S_B}{S_A} = \frac{900}{1000}$ → $S_B = 9.9$ m/s.")
    S.pattern("tsd-p18", "Race won by t seconds, or by x m or t s", "very common",
        "'A beats B by t seconds' or the combined form 'by x metres or t seconds' — a finishing time or a speed is asked.",
        r"t_B = t_A + t; \qquad S_B = \frac{x}{t}",
        r"""1. 'By t s': the loser needs t more seconds after the winner finishes — $t_B = t_A + t$.
2. 'By x m or t s': the loser covers the last x m in exactly t s → $S_B = \frac{x}{t}$.
3. If the winner's time is known, $t_A$ is read off directly; otherwise compute the loser's full time first.

Why: the two phrasings describe the same finishing moment — x metres and t seconds are two views of the loser's final stretch.""",
        "In a 200 m race A beats B by 20 metres or 5 seconds. A's time over the race is:",
        r"$S_B = \frac{20}{5} = 4$ m/s → B's full time $= \frac{200}{4} = 50$ s → A's time $= 50 - 5 = 45$ s.")
    S.pattern("tsd-p19", "Starts and handicaps", "common",
        "A runner is given a head start (x metres or t seconds), and the outcome — dead heat, win margin, or the start needed — is asked.",
        r"\text{B runs } D - x; \qquad \text{wins by } y \Rightarrow S_A:S_B = D : (D - x - y)",
        r"""1. Write how far each runner actually runs: the favoured runner runs $D - x$.
2. Dead heat → the two distances are covered in equal time → ratio $D : (D-x)$.
3. If the giver still wins by y m, subtract that too: B covers $D - x - y$.

Why: a start shortens one runner's course; the win margin shortens it further at the finish.""",
        "In a 300 m race A gives B a start of 30 m and still beats him by 45 m. The ratio of their speeds is:",
        r"B runs $300 - 30 - 45 = 225$ m while A runs 300 → $S_A : S_B = 300 : 225 = 4 : 3$.")
    S.pattern("tsd-p20", "Games of points / chained races", "common",
        "'A can give B p points in a game of N' chains, or two consecutive race margins (A over B, B over C) combine into A over C.",
        r"\frac{S_A}{S_B} = \frac{N}{N-p}; \qquad \frac{S_A}{S_C} = \frac{S_A}{S_B} \times \frac{S_B}{S_C}",
        r"""1. Convert every statement into a ratio: giving p points in a game of N means $N : (N - p)$.
2. Multiply the ratios along the chain — never add the margins.
3. Read the combined margin off the final ratio: when A scores N, the last runner scores $N \times \prod \frac{N - p_i}{N}$.

Why: margins compose multiplicatively because each link compares distances run in a common time.""",
        "In a game of 100, A can give B 20 points and B can give C 10 points. How many points can A give C in a game of 100?",
        r"$\frac{A}{B} = \frac{100}{80}$, $\frac{B}{C} = \frac{100}{90}$ → when A has 100, C has $80 \times \frac{90}{100} = 72$ → A gives C 28.")

    # ---- practice (tsd-races) ----
    assert F(100, 90) == F(10, 9)
    S.q("tsd-p17", "easy",
        "In a 100 m race A beats B by 10 metres. The ratio of the speeds of A and B is:",
        ["10 : 9", "9 : 10", "11 : 10", "10 : 11"], "10 : 9",
        r"When A finishes, B has run 90 m in the same time → $S_A : S_B = 100 : 90 = 10 : 9$.",
        None, 25)
    assert F(200, 175) == F(8, 7)
    S.q("tsd-p17", "easy",
        "In a 200 m race A beats B by 25 metres. The ratio of the speeds of A and B is:",
        ["8 : 7", "7 : 8", "9 : 8", "8 : 9"], "8 : 7",
        r"$S_A : S_B = 200 : 175 = 8 : 7$.",
        None, 25)
    assert F(100, 15) * 12 == 80
    S.q("tsd-p18", "easy",
        "A runs 100 m in 12 seconds and B runs 100 m in 15 seconds. By how many metres does A beat B?",
        ["20 m", "25 m", "15 m", "18 m"], "20 m",
        r"In 12 s B covers $\frac{100}{15} \times 12 = 80$ m → A beats B by 20 m.",
        None, 30)
    assert F(100, 90) == F(10, 9)
    S.q("tsd-p19", "easy",
        "In a 100 m race, A gives B a start of 10 m and the race ends in a dead heat. The ratio of the speeds of A and B is:",
        ["10 : 9", "9 : 10", "10 : 11", "11 : 9"], "10 : 9",
        r"B runs 90 m while A runs 100 m in the same time → $S_A : S_B = 100 : 90 = 10 : 9$.",
        None, 25)
    assert F(20, 5) == 4 and F(200, 4) - 5 == 45
    S.q("tsd-p18", "medium",
        "In a 200 m race A beats B by 20 metres or 5 seconds. A's time over the course is:",
        ["45 s", "40 s", "50 s", "42.5 s"], "45 s",
        r"$S_B = \frac{20}{5} = 4$ m/s → B's time $= 50$ s → A's time $= 50 - 5 = 45$ s.",
        None, 45)
    assert F(300, 160) == F(15, 8)
    S.q("tsd-p19", "medium",
        "In a 200 m race A gives B a start of 20 m and then beats him by 20 m. The ratio of the speeds of A and B is:",
        ["5 : 4", "4 : 5", "6 : 5", "11 : 9"], "5 : 4",
        r"B effectively runs $200 - 20 - 20 = 160$ m while A runs 200 → $S_A : S_B = 200 : 160 = 5 : 4$.",
        None, 45)
    c = F(80, 100) * 90
    assert 100 - c == 28
    S.q("tsd-p20", "medium",
        "In a game of 100 points, A can give B 20 points and B can give C 10 points. In a game of 100 points, A can give C:",
        ["28 points", "30 points", "25 points", "32 points"], "28 points",
        r"When A scores 100, B scores 80; when B scores 100, C scores 90 → C scores $80 \times \frac{90}{100} = 72$. Margin $= 100 - 72 = 28$.",
        "Chain through ratios — 20 + 10 = 30 is the classic wrong answer.", 45)
    assert F(11) * F(900, 1000) == F(99, 10)
    S.q("tsd-p17", "medium",
        "In a 1 km race A beats B by 100 m. If A runs at 11 m/s, B's speed is:",
        ["9.9 m/s", "10 m/s", "9.5 m/s", "10.1 m/s"], "9.9 m/s",
        r"$S_B = 11 \times \frac{900}{1000} = 9.9$ m/s.",
        None, 35)
    assert F(400, 44) * F(360, 400) == F(90, 11) and abs(float(F(360, 100 / F(11))) - 39.6) < 1e-9
    S.q("tsd-p18", "hard",
        "In a 400 m race A beats B by 40 m. If B's time for the race is 44 seconds, A's time for the race is:",
        ["39.6 s", "40 s", "38.5 s", "41 s"], "39.6 s",
        r"""$S_B = \frac{400}{44} = \frac{100}{11}$ m/s.
When A finishes, B has run 360 m → time $= \frac{360}{100/11} = 39.6$ s.""",
        None, 55)
    c = 95 * F(92, 100)
    assert 100 - c == F(63, 5)
    S.q("tsd-p20", "hard",
        "In a 100 m race A beats B by 5 metres, and in a 100 m race B beats C by 8 metres. By how many metres will A beat C in a 100 m race?",
        ["12.6 m", "13 m", "12 m", "11.6 m"], "12.6 m",
        r"""$\frac{B}{C} = \frac{100}{92}$ → when A runs 100, B runs 95 and C runs $95 \times \frac{92}{100} = 87.4$ m.
Margin $= 100 - 87.4 = 12.6$ m.""",
        None, 55)
    rem = (300 - 30) - 6 * F(300, 8)
    assert rem == 45
    S.q("tsd-p19", "medium",
        "A runs at 8 m/s and B at 6 m/s. In a 300 m race, A gives B a start of 30 m. By what distance does A win?",
        ["45 m", "40 m", "50 m", "35 m"], "45 m",
        r"""A's time $= \frac{300}{8} = 37.5$ s. B covers $6 \times 37.5 = 225$ m of his 270 m course.
B is short of the finish by $270 - 225 = 45$ m → A wins by 45 m.""",
        None, 45)
    return S
