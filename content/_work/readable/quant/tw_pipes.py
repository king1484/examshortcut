"""Readable rewrite of Time & Work > Pipes & Cisterns (tw-pipes).

Simple English, one idea per section, LCM-units method throughout.
Every number in an example is recomputed below with exact fractions.
Run: python tw_pipes.py  (patches content/core/topics/quant/time-work.json in place)
"""
import json
from fractions import Fraction as F
from math import lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "time-work.json"

# ---------- answer checks (every example on the page) ----------
# notes
assert lcm(12, 18) == 36 and F(36, 3 + 2) == F(36, 5) == F(72, 10)          # 7.2 h = 7 h 12 min
assert lcm(6, 9) == 18 and F(18, 3 - 2) == 18 and F(6 * 9, 9 - 6) == 18
assert lcm(10, 15) == 30 and 30 - 5 * 2 == 20 and F(20, 5 - 1) == 5            # staged: 2 + 5 = 7 h
assert lcm(8, 10) == 40 and 40 // 8 - 40 // 10 == 1 and F(8 * 10, 10 - 8) == 40
assert lcm(4, 6) == 12 and 12 - 2 * (3 + 2) == 2 and F(2, 3) * 60 == 40         # alternate: 4 h 40 min
C = F(240) / (F(1, 6) - F(1, 8)); assert C == 5760                             # litres
# patterns
assert lcm(20, 30, 60) == 60 and F(60, 3 + 2 + 1) == 10                          # p9: three inlets
assert lcm(12, 15, 20) == 60 and F(60, 5 + 4 - 3) == 10                          # p10: two in, one out
assert F(1, 6) - F(1, 8) == F(1, 24)                                             # p11: 6 h normal, 8 h with leak -> 24 h
assert lcm(12, 16, 24) == 48 and 48 - (4 + 3) * 4 == 20 and F(20, 7 - 2) == 4   # p12: 4 + 4 = 8 h
def alternate(tank, speeds):
    """Hour-by-hour simulation of pipes opened in turn; returns the exact fill time."""
    filled, t, k = F(0), F(0), 0
    while True:
        v = speeds[k % len(speeds)]
        if filled + v >= tank:
            return t + F(tank - filled, v)
        filled, t, k = filled + v, t + 1, k + 1
assert alternate(12, [3, 2]) == F(14, 3)                                         # notes: 4 h 40 min
assert lcm(3, 4) == 12 and alternate(12, [4, 3]) == F(10, 3)                     # p21: 3 h 20 min
cap = F(3) * 60 / (F(1, 5) - F(1, 20)) ; assert cap == 1200                      # p22: litres
assert lcm(20, 30) == 60 and 60 - 2 * 18 == 24 and F(24, 3) == 8                 # p23: A closed after 8 min
assert 12 * (2 + 1) == 36 and F(36, 1) == 36 and F(36, 2) == 18                  # p24: B 36 h, A 18 h
# tricks
assert F(10 * 15, 15 - 10) == 30
assert F(1, 8) - F(3, 26) == F(1, 104)

concept = (
    "A tank is filled by some pipes and emptied by others. A pipe that **fills** is an *inlet*. "
    "A pipe or a leak that **empties** is an *outlet*.\n\n"
    "Treat it exactly like a time-and-work question. Inlets do positive work, outlets do negative work. "
    "The quickest method: take the tank's capacity as the **LCM of all the times**, so every pipe's speed "
    "becomes a whole number of units per hour."
)

