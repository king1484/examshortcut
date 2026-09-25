"""Phase-2 deep content for quant/time-speed-distance — basics + relative speed modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, mixed


def build_basics():
    S = Sub("tsd-basics")

    S.notes = r"""### The spine: $D = S \times T$
Every question in this topic is one equation in different clothes:
$$\text{Distance} = \text{Speed} \times \text{Time}, \qquad S = \frac{D}{T}, \qquad T = \frac{D}{S}$$
Ask at every question: "which two of the three do I know?" Speed and time are inversely proportional for a fixed distance — if the speed drops to $\frac34$, the time becomes $\frac43$ of the old time. This inverse reflex solves a surprising number of questions on its own.

### Unit conversion — the 5/18 rule
Train lengths are in metres and times in seconds, but speeds are usually quoted in km/h. Convert first, always:
$$1 \text{ km/h} = \frac{5}{18} \text{ m/s}, \qquad 1 \text{ m/s} = \frac{18}{5} \text{ km/h}$$
Keep the friendly table by heart: 36 km/h = 10 m/s, 54 = 15, 72 = 20, 90 = 25, 108 = 30 m/s. To convert by hand, divide by 18 first when using $\frac5{18}$ (54 → 3 → 5×3 = 15).

### Average speed — a division, not an average
$$\text{Average speed} = \frac{\text{total distance}}{\text{total time}}$$
It is the average of the speeds **only when the times are equal**. Distances are more often equal (out and back), and then the answer is the harmonic mean:
$$\bar{S} = \frac{2ab}{a + b}$$
40 km/h out, 60 km/h back → $\frac{2 \times 2400}{100} = 48$ km/h, not 50. The equal-distance average always sits **below** the arithmetic mean, and below the mid-value of the two speeds. Three equal legs at a, b, c give $\frac{3}{\frac1a + \frac1b + \frac1c}$ — e.g. 20, 30, 60 → $\frac{3}{\frac{3+2+1}{60}} = 30$ km/h.
For legs of **different lengths**, go back to basics: add the distances, add the times, divide.

### "Late by…" and "early by…" questions
The distance is the same in both runs, so equate the two time expressions. Walking at $\frac34$ of the usual speed makes the time $\frac43 t$; the lateness is $\frac43 t - t = \frac{t}{3}$. So "20 minutes late" → $t = 60$ minutes. With two speeds s₁ and s₂ and a stated gap between the arrival times:
$$\frac{d}{s_1} - \frac{d}{s_2} = \text{gap (in hours)}$$
e.g. 5 min late at 4 km/h, 10 min early at 5 km/h → $\frac{d}{4} - \frac{d}{5} = \frac{15}{60} = \frac14$ → $d = 5$ km. Add the two gaps when one is late and the other early; subtract when both are late.

### Percentage shortcuts
Speed 20% more → time $\frac{5}{6}$ of before (7 min early on a 42-min run, etc.). Speed 20% less → time $\frac54$ of before. Convert every "reduces his speed to ¾" into the time multiplier $\frac43$ before writing any equation.

### Common traps
- Averaging the two speeds for equal distances (50 instead of 48).
- Dividing metres by km/h — no conversion done.
- Reading "speed is ¾ of usual" as "time is ¾ of usual" (it is 4/3).
- Mixing minutes and hours inside one equation — convert to hours (or fractions of an hour).

### Quick revision
- $D = ST$; speed and time are inverse for fixed distance.
- km/h → m/s: × 5/18 (table: 36→10, 54→15, 72→20, 90→25).
- Equal distances: $\frac{2ab}{a+b}$; three equal legs: $3 \div (\frac1a+\frac1b+\frac1c)$.
- Late/early: $\frac{d}{s_1} - \frac{d}{s_2} =$ time gap in hours.
- Speed ×(p/q) ⇒ time ×(q/p).
"""

    S.pattern("tsd-p1", "Direct distance–speed–time (with conversion)", "very common",
        "Two of distance, speed and time are given in mixed units; the third is asked (very often with a km/h ↔ m/s conversion built in).",
        r"S = \frac{D}{T}, \qquad \text{km/h} \times \frac{5}{18} = \text{m/s}",
        r"""1. Put all quantities in one unit system (metres and seconds, or km and hours).
2. Apply $D = S \times T$ in the direction you need.
3. Convert the answer back to the unit the options use.

