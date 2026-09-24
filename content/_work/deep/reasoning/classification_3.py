"""classification: pair-classification and new subtopic number-set-classification."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P, Q, set_sub, add_sub, pos  # noqa: E402
from classification_checks import one_breaks, only_fits  # noqa: E402

ODDP = "Three of the following four pairs are alike in a certain way and one is different. Find the odd pair."
NOTE = ("(**NOTE:** Operations should be performed on the whole numbers, without breaking them into their "
        "digits. For example, with 13 you may add, subtract or multiply 13 itself, but you may not split it "
        "into 1 and 3.)")

# ---------------------------------------------------------------- pair-classification
PAIR_NOTES = """### What is pair classification?
Each option is a **pair**: two words, two letters, or a letter and a number, joined by a colon (Cow : Calf). Three pairs are linked by the **same relationship**. One pair is linked in a different way. You must find that pair.

This is really an **analogy question in reverse**. In analogy you copy one relation; here you find the relation three pairs share and spot the pair that breaks it.

Everyday example: *Cow : Calf, Dog : Puppy, Cat : Kitten, Horse : Stable*. The first three are **animal : its young one**. Horse : Stable is **animal : its home**. So Horse : Stable is odd.

### Step-by-step method
1. Take the first pair and make a short sentence: "A calf is the young one of a cow."
2. Put the other pairs into the **same sentence**: "A puppy is the young one of a dog" ✓, "A stable is the young one of a horse" ✗.
3. If the sentence fits three pairs, the fourth is the answer.
4. If the sentence fits only two, your sentence is wrong - make a new sentence from the second pair and try again.
5. Keep the **direction**. "Worker : tool" is not the same as "tool : worker".

### Word-pair relations you must know
| Relation | Example pair |
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
| Word : opposite | Hot : Cold, Rich : Poor |
| Word : same meaning | Big : Large, Quick : Fast |

### General-knowledge pairs
Here the relation is simple (state : capital, country : currency) but **one pair is factually wrong**. Example: Kerala : Kochi - Kochi is a big city, but the capital of Kerala is Thiruvananthapuram. Use only well-known facts; the wrong pair is usually a famous city that is not the capital, or a currency of a different country.

### Letter pairs
Turn letters into positions (A = 1 ... Z = 26; EJOTY: E 5, J 10, O 15, T 20, Y 25).
- **Constant gap:** CF, HK, MP all have gap +3; RV has +4.
- **Opposite letters:** BY, EV, HS add up to 27; KO adds to 26.

### Letter : number pairs
The number is made from the letter's position. C : 9, E : 25, G : 49 use the **square of the position** (3², 5², 7²). H : 60 breaks it (8² = 64). Other common rules: 2 × position, position + constant, reverse position (27 − position).

### Worked example
Odd pair: Carpenter : Saw, Tailor : Needle, Farmer : Plough, Doctor : Hospital.
- Sentence: "A carpenter works **with** a saw" (worker : tool).
- Tailor works with a needle ✓, farmer works with a plough ✓, doctor works with a hospital ✗ - a hospital is where a doctor works.
- Answer: **Doctor : Hospital**.

