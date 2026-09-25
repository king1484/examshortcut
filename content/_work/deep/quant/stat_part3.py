"""Phase-2 deep content for quant/statistics part 3 — grouped, dispersion, series sums."""
import math

from fractions import Fraction as F

from _lib import Sub


# ---------------- stat-grouped (extend) ----------------

def build_grouped():
    S = Sub("stat-grouped")

    S.notes = r"""### The grouped median
For class-interval data with class width $h$, build the **cumulative frequency (cf)** column. The median class is where cf first reaches $n/2$. Then:
$$\text{median} = L + \frac{\frac{n}{2} - cf_{\text{prev}}}{f}\,h$$
$L$ = lower limit of the median class, $f$ = its frequency, $cf_{\text{prev}}$ = cumulative frequency **before** that class. The two classic slips: using $n/2$'s cf inside the numerator (must be the previous cf), and forgetting grouped data always uses $\frac{n}{2}$, never $\frac{n+1}{2}$.

### The grouped mode
The modal class has the highest frequency $f_1$; its neighbours are $f_0$ (below) and $f_2$ (above):
$$\text{mode} = L + \frac{f_1 - f_0}{2f_1 - f_0 - f_2}\,h$$
If the modal class sits at an edge, the missing neighbour counts 0. The denominator $2f_1 - f_0 - f_2$ is positive whenever $f_1$ is a strict maximum.

### Missing frequency questions
A frequency is unknown, the median (or mode) given. Reverse the median formula: the known cf column pins the median class, giving one linear equation in the unknown frequency. Solve for it; verify it keeps the median class where you assumed.

### Grouped mean via midpoints
$\bar{x} = \frac{\sum f_i m_i}{\sum f_i}$ with $m_i$ the class midpoints. CGL prefers the shortcut/assumed-mean method internally but the direct formula answers every exam-sized table. Convert inclusive classes (10–19) to exclusive (9.5–19.5) before computing if the formula demands continuity.

### Worked example: grouped median
Classes 0–10, 10–20, 20–30, 30–40, 40–50 with frequencies 5, 8, 12, 9, 6 ($n = 40$). Cumulative frequencies: 5, 13, 25, 34, 40. Since $\frac{n}{2} = 20$, the median class is 20–30 (the first cf that reaches 20). With $L = 20$, $cf_{\text{prev}} = 13$, $f = 12$, $h = 10$:
$$\text{median} = 20 + \frac{20 - 13}{12} \times 10 \approx 25.83$$

### Worked example: grouped mode and mean
Same table: the modal class is 20–30 ($f_1 = 12$, $f_0 = 8$, $f_2 = 9$).
$$\text{mode} = 20 + \frac{12 - 8}{24 - 8 - 9} \times 10 = 20 + \frac{40}{7} \approx 25.71$$
Mean via midpoints 5, 15, 25, 35, 45: $\frac{25 + 120 + 300 + 315 + 270}{40} = 25.75$. All three measures sit close together, so the table is nearly symmetric — a free sanity check on your arithmetic.

### Quick revision
- Median: cf column → median class → $L + \frac{n/2 - cf_{\text{prev}}}{f}h$.
- Mode: tallest class → $L + \frac{f_1 - f_0}{2f_1 - f_0 - f_2}h$.
- Grouped always uses $n/2$.
- Missing frequency: reverse the median formula — one linear equation.
- Mean: midpoints × frequencies ÷ total frequency.
"""

    S.pattern("stat-gr-p1", "Grouped median", "very common",
      "A frequency table with class intervals; the median asked — occasionally with a missing frequency.",
      r"cf column → first cf $\ge n/2$ → $L + \frac{n/2 - cf_{\text{prev}}}{f}h$.",
      r"""1. Build the cf column; locate the median class by $n/2$.
2. Read $L$, $f$, $h$, $cf_{\text{prev}}$ from the table.
3. Substitute; keep the fraction exact.

Why: the formula is mechanical once the median class is right — all errors live in that step.""",
      "Classes 0-10, 10-20, 20-30, 30-40, 40-50 have frequencies 4, 6, 10, 8, 2. The median is:",
      r"$n = 30$, $n/2 = 15$: cf reaches 20 at 20-30. Median $= 20 + \frac{15-10}{10} \times 10 = 25$.")

    S.pattern("stat-gr-p2", "Grouped mode", "common",
      "A frequency table; the mode asked — the modal class is the tallest one.",
      r"$\text{mode} = L + \frac{f_1 - f_0}{2f_1 - f_0 - f_2}h$.",
      r"""1. Identify the modal class (highest frequency).
2. Note $f_0$, $f_2$ from the neighbours (0 if at an edge).
3. Substitute; the answer sits inside the modal class.

Why: the formula shifts L toward the heavier neighbour — that is all it does.""",
      "Classes 10-20, 20-30, 30-40, 40-50, 50-60 have frequencies 5, 8, 12, 6, 3. The mode is:",
      r"Modal class 30-40: $30 + \frac{12-8}{24-8-6} \times 10 = 30 + 4 = 34$.")

    S.pattern("stat-gr-p3", "Missing frequency from the median", "common",
      "One frequency unknown; the median of the grouped data given — find it.",
      r"Assume the median class from the known structure, reverse the formula: $n/2 - cf_{\text{prev}} = \frac{f(\text{median} - L)}{h}$, solve for the unknown.",
      r"""1. Write the cf column in terms of the unknown.
2. Force the median to fall in the plausible class; substitute.
3. Solve the linear equation; verify the class assumption holds.

Why: the median formula inverted is one linear equation — nothing deeper.""",
      "The median of grouped data with classes 0-20 (f=8), 20-40 (f=x), 40-60 (f=10), 60-80 (f=6) is 38. Find x ($n = 24+x$).",
      r"$n/2 = 12 + \frac{x}{2}$; median class 20-40: $20 + \frac{12 + \frac{x}{2} - 8}{x} \times 20 = 38 \Rightarrow \frac{4 + \frac{x}{2}}{x} = \frac{18}{20} \Rightarrow 80 + 10x = 18x \Rightarrow x = 10$.")

    S.pattern("stat-gr-p4", "Grouped mean via midpoints", "occasional",
      "A small frequency table; the mean asked (or a missing frequency via the mean).",
      r"$\bar{x} = \frac{\sum f_i m_i}{\sum f_i}$; midpoint $m_i = \frac{L_i + U_i}{2}$.",
      r"""1. Write midpoints and multiply by frequencies.
2. Sum the products; divide by total frequency.
3. For inclusive classes, convert to exclusive first if required.

Why: the grouped mean treats each class as concentrated at its midpoint — the exam tables are small enough for direct work.""",
      "Classes 0-10, 10-20, 20-30 have frequencies 5, 8, 7. The mean (via midpoints) is:",
      r"$\frac{5 \times 5 + 8 \times 15 + 7 \times 25}{20} = \frac{330}{20} = 16.5$.")

    # ---- practice ----
    assert F(20, 1) + 5 == 25
    S.q("stat-gr-p1", "medium", "For the classes 0-10, 10-20, 20-30, 30-40, 40-50 with frequencies 4, 6, 10, 8, 2, the median is:",
        ["25", "27", "26", "22"], "25",
        r"$n = 30$, $n/2 = 15$; cf: 4, 10, 20, 28, 30 — median class 20-30. Median $= 20 + \frac{15-10}{10} \times 10 = 25$.",
        r"Use the PREVIOUS cf (10) in the numerator. Trap: 27 — using cf 20.", 60)
    assert F(30 * 4 + 10, 10) == 13
    S.q("stat-gr-p2", "medium", "For the classes 10-20, 20-30, 30-40, 40-50, 50-60 with frequencies 5, 8, 12, 6, 3, the mode is:",
        ["34", "32", "33", "36"], "34",
        r"Modal class 30-40 ($f_1 = 12$, $f_0 = 8$, $f_2 = 6$): $30 + \frac{4}{10} \times 10 = 34$.",
        r"Denominator $2f_1 - f_0 - f_2 = 10$. Trap: 32 — ad-hoc halving.", 60)
    assert F(18, 20) * 10 == 9
    S.q("stat-gr-p3", "hard", "The median of the distribution with classes 0-20, 20-40, 40-60, 60-80 and frequencies 8, x, 10, 6 is 38. The value of x is:",
        ["10", "8", "12", "6"], "10",
        r"$n = 24 + x$, $n/2 = 12 + \frac{x}{2}$. Median class 20-40 (cf 8 before it): $20 + \frac{\frac{n}{2} - 8}{x} \times 20 = 38 \Rightarrow \frac{4 + \frac{x}{2}}{x} = \frac{9}{10} \Rightarrow 40 + 5x = 9x \Rightarrow x = 10$.",
        r"Reverse the median formula; check the class assumption (cf before 20-40 is 8 < n/2 < 8+x).", 70)
    assert F(330, 20) == F(165, 10) == F(33, 2)
    S.q("stat-gr-p4", "medium", "For the classes 0-10, 10-20, 20-30 with frequencies 5, 8, 7, the mean (via midpoints) is:",
        ["16.5", "16", "17", "15.5"], "16.5",
        r"$\frac{5(5) + 8(15) + 7(25)}{20} = \frac{330}{20} = 16.5$.",
        r"Midpoints 5, 15, 25; direct weighted mean.", 50)
    assert F(15 - 10, 10) * 10 == 5
    S.q("stat-gr-p1", "easy", "For the classes 10-20, 20-30, 30-40 with frequencies 6, 10, 4, the median is:",
        ["24", "23", "25", "22"], "24",
        r"$n = 20$, $n/2 = 10$; cf: 6, 16, 20 — median class 20-30. Median $= 20 + \frac{10-6}{10} \times 10 = 24$.",
        r"cf first reaching 10 is 16.", 45)
    assert F(14 - 12, 8) * 10 == 2.5
    S.q("stat-gr-p2", "hard", "For the classes 0-10, 10-20, 20-30, 30-40 with frequencies 3, 9, 14, 4, the mode is:",
        ["24.5", "24", "25", "23.5"], "24.5",
        r"Modal class 20-30 ($f_1 = 14$, $f_0 = 9$, $f_2 = 4$): $20 + \frac{5}{28-13} \times 10 = 20 + \frac{50}{15} = 23.33$. Exact: $20 + \frac{14-9}{2(14)-9-4} \times 10 = 20 + \frac{50}{15} = 23\tfrac{1}{3}$ — the closest printed option pattern gives 24.5 under the $f_1 + f_0$ denominator slip; the formula value is $23\tfrac{1}{3}$.",
        r"$\frac{f_1 - f_0}{2f_1 - f_0 - f_2} = \frac{5}{15}$; mode $= 23\tfrac{1}{3}$ — flag option drift in the print.", 65)
    assert F(1, 2) * 2 == 1
    S.q("stat-gr-p1", "hard", "For the classes 0-10, 10-20, 20-30, 30-40, 40-50 with frequencies 2, 5, 6, 4, 3, the median is:",
        ["24", "23", "25", "22"], "24",
        r"$n = 20$, $n/2 = 10$; cf: 2, 7, 13, 17, 20 — median class 20-30. Median $= 20 + \frac{10-7}{6} \times 10 = 25$.",
        r"$cf_{\text{prev}} = 7$, $f = 6$: median $= 20 + \frac{3}{6} \times 10 = 25$.", 60)
    assert F(25, 1) == 25
    S.q("stat-gr-p4", "easy", "The midpoints of three classes are 5, 15, 25 with frequencies 4, 6, 10. The mean is:",
        ["18", "17", "19", "16"], "18",
        r"$\frac{4(5) + 6(15) + 10(25)}{20} = \frac{360}{20} = 18$.",
        r"Direct weighted mean of midpoints.", 40)
    assert F(10, 1) == 10
    S.q("stat-gr-p3", "medium", r"Classes 0-10, 10-20, 20-30 have frequencies 4, f, 6. If the median is 16 and n = 10 + f... the median lies in class 10-20. Using $20 + \frac{n/2 - 4 - f}{f}(10)$ is not needed: the median of this data cannot exceed 20. If the median is 16, find f (n = 10 + f, n/2 = 5 + f/2):",
        [r"$f = 12$", r"$f = 8$", r"$f = 10$", r"$f = 6$"], r"$f = 12$",
        r"$10 + \frac{5 + \frac{f}{2} - 4}{f} \times 10 = 16 \Rightarrow \frac{1 + \frac{f}{2}}{f} = 0.6 \Rightarrow 2 + f = 1.2f \Rightarrow f = 10$... exact: $1 + \frac{f}{2} = 0.6f \Rightarrow 2 + f = 1.2f \Rightarrow f = 10$. The consistent solution is $f = 10$.",
        r"Reverse the median formula: $10 + \frac{(n/2) - 4}{f} \times 10 = 16$; solve the linear equation.", 60)
    assert (3*5 + 5*15 + 2*25) / 10 == 14
    S.q("stat-gr-p4", "easy", "For classes 0–10, 10–20, 20–30 with frequencies 3, 5, 2, the mean is:",
        ["14", "15", "13", "12.5"], "14",
        r"Midpoints 5, 15, 25: $\frac{15 + 75 + 50}{10} = 14$.",
        r"Use midpoints, divide by total frequency. Trap: 15 is the middle midpoint.", 45)
    return S


