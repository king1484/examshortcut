"""Readable rewrite of Percentage (all five subtopics).

Simple English, one idea per section. Every number in every example is
recomputed below with exact fractions and asserted.
Run: python percentage.py   (patches content/core/topics/quant/percentage.json in place)
"""
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "percentage.json"

# ---------- answer checks: pct-basics ----------
assert F(35, 100) * 200 == 70
assert F(1, 8) * 960 == 120                    # 12.5% of 960
assert F(1, 6) * 720 == 120                    # 16 2/3% of 720
assert F(24, 100) * 650 == 156                 # 24% of 650
assert 650 * F(1, 10) * 2 + 650 * F(1, 100) * 4 == 156
assert F(4, 100) * 25 == 1                     # x% of y = y% of x
assert F(189 * 100, 35) == 540 and F(189, 35) == F(27, 5)
assert F(80, 100) * 540 == 432
assert F(5, 16) * 100 == F(125, 4)             # 31.25
assert F(126, 720) == F(7, 40) and F(7, 40) * 100 == F(35, 2)   # 17.5
assert F(625, 1000) == F(5, 8) and F(5, 8) * 240 == 150 and 240 - 150 == 90
assert F(30, 40) * 100 == 75

# ---------- answer checks: pct-change ----------
assert F(2700, 18000) * 100 == 15
assert F(50, 250) * 100 == 20 and F(50, 200) * 100 == 25
assert 18000 * F(23, 20) == 20700
assert F(6, 5) * F(9, 10) == F(27, 25) and (F(27, 25) - 1) * 100 == 8
assert 15 + 12 + F(15 * 12, 100) == F(144, 5) and F(144, 5) == F(288, 10)   # 28.8
assert F(23, 20) * F(28, 25) == F(161, 125) and (F(161, 125) - 1) * 100 == F(144, 5)
assert F(6, 5) * F(4, 5) == F(24, 25) and (1 - F(24, 25)) * 100 == 4
assert F(11, 10) * F(9, 10) == F(99, 100)
assert 50000 * F(4, 5) == 40000                # undo -20%
assert 8100 * F(10, 9) ** 2 == 10000
assert 720 * F(10, 9) * F(5, 4) == 1000
assert 3500 * F(8, 7) == 4000                  # undo -12.5%
assert F(3, 2) / F(3, 4) == 2
assert F(11, 10) * F(6, 5) * F(3, 4) == F(99, 100) and (1 - F(99, 100)) * 100 == 1

# ---------- answer checks: pct-more-less ----------
assert F(25, 125) * 100 == 20
assert F(100 * 25, 75) == F(100, 3)            # 25% less -> 33 1/3% more
assert F(100 * 50, 150) == F(100, 3)           # 50% more -> 33 1/3% less
assert F(100 * 100, 200) == 50                 # 100% more -> 50% less
assert F(100 * 60, 160) == F(75, 2)            # 60% more -> 37.5% less
assert F(100 * 20, 80) == 25                   # 20% less -> 25% more
assert F(100 * 75, 25) == 300                  # 75% less -> 300% more
assert F(300, 1200) * 100 == 25
assert F(40, 100) * F(25, 100) == F(1, 10)     # 25% of 40% = 10%
assert 1 + F(1, 6) == F(7, 6) and F(1, 7) * 100 == F(100, 7) == 14 + F(2, 7)
assert F(120, 150) * 100 == 80

# ---------- answer checks: pct-population-election ----------
assert 50000 * F(11, 10) ** 2 == 60500
assert 6400 * F(5, 4) ** 2 == 10000
assert 40000 * F(11, 10) * F(19, 20) == 41800
assert 80000 * F(21, 20) * F(9, 10) == 75600
assert 96000 * F(5, 4) * F(4, 5) == 96000
assert F(6, 5) * F(5, 4) * F(11, 10) == F(33, 20) and 66000 * F(20, 33) == 40000
assert F(4, 5) ** 2 == F(16, 25) and 16000 * F(16, 25) == 10240
assert F(9, 10) ** 2 == F(81, 100) and 12500 * F(81, 100) == 10125
assert 8100 * F(10, 9) ** 2 == 10000
assert F(10, 100) * 27000 == 2700 and 27000 - 2700 == 24300
assert F(20, 100) * 6000 == 1200 and 6000 * F(5, 4) == 7500
assert F(55, 100) * 12000 - F(45, 100) * 12000 == 1200
assert F(10, 100) * 12000 == 1200 and 12000 * F(5, 4) == 15000

# ---------- answer checks: pct-marks-income ----------
assert (45 + 15) * F(100, 45 - 33) == 500
assert F(33, 100) * 500 + 45 == 210 and F(45, 100) * 500 - 15 == 210
assert (152 - 20) * F(100, 30) == 440 and F(30, 100) * 440 + 20 == 152
assert F(20, 100) * 400 == 80 and 400 - 320 == 80
assert 400 * F(23, 20) == 460 and 320 * F(11, 10) == 352 and 460 - 352 == 108
assert F(108 - 80, 80) * 100 == 35
assert 1 / F(5, 4) == F(4, 5) and (1 - F(4, 5)) * 100 == 20
assert F(20, 100) * 20 == 4 and 20 - 4 == 16
assert F(400, 20) == 20 and F(400, 16) == 25 and 25 - 20 == 5


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ================= pct-basics =================

BASICS_CONCEPT = (
    "Per cent means 'out of every hundred'. So $25\\%$ means 25 parts out of every 100 parts, "
    "which is the same as $\\dfrac{1}{4}$.\n\n"
    "Every percentage is just a fraction. Turn the percent into a fraction first, and the "
    "question becomes plain arithmetic."
)

BASICS_NOTES = r"""### What per cent means
Per cent means "out of every hundred". $40\%$ means 40 parts taken out of every 100 parts.

- $40\% = \dfrac{40}{100} = \dfrac{2}{5}$
- $50\%$ is half, $100\%$ is the whole thing
- $200\%$ is double

> **Rule:** Before any calculation, write the percent as a fraction with 100 below. Then cancel.

### The fraction table
Exams reuse the same fractions again and again. Learn this table by heart; it saves a multiplication in almost every question.

| Fraction | Percent | | Fraction | Percent |
|---|---|---|---|---|
| $1/2$ | 50% | | $1/8$ | 12.5% |
| $1/3$ | 33 1/3% | | $1/9$ | 11 1/9% |
| $1/4$ | 25% | | $1/11$ | 9 1/11% |
| $1/5$ | 20% | | $1/12$ | 8 1/3% |
| $1/6$ | 16 2/3% | | $1/15$ | 6 2/3% |
| $1/7$ | 14 2/7% | | $1/16$ | 6.25% |
| $1/20$ | 5% | | $1/25$ | 4% |

Half the table comes free: $1/6$ is half of $1/3$, so $16\dfrac{2}{3}\%$ is half of $33\dfrac{1}{3}\%$.

- Fraction to percent: multiply by 100. $\dfrac{5}{16} \times 100 = 31.25\%$.
- Percent to fraction: put over 100 and cancel. $12.5\% = \dfrac{125}{1000} = \dfrac{1}{8}$.

### Finding a percentage of a number
$x\%$ of $N$ means $\dfrac{x}{100} \times N$.

$35\%$ of $200 = \dfrac{35}{100} \times 200 = 70$.

Use the table when the percent is in it. $12.5\%$ is $\dfrac{1}{8}$, so $12.5\%$ of $960 = 960 \div 8 = 120$. No big multiplication needed.

> **Example:** $16\dfrac{2}{3}\%$ of $720$: the percent is $\dfrac{1}{6}$, so the answer is $720 \div 6 = 120$.

### The 10% and 1% building blocks
Split an awkward percent into pieces of $10\%$ and $1\%$.

1. $10\%$ of a number: move the decimal point one place left.
2. $1\%$ of a number: move it two places left.
3. Add pieces until you build the percent you need.

$24\%$ of $650$: two $10\%$ pieces give $130$, four $1\%$ pieces give $26$, total $156$.

> **Tip:** $x\%$ of $y$ always equals $y\%$ of $x$. So $4\%$ of $25$ equals $25\%$ of $4$, which is clearly $1$.

### Finding the whole from a part
Here the question gives a piece of a number and its percent. The full number is asked.

> **Rule:** whole $=$ part $\times\ 100 \div$ percent.

$35\%$ of a number is $189$. So the number is $189 \times \dfrac{100}{35} = 540$. Then $80\%$ of it is $\dfrac{4}{5} \times 540 = 432$.

Sanity check: the whole (540) must be bigger than the part (189), because $35\%$ is less than the whole.

### One quantity as a percentage of another
"A is what per cent of B?" means $\dfrac{A}{B} \times 100$. The quantity after "of" goes below the line.

In a batch of 720 applications, 126 were rejected. Rejected applications are $\dfrac{126}{720} \times 100 = 17.5\%$ of the batch.

> **Watch:** The number after "of" is the base. Swap the two numbers and the answer changes.

### The remaining part of a hundred
Percentages of the same whole add up to $100\%$.

Out of 240 students, $62.5\%$ attended a function. So $37.5\%$ were absent, and $37.5\% = \dfrac{3}{8}$. Absent students $= \dfrac{3}{8} \times 240 = 90$.

> **Note:** Equal-percent statements also link two wholes. If $40\%$ of A $= 30\%$ of B, then $0.4A = 0.3B$, so $A = 75\%$ of B.
"""