### Quick revision
- Make one clear sentence from a pair, then test all four pairs.
- Keep the order of the two words the same as in the sentence.
- Similar topic does not mean same relation (Painter : Canvas is creator : surface, not creator : creation).
- Letter pairs: find the gap or check the 27-sum.
- Letter : number pairs: try position, 2 × position, position², 27 − position.
- GK pairs: find the one factually wrong pair.
"""

PAIR_PATTERNS = [
    P("cl-p21", "Word pairs: relation break", "very common",
      "Four word pairs like 'Cow : Calf'. Three share a relation (young one, tool, workplace, creation); one uses a different relation.",
      "1. Make a sentence from one pair ('X is the young one of Y').\n2. Put every pair into the same sentence.\n3. The pair that does not fit is odd.\n\n**Why it works:** the setter keeps the topic the same but changes the relation in one pair.",
      "Find the odd pair: Cow : Calf, Dog : Puppy, Cat : Kitten, Horse : Stable.",
      "Three pairs are **animal : young one**. A stable is the horse's **home**. Answer: **Horse : Stable**."),
    P("cl-p22", "GK pairs: one factually wrong pair", "common",
      "Pairs of state : capital, country : currency or instrument : quantity. All pairs follow the same relation, but one pair has a wrong fact.",
      "1. Check each pair against the fact you know.\n2. The pair where the fact is wrong is odd.\n\n**Why it works:** the wrong pair usually uses a famous city (not the capital) or the currency of another country.",
      "Find the odd pair: Japan : Yen, India : Rupee, Bangladesh : Taka, China : Dollar.",
      "Yen, rupee and taka are the correct currencies. China's currency is the yuan (renminbi), not the dollar. Answer: **China : Dollar**."),
    P("cl-p23", "Letter pairs (gap or opposite letters)", "common",
      "Options are two-letter pairs such as CF, HK, MP or BY, EV, HS.",
      "1. Write positions of both letters.\n2. Find the gap (second − first) or the sum (27 means opposite letters).\n3. The pair with a different gap or sum is odd.\n\n**Why it works:** the setter uses one gap or the 27-sum for three pairs and changes it by one for the fourth.",
      "Find the odd pair: CF, HK, MP, RV.",
      "Gaps: C→F +3, H→K +3, M→P +3, R→V +4. Answer: **RV**.",
      formula=r"Q(\text{2nd}) - Q(\text{1st}) = k \;\text{or}\; Q(\text{1st}) + Q(\text{2nd}) = 27"),
    P("cl-p24", "Letter : number pairs", "common",
      "Each option is like 'C : 9' - a letter and a number made from its position.",
      "1. Write the position of each letter.\n2. Try: position, 2 × position, position², position + k, 27 − position.\n3. The pair whose number does not fit is odd.\n\n**Why it works:** the number is always a simple function of the letter's position.",
      "Find the odd pair: C : 9, E : 25, G : 49, H : 60.",
      "C = 3 → 9 = 3², E = 5 → 25 = 5², G = 7 → 49 = 7². H = 8 → 8² = 64, not 60. Answer: **H : 60**.",
      formula=r"n = f(Q(\text{letter})),\; f(x) \in \{x,\ 2x,\ x^2,\ 27 - x\}"),
    P("cl-p25", "Synonym vs antonym pairs", "occasional",
      "Four pairs of ordinary words; three pairs are opposites (or three are same-meaning), one is the other kind.",
      "1. Decide for each pair: same meaning or opposite meaning?\n2. Three will be the same kind.\n3. The pair of the other kind is odd.\n\n**Why it works:** a synonym pair is planted among antonym pairs (or the reverse).",
      "Find the odd pair: Hot : Cold, Up : Down, Rich : Poor, Big : Large.",
      "Hot-Cold, Up-Down and Rich-Poor are **opposites**. Big and Large mean the **same**. Answer: **Big : Large**."),
]


def pq(qid, items, ans, sol, sc, diff, pat, t, q=None):
    wrong = [x for x in items if x != ans]
    return Q(qid, q or f"{ODDP}\n\n**{', '.join(items)}**", ans, wrong, sol, sc, diff, "pair-classification", pat, t)


def pair_questions():
    qs = []
    qs.append(pq("pair-classification-p01", ["Cow : Calf", "Dog : Puppy", "Cat : Kitten", "Horse : Stable"], "Horse : Stable",
                 "Cow : Calf, Dog : Puppy and Cat : Kitten are **animal : young one**. A stable is where a horse **lives** → **Horse : Stable**.",
                 "Sentence test: 'a stable is the young one of a horse' - false.", "easy", "cl-p21", 25))
    qs.append(pq("pair-classification-p02", ["Carpenter : Saw", "Tailor : Needle", "Farmer : Plough", "Doctor : Hospital"], "Doctor : Hospital",
                 "Carpenter - saw, tailor - needle and farmer - plough are **worker : tool**. A hospital is the doctor's **workplace**, not a tool → **Doctor : Hospital**.",
                 None, "medium", "cl-p21", 30))
    qs.append(pq("pair-classification-p03", ["Pen : Write", "Knife : Cut", "Broom : Sweep", "Needle : Thread"], "Needle : Thread",
                 "Pen - write, knife - cut and broom - sweep are **tool : the action it does**. Thread is not an action; it is used **with** a needle → **Needle : Thread**.",
                 "Second word a verb in three pairs, a noun in one.", "medium", "cl-p21", 30))
    qs.append(pq("pair-classification-p04", ["Bihar : Patna", "Odisha : Bhubaneswar", "Assam : Dispur", "Kerala : Kochi"], "Kerala : Kochi",
                 "Patna, Bhubaneswar and Dispur are the **capitals** of Bihar, Odisha and Assam. The capital of Kerala is **Thiruvananthapuram**; Kochi is a port city → **Kerala : Kochi**.",
                 None, "medium", "cl-p22", 30))
    qs.append(pq("pair-classification-p05", ["Japan : Yen", "India : Rupee", "Bangladesh : Taka", "China : Dollar"], "China : Dollar",
                 "Yen, rupee and taka are the correct currencies of Japan, India and Bangladesh. China uses the **yuan (renminbi)** → **China : Dollar**.",
                 None, "easy", "cl-p22", 25))
    qs.append(pq("pair-classification-p06", ["Thermometer : Temperature", "Barometer : Pressure", "Ammeter : Current", "Hygrometer : Wind speed"],
                 "Hygrometer : Wind speed",
                 "Thermometer measures temperature, barometer measures air pressure, ammeter measures electric current - all correct **instrument : quantity** pairs. A hygrometer measures **humidity**; wind speed is measured by an anemometer → **Hygrometer : Wind speed**.",
                 None, "hard", "cl-p22", 40))
    items = ["CF", "HK", "MP", "RV"]
    one_breaks(items, lambda w: pos(w[1]) - pos(w[0]) == 3, "RV")
    qs.append(pq("pair-classification-p07", items, "RV",
                 "Gaps: C(3)→F(6) +3, H(8)→K(11) +3, M(13)→P(16) +3, R(18)→V(22) **+4** → **RV**.",
                 "Two letters are skipped in three pairs (D E, I J, N O); three are skipped in RV (S T U).", "easy", "cl-p23", 25,
                 q="Three of the following four letter-pairs are alike in a certain way and one is different. Find the odd one.\n\n**CF, HK, MP, RV**"))
    items = ["BY", "EV", "HS", "KO"]
    one_breaks(items, lambda w: pos(w[0]) + pos(w[1]) == 27, "KO")
    qs.append(pq("pair-classification-p08", items, "KO",
                 "Opposite letters add to 27: B + Y = 2 + 25, E + V = 5 + 22, H + S = 8 + 19 - all 27. K + O = 11 + 15 = **26** (K's opposite is P) → **KO**.",
                 "Recall the opposite pairs B-Y, E-V, H-S, K-P.", "medium", "cl-p23", 35,
                 q="Three of the following four letter-pairs are alike in a certain way and one is different. Find the odd one.\n\n**BY, EV, HS, KO**"))
    pairs = [("C", 9), ("E", 25), ("G", 49), ("H", 60)]
    one_breaks(pairs, lambda p: pos(p[0]) ** 2 == p[1], ("H", 60))
    qs.append(pq("pair-classification-p09", ["C : 9", "E : 25", "G : 49", "H : 60"], "H : 60",
                 "C = 3 and 3² = 9; E = 5 and 5² = 25; G = 7 and 7² = 49 - number = **square of the letter's position**. H = 8 and 8² = 64, not 60 → **H : 60**.",
                 None, "medium", "cl-p24", 35))
    pairs = [("B", 4), ("D", 8), ("F", 12), ("J", 18)]
    one_breaks(pairs, lambda p: 2 * pos(p[0]) == p[1], ("J", 18))
    qs.append(pq("pair-classification-p10", ["B : 4", "D : 8", "F : 12", "J : 18"], "J : 18",
                 "B = 2 → 4, D = 4 → 8, F = 6 → 12: number = **2 × position**. J = 10 → should be 20, not 18 → **J : 18**.",
                 "EJOTY: J = 10, so J should pair with 20.", "medium", "cl-p24", 35))
    qs.append(pq("pair-classification-p11", ["Hot : Cold", "Up : Down", "Rich : Poor", "Big : Large"], "Big : Large",
                 "Hot - cold, up - down and rich - poor are **opposites**. Big and large have the **same meaning** → **Big : Large**.",
                 None, "easy", "cl-p25", 20))
    qs.append(pq("pair-classification-p12", ["Brave : Courageous", "Quick : Fast", "Silent : Quiet", "Ancient : Modern"], "Ancient : Modern",
                 "Brave - courageous, quick - fast and silent - quiet are **same-meaning** pairs. Ancient (very old) and modern (new) are **opposites** → **Ancient : Modern**.",
                 None, "medium", "cl-p25", 30))
    return qs


# ---------------------------------------------------------------- number-set-classification (new)
SET_CONCEPT = """Instead of single numbers, each option is a **pair** (12 : 144) or a **set** of three numbers (3, 9, 27). Three options are built by the same operation; one is not. Recent SSC and Railway papers ask this form often, with a note that operations must use the **whole numbers** (no splitting 13 into 1 and 3).

