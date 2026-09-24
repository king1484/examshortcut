"""classification: subtopics classification-idea and word-classification."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P, Q, set_sub, steps  # noqa: E402
from classification_checks import isprime, issq, alt_num, one_breaks, only_fits, alt_letters  # noqa: E402

ODD = "Three of the following four are alike in a certain way and one is different. Find the odd one out."

# ---------------------------------------------------------------- classification-idea
IDEA_NOTES = """### What is classification?
Classification means **putting things into groups**. In the exam it appears as **"odd one out"**: you get four (sometimes five) items. Three of them share one common feature. One item does not. You must pick that one item.

Everyday example: *apple, mango, banana, potato*. Apple, mango and banana are fruits. Potato is a vegetable. So potato is the odd one out. The exam works exactly like this, only the hidden feature is a little harder to see.

### The golden rule: find what the THREE share
Do not hunt for "something strange" in one option. Every option can look strange in some way. Instead, find a rule that **exactly three options obey**. The fourth option, which breaks that rule, is the answer. Say the rule in one short sentence: "these three are fruits", "these three are prime numbers", "in these three the letters jump by +2".

### Levels where the rule can hide
1. **Category** – what kind of thing it is (bird, metal, state, planet).
2. **Function or use** – what it does (input device, writing tool, measuring instrument).
3. **Property** – a quality it has (liquid or solid, living or non-living, natural or man-made).
4. **Number property** – prime, square, cube, multiple of 7, digit sum.
5. **Letter structure** – steps between letters, vowels, opposite letters.
6. **Word structure** – the spelling itself: letters in alphabetical order, double letters, a word that reads the same backwards (palindrome).

### Which level to test first
Test **objective** rules first, because they can be checked with certainty: number properties, letter steps and spelling. Then test function, then category. If a rule gives you **two odd options**, the rule is wrong or too shallow – go one level deeper. Example: 121, 169, 225, 289 are all perfect squares (level 1 gives no answer). Go deeper: 11, 13, 17 are prime but 15 is not, so **225** is the odd one.

### The four question formats
- **Find the odd one out** – the standard form: "Three of the following four are alike... find the one that is different."
- **Find the one that belongs** – three items are given as a group (e.g. *Mercury, Venus, Mars*) and you choose the option that fits the same group (*Jupiter*). This is odd-one-out turned upside down: now three options break the rule and one obeys it.
- **Two-level (tie-break) questions** – all four share a first property; three share a second one.
- **Meaning-free word questions** – the words have no common meaning; the rule sits in the spelling. Example: *BEFIT, GHOST, ALMOST, DREAM* – in the first three the letters are already in A-to-Z order; in DREAM they are not.

### Worked example
Find the odd one: 15, 21, 35, 43.
- Parity: all odd – no help.
- Prime check: 15 = 3 × 5, 21 = 3 × 7, 35 = 5 × 7, but 43 is prime.
- Rule: three are products of two odd primes; 43 is itself prime. Answer **43**.

### Exam habits that save marks
- Write the rule for the three before you mark the answer.
- Check the rule on all four options, not just the one you suspect.
- Use only school-level facts. The exam never needs rare knowledge; if you need a rare fact, you are on the wrong rule.
- In "which belongs to the group" questions, remember the answer is the one that **fits**, not the one that is different.