notes = r"""### The basic idea
Every question gives you pipes and the time each one takes on its own.

- An **inlet** fills the tank. Count its work as **plus (+)**.
- An **outlet** or a **leak** empties the tank. Count its work as **minus (−)**.
- "A fills the tank in 6 hours" means A fills $\frac{1}{6}$ of the tank every hour.

> **Rule:** Fill = plus, empty = minus. Write the sign next to every pipe before you calculate anything.

### The LCM method (use it every time)
Fractions like $\frac{1}{12} + \frac{1}{18}$ are slow and easy to get wrong. Give the tank a number of units instead.

1. Tank capacity = LCM of all the given times.
2. Speed of each pipe = capacity ÷ its time (units per hour).
3. Net speed = inlets added, outlets subtracted.
4. Time = capacity ÷ net speed.

> **Example:** A fills a tank in 12 hours, B in 18 hours. Tank = LCM(12, 18) = 36 units. A fills 3 units/hour, B fills 2 units/hour. Together: 5 units/hour, so $36 \div 5 = 7.2$ hours = **7 hours 12 minutes**.

### When one pipe empties the tank
Use the same method. Just subtract the emptying pipe.

A fills in 6 hours, B empties in 9 hours. Tank = 18 units. A = +3, B = −2, so net = +1 unit/hour. The tank fills in **18 hours**.

For exactly one filling pipe (a hours) and one emptying pipe (b hours):
$$T = \frac{a \times b}{b - a}$$
Check: $\frac{6 \times 9}{9 - 6} = 18$ hours.

> **Watch:** If the emptying pipe is faster, the net speed is negative. A full tank will empty; an empty tank will never fill.

### Pipes opened or closed in between
Split the question into stages. The tank only cares how much water is already in it.

1. Stage 1: water filled = speed × time.
2. Water still needed = capacity − water filled.
3. Stage 2: water still needed ÷ new net speed.

A (10 h) and B (15 h) run for 2 hours. Tank = 30 units, speed 5, so 10 units are filled and 20 are left. Now a drain C (30 h) opens: net speed = 5 − 1 = 4. The rest takes 5 hours, so the total is **7 hours**.

> **Watch:** Read the last line carefully. Some questions ask for the *extra* time (5 hours), others for the *total* time (7 hours).

### Finding the leak
"A tank normally fills in 8 hours. Because of a leak, it now takes 10 hours. How long will the leak take to empty the full tank?"

Tank = LCM(8, 10) = 40 units. Normal speed = 5, speed with the leak = 4. The difference, 1 unit/hour, is the leak. So the leak empties the tank in **40 hours**.

> **Tip:** Leak time = $\frac{t_1 \times t_2}{t_2 - t_1}$ where $t_1$ is the normal time and $t_2$ the slower time: $\frac{8 \times 10}{2} = 40$.

### Pipes opened one after the other
Some questions open the pipes turn by turn, one hour each. Treat one full round as a single unit of time.

A fills in 4 hours, B in 6 hours. They are opened alternately for one hour each, starting with A. Tank = 12 units, A = 3, B = 2, so one round (2 hours) fills 5 units. After 2 rounds (4 hours) 10 units are filled and 2 are left. It is A's turn: 2 units at 3 per hour take $\frac{2}{3}$ hour = 40 minutes. Total = **4 hours 40 minutes**.

> **Watch:** Before counting the last round, check whether the tank gets full *during* the round. Stop there.

### When the answer is in litres
If one pipe's speed is given in litres, the capacity is a real number. Write every pipe's speed in litres per hour and solve for the capacity.

A leak empties a full tank in 6 hours. An inlet that fills 4 litres a minute (240 litres an hour) is opened, and now the full tank empties in 8 hours. Leak − inlet = capacity ÷ 8:
$$\frac{C}{6} - 240 = \frac{C}{8} \Rightarrow \frac{C}{24} = 240 \Rightarrow C = 5760 \text{ litres}$$
"""

formulas = [
    {"name": "Net speed", "tex": r"\text{net} = (\text{inlets}) - (\text{outlets})", "note": "Speeds in units per hour, with tank = LCM of the times."},
    {"name": "Time to fill", "tex": r"T = \frac{\text{capacity}}{\text{net speed}}"},
    {"name": "Two inlets", "tex": r"T = \frac{a b}{a + b}", "note": "Both pipes fill."},
    {"name": "One inlet, one outlet", "tex": r"T = \frac{a b}{b - a}", "note": "a = filling time, b = emptying time, b > a."},
    {"name": "Leak time from two fill times", "tex": r"T_{\text{leak}} = \frac{t_1 t_2}{t_2 - t_1}", "note": "t₁ = normal time, t₂ = time with the leak."},
    {"name": "Stage method", "tex": r"t_2 = \frac{\text{capacity} - \text{speed}_1 \times t_1}{\text{speed}_2}"},
]

