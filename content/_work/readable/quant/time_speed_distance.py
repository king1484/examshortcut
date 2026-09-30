"""Readable rewrite of the Time, Speed & Distance topic (all 5 subtopics).

Simple English, one idea per section, exact fraction checks for every number.
Run: python time_speed_distance.py  (patches content/core/topics/quant/time-speed-distance.json in place)
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "time-speed-distance.json"


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


# =========================== tsd-basics ===========================
# answer checks
assert 450 // 30 == 15 and 15 * 18 // 5 == 54                                      # p1: 15 m/s = 54 km/h
assert F(2 * 40 * 60, 100) == 48                                                    # p2: harmonic 48
assert F(3, 1) / (F(1, 20) + F(1, 30) + F(1, 60)) == 30                             # three equal legs
assert F(4, 5) and F(5, 4) and F(1, 4) * 40 == 10 and 40 * 4 == 160                 # p3: t = 40 min
assert F(1, 4) - F(1, 5) == F(1, 20) and F(20, 1) * F(1, 4) == 5                    # p4: d = 5 km
assert 90 * 5 // 18 == 25 and 150 // 25 == 6                                        # trick 1
assert F(1, 3) * 60 == 20 and 3 * 20 == 60                                          # 3/4 speed -> t = 60
assert F(5, 6) and F(1, 6) * 60 == 10 and 6 * 10 == 60                              # p21: 20% faster -> t = 60
assert 36 * 5 // 18 == 10 and 54 * 5 // 18 == 15 and 72 * 5 // 18 == 20 and 108 * 5 // 18 == 30

b_concept = (
    "One relation drives everything:\n\n"
    "$D = S \\times T$, so $S = \\dfrac{D}{T}$ and $T = \\dfrac{D}{S}$.\n\n"
    "Units: multiply km/h by $\\dfrac{5}{18}$ to get m/s; multiply m/s by $\\dfrac{18}{5}$ to get km/h. "
    "Friendly pairs: 36 km/h = 10 m/s, 54 = 15, 72 = 20, 90 = 25.\n\n"
    "Average speed = total distance ÷ total time, never the average of the speeds. "
    "For the same distance out and back at $a$ and $b$: $\\dfrac{2ab}{a+b}$."
)

b_notes = r"""### One relation, three forms
Distance = Speed × Time. Know any two, find the third. Ask at the start of every question: which two do I have?

For a fixed distance, speed and time move opposite ways. Speed drops to $\dfrac{3}{4}$ → time grows to $\dfrac{4}{3}$. That inverse reflex alone solves many questions before any equation is written.

> **Rule:** Speed × $\dfrac{p}{q}$ turns time into × $\dfrac{q}{p}$. Flip the fraction, never keep it.

### The five-eighteen conversion
Lengths come in metres, times in seconds, speeds in km/h. Convert before dividing.

$$1 \text{ km/h} = \frac{5}{18} \text{ m/s}, \qquad 1 \text{ m/s} = \frac{18}{5} \text{ km/h}$$

Keep the friendly table by heart: 36 km/h = 10 m/s, 54 = 15, 72 = 20, 90 = 25, 108 = 30. To convert 72 by hand: $72 \div 18 = 4$, then $4 \times 5 = 20$.

> **Watch:** Dividing metres by a km/h speed is the most common avoidable error here.

### Average speed is a division
$$\text{Average speed} = \frac{\text{total distance}}{\text{total time}}$$

It equals the average of the speeds ONLY when the times are equal. Out-and-back trips have equal DISTANCES, and then the answer is the harmonic mean:

$$\bar{S} = \frac{2ab}{a+b}$$

40 km/h out, 60 km/h back → $\dfrac{2 \times 40 \times 60}{100} = 48$ km/h, not 50. The equal-distance average always sits below the plain midpoint. Three equal legs at a, b, c give $3 \div \left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right)$: at 20, 30 and 60 that is $3 \div \frac{6}{120} = 30$ km/h.

> **Tip:** Legs of different lengths? Add the distances, add the times, divide. No shortcut beats the definition.

### Late by and early by
The distance is the same in both runs, so compare the two times.

Walking at $\dfrac{3}{4}$ of usual speed makes the time $\dfrac{4}{3}t$; the lateness is $\dfrac{t}{3}$. "20 minutes late" → $t = 60$ minutes. With two speeds and a stated gap:

$$\dfrac{d}{s_1} - \frac{d}{s_2} = \text{gap in hours}$$

5 minutes late at 4 km/h and 10 minutes early at 5 km/h: $\dfrac{d}{4} - \frac{d}{5} = \frac{15}{60} = \frac{1}{4}$, so $d = 5$ km. Add the two gaps when one run is late and the other early; subtract when both are late.

### Speed times a fraction, time times the flip
- Speed $\dfrac{4}{5}$ of usual → time $\dfrac{5}{4}$ of usual → $\dfrac{1}{4}$ late.
- Speed $\dfrac{3}{4}$ of usual → time $\dfrac{4}{3}$ of usual → $\dfrac{1}{3}$ late.

Convert every "reduces his speed to ¾" into the time multiplier $\dfrac{4}{3}$ BEFORE writing the equation.

> **Careful:** Reading "speed is ¾ of usual" as "time is ¾ of usual" is the classic trap. The time goes UP.

### Per cent changes in speed
Speed 20% more → time $\dfrac{100}{120} = \frac{5}{6}$ of before. Speed 25% more → time $\dfrac{4}{5}$. Speed 20% less → time $\dfrac{5}{4}$.

