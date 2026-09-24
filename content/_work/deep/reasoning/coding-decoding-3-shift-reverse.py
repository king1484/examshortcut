"""coding-decoding step 3: letter-shift-coding and reverse-coding."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _lib import *  # noqa

_spec = importlib.util.spec_from_file_location("cdh", os.path.join(HERE, "coding-decoding-helpers.py"))
cdh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cdh)
tup, opps = cdh.tup, cdh.opps

T = "coding-decoding"
d = load(T)

# =====================================================================
# letter-shift-coding
# =====================================================================
SUB = "letter-shift-coding"
NOTES_SHIFT = r"""### What is letter-shift coding?
Think of the alphabet as a circular road with 26 houses, A to Z. In **letter-shift coding** every letter of a word walks forward (or backward) a fixed number of houses. If every letter walks 2 houses forward, CAT becomes ECV. This is the most common coding question in SSC, Railway and Banking papers.

### Step 1: know the positions
Each letter has a **position number**: A=1, B=2 ... Z=26. Do not count on your fingers every time. Learn the **EJOTY** anchors:

| E | J | O | T | Y |
|---|---|---|---|---|
| 5 | 10 | 15 | 20 | 25 |

Any letter is at most 2 steps from an anchor. For example, R = T − 2 = 18 and H = J − 2 = 8.

### Step 2: find the shift
Write the sample word and its code one above the other. For each slot, subtract: code position − word position. The list of answers is the **shift tuple**.

Example: KITE → MKVG. K(11)→M(13) is +2, I→K +2, T→V +2, E→G +2. The tuple is (+2, +2, +2, +2), a **flat shift**.

### Wrap-around
After Z the road starts again at A. So Y + 3 = B (Y→Z→A→B). In numbers: if the new position is more than 26, subtract 26. If it is 0 or less, add 26. Example: C − 5 → 3 − 5 = −2 → −2 + 26 = 24 = X.

### Types of shift you will meet
1. **Flat shift**: every letter moves by the same number, e.g. +2 or −3.
2. **Per-slot (rising or falling) shift**: 1st letter +1, 2nd +2, 3rd +3 ... or −1, −2, −3 ... The tuple changes but follows a pattern.
3. **Alternating shift**: +1, −1, +1, −1 ... or odd places +2 and even places −2.
4. **Length-based shift**: each letter moves by the number of letters in the word. CAT (3 letters) → FDW; FISH (4 letters) → JMWL. When two samples of different length show different flat shifts, check the letter count.
5. **Decoding**: the code is given and the word is asked. Run the tuple backwards: where the rule adds 2, you subtract 2.

### A full worked example
**Q.** If WORD is written as XQUH, how is BOOK written?

W→X +1, O→Q +2, R→U +3, D→H +4. The tuple rises: (+1, +2, +3, +4). Apply it to BOOK: B+1 = C, O+2 = Q, O+3 = R, K+4 = O. Answer **CQRO**.

Notice that the two O's in BOOK get **different** codes (Q and R). In per-slot rules the slot decides the shift, not the letter.

### Speed habits
- Find the shift from the **first two letters** and confirm it with one more letter before coding.
- Look at the options: usually only one option has the right **first** letter. Check the last letter to be sure.
- For decoding, code your chosen option forward once. If it gives the code, you are right.