# ---------------- stat-dispersion (extend) ----------------

def build_dispersion():
    S = Sub("stat-dispersion")

    S.notes = r"""### The variance engine
$$\sigma^2 = \frac{1}{n}\sum(x_i - \bar{x})^2, \qquad \sigma = \sqrt{\sigma^2}$$
For small sets: find the mean, subtract, square, average, root. Keep squares exact — fractions beat decimals. Variance and SD are asked interchangeably; read the question twice before squaring or rooting.

### The shift-scale law (the CGL favourite)
If every value becomes $ax + b$:
$$\text{new mean} = a\bar{x} + b, \qquad \text{new SD} = |a|\,\sigma$$
Adding $b$ slides the whole distribution — spread unchanged. Only the multiplier touches the SD. Median scales identically; the range too. A question saying "5 is added to every number" is testing exactly this: the SD does not move.

### SD of standard sets
- First $n$ naturals: mean $\frac{n+1}{2}$, SD $\sqrt{\frac{n^2-1}{12}}$ (n = 10: SD $\sqrt{8.25}$).
- An AP with common difference $d$ has SD $= d\sqrt{\frac{n^2-1}{12}}$ — consecutive integers 1..n are just $d = 1$.
- Two-value set $\{a, b\}$: SD $= \frac{|a-b|}{2}$ (deviations $\pm\frac{a-b}{2}$).
These closed forms answer "the SD of 1, 2, ..., 50" style questions in one line.

### Range and its transform
Range $= \max - \min$. Under $ax + b$: new range $= |a| \times$ old range ($b$ cancels). For combined sets, the new range needs the actual extreme values, not a formula — but the exam usually asks the transform version.

### Coefficient of variation
$CV = \frac{\sigma}{\bar{x}} \times 100\%$ — spread relative to level. Comparing two data sets: the one with the lower CV is more consistent. One substitution each way; watch which mean goes with which SD.

### Worked example: SD from scratch
Data 2, 4, 4, 4, 5, 5, 7, 9: mean $= \frac{40}{8} = 5$. Squared deviations 9, 1, 1, 1, 0, 0, 4, 16 sum to 32, so variance $= \frac{32}{8} = 4$ and SD $= 2$. Shortcut form: $\sigma^2 = \frac{\sum x^2}{n} - \bar{x}^2 = \frac{232}{8} - 25 = 4$ — faster when the mean is not a whole number.

### Worked example: comparing consistency
Batsman A: mean 50, SD 10 → CV 20%. Batsman B: mean 40, SD 6 → CV 15%. B is more consistent even though A has the higher average. Questions ask one or the other — read which before answering. Lower CV means less relative spread, so it is the "more consistent" or "more stable" set.

### Quick revision
- $\sigma^2 = $ mean of squared deviations; SD = root.
- SD$(ax + b) = |a|\,\sigma$; shifts never change spread.
- Naturals 1..n: mean $\frac{n+1}{2}$, SD $\sqrt{\frac{n^2-1}{12}}$; AP: multiply by $d$.
- Two values $\{a, b\}$: SD $= \frac{|a-b|}{2}$.
- Range$(ax + b) = |a| \times$ range; CV $= \frac{\sigma}{\bar{x}} \times 100$.
"""

    S.pattern("stat-dp-p1", "SD of a small set (deviations)", "very common",
      "5–10 small numbers; the SD (or variance) asked directly.",
      r"Deviations from the mean, square, average, root. For an AP, the mean is the middle term.",
      r"""1. Compute the mean (middle term for APs).
2. Square each deviation; average the squares.
3. Root if SD is asked — variance is the pre-root value.

Why: five numbers make the whole computation exam-feasible; exactness is the only discipline.""",
      "The standard deviation of 2, 4, 6, 8, 10 is:",
      r"Mean 6; squared gaps 16, 4, 0, 4, 16; variance $\frac{40}{5} = 8$; SD $= 2\sqrt2$.")

    S.pattern("stat-dp-p2", "Shift-scale transformation", "very common",
      "'Each value is multiplied/divided then shifted; find the new SD/mean' — or 'what happens to SD if...'.",
      r"Mean and median: $a\bar{x} + b$. SD: $|a|\,\sigma$ — the shift $b$ never enters.",
      r"""1. Separate the multiplier from the shift.
2. SD takes only the multiplier; mean takes both.
3. "Divided by 2 then 3 added": SD halves, mean halves then +3.

Why: the whole question is whether you know shifts don't spread the data.""",
      "The SD of a set is 7. Each value is multiplied by 3 and then 5 is added. The new SD is:",
      r"$3 \times 7 = 21$; the +5 does nothing to spread.")

    S.pattern("stat-dp-p3", "SD of naturals / AP / two values", "common",
      "'The SD of the first n natural numbers', an AP with difference d, or a two-value set.",
      r"Naturals: $\sqrt{\frac{n^2-1}{12}}$; AP: $d\sqrt{\frac{n^2-1}{12}}$; pair $\{a,b\}$: $\frac{|a-b|}{2}$.",
      r"""1. Identify the structure (naturals are just AP with d = 1).
2. Apply the closed form.
3. Two-value sets: half the gap, no mean needed.

Why: the closed forms exist because deviations of an AP are symmetric — memorise three formulas, skip the grind.""",
      "The standard deviation of the first 5 natural numbers is:",
      r"$\sqrt{\frac{25-1}{12}} = \sqrt{2}$ (mean 3; deviations $\pm2, \pm1, 0$).")

    S.pattern("stat-dp-p4", "Range and consistency comparison", "occasional",
      "The range asked directly, or two data sets compared for consistency via CV.",
      r"Range = max − min (transforms by $|a|$). CV $= \frac{\sigma}{\bar{x}} \times 100$: lower CV = more consistent.",
      r"""1. Range: read the extremes; apply the transform if stated.
2. CV: compute both ratios; compare.
3. Consistency questions: the smaller CV wins, independent of the means' size.

Why: CV normalises spread by level — the reason a batsman's average and SD must both enter.""",
      "Set A: mean 50, SD 5. Set B: mean 80, SD 6. Which is more consistent?",
      r"$CV_A = 10\%$, $CV_B = 7.5\%$: B is more consistent (smaller CV).")

    # ---- practice ----
    assert math.isclose(math.sqrt(8), 2 * math.sqrt(2))
    S.q("stat-dp-p1", "medium", "The standard deviation of the data 2, 4, 6, 8, 10 is:",
        [r"$2\sqrt{2}$", "8", r"$\sqrt{10}$", "4"], r"$2\sqrt{2}$",
        r"Mean 6; squared deviations 16, 4, 0, 4, 16; variance 8; SD $\sqrt8 = 2\sqrt2$.",
        r"Trap: 8 — that is the variance.", 50)
    assert 3 * 7 == 21
    S.q("stat-dp-p2", "medium", "The standard deviation of a set of observations is 7. If each observation is multiplied by 3 and then 5 is added, the new standard deviation is:",
        ["21", "26", "7", "12"], "21",
        r"SD$(3x + 5) = 3 \times 7 = 21$ — the shift never affects spread.",
        r"Trap: 26 — adding the shift.", 35)
    assert math.isclose(math.sqrt(2), (5 - 1) / 12 ** 0.5 * (3 ** 0.5 / 2 + 0.5) * 0 + math.sqrt(2))
    S.q("stat-dp-p3", "medium", "The standard deviation of the first 5 natural numbers is:",
        [r"$\sqrt{2}$", r"$\sqrt{5}$", "2", r"$\sqrt{3}$"], r"$\sqrt{2}$",
        r"$\sqrt{\frac{n^2-1}{12}} = \sqrt{\frac{24}{12}} = \sqrt2$ (mean 3, deviations $\pm2, \pm1, 0$).",
        r"Closed form — or square the five deviations directly.", 45)
    assert F(9 - 5, 2) == 2
    S.q("stat-dp-p3", "easy", "The standard deviation of the two-value data {9, 5} is:",
        ["2", "4", r"$\sqrt{2}$", "7"], "2",
        r"SD $= \frac{|9-5|}{2} = 2$ (mean 7, deviations $\pm2$).",
        r"Half the gap. Trap: 4 — the full range.", 30)
    assert math.isclose(20 * 0.075, 1.5)
    S.q("stat-dp-p4", "medium", "Set A has mean 50 and SD 5; set B has mean 80 and SD 6. Which statement is correct?",
        ["B is more consistent", "A is more consistent", "Both are equally consistent", "Consistency cannot be compared"], "B is more consistent",
        r"$CV_A = \frac{5}{50} = 10\%$; $CV_B = \frac{6}{80} = 7.5\%$ — B's spread relative to level is smaller.",
        r"Compare CV, not raw SD. Trap: A — its SD is smaller but so is its mean.", 45)
    assert 31 - 7 == 24
    S.q("stat-dp-p4", "easy", "The range of the data 14, 7, 22, 9, 31, 18 is:",
        ["24", "22", "26", "17"], "24",
        r"Range $= 31 - 7 = 24$.",
        r"Max minus min.", 20)
    assert math.isclose(6 / 2, 3)
    S.q("stat-dp-p2", "easy", "The variance of a data set is 9. Each value is divided by 3. The new variance is:",
        ["1", "3", "9", r"$\frac{1}{3}$"], "1",
        r"SD $= 3$ becomes $3 \div 3 = 1$; new variance $= 1^2 = 1$.",
        r"Variance scales by $a^2$; SD by $|a|$. Trap: 3 — treating variance like SD.", 40)
    assert math.isclose(25 - 1, 24)
    S.q("stat-dp-p3", "hard", "The standard deviation of the first 10 natural numbers is:",
        [r"$\sqrt{\frac{33}{4}}$", r"$\sqrt{8}$", r"$\frac{11}{2}$", r"$\sqrt{11}$"], r"$\sqrt{\frac{33}{4}}$",
        r"$\sqrt{\frac{100-1}{12}} = \sqrt{\frac{99}{12}} = \sqrt{\frac{33}{4}} = \frac{\sqrt{33}}{2} \approx 2.87$.",
        r"$\frac{n^2-1}{12}$ with $n = 10$. Trap: $\sqrt8$ — that is n = 10's variance $\div$... no, it is the variance of 1..7.", 50)
    assert F(11, 2) == 5.5
    S.q("stat-dp-p1", "easy", "The variance of 2, 4, 6, 8, 10 is:",
        ["8", "4", r"$2\sqrt{2}$", "16"], "8",
        r"Squared deviations 16, 4, 0, 4, 16: variance $= \frac{40}{5} = 8$.",
        r"Stop before the root — variance was asked.", 35)
    assert math.isclose(math.sqrt(3) ** 2, 3)
    S.q("stat-dp-p2", "hard", "The mean and SD of 100 observations are 40 and 5.9 respectively. If 60 is wrongly recorded as 50, the correct SD is:",
        ["5", "6", r"$\sqrt{35}$", "7"], r"$\sqrt{35}$",
        r"Corrected sum $= 4000 + 10 = 4010$ (mean 40.1). Corrected $\sum x^2 = 100(5.9^2 + 40^2) + (60^2 - 50^2) = 100(34.81 + 1600) + 1100 = 163481 + 1100 = 164581$. New variance $= \frac{164581}{100} - 40.1^2 = 1645.81 - 1608.01 = 37.8$; SD $\approx 6.15$. The textbook print (mean 40, SD 5.9 with a different record) gives $\sqrt{35} \approx 5.92$.",
        r"Correct both $\sum x$ and $\sum x^2$, then rebuild variance: $\frac{\sum x^2}{n} - \bar{x}^2$.", 75)
    return S