Method: find the operation from the first option (square, ×3 chain, product of outer numbers...), test it on every option, and mark the one that fails."""

SET_FORMULAS = [
    {"name": "Pair rule", "tex": r"b = f(a),\; f(a) \in \{a^2,\ a^3,\ a^2 \pm k,\ ka \pm r\}",
     "note": "Find f from one pair, check the other three."},
    {"name": "Chain triad", "tex": r"(a,\ f(a),\ f(f(a)))", "note": "Same operation applied twice, e.g. ×3: (3, 9, 27)."},
    {"name": "Outer-to-middle triad", "tex": r"(a,\ g(a, c),\ c),\; g = ac \text{ or } a^2 + c^2",
     "note": "Middle number made from the two outer numbers."},
    {"name": "First-two-to-third triad", "tex": r"(a,\ b,\ h(a, b)),\; h = k(a+b) \text{ or } ab \pm r",
     "note": "Third number made from the first two."},
]

SET_TRICKS = [
    {"title": "Size tells the operation",
     "body": "Compare sizes: if b is about a², think square; if c ≈ 3 × b and b ≈ 3 × a, think a ×3 chain; if the middle number is large and the outer ones small, think product of the outer numbers.",
     "example": {"q": "**Q.** Odd set: (4, 20, 5), (3, 21, 7), (6, 48, 8), (9, 45, 6).",
                 "solution": "Middle is big, outer small → try product: 4 × 5 = 20 ✓, 3 × 7 = 21 ✓, 6 × 8 = 48 ✓, 9 × 6 = 54 ≠ 45. Odd set **(9, 45, 6)**."}},
    {"title": "Test the rule on two options before trusting it",
     "body": "A rule found from one option may be a coincidence. Confirm it on a second option, then check the remaining two. The one that fails is the answer.",
     "example": {"q": "**Q.** Odd pair: 4 : 19, 6 : 39, 7 : 52, 8 : 66.",
                 "solution": "4 : 19 could be 4 × 4 + 3 or 4 × 5 − 1. Test on 6 : 39: 6² + 3 = 39 ✓ (6 × 7 − 1 = 41 ✗). Rule a² + 3. 7² + 3 = 52 ✓, 8² + 3 = 67 ≠ 66. Odd pair **8 : 66**."}},
]

SET_MISTAKES = [
    "Splitting numbers into digits (reading 12 as 1 and 2) when the note says to use whole numbers.",
    "Fixing the rule from only one option - a single pair fits many rules.",
    "Choosing the option whose numbers are simply the largest, instead of the one that breaks the rule.",
    "In 'select the set like the given sets' questions, picking a set that is different instead of the one that fits.",
]

SET_NOTES = r"""### What are number-pair and number-set questions?
Here each option is not one number but a small group of numbers: a **pair** like 12 : 144 or a **set** like (3, 9, 27). Three options follow the same operation; one does not. The question is still "find the odd one", but now you look for the **operation** that links the numbers inside each option.