### Quick revision
| Step | What to do |
|---|---|
| 1 | Read all four items once, fast |
| 2 | Try objective rules: numbers, letter steps, spelling |
| 3 | Then function, property, category |
| 4 | Rule must fit exactly three items |
| 5 | Two odd items? Go one level deeper |
| 6 | "Belongs to the group" = pick the one that FITS |
"""

IDEA_PATTERNS = [
    P("cl-p1", "Standard odd one out (three alike, one different)", "very common",
      "The question says 'three of the following four are alike in a certain way'. The items can be words, numbers or letter groups.",
      "1. Read all four options.\n2. Try objective rules first (number or letter properties), then use, property and category.\n3. Write the rule the three share in one sentence.\n4. Mark the item that breaks it.\n\n**Why it works:** the setter builds the question around one rule that fits exactly three items.",
      "Find the odd one out: Square, Rectangle, Rhombus, Cube.",
      "Square, rectangle and rhombus are **flat (2-D)** shapes. A cube is a **solid (3-D)** shape. Answer: **Cube**."),
    P("cl-p2", "Select the item that belongs to the same group", "common",
      "Three items are given together (for example 'Mercury, Venus, Mars') and you must choose the option that fits with them.",
      "1. Name the group the three given items form.\n2. Test every option against that group.\n3. Exactly one option fits; the other three are outsiders.\n\n**Why it works:** it is odd-one-out turned upside down; the rule of the given three decides.",
      "Mercury, Venus, Mars belong to a group. Which of these also belongs? Moon, Sun, Jupiter, Sirius.",
      "The three are **planets** of our solar system. Moon is a satellite, Sun and Sirius are stars. Answer: **Jupiter**."),
    P("cl-p3", "Two-level (tie-break) odd one out", "common",
      "The first rule you try fits all four items (all squares, all animals, all consecutive letters).",
      "1. Note the property all four share - it cannot decide the answer.\n2. Look one level deeper inside that property (square of what? which kind of animal?).\n3. The item that breaks the deeper rule is the answer.\n\n**Why it works:** setters make the obvious rule common to all four to trap hasty students.",
      "Find the odd one: 121, 169, 225, 289.",
      "All are squares: $11^2, 13^2, 15^2, 17^2$. Level two: 11, 13 and 17 are prime, 15 is not. Answer: **225**."),
    P("cl-p4", "Word-structure (spelling) odd one out", "occasional",
      "The words have no common meaning. The rule is in the spelling: letters in alphabetical order, double letters, palindrome, first and last letter.",
      "1. Check if the letters of each word are in A-to-Z order.\n2. Check for double letters and palindromes (same forwards and backwards).\n3. Check first/last letters and vowel count.\n4. The word that fails the spelling rule is the answer.\n\n**Why it works:** when meaning gives no single odd item, the setter has used the letters themselves.",
      "Find the odd one: LEVEL, RADAR, CIVIC, MOTOR.",
      "LEVEL, RADAR and CIVIC read the same backwards (palindromes). MOTOR backwards is ROTOM. Answer: **MOTOR**."),
]


def idea_questions():
    S = "classification-idea"
    qs = []
    qs.append(Q("classification-idea-p01", f"{ODD}\n\n**Square, Rectangle, Rhombus, Cube**", "Cube",
                ["Square", "Rectangle", "Rhombus"],
                "Square, rectangle and rhombus are **2-D** (flat) shapes. A cube is a **3-D** solid → **Cube**.",
                "Ask 'flat or solid?' - the solid one is out.", "easy", S, "cl-p1", 25))
    qs.append(Q("classification-idea-p02", f"{ODD}\n\n**Delhi, Mumbai, Chennai, Bihar**", "Bihar",
                ["Delhi", "Mumbai", "Chennai"],
                "Delhi, Mumbai and Chennai are **cities**. Bihar is a **state** → **Bihar**.",
                None, "easy", S, "cl-p1", 20))
    items = [15, 21, 35, 43]
    one_breaks(items, lambda n: not isprime(n) and sum(1 for p in (3, 5, 7) if n % p == 0) == 2, 43)
    alt_num(items, 43)
    qs.append(Q("classification-idea-p03", f"{ODD}\n\n**15, 21, 35, 43**", "43", ["15", "21", "35"],
                "15 = 3 × 5, 21 = 3 × 7, 35 = 5 × 7 - each is a product of two odd primes. **43** is itself a prime number → **43**.",
                "Prime check first: only 43 has no small divisor (not divisible by 2, 3, 5).", "medium", S, "cl-p1", 35))
    qs.append(Q("classification-idea-p04",
                "**Mercury, Venus, Mars** belong to a group. Which of the following belongs to the same group?",
                "Jupiter", ["Moon", "Sun", "Sirius"],
                "The three are **planets** of the solar system. Moon is a satellite; Sun and Sirius are stars. Only **Jupiter** is a planet.",
                "Name the group first ('planets'), then pick the only option inside it.", "easy", S, "cl-p2", 25))
    opts = [53, 51, 57, 49]
    only_fits(opts, isprime, 53)
    assert all(isprime(n) for n in (17, 29, 41))
    qs.append(Q("classification-idea-p05",
                "**17, 29, 41** belong to a group. Which of the following numbers belongs to the same group?",
                "53", ["51", "57", "49"],
                "17, 29 and 41 are **prime numbers**. 51 = 3 × 17, 57 = 3 × 19, 49 = 7 × 7 are composite. **53** is prime → **53**.",
                "Digit-sum test kills 51 and 57 (sum 6 and 12, so divisible by 3); 49 = 7². Only 53 survives.", "medium", S, "cl-p2", 35))
    given = ["ACE", "GIK", "MOQ"]
    assert all(steps(w) == [2, 2] for w in given)
    opts = ["SUW", "PRU", "BDG", "HJM"]
    only_fits(opts, lambda w: steps(w) == [2, 2], "SUW")
    qs.append(Q("classification-idea-p06",
                "**ACE, GIK, MOQ** belong to a group. Which letter-cluster belongs to the same group?",
                "SUW", ["PRU", "BDG", "HJM"],
                "In ACE, GIK and MOQ each letter moves **+2** (A→C→E). Steps: SUW (+2, +2) ✓, PRU (+2, +3), BDG (+2, +3), HJM (+2, +3). Answer **SUW**.",
                "Write the step pair under each option; only one copies (+2, +2).", "medium", S, "cl-p2", 40))
    items = [121, 169, 225, 289]
    assert all(issq(n) for n in items)
    one_breaks(items, lambda n: isprime(int(round(n ** 0.5))), 225)
    alt_num(items, 225)
    qs.append(Q("classification-idea-p07", f"{ODD}\n\n**121, 169, 225, 289**", "225", ["121", "169", "289"],
                "All four are perfect squares: 11², 13², 15², 17² - so 'square' cannot decide. Level two: 11, 13 and 17 are **prime**; 15 = 3 × 5 is not → **225**.",
                "All squares? Look at the roots. Also 225 is the only one ending in 5.", "medium", S, "cl-p3", 40))
    qs.append(Q("classification-idea-p08", f"{ODD}\n\n**Cow, Goat, Buffalo, Tiger**", "Tiger",
                ["Cow", "Goat", "Buffalo"],
                "All four are animals (level one gives no answer). Level two: cow, goat and buffalo are **domestic, plant-eating** animals; the tiger is a **wild, flesh-eating** animal → **Tiger**.",
                None, "easy", S, "cl-p3", 25))
    items = ["BCD", "FGH", "JKL", "OPQ"]
    assert all(steps(w) == [1, 1] for w in items)
    one_breaks(items, lambda w: not any(c in "AEIOU" for c in w), "OPQ")
    qs.append(Q("classification-idea-p09", f"{ODD}\n\n**BCD, FGH, JKL, OPQ**", "OPQ", ["BCD", "FGH", "JKL"],
                "All four are three consecutive letters (+1, +1), so steps give no answer. Level two: BCD, FGH, JKL contain **no vowel**; OPQ begins with the vowel **O**. (Also, the first letters B, F, J go +4 each; the next would be N, not O.) → **OPQ**.",
                "Same steps everywhere? Check vowels next.", "hard", S, "cl-p3", 50))
    words = ["BEFIT", "GHOST", "ALMOST", "DREAM"]
    one_breaks(words, lambda w: list(w) == sorted(w), "DREAM")
    qs.append(Q("classification-idea-p10", f"{ODD}\n\n**BEFIT, GHOST, ALMOST, DREAM**", "DREAM",
                ["BEFIT", "GHOST", "ALMOST"],
                "The words share no meaning, so look at spelling. B-E-F-I-T, G-H-O-S-T, A-L-M-O-S-T: letters are already in **alphabetical order**. In DREAM, R comes before E - not in order → **DREAM**.",
                "Scan each word left to right: does every letter come later in A-Z than the one before?", "hard", S, "cl-p4", 50))
    words = ["LEVEL", "RADAR", "CIVIC", "MOTOR"]
    one_breaks(words, lambda w: w == w[::-1], "MOTOR")
    qs.append(Q("classification-idea-p11", f"{ODD}\n\n**LEVEL, RADAR, CIVIC, MOTOR**", "MOTOR",
                ["LEVEL", "RADAR", "CIVIC"],
                "LEVEL, RADAR and CIVIC read the same from both ends (**palindromes**). MOTOR read backwards is ROTOM → **MOTOR**.",
                "Compare first and last letters: M ≠ R ends it at once.", "easy", S, "cl-p4", 25))
    words = ["LETTER", "BALLOON", "COFFEE", "GARDEN"]
    one_breaks(words, lambda w: any(a == b for a, b in zip(w, w[1:])), "GARDEN")
    qs.append(Q("classification-idea-p12", f"{ODD}\n\n**LETTER, BALLOON, COFFEE, GARDEN**", "GARDEN",
                ["LETTER", "BALLOON", "COFFEE"],
                "No common meaning, so check spelling. LETTER has TT, BALLOON has LL and OO, COFFEE has FF and EE - each has a **double letter**. GARDEN has none → **GARDEN**.",
                None, "medium", S, "cl-p4", 35))
    return qs


# ---------------------------------------------------------------- word-classification
WORD_NOTES = """### What is word classification?
You get four words. Three belong to one group; one does not. The group can be a **category** (all birds), a **use** (all writing tools), a **property** (all liquids), a **general-knowledge set** (all state capitals) or a **meaning** (all words meaning 'happy'). The exam needs only school-level knowledge - things taught up to Class 10.