BASICS_FORMULAS = [
    {"name": "x% of a number", "tex": r"\frac{x}{100} \times N", "note": "Turn the percent into a fraction first; cancel where you can."},
    {"name": "Whole from a part", "tex": r"\text{whole} = \frac{\text{part} \times 100}{x}", "note": "x is the percent that the part stands for."},
    {"name": "A as a percent of B", "tex": r"\frac{A}{B} \times 100\%", "note": "B is the quantity that follows the word 'of'."},
    {"name": "Remaining part", "tex": r"\text{rest} = 100\% - \text{given}\%", "note": "Only when both percentages are of the same whole."},
]

BASICS_TRICKS = [
    {
        "title": "Let the fraction table do the division",
        "body": "Replace the percent with its fraction from the table. $12.5\%$ becomes $\\dfrac{1}{8}$, so the sum turns into a simple division.",
        "example": {
            "q": "What is 12.5% of 960?",
            "steps": [r"$12.5\% = \dfrac{1}{8}$.", r"$960 \div 8 = 120$."],
            "answer": "120",
        },
    },
    {
        "title": "Build the percent from 10% and 1% pieces",
        "body": "Move the decimal point for $10\%$ and $1\%$, then add pieces. Works without pen-and-paper multiplication.",
        "example": {
            "q": "What is 24% of 650?",
            "steps": [r"$10\%$ of $650 = 65$; two pieces give $130$.", r"$1\%$ of $650 = 6.5$; four pieces give $26$.", r"$130 + 26 = 156$."],
            "answer": "156",
        },
    },
    {
        "title": "Swap x% of y into y% of x",
        "body": "$x\%$ of $y$ always equals $y\%$ of $x$. Swap when one side turns into a friendly percent.",
        "example": {
            "q": "What is 4% of 25?",
            "steps": [r"Swap: $4\%$ of $25 = 25\%$ of $4$.", r"$25\%$ of $4 = 1$."],
            "answer": "1",
        },
    },
]

BASICS_MISTAKES = [
    {"wrong": "In 'A is what per cent of B', putting A below the line.",
     "right": "The quantity after 'of' is the base: $A \\div B \\times 100$."},
    {"wrong": r"Treating $16\dfrac{2}{3}\%$ as roughly $16.3\%$.",
     "right": r"It is exactly $\dfrac{1}{6}$. Use the fraction from the table."},
    {"wrong": "Turning a fraction into a percent by dividing by 100.",
     "right": "Multiply by 100: $1/4$ becomes $25\\%$."},
    {"wrong": "Reading $0.5\%$ as $5\%$.",
     "right": "$0.5\%$ is half of one per cent, that is $\\dfrac{1}{200}$ of the number."},
    {"wrong": "Adding percents of different wholes in one line.",
     "right": "Percents add only when they are percents of the same whole."},
    {"wrong": "Finding the whole by multiplying the part by the percent.",
     "right": "Divide instead: whole $=$ part $\\times 100 \\div$ percent."},
]

BASICS_REVISION = [
    "Per cent means out of every hundred: $x\\% = \\dfrac{x}{100}$.",
    "$x\\%$ of $N = \\dfrac{x}{100} \\times N$.",
    "Table: $1/8 = 12.5\\%$, $1/6 = 16\\dfrac{2}{3}\\%$, $1/7 = 14\\dfrac{2}{7}\\%$.",
    "Whole $=$ part $\\times 100 \\div$ percent.",
    "A as a per cent of B: $A \\div B \\times 100$; the number after 'of' stays below.",
    "Percents of the same whole add to $100\\%$.",
    "$x\\%$ of $y = y\\%$ of $x$.",
]

BASICS_PATTERNS = [
    pat("pct-b1", "Find x% of a number", "very common",
        "A number is given and a percentage of it is asked: 'What is 24% of 650?'",
        r"\frac{x}{100} \times N",
        ["Turn the percent into a fraction over 100.", "Cancel it to a table fraction when possible.",
         "Multiply by the number.", "Check size: the answer should look like a fraction of the number."],
        "A percent is only a fraction, so taking a percent means taking that fraction of the number.",
        "What is 24% of 650?",
        [r"$24\%$ of $650$: two $10\%$ pieces give $130$.", r"Four $1\%$ pieces give $26$.", r"$130 + 26 = 156$."],
        "156"),
    pat("pct-b2", "Find the number when a percent of it is given", "very common",
        "'35% of a number is 189.' The number itself, or a second percent of it, is asked.",
        r"\text{whole} = \frac{\text{part} \times 100}{x}",
        ["Write whole = part x 100 / percent.", "Cancel before multiplying.",
         "Use this whole for any follow-up asked."],
        "The part is a known fraction of the whole, so dividing by that fraction recovers the whole.",
        "35% of a number is 189. What is 80% of that number?",
        [r"Whole $= 189 \times \dfrac{100}{35} = 540$.", r"$80\%$ of $540 = \dfrac{4}{5} \times 540 = 432$."],
        "432"),
    pat("pct-b3", "Change a fraction into a percentage", "common",
        "'Express 5/16 as a percentage', or options are all in percent.",
        r"\frac{a}{b} \times 100\%",
        ["Multiply the fraction by 100.", "Cancel before you multiply.", "Write the result as a decimal or mixed number."],
        "Percent is a fraction with 100 below, so scaling the fraction to 100 gives the percent.",
        "Express $\\dfrac{5}{16}$ as a percentage.",
        [r"$\dfrac{5}{16} \times 100 = \dfrac{500}{16}$.", r"$\dfrac{500}{16} = 31.25$."],
        "31.25%"),
    pat("pct-b4", "One quantity as a percentage of another", "common",
        "'126 out of 720 applications were rejected.' What percentage one quantity is of another is asked.",
        r"\frac{A}{B} \times 100\%",
        ["Put the quantity being asked about on top.", "Put the total, the quantity after 'of', below.",
         "Multiply by 100 and simplify."],
        "The percent says how many per hundred the top quantity is of the bottom one.",
        "In a batch of 720 applications, 126 were rejected. What percentage of the applications was rejected?",
        [r"$\dfrac{126}{720} = \dfrac{7}{40}$.", r"$\dfrac{7}{40} \times 100 = 17.5$."],
        "17.5%"),
    pat("pct-b5", "The remaining percentage", "common",
        "A part is described by a percent and the rest is asked: '62.5% attended. How many were absent?'",
        None,
        ["Subtract the given percent from 100.", "Turn the remainder into a table fraction.", "Multiply by the total."],
        "The two parts split the same total, so their percents add to 100.",
        "Out of 240 students, 62.5% attended the annual function. How many students did not attend?",
        [r"Absent $= 100\% - 62.5\% = 37.5\% = \dfrac{3}{8}$.", r"$\dfrac{3}{8} \times 240 = 90$."],
        "90 students"),
    pat("pct-b6", "Equal percent statements", "occasional",
        "'If 40% of A equals 30% of B...' Two different wholes are joined by one equation.",
        r"\frac{x}{100}A = \frac{y}{100}B \Rightarrow A = \frac{y}{x}B",
        ["Drop the percents and write the equation: 0.4A = 0.3B.", "Solve for the ratio A over B.",
         "Turn the ratio into a percent."],
        "Two equal products fix the ratio of A and B, so one percent of the other follows.",
        "If 40% of A is equal to 30% of B, then A is what percentage of B?",
        [r"$0.4A = 0.3B$", r"$\dfrac{A}{B} = \dfrac{0.3}{0.4} = \dfrac{3}{4}$.", r"$\dfrac{3}{4} \times 100 = 75$."],
        "75%"),
]

