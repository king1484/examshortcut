import sympy as sp
from qa_common import Q, F, T, S, P, U, write_topic

# ---------------------------------------------------------------- sanity checks
# combined mean
assert sp.Rational(30 * 62 + 20 * 58, 50) == sp.Rational(302, 5)  # 60.4
# empirical relation: median = (mode + 2*mean)/3
assert (45 + 2 * 27) / 3 == 33
assert 3 * 32 - 2 * 30 == 36
# median of even set
assert sp.Rational(6 + 8, 2) == 7
# mean of squares of first 10 naturals
assert sp.Rational(10 * 11 * 21, 6) / 10 == sp.Rational(77, 2)  # 38.5
# mean of cubes of first 6 naturals
assert sp.Rational(6 * 7, 2) ** 2 / 6 == sp.Rational(147, 2)  # 73.5
# teacher joining: 25*35.5 - 24*35
assert sp.Rational(25 * 355, 10) - 24 * 35 == sp.Rational(95, 2)  # 47.5
# grouped median: L=20, n/2=15, cf=10, f=10, h=10
assert 20 + sp.Rational(15 - 10, 10) * 10 == 25
# grouped mode: L=30, f1=12, f0=8, f2=6, h=10
assert 30 + sp.Rational(12 - 8, 2 * 12 - 8 - 6) * 10 == 34
# SD of 2,4,6,8,10 = sqrt(8)
data = sp.Matrix([2, 4, 6, 8, 10])
assert sp.sqrt(sum((v - 6) ** 2 for v in data) / 5) == sp.sqrt(8) == 2 * sp.sqrt(2)
# misread value: (600 + 3)/30 = 20.1
assert sp.Rational(600 + 3, 30) == sp.Rational(201, 10)
# batsman: (360 + x)/9 = 50 -> x = 90
assert 9 * 50 - 8 * 45 == 90
# SD scaling: sd 7, x -> 3x + 5 => sd 21
assert 3 * 7 == 21
# overlapping means: middle = 10*3 + 15*3 - 12*5
assert 3 * 10 + 3 * 15 - 5 * 12 == 15
# consecutive even: middle 16 -> largest 20
assert 16 + 2 * 2 == 20
# SD of first n naturals: sqrt((n^2-1)/12); n=5 -> sqrt(2)
assert sp.sqrt(sp.Rational(5 ** 2 - 1, 12)) == sp.sqrt(2)
# range
assert 31 - 7 == 24

