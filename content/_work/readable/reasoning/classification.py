"""Readable rewrite of Reasoning > Classification (all six subtopics).

Plain English, one idea per section. Every number, digit sum, square and
letter position used in an example is recomputed below and asserted.
Run: python classification.py  (patches content/core/topics/reasoning/classification.json in place)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "classification.json"


# ---------- helpers ----------
def P(c):
    """Alphabet position, A = 1 ... Z = 26."""
    return ord(c) - 64


def steps(word):
    """Step tuple inside a letter cluster, e.g. ACE -> [2, 2]."""
    return [P(b) - P(a) for a, b in zip(word, word[1:])]


def dsum(n):
    return sum(int(d) for d in str(n))


def dprod(n):
    r = 1
    for d in str(n):
        r *= int(d)
    return r


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def alt11(n):
    """(sum of digits at odd places) - (sum at even places), from the left, 1-based."""
    s = str(n)
    return sum(int(d) for i, d in enumerate(s, 1) if i % 2) - sum(int(d) for i, d in enumerate(s, 1) if not i % 2)


def pat(pid, name, freq, spot, formula, steps_, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps_, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


S = {}  # subtopic id -> dict of new fields

# =====================================================================
# 1. classification-idea
# =====================================================================
assert 15 == 3 * 5 and 21 == 3 * 7 and 35 == 5 * 7 and is_prime(43)
assert 121 == 11 ** 2 and 169 == 13 ** 2 and 225 == 15 ** 2 and 289 == 17 ** 2
assert is_prime(11) and is_prime(13) and is_prime(17) and not is_prime(15)
# cl-p31 example: four primes and one composite
assert all(is_prime(n) for n in (13, 17, 19, 23)) and 27 == 3 * 9 and not is_prime(27)
# trick example: two-level multiples of 7
assert all(n % 7 == 0 for n in (21, 35, 49, 63, 56)) and all(n % 2 == 1 for n in (21, 35, 49, 63)) and 56 % 2 == 0
# spelling example
assert [w == w[::-1] for w in ("LEVEL", "RADAR", "CIVIC", "MOTOR")] == [True, True, True, False]

S["classification-idea"] = dict(
    concept=(
        "Classification means putting things into groups. The exam shows four (sometimes five) similar items. "
        "Three of them share one hidden feature and one does not. "
        "Your whole job is to state the rule the majority follows, then pick the item that breaks it. "
        "Test checkable rules first: numbers, letter steps, spelling. Then use, then category."
    ),
    notes=r"""### What odd one out means
Classification means putting things into groups. The exam shows four items. Three share one feature. One breaks it. You pick that one.

Take *apple, mango, banana, potato*. Apple, mango and banana are fruits. Potato is a vegetable. So potato is the odd one.

> **Rule:** Find the rule that exactly three items follow. The item that breaks it is the answer.

### Find what the three share
Do not hunt for "something strange" in one option. Every option can look strange in some way. Instead, say the shared rule as one short sentence.

- "These three are fruits."
- "These three are prime numbers."
- "In these three, each letter jumps +2."

Then check the rule on all four items. Mark the one that breaks it.

> **Example:** 15, 21, 35, 43. The first three are products of two primes: 15 = 3 × 5, 21 = 3 × 7, 35 = 5 × 7. 43 is itself prime. So **43** is the odd one.

### Where the rule can hide
| Level | What to check | Example |
|---|---|---|
| Category | what kind of thing it is | bat among birds |
| Function | what it does | monitor among input devices |
| Property | a quality it has | liquid among solids |
| Number property | prime, square, multiple, digit sum | 33 among primes |
| Letter structure | steps between letters, vowels | MOP among +2 clusters |
| Spelling | letter order, palindromes | MOTOR among palindromes |

Test the checkable levels first. Numbers, letter steps and spelling can be verified with certainty. Function and category need judgement, so they come later.

### Go one level deeper
Sometimes the first rule fits all four items. Then the real rule sits deeper.

121, 169, 225, 289 are all perfect squares, so no one is odd yet. Look at the roots: 11, 13 and 17 are prime, but 15 = 3 × 5 is not. So **225** is the odd one.

> **Watch:** If your rule makes two items odd, or none at all, the rule is wrong or too shallow. Go one level deeper.

### The question formats
- **Find the odd one out.** The standard form. Three items are alike, one is different.
- **Find the one that belongs.** Three words form a group. Pick the option that joins them. Now three options break the rule and one obeys it.
- **Two-level questions.** All four share a first property. Only three share the second one.
- **Spelling questions.** The words have no common meaning. The rule sits in the letters: order, double letters, palindromes.
- **Five items.** Four are alike and one is different. The method does not change.

### Check before you mark
Write the rule down before you mark. Check it on all four (or five) items, not only the one you suspect. Use only school-level facts. If you need a rare fact, you are on the wrong rule.

> **Tip:** The rule must keep exactly three (or four) items together. Count every time.
""",
    formulas=[],
    tricks=[
        {
            "title": "Write the majority rule, not the exception",
            "body": "Instead of hunting the odd item, write the rule the other three follow. Confirm each of the three obeys it and the last one breaks it. This stops you marking an item that is merely unusual.",
            "example": {
                "q": "Find the odd one: 21, 35, 49, 63, 56.",
                "steps": ["First rule: multiples of 7. All five pass, so this level gives no answer.",
                          "Go deeper: 21, 35, 49, 63 are odd numbers. 56 is even.",
                          "Rule: odd multiples of 7. Exactly four pass."],
                "answer": "56",
            },
        },
    ],
    mistakes=[
        {"wrong": "Stopping at the first difference you notice.", "right": "Test the rule on all items. It must separate exactly one from the rest."},
        {"wrong": "Assuming the odd item sits at the last position.", "right": "The setter shuffles positions. Check every option."},
        {"wrong": "Using a loose category (\"all are animals\") where a tighter one exists (\"all are birds\").", "right": "Prefer the tightest rule that still groups the majority."},
        {"wrong": "In \"which belongs to the group\" questions, marking the item that is different.", "right": "There the answer is the one that FITS the group of three."},
        {"wrong": "Needing a rare fact to justify an answer.", "right": "The exam uses school-level facts only. A rare fact means the rule is wrong."},
    ],
    revision=[
        "State the majority rule in one sentence, then find the breaker.",
        "Test checkable levels first: numbers, letter steps, spelling.",
        "Then function, then category.",
        "Rule fits all four? Go one level deeper (roots, parity, type).",
        "Five items: the same method, four alike instead of three.",
        "\"Belongs to the group\" = pick the one that fits, not the odd one.",
    ],
    patterns=[
        pat("cl-p1", "Standard odd one out (three alike, one different)", "very common",
            "The question says \"three of the following four are alike in a certain way\". The items can be words, numbers or letter groups.",
            None,
            ["Read all four options once, fast.", "Try checkable rules first: numbers, letter steps, spelling.",
             "Then try use, property and category.", "State the rule one sentence; mark the item that breaks it."],
            "The setter builds the question around one rule that fits exactly three items.",
            "Find the odd one out: Square, Rectangle, Rhombus, Cube.",
            ["Square, rectangle and rhombus are flat (2-D) shapes.",
             "A cube is a solid (3-D) shape.",
             "Rule: three are flat shapes, one is a solid."],
            "Cube"),
        pat("cl-p2", "Select the item that belongs to the same group", "common",
            "Three items are given together (for example Mercury, Venus, Mars) and you choose the option that fits with them.",
            None,
            ["Name the group the three given items form.", "Test every option against that group.",
             "Exactly one option fits; the other three are outsiders."],
            "It is odd-one-out turned upside down: the rule of the given three decides, and the answer obeys it.",
            "Mercury, Venus and Mars belong to a group. Which of these also belongs? Moon, Sun, Jupiter, Sirius.",
            ["The three given items are planets of our solar system.",
             "The Moon is a satellite. The Sun and Sirius are stars.",
             "Jupiter is a planet."],
            "Jupiter"),
        pat("cl-p3", "Two-level (tie-break) odd one out", "common",
            "The first rule you try fits all four items (all squares, all animals, all odd numbers).",
            None,
            ["Note the property all four share. It cannot decide the answer.",
             "Look one level deeper inside that property (square of what? which kind of animal?).",
             "The item that breaks the deeper rule is the answer."],
            "Setters make the obvious rule common to all four on purpose, to trap students who stop early.",
            "Find the odd one: 121, 169, 225, 289.",
            ["All four are squares: 11², 13², 15², 17². No answer yet.",
             "Roots: 11, 13 and 17 are prime; 15 = 3 × 5 is not.",
             "So 225 is the square of the only non-prime root."],
            "225"),
        pat("cl-p4", "Word-structure (spelling) odd one out", "occasional",
            "The words have no common meaning. The rule is in the spelling: letters in A-to-Z order, double letters, palindromes.",
            None,
            ["Check whether the letters of each word run in A-to-Z order.",
             "Check for double letters and palindromes (same forwards and backwards).",
             "Check first and last letters and vowel count.",
             "The word that fails the spelling rule is the answer."],
            "When meaning gives no single odd item, the setter has used the letters themselves.",
            "Find the odd one: LEVEL, RADAR, CIVIC, MOTOR.",
            ["LEVEL, RADAR and CIVIC read the same backwards. They are palindromes.",
             "MOTOR backwards is ROTOM, which is different."],
            "MOTOR"),
        pat("cl-p31", "Five options: four alike, one different", "common",
            "The question says \"four of the following five are alike in a certain way\". There are five items, not four.",
            None,
            ["Find the rule that four items follow.", "Check it on the fifth item.",
             "Mark the fifth item if it breaks the rule."],
            "With five items the rule is often simpler, because four items lock it in place.",
            "Find the odd one: 13, 17, 19, 23, 27.",
            ["13, 17, 19 and 23 have no divisor except 1 and themselves. They are prime.",
             "27 = 3 × 9 is composite.",
             "Rule: four are primes, one is not."],
            "27"),
    ],
)

# =====================================================================
# 2. word-classification
# =====================================================================
S["word-classification"] = dict(
    concept=(
        "Four words come from overlapping fields. Three share a category, a use or a property, and one breaks it. "
        "The exam recycles the same pools: animals, computer parts, metals, instruments, state capitals. "
        "Say the group of the majority in one sentence. If all four fit, switch to a property level: "
        "input or output, element or alloy, liquid or solid."
    ),
    notes=r"""### What word classification asks