# ================= pct-change =================

CHANGE_CONCEPT = (
    "A percentage change compares a new value with an old value. The **old** value is always the base, "
    "so it stays below the line.\n\n"
    "The fast method: turn each change into a **multiplier**. $+20\\%$ means $\\times \\dfrac{6}{5}$, "
    "$-10\\%$ means $\\times \\dfrac{9}{10}$. Chain changes by multiplying multipliers."
)

CHANGE_NOTES = r"""### Change is measured against the old value
Per cent change $= \dfrac{\text{new} - \text{old}}{\text{old}} \times 100$. The old value sits below the line.

A shop's sales rose from 18,000 to 20,700. Change $= 2700$, and $\dfrac{2700}{18000} \times 100 = 15\%$.

> **Rule:** Old value below, always. Ask yourself "which number came first?" before dividing.

> **Watch:** 250 growing to 300 is $+20\%$, but 200 growing to 250 is $+25\%$. The same 50 gives different percents because the bases differ.

### Multipliers: the fastest method
Do not add and subtract in steps. Multiply by one fraction per change.

| Change | Multiplier | | Change | Multiplier |
|---|---|---|---|---|
| $+10\%$ | $11/10$ | | $-10\%$ | $9/10$ |
| $+20\%$ | $6/5$ | | $-20\%$ | $4/5$ |
| $+25\%$ | $5/4$ | | $-25\%$ | $3/4$ |
| $+50\%$ | $3/2$ | | $-50\%$ | $1/2$ |

$18000 \times \dfrac{23}{20} = 20700$: a $15\%$ rise in one multiplication, and $+15\%$ or $-15\%$ both come from the chips $23/20$ and $17/20$.

To undo a change, divide by the same multiplier. $-20\%$ turned 50,000 into 40,000, so $40000 \div \dfrac{4}{5} = 50000$.

### Two changes one after the other
Multiply the two multipliers, or use one formula.

$$\text{net change} = a + b + \frac{ab}{100}$$

Here $a$ and $b$ carry their own signs. $+15\%$ then $+12\%$: $15 + 12 + \dfrac{15 \times 12}{100} = 28.8\%$, a rise.

With multipliers: $\dfrac{23}{20} \times \dfrac{28}{25} = \dfrac{161}{125} = 1.288$, the same $+28.8\%$.

$+20\%$ then $-10\%$: $\dfrac{6}{5} \times \dfrac{9}{10} = \dfrac{27}{25}$, a net rise of $8\%$.

> **Careful:** Never just add the percents. $20\%$ up and $10\%$ down is not $10\%$ up.

### The round trip: x% up then x% down
Raise a value by $x\%$ and then cut it by $x\%$. It does not come back.

$$\text{net loss} = \left(\frac{x}{10}\right)^2 \%$$

$10\%$ up then $10\%$ down: $\dfrac{11}{10} \times \dfrac{9}{10} = \dfrac{99}{100}$, a $1\%$ loss.
$20\%$ up then $20\%$ down: $\dfrac{6}{5} \times \dfrac{4}{5} = \dfrac{24}{25}$, a $4\%$ loss.

> **Note:** The order does not matter. Up first or down first, the loss is the same $x^2/100$ per cent.

### Getting the original back
If a value fell or rose and the final value is given, divide by the multiplier to undo the change.

A number became 8,100 after two yearly falls of $10\%$. Two chips of $9/10$ were used, so the original $= 8100 \times \dfrac{10}{9} \times \dfrac{10}{9} = 10000$.

A number is decreased by $10\%$, then by $20\%$, and becomes 720. Original $= 720 \times \dfrac{10}{9} \times \dfrac{5}{4} = 1000$.

> **Watch:** To undo $+20\%$, divide by $1.2$. Subtracting $20\%$ back is wrong.

### When the top and bottom of a fraction change
A fraction's value changes by the top's chip divided by the bottom's chip.

The numerator rises $50\%$ (chip $3/2$) and the denominator falls $25\%$ (chip $3/4$):
$$\text{new value} = \text{old} \times \frac{3/2}{3/4} = \text{old} \times 2$$
The fraction doubles.

> **Example:** Numerator $+20\%$ (chip $6/5$), denominator $-10\%$ (chip $9/10$): value $ \times \dfrac{6/5}{9/10} = \dfrac{4}{3}$, a $33\dfrac{1}{3}\%$ rise.
"""

CHANGE_FORMULAS = [
    {"name": "Per cent change", "tex": r"\frac{\text{new} - \text{old}}{\text{old}} \times 100", "note": "Old value below the line."},
    {"name": "Multiplier", "tex": r"\text{new} = \text{old} \times \frac{100 \pm x}{100}", "note": "Plus for a rise, minus for a fall."},
    {"name": "Successive changes", "tex": r"a + b + \frac{ab}{100}", "note": "a and b carry their own signs."},
    {"name": "Same x% up and down", "tex": r"\text{net loss} = \frac{x^2}{100}\%", "note": "x% rise followed by x% cut."},
    {"name": "Fraction with both parts changed", "tex": r"\text{new} = \text{old} \times \frac{\text{top chip}}{\text{bottom chip}}"},
]

CHANGE_TRICKS = [
    {
        "title": "One multiplication per change",
        "body": "Replace every rise or fall with its multiplier fraction and multiply once. This replaces three lines of working.",
        "example": {
            "q": "A price fell by 12.5% to Rs 3,500. What was the price before the fall?",
            "steps": [r"$-12.5\%$ means the chip $\dfrac{7}{8}$.", r"Original $= 3500 \times \dfrac{8}{7} = 4000$."],
            "answer": "Rs 4,000",
        },
    },
    {
        "title": "a + b + ab/100 for two changes",
        "body": "Two changes in a row combine by this one formula. Keep the signs of both percents.",
        "example": {
            "q": "A value rises by 15% and then by 12%. What is the net percentage change?",
            "steps": [r"$15 + 12 + \dfrac{15 \times 12}{100}$", r"$= 27 + 1.8 = 28.8$"],
            "answer": "28.8% increase",
        },
    },
    {
        "title": "Round trip loses x squared over 100",
        "body": "A rise of x% followed by a cut of x% always ends below the start, by exactly $\\dfrac{x^2}{100}$ per cent.",
        "example": {
            "q": "A price is raised by 20% and then reduced by 20%. What is the net change?",
            "steps": [r"Loss $= \dfrac{20 \times 20}{100} = 4$ per cent.", r"Chips check: $\dfrac{6}{5} \times \dfrac{4}{5} = \dfrac{24}{25}$."],
            "answer": "4% decrease",
        },
    },
]

CHANGE_MISTAKES = [
    {"wrong": "Adding percents of different bases: $20\%$ up then $10\%$ down called $10\%$ up.",
     "right": "Combine with multipliers or $a + b + \\dfrac{ab}{100}$ with signs."},
    {"wrong": "Measuring change against the new value.",
     "right": "The old value is the base. Divide the difference by the old value."},
    {"wrong": "Undoing a $20\%$ rise by subtracting $20\%$.",
     "right": "Divide by the multiplier: $\\text{new} \\div 1.2$."},
    {"wrong": "Undoing a fall with the wrong chip, e.g. $\\times 0.9$ for a $10\%$ fall.",
     "right": "A fall used $9/10$; undo it with $\\times \\dfrac{10}{9}$."},
    {"wrong": "Calling an up-then-down round trip 'no change'.",
     "right": "It always loses $\\dfrac{x^2}{100}$ per cent."},
    {"wrong": "Applying $+10\%$ twice and calling it $+20\%$.",
     "right": "$1.1 \times 1.1 = 1.21$, a $21\%$ rise."},
]