# ---------------------------------------------------------------- subtopics
subtopics = [
S("stat-mean", "Mean, weighted mean and combined mean",
r"""
$$\text{Mean}=\frac{\sum x_i}{n}$$

Three moves cover almost all CGL average questions:

- **Missing value**: asked value $=$ (target mean $\times$ new $n$) $-$ (old sum).
- **Combined mean** of two groups: $\bar x=\dfrac{n_1\bar x_1+n_2\bar x_2}{n_1+n_2}$ — a weighted average by group size.
- **Member change**: if replacing/adding one member shifts the average by $d$, the member's value is
  old mean $\pm$ (change $\times$ new count).
""",
[
F("Mean", r"\bar{x}=\frac{x_1+x_2+\cdots+x_n}{n}=\frac{\sum x_i}{n}"),
F("Combined mean", r"\bar{x}=\frac{n_1\bar{x}_1+n_2\bar{x}_2}{n_1+n_2}"),
F("Weighted mean", r"\bar{x}=\frac{\sum w_i x_i}{\sum w_i}"),
F("Member replacement", r"\text{value brought in}=\text{old mean}+(\text{avg shift})\times n_{\text{new}}"),
],
[
T("Think in totals, not averages",
r"""Every average question is one subtraction away if you track $\text{sum}=\text{mean}\times n$. Convert both
sides to sums before combining.""",
r"The average of 5 numbers is 27. If four of them are 23, 25, 28 and 26, find the fifth.",
r"Total $=135$, present $=102$, fifth $=33$."),
T("Average of equal-sized groups is the plain middle",
r"""For two groups of **equal** size the combined mean is just $\frac{\bar x_1+\bar x_2}{2}$; weighting only
matters when sizes differ.""",
r"Two classes of 40 students each average 62% and 68%. Find the combined average.",
r"Equal sizes: $\frac{62+68}{2}=65\%$."),
],
[
"Forgetting to update $n$ when a member joins or leaves (dividing by the old count).",
"Plain-averaging group means with different group sizes.",
"Median confused with mean when 'average of positions' is asked.",
]),
S("stat-median-mode", "Median and mode of raw data",
r"""
**Median**: sort first. For $n$ values,
- $n$ odd: the $\left(\frac{n+1}{2}\right)$-th value.
- $n$ even: mean of the $\frac{n}{2}$-th and $\left(\frac{n}{2}+1\right)$-th values.

**Mode**: the most frequent value (a list can have several or none).

**Empirical relation** (approximate, but treated as exact in CGL):
$$\text{mode}=3\,\text{median}-2\,\text{mean}\quad\Leftrightarrow\quad \text{median}=\frac{\text{mode}+2\,\text{mean}}{3}$$
""",
[
F("Median (odd)", r"\text{median}=\left(\frac{n+1}{2}\right)\text{th value}"),
F("Median (even)", r"\text{median}=\frac{(\frac{n}{2})\text{th}+(\frac{n}{2}+1)\text{th}}{2}"),
F("Mode", r"\text{mode}=\text{most frequent value}"),
F("Empirical relation", r"\text{mode}=3\,\text{median}-2\,\text{mean}"),
],
[
T("Sort, then count to the middle",
r"""Never find a median of unsorted data. For small sets, sort and walk in from both ends — the meeting point
is the answer.""",
r"Find the median of 8, 3, 11, 6, 14, 5.",
r"Sorted: 3, 5, 6, 8, 11, 14. Even count → $\frac{6+8}{2}=7$."),
T("The 3M relation runs both ways",
r"""Given any two of mean/median/mode, the third is one substitution away — keep the form
$\text{mode}=3m-2\bar x$ in mind.""",
r"If median = 32 and mean = 30, find the mode.",
r"$3\times32-2\times30=36$."),
],
[
"Taking the middle value without sorting the data.",
"Averaging the two middle values for odd $n$ (that is only for even $n$).",
"Applying the empirical relation to small datasets where it need not hold — in CGL, just use the formula.",
]),
S("stat-grouped", "Median and mode of grouped data",
r"""
For class-interval data:

**Median** (continuous classes, width $h$): locate the median class where cumulative frequency first reaches
$n/2$, then
$$\text{median}=L+\frac{\frac{n}{2}-cf}{f}\,h$$
($L$ = lower limit of median class, $cf$ = cumulative frequency before it, $f$ = its frequency).

**Mode**: the modal class has the highest frequency $f_1$ (neighbours $f_0$ below, $f_2$ above):
$$\text{mode}=L+\frac{f_1-f_0}{2f_1-f_0-f_2}\,h$$
""",
[
F("Grouped median", r"\text{median}=L+\frac{\frac{n}{2}-cf}{f}\,h"),
F("Grouped mode", r"\text{mode}=L+\frac{f_1-f_0}{2f_1-f_0-f_2}\,h"),
F("Cumulative frequency", r"cf_i=f_1+f_2+\cdots+f_i"),
F("Grouped mean (midpoints)", r"\bar{x}=\frac{\sum f_i m_i}{\sum f_i},\quad m_i=\frac{L_i+U_i}{2}"),
],
[
T("Find the median class by cf, not by eye",
r"""Build the cf column, stop at the first cf $\ge n/2$. That row's lower limit is $L$. Everything else is
substitution.""",
r"Classes 0-10, 10-20, 20-30, 30-40, 40-50 have frequencies 4, 6, 10, 8, 2. Find the median.",
r"$n=30$, $n/2=15$; cf reaches 20 at 20-30. $L=20$, $cf=10$, $f=10$, $h=10$: median $=20+\frac{5}{10}\times10=25$."),
T("Modal class first, formula second",
r"""The modal class is just the tallest bar. If it sits at an edge, the missing neighbour counts 0 in the
formula.""",
r"Classes 10-20, 20-30, 30-40, 40-50, 50-60 have frequencies 5, 8, 12, 6, 3. Find the mode.",
r"Modal class 30-40: $30+\frac{12-8}{24-8-6}\times10=30+\frac{4}{10}\times10=34$."),
],
[
"Using $n/2$ instead of $(n+1)/2$ in the grouped median — grouped data always uses $n/2$.",
"Taking $cf$ as the cumulative frequency including the median class (it must exclude it).",
"Reading class limits as inclusive when the data is exclusive (10-20 vs 10-19.5).",
]),
S("stat-dispersion", "Range, variance and standard deviation",
r"""
- **Range** $=$ maximum $-$ minimum.
- **Variance**: $\sigma^2=\frac{1}{n}\sum(x_i-\bar x)^2$. **Standard deviation** $\sigma=\sqrt{\text{variance}}$.

**Transformation rules** (the CGL favourite): if every value $x$ becomes $a x+b$,
$$\text{new mean}=a\bar{x}+b,\qquad \text{new SD}=|a|\,\sigma\ (b\ \text{does not touch SD})$$
Adding/subtracting a constant shifts the mean but leaves SD unchanged.

Useful closed forms for the first $n$ naturals: mean $=\frac{n+1}{2}$, SD $=\sqrt{\frac{n^2-1}{12}}$.
""",
[
F("Range", r"\text{range}=x_{\max}-x_{\min}"),
F("Variance and SD", r"\sigma^2=\frac{1}{n}\sum(x_i-\bar{x})^2,\quad \sigma=\sqrt{\sigma^2}"),
F("Shift-scale rule", r"\text{SD}(a x+b)=|a|\,\text{SD}(x)"),
F("SD of 1 to n", r"\sigma=\sqrt{\frac{n^2-1}{12}}"),
],
[
T("Shifts never change spread",
r"""A question saying "5 is added to every number, what happens to SD?" answers itself: nothing. Only the
multiplier scales SD.""",
r"The SD of a set is 7. Each value is multiplied by 3 and then 5 is added. Find the new SD.",
r"Scale by $a=3$, shift ignores: new SD $=21$."),
T("Small set? Deviations from the mean",
r"""For 5-10 numbers, subtract the mean, square, average, take the root — keep squares exact with fractions.""",
r"Find the SD of 2, 4, 6, 8, 10.",
r"Mean 6; squared gaps $16,4,0,4,16$; variance $=\frac{40}{5}=8$; SD $=2\sqrt2$."),
],
[
"Adding the shift $b$ into the new SD.",
"Reporting variance when SD is asked (or the reverse) — check the root.",
"Range computed as difference of the two extreme means instead of the data extremes.",
]),
S("stat-series-sums", "Averages of special series",
r"""
Closed-form sums give instant averages for standard series (first $n$ of each):

| series | sum | mean |
|---|---|---|
| naturals $1..n$ | $\frac{n(n+1)}{2}$ | $\frac{n+1}{2}$ |
| squares | $\frac{n(n+1)(2n+1)}{6}$ | $\frac{(n+1)(2n+1)}{6}$ |
| cubes | $\left[\frac{n(n+1)}{2}\right]^2$ | $\frac{n(n+1)^2}{4}$ |
| AP (first $a$, last $l$) | $\frac{n(a+l)}{2}$ | $\frac{a+l}{2}$ |

For consecutive equally-spaced numbers (AP), the **mean is the middle term** — with an even count, halfway
between the two middles.
""",
[
F("First n naturals", r"\sum_{1}^{n}k=\frac{n(n+1)}{2},\quad \text{mean}=\frac{n+1}{2}"),
F("Squares", r"\sum_{1}^{n}k^2=\frac{n(n+1)(2n+1)}{6}"),
F("Cubes", r"\sum_{1}^{n}k^3=\left[\frac{n(n+1)}{2}\right]^2"),
F("AP mean", r"\text{mean of AP}=\frac{\text{first}+\text{last}}{2}"),
],
[
T("Consecutive numbers: average = middle",
r"""For any run of consecutive terms (odd, even, naturals), the average equals the median — the middle term.
No summation needed.""",
r"The average of 5 consecutive even numbers is 16. Find the largest.",
r"Middle (3rd) $=16$; largest $=16+2\times2=20$."),
T("Squares and cubes via the sums",
r"""Divide the closed-form sum by $n$; memorise the $n=10$ anchor (mean of squares $=38.5$) as a sanity check.""",
r"Find the mean of the cubes of the first 6 natural numbers.",
r"Sum $=\left(\frac{6\times7}{2}\right)^2=441$; mean $=\frac{441}{6}=73.5$."),
],
[
"Using $\\frac{(n+1)(2n+1)}{6}$ (the mean of squares) as if it were a sum.",
"Off-by-one on 'consecutive': between the middle two for even counts, exactly the middle term for odd.",
"Cubes sum confused with square of sum of naturals (they are equal, but the mean needs dividing by $n$).",
]),
]

