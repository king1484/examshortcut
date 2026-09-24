"""coding-decoding: notes + patterns + practice for number-coding, substitution-coding,
symbol-coding and language-coding (the four subtopics the earlier scripts did not cover)."""
import importlib.util
import os
import sys

_dir = os.path.dirname(__file__)
sys.path.insert(0, _dir)
from _lib import *  # noqa

_spec = importlib.util.spec_from_file_location(
    "cd_helpers", os.path.join(_dir, "coding-decoding-helpers.py"))
_cdh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cdh)
fixed, possible = _cdh.fixed, _cdh.possible

T = "coding-decoding"
d = load(T)

# ================================================================ number-coding
set_sub(d, "number-coding",
    notes="""### What is number coding?
A **word is coded as a number**. You are told (or you discover) how one word turns into its number, and you must code another word the same way. Example: **SUN is coded 54**, so how is DOG coded?

The number is almost always built from the **alphabet positions** of the letters: A = 1, B = 2, ... Z = 26. The EJOTY anchors make positions fast: E = 5, J = 10, O = 15, T = 20, Y = 25.

### Step 1: find the position sum of the model word
Add the positions of the model word's letters. For SUN: S = 19, U = 21, N = 14, and 19 + 21 + 14 = **54**. The code 54 is exactly this sum — the rule is a **plain position sum**.

### Step 2: compare the sum with the code
If the sum does not equal the code, look at the difference:

| What you see | Rule family |
|---|---|
| Code = sum of positions | plain sum (SUN = 54) |
| Code uses A = 26, B = 25 ... Z = 1 | **reverse positions** (27 − p) |
| Code = 2 × sum, sum + 10, sum − 5 ... | sum with an **extra step** |
| Code grows fast for 4-letter words | **weighted sum** (position × place in word) |
| Code = letters **plus** a number | **mixed code** (shifted letters + sum) |

The question often states the rule ("sum of alphabet positions", "A = 26, B = 25..."). When it does not, this table is your test order.

### The rule bank with worked examples
1. **Plain sum.** SUN = 19 + 21 + 14 = 54. DOG = 4 + 15 + 7 = 26.
2. **Reverse-position sum.** Treat A as 26 and Z as 1 (each letter counts 27 − its normal position). CAT = 24 + 26 + 7 = 57.
3. **Sum with an extra step.** CAB: sum = 6, code 16 → the rule adds 10. Apply the same extra step to the new word.
4. **Weighted sum.** Each letter's position is multiplied by its place in the word, then added. BAG = 2×1 + 1×2 + 7×3 = 25.
5. **Mixed letter-plus-number code.** 'TREE' → 'USFF48': each letter moves +1 (TREE → USFF) and the position sum (48) is written after. For the new word, do both parts again from scratch.

### Worked example (weighted sum)
**DAB is coded 12. How is CAD coded?** D×1 + A×2 + B×3 = 4 + 2 + 6 = 12 ✓. CAD = 3×1 + 1×2 + 4×3 = 3 + 2 + 12 = **17**.

### Common traps
- **Reusing the sample's number.** In mixed codes, the number part must be recomputed for the new word — it is never copied.
- **Wrong direction.** If the paper says A = 26, do not keep summing normal positions.
- **Assuming the plain sum.** Always check: does the model word's plain sum equal the code? If not, find the extra step before coding the new word.
- **Adding instead of multiplying** in weighted sums — B×1 + A×2 means A is multiplied by 2, not added.

### Quick revision
- Positions A = 1 ... Z = 26; EJOTY anchors give fast look-ups.
- Test order: plain sum → reverse sum (27 − p) → sum ± r or × k → weighted (p × place) → mixed letter + number.
- The rule must reproduce the model word's code exactly before you use it.
- Reverse position of a letter = 27 − position. Z counts as 1, A as 26.
- Mixed codes: shift the letters and append the fresh position sum of the new word.
""", patterns=[
    P("cd-p15", "Plain position-sum coding", "very common",
      "A word is coded with a number close to 30-80, and the question may say 'sum of alphabet positions'.",
      "1. Add the positions of the model word's letters (EJOTY helps).\n2. If the sum equals the code, the rule is a plain sum.\n3. Add the positions of the new word.\n\n*Why it works:* the plain sum is the most common number code in SSC, Railway and Banking papers.",
      "**HAT is coded 29** (sum of positions). How is **PEN** coded?",
      "H + A + T = 8 + 1 + 20 = 29 ✓ (plain sum). P + E + N = 16 + 5 + 14 = **35**.",
      formula=r"\text{code} = \sum p_i"),
    P("cd-p16", "Reverse-position sum (A = 26 ... Z = 1)", "common",
      "The question says 'A = 26, B = 25 ... Z = 1', or the code is large for a short word.",
      "1. Convert each letter to 27 − its normal position.\n2. Add them for the model word and confirm the code.\n3. Repeat for the new word.\n\n*Why it works:* reverse positions are the same table read backwards; Z = 1 and A = 26.",
      "**EAT is coded 55** (A = 26, B = 25 ... Z = 1). How is **TEN** coded?",
      "E = 22, A = 26, T = 7 → 55 ✓. T = 7, E = 22, N = 13 → **42**.",
      formula=r"\text{code} = \sum (27 - p_i)"),
    P("cd-p17", "Position sum with an extra step (× k or + r)", "common",
      "The plain sum of the model word is close to, but not equal to, the code.",
      "1. Compute the plain sum of the model word.\n2. Find the extra step: code − sum, or code ÷ sum.\n3. Apply the same step to the new word's sum.\n\n*Why it works:* a single extra operation turns the plain sum into any number the setter wants.",
      "**DIG is coded 22**. How is **BIG** coded?",
      "D + I + G = 4 + 9 + 7 = 20; 20 + 2 = 22, so the rule is **sum + 2**. BIG = 2 + 9 + 7 = 18, plus 2 = **20**.",
      formula=r"\text{code} = k\sum p_i + r"),
    P("cd-p18", "Weighted sum (position × place in the word)", "occasional",
      "The code cannot be reached by any plain sum; the word has 3-4 letters and the code is mid-sized.",
      "1. Multiply each letter's position by its place (1st, 2nd, 3rd ...).\n2. Add the products and check the model word's code.\n3. Do the same for the new word.\n\n*Why it works:* weighting explains codes that no flat sum can reach.",
      "**DAB is coded 12** (position × place). How is **CAD** coded?",
      "D×1 + A×2 + B×3 = 4 + 2 + 6 = 12 ✓. CAD = 3×1 + 1×2 + 4×3 = 3 + 2 + 12 = **17**.",
      formula=r"\text{code} = \sum i \cdot p_i"),
    P("cd-p19", "Mixed letter-plus-number code", "occasional",
      "The code is a string like 'USFF48' — letters followed by a number (or the reverse).",
      "1. Solve the letter part first (usually a shift).\n2. Compute the number part for the NEW word afresh (usually its position sum).\n3. Join both parts in the same order as the sample.\n\n*Why it works:* the two halves are independent mini-codes; the number always changes with the word.",
      "**TREE is written USFF48** (+1 letters, position sum appended). How is **LEAF** written?",
      "LEAF + 1 = **MFBG**. Sum = 12 + 5 + 1 + 6 = **24**. Code = **MFBG24**."),
])