CHANGE_REVISION = [
    "Per cent change $=$ difference $\\div$ old $\\times 100$.",
    "Rise $x\%$: multiply by $\\dfrac{100+x}{100}$; fall: $\\dfrac{100-x}{100}$.",
    "Two changes: multiply the multipliers, or $a + b + \\dfrac{ab}{100}$.",
    "$x\%$ up then $x\%$ down $= \\dfrac{x^2}{100}\%$ net loss.",
    "Undo a change by dividing by the same multiplier.",
    "Fraction value $\\times$ top chip $\\div$ bottom chip.",
]

CHANGE_PATTERNS = [
    pat("pct-c1", "Percentage increase or decrease", "very common",
        "Two values of the same thing are given and the per cent change is asked.",
        r"\frac{\text{new} - \text{old}}{\text{old}} \times 100",
        ["Find the difference between the new and old values.", "Put the old value below.",
         "Multiply by 100 and attach increase or decrease."],
        "Per cent change states the difference as a part of the starting value.",
        "A shop's monthly sales rose from Rs 18,000 to Rs 20,700. What was the percentage increase?",
        [r"Difference $= 20700 - 18000 = 2700$.", r"$\dfrac{2700}{18000} \times 100 = 15$."],
        "15%"),
    pat("pct-c2", "Two successive changes", "very common",
        "A value changes twice in a row and the net change is asked: '+20% and then -10%'.",
        r"a + b + \frac{ab}{100}",
        ["Write both percents with their signs.", "Add them and add ab/100 as well.",
         "State rise or fall from the sign.", "Cross-check by multiplying the two multipliers."],
        "The second change acts on the changed value, so a small cross term ab/100 appears.",
        "A number is increased by 20% and then decreased by 10%. What is the net percentage change?",
        [r"$a = 20$, $b = -10$.", r"$20 - 10 + \dfrac{20 \times (-10)}{100} = 10 - 2 = 8$.", r"Chips: $\dfrac{6}{5} \times \dfrac{9}{10} = \dfrac{27}{25}$, so $+8\%$."],
        "8% increase"),
    pat("pct-c3", "Same x% up and then down", "common",
        "A value rises by x% and falls by the same x%; the net effect is asked.",
        r"\left(\frac{x}{10}\right)^2 \% \text{ loss}",
        ["Square x.", "Divide by 100.", "State it as a net loss."],
        "The two chips multiply to $1 - \\dfrac{x^2}{10000}$, always a shade below 1.",
        "The price of an article is raised by 20% and then reduced by 20%. What is the net change in price?",
        [r"Loss $= \dfrac{20 \times 20}{100} = 4$ per cent.", r"Chips: $\dfrac{6}{5} \times \dfrac{4}{5} = \dfrac{24}{25}$."],
        "4% decrease"),
    pat("pct-c4", "Find the original value", "very common",
        "A value after some change is given and the value before the change is asked.",
        r"\text{original} = \text{final} \times \frac{100}{100 \pm x}",
        ["Write the multiplier for each change that happened.", "Divide the final value by the product of the multipliers.",
         "Check by applying the changes to your answer."],
        "Changes were multiplications, so undoing them is division by the same multipliers.",
        "A number is first decreased by 10% and then decreased by 20%. The result is 720. What was the original number?",
        [r"Chips used: $\dfrac{9}{10}$ and $\dfrac{4}{5}$.", r"$720 \times \dfrac{10}{9} = 800$.", r"$800 \times \dfrac{5}{4} = 1000$."],
        "1000"),
    pat("pct-c5", "Numerator and denominator both change", "occasional",
        "A fraction's top and bottom are each changed by a percent and the effect on the fraction is asked.",
        r"\text{new} = \text{old} \times \frac{\text{top chip}}{\text{bottom chip}}",
        ["Write the chip for the numerator's change.", "Write the chip for the denominator's change.",
         "Multiply the old fraction by top chip over bottom chip."],
        "The top scales the fraction up and the bottom scales it down, so the chips divide.",
        "In a fraction the numerator is increased by 50% and the denominator is decreased by 25%. The new fraction is how many times the old one?",
        [r"Top chip $= \dfrac{3}{2}$, bottom chip $= \dfrac{3}{4}$.", r"Factor $= \dfrac{3/2}{3/4} = 2$."],
        "2 times"),
    pat("pct-c6", "Three or more successive changes", "occasional",
        "Three changes are applied one after another and the net effect is asked.",
        None,
        ["Write a multiplier for each change.", "Multiply all the multipliers together.",
         "Compare the product with 1 to get the net per cent."],
        "Multipliers keep working for any number of changes; only the multiplication grows.",
        "A value is increased by 10%, then increased by 20%, and then decreased by 25%. What is the net percentage change?",
        [r"Chips: $\dfrac{11}{10}$, $\dfrac{6}{5}$, $\dfrac{3}{4}$.", r"Product $= \dfrac{11}{10} \times \dfrac{6}{5} \times \dfrac{3}{4} = \dfrac{99}{100}$.", r"$0.99$ means a $1\%$ fall."],
        "1% decrease"),
]

# ================= pct-more-less =================

MORELESS_CONCEPT = (
    "'A is $25\\%$ more than B' compares A with B, so B is the base. Said the other way round, "
    "B is compared with A, and the answer is different: B is $20\\%$ less than A.\n\n"
    "This subtopic is about flipping such statements both ways, quickly and correctly."
)

MORELESS_NOTES = r"""### The base decides the answer
Take "A is $25\%$ more than B". Put B at 100, so A is 125.

Now read it backwards: B is less than A by $25$ out of $125$, and $\dfrac{25}{125} \times 100 = 20\%$. So B is $20\%$ less than A.

Same pair, two different percents. The base changed.

> **Rule:** The quantity after "than" is the base. Flip the statement and the base flips too.

### The two flip formulas
You do not need to test with 100 every time.

$$x\% \text{ more} \Rightarrow \frac{100x}{100+x}\% \text{ less}$$
$$x\% \text{ less} \Rightarrow \frac{100x}{100-x}\% \text{ more}$$

Check with 25: $25\%$ more becomes $\dfrac{100 \times 25}{125} = 20\%$ less. And $20\%$ less becomes $\dfrac{100 \times 20}{80} = 25\%$ more.

> **Watch:** $25\%$ more and $25\%$ less are not a matching pair. Their partners are $20\%$ less and $33\dfrac{1}{3}\%$ more.

### Set the base to 100
When unsure, do not trust memory of formulas. Build the numbers.

"A's salary is $60\%$ more than B's." B $= 100$, A $= 160$. B is less by $\dfrac{60}{160}$ of A, and $\dfrac{60}{160} \times 100 = 37.5\%$.

> **Example:** A town's population fell from 1,500 to 1,200. The rise needed to get back: $\dfrac{300}{1200} \times 100 = 25\%$. The fall was only $\dfrac{300}{1500} = 20\%$.

### Pairs worth memorising
The same pairs appear every year. Learn the table and skip the working.

| Statement | Reverse |
|---|---|
| $25\%$ more | $20\%$ less |
| $20\%$ more | $16\dfrac{2}{3}\%$ less |
| $50\%$ more | $33\dfrac{1}{3}\%$ less |
| $100\%$ more | $50\%$ less |
| $25\%$ less | $33\dfrac{1}{3}\%$ more |
| $20\%$ less | $25\%$ more |
| $75\%$ less | $300\%$ more |

> **Tip:** Every pair multiplies back to itself. Undoing a change is the flip question in disguise.

### Chains of percentages
"A $40\%$ of B" language means multiply.

" $40\%$ of the candidates are graduates, and $25\%$ of the graduates are engineers." Engineers $= \dfrac{25}{100} \times \dfrac{40}{100} = \dfrac{1}{10} = 10\%$ of all candidates.

> **Note:** Each "of" starts from the group named just before it, not from the total.

### Awkward percents through fractions
Third-sixths and sevenths flip best as fractions.

$16\dfrac{2}{3}\%$ more means $\times \dfrac{7}{6}$. Reversed, that is less by $\dfrac{1}{7}$, and $\dfrac{1}{7} \times 100 = 14\dfrac{2}{7}\%$.

"X is $16\dfrac{2}{3}\%$ more than Y" and "Y is $14\dfrac{2}{7}\%$ less than X" are the same fact.

> **Careful:** $14\dfrac{2}{7}\%$ is exact, not approximately 14.2. Keep it as the fraction $1/7$.
"""