patterns = [
P("Combined average of two groups", "very common",
  r"Two classes/teams/genders with different averages merge into one.",
  r"Weighted mean $\frac{n_1\bar x_1+n_2\bar x_2}{n_1+n_2}$; equal sizes → plain average."),
P("Member joins / leaves / replaced", "very common",
  r"A new batsman, teacher or watch changes the group average by a stated amount.",
  r"Work in totals: new value = target total − old total, i.e. old mean + shift × new count."),
P("Empirical 3M relation", "very common",
  r"Two of mean/median/mode given (often as 27/45 style numbers), third asked.",
  r"$\text{mode}=3\,\text{median}-2\,\text{mean}$; solve directly."),
P("Median/mode of grouped data", "common",
  r"A frequency table with class intervals; sometimes a missing frequency to solve for.",
  r"cf column → median class → $L+\frac{n/2-cf}{f}h$; tallest frequency → modal class formula."),
P("Effect of scaling on mean and SD", "common",
  r"'Each value is multiplied/divided and then shifted; find new mean/SD/median.'",
  r"Mean and median scale by $a$ then shift by $b$; SD only scales by $|a|$."),
P("Averages of consecutive / special series", "common",
  r"First n naturals/squares/cubes, consecutive odds/evens, AP terms.",
  r"AP → middle term; squares/cubes → closed-form sums divided by $n$."),
]