def nq(qid, q, ans, wrong, sol, sc, diff, pat, t, check=None):
    return Q(qid, q, ans, wrong, sol, shortcut=sc, diff=diff, sub="number-coding", pat=pat, t=t, check=check)

NUMQ = [
    nq("number-coding-p01", "In a certain code, **HAT is coded 29** (sum of alphabet positions). How is **PEN** coded?",
       str(psum("PEN")), ["34", "36", "45"],
       f"H + A + T = 8 + 1 + 20 = 29 ✓ (plain sum). PEN = 16 + 5 + 14 = **{psum('PEN')}**.",
       "Add positions straight away when the question says 'sum'.", "easy", "cd-p15", 30, check=str(psum("PEN"))),
    nq("number-coding-p02", "In a certain code, **BAT is coded 23** (sum of alphabet positions). How is **CUP** coded?",
       str(psum("CUP")), ["38", "39", "41"],
       f"B + A + T = 2 + 1 + 20 = 23 ✓. C + U + P = 3 + 21 + 16 = **{psum('CUP')}**.",
       None, "easy", "cd-p15", 30, check=str(psum("CUP"))),
    nq("number-coding-p03", "In a certain code, **EAT is coded 55** (A = 26, B = 25 ... Z = 1). How is **TEN** coded?",
       str(rpos("T") + rpos("E") + rpos("N")), ["41", "43", "52"],
       "Reverse positions: E = 22, A = 26, T = 7 → 55 ✓. TEN = 7 + 22 + 13 = **42**.",
       "Reverse position = 27 − position. Z counts 1, A counts 26.", "medium", "cd-p16", 40,
       check=str(rpos("T") + rpos("E") + rpos("N"))),
    nq("number-coding-p04", "In a certain code, **ZIP is coded 30** (A = 26, B = 25 ... Z = 1). How is **MAP** coded?",
       str(rpos("M") + rpos("A") + rpos("P")), ["50", "49", "61"],
       "Reverse: Z = 1, I = 18, P = 11 → 30 ✓. MAP = 14 + 26 + 11 = **51**.",
       None, "medium", "cd-p16", 40, check=str(rpos("M") + rpos("A") + rpos("P"))),
    nq("number-coding-p05", "In a certain code, **MAN is coded 56** — double the sum of the letter positions. How is **FAN** coded?",
       str(psum("FAN") * 2), ["40", "44", "21"],
       f"M + A + N = 13 + 1 + 14 = 28, and 2 × 28 = 56 ✓. FAN = 6 + 1 + 14 = 21, doubled = **{psum('FAN')*2}**.",
       "Confirm the extra step on the model word before doubling anything.", "medium", "cd-p17", 40,
       check=str(psum("FAN") * 2)),
    nq("number-coding-p06", "In a certain code, **DIG is coded 22** — two more than the sum of the positions. How is **BIG** coded?",
       str(psum("BIG") + 2), ["18", "22", "19"],
       f"D + I + G = 4 + 9 + 7 = 20, and 20 + 2 = 22 ✓. BIG = 2 + 9 + 7 = 18, plus 2 = **{psum('BIG')+2}**. (18 alone forgets the step.)",
       None, "medium", "cd-p17", 40, check=str(psum("BIG") + 2)),
    nq("number-coding-p07", "In a certain code, **DAB is coded 12**: each letter's position is multiplied by its place in the word and the products are added. How is **CAD** coded?",
       str(3 * 1 + 1 * 2 + 4 * 3), ["12", "16", "18"],
       f"DAB = 4×1 + 1×2 + 2×3 = 12 ✓. CAD = 3×1 + 1×2 + 4×3 = 3 + 2 + 12 = **{3*1+1*2+4*3}**.",
       "Weighted sums are the only family that reaches some codes — test them after plain sums fail.", "hard", "cd-p18", 50,
       check=str(3 * 1 + 1 * 2 + 4 * 3)),
    nq("number-coding-p08", "In a certain code, **DIME is coded 81**: each letter's position is multiplied by its place in the word and the products are added. How is **TIME** coded?",
       str(20 + 18 + 39 + 20), ["91", "81", "99"],
       f"DIME = 4×1 + 9×2 + 13×3 + 5×4 = 4 + 18 + 39 + 20 = 81 ✓. TIME = 20×1 + 9×2 + 13×3 + 5×4 = **{20+18+39+20}**.",
       "Only the first letter changes (D → T), so recompute just that product: 4 → 20 adds 16 to 81 − 4 = 77... quick way: 81 − 4 + 20 = 97.",
       "hard", "cd-p18", 55, check=str(20 + 18 + 39 + 20)),
    nq("number-coding-p09", "In a certain code, **GOAT is written HPBU43** — each letter moves one step forward and the word's position sum is written after it. How is **LAMP** written?",
       shift("LAMP", 1) + str(psum("LAMP")), ["MBNQ36", "LAMP42", "MBNQ41"],
       f"Letters: GOAT + 1 = HPBU ✓, and 7 + 15 + 1 + 20 = 43 ✓. LAMP + 1 = **{shift('LAMP',1)}**; sum = 12 + 1 + 13 + 16 = **{psum('LAMP')}**. Code = **{shift('LAMP',1)+str(psum('LAMP'))}**.",
       "Two-part code: shift the letters; recompute the number from the new word.", "medium", "cd-p19", 50,
       check=shift("LAMP", 1) + str(psum("LAMP"))),
    nq("number-coding-p10", "In a certain code, **BIRD is written CJSE33** — each letter moves one step forward and the word's position sum is written after it. How is **FISH** written?",
       shift("FISH", 1) + str(psum("FISH")), ["GJTI41", "FISH42", "GJTJ42"],
       f"BIRD + 1 = CJSE ✓, sum 2 + 9 + 18 + 4 = 33 ✓. FISH + 1 = **{shift('FISH',1)}**; sum = 6 + 9 + 19 + 8 = **{psum('FISH')}**. Code = **{shift('FISH',1)+str(psum('FISH'))}**.",
       None, "hard", "cd-p19", 55, check=shift("FISH", 1) + str(psum("FISH"))),
]
upsert(d["practice"], NUMQ)

