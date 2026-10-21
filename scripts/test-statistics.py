"""Independently calculate the answers in the statistics question bank.

Run with Python's standard library: python scripts/test-statistics.py
Keep calculations here separate from the content's worked solutions.
"""
import json
import math
from pathlib import Path
import re
import statistics as stats
import unittest
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[1]
TOPIC = json.loads((ROOT / 'content/core/topics/quant/statistics.json').read_text(encoding='utf-8'))
QUESTIONS = {q['id']: q for q in TOPIC['solvedExamples'] + TOPIC['practice']}


def numeric_option(text):
    text = text.replace('−', '-').strip('$ ').removesuffix(' kg').strip('$ ')
    text = re.sub(r'^\$?f\s*=\s*', '', text).strip('$ ')
    # Support only the numeric TeX forms used by this bank; never evaluate code.
    mixed = re.fullmatch(r'(-?\d+)\\tfrac\{(\d+)\}\{(\d+)\}', text)
    if mixed:
        whole, numerator, denominator = map(int, mixed.groups())
        return whole + F(numerator, denominator)
    fraction = re.fullmatch(r'\\(?:d?frac|tfrac)\{(-?\d+)\}\{(\d+)\}', text)
    if fraction:
        return F(*map(int, fraction.groups()))
    root = re.fullmatch(r'(\d*)\\sqrt\{(.+)\}', text)
    if root:
        return int(root[1] or 1) * math.sqrt(numeric_option(root[2]))
    return F(text)


def grouped_median(lower, frequencies, width):
    halfway = F(sum(frequencies), 2)
    cumulative = 0
    for low, frequency in zip(lower, frequencies):
        if cumulative + frequency >= halfway:
            return low + (halfway - cumulative) * width / frequency
        cumulative += frequency
    raise AssertionError('No median class')


def grouped_mean(midpoints, frequencies):
    return F(sum(x * f for x, f in zip(midpoints, frequencies)), sum(frequencies))