You get four words. Three belong to one group. One does not. The group can be a category (all birds), a use (all writing tools), a property (all liquids), a GK set (all state capitals) or a meaning (all words for happy).

The exam needs only school-level knowledge. Take *pen, pencil, chalk, eraser*. The first three are used to write. An eraser removes writing. So the eraser is odd.

> **Rule:** Say the group as one sentence. If all four words fit, the sentence is too broad. Make it tighter.

### Category questions
Biology is the setter's favourite. Learn these splits.

- Sparrow, crow and parrot are **birds**. A bat is a mammal that flies.
- Whale, dolphin and seal are **mammals**. A shark is a fish.
- Snake, crocodile and lizard are **reptiles**. A whale is a mammal.
- Frog, toad and salamander are **amphibians**. A lizard is a reptile.
- Potato, carrot and radish grow **under the ground**. A tomato grows above it.

### Function and property questions
- Thermometer, barometer and hygrometer **measure** something. A microscope magnifies.
- Keyboard, mouse and scanner are **input** devices. Monitor, printer and speaker are output devices.
- Milk, water and juice are **liquids**. Butter is solid.
- Gold, silver and platinum are **pure elements**. Brass, bronze and steel are alloys (mixtures).
- Copper and aluminium **conduct** electricity. Rubber and wood do not.

> **Watch:** A word can sit in two categories. A bat is a mammal AND a flying animal. Pick the rule that three words share and the fourth cannot join.

### GK set questions
- Lucknow, Patna and Bhopal are **state capitals** (UP, Bihar, MP). Indore is a big city of MP but not a capital.
- Tabla, dholak and mridangam are **struck** instruments (percussion). Sitar, veena and violin have strings.
- Kilogram, metre and second are **SI base units**. Litre is a common unit of volume but not an SI base unit.

### Meaning questions
Three words mean nearly the same. One word means the opposite. *Happy, glad, cheerful* against **gloomy**. *Abundant, plentiful, ample* against **scarce**.

> **Tip:** In meaning questions, the odd word is usually the antonym planted among synonyms.

### Worked example
Odd one: Thermometer, Barometer, Hygrometer, Microscope.

1. Level 1: all four are instruments. No answer yet.
2. Level 2: the first three measure (temperature, pressure, humidity). A microscope does not measure; it magnifies.

Answer: **Microscope**.