# ================================================================ substitution-coding
set_sub(d, "substitution-coding",
    notes="""### What is substitution coding?
The exam **renames things** or **renames code words**, and you must answer from the renamed world. Two very different looks share this subtopic:

1. **'Is called' chains.** "If cloud is called rain, rain is called wind..." — the real thing and its new name are linked in a chain, and you answer with the **new name**.
2. **Word-code matching.** "In a code language, 'red light' is 'pa ka'..." — English words are written with code words (pa, ka, ni ...), usually **jumbled**, and you find which code stands for which word.

### 'Is called' chains — the one rule
The question always asks about the **real world**, and the answer lies in the **renamed world**.

- Ask: what is the real answer in everyday life? (What do farmers wait for? **Rain**.)
- Then look up what that thing **is called** in the question. (Rain is called **wind**.)
- Answer with the new name: **wind**.

Read the chain in one direction only. "Cloud is called rain" tells you the new name of cloud — it does **not** tell you the new name of rain. That comes from the next line of the chain.

### Word-code matching — intersect and subtract
- A word common to two sentences has its code among the code words **common** to those two sentences.
- Find a code for every common word first. Then remove those codes from each sentence: what is left over belongs to the left-over words.

Example: 'red light' = 'pa ka', 'green light' = 'ka na'. 'light' is common and 'ka' is the common code → light = ka. In sentence 1 the leftover word 'red' takes the leftover code **pa**.

### The 'cannot be determined' rule
Sometimes two codes remain possible for one word. Example: 'red rose' = 'pa ka', 'white lotus' = 'za ka'. No word is common to the two sentences, so 'ka' is not pinned to anything: 'rose' could be 'pa' or 'ka'. When **two or more** codes remain equally possible after all elimination, the answer is **cannot be determined**. Do not guess one of them — the exam keeps this option exactly for this case.

With three sentences, elimination usually pins every word down. Work in this order:
1. Words common to two (or three) sentences.
2. Codes common to the same sentences.
3. Subtract fixed codes; assign leftovers.

### Other substitution forms
- **Longer chains with reverse look-up:** "when do we sleep?" — real answer 'night' — night is called 'morning' → answer 'morning'.
- **Digits or symbols standing for words:** a small dictionary is given (1 = come, 2 = home ...); build the answer phrase in the **same word order as the question** asks.

### Quick revision
- 'Is called': find the real-world answer first, then answer with its **new name**. Never mix the two worlds.
- One line of a chain names only the word at its left end.
- Word-code: common word ↔ common code; then subtract what is fixed.
- Two possible codes left after elimination → cannot be determined.
- Phrase codes keep the order in which the question writes the phrase.
""", patterns=[
    P("cd-p20", "Simple 'is called' chains", "very common",
      "Lines like 'if white is called blue, blue is called red ...' ending with a real-life question.",
      "1. Answer the everyday question with the REAL thing (what do we write with? a pen).\n2. Read off the new name of that real thing from the chain.\n3. Give the new name as the answer.\n\n*Why it works:* the chain only renames things; the asked fact lives in the real world, the answer in the renamed one.",
      "**If cloud is called rain, rain is called wind, wind is called sun** — what do farmers wait for?",
      "Farmers wait for real **rain**. Rain is called **wind**. Answer: Wind (not rain — that is cloud's new name)."),
    P("cd-p21", "Word-code matching by elimination", "common",
      "Two or three English sentences with code words ('pa ka ni'); the code order is usually jumbled.",
      "1. Find words common to two sentences; their codes are the common code words.\n2. Fix those codes, then subtract them from each sentence.\n3. Left-over words take left-over codes.\n\n*Why it works:* a word's code must appear in every sentence that contains the word.",
      "**'hot tea' = 'na pi', 'cold tea' = 'pi ka', 'hot milk' = 'na ru'** — code for 'milk'?",
      "hot ↔ na (sentences 1, 3), tea ↔ pi (1, 2). Sentence 2 leaves cold = ka; sentence 3 leaves milk = **ru**."),
    P("cd-p22", "Cannot be determined (two codes left)", "common",
      "A word appears in only one sentence, and its sentence shares two or more codes with the other sentence.",
      "1. Fix every code you can by the common-word method.\n2. If two codes still fit the asked word, stop — the answer is 'cannot be determined'.\n3. Never pick one of the two possible codes.\n\n*Why it works:* elimination needs leftovers of size one; size two leaves a genuine ambiguity.",
      "**'red rose' = 'pa ka', 'white lotus' = 'za ka'** — what is the code for 'rose'?",
      "No word is common to the two sentences, so 'ka' belongs to nothing for certain. Rose can be 'pa' or 'ka' → **cannot be determined**."),
    P("cd-p23", "Longer chains and reverse look-up", "common",
      "Chains of four or five renames, or questions that run the chain the other way ('what does 'morning' really mean?').",
      "1. Write the chain as a list: real thing → new name.\n2. Start from the real-world fact the question asks about.\n3. Walk to its new name (or, for reverse look-up, find which real thing maps to the given name).\n\n*Why it works:* a written-down chain stops the confusion that costs marks here.",
      "**If day is called night, night is called morning, morning is called evening** — when do we sleep?",
      "We sleep at real **night**. Night is called **morning**. Answer: Morning."),
])