tricks = [
    {
        "title": "One inlet, one outlet: multiply over subtract",
        "body": "For one filling pipe and one emptying pipe, time = product ÷ difference. No LCM needed.",
        "example": {
            "q": "A pipe fills a tank in 10 hours. A leak empties the full tank in 15 hours. With both open, how long does the tank take to fill?",
            "steps": [r"Product = $10 \times 15 = 150$.", r"Difference = $15 - 10 = 5$.", r"Time = $150 \div 5 = 30$ hours."],
            "answer": "30 hours",
        },
    },
    {
        "title": "Leak from two fill times",
        "body": "The leak is the only thing that changed, so the drop in speed belongs to the leak. Use product ÷ difference of the two fill times.",
        "example": {
            "q": "A cistern fills in 8 hours. Because of a leak it takes 8 hours 40 minutes. The leak alone can empty the full cistern in:",
            "steps": [r"8 h 40 min = $\frac{26}{3}$ hours.", r"Leak speed = $\frac{1}{8} - \frac{3}{26} = \frac{13 - 12}{104} = \frac{1}{104}$ tank per hour.", "So the leak empties the tank in 104 hours."],
            "answer": "104 hours",
        },
    },
    {
        "title": "Check the options before finishing",
        "body": "Filling pipes together are always faster than the fastest pipe alone. Adding an outlet always makes it slower than the inlets alone. Use this to cut two options in a few seconds.",
    },
]

mistakes = [
    {"wrong": "Adding the emptying pipe's speed as if it fills the tank.", "right": "Put a minus sign in front of every outlet or leak before adding."},
    {"wrong": r"Using $\frac{ab}{a+b}$ for one filling and one emptying pipe.", "right": r"That formula is for two inlets. For fill + empty use $\frac{ab}{b-a}$."},
    {"wrong": "Giving the stage-2 time when the question asks for the total time.", "right": "Underline the last line: extra time or total time. Add the stages if it says total."},
    {"wrong": "Forgetting the tank is already part-full when a new pipe is opened.", "right": "Find the water still needed first, then divide by the new speed."},
    {"wrong": "In alternate-pipe questions, counting full rounds past the point where the tank is full.", "right": "Before each hour, check whether the water left is less than that pipe fills in an hour."},
    {"wrong": "Mixing minutes and hours (8 h 40 min taken as 8.4 hours).", "right": r"Convert first: 40 minutes = $\frac{2}{3}$ hour, so 8 h 40 min = $\frac{26}{3}$ hours."},
]

revision = [
    "Inlet = plus, outlet or leak = minus.",
    "Tank = LCM of the times; speed = tank ÷ time.",
    r"Two inlets: $\frac{ab}{a+b}$. One inlet, one outlet: $\frac{ab}{b-a}$.",
    "Stages: water filled so far, water left, then divide by the new speed.",
    r"Leak time = $\frac{t_1 t_2}{t_2 - t_1}$.",
    "Alternate pipes: count full rounds, then check the last round hour by hour.",
    "Net speed zero or negative: an empty tank never fills.",
]

def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}