# ---------------------------------------------------------------- solved examples
solved = []

solved.append(Q("stat-s01",
r"The average weight of 30 boys is 62 kg and that of 20 girls is 58 kg. Find the average weight of the class.",
U(" kg", sp.Rational(302, 5), 60, 61, 59), sp.Rational(302, 5),
r"""
Combined mean $=\frac{30\times62+20\times58}{30+20}=\frac{1860+1160}{50}=\frac{3020}{50}=60.4$ kg.
""",
r"Track totals: $1860+1160=3020$ over 50 students → 60.4 kg. (Sizes differ, so don't just average 62 and 58.)",
"easy", "stat-mean", "combined mean", 40))

solved.append(Q("stat-s02",
r"The mean of a distribution is 27 and the mode is 45. Using the empirical relation, the median is:",
U("", 33, 36, 31, 34), 33,
r"""
Median $=\frac{\text{mode}+2\times\text{mean}}{3}=\frac{45+54}{3}=\frac{99}{3}=33$.
""",
r"Rearranged empirical relation: median $=\frac{\text{mode}+2\,\text{mean}}{3}=\frac{45+54}{3}=33$.",
"easy", "stat-median-mode", "empirical relation", 30))

solved.append(Q("stat-s03",
r"Find the median of 8, 3, 11, 6, 14, 5.",
U("", 7, sp.Rational(13, 2), 6, sp.Rational(15, 2)), 7,
r"""
Sorted: 3, 5, 6, 8, 11, 14. With $n=6$ (even), the median is the mean of the 3rd and 4th values:

$\frac{6+8}{2}=7$.
""",
r"Sort first, then average the two middle terms: $\frac{6+8}{2}=7$. Trap: $6.5$ = mean of middle two *unsorted* neighbors.",
"easy", "stat-median-mode", "median of even set", 35))

solved.append(Q("stat-s04",
r"The mean of the squares of the first 10 natural numbers is:",
U("", sp.Rational(77, 2), 55, 38, sp.Rational(121, 2)), sp.Rational(77, 2),
r"""
Sum of squares $=\frac{10\times11\times21}{6}=385$. Mean $=\frac{385}{10}=38.5$.
""",
r"Formula chain: $\frac{(n+1)(2n+1)}{6}=\frac{11\times21}{6}=38.5$ for the mean (no need to write the sum).",
"medium", "stat-series-sums", "mean of squares", 40))