def sq2(qid, q, ans, wrong, sol, sc, diff, pat, t, verify=None):
    if verify:
        assert verify, qid
    return Q(qid, q, ans, wrong, sol, shortcut=sc, diff=diff, sub="substitution-coding", pat=pat, t=t)

SUBQ = [
    sq2("substitution-coding-p01", "If **cloud is called rain**, **rain is called wind**, **wind is called sun**, and **sun is called moon**, what do farmers wait for?",
        "Wind", ["Rain", "Sun", "Moon"],
        "Farmers wait for real **rain**. The chain says rain is called **wind**. Answer: Wind.",
        "Real-world answer first, then its new name.", "easy", "cd-p20", 30),
    sq2("substitution-coding-p02", "If **pen is called sword**, **sword is called shield**, **shield is called gun**, and **gun is called book**, which one is used to write?",
        "Sword", ["Pen", "Shield", "Book"],
        "We write with a real **pen**. Pen is called **sword**. Answer: Sword.",
        None, "easy", "cd-p20", 30),
    sq2("substitution-coding-p03", "If **dog is called cat**, **cat is called rat**, **rat is called lion**, and **lion is called cow**, which animal catches mice?",
        "Rat", ["Cat", "Lion", "Cow"],
        "A real **cat** catches mice. Cat is called **rat**. Answer: Rat. (Cat is only the new name of a dog.)",
        None, "easy", "cd-p23", 30),
    sq2("substitution-coding-p04", "If **day is called night**, **night is called morning**, **morning is called evening**, and **evening is called noon**, when do we sleep?",
        "Morning", ["Night", "Evening", "Noon"],
        "We sleep at real **night**. Night is called **morning**. Answer: Morning.",
        "Write the chain down before answering long ones.", "medium", "cd-p23", 35),
    sq2("substitution-coding-p05", "If **hot is called cold**, **cold is called warm**, **warm is called cool**, and **cool is called freezing**, how does ice feel?",
        "Warm", ["Cold", "Cool", "Freezing"],
        "Ice feels real **cold**. Cold is called **warm**. Answer: Warm.",
        None, "medium", "cd-p23", 35),
    sq2("substitution-coding-p06", "In a code language, **'blue sky' is written 'ta pa'** and **'sky walk' is written 'pa sa'**. What is the code for **'blue'**?",
        "ta", ["pa", "sa", "na"],
        "'sky' is common to both sentences and 'pa' is the common code → sky = pa. In sentence 1 the leftover word 'blue' takes the leftover code **ta**.",
        "Common word ↔ common code; leftovers pair up.", "easy", "cd-p21", 35,
        verify=fixed([["blue", "sky"], ["sky", "walk"]], [["ta", "pa"], ["pa", "sa"]], "blue") == "ta"),
    sq2("substitution-coding-p07", "In a code language, **'hot tea' = 'na pi'**, **'cold tea' = 'pi ka'**, **'hot milk' = 'na ru'**. What is the code for **'milk'**?",
        "ru", ["na", "ka", "pi"],
        "hot ↔ na (sentences 1, 3) and tea ↔ pi (sentences 1, 2). Sentence 2 leaves cold = ka. Sentence 3 leaves milk = **ru**.",
        None, "medium", "cd-p21", 45,
        verify=fixed([["hot", "tea"], ["cold", "tea"], ["hot", "milk"]], [["na", "pi"], ["pi", "ka"], ["na", "ru"]], "milk") == "ru"),
    # p08: 4 words, 3 codes — the exam's classic loose design; no global bijection exists,
    # which is exactly why the answer is 'cannot be determined'. Verified by hand:
    # rose = pa (pa=rose, ka=red) and rose = ka (ka=rose, pa=red) are both consistent.
    sq2("substitution-coding-p08", "In a code language, **'red rose' = 'pa ka'** and **'white lotus' = 'za ka'**. What is the code for **'rose'**?",
        "Cannot be determined", ["pa", "ka", "za"],
        "No word is common to the two sentences, so the shared code 'ka' is not fixed to any word. 'Rose' can be 'pa' or 'ka' — two codes remain → **cannot be determined**.",
        "Two possible codes after full elimination = the CBD option.", "medium", "cd-p22", 40),
    sq2("substitution-coding-p09", "In a code language, **'birds fly' = 'lo pe'**, **'fly high' = 'pe ni'**, **'birds sing' = 'lo ra'**. What is the code for **'sing'**?",
        "ra", ["lo", "pe", "ni"],
        "birds ↔ lo (sentences 1, 3) and fly ↔ pe (sentences 1, 2). Sentence 3 leaves sing = **ra**.",
        "Three sentences usually pin every code down.", "hard", "cd-p22", 45,
        verify=fixed([["birds", "fly"], ["fly", "high"], ["birds", "sing"]], [["lo", "pe"], ["pe", "ni"], ["lo", "ra"]], "sing") == "ra"),
]
upsert(d["practice"], SUBQ)

# ================================================================ symbol-coding
MATRIX = ["A B C D E", "F G H I K", "L M N O P", "Q R S T U", "V W X Y Z"]
MATRIX_Q = ("In the following 5 × 5 matrix, columns are numbered 1-5 from left to right and rows 1-5 from top "
            "to bottom:\nRow 1: A B C D E\nRow 2: F G H I K\nRow 3: L M N O P\nRow 4: Q R S T U\n"
            "Row 5: V W X Y Z\n")


def rc(ch):
    for r, row in enumerate(MATRIX, 1):
        cols = row.split()
        if ch in cols:
            return r, cols.index(ch) + 1
    raise KeyError(ch)