### Quick revision
- Positions: A=1 ... Z=26; anchors E5, J10, O15, T20, Y25.
- Shift tuple = code position − word position, slot by slot.
- Flat, rising/falling, alternating and length-based shifts are the four families.
- Wrap-around: above 26 subtract 26; 0 or below add 26.
- Decode = subtract the tuple. Check the answer by coding it forward.
"""

PAT_SHIFT = [
    P("cd-p6", "Flat shift (+k or −k on every letter)", "very common",
      "Every letter of the code is the same number of places ahead of (or behind) the matching letter of the word.",
      "1. Subtract positions for two or three letters of the sample.\n2. If all differences are equal, that is k.\n"
      "3. Add k to each letter of the new word (wrap after Z).\n\nWhy it works: a flat rule treats every letter the same.",
      "If KITE is written as MKVG, how is LAMP written?",
      f"{tup('KITE', 'MKVG')} → flat +2. LAMP +2 → **{shift('LAMP', 2)}**.",
      formula=r"\text{code}_i = \text{letter}_i + k \pmod{26}"),
    P("cd-p7", "Per-slot shift (rising, falling or fixed tuple)", "common",
      "The differences are not equal but follow a pattern by position: +1, +2, +3, +4 or −1, −2, −3 or (+3, +1, +4...).",
      "1. Write the full shift tuple from the sample.\n2. Apply the same tuple to the new word, slot by slot.\n"
      "3. Repeated letters may get different codes — that is expected.\n\nWhy it works: the slot number decides the shift.",
      "If WORD is written as XQUH, how is BOOK written?",
      f"{tup('WORD', 'XQUH')} → (+1, +2, +3, +4). BOOK → **{shift('BOOK', [1, 2, 3, 4])}**.",
      formula=r"\text{code}_i = \text{letter}_i + d_i"),
    P("cd-p8", "Decoding (code given, word asked)", "common",
      "The question gives a code and asks 'which word is written as ...?' — the direction is reversed.",
      "1. Find the rule from the sample pair.\n2. Undo it: subtract where the rule adds, add where it subtracts.\n"
      "3. Code your answer forward once to confirm.\n\nWhy it works: decoding is the same rule played backwards.",
      "If DOG is written as FQI, which word is written as DKTF?",
      f"Rule +2, so decode −2: DKTF → **{shift('DKTF', -2)}**.",
      formula=r"\text{letter}_i = \text{code}_i - d_i"),
    P("cd-p9", "Alternating or odd/even-place shift", "common",
      "The shifts swing: +1, −1, +1, −1 ... or letters in odd places move one way and letters in even places the other way.",
      "1. Write the tuple and look for a repeating 2-step cycle.\n2. Apply the cycle to the new word from the first letter.\n"
      "3. For a longer new word, just keep repeating the cycle.\n\nWhy it works: the rule depends only on odd/even place.",
      "If FLOWER is written as GKPVFQ, how is GARDEN written?",
      f"{tup('FLOWER', 'GKPVFQ')} → +1, −1 repeating. GARDEN → **{shift('GARDEN', [1, -1])}**."),
    P("cd-p10", "Shift equal to the number of letters", "occasional",
      "Two or more samples of different lengths each have a flat shift, and the shift equals the word's letter count "
      "(3-letter word +3, 4-letter word +4), or its negative.",
      "1. Find the flat shift of each sample.\n2. Compare it with the word length.\n3. For the new word, count its "
      "letters and shift by that number.\n\nWhy it works: the shift is not fixed; it is tied to the length.",
      "If CAT is written as FDW and FISH as JMWL, how is TIGER written?",
      f"CAT: +3 (3 letters); FISH: +4 (4 letters). TIGER has 5 letters → +5 → **{shift('TIGER', 5)}**."),
]
assert shift("KITE", 2) == "MKVG" and shift("WORD", [1, 2, 3, 4]) == "XQUH"
assert shift("DOG", 2) == "FQI" and shift("BIRD", 2) == "DKTF"
assert shift("FLOWER", [1, -1]) == "GKPVFQ" and shift("CAT", 3) == "FDW" and shift("FISH", 4) == "JMWL"

S = SUB
qs = []
# cd-p6 flat
w = "LAMP"; a = shift(w, 2)
qs.append(Q(f"{S}-p01", "In a certain code, **KITE** is written as **MKVG**. How is **LAMP** written in that code?",
            a, [shift(w, 1), shift(w, 3), shift(w, -2)],
            f"{tup('KITE', 'MKVG')}: flat **+2**. LAMP: L+2 = N, A+2 = C, M+2 = O, P+2 = R → **{a}**.",
            "Only one option starts with N (L+2); confirm with the last letter R.",
            "easy", S, "cd-p6", 30, check=a))
w = "WATER"; a = shift(w, -3)
assert shift("HOUSE", -3) == "ELRPB"
qs.append(Q(f"{S}-p02", "In a certain code, **HOUSE** is written as **ELRPB**. How is **WATER** written in that code?",
            a, [shift(w, 3), shift(w, -2), "TXQBP"],
            f"{tup('HOUSE', 'ELRPB')}: flat **−3**. WATER: W−3 = T, A−3 = X (wrap: 1−3+26 = 24), T−3 = Q, "
            f"E−3 = B, R−3 = O → **{a}**.",
            "Backward shift with wrap: A − 3 = X. Anchor check: R = T − 2, so R − 3 = O.",
            "medium", S, "cd-p6", 40, check=a))
# cd-p7 per-slot
w = "BOOK"; a = shift(w, [1, 2, 3, 4])
qs.append(Q(f"{S}-p03", "In a certain code, **WORD** is written as **XQUH**. How is **BOOK** written in that code?",
            a, [shift(w, 1), "CQQO", shift(w, [4, 3, 2, 1])],
            f"{tup('WORD', 'XQUH')}: tuple (+1, +2, +3, +4). BOOK: B+1 = C, O+2 = Q, O+3 = R, K+4 = O → **{a}**.",
            "The two O's get different codes (Q, R) because the slot decides the shift.",
            "medium", S, "cd-p7", 45, check=a))
tp = [-1, -2, -3, -4, -5]
sc = shift("PLANT", tp); w = "GRASS"; a = shift(w, tp)
qs.append(Q(f"{S}-p04", f"In a certain code, **PLANT** is written as **{sc}**. How is **GRASS** written in that code?",
            a, [shift(w, -1), shift(w, [1, 2, 3, 4, 5]), shift(w, [-5, -4, -3, -2, -1])],
            f"{tup('PLANT', sc)}: tuple (−1, −2, −3, −4, −5). GRASS: G−1 = F, R−2 = P, A−3 = X, S−4 = O, S−5 = N "
            f"→ **{a}**.",
            "Falling tuple; A − 3 wraps to X.",
            "hard", S, "cd-p7", 55, check=a))
# cd-p8 decode
a = shift("DKTF", -2)
qs.append(Q(f"{S}-p05", "In a certain code, **DOG** is written as **FQI**. Which word is written as **DKTF** in that code?",
            a, ["FMVH", "CJSE", "BIRT"],
            f"{tup('DOG', 'FQI')}: rule +2. To decode, subtract 2: D→B, K→I, T→R, F→D → **{a}**.",
            "Decode = subtract. Check: BIRD + 2 = DKTF ✓.",
            "easy", S, "cd-p8", 30, check="BIRD"))
assert shift("CHAIR", 3) == "FKDLU"
a = shift("ZDWHU", -3)
qs.append(Q(f"{S}-p06", "In a certain code, **CHAIR** is written as **FKDLU**. Which word is written as **ZDWHU**?",
            a, ["CGZKX", "XBUFS", "WATES"],
            f"{tup('CHAIR', 'FKDLU')}: rule +3. Decode with −3: Z→W, D→A, W→T, H→E, U→R → **{a}**.",
            "Z − 3 = W; D − 3 = A. The word WATER appears after the first two letters.",
            "medium", S, "cd-p8", 40, check="WATER"))
tp = [1, 2, 3, 4]
code = shift("MARK", tp)
opts = ["MARK", "MASK", "LARK", "PARK"]
assert [o for o in opts if shift(o, tp) == code] == ["MARK"]
assert shift("PEN", [1, 2, 3]) == "QGQ"
qs.append(Q(f"{S}-p07", f"In a certain code, **PEN** is written as **QGQ**. Using the same rule, which word is written as **{code}**?",
            "MARK", ["MASK", "LARK", "PARK"],
            f"{tup('PEN', 'QGQ')}: tuple (+1, +2, +3), so the 4th letter moves +4. Decode {code} with (−1, −2, −3, −4): "
            f"{code[0]}→M, {code[1]}→A, {code[2]}→R, {code[3]}→K → **MARK**.",
            "Code each option forward: MASK gives NCVO, LARK gives MCUO, PARK gives QCUO — only MARK gives NCUO.",
            "hard", S, "cd-p8", 55, check=shift(code, [-1, -2, -3, -4])))
# cd-p9 alternating
w = "GARDEN"; a = shift(w, [1, -1])
qs.append(Q(f"{S}-p08", "In a certain code, **FLOWER** is written as **GKPVFQ**. How is **GARDEN** written in that code?",
            a, [shift(w, [-1, 1]), shift(w, 1), "HZSCFO"],
            f"{tup('FLOWER', 'GKPVFQ')}: +1, −1 repeating. GARDEN: G+1 = H, A−1 = Z, R+1 = S, D−1 = C, E+1 = F, "
            f"N−1 = M → **{a}**.",
            "Two-step cycle (+1, −1); A − 1 wraps to Z.",
            "medium", S, "cd-p9", 45, check=a))
sc = shift("SCHOOL", [2, -2]); w = "COLLEGE"; a = shift(w, [2, -2])
qs.append(Q(f"{S}-p09", f"In a certain code, **SCHOOL** is written as **{sc}**. How is **COLLEGE** written in that code?",
            a, [shift(w, [-2, 2]), shift(w, 2), a[:-1] + shift(w[-1], -2)],
            f"{tup('SCHOOL', sc)}: odd places +2, even places −2. COLLEGE has 7 letters, so the 7th (odd) letter "
            f"also gets +2: C+2 = E, O−2 = M, L+2 = N, L−2 = J, E+2 = G, G−2 = E, E+2 = G → **{a}**.",
            "The new word is longer than the sample — just continue the +2, −2 cycle.",
            "medium", S, "cd-p9", 50, check=a))
# cd-p10 length based
w = "TIGER"; a = shift(w, 5)
qs.append(Q(f"{S}-p10", "In a certain code, **CAT** is written as **FDW** and **FISH** is written as **JMWL**. "
            "How is **TIGER** written in that code?",
            a, [shift(w, 4), shift(w, 3), shift(w, 6)],
            f"CAT → FDW is +3 and CAT has 3 letters; FISH → JMWL is +4 and FISH has 4 letters. So each letter moves "
            f"by the number of letters. TIGER has 5 letters → +5: T→Y, I→N, G→L, E→J, R→W → **{a}**.",
            "Different flat shifts for different lengths = letter-count rule.",
            "medium", S, "cd-p10", 45, check=a))
s1, s2 = shift("DOG", -3), shift("BIRD", -4)
w = "MONKEY"; a = shift(w, -6)
qs.append(Q(f"{S}-p11", f"In a certain code, **DOG** is written as **{s1}** and **BIRD** is written as **{s2}**. "
            "How is **MONKEY** written in that code?",
            a, [shift(w, 6), shift(w, -5), shift(w, -4)],
            f"DOG → {s1}: each letter −3 (3 letters). BIRD → {s2}: each letter −4 (4 letters). MONKEY has 6 letters "
            f"→ −6: M→G, O→I, N→H, K→E, E→Y (wrap), Y→S → **{a}**.",
            "Backward by the letter count; E − 6 wraps: 5 − 6 + 26 = 25 = Y.",
            "hard", S, "cd-p10", 55, check=a))

set_sub(d, SUB, notes=NOTES_SHIFT.strip(), patterns=PAT_SHIFT)
upsert(d["practice"], qs)

# =====================================================================
# reverse-coding
# =====================================================================
SUB = "reverse-coding"
NOTES_REV = r"""### What is reverse coding?
Hold a word in front of a mirror and you see it backwards. **Reverse coding** writes the word from right to left: LOGIC becomes CIGOL. Examiners like to add one more step, such as a shift after reversing, or they replace each letter by its **opposite letter** in the alphabet. All three ideas are covered in this lesson.