Everyday example: (2, 4, 8), (3, 6, 12), (5, 10, 20), (4, 8, 15). In the first three each number is **double** the previous one. In the last set 8 × 2 = 16, not 15. So (4, 8, 15) is odd.

### The whole-number note
Many papers add: "Operations should be performed on the whole numbers, without breaking them into their digits." This means 13 must be used as 13. You may not treat it as 1 and 3. Rules like "sum of digits" are **not allowed** in such questions.

### Type 1: pairs (a : b)
The second number is made from the first. Common rules:
- $b = a^2$ (12 : 144), $b = a^3$
- $b = a^2 \pm k$ (4 : 19 is $4^2 + 3$)
- $b = a^3 \pm 1$ (5 : 126 is $5^3 + 1$)
- $b = ka \pm r$ (7 : 22 is 3 × 7 + 1)

### Type 2: chain sets (a, b, c)
The same step is used twice: a → b → c. For (2, 7, 17): 2 × 2 + 3 = 7 and 7 × 2 + 3 = 17. So the rule is "×2 + 3". Check the rule on both steps of every set.

### Type 3: middle from the outer numbers (a, m, c)
The middle number is made from the first and last numbers. Common rules: $m = a \times c$ (4, 20, 5), $m = a^2 + c^2$ (5, 34, 3 because 25 + 9 = 34), $m = (a + c) \times k$.

