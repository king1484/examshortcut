"""Phase-2 deep content build for quant/statistics. Run: py -3 statistics.py"""
from _lib import apply_topic
import stat_part1
import stat_part2
import stat_part3


def P(pattern, frequency, howToSpot, approach, subtopic, ex_q, ex_sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot,
            "approach": approach, "subtopic": subtopic,
            "example": {"q": ex_q, "solution": ex_sol}}


PYQ = [
    P("Combined average of two groups", "very common",
      "Two classes/teams/genders with different sizes and averages merge into one.",
      r"Weighted mean $\frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1+n_2}$; equal sizes → plain average of the means.",
      "stat-mean",
      r"30 boys average 62 kg and 20 girls average 58 kg. The class average is:",
      r"$\frac{30 \times 62 + 20 \times 58}{50} = 60.4$ kg."),
    P("Member joins / leaves / replaced", "very common",
      "A new batsman, teacher or watch changes the group average by a stated amount.",
      r"Work in totals: newcomer $= b + n(b-a)$; leaver $= a + n(a-b)$; replacement carries $n \times$ the shift.",
      "stat-mean",
      r"24 students average 35 kg; with the teacher it rises 0.5 kg. The teacher's weight is:",
      r"$35 + 25 \times 0.5 = 47.5$ kg."),
    P("Empirical 3M relation", "very common",
      "Two of mean/median/mode given (often clean integers), the third asked.",
      r"$\text{mode} = 3\,\text{median} - 2\,\text{mean}$; rearrange for whichever is missing.",
      "stat-median-mode",
      r"Median 32, mean 30. The mode is:",
      r"$3 \times 32 - 2 \times 30 = 36$."),
    P("Median/mode of grouped data", "common",
      "A frequency table with class intervals; sometimes a missing frequency to solve for.",
      r"cf column → median class → $L + \frac{n/2 - cf}{f}h$; tallest frequency → mode formula.",
      "stat-grouped",
      r"Frequencies 4, 6, 10, 8, 2 over classes 0-10...40-50. The median is:",
      r"$20 + \frac{15-10}{10} \times 10 = 25$."),
    P("Effect of scaling on mean and SD", "common",
      "'Each value is multiplied/divided and then shifted; find the new mean/SD/median.'",
      r"Mean and median scale by $a$ then shift by $b$; SD only scales by $|a|$ — the shift never enters.",
      "stat-dispersion",
      r"SD is 7; each value is tripled and 5 added. The new SD is:",
      r"$3 \times 7 = 21$."),
    P("Averages of consecutive / special series", "common",
      "First n naturals/squares/cubes, consecutive odds/evens, AP terms.",
      r"AP → middle term; squares/cubes → closed-form sums ÷ n; cubes sum = (naturals sum)².",
      "stat-series-sums",
      r"The mean of the squares of the first 10 naturals is:",
      r"$\frac{11 \times 21}{6} = 38.5$."),
    P("Raise-the-average / innings problems", "common",
      "'How many runs in the next innings to raise the average to X?'",
      r"Needed = new total − old total $= (n+1)X - n\bar{x}$, i.e. $X + n(X - \bar{x})$.",
      "stat-mean",
      r"Averaging 45 over 8 innings; score in the 9th to average 50:",
      r"$450 - 360 = 90$."),
    P("Misrecorded value corrections", "occasional",
      "A value was wrongly recorded; the corrected mean (or SD) asked.",
      r"Correct the total by (true − recorded); mean shifts by $\frac{\text{error}}{n}$. For SD, correct $\sum x^2$ too.",
      "stat-mean",
      r"Average of 30 results was 20; 24 was recorded as 21. The corrected average is:",
      r"$\frac{600 + 3}{30} = 20.1$."),
]

if __name__ == "__main__":
    subs = [
        stat_part1.build_mean(),
        stat_part2.build_median_mode(),
        stat_part3.build_grouped(),
        stat_part3.build_dispersion(),
        stat_part3.build_series(),
    ]
    apply_topic("statistics", subs, PYQ)