patterns = [
    pat("tw-p9", "Two or three filling pipes together", "very common",
        "All the pipes fill the same tank. Each pipe's time is given, and the time with all of them open is asked.",
        r"\frac{1}{T} = \frac{1}{T_1} + \frac{1}{T_2} + \frac{1}{T_3}",
        ["Take tank = LCM of the times.", "Find each pipe's speed = tank ÷ its time.", "Add the speeds.", "Time = tank ÷ total speed."],
        "Each pipe adds its own share of water every hour, so the shares simply add up.",
        "Three pipes can fill a tank in 20, 30 and 60 minutes. If all three are opened together, the tank fills in:",
        ["Tank = LCM(20, 30, 60) = 60 units.", "Speeds: 3, 2 and 1 units per minute.", "Total speed = 6 units per minute.", r"Time = $60 \div 6 = 10$ minutes."],
        "10 minutes"),
    pat("tw-p10", "Filling and emptying pipes open together", "very common",
        "At least one pipe fills and at least one pipe (or a leak) empties, all at the same time.",
        r"\text{net} = \sum \text{inlets} - \sum \text{outlets}",
        ["Mark each pipe + (fills) or − (empties).", "Take tank = LCM of the times.", "Net speed = inlets − outlets.", "Time = tank ÷ net speed."],
        "The emptying pipe removes water while the others add it, so its speed cancels part of theirs.",
        "Pipes A and B fill a tank in 12 hours and 15 hours. Pipe C empties it in 20 hours. If all three are opened together, the tank fills in:",
        ["Tank = LCM(12, 15, 20) = 60 units.", "A = +5, B = +4, C = −3.", "Net speed = 6 units per hour.", r"Time = $60 \div 6 = 10$ hours."],
        "10 hours"),
    pat("tw-p11", "Find the leak from two fill times", "common",
        "\"It normally fills in t hours, but because of a leak it takes longer.\" The leak's own emptying time is asked.",
        r"T_{\text{leak}} = \frac{t_1 t_2}{t_2 - t_1}",
        ["Take tank = LCM of the normal time and the slower time.", "Normal speed − slower speed = speed of the leak.", "Leak time = tank ÷ leak speed."],
        "The only difference between the two cases is the leak, so the lost speed is the leak's speed.",
        "A pipe fills a tank in 6 hours. Because of a leak at the bottom, it takes 8 hours. How long will the leak take to empty the full tank?",
        ["Tank = LCM(6, 8) = 24 units.", "Normal speed = 4, speed with the leak = 3.", "Leak speed = 1 unit per hour.", r"Leak time = $24 \div 1 = 24$ hours."],
        "24 hours"),
    pat("tw-p12", "A pipe is opened or closed in between", "common",
        "Pipes run for some time, then a pipe is added or removed. The remaining time or the total time is asked.",
        r"t_2 = \frac{\text{capacity} - \text{speed}_1 \times t_1}{\text{speed}_2}",
        ["Stage 1: water filled = speed × time.", "Water still needed = tank − water filled.", "Stage 2: divide what is left by the new net speed.", "Add the stages if the total time is asked."],
        "The tank does not care how the water got there. Each stage is a fresh, smaller question.",
        "Pipes A and B fill a tank in 12 hours and 16 hours. Both are opened for 4 hours. Then a drain that can empty the full tank in 24 hours is also opened. In how many more hours will the tank be full?",
        ["Tank = LCM(12, 16, 24) = 48 units. A = 4, B = 3, drain = −2.", r"First 4 hours: $7 \times 4 = 28$ units, so 20 units are left.", "New net speed = 7 − 2 = 5 units per hour.", r"More time = $20 \div 5 = 4$ hours."],
        "4 more hours (8 hours in total)"),
    pat("tw-p21", "Pipes opened one after the other", "occasional",
        "The pipes are opened in turns, one hour (or one minute) each: \"alternately\" or \"A, then B, then A…\".",
        None,
        ["Take tank = LCM of the times.", "Water filled in one round = sum of the speeds in that round.", "Count the full rounds that fit without filling the tank.", "Finish the last part pipe by pipe; stop the moment the tank is full."],
        "The pattern repeats every round, so full rounds can be counted in one step. Only the last round needs care.",
        "Pipe A fills a tank in 3 hours and pipe B in 4 hours. They are opened alternately for one hour each, starting with A. In how much time will the tank be full?",
        ["Tank = LCM(3, 4) = 12 units. A = 4, B = 3.", "One round (A then B, 2 hours) = 7 units.", "After 1 round: 7 units in 2 hours, 5 left.", "A's hour adds 4 (3 hours, 1 left). B needs $\\frac{1}{3}$ hour = 20 minutes for the last unit."],
        "3 hours 20 minutes"),
    pat("tw-p22", "Tank capacity in litres", "common",
        "One pipe's speed is given in litres per minute or per hour, and the tank's capacity is asked.",
        r"\frac{C}{t_{\text{out}}} - \text{inlet (L/h)} = \frac{C}{t_{\text{net}}}",
        ["Change every speed to the same unit (litres per hour).", "Write each pipe's speed with C as the capacity, e.g. C/5.", "Make an equation from the net speed.", "Solve for C."],
        "A speed in litres fixes the size of the tank, so the capacity is a real number, not LCM units.",
        "A leak can empty a full tank in 5 hours. An inlet pipe that fills 3 litres a minute is opened, and now the full tank empties in 20 hours. What is the capacity of the tank?",
        ["Inlet = 3 × 60 = 180 litres per hour.", r"Leak − inlet = net emptying: $\frac{C}{5} - 180 = \frac{C}{20}$.", r"$\frac{C}{5} - \frac{C}{20} = \frac{3C}{20} = 180$.", r"$C = 180 \times \frac{20}{3} = 1200$ litres."],
        "1200 litres"),
    pat("tw-p23", "When was a pipe closed?", "occasional",
        "Two pipes start together, one is closed after some time, and the tank still fills in a given total time. The closing time is asked.",
        None,
        ["Take tank = LCM of the times.", "The pipe that was never closed works for the whole time: find its water.", "The rest of the water came from the closed pipe.", "Its working time = its water ÷ its speed."],
        "Working backwards from the finished tank is faster than guessing the closing time.",
        "Pipes A and B can fill a tank in 20 minutes and 30 minutes. Both are opened together, but A is closed after some time. The tank is full in 18 minutes. After how many minutes was A closed?",
        ["Tank = LCM(20, 30) = 60 units. A = 3, B = 2 per minute.", r"B works all 18 minutes: $2 \times 18 = 36$ units.", "A filled the other 60 − 36 = 24 units.", r"A worked $24 \div 3 = 8$ minutes."],
        "After 8 minutes"),
    pat("tw-p24", "One pipe is faster than the other", "common",
        "The question compares the pipes (\"twice as fast\", \"takes 5 hours more\") and gives only the time together.",
        None,
        ["Turn the comparison into speeds, e.g. twice as fast → speeds 2 and 1.", "Tank = speed together × time together.", "Each pipe's time = tank ÷ its speed."],
        "Once speeds are in a ratio, the tank size follows from the time together and everything else is division.",
        "Pipe A is twice as fast as pipe B. Together they fill a tank in 12 hours. How long will B alone take?",
        ["Speeds: A = 2, B = 1 unit per hour; together 3.", r"Tank = $3 \times 12 = 36$ units.", r"B alone = $36 \div 1 = 36$ hours (A alone = 18 hours)."],
        "36 hours"),
]

# Inline fractions render tiny; use \dfrac anywhere a formula sits inside a sentence.
dfrac = lambda x: x.replace(r"\frac", r"\dfrac")
mistakes = [{k: dfrac(v) for k, v in m.items()} for m in mistakes]
revision = [dfrac(r) for r in revision]

data = json.loads(TOPIC.read_text(encoding="utf-8"))
sub = next(s for s in data["subtopics"] if s["id"] == "tw-pipes")
old_ids = {p["id"] for p in sub.get("patterns", [])}
assert old_ids <= {p["id"] for p in patterns}, "never drop a pattern id that practice questions may point to"
all_other = {p["id"] for s in data["subtopics"] if s["id"] != "tw-pipes" for p in s.get("patterns", [])}
assert not (all_other & {p["id"] for p in patterns}), "pattern id clash"
assert 2500 <= len(notes) <= 5000, len(notes)
sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
           mistakes=mistakes, revision=revision, patterns=patterns)
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("tw-pipes updated:", len(notes), "chars of notes,", len(patterns), "patterns")