solved.append(Q("stat-s05",
r"The standard deviation of a set of observations is 7. If each observation is multiplied by 3 and then 5 is added, the new standard deviation is:",
U("", 21, 26, 7, 12), 21,
r"""
Shifting by 5 changes only the mean. Multiplying by 3 multiplies the SD:

new SD $=3\times7=21$.
""",
r"SD$(3x+5)=3\times$SD$(x)=21$ — the +5 never affects spread. Trap: 26 (added the shift).",
"medium", "stat-dispersion", "SD transformation", 35))

# ---------------------------------------------------------------- practice
pr = []

pr.append(Q("stat-q01",
r"The average of 5 numbers is 27. Four of the numbers are 23, 25, 28 and 26. The fifth number is:",
U("", 33, 32, 34, 31), 33,
r"Total $=5\times27=135$; given sum $=102$; fifth $=135-102=33$.",
r"Total minus known sum: $135-102=33$.",
"easy", "stat-mean", "missing value", 30))

pr.append(Q("stat-q02",
r"The median of 12, 5, 9, 7, 15 is:",
U("", 9, 7, 12, sp.Rational(21, 2)), 9,
r"Sorted: 5, 7, 9, 12, 15. The middle (3rd) value is 9.",
r"Sort → pick the middle term for odd $n$: 9.",
"easy", "stat-median-mode", "median odd set", 25))

pr.append(Q("stat-q03",
r"The mode of the data 2, 3, 3, 5, 3, 7, 2, 3 is:",
U("", 3, 2, 5, 7), 3,
r"3 occurs four times — more than any other value, so the mode is 3.",
r"Count frequencies: 3 appears 4 times → mode 3.",
"easy", "stat-median-mode", "mode raw data", 20))

pr.append(Q("stat-q04",
r"The average of the first 10 natural numbers is:",
U("", sp.Rational(11, 2), 5, 10, sp.Rational(21, 2)), sp.Rational(11, 2),
r"Mean $=\frac{n+1}{2}=\frac{11}{2}=5.5$.",
r"$\frac{n+1}{2}=\frac{11}{2}=5.5$. (Sum $55$ over $10$ also gives it.)",
"easy", "stat-series-sums", "first n naturals", 25))

pr.append(Q("stat-q05",
r"The range of the data 14, 7, 22, 9, 31, 18 is:",
U("", 24, 17, 22, 26), 24,
r"Range $=31-7=24$.",
r"Max minus min: $31-7=24$.",
"easy", "stat-dispersion", "range", 20))

pr.append(Q("stat-q06",
r"The average weight of 24 students of a class is 35 kg. When the teacher is included, the average rises by 0.5 kg. The weight of the teacher is:",
U(" kg", sp.Rational(95, 2), 47, sp.Rational(89, 2), 35), sp.Rational(95, 2),
r"""
New total $=25\times35.5=887.5$ kg; students' total $=24\times35=840$ kg.

Teacher $=887.5-840=47.5$ kg.
""",
r"Teacher = old mean + shift × new count $=35+0.5\times25=47.5$ kg.",
"medium", "stat-mean", "member joins", 45))

pr.append(Q("stat-q07",
r"If the median of a distribution is 32 and the mean is 30, then the mode is:",
U("", 36, 34, 35, 33), 36,
r"$\text{mode}=3\times32-2\times30=96-60=36$.",
r"Empirical relation straight in: $3m-2\bar x=36$.",
"medium", "stat-median-mode", "empirical relation", 30))

pr.append(Q("stat-q08",
r"For the classes 0-10, 10-20, 20-30, 30-40, 40-50 with frequencies 4, 6, 10, 8, 2, the median is:",
U("", 25, 26, 22, 27), 25,
r"""
$n=30$, $n/2=15$. Cumulative frequencies: 4, 10, 20, 28, 30 — the median class is 20-30 ($cf=20\ge15$).

Median $=20+\frac{15-10}{10}\times10=25$.
""",
r"cf first reaching 15 is 20 at class 20-30: $20+\frac{5}{10}\times10=25$. Trap: using $cf=20$ inside the formula instead of the *previous* cf 10.",
"medium", "stat-grouped", "grouped median", 60))