def mcode(word):
    return ", ".join(f"{a}{b}" for a, b in (rc(c) for c in word))


set_sub(d, "symbol-coding",
    notes="""### What is symbol and digit coding?
Letters (or digits) are replaced by **symbols** (@ # % * ...) or **digits**, one fixed code per letter. Two exam looks:

1. **A table is given**: M = #, A = @, T = %. Code the word letter by letter.
2. **No table**: two or three words come with their codes, and you discover which symbol stands for which letter by **matching**.

Once a letter's code is known, it never changes inside the question.

### Type 1: code straight from the table
Write the table's letter under each letter of the word, in order. If MAT has M = #, A = @, T = %, then MAT = **#@%**. Watch for extra **conditions**:
- "If the word begins with a vowel, write the codes in reverse order."
- "If the digit sum is even, reverse the digits first."

Check the condition **before** touching the table — the setter counts on you forgetting it.

### Type 2: match common letters with common symbols
When two coded words share letters, their codes share exactly those symbols:

- PEN = @ # %  and NET = % # &
- Common letters E, N sit at the same places as common symbols #, % → E = #, N = %.
- The leftover letter of PEN (P) takes the leftover symbol **@**.

This works when the symbols keep their positions. If the question says the symbol order may differ, match by **count**: two common letters must appear as two common symbols; the leftover pairs up one-to-one.

### Digit tables
Digits may stand for letters with a simple build: A = 2, B = 4, C = 6 (double the position). Code letter by digit, keeping one digit per letter. 4 can be one letter (D) or part of 10 (J) — count letters, not digits.

### Matrix coding (SSC favourite)
Letters sit in a 5 × 5 grid; rows and columns are numbered 1-5. Each letter's code is its **(row, column)** pair. Read the word letter by letter and write the pairs: H is in row 2, column 3 → 23. The code of a 4-letter word is four two-digit numbers.

Speed tip: the same letter may appear more than once in the grid in some papers — any valid position pair is accepted; pick the one that matches an option.

### Conditions with numbers
Number codes come with a test: "if the sum of the digits is even, reverse the digits before coding." Sum first, then decide the order, then map digit → symbol.

### Quick revision
- Table given: map letter by letter; check conditions first.
- No table: common letters ↔ common symbols; leftovers pair up.
- Symbols may not keep order — then only counts are safe, and two possible codes mean 'cannot be determined'.
- Matrix: code = (row, column) per letter; the grid has no J in the classic version.
- Mixed conditions: decide the order rule before coding anything.
""", patterns=[
    P("cd-p24", "Direct table look-up", "very common",
      "A letter → symbol/digit table is printed with the question.",
      "1. Write the code symbol under each letter of the word, in order.\n2. Join the symbols without spaces (or as the options show).\n3. Double-check the table row you used.\n\n*Why it works:* the table fixes every letter; nothing needs discovering.",
      "**M = #, A = @, T = %.** What is the code of **MAT**?",
      "M → #, A → @, T → %. MAT = **#@%**.",
      formula=None),
    P("cd-p25", "Condition before the table", "common",
      "The question lists conditions ('if the word begins with a vowel, reverse the codes') above the table.",
      "1. Test the conditions on the word in order.\n2. Apply the first matching condition (reverse order, swap rows ...).\n3. Only then code from the table.\n\n*Why it works:* the condition changes the ORDER of symbols, not their letter values.",
      "Table: E = &, C = $, H = %, O = *. Condition: if the word begins with a vowel, write the codes in reverse order. Code of **ECHO**?",
      "ECHO begins with the vowel E → reverse. Direct codes are & $ % *; reversed → ***%$&**."),
    P("cd-p26", "Match common letters ↔ common symbols (no table)", "common",
      "Words like 'PEN = @ # %' and 'NET = % # &' come with no table; you must infer codes.",
      "1. Circle letters shared by two words and symbols shared by their codes.\n2. Pair them (position-wise when order is fixed).\n3. Left-over letter takes the left-over symbol.\n\n*Why it works:* codes are letter-for-symbol, so shared letters force shared symbols.",
      "**PEN = @ # %, NET = % # &.** What is the code for **P**?",
      "E and N are common; # and % are the common symbols → E = #, N = %. PEN's leftover P takes PEN's leftover **@**."),
    P("cd-p27", "Digit substitution for letters", "common",
      "Letters map to digits by a rule (A = 2, B = 4, C = 6 ... or vowels to their positions).",
      "1. Find the build rule from the given examples (double the position, position itself ...).\n2. Convert the word letter by letter.\n3. Keep one number per letter — 10 takes two digit places.\n\n*Why it works:* the build rule is a small arithmetic step on positions.",
      "**A = 2, B = 4, C = 6 ...** (double the position). What is the code of **CAB**?",
      "C = 6, A = 2, B = 4 → **624**."),
    P("cd-p28", "Matrix coding (row, column)", "very common",
      "A 5 × 5 grid of letters with numbered rows and columns; the code of each letter is a two-digit (row, column) pair.",
      "1. Find each letter's row and column in the grid.\n2. Write the pair as two digits (row first, then column).\n3. Join the pairs for the whole word.\n\n*Why it works:* the grid is just a table; the pair is an address.",
      MATRIX_Q + "What is the code for **HIDE**?",
      "H = (2, 3), I = (2, 4), D = (1, 4), E = (1, 5) → **23, 24, 14, 15**."),
])