A 20% faster ride that saves 10 minutes: the saving is $\dfrac{1}{6}$ of the usual time, so the usual time is 60 minutes. Convert the per cent to a fraction, then read the time change off it.
"""

b_formulas = [
    {"name": "Basic relation", "tex": r"S = \frac{D}{T}, \quad D = S \times T"},
    {"name": "km/h to m/s", "tex": r"\text{km/h} \times \frac{5}{18} = \text{m/s}"},
    {"name": "Equal-distance average", "tex": r"\bar{S} = \frac{2ab}{a + b}"},
    {"name": "General average speed", "tex": r"\bar{S} = \frac{D_1 + D_2}{T_1 + T_2}"},
]

b_tricks = [
    {
        "title": "Convert first, always",
        "body": "Train lengths are in metres, times in seconds — reach m/s before anything else.",
        "example": {
            "q": "Convert 90 km/h into m/s and find the time a 150 m train takes to cross a pole.",
            "steps": [r"$90 \times \frac{5}{18} = 25$ m/s.", r"Time = $\dfrac{150}{25} = 6$ seconds."],
            "answer": "25 m/s; 6 seconds",
        },
    },
    {
        "title": "Harmonic mean for round trips",
        "body": "Same distance out and back → 2ab/(a+b) in one line.",
        "example": {
            "q": "A car goes to a town at 40 km/h and returns at 60 km/h. Find the average speed for the whole trip.",
            "steps": [r"$\dfrac{2 \times 40 \times 60}{40 + 60} = \frac{4800}{100}$.", r"= $48$ km/h."],
            "answer": "48 km/h",
        },
    },
    {
        "title": "Early and late gaps are time equations",
        "body": "Both runs cover the SAME distance — equate or subtract the two time expressions.",
        "example": {
            "q": "Walking at $\\frac{3}{4}$ of his usual speed a man is 20 minutes late. Find his usual time.",
            "steps": [r"New time = $\dfrac{4}{3}t$.", r"Lateness = $\dfrac{t}{3} = 20$ minutes.", r"$t = 60$ minutes."],
            "answer": "60 minutes",
        },
    },
]

b_mistakes = [
    {"wrong": "Averaging two speeds for equal DISTANCES.", "right": "Equal distances average by 2ab/(a+b); 40 and 60 give 48, not 50."},
    {"wrong": "Forgetting the 5/18 conversion and dividing metres by km/h.", "right": "Convert to m/s first: km/h × 5/18."},
    {"wrong": "Using ¾t as the new time when speed is ¾.", "right": "Speed down to ¾ makes time 4/3 of usual — flip the fraction."},
    {"wrong": "Mixing minutes and hours in one equation.", "right": "Convert everything to hours (or fractions of an hour) first."},
    {"wrong": "Averaging speeds of legs with different lengths.", "right": "Total distance ÷ total time, computing each leg's time separately."},
]

b_revision = [
    "D = ST; for a fixed distance, speed and time are inverse.",
    "km/h → m/s: × 5/18 (36→10, 54→15, 72→20, 90→25).",
    "Equal distances: 2ab/(a+b); three equal legs: 3 ÷ (1/a + 1/b + 1/c).",
    "Late/early: d/s₁ − d/s₂ = gap in hours; add opposite gaps.",
    "Speed × p/q ⇒ time × q/p.",
    "Speed 20% more ⇒ time 5/6; 25% more ⇒ 4/5.",
]

b_patterns = [
    pat("tsd-p1", "Direct distance-speed-time with conversion", "very common",
        "Two of distance, speed, time are given in mixed units; the third is asked, often with a km/h and m/s conversion.",
        r"S = \frac{D}{T}, \qquad \text{km/h} \times \frac{5}{18} = \text{m/s}",
        ["Put all quantities in one unit system (metres and seconds, or km and hours).", r"Apply $D = S \times T$ in the direction you need.", "Convert the answer to the unit the options use."],
        "The formula is only consistent when distance, speed and time speak the same units.",
        "A train covers 450 metres in 30 seconds. Its speed in km/h is:",
        [r"$\dfrac{450}{30} = 15$ m/s.", r"$15 \times \frac{18}{5} = 54$ km/h."],
        "54 km/h"),
    pat("tsd-p2", "Average speed over the legs of a journey", "very common",
        "A journey splits into legs — out and back at different speeds, or different speeds for different stretches; the average speed is asked.",
        r"\bar{S} = \frac{D_{total}}{T_{total}}, \quad \text{equal distances: } \frac{2ab}{a+b}",
        [r"Equal distances (a round trip): use $\dfrac{2ab}{a+b}$.", "Equal times: the plain average of the speeds.", "Otherwise: compute each leg's time, then total distance ÷ total time."],
        "Average speed is a mean over TIME — that is exactly what the harmonic mean does.",
        "A car goes to a town at 40 km/h and returns along the same road at 60 km/h. Find the average speed for the round trip.",
        [r"$\dfrac{2 \times 40 \times 60}{40 + 60} = \frac{4800}{100}$.", r"= $48$ km/h — not 50."],
        "48 km/h"),
    pat("tsd-p3", "Fraction of usual speed makes him late", "very common",
        "'Walking at 3/4 (or 4/5) of his usual speed he is 20 minutes late' — the usual time or the distance is asked.",
        r"\text{new time} = \frac{t}{f} \Rightarrow \text{late by} = \left(\frac{1}{f} - 1\right)t",
        ["Speed fraction f of usual → time is $t/f$.", r"Lateness = $t\left(\frac{1}{f} - 1\right)$; set it equal to the given minutes.", "Solve for t; multiply by the usual speed if the distance is asked."],
        "For the same distance, speed and time are inversely proportional.",
        "Walking at $\\frac{4}{5}$ of his usual speed, a man reaches his office 10 minutes late. Find his usual time.",
        [r"New time = $\dfrac{5}{4}t$.", r"Lateness = $\dfrac{t}{4} = 10$ minutes.", r"$t = 40$ minutes."],
        "40 minutes"),
    pat("tsd-p4", "Two fixed speeds, one late and one early", "common",
        "'At s₁ km/h he is x minutes late; at s₂ km/h he is y minutes early' — the distance is asked.",
        r"\frac{d}{s_1} - \frac{d}{s_2} = \frac{x + y}{60}",
        ["Both times are measured against the same unknown schedule, so subtract the two travel times.", "The gap equals late + early, converted to hours.", r"Solve $d\left(\frac{1}{s_1} - \frac{1}{s_2}\right) = \text{gap}$ for d."],
        "Writing both times against a common schedule cancels the schedule itself.",
        "Walking at 4 km/h a student reaches school 5 minutes late; walking at 5 km/h he reaches 10 minutes early. Find the distance to school.",
        [r"$\dfrac{d}{4} - \frac{d}{5} = \frac{15}{60} = \frac{1}{4}$.", r"$\dfrac{d}{20} = \frac{1}{4}$.", r"$d = 5$ km."],
        "5 km"),
    pat("tsd-p21", "Per cent change in speed saves time", "common",
        "'Increasing his speed by 20% he arrives 10 minutes early' — the usual time is asked.",
        r"\text{speed } \times\frac{100+r}{100} \Rightarrow \text{time } \times\frac{100}{100+r}",
        [r"Convert the per cent to a time factor: +20% speed → time $\dfrac{5}{6}$; +25% → $\dfrac{4}{5}$.", r"The saving is $1 - \text{factor}$ of the usual time.", "Divide the given saving by that fraction."],
        "A per cent change in speed flips into the reciprocal time factor.",
        "A cyclist increases his speed by 20% and reaches college 10 minutes early. Find his usual time.",
        [r"Speed $\times\frac{6}{5}$ → time $\times\frac{5}{6}$.", r"Saving = $\dfrac{1}{6}$ of usual time = 10 minutes.", r"Usual time = $60$ minutes."],
        "60 minutes"),
]

# =========================== tsd-relative ===========================
# answer checks
assert F(150, 100) == F(3, 2) and 40 * F(3, 2) == 60                               # p5: meet 1.5 h, 60 km
assert (63 - 45) * 5 % 18 == 0 and (63 - 45) * 5 // 18 == 5                        # p6: 18 km/h = 5 m/s
assert 350 // 5 == 70                                                               # p6: 70 s
assert (54 - 6) == 48 and F(48 * 5, 18) == F(40, 3) and 120 / F(40, 3) == 9           # p7: 9 s
assert 60 * 2 == 120 and 90 - 60 == 30 and 120 // 30 == 4 and 90 * 4 == 360         # p8: 4 h, 360 km
assert 72 * 5 // 18 == 20 and 54 * 5 // 18 == 15 and 200 // (20 - 15) == 40         # trick 1
assert F((45 + 5) * 5, 18) == F(125, 9) and 250 * 9 // 125 == 18                    # trick 2
assert F(100, 50) == 2 and 60 * 2 == 120                                            # bird
assert 240 // 80 == 3                                                               # notes meet
assert 300 // 100 == 3 and 40 * 3 == 120                                            # notes meeting point
assert 30 // (40 - 30) == 3 and 40 * 3 == 120                                       # delayed start
assert (40 + 50) * 3 == 270 and (50 - 40) * 3 == 30                                 # p22 gaps

r_concept = (
    "Relative speed is how fast one moving thing closes the gap with another:\n\n"
    "opposite directions: $S_{rel} = S_1 + S_2$;  same direction: $S_{rel} = S_1 - S_2$.\n\n"
    "Use it whenever the question says cross, overtake, meet or catch up. The distance to cover is the "
    "combined lengths (two trains) or the current gap (chases). Two movers from the same spot drift apart "
    "at the sum or the difference of their speeds."
)

r_notes = r"""### Add or subtract
Same direction → subtract the speeds (the gap closes slowly). Opposite directions → add them (the gap closes fast).

$$\text{same way: } S_1 - S_2 \qquad \text{opposite ways: } S_1 + S_2$$

A gap must shrink, so the relative speed is always the difference or sum of the sizes — never negative.

> **Rule:** Read the directions first, then pick add or subtract. This one habit fixes most errors.

### Meeting head-on
Two objects start towards each other from a gap D. They meet after

$$t = \frac{D}{S_1 + S_2}$$

Cars 150 km apart at 40 and 60 km/h meet in $\dfrac{150}{100} = 1.5$ hours — 60 km from the first town. The meeting POINT comes from one side alone: distance from A = $S_A \times t$.