### 1. Pure reversal
Write the last letter first and the first letter last. GARDEN → NEDRAG. Test: read the code from right to left. If you get the original word, the rule is pure reversal.

### 2. Reverse and shift
The code is the reversed word with every letter moved by the same amount.

Example: PAINT → UOJBQ. Reverse PAINT → TNIAP. Compare TNIAP with UOJBQ: T→U, N→O, I→J, A→B, P→Q — each +1. So the rule is **reverse, then +1**.

When the shift is the same for every letter, 'reverse then shift' and 'shift then reverse' give the same result. When the shift changes by slot (+1, +2, +3 ...), the order matters, so copy the order used in the sample.

### 3. Opposite letters
Fold the alphabet in the middle: A sits on Z, B on Y, C on X, and so on. Each pair is called **opposite letters**. The positions of a pair always add up to **27**.

| A-Z | B-Y | C-X | D-W | E-V | F-U | G-T |
|---|---|---|---|---|---|---|
| **H-S** | **I-R** | **J-Q** | **K-P** | **L-O** | **M-N** | |

Memory aid: 'AZ', 'BY', 'CX' then 'DeW', 'EVe', 'FUn', 'GT', 'HS', 'IR', 'JQ', 'KP', 'LO', 'MN'. To find an opposite quickly: opposite = 27 − position. Example: opposite of K(11) = 27 − 11 = 16 = P.