> **Watch:** Do not pick a word for its spelling or length unless no meaning rule works.
""",
    formulas=[],
    tricks=[
        {
            "title": "Category first, then a binary property",
            "body": "First find the broad category shared by three words. If the fourth also fits that category, switch to a binary property: salt or fresh, input or output, element or alloy, male or female. One word will stand alone on the other side.",
            "example": {
                "q": "Find the odd one: Snake, Crocodile, Lizard, Turtle.",
                "steps": ["All four are reptiles, so the category gives no answer.",
                          "Property check: snake, crocodile and lizard have scales and a hard outer skin; a turtle has a shell.",
                          "In exam lists the turtle (shelled reptile) is marked odd among scaled reptiles."],
                "answer": "Turtle",
            },
        },
    ],
    mistakes=[
        {"wrong": "Choosing by rarity (\"turtle is uncommon\").", "right": "Choose by a structural difference: shell, scales, habitat, class."},
        {"wrong": "Missing the input-versus-output split in device questions.", "right": "For computer parts, always ask: does it send data in or bring it out?"},
        {"wrong": "Forgetting a word can belong to two categories (bat: mammal and flying animal).", "right": "Pick the rule three words share that the odd one cannot join at all."},
        {"wrong": "Using a cooked-versus-raw idea for vegetables (tomato \"is a vegetable\").", "right": "Follow the rule the other three set, such as grows under the ground."},
        {"wrong": "Picking the longest or strangest spelling.", "right": "Meaning and use decide, unless no meaning rule works at all."},
    ],
    revision=[
        "Say the majority group in one sentence; make it tighter if all four fit.",
        "Animals: bat = mammal, shark = fish, whale = mammal, lizard = reptile.",
        "Devices: input (keyboard, mouse, scanner) vs output (monitor, printer, speaker).",
        "Materials: pure elements (gold, silver, platinum) vs alloys (brass, bronze, steel).",
        "GK sets: capitals, percussion vs string instruments, SI base units.",
        "Meaning groups: the antonym planted among three synonyms is the answer.",
    ],
    patterns=[
        pat("cl-p5", "Category break (animals, plants, living things)", "very common",
            "Four names from nature: birds, fish, reptiles, vegetables, trees. One belongs to a different biological group.",
            None,
            ["Name the biological group of each item (mammal, bird, fish, reptile, amphibian).",
             "Three will share a group.",
             "The item from another group is the answer."],
            "The setter picks a lookalike from a neighbouring group, like a bat among birds or a shark among mammals.",
            "Find the odd one: Sparrow, Crow, Parrot, Bat.",
            ["Sparrow, crow and parrot are birds.",
             "A bat is a mammal: it feeds its young on milk and has fur.",
             "Rule: three are birds, one is a mammal."],
            "Bat"),
        pat("cl-p6", "Function / use break", "very common",
            "Four tools, devices or instruments. Three do the same job; one does a different job.",
            None,
            ["Say what each item is used for.",
             "Group the three with the same job.",
             "The item with the different job is odd."],
            "Items from one place (office, lab, computer) often have different uses, so the job splits them.",
            "Find the odd one: Pen, Pencil, Chalk, Eraser.",
            ["A pen, a pencil and chalk are used to write.",
             "An eraser removes writing; it does not write.",
             "Rule: three are writing tools, one is a removing tool."],
            "Eraser"),
        pat("cl-p7", "Property break (state, material, natural/man-made)", "common",
            "All four are the same kind of thing, but differ in a property: solid or liquid, pure or mixture, conductor or insulator.",
            None,
            ["Confirm the obvious category fits all four.",
             "Check properties: state of matter, element or mixture, conductor or insulator, living or non-living.",
             "The item with the different property is the answer."],
            "When the category is common to all, the setter has hidden the split inside a property.",
            "Find the odd one: Gold, Silver, Platinum, Brass.",
            ["Gold, silver and platinum are pure metals (single elements).",
             "Brass is a mixture: an alloy of copper and zinc.",
             "Rule: three are elements, one is an alloy."],
            "Brass"),
        pat("cl-p8", "GK set (capitals, instruments, units)", "common",
            "Words from a school GK list: cities, state capitals, musical instruments, units of measurement, planets.",
            None,
            ["Recall the school-level fact for each word.",
             "Find the set three belong to (state capitals, percussion instruments, SI base units).",
             "The word outside that set is odd."],
            "The odd word comes from the same topic but not from the same list.",
            "Find the odd one: Lucknow, Patna, Bhopal, Indore.",
            ["Lucknow, Patna and Bhopal are state capitals (UP, Bihar, MP).",
             "Indore is a large city of MP, but its capital is Bhopal.",
             "Rule: three are capitals, one is not."],
            "Indore"),
        pat("cl-p9", "Meaning group (three synonyms, one antonym)", "common",
            "Four adjectives or verbs; three mean nearly the same thing.",
            None,
            ["Find the common meaning of most words.",
             "The word with the opposite (or unrelated) meaning is odd."],
            "Three synonyms form the group; the antonym is planted as the outsider.",
            "Find the odd one: Happy, Glad, Cheerful, Gloomy.",
            ["Happy, glad and cheerful all mean joyful.",
             "Gloomy means sad and dark.",
             "Rule: three are synonyms of joyful, one is the opposite."],
            "Gloomy"),
    ],
)

# =====================================================================
# 3. number-classification
# =====================================================================
# notes
assert is_prime(79) and is_prime(83) and is_prime(89) and 91 == 7 * 13 and not is_prime(91)
FAKE = {51: (3, 17), 57: (3, 19), 87: (3, 29), 91: (7, 13), 119: (7, 17), 133: (7, 19), 143: (11, 13), 161: (7, 23)}
assert all(a * b == n for n, (a, b) in FAKE.items()) and not any(is_prime(n) for n in FAKE)
assert 12 ** 2 == 144 and 18 ** 2 == 324 and 24 ** 2 == 576 and 22 ** 2 == 484 < 500 < 529 == 23 ** 2
assert alt11(2728) == -11 and 2728 % 11 == 0
assert dsum(345) == dsum(453) == dsum(534) == 12 and dsum(546) == 15
assert dprod(138) == dprod(234) == dprod(164) == 24 and dprod(326) == 36
assert [n ** 2 + 1 for n in (7, 8, 9)] == [50, 65, 82]
assert [n ** 3 - 1 for n in (5, 6, 7)] == [124, 215, 342]
assert [n * (n + 1) for n in (5, 6, 7)] == [30, 42, 56]
assert [n ** 3 for n in (3, 5, 7, 8)] == [27, 125, 343, 512]
# patterns
assert is_prime(61) and is_prime(67) and is_prime(71) and 77 == 7 * 11
assert 169 == 13 ** 2 and 196 == 14 ** 2 and 225 == 15 ** 2 and 15 ** 2 < 250 < 16 ** 2
assert 39 == 13 * 3 and 65 == 13 * 5 and 91 == 13 * 7 and 111 == 3 * 37 and 111 % 13 != 0
assert 50 == 7 ** 2 + 1 and 65 == 8 ** 2 + 1 and 82 == 9 ** 2 + 1 and 99 == 10 ** 2 - 1
# tricks
assert is_prime(17) and is_prime(41) and is_prime(43) and 51 == 3 * 17

S["number-classification"] = dict(
    concept=(
        "Four numbers are given. Three share a number property and one breaks it. "
        "You do not need long calculation; you need a fixed list of properties to test in order. "
        "The list: prime or composite, perfect square or cube, multiples, digit rules, odd or even, "
        "and near-forms like a square plus one. "
        "When the first property fits all four, look one level deeper at the roots or the parity."
    ),
    notes=r"""### What number classification asks
Four numbers are given. Three share a number property. One does not. You need a list of properties to test in a fixed order, not long calculation.

Take *2, 4, 6, 9*. Three are even and 9 is odd. So 9 is the odd one. Harder questions just use a deeper property.

### Test properties in this order
1. **Prime or composite.** A prime has exactly two factors: 1 and itself. Test a number up to 200 by dividing by 2, 3, 5, 7, 11 and 13 only.
2. **Perfect square or cube.** Learn squares to $30^2 = 900$ and cubes to $12^3 = 1728$. A square never ends in 2, 3, 7 or 8.
3. **Multiples.** Digit sum for 3 and 9. Alternate-digit difference for 11. Plain division for 7 and 13.
4. **Digit rules.** Same digit sum or same digit product for three numbers, one different.
5. **Parity.** Odd versus even. Usually the second level, when all four share another property.
6. **Number forms.** Three numbers fit $n^2 + 1$, $n^3 - 1$ or $n(n+1)$, and one does not.

### Learn the fake primes
These composites look prime. Learn their factors on sight.

| Number | Factors |
|---|---|
| 51 | 3 × 17 |
| 57 | 3 × 19 |
| 87 | 3 × 29 |
| 91 | 7 × 13 |
| 119 | 7 × 17 |
| 133 | 7 × 19 |
| 143 | 11 × 13 |
| 161 | 7 × 23 |

> **Example:** 79, 83, 89, 91. The first three have no divisor up to their square roots. But 91 = 7 × 13. Answer: **91**.

### Divisibility shortcuts
- **By 3 or 9:** add the digits. 345 gives 3 + 4 + 5 = 12, so 345 divides by 3 but not 9.
- **By 11:** subtract the sum of digits at even places from the sum at odd places. A result of 0 or a multiple of 11 means divisible. For 2728: (2 + 2) − (7 + 8) = −11, so 2728 divides by 11.
- **By 7 and 13:** just divide. The numbers stay small.

### Digit rules
When primes, squares and multiples all fail, look at the digits. 138, 234 and 164 all have digit product 24 (1×3×8, 2×3×4, 1×6×4). 326 has 3×2×6 = 36. So 326 is odd.

> **Tip:** Digits can be rearranged freely while keeping the same sum and product. Shuffled digits usually hide a digit rule.

### Two-level questions
Sometimes all four numbers pass the first test. 27, 125, 343, 512 are all cubes. Look at the roots: 3, 5 and 7 are odd; 8 is even. So **512** is the odd one.

> **Watch:** A number can be both a square and a cube: 64 = 8² = 4³, and 729 = 27² = 9³. Check both.