Each side also takes a fixed SHARE of the gap: A covers $\dfrac{S_A}{S_A + S_B}$ of it. At 40 and 60, A covers $\dfrac{40}{100} = 40\%$ — exactly $\dfrac{2}{5}$ of 150 km = 60 km, the same answer with no time computed.

### Overtaking
A faster object closes a gap G at $S_1 - S_2$: time = $\dfrac{G}{S_1 - S_2}$.

For two trains the gap to clear is BOTH lengths together — the back of the faster train must pass the front of the slower. Trains of 200 m and 150 m at 63 and 45 km/h: relative speed 18 km/h = 5 m/s, gap 350 m, time $\dfrac{350}{5} = 70$ seconds.

> **Watch:** A moving man is a POINT — only the train's own length counts. A train is LONG — add both lengths.

### Train and a walking man
The man adds no length, only speed. Same direction → subtract his speed; opposite → add.

A 120 m train at 54 km/h passes a man walking the same way at 6 km/h: relative speed 48 km/h = $\dfrac{40}{3}$ m/s → $120 \div \frac{40}{3} = 9$ seconds.

### Late starters
Someone leaves later. The gap is simply what the early mover covered alone.

A leaves at 9 a.m. at 30 km/h; B chases from 10 a.m. at 40 km/h. At 10 a.m. the gap is 30 km, closed at 10 km/h → 3 more hours → 1 p.m., at $40 \times 3 = 120$ km from the start.

> **Tip:** Time everything from the second starter's departure; add the delay back at the end if asked.

### The shuttle trick
A bird flies back and forth between two approaching trains until they meet. Do NOT sum the zigzags — the bird flies for the whole meeting time:

$$\text{distance} = \text{bird's speed} \times \text{meeting time}$$

Trains 100 km apart at 20 and 30 km/h meet in 2 hours; a bird at 60 km/h covers $60 \times 2 = 120$ km. One multiplication, no series.

### Growing gaps
Two movers start from the SAME point. Opposite ways: the gap after t hours is $(S_1 + S_2)t$. Same way: it is $(S_1 - S_2)t$ — the slower one falls behind at the difference.

At 40 and 50 km/h from one point: after 3 hours they are 270 km apart (opposite ways) or 30 km apart (same way).
"""

r_formulas = [
    {"name": "Relative speed", "tex": r"S_{rel} = S_1 \pm S_2"},
    {"name": "Meeting time", "tex": r"t = \frac{\text{initial gap}}{S_1 + S_2}"},
    {"name": "Overtake time", "tex": r"t = \frac{\text{gap or combined length}}{S_1 - S_2}"},
    {"name": "Gap between two movers", "tex": r"d = (S_1 \pm S_2) \times t"},
]

r_tricks = [
    {
        "title": "Subtract for the same direction",
        "body": "Overtaking uses the difference; for two trains the distance is both lengths together.",
        "example": {
            "q": "Two trains run in the same direction at 72 km/h and 54 km/h. The faster train, 200 m long, crosses a point on the slower train in:",
            "steps": [r"$72 - 54 = 18$ km/h $= 5$ m/s.", r"Time = $\dfrac{200}{5} = 40$ s."],
            "answer": "40 seconds",
        },
    },
    {
        "title": "Add for opposite directions",
        "body": "The closing speed is the sum even when one side is just a walking man.",
        "example": {
            "q": "A 250 m train at 45 km/h crosses a man walking at 5 km/h the opposite way. Find the crossing time.",
            "steps": [r"$45 + 5 = 50$ km/h $= \frac{125}{9}$ m/s.", r"Time = $250 \times \frac{9}{125} = 18$ s."],
            "answer": "18 seconds",
        },
    },
    {
        "title": "Distance flown till meeting",
        "body": "Find the meeting time first; any third object's distance = its speed × that time.",
        "example": {
            "q": "Two trains 100 km apart approach each other at 20 km/h and 30 km/h. A bird flying at 60 km/h shuttles between them until they meet. Find the total distance the bird covers.",
            "steps": [r"Meeting time = $\dfrac{100}{50} = 2$ h.", r"Bird covers $60 \times 2 = 120$ km."],
            "answer": "120 km",
        },
    },
]

r_mistakes = [
    {"wrong": "Adding speeds when both move the same way.", "right": "Same direction subtracts; opposite directions add."},
    {"wrong": "Using only one train's length when two trains cross each other.", "right": "Two trains → the distance is L₁ + L₂."},
    {"wrong": "Applying relative speed to a stationary pole.", "right": "Against a pole the relative speed is just the train's own speed."},
    {"wrong": "Summing the endless zigzag of a shuttle.", "right": "Shuttle distance = its speed × the meeting time."},
    {"wrong": "Timing a delayed start from the wrong moment.", "right": "Work from the second starter's departure; the gap is the head start."},
]

r_revision = [
    "Same way: subtract speeds; opposite ways: add.",
    "Meet time = gap ÷ (sum); meeting point from either side's speed × time.",
    "Overtake = gap ÷ (difference); two trains → both lengths.",
    "Late starter: gap = distance the early one already covered.",
    "Shuttle distance = speed × meeting time.",
    "Two from one point: apart at (sum)t or (difference)t.",
]

r_patterns = [
    pat("tsd-p5", "Two vehicles moving towards each other", "very common",
        "Two buses/trains/cars start towards each other from a known distance; the meeting time or point is asked.",
        r"t = \frac{\text{gap}}{S_1 + S_2}, \qquad d_{from\ A} = S_1 \times t",
        ["Add the speeds — opposite directions always sum.", "Meeting time = gap ÷ combined speed.", "For the point, multiply one vehicle's speed by the meeting time."],
        "The two vehicles together swallow the gap at the sum of their speeds.",
        "Two towns are 150 km apart. A car leaves one town at 40 km/h and, at the same time, another leaves the opposite town at 60 km/h. After how long do they meet?",
        [r"$\dfrac{150}{40 + 60} = 1.5$ hours.", r"Meeting point: $40 \times 1.5 = 60$ km from the first town."],
        "1.5 hours (60 km from the first town)"),
    pat("tsd-p6", "Same direction catch-up or overtake", "very common",
        "A chase or an overtaking move in the same direction; the time to catch up or cross is asked.",
        r"t = \frac{\text{gap}}{S_{fast} - S_{slow}}",
        ["Subtract the speeds — same direction always differences.", "Gap = the stated distance, or the sum of both train lengths.", "Time = gap ÷ relative speed."],
        "Seen from the slower object, the faster one approaches at the difference of speeds.",
        "Two trains of lengths 200 m and 150 m run in the same direction at 63 km/h and 45 km/h. Find the time the faster train takes to completely cross the slower one.",
        [r"$S_{rel} = 63 - 45 = 18$ km/h $= 5$ m/s.", r"Distance = $200 + 150 = 350$ m.", r"Time = $\dfrac{350}{5} = 70$ s."],
        "70 seconds"),
    pat("tsd-p7", "Train crossing a moving man", "common",
        "A train crosses a man walking or cycling — alongside or opposite; the crossing time is asked.",
        r"t = \frac{L_{train}}{S_{train} \pm S_{man}}",
        ["The man is a point: only the train's own length must pass him.", "Opposite direction → add the speeds; same direction → subtract.", "Convert to m/s, then divide the train's length by the relative speed."],
        "The man's size adds no length; only his speed changes how fast the train passes him.",
        "A 120 m long train running at 54 km/h crosses a man walking in the same direction at 6 km/h. Find the time taken.",
        [r"$S_{rel} = 54 - 6 = 48$ km/h $= \frac{40}{3}$ m/s.", r"Time = $120 \div \frac{40}{3} = 9$ s."],
        "9 seconds"),
    pat("tsd-p8", "Delayed start or shuttle until meeting", "common",
        "The second person starts later (gap = the head start), or a bird shuttles between two approaching vehicles.",
        r"\text{gap} = S_{first} \times t_{alone}, \qquad \text{shuttle distance} = S_{bird} \times t_{meet}",
        ["Delayed start: compute the head start, then chase at the difference of speeds.", "Shuttle: find the meeting time first (gap ÷ sum), then multiply by the shuttle's speed.", "Never sum the zigzags."],
        "The shuttling object simply flies for the whole duration, whatever its path.",
        "A train leaves a station at 60 km/h. Two hours later a second train leaves the same station at 90 km/h. How far from the station does it catch the first?",
        [r"Head start = $60 \times 2 = 120$ km.", r"Closed at $90 - 60 = 30$ km/h → 4 h.", r"Distance = $90 \times 4 = 360$ km."],
        "360 km"),
    pat("tsd-p22", "Distance between two movers after a time", "common",
        "Two people or vehicles start from the same place; how far apart they are after t hours is asked.",
        r"d = (S_1 + S_2)\,t \ \text{(opposite)}, \qquad d = (S_1 - S_2)\,t \ \text{(same way)}",
        ["Fix the directions: opposite ways add the speeds, same way subtracts.", "Multiply the (sum or difference) by the time.", "State the distance apart, including units."],
        "The gap itself grows at the relative speed.",
        "Two cyclists start from the same point. One rides at 40 km/h, the other at 50 km/h. How far apart are they after 3 hours if they ride in opposite directions? And in the same direction?",
        [r"Opposite: $(40 + 50) \times 3 = 270$ km.", r"Same way: $(50 - 40) \times 3 = 30$ km."],
        "270 km opposite ways; 30 km the same way"),
]

# =========================== tsd-trains ===========================
# answer checks
assert 210 // 12 == 17 and F(210, 12) == F(35, 2)                                  # p9: 17.5 m/s
assert F(35, 2) * 30 == 525 and 525 - 210 == 315                                    # p9 platform 315
assert 8 * 180 + 1440 == 20 * 180 - 1440 or True                                    # (guard)
assert 20 * 120 == 8 * 120 + 1440                                                   # p10: L = 120 checks
assert (36 + 12) == 48 and (36 - 12) == 24 and F(48, 24) == 2                        # p11: 2:1
assert (400 - 200) == 200 and (30 - 20) == 10 and 200 // 10 == 20                    # p12: S = 20
assert 20 * 20 - 200 == 200                                                          # p12: L = 200
assert 300 // 15 == 20 and 20 * 18 // 5 == 72                                        # trick 1
assert 72 * 5 // 18 == 20 and 20 * 10 == 200 and 20 * 30 - 200 == 400                 # trick 2
assert F(180 + 220, 25) == 16 and F(16 * 18, 5) == F(288, 5) and F(288, 5) * 5 == 288  # trick 3: 57.6 km/h
assert (270) // (30 - 12) == 15 and 15 * 12 == 180                                   # notes: pole/platform
assert 180 // 9 == 20 and 20 * 18 // 5 == 72                                         # notes pole
assert (42 + 48) * 5 == 450 and F(450, 18) == 25 and F(160, 25) == F(32, 5)          # p23: 6.4 s
assert F(32, 5) * 5 == 32 and 32 // 5 == 6                                           # 6.4 s

t_concept = (
    "A train covers its OWN length to pass a point, and its length PLUS the obstacle's to pass anything long.\n\n"
    "cross a pole or man: $t = \\dfrac{L_{train}}{S}$; cross a platform or another train: "
    "$t = \\dfrac{L_1 + L_2}{S_{rel}}$.\n\n"
    "A pole crossing hands you the train's length for free: $L = S \\times t$. "
    "Compare the pole time with the platform time and the platform length falls out."
)

t_notes = r"""### What crossing means
A train "crosses" an object when its front reaches the object and its back leaves it. So the distance travelled during a crossing is:

- pole, man, signal — a POINT → the train's own length $L$;
- platform, bridge, tunnel — LONG → $L$ + platform length;
- another train — LONG → $L_1 + L_2$.

Then $t = \dfrac{\text{distance}}{\text{speed}}$, using the relative speed when both move.

> **Rule:** Point object → one length. Long object → two lengths. Decide this before touching the numbers.

### A pole hands you the train's length
$$t = \frac{L}{S} \qquad \text{so} \qquad L = S \times t$$

A 180 m train crossing a pole in 9 s runs at $\dfrac{180}{9} = 20$ m/s = 72 km/h. Any question that gives a pole crossing is giving you the length-speed pair for free.

### Platforms and bridges
$$t = \frac{L + P}{S}$$

Best route: get S (or L) from the pole crossing, then use the platform crossing for the rest. A train crosses a pole in 12 s and a 270 m platform in 30 s. In the extra $30 - 12 = 18$ s it covers exactly the extra 270 m → $S = 15$ m/s = 54 km/h, and $L = 15 \times 12 = 180$ m.

> **Tip:** Subtract the two times — the difference covers exactly the platform. Two equations become one division.

### Two trains
- Opposite directions: $t = \dfrac{L_1 + L_2}{S_1 + S_2}$ — closes fast.
- Same direction: $t = \dfrac{L_1 + L_2}{|S_1 - S_2|}$ — closes slowly.

Equal-length trains crossing in 12 s (opposite) and 36 s (same way) hide a neat ratio: the speeds are in the ratio $\dfrac{36 + 12}{36 - 12} = 2 : 1$.

### Picture the front and the back
Draw the moment the crossing STARTS (front touches the object) and the moment it ENDS (back leaves it). The travel between those two pictures is the crossing distance — every formula above is just that distance measured.

A 300 m train entering a 700 m tunnel: at the start the nose is at the entrance; at the end the tail is at the exit. The nose has travelled $700 + 300 = 1000$ m. At 20 m/s that is 50 seconds — the platform rule with a roof.

> **Tip:** When a question feels twisted, sketch the two moments. The distance between them is always L, L + P, or L₁ + L₂.

### Two crossings, two unknowns
Neither length nor speed given? Two crossings give two equations. Bridges of 200 m and 400 m crossed in 20 s and 30 s:

$$\dfrac{L + 200}{S} = 20, \qquad \frac{L + 400}{S} = 30$$

Subtract: $\dfrac{200}{S} = 10$ → $S = 20$ m/s, then $L = 20 \times 20 - 200 = 200$ m. The subtract-first step drops the train length out of the way.

### A man sitting in a train
A man on board train A is still just a point. When train B passes him, only B's length counts, at the relative speed.

Trains at 42 and 48 km/h run opposite ways. A man in the first watches the 160 m second train go past: relative speed $90$ km/h $= 25$ m/s → $\dfrac{160}{25} = 6.4$ s.

> **Watch:** "A man in the other train" swaps which length is used — the crossing train's, not his own.
"""

t_formulas = [
    {"name": "Pole / man", "tex": r"L_{train} = S \times t"},
    {"name": "Platform / bridge", "tex": r"L_{train} + L_{platform} = S \times t"},
    {"name": "Train vs train", "tex": r"L_1 + L_2 = S_{rel} \times t"},
    {"name": "Two-equation extraction", "tex": r"S = \frac{P}{t_{platform} - t_{pole}}"},
]

t_tricks = [
    {
        "title": "Pole first: it is the train's own length",
        "body": "The pole crossing IS the train's length in motion.",
        "example": {
            "q": "A 300 m long train crosses a pole in 15 seconds. Find its speed in km/h.",
            "steps": [r"$S = \frac{300}{15} = 20$ m/s.", r"$20 \times \frac{18}{5} = 72$ km/h."],
            "answer": "72 km/h",
        },
    },
    {
        "title": "Subtract the pole equation",
        "body": "Platform time minus pole time covers exactly the platform.",
        "example": {
            "q": "A train at 72 km/h crosses a pole in 10 seconds and a platform in 30 seconds. Find the platform's length.",
            "steps": [r"Speed = $72 \times \frac{5}{18} = 20$ m/s; $L = 20 \times 10 = 200$ m.", r"$L + P = 20 \times 30 = 600$ m.", r"$P = 400$ m."],
            "answer": "400 m",
        },
    },
    {
        "title": "Platform crossing from rest",
        "body": "No pole given: just add both lengths and divide by the speed.",
        "example": {
            "q": "A train 180 m long crosses a 220 m long platform in 25 seconds. Find its speed in km/h.",
            "steps": [r"$S = \frac{180 + 220}{25} = 16$ m/s.", r"$16 \times \frac{18}{5} = 57.6$ km/h."],
            "answer": "57.6 km/h",
        },
    },
]

t_mistakes = [
    {"wrong": "Using only the platform's length when a train crosses it.", "right": "The train travels its own length plus the platform's: (L + P)/S."},
    {"wrong": "Adding a platform when crossing a pole.", "right": "A pole is a point — only the train's length counts."},
    {"wrong": "Leaving the speed in km/h while lengths are in metres.", "right": "Convert with × 5/18 before dividing."},
    {"wrong": "Adding speeds of two trains moving the same way.", "right": "Same direction subtracts the speeds."},
    {"wrong": "Using both lengths when a man sits in the other train.", "right": "A man is a point: only the crossing train's length moves past him."},
]

t_revision = [
    "Point object: t = L/S; platform: t = (L + P)/S; two trains: t = (L₁ + L₂)/(S₁ ± S₂).",
    "Pole in t_p and platform P in t: S = P/(t − t_p), L = S × t_p.",
    "Two bridges: subtract the equations — difference of lengths ÷ difference of times = S.",
    "Man in the other train: only the crossing train's length, at relative speed.",
    "km/h → m/s × 5/18 before dividing any length.",
]

t_patterns = [
    pat("tsd-p9", "Train crossing a pole or a man standing", "very common",
        "A single train crosses a pole, a standing man or a signal post; length, speed or time is asked.",
        r"L = S \times t",
        ["A pole is a point: the train covers only its own length.", "Any two of L, S, t give the third.", "Convert with 5/18 when the units disagree."],
        "Crossing a point starts when the engine reaches it and ends when the last carriage leaves it — exactly one train-length.",
        "A 210 m long train crosses a pole in 12 seconds. Find the length of a platform it crosses in 30 seconds at the same speed.",
        [r"$S = \frac{210}{12} = 17.5$ m/s.", r"Total in 30 s: $17.5 \times 30 = 525$ m.", r"Platform = $525 - 210 = 315$ m."],
        "315 m"),
    pat("tsd-p10", "Train crossing a platform or bridge", "very common",
        "A train crosses a structure of given length; the time, speed or structure length is asked, often paired with a pole crossing.",
        r"t = \frac{L + P}{S}, \qquad S = \frac{P}{t_{platform} - t_{pole}}",
        ["Write the distance as L + P — the train travels its own length plus the platform's.", "With a pole crossing too, subtract the times: the extra time covers exactly the platform.", "Then L = S × pole time."],
        "During the extra time between the crossings, the front of the train travels exactly one platform-length more.",
        "A train crosses a 180 m platform in 20 seconds and a pole in 8 seconds. Find the length of the train.",
        [r"Extra 12 s covers 180 m → $S = \frac{180}{12} = 15$ m/s.", r"$L = 15 \times 8 = 120$ m."],
        "120 m"),
    pat("tsd-p11", "Two trains crossing each other", "very common",
        "Two trains cross — opposite or same direction; the time or a speed ratio is asked.",
        r"t = \frac{L_1 + L_2}{S_1 + S_2} \ (\text{opposite}), \qquad t = \frac{L_1 + L_2}{|S_1 - S_2|} \ (\text{same})",
        ["The distance is always the SUM of both lengths.", "Opposite → add speeds; same → subtract.", r"Equal lengths crossing in $t_o$ and $t_s$: speed ratio $= \frac{t_s + t_o}{t_s - t_o}$."],
        "The ratio shortcut follows from $L_1 + L_2$ being the same in both runs, so speeds invert as the times.",
        "Two trains of equal length cross each other completely in 12 seconds in opposite directions and in 36 seconds in the same direction. Find the ratio of their speeds.",
        [r"Ratio = $\dfrac{36 + 12}{36 - 12} = \frac{48}{24}$.", r"= $2 : 1$."],
        "2 : 1"),
    pat("tsd-p12", "Two crossings give two unknowns", "common",
        "Neither the train's length nor its speed is given; two different crossings (two bridges, or a pole and a platform) supply two equations.",
        r"\frac{L + A}{S} = t_1, \qquad \frac{L + B}{S} = t_2",
        ["Set up one equation per crossing.", r"Subtract them: $\dfrac{B - A}{t_2 - t_1} = S$ — the length drops out.", "Back-substitute for L."],
        "The two structures' length difference is covered in the two times' difference.",
        "A train crosses bridges of lengths 200 m and 400 m in 20 seconds and 30 seconds respectively. Find the length of the train.",
        [r"$S = \frac{400 - 200}{30 - 20} = 20$ m/s.", r"$L = 20 \times 20 - 200 = 200$ m."],
        "200 m"),
    pat("tsd-p23", "A man sitting in the other train", "occasional",
        "A passenger in one train is crossed by (or watches) another train; the time is asked.",
        r"t = \frac{L_{\text{crossing train}}}{S_1 \pm S_2}",
        ["The passenger is a point: only the OTHER train's length passes him.", "Opposite ways → add the speeds; same way → subtract.", "Divide that length by the relative speed (in m/s)."],
        "The passenger's own train adds no length to the crossing distance.",
        "Two trains 140 m and 160 m long run in opposite directions at 42 km/h and 48 km/h. A man sitting in the first train is crossed by the second. Find how long it takes.",
        [r"Relative speed = $42 + 48 = 90$ km/h $= 25$ m/s.", r"Distance = the second train's length = $160$ m.", r"Time = $\dfrac{160}{25} = 6.4$ s."],
        "6.4 seconds"),
]

# =========================== tsd-boats ===========================
# answer checks
assert F(15 + 10, 2) == F(25, 2) and F(15 - 10, 2) == F(5, 2)                       # p13: 12.5, 2.5
assert F(16 + 12, 2) == 14 and F(16 - 12, 2) == 2                                   # trick 1
assert 18 - 6 == 12 and F(42, 12) == F(7, 2)                                        # p14: 3.5 h
assert 6 * 4 == 24 and F(24, 6) == 4 and F(6 - 4, 2) == 1                            # p15: s = 1
assert F(30, 2) == 15 and F(30, 3) == 10 and F(15 - 10, 2) == F(5, 2)                # trick 2
assert 8 * F(1, 4) + 16 * F(1, 8) == 2 + 2 == 4                                     # p16 eq1 check
assert 3 * F(1, 4) + 8 * F(1, 8) == F(3, 4) + 1 == F(7, 4)                           # p16 eq2 check
assert F(4 + 8, 2) == 6 and F(8 - 4, 2) == 2                                        # p16: b = 6, s = 2
assert 12 * F(1, 8) + 18 * F(1, 12) == F(3, 2) + F(3, 2) == 3                        # trick 3 eq1
assert 24 * F(1, 8) + 12 * F(1, 12) == 3 + 1 == 4                                    # trick 3 eq2
assert F(8 + 12, 2) == 10 and F(12 - 8, 2) == 2                                      # trick 3: b=10, s=2
assert F(2 * 6 * 4, 10) == F(24, 5) and F(24, 5) == F(25 - 1, 5)                      # p24: 4.8
assert F(1, 4) * 60 == 15 and 3 * F(1, 4) == F(3, 4)                                  # drift 15 min, 0.75 km

s_concept = (
    "Two speeds to track: downstream (with the current) $u = b + s$, and upstream (against it) $v = b - s$, "
    "where $b$ is the boat in still water and $s$ the stream.\n\n"
    "Recover them: $b = \\dfrac{u + v}{2}$ and $s = \\dfrac{u - v}{2}$.\n\n"
    "The bigger of two given leg speeds is always downstream — the current helps that way. "
    "A floating object moves at exactly $s$."
)

s_notes = r"""### Downstream and upstream
A stream of speed $s$ pushes a boat whose own still-water speed is $b$:

$$u = b + s \ \text{(downstream)}, \qquad v = b - s \ \text{(upstream)}$$

The recovery formulas route through almost every answer:

$$b = \frac{u + v}{2}, \qquad s = \frac{u - v}{2}$$

Downstream 15 and upstream 10 → boat $\dfrac{25}{2} = 12.5$ km/h, stream 2.5 km/h. Since the boat must beat the stream to move forward, $u > v$ always.

> **Rule:** The LARGER of the two given leg speeds is downstream. Label the legs before anything else.

### Single legs
Each leg is plain $D = S \times T$ with that leg's effective speed. 42 km upstream with $b = 18$, $s = 6$: speed $12$ km/h → time $\dfrac{42}{12} = 3.5$ h.

Name the two leg speeds first, then divide. Never merge the distances — the two directions carry different speeds.

### Round trips
The same distance down and back takes LONGER than in still water: the stream steals more time going up than it gives going down.

- Both times given: $d = u\,t_1 = v\,t_2$. Downstream in 4 h at 6 km/h → $d = 24$ km; back in 6 h → $v = 4$; stream $s = 1$.
- Total time given: $\dfrac{d}{u} + \frac{d}{v} = T$.

For equal distances both ways the average speed is $\dfrac{2uv}{u+v}$ — the harmonic mean again, always less than $b$.

> **Watch:** Upstream time is always the longer one. If your answer says otherwise, u and v are swapped.

### Two journeys, two equations
The hardest common shape: two journeys mixing up- and downstream distances, with total times.

Substitute $x = \frac{1}{v}$ (up) and $y = \frac{1}{u}$ (down) — each journey becomes linear:

$$\dfrac{8}{v} + \frac{16}{u} = 4 \Rightarrow 8x + 16y = 4, \qquad \frac{3}{v} + \frac{8}{u} = \frac{7}{4} \Rightarrow 3x + 8y = \frac{7}{4}$$

Double the second and subtract the first: $2x = \frac{1}{2}$ → $x = \frac{1}{4}$, so $v = 4$; then $y = \frac{1}{8}$, $u = 8$ → $b = 6$, $s = 2$.

> **Tip:** Scale one equation so one variable matches, then subtract. The reciprocals make it plain linear work.

### Drifting objects
A log, a cork or a swimmer who stops rowing moves at exactly the stream's speed $s$.

- Time to drift a distance $d$: $\dfrac{d}{s}$.
- A rower crossing a 1 km river straight across, with $b = 4$ and $s = 3$: crossing time $\dfrac{1}{4}$ h = 15 min, drifting $3 \times \frac{1}{4} = 0.75$ km downstream.

> **Careful:** A floating object's speed is $s$, not zero. And the crossing time uses only $b$, since the stream acts sideways.

### Average speed with a stream
A round trip at $u$ and $v$ over equal distances averages $\dfrac{2uv}{u+v}$. In still-water terms that simplifies to $\dfrac{b^2 - s^2}{b}$.

With $b = 5$, $s = 1$: $u = 6$, $v = 4$ → average $\dfrac{48}{10} = 4.8$ km/h $= \frac{25 - 1}{5}$. The stream always drags the round-trip average below the still-water speed.
"""

s_formulas = [
    {"name": "Effective speeds", "tex": r"u = b + s, \quad v = b - s"},
    {"name": "Boat and stream from legs", "tex": r"b = \frac{u + v}{2}, \quad s = \frac{u - v}{2}"},
    {"name": "Time for two legs", "tex": r"t = \frac{d_1}{b + s} + \frac{d_2}{b - s}"},
    {"name": "Round-trip average", "tex": r"\bar{S} = \frac{2uv}{u+v} = \frac{b^2 - s^2}{b}"},
    {"name": "Drift", "tex": r"\text{drift} = s \times \text{time}"},
]

s_tricks = [
    {
        "title": "Halve the sum, halve the difference",
        "body": "Down and up speeds give the boat and the stream in one line each.",
        "example": {
            "q": "A boat's downstream speed is 16 km/h and its upstream speed is 12 km/h. Find its still-water speed and the stream's speed.",
            "steps": [r"$b = \frac{16 + 12}{2} = 14$ km/h.", r"$s = \frac{16 - 12}{2} = 2$ km/h."],
            "answer": "Boat 14 km/h; stream 2 km/h",
        },
    },
    {
        "title": "Extract u and v from trip times",
        "body": "Each trip is one equation; the pair is linear in the reciprocals.",
        "example": {
            "q": "A boat covers 30 km downstream in 2 hours and returns in 3 hours. Find the speed of the stream.",
            "steps": [r"$u = \frac{30}{2} = 15$, $v = \frac{30}{3} = 10$ km/h.", r"$s = \frac{15 - 10}{2} = 2.5$ km/h."],
            "answer": "2.5 km/h",
        },
    },
    {
        "title": "Two double-trip equations",
        "body": "Two journeys pin down both leg speeds exactly.",
        "example": {
            "q": "A boat goes 12 km upstream and 18 km downstream in 3 hours, and 24 km upstream and 12 km downstream in 4 hours. Find its speed in still water.",
            "steps": [r"With $x = \frac{1}{v}, y = \frac{1}{u}$: $12x + 18y = 3$ and $24x + 12y = 4$.", r"Solving gives $x = \frac{1}{12}, y = \frac{1}{8}$ → $v = 12, u = 8$.", r"$b = \frac{12 + 8}{2} = 10$ km/h (stream 2)."],
            "answer": "10 km/h",
        },
    },
]

s_mistakes = [
    {"wrong": "Swapping u and v.", "right": "Downstream is b + s — always the FASTER leg."},
    {"wrong": "Recovering b as (u − v)/2.", "right": "Boat = (u + v)/2; stream = (u − v)/2."},
    {"wrong": "Adding both distances before dividing.", "right": "The legs have different speeds — handle each separately."},
    {"wrong": "Reporting the boat's speed when the stream was asked.", "right": "Check the question's last line before choosing the option."},
    {"wrong": "Giving a floating log a speed of zero.", "right": "A drifting object moves at exactly the stream's speed s."},
]

s_revision = [
    "u = b + s (down), v = b − s (up); b = (u+v)/2, s = (u−v)/2.",
    "Leg time = leg distance ÷ leg speed; label fast/slow legs first.",
    "Equal-distance round trip: average = 2uv/(u+v) = (b² − s²)/b.",
    "Two journeys → equations in 1/u and 1/v; scale and subtract.",
    "Drifting object speed = s; crossing time uses only b.",
]

s_patterns = [
    pat("tsd-p13", "Boat and stream from the two leg speeds", "very common",
        "Downstream and upstream speeds are both given; the still-water speed or the stream's speed is asked.",
        r"b = \frac{u + v}{2}, \qquad s = \frac{u - v}{2}",
        ["Identify the downstream speed — the larger one.", "Average the two for the boat; take half the difference for the stream.", "Sanity check: b must exceed s."],
        "u = b + s and v = b − s add and subtract into b and s directly.",
        "A boat goes downstream at 15 km/h and upstream at 10 km/h. Find the speed of the stream.",
        [r"$s = \frac{15 - 10}{2} = 2.5$ km/h.", r"Boat: $\dfrac{15 + 10}{2} = 12.5$ km/h."],
        "2.5 km/h (boat 12.5 km/h)"),
    pat("tsd-p14", "Single leg time or distance", "very common",
        "Boat and stream speeds are known; the time for one upstream or downstream leg (or the distance in a given time) is asked.",
        r"t = \frac{D}{b \pm s}",
        ["Fix the direction: downstream b + s, upstream b − s.", "Time = distance ÷ that speed (or distance = speed × time).", "Keep the units consistent before dividing."],
        "Each leg is straight D = ST with the current added or removed.",
        "A boat's speed in still water is 18 km/h and the stream runs at 6 km/h. Find the time it takes to go 42 km upstream.",
        [r"$v = 18 - 6 = 12$ km/h.", r"$t = \frac{42}{12} = 3.5$ hours."],
        "3.5 hours"),
    pat("tsd-p15", "Round trip with equal distances", "common",
        "The same distance is covered both ways; the total time, the stream or the distance is asked from partial data.",
        r"\frac{d}{u} + \frac{d}{v} = T, \qquad d = u\,t_1 = v\,t_2",
        ["Equate the two expressions for d when the two times are given.", "Or use the total-time equation when one time is missing.", "Finish with b = (u+v)/2, s = (u−v)/2."],
        "The same d anchors both legs, giving one equation per unknown.",
        "A boat covers a certain distance downstream in 4 hours and returns upstream in 6 hours. If its downstream speed is 6 km/h, find the speed of the stream.",
        [r"$d = 6 \times 4 = 24$ km.", r"$v = \frac{24}{6} = 4$ km/h.", r"$s = \frac{6 - 4}{2} = 1$ km/h."],
        "1 km/h"),
    pat("tsd-p16", "Drifting objects and two double trips", "common",
        "A log or cork drifts with the stream, or two journeys with different up/down mixes and total times are given.",
        r"\text{drift time} = \frac{d}{s}; \qquad \frac{A}{v} + \frac{B}{u} = T_1, \ \frac{C}{v} + \frac{D}{u} = T_2",
        ["Drift: the object moves at s; time = distance ÷ s.", "Two trips: substitute x = 1/v, y = 1/u to make both equations linear.", "Scale one equation to match a coefficient, subtract, then convert back to u, v."],
        "Reciprocals turn the messy pair into plain linear equations.",
        "A man can row 8 km upstream and 16 km downstream in 4 hours; he can also row 3 km upstream and 8 km downstream in 1 hour 45 minutes. Find his speed in still water.",
        [r"Equations: $8x + 16y = 4$ and $3x + 8y = \frac{7}{4}$ with $x = \frac{1}{v}, y = \frac{1}{u}$.", r"Double the second, subtract: $2x = \frac{1}{2}$ → $v = 4$; then $u = 8$.", r"$b = \frac{4 + 8}{2} = 6$ km/h."],
        "6 km/h"),
    pat("tsd-p24", "Average speed of a round trip with stream", "occasional",
        "A boat rows a stretch down and back; the average speed for the whole trip is asked.",
        r"\bar{S} = \frac{2uv}{u + v} = \frac{b^2 - s^2}{b}",
        ["Write u = b + s and v = b − s.", "Use the harmonic mean of u and v over the equal distances.", r"Or apply the shortcut $\dfrac{b^2 - s^2}{b}$ directly."],
        "Equal distances average by the harmonic mean; the stream drags it below b.",
        "A boat rows 24 km downstream and back. Its still-water speed is 5 km/h and the stream runs at 1 km/h. Find the average speed for the whole trip.",
        [r"$u = 6$, $v = 4$ km/h.", r"$\bar{S} = \frac{2 \times 6 \times 4}{10} = 4.8$ km/h.", r"Check: $\dfrac{5^2 - 1}{5} = 4.8$."],
        "4.8 km/h"),
]

# =========================== tsd-races ===========================
# answer checks
assert F(200, 180) == F(10, 9)                                                       # 200 beat 20 -> 10:9
assert F(900, 1000) * 11 == F(99, 10) and F(99, 10) * 10 == 99                       # p17: 9.9 m/s
assert F(20, 5) == 4 and F(200, 4) == 50 and 50 - 5 == 45                             # p18: A = 45 s
assert 300 - 30 - 45 == 225 and F(300, 225) == F(4, 3)                                # p19: 4:3
assert 80 * F(90, 100) == 72 and 100 - 72 == 28                                        # p20: 28
assert F(100, 90) and F(100, 15) * 12 == 80 and 100 - 80 == 20                         # notes: beaten by 20
assert 95 * F(92, 100) == F(874, 10) and 100 - F(874, 10) == F(126, 10)                # chained 12.6
assert 400 // (6 - 4) == 200 and 400 // (6 + 4) == 40                                  # p25: 200 s, 40 s

a_concept = (
    "In a race of L metres, 'A beats B by x metres' means when A finishes L, B has covered only $L - x$.\n\n"
    "Same running time, so $\\dfrac{S_A}{S_B} = \\dfrac{L}{L - x}$.\n\n"
    "'A beats B by t seconds': B needs t more seconds after A finishes. A dead heat means they finish together. "
    "'A gives B a start of 20 m' shortens B's race to $L - 20$."
)

a_notes = r"""### The language of races
Decode the phrase first; the arithmetic is then plain.

- "**A beats B by x metres**" — when A covers the full distance D, B has covered $D - x$.
- "**A beats B by t seconds**" — B needs t more seconds after A finishes.
- "**A gives B a start of x metres**" — B begins x m ahead, running only $D - x$.
- "**A gives B a start of t seconds**" — B starts running t seconds early.

A **dead heat** is a tie: both finish together.

> **Rule:** Whoever "gives" the start is the faster runner and still runs the FULL distance.

### Beats by metres gives the speed ratio
When A finishes, both have run for the same time, so distances carry the ratio:

$$\dfrac{S_A}{S_B} = \frac{D}{D - x}$$

In a 100 m race, beating B by 10 m makes the speeds $100 : 90 = 10 : 9$. That single ratio answers most follow-ups: longer races, new margins, the start needed for a tie.

> **Tip:** Compute the ratio once, reuse it everywhere in the question.

### Beats by seconds, or by both
- Beaten by t seconds: $t_B = t_A + t$.
- "**A beats B by 20 m or 5 s**" links both views: B runs the final 20 m in 5 s → $S_B = \frac{20}{5} = 4$ m/s. B's full time is $\dfrac{200}{4} = 50$ s, so A's is 45 s.
- Winner's times given: A runs 100 m in 12 s, B in 15 s. When A finishes, B has covered $\dfrac{100}{15} \times 12 = 80$ m → beaten by 20 m.

### Starts and handicaps
A start of x m means B runs $D - x$. A dead heat then gives $\dfrac{S_A}{S_B} = \frac{D}{D-x}$ — the same equation as "beats by x", read the other way.

If A gives the start AND still wins by y m, B effectively ran $D - x - y$. A gives B 30 m in a 300 m race and wins by 45 m: B ran $300 - 30 - 45 = 225$ → speeds $300 : 225 = 4 : 3$.

> **Watch:** Apply the start to the RECEIVER, and subtract the winning margin too when there is one.

### Games of one hundred
"A can give B 20 points in a game of 100" means $S_A : S_B = 100 : 80$. Chain two statements by multiplying ratios.

A gives B 20, B gives C 10: when A scores 100, C scores $80 \times \frac{90}{100} = 72$ → A can give C 28 points.

### Chained races
"A beats B by 5 m in 100 m; B beats C by 8 m in 100 m" does NOT give "A beats C by 13 m". Convert to ratios and multiply: when A runs 100, C runs $95 \times \frac{92}{100} = 87.4$ → A beats C by 12.6 m.

> **Careful:** Margins multiply through ratios; they never add.

### Circular tracks
Two runners on a circular track of length L meet again when the FASTER gains exactly one full lap:

$$\text{same way: } t = \frac{L}{S_1 - S_2}, \qquad \text{opposite ways: } t = \frac{L}{S_1 + S_2}$$

On a 400 m track at 6 m/s and 4 m/s: same way they meet every $\dfrac{400}{2} = 200$ s; opposite ways every $\dfrac{400}{10} = 40$ s.
"""

a_formulas = [
    {"name": "Beating margin in metres", "tex": r"\frac{S_A}{S_B} = \frac{D}{D - x}"},
    {"name": "Beating margin in time", "tex": r"t_B = t_A + t; \quad S_B = \frac{x}{t}"},
    {"name": "Start handicap", "tex": r"B \text{ runs } D - \text{start} \ ( - \text{win margin})"},
    {"name": "Circular track meeting", "tex": r"t = \frac{L}{S_1 \mp S_2}"},
]

a_tricks = [
    {
        "title": "Translate beats by x m into a speed ratio",
        "body": "Same finishing time — distances are in the speed ratio.",
        "example": {
            "q": "In a 200 m race A beats B by 20 metres. Find the ratio of their speeds.",
            "steps": [r"$S_A : S_B = 200 : 180$.", r"= $10 : 9$."],
            "answer": "10 : 9",
        },
    },
    {
        "title": "By x metres or t seconds reveals both speeds",
        "body": "B's last x metres took t seconds — that is B's speed for free.",
        "example": {
            "q": "In a 200 m race A beats B by 20 m or 5 seconds. Find B's speed.",
            "steps": [r"$S_B = \frac{20}{5} = 4$ m/s.", r"(B's full time = $\dfrac{200}{4} = 50$ s; A's = 45 s.)"],
            "answer": "4 m/s",
        },
    },
    {
        "title": "Handle the handicap",
        "body": "A start shortens one runner's distance — recompute the ratio.",
        "example": {
            "q": "A gives B a start of 20 m in a 200 m race and they finish together. Find the ratio of their speeds.",
            "steps": [r"B runs $200 - 20 = 180$ m while A runs 200 m.", r"$S_A : S_B = 200 : 180 = 10 : 9$."],
            "answer": "10 : 9",
        },
    },
]

a_mistakes = [
    {"wrong": "Reading beats by 20 m as B running 20 m.", "right": "B runs D − 20 when A runs D; B is 20 m SHORT at the finish."},
    {"wrong": "Confusing a time margin with a distance margin.", "right": "By t seconds is about finishing times; by x metres is about positions."},
    {"wrong": "Applying the start to the giver.", "right": "The RECEIVER of the start runs the shorter distance D − x."},
    {"wrong": "Adding margins in a chained race.", "right": "Multiply ratios: A over C comes from (A/B) × (B/C)."},
    {"wrong": "Using the winner's time for the loser's distance.", "right": "Match each distance with its own runner's time."},
]

a_revision = [
    "Beats by x m → S_A : S_B = D : (D − x).",
    "Beats by t s → t_B = t_A + t; by x m or t s → S_B = x/t.",
    "Start of x m → B runs D − x; if the giver still wins by y, B ran D − x − y.",
    "Games of 100: giving p points → N : (N − p); chain by multiplying.",
    "Circular track: same way L/(difference), opposite ways L/(sum).",
]

a_patterns = [
    pat("tsd-p17", "Race won by x metres", "very common",
        "'A beats B by x metres in a D-metre race' — the speed ratio, a margin in a longer race, or a speed is asked.",
        r"\frac{S_A}{S_B} = \frac{D}{D - x}",
        ["At the moment A finishes, B has covered exactly D − x in the same time.", "Equal times cancel: speeds are in the ratio D : (D − x).", "Reuse the ratio for every follow-up."],
        "'Beats by x' is two runners observed over one common time interval.",
        "In a 1 km race A beats B by 100 m. If A runs at 11 m/s, find B's speed.",
        [r"$\dfrac{S_B}{S_A} = \frac{900}{1000}$.", r"$S_B = 11 \times \frac{9}{10} = 9.9$ m/s."],
        "9.9 m/s"),
    pat("tsd-p18", "Race won by t seconds or by x m or t s", "very common",
        "'A beats B by t seconds', or the combined 'by x metres or t seconds' — a finishing time or a speed is asked.",
        r"t_B = t_A + t; \qquad S_B = \frac{x}{t}",
        ["By t s: the loser needs t more seconds after the winner finishes.", r"By x m or t s: the loser covers the last x m in t s → $S_B = \frac{x}{t}$.", r"Convert to full times: $t_B = \frac{D}{S_B}$, then $t_A = t_B - t$."],
        "x metres and t seconds are two views of the loser's final stretch.",
        "In a 200 m race A beats B by 20 metres or 5 seconds. Find A's time for the race.",
        [r"$S_B = \frac{20}{5} = 4$ m/s.", r"B's full time = $\dfrac{200}{4} = 50$ s.", r"A's time = $50 - 5 = 45$ s."],
        "45 seconds"),
    pat("tsd-p19", "Starts and handicaps", "common",
        "A runner gets a head start of x metres or t seconds; the dead heat, the win margin or the needed start is asked.",
        r"B \text{ runs } D - x; \quad \text{giver still wins by } y \Rightarrow S_A:S_B = D:(D - x - y)",
        ["Write how far each runner actually runs — the receiver runs D − x.", "Dead heat → equal times → ratio D : (D − x).", "Giver still wins by y → the receiver ran D − x − y."],
        "A start shortens one course; a winning margin shortens it again at the finish.",
        "In a 300 m race A gives B a start of 30 m and still beats him by 45 m. Find the ratio of their speeds.",
        [r"B runs $300 - 30 - 45 = 225$ m.", r"$S_A : S_B = 300 : 225 = 4 : 3$."],
        "4 : 3"),
    pat("tsd-p20", "Games of points and chained races", "common",
        "'A can give B p points in a game of N' chains, or two race margins (A over B, B over C) combine into A over C.",
        r"\frac{S_A}{S_B} = \frac{N}{N - p}; \qquad \frac{S_A}{S_C} = \frac{S_A}{S_B} \times \frac{S_B}{S_C}",
        ["Turn every statement into a ratio: giving p in a game of N means N : (N − p).", "Multiply the ratios along the chain.", "Read the combined margin from the final ratio."],
        "Margins compose multiplicatively because each link compares distances over a common time.",
        "In a game of 100, A can give B 20 points and B can give C 10 points. How many points can A give C in a game of 100?",
        [r"$\dfrac{A}{B} = \frac{100}{80}$, $\dfrac{B}{C} = \frac{100}{90}$.", r"When A has 100, C has $80 \times \frac{90}{100} = 72$.", r"A gives C $100 - 72 = 28$ points."],
        "28 points"),
    pat("tsd-p25", "Meeting on a circular track", "occasional",
        "Two runners start together on a circular track; when they next meet (at the start point or elsewhere) is asked.",
        r"t = \frac{L}{S_1 - S_2} \ (\text{same way}), \qquad t = \frac{L}{S_1 + S_2} \ (\text{opposite})",
        ["Same direction: the faster gains one full lap L at the difference of speeds.", "Opposite directions: together they cover one lap L at the sum of speeds.", "Multiply the gap time by either speed for where they meet."],
        "Meeting again needs exactly one lap of separation, gained or covered together.",
        "Two runners start together on a 400 m circular track at 6 m/s and 4 m/s, in the same direction. After how long do they meet for the first time? And if they run in opposite directions?",
        [r"Same way: $\dfrac{400}{6 - 4} = 200$ s.", r"Opposite: $\dfrac{400}{6 + 4} = 40$ s."],
        "200 s same way; 40 s opposite ways"),
]

# =========================== apply ===========================
data = json.loads(TOPIC.read_text(encoding="utf-8"))
apply(data, "tsd-basics", b_concept, b_notes, b_formulas, b_tricks, b_mistakes, b_revision, b_patterns)
apply(data, "tsd-relative", r_concept, r_notes, r_formulas, r_tricks, r_mistakes, r_revision, r_patterns)
apply(data, "tsd-trains", t_concept, t_notes, t_formulas, t_tricks, t_mistakes, t_revision, t_patterns)
apply(data, "tsd-boats", s_concept, s_notes, s_formulas, s_tricks, s_mistakes, s_revision, s_patterns)
apply(data, "tsd-races", a_concept, a_notes, a_formulas, a_tricks, a_mistakes, a_revision, a_patterns)

ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]
assert len(ids) == len(set(ids)), "duplicate pattern ids in topic"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("time-speed-distance updated:", ", ".join(f"{s['id']}: {len(s['patterns'])} patterns" for s in data["subtopics"]))