How to spot it: take the first letter of the word and the first letter of the code. If their positions add to 27, check one more letter. Example: WHITE → DSRGV. W(23) + D(4) = 27, H(8) + S(19) = 27. Opposite letters confirmed.

### 4. Opposite and reverse together
Some codes first write the opposite letters and then reverse the whole word. LAMP → opposites OZNK → reversed **KNZO**. Test: if the first code letter is the opposite of the **last** word letter, both steps are present.

### Decoding
- Reversal undoes itself: reverse the code to get the word.
- Opposite letters also undo themselves: the opposite of the opposite is the same letter.
- For reverse + shift, first un-shift, then reverse (or the other way; with a flat shift both orders work).

### Common traps
- Reversing but forgetting the extra shift.
- Using 26 instead of 27 for opposites (26 − 11 = 15 = O is wrong; the opposite of K is P).
- In odd-length words the middle letter stays in the middle after reversal, but it still gets the shift or opposite.

### Quick revision
- Read the code backwards first: word appears → reversal.
- Word appears shifted → reverse + shift; find k from one letter.
- Positions add to 27 → opposite letters; opposite = 27 − position.
- First code letter pairs with the last word letter → opposite + reverse.
- Reversal and opposite undo themselves when decoding.
"""

PAT_REV = [
    P("cd-p11", "Pure reversal", "common",
      "The code has the same letters as the word, written from right to left (GARDEN → NEDRAG).",
      "1. Read the code backwards; you should see the sample word.\n2. Write the new word backwards.\n"
      "3. For decoding, reverse the code.\n\nWhy it works: reversal is its own undo.",
      "If GARDEN is written as NEDRAG, how is FLOWER written?",
      f"Pure reversal → **{rev('FLOWER')}**."),
    P("cd-p12", "Reverse and then shift", "common",
      "Reading the code backwards gives the sample word with every letter moved by the same (or patterned) amount.",
      "1. Reverse the sample word.\n2. Compare the reversed word with the code letter by letter to find the shift.\n"
      "3. Reverse the new word and apply the same shift in the same order.\n\nWhy it works: two simple rules in a row.",
      "If PAINT is written as UOJBQ, how is BRUSH written?",
      f"PAINT reversed = TNIAP; TNIAP → UOJBQ is +1. BRUSH reversed = HSURB; +1 → **{shift(rev('BRUSH'), 1)}**.",
      formula=r"\text{code} = \text{shift}_k(\text{reverse}(w))"),
    P("cd-p13", "Opposite letters (positions add to 27)", "common",
      "Code letters look far from the word letters, and each word letter + its code letter = 27 (A↔Z, M↔N).",
      "1. Add the positions of the first word letter and first code letter; 27 means opposites.\n"
      "2. Confirm with one more letter.\n3. Write the opposite of each letter of the new word (27 − position).\n\n"
      "Why it works: opposite pairs are fixed, so the code is a simple look-up.",
      "If WHITE is written as DSRGV, how is GREEN written?",
      f"W+D = 23+4 = 27 → opposites. GREEN: {opps('GREEN')} → **{opp('GREEN')}**.",
      formula=r"\text{opposite}(p) = 27 - p"),
    P("cd-p14", "Opposite letters plus reversal", "occasional",
      "The first code letter is the opposite of the LAST word letter; the code is the opposite word read backwards.",
      "1. Pair the first code letter with the last word letter (sum 27).\n2. For the new word, write the opposite letters, "
      "then reverse the result.\n\nWhy it works: both steps are self-undoing, so the order does not change the answer.",
      "If LAMP is written as KNZO, how is DESK written?",
      f"LAMP → opposites OZNK → reversed KNZO ✓. DESK → opposites {opp('DESK')} → reversed **{rev(opp('DESK'))}**."),
]
assert shift(rev("PAINT"), 1) == "UOJBQ" and opp("WHITE") == "DSRGV" and rev(opp("LAMP")) == "KNZO"

S = SUB
qs = []
# cd-p11
w = "FLOWER"; a = rev(w)
qs.append(Q(f"{S}-p01", "In a certain code, **GARDEN** is written as **NEDRAG**. How is **FLOWER** written in that code?",
            a, ["REWLOF", "RWEOLF", "FLOWER"[1:] + "F"],
            f"NEDRAG read backwards is GARDEN → pure reversal. FLOWER backwards → **{a}**.",
            "Read the code right to left — the word appears, so just reverse.",
            "easy", S, "cd-p11", 25, check=a))
a = rev("TEKCOP")
qs.append(Q(f"{S}-p02", "In a certain code, **MOBILE** is written as **ELIBOM**. Which word is written as **TEKCOP** in that code?",
            a, ["PACKET", "POCKTE", "ROCKET"],
            f"ELIBOM backwards is MOBILE → the rule is reversal. Reverse TEKCOP → **{a}**.",
            "Reversal undoes itself — reverse the code.",
            "easy", S, "cd-p11", 25, check="POCKET"))
# cd-p12
w = "BRUSH"; a = shift(rev(w), 1)
qs.append(Q(f"{S}-p03", "In a certain code, **PAINT** is written as **UOJBQ**. How is **BRUSH** written in that code?",
            a, [shift(w, 1), rev(w), shift(rev(w), -1)],
            f"PAINT reversed = TNIAP; {tup('TNIAP', 'UOJBQ')} → reverse, then +1. BRUSH reversed = HSURB; +1 → **{a}**.",
            "First code letter U = T + 1, and T is the last letter of PAINT → reversal + 1.",
            "medium", S, "cd-p12", 40, check=a))
sc = shift(rev("CLOUD"), -2); w = "STORM"; a = shift(rev(w), -2)
qs.append(Q(f"{S}-p04", f"In a certain code, **CLOUD** is written as **{sc}**. How is **STORM** written in that code?",
            a, [shift(w, -2), shift(rev(w), 2), rev(w)],
            f"CLOUD reversed = DUOLC; {tup('DUOLC', sc)} → reverse, then −2. STORM reversed = MROTS; −2 → **{a}**.",
            "Reverse, then subtract 2 from each letter.",
            "medium", S, "cd-p12", 45, check=a))
tp = [1, 2, 3, 4]
sc = shift(rev("NOTE"), tp); w = "BOAT"; a = shift(rev(w), tp)
qs.append(Q(f"{S}-p05", f"In a certain code, **NOTE** is written as **{sc}**. How is **BOAT** written in that code?",
            a, [rev(shift(w, tp)), shift(rev(w), 1), shift(w, tp)],
            f"NOTE reversed = ETON; {tup('ETON', sc)} → reverse, then (+1, +2, +3, +4). BOAT reversed = TAOB; "
            f"T+1 = U, A+2 = C, O+3 = R, B+4 = F → **{a}**.",
            "With a rising tuple the order matters: shifting BOAT first and then reversing gives XDQC — a trap option.",
            "hard", S, "cd-p12", 60, check=a))
# cd-p13
assert opp("BOY") == "YLB"
w = "GIRL"; a = opp(w)
qs.append(Q(f"{S}-p06", "In a certain code, **BOY** is written as **YLB**. How is **GIRL** written in that code?",
            a, [shift(w, 1), "TRIP", rev(a)],
            f"B(2)+Y(25) = 27, O(15)+L(12) = 27 → opposite letters. GIRL: {opps(w)} → **{a}**.",
            "27-sum check, then the opposite-pairs table.",
            "easy", S, "cd-p13", 30, check=a))
w = "GREEN"; a = opp(w)
qs.append(Q(f"{S}-p07", "In a certain code, **WHITE** is written as **DSRGV**. How is **GREEN** written in that code?",
            a, ["TIVVN", "SIVVM", rev(a)],
            f"W(23)+D(4) = 27, H(8)+S(19) = 27 → opposite letters. GREEN: {opps(w)} → **{a}**.",
            "Opposite = 27 − position: G(7) → 20 = T, R(18) → 9 = I, E(5) → 22 = V, N(14) → 13 = M.",
            "medium", S, "cd-p13", 35, check=a))
assert opp("PAPER") == "KZKVI"
a = opp("XLOW")
qs.append(Q(f"{S}-p08", "In a certain code, **PAPER** is written as **KZKVI**. Which word is written as **XLOW** in that code?",
            a, ["CORD", "BOLD", "COLT"],
            f"P(16)+K(11) = 27 → opposite letters. Opposites undo themselves: X↔C, L↔O, O↔L, W↔D → **{a}**.",
            "Decode opposites with the same table — no subtraction needed.",
            "medium", S, "cd-p13", 35, check="COLD"))
# cd-p14
w = "DESK"; a = rev(opp(w))
qs.append(Q(f"{S}-p09", "In a certain code, **LAMP** is written as **KNZO**. How is **DESK** written in that code?",
            a, [opp(w), rev(w), "PHWV"],
            f"LAMP → opposite letters OZNK → reversed KNZO ✓. DESK → opposites {opp(w)} → reversed **{a}**.",
            "First code letter K is the opposite of the last letter P → opposite + reverse.",
            "medium", S, "cd-p14", 45, check=a))
code = rev(opp("HOUSE"))
opts = ["HOUSE", "MOUSE", "HORSE", "HOSES"]
assert [o for o in opts if rev(opp(o)) == code] == ["HOUSE"]
assert rev(opp("SMART")) == "GIZNH"
qs.append(Q(f"{S}-p10", f"In a certain code, **SMART** is written as **GIZNH**. Which word is written as **{code}** in that code?",
            "HOUSE", ["MOUSE", "HORSE", "HOSES"],
            f"SMART → opposites HNZIG → reversed GIZNH ✓ (opposite + reverse). Decode {code}: reverse → {rev(code)}, "
            f"then opposites → **HOUSE**.",
            "Both steps undo themselves — reverse the code, then take opposites.",
            "hard", S, "cd-p14", 55, check=opp(rev(code))))

set_sub(d, SUB, notes=NOTES_REV.strip(), patterns=PAT_REV)
upsert(d["practice"], qs)
finish(T, d)