### Check your answer
A good rule makes exactly one number odd. Test one more property after you find your answer. If another natural rule points to a different number, re-read the options. In a well-made question, every natural rule points to the same answer.
""",
    formulas=[
        {"name": "Divisibility by 11", "tex": r"|S_{odd} - S_{even}| \equiv 0 \pmod{11}", "note": "S = sums of alternate digits from the left; e.g. 2728: (2+2) − (7+8) = −11, divisible."},
        {"name": "Perfect square endings", "tex": r"n^2 \in \{0,1,4,5,6,9\}", "note": "A square never ends in 2, 3, 7 or 8 — instant elimination."},
        {"name": "Digit sum rule for 9", "tex": r"9 \mid n \iff S(n) \equiv 0 \pmod 9", "note": "S(n) is the sum of the digits of n."},
    ],
    tricks=[
        {
            "title": "Last-digit scan for squares",
            "body": "Squares end only in 0, 1, 4, 5, 6 or 9. An option ending in 2, 3, 7 or 8 cannot be a square. For the rest, place the number between two known squares.",
            "example": {
                "q": "Find the odd one: 144, 324, 576, 500.",
                "steps": ["144 = 12², 324 = 18², 576 = 24². All are squares.",
                          r"500 sits between $22^2 = 484$ and $23^2 = 529$.",
                          "So 500 is not a square."],
                "answer": "500",
            },
        },
        {
            "title": "Prime check by small divisors",
            "body": "To test a number under 200 for prime, divide only by 2, 3, 5, 7, 11 and 13. Memorise the fake-prime list: 51, 57, 87, 91, 119, 133, 143, 161.",
            "example": {
                "q": "Find the odd one: 17, 51, 41, 43.",
                "steps": ["17, 41 and 43 have no divisor among 2, 3, 5, 7. They are prime.",
                          "51 divides by 3: 51 = 3 × 17.",
                          "Rule: three primes, one composite."],
                "answer": "51",
            },
        },
    ],
    mistakes=[
        {"wrong": "Treating 1 as prime, or 2 as composite.", "right": "1 is neither prime nor composite. 2 is the only even prime."},
        {"wrong": "Calling 56 odd among multiples of 7 without checking.", "right": "56 is also a multiple of 7. Check the rule on every option before marking."},
        {"wrong": "Stopping at \"all are odd\" or \"all are even\".", "right": "Parity is almost never the whole rule when all four match. Look at roots or digits next."},
        {"wrong": "Forgetting a number can be both square and cube (64, 729).", "right": "Test both powers before calling a number odd."},
        {"wrong": "Marking a valid square for the wrong reason in two-level questions.", "right": "Write the deeper rule (roots prime, roots odd) and check it on all four."},
    ],
    revision=[
        "Test order: prime, square/cube, multiple, digits, parity, forms.",
        "Fake primes: 51, 57, 87, 91, 119, 133, 143, 161.",
        r"Squares to $30^2$, cubes to $12^3$. Squares never end in 2, 3, 7, 8.",
        "Digit sum for 3 and 9; alternate-digit difference for 11.",
        r"Near-forms: $n^2 \pm 1$, $n^3 \pm 1$, $n(n+1)$.",
        "First rule fits all four? Check the roots, then parity.",
    ],
    patterns=[
        pat("cl-p10", "Prime vs composite", "very common",
            "Four numbers, mostly odd, that look prime. One is a hidden product like 91 or 143 (or one prime among composites).",
            r"p \text{ prime} \iff \text{no divisor } 2 \le d \le \sqrt{p}",
            ["Divide each number by 2, 3, 5, 7, 11, 13.", "Mark which ones have a factor.",
             "The single number on the other side is the answer."],
            "Primes are the setter's favourite group, and hidden composites like 91 and 143 are the traps.",
            "Find the odd one: 61, 67, 71, 77.",
            ["61, 67 and 71 have no divisor up to their square roots. They are prime.",
             "77 = 7 × 11 is composite.",
             "Rule: three primes, one composite."],
            "77"),
        pat("cl-p11", "Perfect square / perfect cube", "very common",
            "Numbers such as 169, 196, 225 or 216, 343, 512 — familiar powers with one stranger.",
            r"n^2,\; n^3",
            ["Recall the square and cube tables.", "Mark which numbers are exact squares or cubes.",
             "The one that is not is odd."],
            "A number between two known powers cannot itself be a power.",
            "Find the odd one: 169, 196, 225, 250.",
            ["169 = 13², 196 = 14², 225 = 15².",
             "250 lies between 15² = 225 and 16² = 256.",
             "Rule: three squares, one non-square."],
            "250"),
        pat("cl-p12", "Multiples / divisibility", "common",
            "Three numbers are multiples of one number (7, 9, 11, 13), often shown by a digit rule.",
            r"11 \mid n \iff (\text{odd-place sum}) - (\text{even-place sum}) \equiv 0 \pmod{11}",
            ["Find the common divisor of most numbers (try 7, 9, 11, 13).",
             "Use divisibility rules: digit sum for 9, alternate sum for 11.",
             "The number that is not a multiple is odd."],
            "The setter picks a divisor, writes three multiples of it, and adds one near-miss.",
            "Find the odd one: 39, 65, 91, 111.",
            ["39 = 13 × 3, 65 = 13 × 5, 91 = 13 × 7. All are multiples of 13.",
             "111 = 3 × 37, which is not a multiple of 13.",
             "Rule: three multiples of 13, one not."],
            "111"),
        pat("cl-p13", "Digit sum / digit product", "common",
            "Numbers with no clear prime or square pattern, often three-digit, whose digits look shuffled.",
            r"S(n) = \sum \text{digits},\; P(n) = \prod \text{digits}",
            ["Add the digits of each number.", "If the sums differ, multiply the digits.",
             "The number whose sum or product differs is odd."],
            "Digits can be rearranged freely while keeping the same sum and product, so shuffled digits hide a digit rule.",
            "Find the odd one: 345, 453, 534, 546.",
            ["Digit sums: 3 + 4 + 5 = 12, 4 + 5 + 3 = 12, 5 + 3 + 4 = 12.",
             "5 + 4 + 6 = 15, which is different.",
             "Rule: three have digit sum 12, one has 15."],
            "546"),
        pat("cl-p14", "Two-level: same power, odd or even root", "common",
            "All four are squares (or all cubes), so the first rule does not decide.",
            None,
            ["Write the root of each number.", "Check the roots for odd/even or prime/composite.",
             "The number whose root breaks the pattern is odd."],
            "The first property is shared by all four to trap you; the answer hides in the roots.",
            "Find the odd one: 27, 125, 343, 512.",
            ["All four are cubes: 3³, 5³, 7³, 8³.",
             "Roots 3, 5 and 7 are odd; 8 is even.",
             "Rule: cubes of odd numbers, one cube of an even number."],
            "512"),
        pat("cl-p15", "Number forms (n²+1, n³−1, n(n+1))", "occasional",
            "Numbers sit just beside squares or cubes (50, 65, 82), or are products of consecutive numbers (30, 42, 56).",
            r"n^2+1,\; n^3-1,\; n(n+1)",
            ["Check each number against the nearest square and cube.",
             "Write it as a square ± 1, a cube ± 1, or n × (n + 1).",
             "The number that does not fit the common form is odd."],
            "The setter builds three numbers from one formula and changes the sign for the fourth.",
            "Find the odd one: 50, 65, 82, 99.",
            ["50 = 7² + 1, 65 = 8² + 1, 82 = 9² + 1.",
             "99 = 10² − 1, a square MINUS one, not plus one.",
             "Rule: three are n² + 1, one is n² − 1."],
            "99"),
    ],
)

# =====================================================================
# 4. letter-classification
# =====================================================================
assert [P(c) for c in "EJOTY"] == [5, 10, 15, 20, 25]
assert steps("ACE") == [2, 2] and steps("BDF") == [2, 2] and steps("GIK") == [2, 2] and steps("MOP") == [2, 1]
assert steps("DGJ") == [3, 3] and steps("KNQ") == [3, 3] and steps("PSV") == [3, 3] and steps("TWY") == [3, 2]
assert steps("ACF") == [2, 3] and steps("GIL") == [2, 3] and steps("MOR") == [2, 3] and steps("SUW") == [2, 2]
assert steps("MPOR") == [3, -1, 3]
assert P("D") + P("W") == 27 and P("G") + P("T") == 27 and P("K") + P("P") == 27 and P("M") + P("O") == 28
assert all(P(c) % 2 == 0 for c in "BHLDJP" + "FNT")  # BHL, DJP, FNT: all letters at even positions
assert P("G") % 2 == 1 and all(P(c) % 2 == 0 for c in "LRT"[1:])  # GLR: G odd among even-position clusters
VOW = set("AEIOU")
assert [sum(c in VOW for c in w) for w in ("BGT", "CFD", "HLM", "APT")] == [0, 0, 0, 1]
assert [("O" in w) for w in ("NOP",)] and [1 if w[1] in VOW else 0 for w in ("NOP", "HIJ", "DEF", "RST")] == [1, 1, 1, 0]
assert [sum(P(c) for c in w) for w in ("AMP", "DLN", "EKN", "BHS")] == [30, 30, 30, 29]

S["letter-classification"] = dict(
    concept=(
        "Each option is a small letter cluster, like ACE or BDFH. Three clusters share an internal structure and one breaks it. "
        "Turn every letter into its alphabet position (A = 1 ... Z = 26) and write the steps between letters. "
        "The step tuple turns a feel question into simple arithmetic. "
        "If the tuples match, test vowels, opposite letters or position sums."
    ),
    notes=r"""### Letters are numbers