Everyday example: *pen, pencil, chalk, eraser*. Pen, pencil and chalk are used to **write**. An eraser **removes** writing. So the eraser is odd.

### Step-by-step method
1. **Say the most obvious group.** "These are all stationery items." If all four fit, this level gives no answer.
2. **Go one level deeper.** "Which of them write?" Now three fit, one does not.
3. **Check the rule on all four.** If two words break it, choose a different rule.
4. **Prefer the most precise rule.** "Three are metals that are pure elements; brass is a mixture (alloy)" is more precise than "all are shiny".

### The five rule families
**1. Category (biology is the favourite).**
- Bat among birds → bat is a mammal.
- Whale, dolphin, seal are mammals; **shark** is a fish.
- Frog, toad, salamander are amphibians; **lizard** is a reptile.
- Potato, carrot, radish grow under the ground; **tomato** grows above.

**2. Function / use.**
- Thermometer, barometer, hygrometer **measure** something; a microscope **magnifies**.
- Keyboard, mouse, scanner are **input** devices; monitor, printer, speaker are **output** devices.

**3. Property.**
- Liquid vs solid (milk, water, juice vs butter).
- Pure element vs alloy (gold, silver, platinum vs brass, bronze, steel).
- Conductor vs insulator (copper, aluminium vs rubber, wood).

