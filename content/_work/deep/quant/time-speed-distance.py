"""Phase-2 deep content for quant/time-speed-distance.json — driver.

Upserts notes/patterns/practice per subtopic and rewrites pyqPatterns (enriched).
Idempotent: re-running never duplicates or drops existing questions.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from fractions import Fraction as F

from tsd_basics_rel import build_basics, build_rel
from tsd_trains_boats import build_trains, build_boats
from tsd_races import build_races

# ---- verified examples for the enriched pyqPatterns ----
assert F(90, 1) * F(5, 18) == 25 and F(150, 25) == 6
assert F(180 + 20, 20) * 0 == 0 and F(180) / F(15) == 12 and 15 * 30 - 180 == 270
assert F(15 - 10, 2) == F(5, 2)
assert F(100, 20 + 30) == 2
assert F(2 * 40 * 60, 100) == 48
assert F(4, 3) * F(1, 3) * 60 * 0 + (F(3) / F(4)) ** -1 == F(4, 3)
assert F(200, 180) == F(10, 9)
assert F(54 * 5, 18) == 15

PYQ = [
    {
        "pattern": "Train crossing a pole or a man",
        "frequency": "very common",
        "howToSpot": "Length of train given, time to pass a point asked (or vice versa).",
        "approach": "$t = \\frac{L}{S}$ with S in m/s — convert with $\\frac{5}{18}$ first. A pole, man or signal is a point: only the train's own length passes it.",
        "subtopic": "tsd-trains",
        "example": {
            "q": "A 150 m long train running at 90 km/h crosses a pole in:",
            "solution": "$S = 90 \\times \\frac{5}{18} = 25$ m/s → $\\frac{150}{25} = 6$ seconds.",
        },
    },
    {
        "pattern": "Train crossing a platform, bridge or another train",
        "frequency": "very common",
        "howToSpot": "Two lengths involved; time for the train to completely cross.",
        "approach": "$t = \\frac{L + P}{S}$ (platform) or $\\frac{L_1 + L_2}{S_1 \\pm S_2}$ (train). Pole + platform times together solve for both $L$ and $S$.",
        "subtopic": "tsd-trains",
        "example": {
            "q": "A train running at 54 km/h crosses a pole in 12 s and a platform in 30 s. The platform's length is:",
            "solution": "$S = 15$ m/s, $L = 180$ m → platform $= 15 \\times 30 - 180 = 270$ m.",
        },
    },
    {
        "pattern": "Boats & streams",
        "frequency": "very common",
        "howToSpot": "Downstream/upstream times, boat or stream speed asked; sometimes two double trips.",
        "approach": "$u = b + s$, $v = b - s$; recover with $b = \\frac{u+v}{2}$, $s = \\frac{u-v}{2}$. Two trip equations are linear in $\\frac1u$ and $\\frac1v$.",
        "subtopic": "tsd-boats",
        "example": {
            "q": "A boat goes downstream at 15 km/h and upstream at 10 km/h. The speed of the stream is:",
            "solution": "$s = \\frac{15 - 10}{2} = 2.5$ km/h (boat: 12.5 km/h).",
        },
    },
    {
        "pattern": "Relative speed — meeting or overtaking",
        "frequency": "common",
        "howToSpot": "Two vehicles move towards or along each other; find meeting time or crossing time.",
        "approach": "Opposite: add the speeds; same direction: subtract. Distance = the gap (or the sum of both lengths for trains).",
        "subtopic": "tsd-relative",
        "example": {
            "q": "Two towns 100 km apart send buses towards each other at 20 km/h and 30 km/h. They meet after:",
            "solution": "$\\frac{100}{20 + 30} = 2$ hours.",
        },
    },
    {
        "pattern": "Average speed for legs of a journey",
        "frequency": "common",
        "howToSpot": "Out-and-back or multi-leg trips; the trap is averaging the speeds.",
        "approach": "Total distance ÷ total time; equal legs ⇒ $\\frac{2ab}{a+b}$; three equal legs ⇒ $3 \\div (\\frac1a+\\frac1b+\\frac1c)$.",
        "subtopic": "tsd-basics",
        "example": {
            "q": "A car goes out at 40 km/h and returns the same road at 60 km/h. The average speed is:",
            "solution": "$\\frac{2 \\times 40 \\times 60}{40 + 60} = 48$ km/h — not 50.",
        },
    },
    {
        "pattern": "Speed change with early/late arrival",
        "frequency": "common",
        "howToSpot": "Walking slower/faster makes the person late/early by known minutes.",
        "approach": "Same distance both ways: $\\frac{d}{s_1} - \\frac{d}{s_2} = $ delay in hours; a speed fraction $f$ multiplies the time by $\\frac1f$.",
        "subtopic": "tsd-basics",
        "example": {
            "q": "Walking at $\\frac34$ of his usual speed a man is 20 minutes late. His usual time is:",
            "solution": "New time $= \\frac43 t$ → late by $\\frac{t}{3} = 20$ → $t = 60$ minutes.",
        },
    },
    {
        "pattern": "Races and starts",
        "frequency": "common",
        "howToSpot": "'A beats B by x m / t s', or start handicaps; find speeds or ratios.",
        "approach": "Distances covered in equal time are in the speed ratio: beats by $x$ m ⇒ $D : (D-x)$; chain margins multiplicatively.",
        "subtopic": "tsd-races",
        "example": {
            "q": "In a 200 m race A beats B by 20 m. The ratio of their speeds is:",
            "solution": "$S_A : S_B = 200 : 180 = 10 : 9$.",
        },
    },
    {
        "pattern": "Unit conversion embedded in other questions",
        "frequency": "common",
        "howToSpot": "Any train/m/s question quietly needs km/h ⇄ m/s.",
        "approach": "$\\frac{5}{18}$ and $\\frac{18}{5}$ — know the 36/54/72/90 table by heart.",
        "subtopic": "tsd-basics",
        "example": {
            "q": "A 120 m train crosses a pole in 8 seconds. Its speed in km/h is:",
            "solution": "$\\frac{120}{8} = 15$ m/s $= 54$ km/h.",
        },
    },
]

apply_topic("time-speed-distance", [build_basics(), build_rel(), build_trains(), build_boats(), build_races()], PYQ)
print("OK time-speed-distance")