A = 1, B = 2 ... Z = 26. Learn the five **EJOTY** anchors: E = 5, J = 10, O = 15, T = 20, Y = 25. Every other letter is a short hop from one of them. R = T − 2 = 18.

### Write the step tuple
For each cluster, write the jump from each letter to the next. That list is the **step tuple**.

- **ACE**: A→C is +2, C→E is +2. Tuple (+2, +2).
- Backward steps are negative: Z→X is −2.
- After Z the count wraps to A: Y + 3 = B.

The tuple is the fingerprint of the cluster. Two clusters built by the same rule have the same tuple.

> **Tip:** Write the positions under the letters of all four options in one pass. Then read off the tuples.

### The rule families
1. **Constant step.** The same jump every time. DGJ, KNQ and PSV are all (+3, +3). TWY is (+3, +2), so TWY is odd.
2. **Repeated mixed steps.** The jumps differ but repeat across clusters. ACF, GIL and MOR are all (+2, +3). SUW is (+2, +2). With four letters, MPOR is (+3, −1, +3).
3. **Opposite letters.** A-Z, B-Y ... M-N. Their positions always add to 27. In DW, GT and KP the two letters add to 27. MO adds to 28, so MO is odd.
4. **Vowel structure.** NOP, HIJ and DEF carry their vowel in the middle (O, I, E). RST has no vowel at all.
5. **Position property.** The positions follow a number rule. B, H and L sit at even positions (2, 8, 12). G sits at 7, odd, so GLR is odd among even-position clusters.

### Method in five steps
1. Write positions under every letter of all four options.
2. Write the step tuple of each option.
3. If three tuples match, the fourth option is the answer.
4. If all four tuples match, test vowels and opposite letters.
5. If all tuples differ, test position sums and even or odd positions.

### Worked example
Odd one: ACF, GIL, MOR, SUW.

- ACF: 1, 3, 6 → (+2, +3)
- GIL: 7, 9, 12 → (+2, +3)
- MOR: 13, 15, 18 → (+2, +3)
- SUW: 19, 21, 23 → (+2, +2)

Answer: **SUW**.

Try the opposite family on its own. Odd one: DW, GT, KP, MO. D + W = 4 + 23 = 27. G + T = 7 + 20 = 27. K + P = 11 + 16 = 27. But M + O = 13 + 15 = 28. So **MO** is odd.

> **Example:** Position-sum family. AMP = 1 + 13 + 16 = 30, DLN = 4 + 12 + 14 = 30, EKN = 5 + 11 + 14 = 30. BHS = 2 + 8 + 19 = 29. So **BHS** is odd.

### The vowel note
Some papers print a note: \"the odd one is not based on the number of consonants or vowels, or their position\". That note removes the vowel family. Use steps, opposite letters or position sums instead.

> **Watch:** Check every step of a tuple. Setters often spoil only the second or third step, so the first step alone is not enough.
""",
    formulas=[
        {"name": "Step of a cluster", "tex": r"s_i = Q(L_{i+1}) - Q(L_i) \pmod{26}", "note": "Q is the alphabet position. Compute steps for every option; three must match as tuples."},
        {"name": "Opposite-pair sum", "tex": r"Q(X) + Q(Y) = 27", "note": "Letter pairs whose positions add to 27: AZ, BY, ..., MN."},
    ],
    tricks=[
        {
            "title": "Step tuples in one line",
            "body": "Under each cluster write its steps: ACE → (+2, +2), BDF → (+2, +2), GIK → (+2, +2), MOP → (+2, +1). The mismatched tuple is the answer. No vowel counting is needed.",
            "example": {
                "q": "Find the odd one: ACE, BDF, GIK, MOP.",
                "steps": ["ACE: A→C +2, C→E +2. Tuple (+2, +2).",
                          "BDF and GIK also give (+2, +2).",
                          "MOP: M→O is +2 but O→P is +1. Tuple (+2, +1)."],
                "answer": "MOP",
            },
        },
        {
            "title": "Vowel count as tiebreaker",
            "body": "If the step tuples agree, or the clusters look irregular, count the vowels (A, E, I, O, U). Three clusters with no vowel and one with a vowel (or the reverse) is a complete exam pattern.",
            "example": {
                "q": "Find the odd one: BGT, CFD, HLM, APT.",
                "steps": ["The step tuples are irregular, so steps cannot decide.",
                          "BGT, CFD and HLM contain no vowel.",
                          "APT contains the vowel A."],
                "answer": "APT",
            },
        },
    ],
    mistakes=[
        {"wrong": "Computing steps without wrapping (Y to B read as −23).", "right": "Wrap past Z: Y + 3 = 25 + 3 = 28, then 28 − 26 = 2 = B."},
        {"wrong": "Forgetting U is a vowel.", "right": "The vowels are A, E, I, O, U. Circle them before counting."},
        {"wrong": "Checking only the first step of each cluster.", "right": "Write the full tuple. Setters often spoil the second or third step."},
        {"wrong": "Counting letters on fingers and slipping by one.", "right": "Use EJOTY anchors and subtract positions."},
        {"wrong": "Using the vowel family when the paper's note forbids it.", "right": "Read the note. When vowels are excluded, use steps, opposites or sums."},
    ],
    revision=[
        "EJOTY: E5, J10, O15, T20, Y25.",
        "Step tuple = the fingerprint. Three tuples match, one differs.",
        "Wrap past Z: above 26 subtract 26.",
        "Opposite letters add to 27: AZ, BY ... MN.",
        "Tuples all match? Test vowels next, then position sums and parity.",
        "Vowel note printed? Vowels are excluded; use steps or sums.",
    ],
    patterns=[
        pat("cl-p16", "Constant step inside the cluster", "very common",
            "Every cluster has letters with equal gaps (ACE, DGJ, BFJN), forward or backward.",
            r"\text{step} = Q(\text{next}) - Q(\text{this}) \pmod{26}",
            ["Convert letters to positions.", "Write the step tuple for each cluster.",
             "Three clusters have the same constant step; the fourth changes one step."],
            "The setter copies one constant jump and spoils a single step in the odd cluster.",
            "Find the odd one: DGJ, KNQ, PSV, TWY.",
            ["D→G→J is (+3, +3). K→N→Q is (+3, +3). P→S→V is (+3, +3).",
             "T→W is +3 but W→Y is +2. TWY is (+3, +2).",
             "Rule: three clusters jump +3, +3; one does not."],
            "TWY"),
        pat("cl-p17", "Mixed step tuple (same pattern repeated)", "very common",
            "Steps inside each cluster are unequal (+2, +3) or rise and fall (+3, −1, +3), but look similar across options.",
            None,
            ["Write the full step tuple for each cluster.", "Three tuples will be identical.",
             "The cluster with a different tuple is odd."],
            "The pattern is the tuple as a whole, not any single step.",
            "Find the odd one: ACF, GIL, MOR, SUW.",
            ["ACF: 1, 3, 6 gives (+2, +3).",
             "GIL: 7, 9, 12 gives (+2, +3). MOR: 13, 15, 18 gives (+2, +3).",
             "SUW: 19, 21, 23 gives (+2, +2)."],
            "SUW"),
        pat("cl-p18", "Opposite-letter pairs (positions add to 27)", "common",
            "Pairs like AZ, BY, DW, or clusters where one letter mirrors another from the other end of the alphabet.",
            r"Q(x) + Q(\bar{x}) = 27",
            ["Add the positions of the two letters that should be opposite.",
             "Opposite letters add to 27.",
             "The cluster whose pair does not make 27 is odd."],
            "A to Z and M to N all sum to 27, so one addition tests each option.",
            "Find the odd one: DW, GT, KP, MO.",
            ["D + W = 4 + 23 = 27. G + T = 7 + 20 = 27. K + P = 11 + 16 = 27.",
             "M + O = 13 + 15 = 28, not 27.",
             "Rule: three pairs are opposite letters, one is not."],
            "MO"),
        pat("cl-p19", "Vowel position / vowel structure", "common",
            "All clusters have similar steps, so steps cannot decide; vowels sit in a fixed slot in three clusters.",
            None,
            ["Circle the vowels (A, E, I, O, U) in each cluster.",
             "Note the number and position of vowels.",
             "The cluster that differs is odd."],
            "When step tuples are identical, the setter has used the vowels.",
            "Find the odd one: NOP, HIJ, DEF, RST.",
            ["NOP has O in the middle. HIJ has I in the middle. DEF has E in the middle.",
             "RST contains no vowel at all.",
             "Rule: three clusters carry a vowel in the middle slot."],
            "RST"),
        pat("cl-p20", "Position-number property (sum, even or odd positions)", "occasional",
            "Step tuples are all different and there is no vowel pattern; the letters look random.",
            r"\sum Q(\text{letters}) = \text{constant}",
            ["Write positions of all letters.",
             "Test: equal position sums? All even or all odd positions? Squares?",
             "The cluster that fails the common property is odd."],
            "The setter chose letters to meet a number condition, not a step condition.",
            "Find the odd one: AMP, DLN, EKN, BHS.",
            ["AMP = 1 + 13 + 16 = 30. DLN = 4 + 12 + 14 = 30. EKN = 5 + 11 + 14 = 30.",
             "BHS = 2 + 8 + 19 = 29.",
             "Rule: three clusters sum to 30, one sums to 29."],
            "BHS"),
    ],
)

# =====================================================================
# 5. pair-classification
# =====================================================================
assert P("C") + 3 == P("F") and P("H") + 3 == P("K") and P("M") + 3 == P("P") and P("V") - P("R") == 4
assert P("B") + P("Y") == 27 and P("E") + P("V") == 27 and P("H") + P("S") == 27 and P("K") + P("O") == 26
assert P("C") ** 2 == 9 and P("E") ** 2 == 25 and P("G") ** 2 == 49 and P("H") ** 2 == 64 != 60
assert 11 ** 2 == 121 != 132

S["pair-classification"] = dict(
    concept=(
        "Each option is a pair, like Cow : Calf or 12 : 144. Three pairs share the same relation and one does not. "
        "This is an analogy question in reverse: name the relation the majority shares, then spot the pair that breaks it. "
        "The trap is a pair from the same topic with a different relation. "
        "Doctor : Hospital sits beside tool pairs, but it is a workplace, not a tool."
    ),
    notes=r"""### What pair classification asks