**4. General-knowledge sets.**
- State capitals: Lucknow (Uttar Pradesh), Patna (Bihar), Bhopal (Madhya Pradesh). Indore, Kanpur, Kochi are big cities but **not** capitals.
- Musical instruments: tabla, dholak, mridangam are **percussion** (struck); sitar, veena, violin are **string** instruments.
- SI base units: kilogram (mass), metre (length), second (time). Litre is a common unit of volume but **not** an SI base unit.

**5. Meaning (synonym group).**
Three words mean nearly the same; one means the opposite. *Happy, glad, cheerful* vs **gloomy**. *Abundant, plentiful, ample* vs **scarce**.

### Worked example
Odd one: Thermometer, Barometer, Hygrometer, Microscope.
- Level 1: all are scientific instruments - no answer.
- Level 2: thermometer measures temperature, barometer measures air pressure, hygrometer measures humidity. A microscope does not measure; it makes tiny things look bigger.
- Answer: **Microscope**.

### Traps to avoid
- **Spelling or length traps.** Do not pick a word just because it is longer or starts with a vowel, unless no meaning rule works.
- **Two possible answers.** If both A and B look odd, your rule is too loose. Find the rule that leaves exactly one.
- **Common-use confusion.** A tomato is cooked like a vegetable, but the question's rule may be "grows under the ground". Read the other three words to find the rule.

