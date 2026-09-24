"""Phase-2 deep content for quant/hcf-lcm. Run: py -3 hcf-lcm.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from hl_basics_methods import build_basics, build_methods
from hl_word_remainder import build_word, build_remainder


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Greatest number dividing with same/known remainders (HCF of differences)", "very common",
      "'Find the greatest number which divides x, y, z leaving remainders a, b, c' (remainders equal or different).",
      "Subtract each remainder from its number and take the HCF of the results — the divisor divides every (number − remainder) exactly. If the remainders are not even mentioned, take the HCF of the pairwise differences of the numbers instead.",
      "hl-word-problems",
      "Find the greatest number which divides 82, 150 and 233 leaving remainders 4, 7 and 12 respectively.",
      "Subtract: 78, 143, 221. HCF = 13 (each is a multiple of 13)."),
    P("Least number leaving the same remainder (LCM + r)", "very common",
      "'Find the least number which when divided by a, b, c leaves remainder r in each case.'",
      "Take the LCM of the divisors and add r. With an extra condition (n-digit bound, or divisible by p), write N = LCM·k + r and fit the condition by testing k = 1, 2, 3, …",
      "hl-word-problems",
      "Find the least number which when divided by 8, 12, 15 and 20 leaves remainder 4 in each case.",
      "LCM(8, 12, 15, 20) = 120, so the answer is 120 + 4 = 124."),
    P("Remainder is (divisor − c) each time (LCM − c)", "common",
      "The remainders look different, but each is a fixed amount less than its divisor — e.g. remainders 2, 3, 4 with divisors 3, 4, 5.",
      "Check that divisor − remainder is the same number c in every case. Then N + c is divisible by all divisors, so the least N is LCM − c (and other values are LCM·k − c).",
      "hl-word-problems",
      "Find the least number which when divided by 6, 9 and 12 leaves remainders 5, 8 and 11 respectively.",
      "Each remainder is 1 less than its divisor: N = LCM − 1 = 36 − 1 = 35."),
    P("Ratio + HCF/LCM → find the numbers", "very common",
      "'Two numbers are in ratio m : n and their HCF (or LCM) is …' — then sum, difference, product or LCM is asked.",
      "Cancel the ratio to co-prime parts m, n. Numbers are h·m and h·n where h is the HCF. From the LCM: h = LCM/(m·n). Then compute whatever is asked — sum = h(m + n), difference = h(n − m), LCM = h·m·n.",
      "hl-basics",
      "Two numbers are in the ratio 5 : 7 and their LCM is 140. Find the numbers.",
      "h = 140/(5 × 7) = 4 → numbers 20 and 28."),
    P("Product / HCF / LCM / one-number relation", "common",
      "Two of {product, HCF, LCM, one number} are given; find the fourth, or 'how many pairs are possible'.",
      "Use HCF × LCM = product (two numbers only). For pair counts, split product ÷ HCF² (or LCM ÷ HCF) into co-prime factor pairs, always including the pair (1, M).",
      "hl-basics",
      "The product of two numbers is 2160 and their HCF is 12. Find their LCM.",
      "LCM = 2160/12 = 180."),
    P("Bells / lights / runners together again", "common",
      "Events repeating at fixed intervals start together; asked when they next coincide, or how many times inside a time window.",
      "Convert all intervals to one unit, take the LCM — that is the coincidence gap. Add it to the start time for 'when next'; divide the window by it for 'how many times' (add 1 only if the start itself counts).",
      "hl-word-problems",
      "Three bells toll at intervals of 9, 12 and 15 minutes, together at 8 a.m. When do they next toll together?",
      "LCM = 180 minutes = 3 hours → 11 a.m."),
    P("Largest tile / rod / measure / group size (HCF)", "common",
      "Paving with the largest square tiles, cutting equal planks of greatest length, the biggest vessel filling containers, biggest equal groups.",
      "Convert all measurements to the same unit and take the HCF. Then count: tiles = (L × B)/side², pieces = total length ÷ HCF, groups = count ÷ HCF.",
      "hl-word-problems",
      "What is the largest vessel that can fill 144 L, 180 L and 240 L containers exactly?",
      "HCF(144, 180, 240) = 12 litres."),
    P("Greatest / least n-digit number with LCM or remainder conditions", "common",
      "'Find the greatest four-digit number divisible by …' / 'least five-digit number which divided by … leaves remainder …'.",
      "Take the LCM first. Least: step up from 10…0 to the next multiple (fit N = LCM·k + r into the range if a remainder is given). Greatest: reduce 99…9 by its remainder.",
      "hl-remainder-cases",
      "Find the least five-digit number exactly divisible by 32, 36, 40, 45 and 48.",
      "LCM = 1440; 10000 ÷ 1440 leaves 1360 → add 80 → 10080."),
    P("HCF / LCM of fractions or decimals", "occasional",
      "A list like 2/3, 8/9, 10/27, or decimals like 0.54, 1.8, 7.2.",
      "Fractions: HCF = (HCF of numerators)/(LCM of denominators); LCM is the mirror image. Decimals: multiply everything by the same power of 10 to clear the point, solve as integers, then put the point back.",
      "hl-methods",
      "Find the HCF of 0.54, 1.8 and 7.2.",
      "As 54, 180, 720 the HCF is 18 → answer 0.18."),
]

if __name__ == "__main__":
    subs = [build_basics(), build_methods(), build_word(), build_remainder()]
    apply_topic("hcf-lcm", subs, PYQ)