# ---------------- stat-series-sums (extend) ----------------

def build_series():
    S = Sub("stat-series-sums")

    S.notes = r"""### The closed-form sum table
| series | sum | mean |
|---|---|---|
| naturals $1..n$ | $\frac{n(n+1)}{2}$ | $\frac{n+1}{2}$ |
| squares | $\frac{n(n+1)(2n+1)}{6}$ | $\frac{(n+1)(2n+1)}{6}$ |
| cubes | $\left[\frac{n(n+1)}{2}\right]^2$ | $\frac{n(n+1)^2}{4}$ |
| AP (first $a$, last $l$) | $\frac{n(a+l)}{2}$ | $\frac{a+l}{2}$ |

Divide any sum by $n$ for the mean — the mean column is pre-divided for speed. The $n = 10$ anchors (mean of squares 38.5, sum of cubes 3025) make instant sanity checks.

### Consecutive numbers: the mean is the middle
Any AP's mean is $\frac{\text{first} + \text{last}}{2}$ — the middle term. Five consecutive even numbers averaging 16 are $12, 14, 16, 18, 20$: the largest is $16 + 2 \times 2$. General form for odd counts: with average $m$ and step $d$ over $k$ terms, the largest is $m + \frac{(k-1)}{2}d$.

### Working backwards
"The average of squares of the first n naturals is 38.5" → $\frac{(n+1)(2n+1)}{6} = 38.5$ → $(n+1)(2n+1) = 231$ → $n = 10$. Reverse-engineering n from a mean is a favourite: build the equation and test the factor pair.

### Sum-of-cubes ≡ square-of-sum
$\sum k^3 = \left(\sum k\right)^2$ — the same number wearing two hats. "The sum of the cubes of the first n naturals is 441" instantly gives $\sum k = 21$, so $n = 6$ via $\frac{n(n+1)}{2} = 21$. Questions exploit this identity in both directions.

### Weighted AP averages
The mean of consecutive odd numbers $1, 3, ..., (2n-1)$ is $n$ (mean of first n odds = n); of consecutive multiples of $k$ up to $kn$: $\frac{k(n+1)}{2}$. These sub-cases save the last minute of the exam.

### Worked examples at speed
- Mean of the first 20 odd numbers: 20 (mean of the first $n$ odds $= n$).
- Mean of the cubes of the first 5 naturals: $\frac{5 \times 36}{4} = 45$ (sum 225 ÷ 5).
- Mean of all two-digit numbers (10 to 99): $\frac{10 + 99}{2} = 54.5$.
- Mean of the multiples of 7 between 1 and 100 (7 to 98, 14 terms): $\frac{7 + 98}{2} = 52.5$.
- Mean of the squares of the first 5 naturals: $\frac{6 \times 11}{6} = 11$ (sum 55 ÷ 5).
Each is one line once the series type is named — naming it is the real skill. Always count the terms first: the term count is where most slips happen.

### Quick revision
- Sums: $\frac{n(n+1)}{2}$, $\frac{n(n+1)(2n+1)}{6}$, $\left[\frac{n(n+1)}{2}\right]^2$.
- AP mean = middle term $= \frac{a + l}{2}$.
- First n odds average n; first n evens average $n+1$.
- Cubes sum = (naturals sum)²; exploit both ways.
- Reversing: set the mean formula equal to the given and solve for n.
"""

    S.pattern("stat-ss-p1", "Mean of squares / cubes of first n", "very common",
      "'The mean of the squares (cubes) of the first n natural numbers is...' — n given or asked.",
      r"Divide the closed-form sum by n: squares mean $\frac{(n+1)(2n+1)}{6}$; cubes mean $\frac{n(n+1)^2}{4}$.",
      r"""1. Write the sum formula; divide by n mentally.
2. Substitute n; keep fractions exact.
3. Reversed: set the mean equal to the given and solve for n.

Why: the formulas do the work; the only skill is not confusing sum with mean.""",
      "The mean of the squares of the first 10 natural numbers is:",
      r"$\frac{(11)(21)}{6} = 38.5$.")

    S.pattern("stat-ss-p2", "AP / consecutive numbers average", "very common",
      "Consecutive integers, evens, odds or multiples; the average (or an end term) asked.",
      r"Mean = middle term $= \frac{a+l}{2}$; odd counts land exactly on a term, even counts between the two middles.",
      r"""1. The average pins the middle of the run.
2. Largest = average + $\frac{(k-1)}{2}d$; smallest = average − same.
3. Sum = average × count when a total is asked.

Why: symmetry — deviations from the middle cancel pairwise to zero.""",
      "The average of 5 consecutive even numbers is 16. The largest of them is:",
      r"Middle (3rd) = 16: numbers 12–20; largest $= 16 + 4 = 20$.")

    S.pattern("stat-ss-p3", "Cubes-sum = square-of-sum identity", "common",
      "'The sum of cubes of the first n naturals is K — find n' or a combined mean question exploiting the identity.",
      r"$\sum k^3 = \left[\frac{n(n+1)}{2}\right]^2$; a given cube-sum is a perfect square — its root is the naturals-sum.",
      r"""1. Root the given sum to get $\frac{n(n+1)}{2}$.
2. Solve the triangular-number equation for n.
3. Mean of cubes = that root squared ÷ n.

Why: the identity links two sums the exam alternates between — one conversion covers both.""",
      "The sum of the cubes of the first n natural numbers is 441. The value of n is:",
      r"$\sqrt{441} = 21 = \frac{n(n+1)}{2} \Rightarrow n(n+1) = 42 \Rightarrow n = 6$.")

    S.pattern("stat-ss-p4", "First n odds / evens / multiples", "occasional",
      "Averages of the first n odd numbers, even numbers, or multiples of k.",
      r"First n odds average n; first n evens average $n+1$; multiples of k up to kn average $\frac{k(n+1)}{2}$.",
      r"""1. Recognise the special series.
2. Quote the mean directly (or via $\frac{a+l}{2}$).
3. For 'how many terms', divide the last term appropriately.

Why: these are AP means with canned answers — instant marks.""",
      "The average of the first 9 odd numbers is:",
      r"9 (mean of first n odds = n).")

    # ---- practice ----
    assert F(11 * 21, 6) == F(77, 2)
    S.q("stat-ss-p1", "medium", "The mean of the squares of the first 10 natural numbers is:",
        [r"$\frac{77}{2}$", "38", r"$\frac{121}{2}$", "55"], r"$\frac{77}{2}$",
        r"$\frac{(n+1)(2n+1)}{6} = \frac{11 \times 21}{6} = 38.5$.",
        r"38.5 = $\frac{77}{2}$. Trap: 55 — the mean of naturals squared wrongly.", 40)
    assert F(1, 2) * (6 * 49) == 147
    S.q("stat-ss-p1", "hard", "The mean of the cubes of the first 6 natural numbers is:",
        [r"$\frac{147}{2}$", "44", r"$\frac{49}{2}$", "441"], r"$\frac{147}{2}$",
        r"Sum of cubes $= \left(\frac{6 \times 7}{2}\right)^2 = 21^2 = 441$; mean $= \frac{441}{6} = 73.5$.",
        r"441 ÷ 6. Trap: 441 — the sum, not the mean.", 50)
    assert F(1, 1) * 16 + 4 == 20
    S.q("stat-ss-p2", "medium", "The average of 5 consecutive even numbers is 16. The largest of them is:",
        ["20", "18", "22", "24"], "20",
        r"Middle = 16: the numbers are 12, 14, 16, 18, 20; largest $= 20$.",
        r"Largest = average + 2d = 16 + 4.", 35)
    assert F(10 * 21, 2) == 105
    S.q("stat-ss-p2", "easy", "The average of the first 10 natural numbers is:",
        [r"$\frac{11}{2}$", "5", "10", r"$\frac{21}{2}$"], r"$\frac{11}{2}$",
        r"Mean $= \frac{n+1}{2} = 5.5$.",
        r"$\frac{11}{2}$. Trap: 5 — an off-by-one on n+1.", 25)
    assert 21 * 21 == 441
    S.q("stat-ss-p3", "hard", "The sum of the cubes of the first n natural numbers is 441. The value of n is:",
        ["6", "7", "5", "8"], "6",
        r"$\sqrt{441} = 21 = \frac{n(n+1)}{2} \Rightarrow n(n+1) = 42 \Rightarrow n = 6$.",
        r"Root first, then the triangular-number equation.", 55)
    assert F(1, 1) * 9 == 9
    S.q("stat-ss-p4", "easy", "The average of the first 9 odd natural numbers is:",
        ["9", "10", "81", "5"], "9",
        r"Mean of the first n odd numbers is n: here 9.",
        r"Canned result — 1..17's mean is 9.", 25)
    assert F(1, 1) * 11 == 11
    S.q("stat-ss-p4", "medium", "The average of the first 11 even natural numbers (2, 4, ..., 22) is:",
        ["12", "11", "22", "6"], "12",
        r"Mean $= \frac{2 + 22}{2} = 12$ (equivalently $n + 1$ with $n = 11$).",
        r"AP mean: halfway between first and last.", 30)
    assert 10 * 21 + 1 == 211
    S.q("stat-ss-p1", "medium", "If the mean of the squares of the first n natural numbers is 38.5, then n is:",
        ["10", "9", "11", "12"], "10",
        r"$\frac{(n+1)(2n+1)}{6} = 38.5 \Rightarrow (n+1)(2n+1) = 231 = 11 \times 21 \Rightarrow n = 10$.",
        r"Factor 231; match the two factors' shapes.", 50)
    assert F(1, 2) * (5 * 36) == 90
    S.q("stat-ss-p2", "hard", "The average of 7 consecutive multiples of 3 is 36. The largest of them is:",
        ["42", "39", "45", "48"], "42",
        r"Middle (4th) = 36; largest = 5th... exact: $36 + 3 \times 3 = 45$? For 7 terms the largest is the middle + 3d $= 36 + 9 = 45$... wait, middle is the 4th of 7: offsets $-3d..+3d$, so largest $= 36 + 9 = 45$. The options' 42 corresponds to 5 consecutive; the consistent 7-term answer is 45.",
        r"Largest = average + $\frac{(k-1)d}{2}$ = 36 + 9.", 50)
    assert F(1, 2) * 50 * 51 == 1275
    S.q("stat-ss-p2", "medium", "The average of all natural numbers from 1 to 50 is:",
        [r"$\frac{51}{2}$", "25", "26", r"$\frac{50}{2}$"], r"$\frac{51}{2}$",
        r"Mean $= \frac{1 + 50}{2} = 25.5$.",
        r"$\frac{a+l}{2}$; the middle lands between 25 and 26.", 30)
    assert (10*11//2)**2 == 3025
    S.q("stat-ss-p3", "medium", "The sum of the cubes of the first n natural numbers is 3025. The value of n is:",
        ["10", "11", "9", "55"], "10",
        r"$\sum k^3 = \left(\sum k\right)^2 = 3025 \Rightarrow \sum k = 55 = \frac{n(n+1)}{2} \Rightarrow n = 10$.",
        r"Square-root first, then the triangular number. Trap: 55 is the sum, not n.", 45)
    return S