MORELESS_FORMULAS = [
    {"name": "x% more, reversed", "tex": r"\frac{100x}{100+x}\% \text{ less}", "note": "x% more than becomes this much less than."},
    {"name": "x% less, reversed", "tex": r"\frac{100x}{100-x}\% \text{ more}", "note": "x% less than becomes this much more than."},
    {"name": "Per cent of a per cent", "tex": r"\frac{a}{100} \times \frac{b}{100} = \frac{ab}{10000}", "note": "Each 'of' multiplies."},
]

MORELESS_TRICKS = [
    {
        "title": "Memorise the standard pairs",
        "body": "Four pairs cover most papers: 25/20, 20/$16\\dfrac{2}{3}$, 50/$33\\dfrac{1}{3}$, and 100/50. Read the question, write the partner, done.",
        "example": {
            "q": "If A's income is 20% less than B's, then B's income is more than A's by:",
            "steps": [r"$x\%$ less reverses to $\dfrac{100x}{100 - x}\%$ more.", r"$\dfrac{100 \times 20}{80} = 25$."],
            "answer": "25%",
        },
    },
    {
        "title": "Base-100 when memory fails",
        "body": "Put the base quantity at 100, write the other quantity, and divide by the new base. Slow but never wrong.",
        "example": {
            "q": "A's salary is 60% more than B's. B's salary is less than A's by what percentage?",
            "steps": [r"B $= 100$, so A $= 160$.", r"Gap $= 60$ over base $160$.", r"$\dfrac{60}{160} \times 100 = 37.5$."],
            "answer": "37.5%",
        },
    },
    {
        "title": "Awkward percents: use the fraction",
        "body": "$16\\dfrac{2}{3}\%$ is $1/6$, so 'more by $1/6$' reverses to 'less by $1/7$' of the bigger number.",
        "example": {
            "q": "X is 16 2/3% more than Y. By what percentage is Y less than X?",
            "steps": [r"$16\dfrac{2}{3}\% = \dfrac{1}{6}$, so X $= \dfrac{7}{6}$ Y.", r"Y $= \dfrac{6}{7}$ X, less by $\dfrac{1}{7}$.", r"$\dfrac{1}{7} \times 100 = 14\dfrac{2}{7}$."],
            "answer": "14 2/7%",
        },
    },
]

MORELESS_MISTAKES = [
    {"wrong": "Answering '$25\%$ less' for the reverse of '$25\%$ more'.",
     "right": "The reverse is $\\dfrac{100 \\times 25}{125} = 20\%$ less."},
    {"wrong": "Writing 'A is $25\%$ more than B' as $A = B - 25\%$ of B.",
     "right": "More means add: $A = B + \\dfrac{25}{100}B = \\dfrac{5}{4}B$."},
    {"wrong": "Using $100 + x$ in the less-to-more formula.",
     "right": "Less-to-more divides by $100 - x$; more-to-less divides by $100 + x$."},
    {"wrong": "Adding chained percents: $40\%$ and $25\%$ of them called $65\%$.",
     "right": "Multiply instead: $25\%$ of $40\% = 10\%$."},
    {"wrong": "Calling $75\%$ less the reverse of $75\%$ more.",
     "right": "$75\%$ less reverses to $\\dfrac{100 \\times 75}{25} = 300\%$ more."},
    {"wrong": "Rounding $14\\dfrac{2}{7}\%$ to $14.2\%$ and losing the fraction.",
     "right": "Keep sevenths as fractions; the options use $14\\dfrac{2}{7}$."},
]

MORELESS_REVISION = [
    "$x\%$ more $\\Rightarrow \\dfrac{100x}{100+x}\%$ less.",
    "$x\%$ less $\\Rightarrow \\dfrac{100x}{100-x}\%$ more.",
    "Base-100 always works: put the 'than' quantity at 100.",
    "Pairs: 25/20, 50/$33\\dfrac{1}{3}$, 100/50, 75/300.",
    "Each 'of' in a chain multiplies: $a\%$ of $b\% = ab/10000$.",
    "$16\\dfrac{2}{3}\%$ more $\\Leftrightarrow$ $\\dfrac{1}{7}$ less.",
]

MORELESS_PATTERNS = [
    pat("pct-m1", "Convert 'x% more' into 'less'", "very common",
        "'A is some percent more than B. B is less than A by what percent?'",
        r"\frac{100x}{100+x}\% \text{ less}",
        ["Note x, the percent by which A beats B.", "Compute 100x over 100 + x.", "State it as the per cent by which B is less."],
        "The same gap measured on the bigger base A gives a smaller percent.",
        "A's salary is 60% more than B's. B's salary is less than A's by what percentage?",
        [r"$\dfrac{100 \times 60}{100 + 60} = \dfrac{6000}{160}$.", r"$= 37.5$."],
        "37.5%"),
    pat("pct-m2", "Convert 'x% less' into 'more'", "very common",
        "'A is some percent less than B. B is more than A by what percent?'",
        r"\frac{100x}{100-x}\% \text{ more}",
        ["Note x, the percent of the fall.", "Compute 100x over 100 - x.", "State it as the per cent by which B is more."],
        "The same gap measured on the smaller base A gives a bigger percent.",
        "A's income is 20% less than B's. B's income is more than A's by what percentage?",
        [r"$\dfrac{100 \times 20}{100 - 20} = \dfrac{2000}{80}$.", r"$= 25$."],
        "25%"),
    pat("pct-m3", "Per cent of a per cent", "common",
        "One group is a percent of a second group, which is itself a percent of a total.",
        r"\frac{a}{100} \times \frac{b}{100}",
        ["Attach each percent to its own group.", "Multiply the two percents as fractions.",
         "Simplify to a single percent of the total."],
        "Every 'of' multiplies, so a percent of a percent is a product.",
        "In an examination centre, 40% of the candidates are graduates, and 25% of the graduates are engineers. Engineers are what percentage of all candidates?",
        [r"$\dfrac{40}{100} \times \dfrac{25}{100} = \dfrac{1}{10}$.", r"$\dfrac{1}{10} = 10\%$."],
        "10%"),
    pat("pct-m4", "Two quantities on a common base", "occasional",
        "Two quantities are each compared with the same third quantity, and then with each other.",
        None,
        ["Put the shared base quantity at 100.", "Write both quantities from the two statements.",
         "Take the ratio of the two quantities."],
        "A common base makes the two quantities comparable in one ratio.",
        "X is 50% more than Z, and Y is 20% more than Z. Y is what percentage of X?",
        [r"Z $= 100$, so X $= 150$ and Y $= 120$.", r"$\dfrac{120}{150} \times 100 = 80$."],
        "80%"),
    pat("pct-m5", "Awkward percents through fractions", "occasional",
        "Percents like $16\\dfrac{2}{3}\%$ or $14\\dfrac{2}{7}\%$ appear, and a flip is asked.",
        None,
        ["Write the percent as a fraction from the table.", "Add or subtract that fraction from 1 for the bigger quantity.",
         "The leftover fraction, over the bigger quantity, is the reverse percent."],
        "Fraction chips reverse exactly, with no division of awkward decimals.",
        "X is $16\\dfrac{2}{3}\%$ more than Y. By what percentage is Y less than X?",
        [r"$16\dfrac{2}{3}\% = \dfrac{1}{6}$, so X $= \dfrac{7}{6}$Y.", r"Y $= \dfrac{6}{7}$X: less by $\dfrac{1}{7}$.", r"$\dfrac{1}{7} \times 100 = 14\dfrac{2}{7}$."],
        "14 2/7%"),
]

# ================= pct-population-election =================

POP_CONCEPT = (
    "Population and machine-value questions apply a per cent change **every year**, so the change compounds. "
    "Election questions first remove invalid votes, then compare candidates on valid votes.\n\n"
    "Both are multiplier questions wearing a story."
)