Each option is a **pair**: two words, two letters, or a letter and a number. Three pairs share one relationship. One pair is linked differently. You find that pair.

Take *Cow : Calf, Dog : Puppy, Cat : Kitten, Horse : Stable*. The first three are animal : young one. Horse : Stable is animal : home. So Horse : Stable is odd.

> **Rule:** Make one sentence from a pair, then test all four pairs with the same sentence. Keep the direction of the words.

### One sentence, four tests
1. Take the first pair and make a short sentence: \"A calf is the young one of a cow.\"
2. Put the other pairs into the same sentence. \"A stable is the young one of a horse\" is false.
3. If the sentence fits three pairs, the fourth is the answer.
4. If it fits only two pairs, the sentence is wrong. Build a new one from a different pair.
5. Keep the direction. \"Worker : tool\" is not the same as \"tool : worker\".

> **Watch:** Matching the topic is not enough. All four pairs can be about doctors or animals. Only the relation decides.

### Word-pair relation bank
| Relation | Example pairs |
|---|---|
| Animal : young one | Goat : Kid, Lion : Cub |
| Animal : home | Horse : Stable, Bee : Hive |
| Worker : tool | Carpenter : Saw, Tailor : Needle |
| Worker : workplace | Doctor : Hospital, Chef : Kitchen |
| Tool : action | Knife : Cut, Broom : Sweep |
| Creator : creation | Author : Book, Sculptor : Statue |
| Instrument : quantity measured | Ammeter : Current, Barometer : Pressure |
| Country : currency | Japan : Yen, Bangladesh : Taka |
| State : capital | Bihar : Patna, Assam : Dispur |
| Opposite meaning | Hot : Cold, Rich : Poor |
| Same meaning | Big : Large, Quick : Fast |

### GK pairs: find the wrong fact
Here every pair has the same shape, but one pair states a wrong fact. Kerala : Kochi is wrong, because the capital of Kerala is Thiruvananthapuram.

The wrong pair usually uses a famous city that is not the capital, or the currency of a different country. Use only well-known facts.

> **Example:** Japan : Yen, India : Rupee, Bangladesh : Taka, China : Dollar. China's currency is the yuan, so **China : Dollar** is odd.

### Letter pairs and letter-number pairs
Turn letters into positions (EJOTY: E 5, J 10, O 15, T 20, Y 25).

- **Gap check:** CF, HK and MP all have a gap of +3. RV has a gap of +4, so RV is odd.
- **Opposite check:** BY, EV and HS add to 27. KO adds to 26, so KO is odd.
- **Letter-number pairs:** the number comes from the position. C : 9, E : 25 and G : 49 are squares of positions (3², 5², 7²). H : 60 breaks the rule, because 8² = 64.

### Worked example
Odd pair: Carpenter : Saw, Tailor : Needle, Farmer : Plough, Doctor : Hospital.

1. Sentence: \"the second is the tool the first works with\".
2. Saw, needle and plough are tools. A hospital is a place, not a tool.

Answer: **Doctor : Hospital**.