pr.append(Q("stat-q09",
r"The average of 5 consecutive even numbers is 16. The largest of them is:",
U("", 20, 18, 22, 24), 20,
r"The middle (3rd) number is 16, so the numbers are 12, 14, 16, 18, 20. Largest $=20$.",
r"Average = middle term: 16 is the 3rd → largest $=16+4=20$.",
"medium", "stat-series-sums", "consecutive evens", 35))

pr.append(Q("stat-q10",
r"The standard deviation of the data 2, 4, 6, 8, 10 is:",
[(r"$2\sqrt{2}$", 2 * sp.sqrt(2)), ("8", 8), (r"$\sqrt{10}$", sp.sqrt(10)), ("4", 4)], 2 * sp.sqrt(2),
r"""
Mean $=6$; squared deviations $16, 4, 0, 4, 16$; variance $=\frac{40}{5}=8$; SD $=\sqrt8=2\sqrt2$.
""",
r"For an AP, mean is the middle term (6); average the squared gaps → 8 → $2\sqrt2$. Trap: 8 is the variance.",
"medium", "stat-dispersion", "SD small set", 50))

pr.append(Q("stat-q11",
r"The average of 30 results was 20. It was later found that a result of 24 had been wrongly recorded as 21. The corrected average is:",
U("", sp.Rational(201, 10), 20, sp.Rational(203, 10), sp.Rational(199, 10)), sp.Rational(201, 10),
r"Shortfall $=24-21=3$. Corrected mean $=\frac{600+3}{30}=20.1$.",
r"Add the error to the total and re-divide: $\frac{603}{30}=20.1$.",
"medium", "stat-mean", "misread value", 40))

pr.append(Q("stat-q12",
r"A batsman scores 45 runs on average in 8 innings. How many runs must he score in the 9th innings to raise his average to 50?",
U("", 90, 95, 85, 50), 90,
r"Required total $=9\times50=450$; current $=8\times45=360$; needed $=450-360=90$.",
r"Target total minus current total: $450-360=90$. (Shortcut: $50+9\times5=90$.)",
"medium", "stat-mean", "raise the average", 40))

pr.append(Q("stat-q13",
r"The mean of the cubes of the first 6 natural numbers is:",
U("", sp.Rational(147, 2), 441, 44, sp.Rational(49, 2)), sp.Rational(147, 2),
r"""
Sum of cubes $=\left[\frac{6\times7}{2}\right]^2=21^2=441$. Mean $=\frac{441}{6}=73.5$.
""",
r"$\left(\frac{n(n+1)}{2}\right)^2/n$: $441/6=73.5$. Trap: 441 (the sum, not the mean).",
"hard", "stat-series-sums", "mean of cubes", 50))

pr.append(Q("stat-q14",
r"For the classes 10-20, 20-30, 30-40, 40-50, 50-60 with frequencies 5, 8, 12, 6, 3, the mode is:",
U("", 34, 32, 36, 33), 34,
r"""
Modal class: 30-40 ($f_1=12$, $f_0=8$, $f_2=6$, $h=10$).

Mode $=30+\frac{12-8}{2(12)-8-6}\times10=30+\frac{4}{10}\times10=34$.
""",
r"Tallest bar 30-40, then $30+\frac{4}{10}\times10=34$. Trap: 32 (using $\frac{f_1-f_0}{2}$ shape instead of the full formula).",
"hard", "stat-grouped", "grouped mode", 60))

pr.append(Q("stat-q15",
r"The mean of 5 observations is 12. The mean of the first 3 is 10 and that of the last 3 is 15. The third observation is:",
U("", 15, 12, 18, 10), 15,
r"""
Total $=5\times12=60$. First 3 sum $=30$, last 3 sum $=45$; their union double-counts the middle term:

Middle $=30+45-60=15$.
""",
r"Overlapping groups: middle = sum(first 3) + sum(last 3) − total = $30+45-60=15$.",
"hard", "stat-mean", "overlapping means", 55))

topic = {
    "id": "statistics",
    "sectionId": "quant",
    "title": "Statistics",
    "order": 18,
    "importance": "high",
    "avgQuestions": {"tier1": 3, "tier2": 4},
    "summary": "Mean, median, mode and simple dispersion: raw-data medians, the mode = 3·median − 2·mean relation, grouped-data formulas, range and SD with shift-scale effects. "
               "Every question is formula-driven with small numbers — statistics is among the most scoring blocks in the Quant paper once the six formulas above are memorised.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