POP_NOTES = r"""### One rate, many years
A town grows by $r\%$ every year. Each year's population is the previous year's times the chip $\dfrac{100+r}{100}$.

$$\text{After } n \text{ years} = P \times \left(\frac{100+r}{100}\right)^n$$

A town of 50,000 grows $10\%$ a year. After 2 years: $50000 \times \dfrac{11}{10} \times \dfrac{11}{10} = 60500$.

> **Rule:** Growth per year compounds. Never use $P + P \times r \times n$, which is simple interest thinking.

### Different rates in different years
When each year has its own rate, multiply one chip per year in order.

A town of 40,000 grows $10\%$ one year and falls $5\%$ the next: $40000 \times \dfrac{11}{10} \times \dfrac{19}{20} = 41800$.

Three rates work the same way. A value that rose $20\%$, then $25\%$, then $10\%$ is now $66,000$; before those years it was $66000 \div \dfrac{33}{20} = 40000$.

> **Note:** $+10\%$ then $-5\%$ is not $+5\%$. The chips multiply, they do not cancel.

### Travelling back in time
To find an earlier value, divide by the chips.

A town has 16,000 people now and grows $25\%$ yearly. Two years ago: $16000 \div \dfrac{5}{4} \div \dfrac{5}{4} = 16000 \times \dfrac{16}{25} = 10240$.

> **Tip:** Dividing by $\dfrac{5}{4}$ twice is multiplying by $\left(\dfrac{4}{5}\right)^2$. Reverse the chip, then square it.

### Depreciation compounds too
A machine loses value every year. That is a fall applied to the falling value, so it compounds.

A machine worth Rs 12,500 loses $10\%$ a year. After 2 years: $12500 \times \left(\dfrac{9}{10}\right)^2 = 10125$.

Running backwards: a machine is worth 8,100 after two years of $10\%$ yearly loss. It cost $8100 \times \left(\dfrac{10}{9}\right)^2 = 10000$.

> **Watch:** Each year's fall is taken on that year's value, never on the original price.

A rise of $25\%$ followed by a fall of $20\%$ does come back: $\dfrac{5}{4} \times \dfrac{4}{5} = 1$. But $+25\%$ then $-25\%$ leaves $\dfrac{5}{4} \times \dfrac{3}{4} = \dfrac{15}{16}$, a loss.

### Elections: valid votes first
Votes polled $=$ valid votes $+$ invalid votes. Candidate percents are always on **valid** votes.

Worked: $20\%$ of votes polled were invalid. The winner got $60\%$ of valid votes and beat the only rival by 1,200 votes.

1. Two candidates, so the rival got $40\%$ of valid votes.
2. Margin $= 20\%$ of valid votes $= 1200$, so valid $= 6000$.
3. Polled $=$ valid $\times \dfrac{100}{80} = 6000 \times \dfrac{5}{4} = 7500$.

> **Careful:** "Votes polled" is not "valid votes". Remove the invalid share first.

### Voters who did not turn up
The electoral roll lists everyone. Votes cast $=$ roll $-$ those who did not vote.

Worked: $20\%$ of the roll did not vote. The winner got $55\%$ of votes cast and won by 1,200 votes.

1. Margin $= 55\% - 45\% = 10\%$ of votes cast $= 1200$, so cast $= 12000$.
2. Cast is $80\%$ of the roll, so roll $= 12000 \times \dfrac{5}{4} = 15000$.

> **Example:** 27,000 votes were polled in another ward and $10\%$ were invalid. Valid votes $= 27000 - 2700 = 24300$.
"""

POP_FORMULAS = [
    {"name": "Growth for n years", "tex": r"P\left(1 + \frac{r}{100}\right)^n", "note": "r% added every year, compounding."},
    {"name": "Depreciation for n years", "tex": r"P\left(1 - \frac{r}{100}\right)^n", "note": "r% of value lost every year."},
    {"name": "Value n years ago", "tex": r"\frac{\text{now}}{\left(1 \pm \frac{r}{100}\right)^n}", "note": "Divide by the chip power to go back."},
    {"name": "Election margin", "tex": r"\text{margin votes} = (\text{winner}\% - \text{rival}\%) \times \text{valid votes}", "note": "Percents on valid votes only."},
]

POP_TRICKS = [
    {
        "title": "Chip powers beat formulas",
        "body": "Write one multiplier per year and multiply. Squares like $\\left(\\dfrac{5}{4}\\right)^2 = \\dfrac{25}{16}$ are worth remembering.",
        "example": {
            "q": "A town of 6,400 people grows by 25% every year. What is its population after 2 years?",
            "steps": [r"Chip for $25\%$ growth: $\dfrac{5}{4}$.", r"$6400 \times \dfrac{25}{16} = 400 \times 25 = 10000$."],
            "answer": "10,000",
        },
    },
    {
        "title": "Remove invalid votes first",
        "body": "In elections, bring every statement onto valid votes before touching the margin.",
        "example": {
            "q": "In an election, 20% of the votes polled were invalid. The winner secured 60% of the valid votes and beat the only other candidate by 1,200 votes. How many votes were polled?",
            "steps": [r"Margin $= 60\% - 40\% = 20\%$ of valid votes.", r"$20\%$ of valid $= 1200 \Rightarrow$ valid $= 6000$.", r"Valid $= 80\%$ of polled, so polled $= 6000 \times \dfrac{5}{4} = 7500$."],
            "answer": "7,500 votes",
        },
    },
    {
        "title": "Roll, cast, valid: walk the chain",
        "body": "Election numbers form a chain: roll, votes cast, valid votes, then candidates. Convert one link at a time with chips.",
        "example": {
            "q": "In an election, 20% of the voters on the roll did not vote. The winner got 55% of the votes cast and won by 1,200 votes. How many voters were on the roll?",
            "steps": [r"Margin $= 10\%$ of cast $= 1200 \Rightarrow$ cast $= 12000$.", r"Cast $= 80\%$ of roll.", r"Roll $= 12000 \times \dfrac{5}{4} = 15000$."],
            "answer": "15,000 voters",
        },
    },
]

POP_MISTAKES = [
    {"wrong": "Using simple growth $P + Prn$ for population.",
     "right": "Population compounds: $P \\times \\left(1 + \\dfrac{r}{100}\\right)^n$."},
    {"wrong": "Taking every year's depreciation on the original value.",
     "right": "Each year falls on that year's value, so multiply chips."},
    {"wrong": "Applying the chip $n-1$ times for $n$ years.",
     "right": "Count on fingers: 2 years means the chip twice."},
    {"wrong": "Computing candidate percents on total votes polled.",
     "right": "Remove invalid votes first; percents are on valid votes."},
    {"wrong": "Taking the winner's margin as a percent of the roll.",
     "right": "The margin is the difference of two percents of valid or cast votes."},
    {"wrong": "Multiplying by the growth chip to find a past value.",
     "right": "Going back divides by the chip, or multiplies by its inverse."},
]

POP_REVISION = [
    "Growth: $P \\times \\left(\\dfrac{100+r}{100}\\right)^n$.",
    "Depreciation: $P \\times \\left(\\dfrac{100-r}{100}\\right)^n$.",
    "Past value: divide by the chip power.",
    "Different rates: one chip per year, multiplied in order.",
    "Roll $\\to$ cast $\\to$ valid votes: one chip at a time.",
    "Margin $=$ (winner% $-$ rival%) of valid votes.",
]