Why: the formula is only consistent when distance, speed and time speak the same units.""",
        "A train covers 450 metres in 30 seconds. Its speed in km/h is:",
        r"$\frac{450}{30} = 15$ m/s → $15 \times \frac{18}{5} = 54$ km/h.")
    S.pattern("tsd-p2", "Average speed over legs of a journey", "very common",
        "A journey is split into legs (often out-and-back at different speeds, or different speeds for different durations); the average speed is asked.",
        r"\bar{S} = \frac{D_{\text{total}}}{T_{\text{total}}}, \quad \text{equal distances: } \frac{2ab}{a+b}",
        r"""1. Equal distances (typical round trip): use $\frac{2ab}{a+b}$; three equal legs: $3 \div (\frac1a+\frac1b+\frac1c)$.
2. Equal times: the plain average of the speeds.
3. Otherwise: total distance ÷ total time, computing each leg's time first.

Why: average speed is a mean over TIME; weighting by time is exactly what the harmonic mean does.""",
        "A car goes to a town at 40 km/h and returns along the same road at 60 km/h. The average speed for the round trip is:",
        r"$\frac{2 \times 40 \times 60}{40 + 60} = 48$ km/h — not 50.")
    S.pattern("tsd-p3", "Fraction of usual speed → late/early", "very common",
        "'Walking at 3/4 (or 4/5) of his usual speed he is 20 minutes late' — the usual time, or the usual speed, is asked.",
        r"\text{new time} = \frac{1}{f}\, t \ \Rightarrow\ \text{late} = \left(\frac{1}{f} - 1\right) t",
        r"""1. Speed fraction f of usual ⇒ time is $t/f$.
2. Lateness $= t(\frac1f - 1)$; set it equal to the given minutes and solve for t.
3. The distance can also be extracted if the usual speed is given.

Why: for the same distance, speed and time are inversely proportional.""",
        "Walking at $\\frac{4}{5}$ of his usual speed, a man reaches his office 10 minutes late. His usual time is:",
        r"New time $= \frac54 t$ → late $= \frac{t}{4} = 10$ → $t = 40$ minutes.")
    S.pattern("tsd-p4", "Two fixed speeds, both 'off schedule' → distance", "common",
        "'At s₁ km/h he is x minutes late; at s₂ km/h he is y minutes early' — the distance (or the exact time) is asked.",
        r"\frac{d}{s_1} - \frac{d}{s_2} = \frac{x + y}{60}",
        r"""1. Both times are compared with the SAME (unknown) schedule time, so subtract the two travel times.
2. The gap between them = late + early, converted to hours.
3. Solve $d\left(\frac{1}{s_1} - \frac{1}{s_2}\right) = \text{gap}$ for d.

Why: writing both time expressions against a common schedule cancels the unknown schedule time.""",
        "Walking at 4 km/h a student reaches school 5 minutes late; walking at 5 km/h he reaches 10 minutes early. The distance to the school is:",
        r"$\frac{d}{4} - \frac{d}{5} = \frac{15}{60} = \frac14$ → $\frac{d}{20} = \frac14$ → $d = 5$ km.")

    # ---- practice (tsd-basics) ----
    assert F(360, 6) == 60
    S.q("tsd-p1", "easy",
        "A car covers a distance of 360 km in 6 hours. Its average speed is:",
        ["60 km/h", "55 km/h", "65 km/h", "72 km/h"], "60 km/h",
        r"$S = \frac{360}{6} = 60$ km/h.",
        None, 20)
    v = F(450, 30) * F(18, 5)
    assert v == 54
    S.q("tsd-p1", "medium",
        "A train covers 450 metres in 30 seconds. Its speed in km/h is:",
        ["54 km/h", "50 km/h", "58 km/h", "60 km/h"], "54 km/h",
        r"$\frac{450}{30} = 15$ m/s → $15 \times \frac{18}{5} = 54$ km/h.",
        "15 m/s is a table value: 54 km/h.", 30)
    a = F(6 * 2 + 10 * 1, 3)
    assert a == F(22, 3)
    S.q("tsd-p2", "medium",
        "A man walks at 6 km/h for 2 hours and at 10 km/h for 1 hour. His average speed for the whole journey is:",
        ["$7\\frac{1}{3}$ km/h", "7 km/h", "8 km/h", "$7\\frac{2}{3}$ km/h"], mixed(F(22, 3)) + " km/h",
        r"""Distance $= 12 + 10 = 22$ km in 3 hours.