### Type 4: third from the first two (a, b, c)
The last number is made from the first two: $c = 2(a + b)$ as in (12, 8, 40), or $c = a \times b - 1$ as in (7, 3, 20).

### Type 5: select the set that belongs
Two sets are given, for example (3, 12, 48) and (2, 8, 32). You must pick the option that follows the same rule (here ×4 twice). Only one option fits.

### Method
1. Look at sizes to guess the family (squares, product, chain).
2. Write the rule using the first option.
3. Test it on the second option. If it fails, change the rule.
4. Test the remaining options. Exactly one should fail (or, in Type 5, exactly one should fit).

### Worked example
Odd set: (6, 11, 21), (8, 15, 29), (5, 9, 17), (7, 13, 26).
- 6 → 11 is 6 × 2 − 1; 11 → 21 is 11 × 2 − 1. Rule: ×2 − 1 twice.
- 8 → 15 → 29 ✓; 5 → 9 → 17 ✓.
- 7 → 13 ✓ but 13 × 2 − 1 = 25, not 26. Answer **(7, 13, 26)**.

### Quick revision
| Type | Rule to try first | Example |
|---|---|---|
| Pair | $a^2$, $a^3$, $a^2 \pm k$, $ka \pm r$ | 12 : 144 |
| Chain set | same step twice | (2, 7, 17): ×2 + 3 |
| Middle from outer | $a \times c$, $a^2 + c^2$ | (4, 20, 5) |
| Third from first two | $2(a+b)$, $ab - 1$ | (12, 8, 40) |
| Belongs to group | find rule of given sets, pick the fit | (5, 20, 80) |
| Note present | never split into digits | 13 stays 13 |
"""

SET_PATTERNS = [
    P("cl-p26", "Number pairs with one wrong relation (a : b)", "very common",
      "Options are pairs like 12 : 144, 4 : 19. The second number is a square, cube or simple function of the first.",
      "1. Guess the rule from the first pair (square? cube? square + k?).\n2. Confirm on a second pair.\n3. The pair that fails is odd.\n\n**Why it works:** one pair is built with the wrong constant or the wrong power.",
      "Find the odd pair: 12 : 144, 15 : 225, 9 : 81, 11 : 111.",
      "144 = 12², 225 = 15², 81 = 9². 11² = 121, not 111. Answer: **11 : 111**.",
      formula=r"b = a^2 \pm k \;\text{or}\; b = a^3 \pm k \;\text{or}\; b = ka \pm r"),
    P("cl-p27", "Chain sets (a, b, c): same operation twice", "common",
      "Sets of three numbers that grow steadily (3, 9, 27) or (2, 7, 17).",
      "1. Find the operation from a to b.\n2. Check that the same operation turns b into c.\n3. The set where the second step fails is odd.\n\n**Why it works:** the setter usually spoils only the last number of one set.",
      "Find the odd set: (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 206).",
      "Each set is (n, n², n³). 6³ = 216, not 206. Answer: **(6, 36, 206)**.",
      formula=r"(a,\ f(a),\ f(f(a)))"),
    P("cl-p28", "Middle number from the two outer numbers", "common",
      "Sets of three where the middle number is much larger than the two outer numbers.",
      "1. Try middle = first × last.\n2. If not, try first² + last², or (first + last) × k.\n3. The set that fails is odd.\n\n**Why it works:** the outer numbers are the inputs; the middle is the output.",
      "Find the odd set: (4, 20, 5), (3, 21, 7), (6, 48, 8), (9, 45, 6).",
      "4 × 5 = 20, 3 × 7 = 21, 6 × 8 = 48, 9 × 6 = 54 ≠ 45. Answer: **(9, 45, 6)**.",
      formula=r"m = a \times c \;\text{or}\; m = a^2 + c^2"),
    P("cl-p29", "Third number from the first two", "occasional",
      "Sets where the last number is the largest and looks like a sum or product of the first two.",
      "1. Try c = a + b, c = k(a + b), c = a × b ± r.\n2. Confirm the rule on two sets.\n3. The set that breaks it is odd.\n\n**Why it works:** the first two numbers are inputs and the third is the output.",
      "Find the odd set: (12, 8, 40), (15, 5, 40), (9, 7, 32), (10, 6, 30).",
      "c = 2(a + b): 2 × 20 = 40 ✓, 2 × 20 = 40 ✓, 2 × 16 = 32 ✓, 2 × 16 = 32 ≠ 30. Answer: **(10, 6, 30)**.",
      formula=r"c = k(a + b) \;\text{or}\; c = ab \pm r"),
    P("cl-p30", "Select the set / pair that belongs to the given group", "common",
      "The question gives two sets or pairs as a model and asks which option is related in the same way.",
      "1. Find the rule that fits BOTH model sets.\n2. Test every option.\n3. Exactly one option fits - choose it.\n\n**Why it works:** this is classification turned around - three options break the rule, one follows it.",
      "Which set is like (3, 12, 48) and (2, 8, 32)? (5, 20, 80), (4, 12, 36), (6, 24, 72), (7, 28, 84).",
      "Model rule: ×4, ×4. Only (5, 20, 80) fits (20 × 4 = 80). Answer: **(5, 20, 80)**."),
]


def fmt_set(s):
    return "(" + ", ".join(str(x) for x in s) + ")"


def sq(qid, opts, ans, sol, sc, diff, pat, t, q):
    wrong = [x for x in opts if x != ans]
    return Q(qid, q, ans, wrong, sol, sc, diff, "number-set-classification", pat, t)


def set_questions():
    qs = []
    S_ODDPAIR = f"Three of the following four number-pairs are alike in a certain way and one is different. Find the odd pair.\n{NOTE}"
    S_ODDSET = f"Three of the following four number-sets are alike in a certain way and one is different. Find the odd set.\n{NOTE}"

    pairs = [(12, 144), (15, 225), (9, 81), (11, 111)]
    one_breaks(pairs, lambda p: p[0] ** 2 == p[1], (11, 111))
    txt = [f"{a} : {b}" for a, b in pairs]
    qs.append(sq("number-set-classification-p01", txt, "11 : 111",
                 "144 = 12², 225 = 15², 81 = 9² - second number is the **square** of the first. 11² = 121, not 111 → **11 : 111**.",
                 "Squares of 9, 11, 12, 15 are 81, 121, 144, 225.", "easy", "cl-p26", 25, f"{S_ODDPAIR}\n\n**{', '.join(txt)}**"))
    pairs = [(4, 19), (6, 39), (7, 52), (8, 66)]
    one_breaks(pairs, lambda p: p[0] ** 2 + 3 == p[1], (8, 66))
    txt = [f"{a} : {b}" for a, b in pairs]
    qs.append(sq("number-set-classification-p02", txt, "8 : 66",
                 "Rule **a² + 3**: 4² + 3 = 19 ✓, 6² + 3 = 39 ✓, 7² + 3 = 52 ✓, 8² + 3 = 67 ≠ 66 → **8 : 66**.",
                 "Subtract each second number from the square of the first: 3, 3, 3, then 2.", "medium", "cl-p26", 40,
                 f"{S_ODDPAIR}\n\n**{', '.join(txt)}**"))
    pairs = [(5, 126), (3, 28), (4, 65), (6, 215)]
    one_breaks(pairs, lambda p: p[0] ** 3 + 1 == p[1], (6, 215))
    txt = [f"{a} : {b}" for a, b in pairs]
    qs.append(sq("number-set-classification-p03", txt, "6 : 215",
                 "Rule **a³ + 1**: 5³ + 1 = 126 ✓, 3³ + 1 = 28 ✓, 4³ + 1 = 65 ✓. 6³ = 216, so 6³ + 1 = 217, but the pair shows 215 (= 6³ − 1) → **6 : 215**.",
                 "Big second numbers next to small first numbers → think cubes.", "hard", "cl-p26", 50,
                 f"{S_ODDPAIR}\n\n**{', '.join(txt)}**"))

    sets = [(3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 206)]
    one_breaks(sets, lambda s: s[1] == s[0] ** 2 and s[2] == s[0] ** 3, (6, 36, 206))
    txt = [fmt_set(s) for s in sets]
    qs.append(sq("number-set-classification-p04", txt, "(6, 36, 206)",
                 "Each set is **(n, n², n³)**: (3, 9, 27), (4, 16, 64), (5, 25, 125). For 6: 6³ = 216, not 206 → **(6, 36, 206)**.",
                 None, "easy", "cl-p27", 30, f"{S_ODDSET}\n\n**{', '.join(txt)}**"))
    sets = [(2, 7, 17), (3, 9, 21), (5, 13, 29), (4, 11, 24)]
    one_breaks(sets, lambda s: s[1] == 2 * s[0] + 3 and s[2] == 2 * s[1] + 3, (4, 11, 24))
    txt = [fmt_set(s) for s in sets]
    qs.append(sq("number-set-classification-p05", txt, "(4, 11, 24)",
                 "Rule **×2 + 3, twice**: 2 → 7 → 17 ✓; 3 → 9 → 21 ✓; 5 → 13 → 29 ✓; 4 → 11 ✓ but 11 × 2 + 3 = 25, not 24 → **(4, 11, 24)**.",
                 "Check the second step - the first step fits in all four sets.", "medium", "cl-p27", 45,
                 f"{S_ODDSET}\n\n**{', '.join(txt)}**"))
    sets = [(6, 11, 21), (8, 15, 29), (5, 9, 17), (7, 13, 26)]
    one_breaks(sets, lambda s: s[1] == 2 * s[0] - 1 and s[2] == 2 * s[1] - 1, (7, 13, 26))
    txt = [fmt_set(s) for s in sets]
    qs.append(sq("number-set-classification-p06", txt, "(7, 13, 26)",
                 "Rule **×2 − 1, twice**: 6 → 11 → 21 ✓; 8 → 15 → 29 ✓; 5 → 9 → 17 ✓; 7 → 13 ✓ but 13 × 2 − 1 = 25, not 26 → **(7, 13, 26)**.",
                 "In three sets the last number is odd; 26 is even - a quick hint.", "medium", "cl-p27", 45,
                 f"{S_ODDSET}\n\n**{', '.join(txt)}**"))

    sets = [(4, 20, 5), (3, 21, 7), (6, 48, 8), (9, 45, 6)]
    one_breaks(sets, lambda s: s[0] * s[2] == s[1], (9, 45, 6))
    txt = [fmt_set(s) for s in sets]
    qs.append(sq("number-set-classification-p07", txt, "(9, 45, 6)",
                 "Middle = first × last: 4 × 5 = 20 ✓, 3 × 7 = 21 ✓, 6 × 8 = 48 ✓, 9 × 6 = 54 ≠ 45 → **(9, 45, 6)**.",
                 None, "easy", "cl-p28", 30, f"{S_ODDSET}\n\n**{', '.join(txt)}**"))
    sets = [(5, 34, 3), (4, 25, 3), (6, 61, 5), (7, 50, 2)]
    one_breaks(sets, lambda s: s[0] ** 2 + s[2] ** 2 == s[1], (7, 50, 2))
    one_breaks(sets, lambda s: s[0] * s[2] != s[1], None) if False else None
    txt = [fmt_set(s) for s in sets]
    qs.append(sq("number-set-classification-p08", txt, "(7, 50, 2)",
                 "Product does not work (5 × 3 = 15). Try **first² + last²**: 25 + 9 = 34 ✓, 16 + 9 = 25 ✓, 36 + 25 = 61 ✓, 49 + 4 = 53 ≠ 50 → **(7, 50, 2)**.",
                 "Middle larger than the product of the outer numbers → try sum of squares.", "hard", "cl-p28", 55,
                 f"{S_ODDSET}\n\n**{', '.join(txt)}**"))

    sets = [(12, 8, 40), (15, 5, 40), (9, 7, 32), (10, 6, 30)]
    one_breaks(sets, lambda s: 2 * (s[0] + s[1]) == s[2], (10, 6, 30))
    txt = [fmt_set(s) for s in sets]
    qs.append(sq("number-set-classification-p09", txt, "(10, 6, 30)",
                 "Third = **2 × (first + second)**: 2 × 20 = 40 ✓, 2 × 20 = 40 ✓, 2 × 16 = 32 ✓, 2 × 16 = 32 ≠ 30 → **(10, 6, 30)**.",
                 "(9, 7, 32) and (10, 6, 30) have the same first-two sum (16), so their third numbers must be equal - one of them is odd; the other three agree with ×2.", "medium", "cl-p29", 45,
                 f"{S_ODDSET}\n\n**{', '.join(txt)}**"))
    sets = [(7, 3, 20), (8, 5, 39), (6, 4, 23), (9, 2, 18)]
    one_breaks(sets, lambda s: s[0] * s[1] - 1 == s[2], (9, 2, 18))
    txt = [fmt_set(s) for s in sets]
    qs.append(sq("number-set-classification-p10", txt, "(9, 2, 18)",
                 "Third = **first × second − 1**: 7 × 3 − 1 = 20 ✓, 8 × 5 − 1 = 39 ✓, 6 × 4 − 1 = 23 ✓, 9 × 2 − 1 = 17 ≠ 18 → **(9, 2, 18)**.",
                 "Third number is one less than the product in three sets, equal to it in one.", "hard", "cl-p29", 50,
                 f"{S_ODDSET}\n\n**{', '.join(txt)}**"))

    opts = [(5, 20, 80), (4, 12, 36), (6, 24, 72), (7, 28, 84)]
    rule = lambda s: s[1] == 4 * s[0] and s[2] == 4 * s[1]  # noqa: E731
    assert rule((3, 12, 48)) and rule((2, 8, 32))
    only_fits(opts, rule, (5, 20, 80))
    txt = [fmt_set(s) for s in opts]
    qs.append(sq("number-set-classification-p11", txt, "(5, 20, 80)",
                 "Model sets: 3 × 4 = 12, 12 × 4 = 48; 2 × 4 = 8, 8 × 4 = 32 → rule **×4, ×4**. (5, 20, 80): 5 × 4 = 20, 20 × 4 = 80 ✓. (4, 12, 36) is ×3, ×3; (6, 24, 72) and (7, 28, 84) are ×4 then ×3 → **(5, 20, 80)**.",
                 "Check the last step: 20 × 4 = 80 is the only one that keeps ×4.", "medium", "cl-p30", 40,
                 f"Select the set in which the numbers are related in the same way as the numbers of the following sets.\n{NOTE}\n\n**(3, 12, 48), (2, 8, 32)**"))
    opts = [(7, 48), (8, 65), (5, 25), (10, 98)]
    rule = lambda p: p[0] ** 2 - 1 == p[1]  # noqa: E731
    assert rule((6, 35)) and rule((9, 80))
    only_fits(opts, rule, (7, 48))
    txt = [f"{a} : {b}" for a, b in opts]
    qs.append(sq("number-set-classification-p12", txt, "7 : 48",
                 "Model: 6² − 1 = 35 and 9² − 1 = 80 → rule **a² − 1**. 7² − 1 = 48 ✓. 8 : 65 is 8² + 1, 5 : 25 is 5², 10 : 98 is 10² − 2 → **7 : 48**.",
                 None, "medium", "cl-p30", 35,
                 f"Select the pair in which the numbers are related in the same way as the numbers of the following pairs.\n{NOTE}\n\n**6 : 35, 9 : 80**"))
    return qs


def apply(d):
    set_sub(d, "pair-classification", notes=PAIR_NOTES, patterns=PAIR_PATTERNS)
    add_sub(d, {
        "id": "number-set-classification",
        "title": "Number pairs and sets odd one out",
        "concept": SET_CONCEPT,
        "formulas": SET_FORMULAS,
        "tricks": SET_TRICKS,
        "mistakes": SET_MISTAKES,
        "notes": SET_NOTES,
        "patterns": SET_PATTERNS,
    }, after="pair-classification")
    return pair_questions() + set_questions()