# Calculations use the observations and relations in each question, not the key.
EXPECTED = {
    'stat-s01': F(30 * 62 + 20 * 58, 50),
    'stat-s02': F(45 + 2 * 27, 3),
    'stat-s03': stats.median([8, 3, 11, 6, 14, 5]),
    'stat-s04': F(sum(x*x for x in range(1, 11)), 10),
    'stat-s05': abs(3) * 7,
    'stat-q01': 5 * 27 - sum([23, 25, 28, 26]),
    'stat-q02': stats.median([12, 5, 9, 7, 15]),
    'stat-q03': stats.mode([2, 3, 3, 5, 3, 7, 2, 3]),
    'stat-q04': F(sum(range(1, 11)), 10),
    'stat-q05': max([14, 7, 22, 9, 31, 18]) - min([14, 7, 22, 9, 31, 18]),
    'stat-q06': 25 * F('35.5') - 24 * 35,
    'stat-q07': 3 * 32 - 2 * 30,
    'stat-q08': grouped_median([0, 10, 20, 30, 40], [4, 6, 10, 8, 2], 10),
    'stat-q09': max([12, 14, 16, 18, 20]),
    'stat-q10': stats.pstdev([2, 4, 6, 8, 10]),
    'stat-q11': F(30 * 20 - 21 + 24, 30),
    'stat-q12': 9 * 50 - 8 * 45,
    'stat-q13': F(sum(x**3 for x in range(1, 7)), 6),
    'stat-q14': 30 + F(12 - 8, 2 * 12 - 8 - 6) * 10,
    'stat-q15': 3 * 10 + 3 * 15 - 5 * 12,
    'stat-mean-p03': F(30 * 62 + 20 * 58, 50),
    'stat-mean-p07': F(24 * 4 - 52, F('24.5') - 24),
    'stat-mean-p08': F(8 * 20 - 2 * F('15.5') - 3 * F(64, 3) - 4 - 5, 3) + 5,
    'stat-mean-p09': 6 * 49 + 6 * 52 - 11 * 50,
    'stat-mean-p10': F(40 * 72 - 58 + 85, 40),
    # Integer runs r must satisfy (110+r)/6 < 24, hence maximum r = 33.
    'stat-mean-p11': max(r for r in range(100) if F(5 * 22 + r, 6) < 24),
    'stat-median-mode-p01': stats.median([8, 3, 11, 6, 14, 5]),
    'stat-median-mode-p04': 3 * 32 - 2 * 30,
    'stat-median-mode-p06': 2 * 15 + 1,
    'stat-median-mode-p07': next(x for x in [6, 7, 9, 8] if stats.median([4, 10, 6, 2, 12, 8, x]) == 7),
    'stat-median-mode-p08': F(22 + 2 * 16, 3),
    'stat-median-mode-p09': 9 + 3,
    'stat-median-mode-p10': 3 * 25 - 2 * 29,
    'stat-median-mode-p11': stats.mode([4, 6, 6, 8, 9, 9, 9, 11, 6, 9]),
    'stat-grouped-p03': next(x for x in range(1, 100) if grouped_median([0, 20, 40, 60], [8, x, 10, 6], 20) == 38),
    'stat-grouped-p04': grouped_mean([5, 15, 25], [5, 8, 7]),
    'stat-grouped-p05': grouped_median([10, 20, 30], [6, 10, 4], 10),
    'stat-grouped-p06': 20 + F(14 - 9, 2 * 14 - 9 - 4) * 10,
    'stat-grouped-p07': grouped_median([0, 10, 20, 30, 40], [2, 5, 6, 4, 3], 10),
    'stat-grouped-p08': grouped_mean([5, 15, 25], [4, 6, 10]),
    'stat-grouped-p09': next(f for f in range(1, 100) if grouped_median([0, 10, 20], [4, f, 6], 10) == 16),
    'stat-grouped-p10': grouped_mean([5, 15, 25], [3, 5, 2]),
    'stat-dispersion-p03': stats.pstdev(range(1, 6)),
    'stat-dispersion-p04': stats.pstdev([9, 5]),
    'stat-dispersion-p07': F(9, 3**2),
    'stat-dispersion-p08': stats.pstdev(range(1, 11)),
    'stat-dispersion-p09': stats.pvariance([2, 4, 6, 8, 10]),
    'stat-dispersion-p10': math.sqrt((100 * (F('5.9')**2 + 40**2) - 50**2 + 60**2) / 100 - F(4010, 100)**2),
    'stat-series-sums-p05': next(n for n in range(1, 30) if sum(k**3 for k in range(1, n+1)) == 441),
    'stat-series-sums-p06': stats.mean(range(1, 18, 2)),
    'stat-series-sums-p07': stats.mean(range(2, 23, 2)),
    'stat-series-sums-p08': next(n for n in range(1, 30) if F(sum(k*k for k in range(1, n+1)), n) == F('38.5')),
    'stat-series-sums-p09': max(range(27, 46, 3)),
    'stat-series-sums-p10': stats.mean(range(1, 51)),
    'stat-series-sums-p11': next(n for n in range(1, 30) if sum(k**3 for k in range(1, n+1)) == 3025),
    'stat-median-mode-p13': stats.median([4, 8, 11, 13, 17, 19]),
    'stat-grouped-p11': grouped_median([F('9.5'), F('19.5'), F('29.5')], [4, 8, 8], 10),
    'stat-dispersion-p11': stats.variance([2, 4, 6]),
    'stat-dispersion-p12': abs(-2) * 4,
    'stat-dispersion-p13': stats.pvariance([2, 4, 6]),
}
TEXT_EXPECTED = {
    'stat-dispersion-p05': 'B is more consistent' if F(6, 80) < F(5, 50) else 'A is more consistent',
    'stat-median-mode-p12': ' and '.join(map(str, sorted(stats.multimode([2, 2, 5, 5, 9])))),
}


class StatisticsAnswers(unittest.TestCase):
    def test_entire_bank_has_calculations(self):
        self.assertEqual(set(QUESTIONS), set(EXPECTED) | set(TEXT_EXPECTED))

    def test_exactly_one_option_matches_each_calculation(self):
        for qid, expected in EXPECTED.items():
            with self.subTest(question=qid):
                q = QUESTIONS[qid]
                matches = [i for i, option in enumerate(q['options']) if math.isclose(float(numeric_option(option)), float(expected), rel_tol=1e-10, abs_tol=1e-10)]
                self.assertEqual(matches, [q['answer']], f"Computed {expected}; options: {q['options']}")
        for qid, expected in TEXT_EXPECTED.items():
            with self.subTest(question=qid):
                q = QUESTIONS[qid]
                self.assertEqual([i for i, option in enumerate(q['options']) if option == expected], [q['answer']])


if __name__ == '__main__':
    unittest.main()