Average $= \frac{22}{3} = 7\frac13$ km/h.""",
        "Different times → weights are the times, not a plain average (8 would be wrong).", 40)
    h = 3 / (1 / F(20) + 1 / F(30) + 1 / F(60))
    assert h == 30
    S.q("tsd-p2", "medium",
        "A man covers three equal distances at 20 km/h, 30 km/h and 60 km/h respectively. His average speed for the whole journey is:",
        ["30 km/h", "36.67 km/h", "33.33 km/h", "25 km/h"], "30 km/h",
        r"Equal legs: $\bar{S} = \dfrac{3}{\frac{1}{20} + \frac{1}{30} + \frac{1}{60}} = \dfrac{3}{\frac{6}{60}} = 30$ km/h.",
        "36.67 is the plain average — the equal-distance trap.", 45)
    t = F(10)
    assert t * 4 == 40
    S.q("tsd-p3", "medium",
        "Walking at $\\frac{4}{5}$ of his usual speed, a man is 10 minutes late. His usual time (in minutes) is:",
        ["40", "50", "30", "45"], "40",
        r"New time $= \frac54 t$; late by $\frac{t}{4} = 10$ → $t = 40$ minutes.",
        None, 35)
    t = F(80) * 3
    assert t == 240
    S.q("tsd-p3", "medium",
        "By walking at $\\frac{3}{4}$ of his usual speed a man reaches his office 1 hour 20 minutes late. His usual time for the journey is:",
        ["4 hours", "3 hours", "5 hours", "3.5 hours"], "4 hours",
        r"New time $= \frac43 t$; late by $\frac{t}{3} = 80$ min → $t = 240$ min $= 4$ hours.",
        None, 35)
    d = F(1, 4) / (1 / F(4) - 1 / F(5))
    assert d == 5
    S.q("tsd-p4", "hard",
        "Walking at 4 km/h a student misses a bus by 5 minutes, while walking at 5 km/h he reaches the stop 10 minutes early. The distance to the bus stop is:",
        ["5 km", "4.5 km", "5.5 km", "6 km"], "5 km",
        r"Gap $= 5 + 10 = 15$ min $= \frac14$ h. $\frac{d}{4} - \frac{d}{5} = \frac{d}{20} = \frac14$ → $d = 5$ km.",
        "One late + one early → ADD the two gaps.", 50)
    d2 = F(12, 60) / (1 / F(10) - 1 / F(12))
    assert d2 == 12
    S.q("tsd-p4", "medium",
        "A cyclist covers a certain distance at 10 km/h and reaches 6 minutes late. Cycling at 12 km/h he reaches 6 minutes early. The distance is:",
        ["12 km", "10 km", "14 km", "15 km"], "12 km",
        r"$\frac{d}{10} - \frac{d}{12} = \frac{12}{60} = \frac15$ → $\frac{d}{60} = \frac15$ → $d = 12$ km.",
        None, 45)
    return S


def build_rel():
    S = Sub("tsd-relative")

    S.notes = r"""### Relative speed in one line
Whenever two moving things matter at once — meeting, crossing, overtaking, catching up — work with the **gap** and the **relative speed**:
$$\text{same direction: } S_{\text{rel}} = S_1 - S_2 \qquad \text{opposite directions: } S_{\text{rel}} = S_1 + S_2$$
Same direction means the gap closes slowly (subtract); opposite directions make it close fast (add). The distance to cover is the current gap — for two trains crossing each other, the gap to "cross completely" is the sum of their lengths.

### Meeting problems (opposite directions)
Two objects start towards each other from a gap D. They meet after
$$t = \frac{D}{S_1 + S_2}$$
240 km apart at 40 and 40 km/h → 3 hours. The meeting **point** is then fixed by one side alone: distance from A's start $= S_A \times t$. Speeds 40 and 60 from 300 km apart: meet after 3 hours, 120 km from A's end.

### Overtaking (same direction)
A faster object closes a gap G at $S_1 - S_2$:
$$t = \frac{G}{S_1 - S_2}$$
For trains the gap to clear is the two lengths together (the back of the faster must pass the front of the slower). For a cyclist or a moving man being crossed, the man is a point — only the train's own length counts.

### Train vs a walking man
The man's own size is zero. Only his speed enters: same direction → subtract it from the train's speed; opposite → add. A 120 m train at 54 km/h passing a man walking the same way at 6 km/h: relative speed 48 km/h $= \frac{40}{3}$ m/s → $120 \div \frac{40}{3} = 9$ seconds.

### Delayed starts
Someone leaves later — the gap is simply the distance the first runner covered alone. A starts at 9 a.m. at 30 km/h; B starts at 10 a.m. at 40 km/h in pursuit: gap at 10 a.m. = 30 km, closed at 10 km/h → 3 hours → 1 p.m., at $40 \times 3 = 120$ km from the start.