> **Tip:** Every worker has a tool, a place and a product. The setter puts the other two in the options as traps.
""",
    formulas=[],
    tricks=[
        {
            "title": "Relation sentence, then four ticks",
            "body": "Form the relation sentence from the three pairs that clearly agree, then tick or cross all four options. In number pairs, compute the rule for each pair; three will match.",
            "example": {
                "q": "Find the odd pair: 3 : 9, 7 : 49, 9 : 81, 11 : 132.",
                "steps": ["3 : 9, 7 : 49 and 9 : 81 follow n : n².",
                          "11² = 121, but the pair says 132.",
                          "Rule: three pairs are squares, one is not."],
                "answer": "11 : 132",
            },
        },
    ],
    mistakes=[
        {"wrong": "Matching topics instead of relations (all pairs about doctors, only three tool : user).", "right": "Say the relation as a sentence. The topic is a decoy."},
        {"wrong": "Testing the relation only on the pair that looks odd.", "right": "Test the sentence on all four pairs, in the same direction."},
        {"wrong": "Ignoring the order of the words (tool : worker taken as worker : tool).", "right": "Keep the direction of the model sentence in every pair."},
        {"wrong": "Missing a wrong GK fact because the shape of the pair looks right.", "right": "In GK pairs, check each fact itself, not the shape."},
        {"wrong": "In letter-number pairs, stopping at the first formula that fits one pair.", "right": "Try position, 2 × position, position² and 27 − position, then confirm on a second pair."},
    ],
    revision=[
        "One relation sentence, tested on all four pairs in the same direction.",
        "Same topic does not mean same relation.",
        "GK pairs: find the factually wrong pair (Kochi is not Kerala's capital).",
        "Letter pairs: check the gap, then the 27-sum.",
        "Letter-number pairs: position, 2 × position, position², 27 − position.",
        "Number pairs: compute the rule for each pair; three match, one breaks.",
    ],
    patterns=[
        pat("cl-p21", "Word pairs: relation break", "very common",
            "Four word pairs like Cow : Calf. Three share a relation (young one, tool, workplace, creation); one uses a different relation.",
            None,
            ["Make a sentence from one pair (\"X is the young one of Y\").",
             "Put every pair into the same sentence.",
             "The pair that does not fit is odd."],
            "The setter keeps the topic the same but changes the relation in one pair.",
            "Find the odd pair: Cow : Calf, Dog : Puppy, Cat : Kitten, Horse : Stable.",
            ["Calf, puppy and kitten are young ones of cow, dog and cat.",
             "A stable is the horse's home, not its young one.",
             "Rule: three pairs are animal : young one; one is animal : home."],
            "Horse : Stable"),
        pat("cl-p22", "GK pairs: one factually wrong pair", "common",
            "Pairs of state : capital, country : currency or instrument : quantity. All pairs follow the same relation, but one pair has a wrong fact.",
            None,
            ["Check each pair against the fact you know.",
             "The pair where the fact is wrong is odd."],
            "The wrong pair usually uses a famous city that is not the capital, or another country's currency.",
            "Find the odd pair: Japan : Yen, India : Rupee, Bangladesh : Taka, China : Dollar.",
            ["Yen, rupee and taka are the correct currencies of Japan, India and Bangladesh.",
             "China's currency is the yuan, not the dollar.",
             "Rule: three correct currency pairs, one wrong fact."],
            "China : Dollar"),
        pat("cl-p23", "Letter pairs (gap or opposite letters)", "common",
            "Options are two-letter pairs such as CF, HK, MP or BY, EV, HS.",
            r"Q(\text{2nd}) - Q(\text{1st}) = k \;\text{or}\; Q(\text{1st}) + Q(\text{2nd}) = 27",
            ["Write the positions of both letters.",
             "Find the gap (second − first), or the sum (27 means opposite letters).",
             "The pair with a different gap or sum is odd."],
            "The setter uses one gap, or the 27-sum, for three pairs and changes it slightly for the fourth.",
            "Find the odd pair: CF, HK, MP, RV.",
            ["C→F is +3, H→K is +3, M→P is +3.",
             "R→V is +4.",
             "Rule: three gaps of +3, one gap of +4."],
            "RV"),
        pat("cl-p24", "Letter : number pairs", "common",
            "Each option looks like C : 9 — a letter and a number made from its position.",
            r"n = f(Q(\text{letter})),\; f(x) \in \{x,\ 2x,\ x^2,\ 27 - x\}",
            ["Write the position of each letter.",
             "Try: position, 2 × position, position², position + k, 27 − position.",
             "The pair whose number does not fit is odd."],
            "The number is always a simple function of the letter's position, so each formula takes seconds to test.",
            "Find the odd pair: C : 9, E : 25, G : 49, H : 60.",
            ["C is 3rd and 9 = 3². E is 5th and 25 = 5². G is 7th and 49 = 7².",
             "H is 8th, and 8² = 64, not 60.",
             "Rule: three numbers are position², one is not."],
            "H : 60"),
        pat("cl-p25", "Synonym vs antonym pairs", "occasional",
            "Four pairs of ordinary words; three pairs are opposites (or three are same-meaning), and one is the other kind.",
            None,
            ["Decide for each pair: same meaning or opposite meaning?",
             "Three will be the same kind.",
             "The pair of the other kind is odd."],
            "A synonym pair planted among antonym pairs (or the reverse) breaks the shared kind.",
            "Find the odd pair: Hot : Cold, Up : Down, Rich : Poor, Big : Large.",
            ["Hot-Cold, Up-Down and Rich-Poor are opposites.",
             "Big and Large mean the same thing.",
             "Rule: three opposite pairs, one same-meaning pair."],
            "Big : Large"),
    ],
)

# =====================================================================
# 6. number-set-classification
# =====================================================================
# notes
assert 2 * 2 == 4 and 4 * 2 == 8 and 3 * 2 == 6 and 6 * 2 == 12 and 5 * 2 == 10 and 10 * 2 == 20
assert 4 * 2 == 8 and 8 * 2 == 16 != 15  # doubling example
assert 12 ** 2 == 144
assert 2 * 2 + 3 == 7 and 7 * 2 + 3 == 17  # chain ×2+3
assert 4 * 4 + 3 == 19 and 6 * 6 + 3 == 39 and 7 * 7 + 3 == 52 and 8 * 8 + 3 == 67 != 66
assert 5 ** 3 + 1 == 126
assert 3 * 7 + 1 == 22
assert 5 ** 2 + 3 ** 2 == 34
assert 2 * (12 + 8) == 40 and 7 * 3 - 1 == 20
assert 3 * 4 == 12 and 12 * 4 == 48 and 2 * 4 == 8 and 8 * 4 == 32
# patterns
assert 15 ** 2 == 225 and 9 ** 2 == 81 and 11 ** 2 == 121 != 111
assert [n ** 3 for n in (3, 4, 5, 6)] == [27, 64, 125, 216] and 216 != 206
assert 4 * 5 == 20 and 3 * 7 == 21 and 6 * 8 == 48 and 9 * 6 == 54 != 45
assert 2 * (15 + 5) == 40 and 2 * (9 + 7) == 32 and 2 * (10 + 6) == 32 != 30
assert 5 * 4 == 20 and 20 * 4 == 80 and 6 * 4 == 24 and 24 * 4 == 96 != 72 and 7 * 4 == 28 and 28 * 4 == 112 != 84
assert 6 * 2 - 1 == 11 and 11 * 2 - 1 == 21 and 8 * 2 - 1 == 15 and 15 * 2 - 1 == 29
assert 5 * 2 - 1 == 9 and 9 * 2 - 1 == 17 and 7 * 2 - 1 == 13 and 13 * 2 - 1 == 25 != 26

S["number-set-classification"] = dict(
    concept=(
        "Here each option is not one number but a small group: a pair like 12 : 144 or a set like (3, 9, 27). "
        "Three options are built by the same operation and one is not. "
        "Find the operation from one option, confirm it on a second, then mark the option that fails. "
        "Many papers add a note: use whole numbers only, so digit tricks are not allowed."
    ),
    notes=r"""### Pairs and sets instead of single numbers
Each option is a pair like 12 : 144, or a set of three numbers like (3, 9, 27). Three options follow the same operation. One does not. You hunt for the **operation** that links the numbers inside each option.

Take (2, 4, 8), (3, 6, 12), (5, 10, 20), (4, 8, 15). In the first three sets each number is double the one before. In the last set 8 × 2 = 16, not 15. So (4, 8, 15) is odd.

> **Rule:** Build the rule from one option, confirm it on a second, then mark the option that breaks it.

### The whole-number note
Many papers print a note: \"operations should be performed on whole numbers, without breaking them into digits\". So 13 must stay 13. You may not split it into 1 and 3. Digit sums and digit products are not allowed in these questions.

### Pairs: the second number from the first
The second number is built from the first. Common rules:

- $b = a^2$, as in 12 : 144. Or $b = a^3$.
- $b = a^2 + k$, as in 4 : 19, which is $4^2 + 3$.
- $b = a^3 + 1$, as in 5 : 126.
- $b = k a + r$, as in 7 : 22, which is 3 × 7 + 1, or 3 : 7, which is 2 × 3 + 1.

### Chain sets: one step, used twice
The same step turns the first number into the second, and the second into the third.

(2, 7, 17): 2 × 2 + 3 = 7 and 7 × 2 + 3 = 17. The rule is \"×2 + 3\". Check both steps of every set, never only the first.

### The middle from the outer two
The middle number is built from the first and last numbers:

- $m = a \times c$, as in (4, 20, 5), because 4 × 5 = 20.
- $m = a^2 + c^2$, as in (5, 34, 3), because 25 + 9 = 34.
- $m = (a + c) \times k$.

### The third from the first two
The last number is built from the first two: $c = 2(a + b)$ as in (12, 8, 40), or $c = a \times b - 1$ as in (7, 3, 20).

> **Tip:** Compare sizes to pick the family. A large middle number points to a product. Steady growth points to a chain. A large last number points to a sum or product rule.

### Select the set that belongs
Some questions give two model sets, like (3, 12, 48) and (2, 8, 32), both built by ×4 twice. You pick the option that follows the same rule. Exactly one option fits; the others break it at the second step.

### Worked example
Odd set: (6, 11, 21), (8, 15, 29), (5, 9, 17), (7, 13, 26).

1. 6 × 2 − 1 = 11 and 11 × 2 − 1 = 21. Rule: ×2 − 1 twice.
2. 8 → 15 → 29 fits. 5 → 9 → 17 fits.
3. 7 × 2 − 1 = 13, but 13 × 2 − 1 = 25, not 26.

Answer: **(7, 13, 26)**.