### Quick revision
| Family | Typical odd one |
|---|---|
| Birds vs mammal | Bat |
| Mammals vs fish | Shark |
| Amphibians vs reptile | Lizard |
| Measuring instruments | Microscope |
| Input devices | Monitor / Printer |
| Pure metals vs alloy | Brass, Bronze, Steel |
| Percussion vs string | Sitar, Veena |
| Synonym group | The antonym |
"""

WORD_PATTERNS = [
    P("cl-p5", "Category break (animals, plants, living things)", "very common",
      "Four names from nature: birds, fish, reptiles, vegetables, trees. One belongs to a different biological group.",
      "1. Name the biological group of each item (mammal, bird, fish, reptile, amphibian).\n2. Three will share a group.\n3. The item from another group is the answer.\n\n**Why it works:** the setter picks a lookalike from a neighbouring group (bat among birds, shark among whales).",
      "Find the odd one: Sparrow, Crow, Parrot, Bat.",
      "Sparrow, crow and parrot are **birds**. A bat is a **mammal** (it feeds its young on milk). Answer: **Bat**."),
    P("cl-p6", "Function / use break", "very common",
      "Four tools, devices or instruments. Three do the same job; one does a different job.",
      "1. Say what each item is used for.\n2. Group the three with the same job.\n3. The item with the different job is odd.\n\n**Why it works:** items from the same place (office, lab, computer) often have different uses.",
      "Find the odd one: Pen, Pencil, Chalk, Eraser.",
      "Pen, pencil and chalk are used to **write**. An eraser **removes** writing. Answer: **Eraser**."),
    P("cl-p7", "Property break (state, material, natural/man-made)", "common",
      "All four are the same kind of thing, but differ in a property such as solid/liquid, pure/mixed, natural/man-made.",
      "1. Confirm the obvious category fits all four.\n2. Check properties: state of matter, element or mixture, conductor or insulator, living or non-living.\n3. The item with the different property is the answer.\n\n**Why it works:** when category is common to all, the setter has used a property.",
      "Find the odd one: Gold, Silver, Platinum, Brass.",
      "Gold, silver and platinum are **pure metals (elements)**. Brass is an **alloy** of copper and zinc. Answer: **Brass**."),
    P("cl-p8", "General-knowledge set (capitals, instruments, units)", "common",
      "Words from a GK list: cities, state capitals, musical instruments, units of measurement, planets.",
      "1. Recall the school-level fact for each word.\n2. Find the set three belong to (state capitals, percussion instruments, SI base units).\n3. The word outside that set is odd.\n\n**Why it works:** the odd word is from the same topic but not from the same list.",
      "Find the odd one: Lucknow, Patna, Bhopal, Indore.",
      "Lucknow, Patna and Bhopal are **state capitals** (UP, Bihar, MP). Indore is a large city of MP but not its capital. Answer: **Indore**."),
    P("cl-p9", "Meaning group (synonym set with one opposite)", "common",
      "Four adjectives or verbs; three mean nearly the same thing.",
      "1. Find the common meaning of most words.\n2. The word with the opposite (or unrelated) meaning is odd.\n\n**Why it works:** three synonyms form the group; the antonym is planted as the outsider.",
      "Find the odd one: Happy, Glad, Cheerful, Gloomy.",
      "Happy, glad and cheerful all mean **joyful**. Gloomy means sad. Answer: **Gloomy**."),
]


def word_questions():
    S = "word-classification"
    qs = []
    qs.append(Q("word-classification-p01", f"{ODD}\n\n**Whale, Shark, Dolphin, Seal**", "Shark",
                ["Whale", "Dolphin", "Seal"],
                "Whale, dolphin and seal are **mammals** - they breathe air with lungs and feed their young on milk. The shark is a **fish** (it breathes through gills) → **Shark**.",
                "All live in water - so 'water animal' is not the rule; ask 'mammal or fish?'", "medium", S, "cl-p5", 35))
    qs.append(Q("word-classification-p02", f"{ODD}\n\n**Potato, Carrot, Radish, Tomato**", "Tomato",
                ["Potato", "Carrot", "Radish"],
                "Potato, carrot and radish are parts that **grow under the ground**. A tomato grows **above the ground** on the plant → **Tomato**.",
                None, "easy", S, "cl-p5", 25))
    qs.append(Q("word-classification-p03", f"{ODD}\n\n**Frog, Toad, Salamander, Lizard**", "Lizard",
                ["Frog", "Toad", "Salamander"],
                "Frog, toad and salamander are **amphibians** (they live on land and in water and lay soft eggs in water). A lizard is a **reptile** with dry, scaly skin → **Lizard**.",
                None, "hard", S, "cl-p5", 40))
    qs.append(Q("word-classification-p04", f"{ODD}\n\n**Thermometer, Barometer, Hygrometer, Microscope**", "Microscope",
                ["Thermometer", "Barometer", "Hygrometer"],
                "Thermometer measures temperature, barometer measures air pressure, hygrometer measures humidity - all **measure** a quantity. A microscope **magnifies** small objects → **Microscope**.",
                "'-meter' words measure; the odd one does a different job.", "medium", S, "cl-p6", 35))
    qs.append(Q("word-classification-p05", f"{ODD}\n\n**Pen, Pencil, Chalk, Eraser**", "Eraser",
                ["Pen", "Pencil", "Chalk"],
                "Pen, pencil and chalk are used to **write**. An eraser **removes** writing → **Eraser**.",
                None, "easy", S, "cl-p6", 20))
    qs.append(Q("word-classification-p06", f"{ODD}\n\n**Keyboard, Scanner, Microphone, Printer**", "Printer",
                ["Keyboard", "Scanner", "Microphone"],
                "Keyboard, scanner and microphone send data **into** the computer (input devices). A printer gives data **out** on paper (output device) → **Printer**.",
                "Input or output? Data going in vs data coming out.", "medium", S, "cl-p6", 30))
    qs.append(Q("word-classification-p07", f"{ODD}\n\n**Gold, Silver, Platinum, Brass**", "Brass",
                ["Gold", "Silver", "Platinum"],
                "Gold, silver and platinum are **pure metals (elements)**. Brass is an **alloy** - a mixture of copper and zinc → **Brass**.",
                None, "medium", S, "cl-p7", 35))
    qs.append(Q("word-classification-p08", f"{ODD}\n\n**Milk, Water, Juice, Butter**", "Butter",
                ["Milk", "Water", "Juice"],
                "Milk, water and juice are **liquids**. Butter is a **solid** at room temperature → **Butter**.",
                None, "easy", S, "cl-p7", 20))
    qs.append(Q("word-classification-p09", f"{ODD}\n\n**Tabla, Mridangam, Dholak, Sitar**", "Sitar",
                ["Tabla", "Mridangam", "Dholak"],
                "Tabla, mridangam and dholak are **percussion** instruments - played by striking with hands. The sitar is a **string** instrument → **Sitar**.",
                "Struck or plucked? The plucked one is out.", "medium", S, "cl-p8", 30))
    qs.append(Q("word-classification-p10", f"{ODD}\n\n**Kilogram, Metre, Second, Litre**", "Litre",
                ["Kilogram", "Metre", "Second"],
                "Kilogram (mass), metre (length) and second (time) are **SI base units**. The litre is a unit of volume that is **not** an SI base unit → **Litre**.",
                None, "hard", S, "cl-p8", 40))
    qs.append(Q("word-classification-p11", f"{ODD}\n\n**Lucknow, Patna, Bhopal, Indore**", "Indore",
                ["Lucknow", "Patna", "Bhopal"],
                "Lucknow (Uttar Pradesh), Patna (Bihar) and Bhopal (Madhya Pradesh) are **state capitals**. Indore is a big city of Madhya Pradesh but not its capital → **Indore**.",
                None, "medium", S, "cl-p8", 30))
    qs.append(Q("word-classification-p12", f"{ODD}\n\n**Happy, Glad, Cheerful, Gloomy**", "Gloomy",
                ["Happy", "Glad", "Cheerful"],
                "Happy, glad and cheerful all mean **joyful**. Gloomy means **sad** → **Gloomy**.",
                None, "easy", S, "cl-p9", 20))
    qs.append(Q("word-classification-p13", f"{ODD}\n\n**Abundant, Plentiful, Ample, Scarce**", "Scarce",
                ["Abundant", "Plentiful", "Ample"],
                "Abundant, plentiful and ample all mean **more than enough**. Scarce means **too little** → **Scarce**.",
                None, "medium", S, "cl-p9", 30))
    return qs


def apply(d):
    set_sub(d, "classification-idea", notes=IDEA_NOTES, patterns=IDEA_PATTERNS)
    set_sub(d, "word-classification", notes=WORD_NOTES, patterns=WORD_PATTERNS)
    return idea_questions() + word_questions()