SYMQ = [
    Q("symbol-coding-p01", "In a certain code, **M = #, A = @, T = %**. What is the code for **MAT**?",
      "#@%", ["%#@", "@#%", "#%@"],
      "M → #, A → @, T → %. MAT = **#@%**.",
      shortcut=None, diff="easy", sub="symbol-coding", pat="cd-p24", t=30,
      check="#@%"),
    Q("symbol-coding-p02", "In a certain code, **D = 8, O = 5, G = 2**. What is the code for **GOD**?",
      "258", ["852", "528", "582"],
      "G → 2, O → 5, D → 8. GOD = **258**. (852 is DOG — the reverse trap.)",
      shortcut=None, diff="easy", sub="symbol-coding", pat="cd-p24", t=30,
      check="258"),
    Q("symbol-coding-p03", "In a certain code, **C = %, A = @, B = #, T = ***. What is the code for **TAB**?",
      "*@#", ["#*@", "@*#", "*#@"],
      "T → *, A → @, B → #. TAB = ***@#**.",
      shortcut=None, diff="easy", sub="symbol-coding", pat="cd-p24", t=30,
      check="*@#"),
    Q("symbol-coding-p04", "In a certain code, digits are coded **1 = @, 2 = #, 3 = $, 4 = %, 5 = &**. What is the code for **245**?",
      "#&%", ["%&#", "#$%", "&#%"],
      "2 → #, 4 → %, 5 → &. 245 = **#&%**.",
      shortcut=None, diff="easy", sub="symbol-coding", pat="cd-p27", t=30,
      check="#&%"),
    Q("symbol-coding-p05", "In a certain code, **A = 2, B = 4, C = 6, D = 8, E = 10** (double the position). What is the code for **CAB**?",
      "624", ["246", "642", "264"],
      "C = 6, A = 2, B = 4 → **624**. (246 writes the word backwards.)",
      shortcut=None, diff="medium", sub="symbol-coding", pat="cd-p27", t=35,
      check="624"),
    Q("symbol-coding-p06", "In a certain code, **A = 2, B = 4, C = 6, D = 8, E = 10** (double the position). What is the code for **BED**?",
      "4 10 8", ["4 8 10", "10 4 8", "4 10 9"],
      "B = 4, E = 10, D = 8 → **4 10 8**. Keep one number per letter — E takes the two-digit 10.",
      shortcut=None, diff="medium", sub="symbol-coding", pat="cd-p27", t=35,
      check="4 10 8"),
    Q("symbol-coding-p07", "In a certain code, **PEN = @ # %** and **NET = % # &**. What is the code for **P**?",
      "@", ["#", "%", "&"],
      "E and N are common to both words; # and % are the common symbols → E = #, N = %. The leftover letter of PEN (P) takes the leftover symbol **@**.",
      shortcut=None, diff="medium", sub="symbol-coding", pat="cd-p26", t=40,
      check="@"),
    Q("symbol-coding-p08", "In a certain code, **CAT = & @ %** and **CUT = & $ %**. What is the code for **ACT**?",
      "@&%", ["&@%", "%&@", "@%&"],
      "CAT and CUT share C and T; their codes share & and % → C = &, T = %. The leftovers give A = @, U = $. ACT = A → @, C → &, T → % = **@&%**.",
      shortcut=None, diff="medium", sub="symbol-coding", pat="cd-p26", t=45,
      check="@&%"),
    Q("symbol-coding-p09", "A code table says: if a word **begins with a vowel**, write the letter codes in **reverse order**; otherwise left to right. Codes: E = &, C = $, H = %, O = *. What is the code for **ECHO**?",
      "*%$&", ["&$%*", "*&$%", "$%*&"],
      "ECHO begins with the vowel E → reverse the order. Direct codes are & $ % *; reversed gives ***%$&**.",
      shortcut=None, diff="hard", sub="symbol-coding", pat="cd-p25", t=50,
      check="*%$&"),
    Q("symbol-coding-p10", "Digits are coded **1 = @, 2 = #, 3 = $, 4 = %, 5 = &, 6 = ***. Condition: if the digit sum is **even**, code the digits in reverse order; otherwise left to right. What is the code for **136**?",
      "*$@", ["@$*", "@$%", "*$%"],
      "Digit sum 1 + 3 + 6 = 10, which is even → reverse to 631. 6 → *, 3 → $, 1 → @ → ***$@**.",
      shortcut=None, diff="hard", sub="symbol-coding", pat="cd-p25", t=50,
      check="*$@"),
    Q("symbol-coding-p11", MATRIX_Q + "What is the code for **HIDE**? (Row, column for each letter.)",
      "23, 24, 14, 15", ["23, 24, 15, 14", "23, 14, 24, 15", "24, 23, 14, 15"],
      f"H is in row 2, column 3 → 23; I → 24; D is in row 1, column 4 → 14; E → 15. Code = **{mcode('HIDE')}**.",
      shortcut="Find the first letter's pair, then walk the grid for the rest.", diff="hard", sub="symbol-coding", pat="cd-p28", t=55,
      check=mcode("HIDE")),
    Q("symbol-coding-p12", MATRIX_Q + "What is the code for **ROSE**? (Row, column for each letter.)",
      "42, 34, 43, 15", ["42, 34, 15, 43", "24, 34, 43, 15", "42, 43, 34, 15"],
      f"R = (4, 2) → 42; O = (3, 4) → 34; S = (4, 3) → 43; E = (1, 5) → 15. Code = **{mcode('ROSE')}**.",
      shortcut=None, diff="hard", sub="symbol-coding", pat="cd-p28", t=55,
      check=mcode("ROSE")),
]
upsert(d["practice"], SYMQ)