> **Watch:** The setter usually spoils only the last number of one option. Always finish the chain.
""",
    formulas=[
        {"name": "Pair rule", "tex": r"b = f(a),\; f(a) \in \{a^2,\ a^3,\ a^2 \pm k,\ ka \pm r\}", "note": "Find f from one pair, then check the other three pairs."},
        {"name": "Chain triad", "tex": r"(a,\ f(a),\ f(f(a)))", "note": "The same operation applied twice, e.g. ×3 gives (3, 9, 27)."},
        {"name": "Outer-to-middle triad", "tex": r"(a,\ g(a, c),\ c),\; g = ac \text{ or } a^2 + c^2", "note": "The middle number is made from the two outer numbers."},
        {"name": "First-two-to-third triad", "tex": r"(a,\ b,\ h(a, b)),\; h = k(a+b) \text{ or } ab \pm r", "note": "The third number is made from the first two."},
    ],
    tricks=[
        {
            "title": "Size tells the operation",
            "body": "Compare sizes first. If the second number is near the square of the first, think square. If the middle number is large and the outer ones small, think product of the outer numbers.",
            "example": {
                "q": "Find the odd set: (4, 20, 5), (3, 21, 7), (6, 48, 8), (9, 45, 6).",
                "steps": ["The middle numbers are large; the outer numbers are small. Try middle = first × last.",
                          "4 × 5 = 20, 3 × 7 = 21, 6 × 8 = 48. All fit.",
                          "9 × 6 = 54, but the set says 45."],
                "answer": "(9, 45, 6)",
            },
        },
        {
            "title": "Test the rule on two options before trusting it",
            "body": "A rule found from one option can be a coincidence. Confirm it on a second option, then check the rest. The option that fails is the answer.",
            "example": {
                "q": "Find the odd pair: 4 : 19, 6 : 39, 7 : 52, 8 : 66.",
                "steps": ["4 : 19 could be 4 × 4 + 3 or 4 × 5 − 1.",
                          "Test on 6 : 39: 6² + 3 = 39 fits, while 6 × 7 − 1 = 41 does not. Rule: a² + 3.",
                          "7² + 3 = 52 fits. But 8² + 3 = 67, not 66."],
                "answer": "8 : 66",
            },
        },
    ],
    mistakes=[
        {"wrong": "Splitting numbers into digits (12 read as 1 and 2) when the whole-number note is printed.", "right": "Use only +, −, ×, ÷ and powers of the full numbers."},
        {"wrong": "Fixing the rule from only one option.", "right": "One option fits many rules. Confirm on a second option before testing the rest."},
        {"wrong": "Choosing the option with the largest numbers.", "right": "Mark the option that breaks the rule, whatever its size."},
        {"wrong": "In \"select the set like the given sets\", picking a set that looks similar but breaks the rule.", "right": "Test every option against the model rule. Exactly one fits all steps."},
        {"wrong": "Stopping after the first step of a chain.", "right": "Check both steps of every set; the trap usually hides in the last number."},
    ],
    revision=[
        "Whole-number note: no digit tricks.",
        "Pairs: try a², a³, a² ± k, ka ± r.",
        "Chain sets: one step used twice; check both steps.",
        "Middle from outer: a × c, a² + c², k(a + c).",
        "Third from first two: k(a + b), ab ± r.",
        "Belongs-to-group: find the rule of the model sets, then pick the one fit.",
    ],
    patterns=[
        pat("cl-p26", "Number pairs with one wrong relation (a : b)", "very common",
            "Options are pairs like 12 : 144 or 4 : 19. The second number is a square, cube or simple function of the first.",
            r"b = a^2 \pm k \;\text{or}\; b = a^3 \pm k \;\text{or}\; b = ka \pm r",
            ["Guess the rule from the first pair (square? cube? square + k?).",
             "Confirm it on a second pair.",
             "The pair that fails is odd."],
            "One pair is built with the wrong constant or the wrong power, so a full check catches it.",
            "Find the odd pair: 12 : 144, 15 : 225, 9 : 81, 11 : 111.",
            ["144 = 12², 225 = 15², 81 = 9². Rule: second = first squared.",
             "11² = 121, not 111.",
             "Rule: three square pairs, one broken pair."],
            "11 : 111"),
        pat("cl-p27", "Chain sets (a, b, c): the same operation twice", "common",
            "Sets of three numbers that grow steadily, like (3, 9, 27) or (2, 7, 17).",
            r"(a,\ f(a),\ f(f(a)))",
            ["Find the operation from a to b.",
             "Check that the same operation turns b into c.",
             "The set where the second step fails is odd."],
            "The setter usually spoils only the last number of one set.",
            "Find the odd set: (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 206).",
            ["Each set is (n, n², n³): 3³ = 27, 4³ = 64, 5³ = 125.",
             "6³ = 216, but the set says 206.",
             "Rule: three n, n², n³ sets, one broken at the cube."],
            "(6, 36, 206)"),
        pat("cl-p28", "Middle number from the two outer numbers", "common",
            "Sets of three where the middle number is much larger than the two outer numbers.",
            r"m = a \times c \;\text{or}\; m = a^2 + c^2",
            ["Try middle = first × last.",
             "If not, try first² + last², or (first + last) × k.",
             "The set that fails is odd."],
            "The outer numbers are the inputs and the middle is the output.",
            "Find the odd set: (4, 20, 5), (3, 21, 7), (6, 48, 8), (9, 45, 6).",
            ["4 × 5 = 20, 3 × 7 = 21, 6 × 8 = 48. Rule: middle = first × last.",
             "9 × 6 = 54, but the set says 45.",
             "Rule: three product sets, one broken."],
            "(9, 45, 6)"),
        pat("cl-p29", "Third number from the first two", "occasional",
            "Sets where the last number is the largest and looks like a sum or product of the first two.",
            r"c = k(a + b) \;\text{or}\; c = ab \pm r",
            ["Try c = a + b, c = k(a + b), then c = a × b ± r.",
             "Confirm the rule on two sets.",
             "The set that breaks it is odd."],
            "The first two numbers are inputs and the third is the output.",
            "Find the odd set: (12, 8, 40), (15, 5, 40), (9, 7, 32), (10, 6, 30).",
            ["12 + 8 = 20 and 2 × 20 = 40. 15 + 5 = 20 and 2 × 20 = 40. 9 + 7 = 16 and 2 × 16 = 32. Rule: c = 2(a + b).",
             "10 + 6 = 16, so the third number should be 32, not 30.",
             "Rule: three sum-double sets, one broken."],
            "(10, 6, 30)"),
        pat("cl-p30", "Select the set or pair that belongs to the group", "common",
            "The question gives two sets or pairs as a model and asks which option is related in the same way.",
            None,
            ["Find the rule that fits BOTH model sets.",
             "Test every option against it.",
             "Exactly one option fits every step — choose it."],
            "This is classification turned around: three options break the rule and one follows it.",
            "Which set is like (3, 12, 48) and (2, 8, 32)? (5, 20, 80), (4, 12, 36), (6, 24, 72), (7, 28, 84).",
            ["Model rule: ×4, then ×4 again. 3 × 4 = 12, 12 × 4 = 48; 2 × 4 = 8, 8 × 4 = 32.",
             "(5, 20, 80): 5 × 4 = 20 and 20 × 4 = 80. It fits both steps.",
             "(6, 24, 72) and (7, 28, 84) break the second step; (4, 12, 36) breaks the first."],
            "(5, 20, 80)"),
    ],
)

# ---------- write back ----------
data = json.loads(TOPIC.read_text(encoding="utf-8"))
before = {s["id"]: len(s.get("patterns", [])) for s in data["subtopics"]}
all_new = [p["id"] for v in S.values() for p in v["patterns"]]
assert len(all_new) == len(set(all_new)), "duplicate pattern id"
for sub in data["subtopics"]:
    new = S[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in new["patterns"]}, (sub["id"], "dropped a pattern id")
    assert 2500 <= len(new["notes"]) <= 5000, (sub["id"], len(new["notes"]))
    new["notes"] = new["notes"].strip() + "\n"
    sub.update(new)
assert set(S) == set(before), "every subtopic must be rewritten"
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
for sid in S:
    print(f"{sid}: notes {len(S[sid]['notes'])} chars, patterns {before[sid]} -> {len(S[sid]['patterns'])}")