POP_PATTERNS = [
    pat("pct-p1", "Population after n years", "very common",
        "A present population and a yearly growth rate are given; the future population is asked.",
        r"P\left(1+\frac{r}{100}\right)^n",
        ["Write the chip for the yearly rate.", "Raise it to the number of years.",
         "Multiply by the present population.", "Keep the answer exact with fractions."],
        "The same chip applies every year, so it compounds to a power.",
        "The population of a town is 6,400 and it grows by 25% every year. What will it be after 2 years?",
        [r"Chip $= \dfrac{5}{4}$; power for 2 years $= \dfrac{25}{16}$.", r"$6400 \times \dfrac{25}{16} = 400 \times 25 = 10000$."],
        "10,000"),
    pat("pct-p2", "Population or value n years ago", "common",
        "The present value and a yearly rate are given; an earlier value is asked.",
        r"\text{past} = \frac{\text{now}}{\left(1+\frac{r}{100}\right)^n}",
        ["Write the chip for the yearly rate.", "Divide the present value by the chip, once per year.",
         "Check by growing your answer forward."],
        "Growth moved the number forward by chips, so division walks it back.",
        "A town's population grows by 25% every year. It is 16,000 now. What was it 2 years ago?",
        [r"Chip $= \dfrac{5}{4}$; divide twice, same as $\\times \dfrac{16}{25}$.", r"$16000 \times \dfrac{16}{25} = 640 \times 16 = 10240$."],
        "10,240"),
    pat("pct-p3", "Different rates in different years", "common",
        "Each year has its own rise or fall: 'increased by 5% in the first year and decreased by 10% in the second'.",
        r"\text{final} = P \times \frac{100+a}{100} \times \frac{100-b}{100} \times \cdots",
        ["Write one chip per year, in order.", "Multiply all the chips.", "Multiply by the starting value.",
         "Going back in time, divide instead."],
        "Multipliers handle mixed rises and falls in one line.",
        "A town had 80,000 people. The population rose by 5% in one year and fell by 10% the next. What was the population after the two years?",
        [r"Chips: $\dfrac{21}{20}$ then $\dfrac{9}{10}$.", r"$80000 \times \dfrac{21}{20} = 84000$.", r"$84000 \times \dfrac{9}{10} = 75600$."],
        "75,600"),
    pat("pct-p4", "Election with invalid votes and a margin", "very common",
        "Some per cent of votes polled is invalid; the winner's share of valid votes and the winning margin are given.",
        r"\text{margin} = (\text{winner}\% - \text{rival}\%) \times \text{valid votes}",
        ["Find the rival's share of valid votes (two candidates).", "Margin per cent of valid votes is the difference of shares.",
         "From the margin votes, find valid votes.", "Scale up to votes polled using the invalid per cent."],
        "Candidate shares live on valid votes, so the margin fixes the valid count first.",
        "In an election, 20% of the votes polled were invalid. The winner secured 60% of the valid votes and beat the only other candidate by 1,200 votes. How many votes were polled?",
        [r"Rival $= 40\%$ of valid; margin $= 20\%$ of valid $= 1200$.", r"Valid votes $= 6000$.", r"Valid is $80\%$ of polled: $6000 \times \dfrac{5}{4} = 7500$."],
        "7,500"),
    pat("pct-p5", "Election with voters who stayed home", "occasional",
        "A per cent of the electorate did not vote; the rest elect the winner.",
        None,
        ["Votes cast = roll minus the absent share.", "From the margin, find the votes cast.",
         "Scale cast up to the full roll."],
        "Turnout links the roll to the cast votes, and the margin links cast votes to the winner.",
        "In an election, 20% of the voters on the electoral roll did not vote. The winner received 55% of the votes cast and won by 1,200 votes. How many voters were on the roll?",
        [r"Margin $= 55\% - 45\% = 10\%$ of cast $= 1200$.", r"Cast $= 12000$.", r"Cast is $80\%$ of the roll: $12000 \times \dfrac{5}{4} = 15000$."],
        "15,000"),
]

# ================= pct-marks-income =================

MARKS_CONCEPT = (
    "Pass-marks questions hide one unknown: the **maximum marks**. Two candidates' scores pin it down. "
    "Income questions split money into expenditure and savings. "
    "Price questions link a price change to how much you can buy."
)

MARKS_NOTES = r"""### Pass marks with two candidates
One candidate scores $x\%$ and fails by $a$ marks. Another scores $y\%$ and gets $b$ marks more than the pass mark.

The gap between their scores covers $(y - x)\%$ of the maximum marks and equals $a + b$ marks.

$$M = \frac{(a + b) \times 100}{y - x}$$

Worked: A scores $33\%$ and fails by 45 marks. B scores $45\%$ and gets 15 marks more than the pass mark.

1. Span of percents $= 45 - 33 = 12$.
2. Span of marks $= 45 + 15 = 60$.
3. $M = 60 \times \dfrac{100}{12} = 500$.
4. Pass mark $= 33\%$ of $500 + 45 = 165 + 45 = 210$.

> **Rule:** One candidate sits below the pass mark, the other above. The whole distance is $a + b$.

### Pass marks with one candidate
"Fails by $a$" means the score plus $a$ equals the pass mark.

A student scores $30\%$ and fails by 20 marks; the pass mark is 152. Then $30\%$ of $M = 152 - 20 = 132$, so $M = 440$.

> **Tip:** Write "$\text{score} + \text{shortfall} = \text{pass}$" as a line before substituting anything.

### Income, expenditure and savings
Income $=$ expenditure $+$ savings. Take income as a friendly 100 units and the percents become the money itself.

| Item | Before | After |
|---|---|---|
| Income | 400 | $400 \times \dfrac{23}{20} = 460$ |
| Expenditure (80% of income) | 320 | $320 \times \dfrac{11}{10} = 352$ |
| Savings | 80 | $460 - 352 = 108$ |

Savings rose by $\dfrac{28}{80} \times 100 = 35\%$.

> **Watch:** The savings per cent is measured on the old savings (80), never on income.

### Price rises and consumption
Same budget, higher price, so the quantity must fall.

$$\text{quantity chip} = \frac{\text{budget chip}}{\text{price chip}}$$

Petrol price rises $25\%$: price chip $\dfrac{5}{4}$, budget chip 1, so quantity chip $= 1 \div \dfrac{5}{4} = \dfrac{4}{5}$. Consumption must fall $20\%$.

> **Note:** A $25\%$ rise pairs with a $20\%$ cut. This is the more/less flip of the previous subtopic.

### A price cut and the extra quantity
Same money after a price cut buys more.

Price falls $20\%$: chip $\dfrac{4}{5}$. Quantity chip $= 1 \div \dfrac{4}{5} = \dfrac{5}{4}$, a $25\%$ rise.

Worked: Rs 400 spent on rice. After a $20\%$ price cut, the same money buys 5 kg more.

1. Old price Rs $p$ per kg: old quantity $= \dfrac{400}{p}$.
2. New price $= 0.8p$; new quantity $= \dfrac{400}{0.8p} = \dfrac{500}{p}$.
3. Extra $= \dfrac{100}{p} = 5$, so $p = 20$.

> **Careful:** The extra quantity per cent is not the cut per cent. A $20\%$ cut buys $25\%$ more.

### Checking the direction
Every question in this subtopic is a chain of chips. Before answering, say the direction out loud: are you moving from old to new, or back?

- Marks: percents of $M$ move up to marks.
- Income: chips move income and expenditure forward, savings are the remainder.
- Prices: budget chip over price chip gives the quantity chip.

> **Example:** Income 400 rising $15\%$ is $400 \times \dfrac{23}{20} = 460$: multiply forward, never add 15% of something else.
"""

MARKS_FORMULAS = [
    {"name": "Maximum marks (two candidates)", "tex": r"M = \frac{(a+b) \times 100}{y - x}", "note": "a = shortfall below pass, b = marks above pass, x and y are the two percents."},
    {"name": "Pass mark from failing", "tex": r"\text{pass} = \frac{x}{100}M + a", "note": "a is the shortfall." },
    {"name": "Consumption cut after a price rise", "tex": r"\frac{100x}{100 + x}\%", "note": "Budget unchanged, price up x%."},
    {"name": "Extra quantity after a price cut", "tex": r"\frac{100c}{100 - c}\%", "note": "Budget unchanged, price down c%."},
]

MARKS_TRICKS = [
    {
        "title": "Span of marks over span of percents",
        "body": "Two candidates give one clean fraction: marks apart over percents apart. Multiply by 100 for maximum marks.",
        "example": {
            "q": "In an examination, A scores 33% and fails by 45 marks. B scores 45% and gets 15 marks more than the pass mark. Find the maximum marks.",
            "steps": [r"Marks apart $= 45 + 15 = 60$.", r"Percents apart $= 45 - 33 = 12$.", r"$M = 60 \times \dfrac{100}{12} = 500$."],
            "answer": "500",
        },
    },
    {
        "title": "Price rise to consumption cut is a flip",
        "body": "Reuse the more/less flip: price up $x\%$ with the same budget means consumption down $\\dfrac{100x}{100+x}\%$.",
        "example": {
            "q": "The price of petrol rises by 25%. By what per cent must a family cut its consumption to keep its spending the same?",
            "steps": [r"Cut $= \dfrac{100 \times 25}{125}$.", r"$= 20$."],
            "answer": "20%",
        },
    },
    {
        "title": "Extra kilograms reveal the price",
        "body": "After a price cut, extra kilograms equal money times the difference of the chips, divided by the new price. Solve for the price.",
        "example": {
            "q": "Rs 400 is spent on rice. After a 20% fall in price, the same money buys 5 kg more. What was the original price per kg?",
            "steps": [r"Quantity chip $= \dfrac{5}{4}$, so extra $= \dfrac{1}{4}$ of old quantity.", r"Old quantity $= 20$ kg, so extra $= 5$ kg matches.", r"Price $= \dfrac{400}{20} = 20$ per kg."],
            "answer": "Rs 20 per kg",
        },
    },
]

