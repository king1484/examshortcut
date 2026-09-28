"""Phase-2 deep content build for quant/data-interpretation. Run: py -3 data-interpretation.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
import di_part1
import di_part2


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


T = di_part1.cars_table()
ST = di_part1.sales_table()
PT = di_part1.budget_pie()
WT = di_part2.week_table()
DT = di_part2.dept_table()
RT = di_part2.rev_table()
IT = di_part2.ie_table()

PYQ = [
    P("Totals and differences from a table", "very common",
      "Sum a row/column, or find the gap between two cells, two years or two companies. The most basic DI ask, and the first question of most table sets.",
      "Add in friendly pairs and keep subtotals in the margin; for a difference of totals, subtract the totals once instead of cell by cell. Check the unit (thousand, lakh) before choosing the option.",
      "di-table",
      T + "\n\nThe total production of company R over the five years is:",
      "$150 + 145 + 160 + 170 + 175 = 800$ thousand."),
    P("Percentage change between periods", "very common",
      "'The percent increase from year A to year B', often with 'approximately' in the question, or 'by what percent is X more than Y'.",
      r"$\frac{\text{new}-\text{old}}{\text{old}}\times100$ with the base as the earlier (or 'than') value; keep the fraction until the end and match the nearest option.",
      "di-percent",
      ST + "\n\nThe percentage increase in sales from 2022 to 2023 is:",
      r"$\frac{320-250}{250}\times100 = 28\%$."),
    P("Pie-chart sector values", "very common",
      "Sectors printed as degrees or percentages with a stated total; a value, a share or an angle asked.",
      r"Value $= \frac{\theta}{360}\times$ total; angle $= \% \times 3.6^\circ$. Find the worth of $1^\circ$ once and reuse it; add angles before converting when two sectors are asked together.",
      "di-pie",
      PT + "\n\nThe amount spent on Rent is:",
      r"$1^\circ = \frac{72000}{360} = ₹200$, so Rent $= 72 \times 200 = ₹14{,}400$."),
    P("Ratios and shares", "common",
      "'Ratio of X to Y in year Z', 'X is what percent of Y', or the share of two heads of a total taken together.",
      "Reduce the ratio fraction directly (cancel the HCF) and keep the order asked; for shares, add the parts first, then divide by the total once.",
      "di-percent",
      ST + "\n\nThe sales in 2020 are what percent of the sales in 2023?",
      r"$\frac{200}{320} \times 100 = 62.5\%$."),
    P("Averages and weighted averages", "common",
      "Row/column averages over the years, or a table of group sizes with group averages to combine.",
      r"Simple mean of the cells for one row/column; for groups, weight by size: $\frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1+n_2}$. The plain average of the group means is the planted trap.",
      "di-average",
      DT + "\n\nThe average salary of departments A and B together is:",
      r"$\frac{40 \times 25000 + 30 \times 32000}{70} = ₹28{,}000$, not the plain $28{,}500$."),
    P("Successive growth / reverse growth", "common",
      "Multi-year growth rates with the final (or initial) value given; sometimes a rise followed by a fall.",
      r"Multiply factors $(1 \pm \frac{a}{100})$ to move forward; divide the final value by the factor to move back. Never add percentages across years.",
      "di-growth",
      "A price rises 10% and then another 10%. The net increase is:",
      r"$1.1 \times 1.1 = 1.21$ → net $+21\%$, not 20%."),
    P("Maximum / minimum year, and counting years", "common",
      "'In which year was the difference/growth the least?' or 'in how many years was X above its average'.",
      "Compute the small derived number (gap, total, rate) for each year and list it in the margin, then pick. For counting, fix the benchmark once; values equal to it do not count for 'more than'.",
      "di-table",
      T + "\n\nIn which year was the difference between the production of R and S the least?",
      "Gaps: 70, 50, 60, 60, 55 — least is 50 in 2020."),
    P("Two pie charts with different totals", "occasional",
      "Two pies (two years, two firms), each with its own total; a change or ratio of one item asked.",
      "Convert the item to a value in each pie using its own total, then compare values. Shares alone mislead: a falling share on a bigger pie can still be a bigger amount.",
      "di-pie",
      "Exports: 2022 total ₹400 cr with Asia 30%; 2023 total ₹500 cr with Asia 27%. The change in exports to Asia is:",
      r"$120 \to ₹135$ cr: a rise of ₹15 crore (12.5%) even though the share fell."),
]

if __name__ == "__main__":
    subs = [
        di_part1.build_table(),
        di_part1.build_percent(),
        di_part1.build_pie(),
        di_part2.build_average(),
        di_part2.build_growth(),
    ]
    apply_topic("data-interpretation", subs, PYQ)