### The shuttle (bird) trick
A bird flies back and forth between two approaching trains "until they meet". Do NOT sum the zigzags — the bird is simply flying the whole time, so
$$\text{distance} = \text{bird's speed} \times \text{meeting time}$$
Trains 100 km apart at 20 and 30 km/h meet in 2 h; a bird at 60 km/h covers $60 \times 2 = 120$ km. One line, no series.

### Sanity habits
- Opposite directions: think "sum" before touching numbers.
- A gap must shrink: if your relative speed came out negative, you subtracted in the wrong order (take the difference of magnitudes).
- Convert km/h to m/s before dividing metres.

### Common traps
- Adding speeds when both move the same way.
- Using one train's length only, when two trains cross each other.
- In delayed-start problems, timing from the wrong start moment.
- Summing an endless zigzag instead of speed × meeting time.

### Quick revision
- Same way: subtract; opposite ways: add.
- Meet time = gap ÷ (sum of speeds); meeting point from either side.
- Overtake = gap ÷ (difference of speeds); two trains → both lengths.
- Late starter: gap = distance already covered.
- Shuttle distance = speed × meeting time.
"""

    S.pattern("tsd-p5", "Two vehicles moving towards each other", "very common",
        "Two buses/trains/people start towards each other from a known distance; the meeting time (or meeting point) is asked.",
        r"t = \frac{\text{gap}}{S_1 + S_2}, \qquad d_{\text{from A}} = S_1 \times t",
        r"""1. Add the speeds — opposite directions always sum.
2. Meeting time = initial gap ÷ combined speed.
3. For the meeting point, multiply one vehicle's speed by the meeting time.

Why: the two vehicles together swallow the gap at the sum of their speeds.""",
        "Two towns are 150 km apart. A car leaves one town for the other at 40 km/h and at the same time another car leaves the opposite town at 60 km/h. After how long do they meet?",
        r"$\frac{150}{40 + 60} = 1.5$ hours (meeting point: 60 km from the first town).")
    S.pattern("tsd-p6", "Same direction — catch up / overtake", "very common",
        "A chase or an overtaking move in the same direction; the time to catch up or the crossing time of two trains is asked.",
        r"t = \frac{\text{gap}}{S_{\text{fast}} - S_{\text{slow}}}",
        r"""1. Subtract the speeds — same direction always differences.
2. Gap = the stated distance, or the sum of both train lengths.
3. Time = gap ÷ relative speed.

Why: viewed from the slower object, the faster one approaches at the difference of speeds.""",
        "Two trains of lengths 200 m and 150 m run in the same direction at 63 km/h and 45 km/h. The time the faster train takes to completely cross the slower one is:",
        r"$S_{\text{rel}} = 18$ km/h $= 5$ m/s; total length 350 m → $\frac{350}{5} = 70$ seconds.")
    S.pattern("tsd-p7", "Train crossing a moving man", "common",
        "A train crosses a man walking/running/cycling — alongside or opposite; the crossing time is asked.",
        r"t = \frac{L_{\text{train}}}{S_{\text{train}} \pm S_{\text{man}}}",
        r"""1. The man is a point: only the train's own length has to pass.
2. Opposite direction → add the speeds; same direction → subtract.
3. Convert to m/s, divide the train's length by the relative speed.

Why: the man's size adds no length, only his speed changes how fast the train passes him.""",
        "A 120 m long train running at 54 km/h crosses a man walking in the same direction at 6 km/h in:",
        r"$S_{\text{rel}} = 48$ km/h $= \frac{40}{3}$ m/s → $120 \times \frac{3}{40} = 9$ seconds.")
    S.pattern("tsd-p8", "Delayed start / shuttle-till-meeting", "common",
        "The second person starts later (gap = what the first already covered), or a bird/object shuttles between two approaching vehicles until they meet.",
        r"\text{gap} = S_{\text{first}} \times t_{\text{alone}}, \qquad \text{shuttle distance} = S_{\text{bird}} \times t_{\text{meet}}",
        r"""1. Delayed start: compute the head start, then chase it at the difference of speeds; add the times if asked from the very beginning.
2. Shuttle: find the meeting time of the two vehicles first (sum of speeds), then multiply by the shuttle's speed.
3. Never sum the zigzags.

Why: the shuttling object simply flies for the whole duration, whatever its path looks like.""",
        "A train leaves a station at 60 km/h. Two hours later a second train leaves the same station along the same track at 90 km/h. How far from the station does the second train catch the first?",
        r"""Head start $= 120$ km; gap closes at 30 km/h → 4 h after the start of the second train.
Distance $= 90 \times 4 = 360$ km.""")

    # ---- practice (tsd-relative) ----
    assert F(240, 80) == 3
    S.q("tsd-p5", "easy",
        "Two towns A and B are 240 km apart. A bus starts from A towards B at 40 km/h and at the same time another bus starts from B towards A at 40 km/h. They will meet after:",
        ["3 hours", "2.5 hours", "3.5 hours", "4 hours"], "3 hours",
        r"$t = \frac{240}{40 + 40} = 3$ hours.",
        None, 25)
    assert F(25 - 20) == 5 and F(5, 2) * 60 == 150
    S.q("tsd-p6", "easy",
        "A thief runs at 20 km/h. A policeman, 2.5 km behind him, chases at 25 km/h. The policeman catches the thief in:",
        ["30 minutes", "25 minutes", "36 minutes", "20 minutes"], "30 minutes",
        r"Gap closes at $25 - 20 = 5$ km/h → $\frac{2.5}{5} = 0.5$ h $= 30$ minutes.",
        None, 30)
    assert F(120, 40 / F(3)) == 9
    S.q("tsd-p7", "easy",
        "A 120 m long train running at 54 km/h crosses a man walking in the same direction at 6 km/h. The train crosses him in:",
        ["9 seconds", "8 seconds", "10 seconds", "12 seconds"], "9 seconds",
        r"$S_{\text{rel}} = 54 - 6 = 48$ km/h $= \frac{40}{3}$ m/s. $t = 120 \div \frac{40}{3} = 9$ seconds.",
        None, 30)
    assert F(150, 100) * 10 == 15
    S.q("tsd-p5", "easy",
        "Two cars start towards each other from towns 150 km apart at 40 km/h and 60 km/h. They meet after:",
        ["1.5 hours", "1 hour", "2 hours", "1.25 hours"], "1.5 hours",
        r"$\frac{150}{40 + 60} = 1.5$ hours.",
        None, 25)
    assert F(350, 5) == 70
    S.q("tsd-p6", "medium",
        "Two trains of lengths 200 m and 150 m run on parallel tracks in the same direction at 63 km/h and 45 km/h. The time the faster train takes to completely cross the slower one is:",
        ["70 seconds", "60 seconds", "80 seconds", "75 seconds"], "70 seconds",
        r"$S_{\text{rel}} = 18$ km/h $= 5$ m/s. Lengths together $= 350$ m → $70$ seconds.",
        None, 40)
    assert 40 * 3 == 120
    S.q("tsd-p5", "medium",
        "Two stations are 300 km apart. A train leaves one station at 40 km/h and at the same time another leaves the other at 60 km/h, moving towards each other. How far from the first station do they meet?",
        ["120 km", "180 km", "150 km", "140 km"], "120 km",
        r"Meeting time $= \frac{300}{100} = 3$ h → from the first station $40 \times 3 = 120$ km.",
        None, 40)
    assert F(30, 10) == 3
    S.q("tsd-p8", "medium",
        "A cyclist leaves town A at 9 a.m. cycling at 30 km/h towards town B. At 10 a.m. a motorist leaves A along the same road at 40 km/h. At what time does the motorist catch the cyclist?",
        ["1 p.m.", "12 noon", "2 p.m.", "1:30 p.m."], "1 p.m.",
        r"Head start $= 30$ km. Gap closes at 10 km/h → 3 h after 10 a.m. = 1 p.m.",
        None, 40)
    assert F(240, 30) == 8
    S.q("tsd-p7", "medium",
        "A 240 m long train running at 90 km/h crosses a cyclist coming from the opposite direction at 18 km/h. The train crosses him in:",
        ["8 seconds", "9 seconds", "7.5 seconds", "10 seconds"], "8 seconds",
        r"$S_{\text{rel}} = 90 + 18 = 108$ km/h $= 30$ m/s → $\frac{240}{30} = 8$ seconds.",
        None, 35)
    assert 120 // 30 == 4 and 90 * 4 == 360
    S.q("tsd-p8", "hard",
        "A train leaves station P at 60 km/h. Two hours later, a faster train leaves P along the same track at 90 km/h and catches the first train. How far from station P does the catch-up happen?",
        ["360 km", "300 km", "320 km", "400 km"], "360 km",
        r"Head start $= 60 \times 2 = 120$ km, closed at 30 km/h → 4 h. Distance $= 90 \times 4 = 360$ km.",
        "From P the first train also ran $60 \\times 6 = 360$ km — a free check.", 50)
    return S