# ================================================================ language-coding
set_sub(d, "language-coding",
    notes="""### What is language coding?
A whole **sentence** is written in a code language: 'good morning sir' becomes 'ta pa ni'. You get two or three such sentence–code pairs and must find the code of a word (or the meaning of a code).

The golden fact: **the code order is usually jumbled**. 'good morning' = 'ta pa' does NOT mean good = ta. Never match by position.

### The intersect-and-subtract method
1. **Intersect.** For the word you need, find every sentence that contains it. The word's code is among the code words those sentences have **in common**.
2. **Subtract.** Remove codes already fixed for other words. One code left → that is the answer.

Example: 'sun is hot' = 'ta mo ri'; 'sun is bright' = 'ri ze mo'. The words 'sun is' are common, so their codes are 'ri mo' (the common code words). Sentence 1's leftover word 'hot' takes the leftover code **ta**.

### When the answer is 'cannot be determined'
If, after subtracting everything you know, **two codes** still fit the word, stop. The answer is **cannot be determined**. Example: 'sky is blue' = 'ta pa ka'; 'sea is deep' = 'pa za la'. Only 'is' is common → is = pa. 'Blue' can be 'ta' or 'ka' — both remain possible. Picking one of them is the classic wrong move; the option 'cannot be determined' exists exactly for this.

More sentences = more information. With three well-chosen sentences every word usually gets pinned down; with two sentences some word almost always stays open.

### Phrase and digit codes
- To code a **phrase** ('sweet home'), find each word's code, then write them **in the order the phrase asks**, not in any remembered order.
- Some papers use **digit codes**: 'come home' = '1 2', 'sweet home' = '2 3' → come = 1, home = 2, sweet = 3. The same intersect-and-subtract method works on digits.

### Reverse questions ('what does pa mean?')
Work exactly the same way, then read the answer backwards: if pa = mango, then the code 'pa' means **mango**. The options are usually English words — check each option against your fixed mapping.

### A watertight check (for practice)
For every sentence, the set of code words and the set of English words must match one-to-one: a word in the sentence ⇔ its code in the code line. If your final mapping makes any sentence inconsistent, you paired something wrongly.

### Quick revision
- Never match by position — code order is jumbled.
- Intersect: word's code ∈ common codes of all sentences containing it.
- Subtract fixed codes; one left = answer.
- Two codes still possible → cannot be determined.
- Phrase codes follow the phrase's own word order; the same method works for digit codes.
""", patterns=[
    P("cd-p29", "Two sentences, one common word", "very common",
      "Two sentence–code pairs sharing exactly one word (or two) — the basic look of this subtopic.",
      "1. Find the word common to both sentences; its code is the common code word.\n2. In one sentence, the leftover word takes the leftover code.\n3. Read the asked word off your mapping.\n\n*Why it works:* with one common word, the common code is forced on both sides.",
      "**'delhi is big' = 'ja pa ni'; 'mumbai is big' = 'sa pa ni'.** Code for **delhi**?",
      "'is' and 'big' are common → their codes are 'pa ni'. Sentence 1's leftover 'delhi' takes **ja**."),
    P("cd-p30", "Three sentences, chain elimination", "common",
      "Three sentence–code pairs; the asked word needs two subtraction steps.",
      "1. Fix codes for words common to sentence pairs (common words ↔ common codes).\n2. Subtract all fixed codes from the asked word's sentence.\n3. The last remaining code is the answer.\n\n*Why it works:* each fixed code shrinks the leftovers; three sentences usually finish the job.",
      "**'train runs fast' = 'la jo me'; 'bus runs fast' = 'la jo fi'; 'fast train' = 'me jo'.** Code for **bus**?",
      "fast and train are common to sentences 1 and 3 → codes 'jo me'. fast also sits in sentence 1–2 pair ('la jo') → fast = jo, the code in both pairs. Then train = me, runs = la, and bus takes sentence 2's leftover **fi**."),
    P("cd-p31", "Cannot be determined (two codes left)", "common",
      "The asked word appears in only one sentence, and two codes there remain unclaimed.",
      "1. Fix every code you can with the common-word method.\n2. Count the codes still possible for the asked word.\n3. Two possible → answer 'cannot be determined'; never guess one.\n\n*Why it works:* jumbled order means both leftovers are equally likely until something pins one down.",
      "**'sky is blue' = 'ta pa ka'; 'sea is deep' = 'pa za la'.** Code for **blue**?",
      "Only 'is' is common → is = pa. Blue can be 'ta' or 'ka' — two codes remain → **cannot be determined**."),
    P("cd-p32", "Phrase codes and digit codes", "common",
      "The question codes a phrase ('sweet home') or uses digits ('come home' = '1 2').",
      "1. Find each word's code by the usual method.\n2. Write the phrase's code in the phrase's own word order.\n3. For digits, the method is identical — the tokens are just numbers.\n\n*Why it works:* a phrase code is only its word codes written in the asked order.",
      "**'come home' = '1 2'; 'home sweet' = '2 3'.** What is the code for **'sweet home'**?",
      "home is common → home = 2. So come = 1 and sweet = 3. 'Sweet home' = **3 2** (sweet first, as the phrase asks)."),
    P("cd-p33", "Reverse: what does the code mean?", "occasional",
      "The question gives a CODE and asks which English word it stands for.",
      "1. Fix the mapping word-by-word with intersect-and-subtract.\n2. Look up the given code in your mapping.\n3. Give the English word as the answer.\n\n*Why it works:* the mapping is symmetric; only the reading direction changes.",
      "**'birds fly' = 'lo pe'; 'fly high' = 'pe ni'; 'birds sing' = 'lo ra'.** What does **'ra'** mean?",
      "birds ↔ lo (sentences 1, 3), fly ↔ pe (1, 2). Sentence 3 leaves sing = ra, so 'ra' means **sing**."),
])

def lq(qid, items, codes, word, ans, wrong, sol, sc, diff, pat, t, cbd=False):
    if cbd:
        p = possible(items, codes, word)
        assert len(p) >= 2, (qid, p)
    else:
        assert fixed(items, codes, word) == ans, (qid, fixed(items, codes, word))
    return Q(qid, f"{qtext(items, codes)} {word}?", ans, wrong, sol, shortcut=sc,
             diff=diff, sub="language-coding", pat=pat, t=t)


def qtext(items, codes):
    s = "In a certain code language, " + "; ".join(
        f"**'{ ' '.join(it) }' is written '{' '.join(c)}'**" for it, c in zip(items, codes))
    return s + ". What is the code for"


def rq(qid, items, codes, code, ans, wrong, sol, sc, diff, pat, t):
    """Reverse question: 'what does <code> mean?' — the answer is an English word.
    Verified: in every consistent solution, exactly the answer word carries this code."""
    target = None
    for w in sorted({w for it in items for w in it}):
        try:
            if fixed(items, codes, w) == code:
                assert target is None, (qid, f"code {code} maps to two words: {target}, {w}")
                target = w
        except AssertionError as e:
            if "maps to two words" in str(e):
                raise
    assert target == ans.lower(), (qid, target, ans)
    s = "In a certain code language, " + "; ".join(
        f"**'{ ' '.join(it) }' is written '{' '.join(c)}'**" for it, c in zip(items, codes))
    q = s + f". What does the code **'{code}'** mean?"
    return Q(qid, q, ans, wrong, sol, shortcut=sc, diff=diff, sub="language-coding", pat=pat, t=t)