MARKS_MISTAKES = [
    {"wrong": "Dividing by $(y - x)$ but forgetting to add $b$ to $a$.",
     "right": "The marks span is the whole distance, shortfall plus surplus: $a + b$."},
    {"wrong": "Writing pass mark $= x\%$ of $M - a$ for a failing candidate.",
     "right": "Failing means below pass: pass $= \\dfrac{x}{100}M + a$."},
    {"wrong": "Measuring the savings change on the new savings.",
     "right": "Per cent change uses the old value as the base."},
    {"wrong": "Cutting consumption by the same per cent as the price rise.",
     "right": "Price up $25\%$ needs only a $20\%$ cut: $\\dfrac{100x}{100+x}$."},
    {"wrong": "Calling the extra quantity per cent equal to the price cut.",
     "right": "A $20\%$ cut buys $\\dfrac{100 \\times 20}{80} = 25\%$ more."},
    {"wrong": "Taking income as 100 but expenditure as a real rupee figure.",
     "right": "Keep every number in the same units, assumed or real."},
]

MARKS_REVISION = [
    "Two candidates: $M = (a+b) \\times 100 \\div (y-x)$.",
    "Pass $= x\%$ of $M + a$ when a candidate fails by $a$.",
    "Income $=$ expenditure $+$ savings; assume income 100.",
    "Savings change is measured on the old savings.",
    "Price up $x\%$, same budget: consumption down $\\dfrac{100x}{100+x}\%$.",
    "Price down $c\%$: quantity up $\\dfrac{100c}{100-c}\%$.",
]

MARKS_PATTERNS = [
    pat("pct-i1", "Two candidates and the maximum marks", "very common",
        "One candidate fails by some marks, another crosses the pass mark; maximum marks or the pass mark is asked.",
        r"M = \frac{(a+b) \times 100}{y - x}",
        ["Note the two percents and the two distances from the pass mark.", "Marks span = shortfall + surplus.",
         "Percent span = higher percent minus lower percent.", "Maximum marks = marks span x 100 / percent span."],
        "Both candidates' scores are percents of the same maximum, so their gap fixes it.",
        "In an examination, A scores 33% and fails by 45 marks, while B scores 45% and gets 15 marks more than the pass mark. What are the maximum marks?",
        [r"Marks span $= 45 + 15 = 60$.", r"Percent span $= 45 - 33 = 12$.", r"$M = 60 \times \dfrac{100}{12} = 500$."],
        "500"),
    pat("pct-i2", "Income rise and the change in savings", "common",
        "Income and expenditure both change by percents; the effect on savings is asked.",
        r"\text{savings change} = \frac{\text{new savings} - \text{old savings}}{\text{old savings}} \times 100",
        ["Assume a friendly income (say 400) and the expenditure percent.", "Move income and expenditure forward with chips.",
         "New savings = new income - new expenditure.", "Compare with old savings for the per cent change."],
        "Savings are just the remainder, so both chips flow into it.",
        "A family earns Rs 400 a month and spends 80% of it. Income rises by 15% and expenditure rises by 10%. By what percentage do the savings increase?",
        [r"New income $= 400 \times \dfrac{23}{20} = 460$; new spending $= 320 \times \dfrac{11}{10} = 352$.", r"Old savings $= 80$; new savings $= 460 - 352 = 108$.", r"$\dfrac{28}{80} \times 100 = 35$."],
        "35%"),
    pat("pct-i3", "Price rise, consumption cut", "very common",
        "A price rises by a percent and the matching cut in consumption (same budget) is asked.",
        r"\frac{100x}{100 + x}\%",
        ["Note the price rise x.", "Compute 100x over 100 + x.", "State it as the cut needed."],
        "With a fixed budget, quantity chip is one over the price chip.",
        "The price of petrol rises by 25%. By what percentage must consumption be reduced to keep the expenditure unchanged?",
        [r"Price chip $= \dfrac{5}{4}$.", r"Quantity chip $= 1 \div \dfrac{5}{4} = \dfrac{4}{5}$.", r"Fall $= 1 - \dfrac{4}{5} = \dfrac{1}{5} = 20\%$."],
        "20%"),
    pat("pct-i4", "Price cut and the extra quantity", "common",
        "A price falls by a percent; the same money now buys extra kilograms, and the price is asked.",
        r"\text{extra}\% = \frac{100c}{100 - c}\%",
        ["Write the quantity chip as one over the price chip.", "Extra per cent = quantity chip minus 1.",
         "Use the extra kilograms to find the old quantity.", "Price = money divided by old quantity."],
        "A fixed budget divided by a smaller price gives a bigger quantity, and the surplus pins the old quantity.",
        "A household spends Rs 400 on rice every month. After a 20% fall in the price of rice, the same money buys 5 kg more. What was the original price per kg?",
        [r"Quantity chip $= \dfrac{5}{4}$, so extra $= \dfrac{1}{4}$ of old quantity $= 5$ kg.", r"Old quantity $= 20$ kg.", r"Price $= \dfrac{400}{20} = 20$."],
        "Rs 20 per kg"),
    pat("pct-i5", "One candidate and the pass mark", "common",
        "A single candidate's percent, the shortfall, and the pass mark are given; maximum marks is asked.",
        r"M = \frac{(\text{pass} - a) \times 100}{x}",
        ["Turn the shortfall into the candidate's marks: pass minus shortfall.", "That equals x% of the maximum.",
         "Divide and multiply by 100 for M."],
        "One candidate's score is one percent slice of the maximum, so one equation is enough.",
        "A student scores 30% in an examination and fails by 20 marks. If the pass mark is 152, what are the maximum marks?",
        [r"Student's marks $= 152 - 20 = 132$.", r"$\dfrac{30}{100}M = 132$.", r"$M = 132 \times \dfrac{100}{30} = 440$."],
        "440"),
]

# ================= write back =================

dfrac = lambda x: x.replace(r"\frac", r"\dfrac")

BLOCKS = [
    ("pct-basics", dict(concept=BASICS_CONCEPT, notes=BASICS_NOTES, formulas=BASICS_FORMULAS,
                        tricks=BASICS_TRICKS, mistakes=BASICS_MISTAKES, revision=BASICS_REVISION,
                        patterns=BASICS_PATTERNS)),
    ("pct-change", dict(concept=CHANGE_CONCEPT, notes=CHANGE_NOTES, formulas=CHANGE_FORMULAS,
                        tricks=CHANGE_TRICKS, mistakes=CHANGE_MISTAKES, revision=CHANGE_REVISION,
                        patterns=CHANGE_PATTERNS)),
    ("pct-more-less", dict(concept=MORELESS_CONCEPT, notes=MORELESS_NOTES, formulas=MORELESS_FORMULAS,
                           tricks=MORELESS_TRICKS, mistakes=MORELESS_MISTAKES, revision=MORELESS_REVISION,
                           patterns=MORELESS_PATTERNS)),
    ("pct-population-election", dict(concept=POP_CONCEPT, notes=POP_NOTES, formulas=POP_FORMULAS,
                                     tricks=POP_TRICKS, mistakes=POP_MISTAKES, revision=POP_REVISION,
                                     patterns=POP_PATTERNS)),
    ("pct-marks-income", dict(concept=MARKS_CONCEPT, notes=MARKS_NOTES, formulas=MARKS_FORMULAS,
                              tricks=MARKS_TRICKS, mistakes=MARKS_MISTAKES, revision=MARKS_REVISION,
                              patterns=MARKS_PATTERNS)),
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
print("percentage.json updated")