LANGQ = [
    lq("language-coding-p01", [["delhi", "is", "big"], ["mumbai", "is", "big"]], [["ja", "pa", "ni"], ["sa", "pa", "ni"]],
       "delhi", "ja", ["pa", "ni", "sa"],
       "'is' and 'big' are common to both sentences, so their codes are 'pa ni'. The leftover word 'delhi' takes the leftover code **ja**.",
       "Common word ↔ common code; leftovers pair up.", "easy", "cd-p29", 35),
    lq("language-coding-p02", [["read", "books"], ["read", "well"]], [["ka", "pi"], ["ka", "ja"]],
       "books", "pi", ["ka", "ja", "ka ja"],
       "'read' is common and 'ka' is the common code → read = ka. The leftover word 'books' takes **pi**.",
       None, "easy", "cd-p29", 35),
    lq("language-coding-p03", [["apples", "are", "red"], ["roses", "are", "red"]], [["to", "na", "pi"], ["to", "na", "gu"]],
       "apples", "pi", ["to", "na", "gu"],
       "'are' and 'red' are common → codes 'to na'. Sentence 1's leftover word 'apples' takes **pi**.",
       None, "medium", "cd-p30", 40),
    lq("language-coding-p04", [["train", "runs", "fast"], ["bus", "runs", "fast"], ["fast", "train"]], [["la", "jo", "me"], ["la", "jo", "fi"], ["me", "jo"]],
       "bus", "fi", ["la", "jo", "me"],
       "Sentences 1–2 share 'runs fast' ↔ 'la jo'; sentences 1–3 share 'train fast' ↔ 'me jo'. 'fast' sits in both pairs → fast = jo. Then runs = la, train = me. Sentence 2's leftovers: bus takes **fi**.",
       "Fix the word that appears in two overlapping pairs first.", "hard", "cd-p30", 55),
    lq("language-coding-p05", [["cats", "drink", "milk"], ["milk", "is", "white"], ["cats", "are", "white"]], [["ba", "da", "la"], ["la", "pa", "ka"], ["ba", "ta", "pa"]],
       "drink", "da", ["la", "pa", "ba"],
       "cats ↔ ba (sentences 1, 3); milk ↔ la (1, 2). White is common to sentences 2–3 → 'pa ka' ∩ 'ta pa' = pa. So is = ka, are = ta. Sentence 1's leftover: drink = **da**.",
       None, "medium", "cd-p30", 50),
    lq("language-coding-p06", [["sky", "is", "blue"], ["sea", "is", "deep"]], [["ta", "pa", "ka"], ["pa", "za", "la"]],
       "blue", "Cannot be determined", ["ta", "pa", "ka"],
       "Only 'is' is common → is = pa. 'Blue' can still be 'ta' or 'ka' — two codes remain → **cannot be determined**.",
       "Two possible codes after elimination = the CBD option.", "medium", "cd-p31", 40, cbd=True),
    lq("language-coding-p07", [["sum", "of", "money"], ["sum", "earned"]], [["ni", "mo", "za"], ["mo", "ka"]],
       "of", "Cannot be determined", ["ni", "za", "mo"],
       "'sum' is common → sum = mo. 'Of' can be 'ni' or 'za' — two codes remain → **cannot be determined**.",
       None, "medium", "cd-p31", 40, cbd=True),
    lq("language-coding-p08", [["he", "is", "kind"], ["she", "is", "honest"]], [["jo", "ma", "ne"], ["ka", "ma", "po"]],
       "he", "Cannot be determined", ["jo", "ma", "ne"],
       "'is' is common → is = ma. 'He' can be 'jo' or 'ne' → **cannot be determined**.",
       None, "medium", "cd-p31", 40, cbd=True),
    Q("language-coding-p09", "In a certain code language, **'come home' = '1 2'** and **'home sweet' = '2 3'**. What is the code for **'sweet home'**?",
      "3 2", ["2 3", "3 1", "1 3"],
      "'home' is common → home = 2. Then come = 1 and sweet = 3. The phrase asks 'sweet home', so sweet first: **3 2**. (2 3 reads 'home sweet'.)",
      shortcut="Phrase codes follow the phrase's own word order.", diff="medium", sub="language-coding", pat="cd-p32", t=40,
      check="3 2"),
    Q("language-coding-p10", "In a certain code language, **'go to school' = '5 7 9'**, **'to the park' = '7 2 4'** and **'school bus' = '9 8'**. What is the code for **'bus go'**?",
      "8 5", ["5 8", "8 9", "9 5"],
      "'to' is common to sentences 1–2 → to = 7. 'school' is common to 1–3 → school = 9. Sentence 3 leaves bus = 8; sentence 1 leaves go = 5. 'Bus go' = **8 5**.",
      shortcut=None, diff="hard", sub="language-coding", pat="cd-p32", t=50,
      check="8 5"),
    rq("language-coding-p11", [["apples", "are", "sweet"], ["sweet", "mango"]], [["ra", "sa", "da"], ["sa", "pa"]],
       "pa", "Mango", ["Apples", "Sweet", "Cannot be determined"],
       "'sweet' is common and 'sa' is the common code → sweet = sa. Sentence 2's leftover word 'mango' takes the leftover code **pa**. So 'pa' means mango.",
       None, "medium", "cd-p33", 40),
    rq("language-coding-p12", [["birds", "fly"], ["fly", "high"], ["birds", "sing"]], [["lo", "pe"], ["pe", "ni"], ["lo", "ra"]],
       "ra", "Sing", ["Birds", "Fly", "High"],
       "birds ↔ lo (sentences 1, 3), fly ↔ pe (1, 2). Sentence 3 leaves sing = ra, so 'ra' means **sing**.",
       "Same mapping as forward questions; only the reading direction changes.", "medium", "cd-p33", 40),
]
upsert(d["practice"], LANGQ)

finish(T, d)
