"""coding-decoding step 2: coding-idea (family overview + rearrangement and mixed-rule codes)."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _lib import *  # noqa

_spec = importlib.util.spec_from_file_location("cdh", os.path.join(HERE, "coding-decoding-helpers.py"))
cdh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cdh)
tup = cdh.tup

T = "coding-decoding"
SUB = "coding-idea"
d = load(T)

VOW = set("AEIOU")


def pair_swap(w):
    out = ""
    for i in range(0, len(w) - 1, 2):
        out += w[i + 1] + w[i]
    if len(w) % 2:
        out += w[-1]
    return out


def halves_rev(w):
    h = len(w) // 2
    if len(w) % 2:
        return w[:h][::-1] + w[h] + w[h + 1:][::-1]
    return w[:h][::-1] + w[h:][::-1]


def first_last(w):
    return w[-1] + w[1:-1] + w[0]


def vc_rule(w, dv, dc):
    return "".join(let(pos(c) + (dv if c in VOW else dc)) for c in w)


def pairs(w):
    return " | ".join(w[i:i + 2] for i in range(0, len(w), 2))


NOTES = r"""### What is coding-decoding?
In daily life we use codes all the time. A bank sends a one-time password, a shop marks a price as 'AB' instead of ₹12, and friends use short secret words. In a **coding-decoding** question, the examiner hides a word using a fixed rule. You are shown one word with its code, you work out the rule, and then you apply the **same** rule to a new word. **Coding** means turning a word into its code. **Decoding** means turning a code back into the word.

The good news: the rule is always mechanical. No vocabulary or general knowledge is tested (except in renaming questions, where you need only simple facts like 'fish live in water').

### The main families
| Family | What happens | Small example |
|---|---|---|
| Letter shift | every letter moves forward or back | CAT → DBU (+1) |
| Reversal / opposite | word written backwards, or each letter replaced by its opposite (A↔Z) | LOGIC → CIGOL |
| Rearrangement | same letters, new order | PLANET → LPNATE |
| Number coding | word becomes a number from letter positions | CAT → 24 |
| Symbol coding | each letter gets a symbol or digit | R = 6, O = 8 |
| Substitution | objects are renamed | sky is called sea |
| Language coding | whole sentences become code words | 'good day' = 'pa ki' |

### How to find any rule — step by step
1. **Count letters.** If the code has the same number of letters, compare them one by one.
2. **Same letters, new order?** Then it is rearrangement. Mark where each letter went.
3. **Different letters?** Write alphabet positions (A=1 ... Z=26) and subtract slot by slot. A constant like +2 is a shift; letters adding to 27 are opposites.
4. **Read the code backwards.** If you see the word (or a shifted word), reversal is part of the rule.
5. **Code is a number?** Add the letter positions first and compare with the code.
6. **Apply the rule exactly** to the new word. Then check one letter again.

### Rearrangement rules
- **Pair swap**: letters are swapped in pairs. PLANET → PL AN ET → LP NA TE → **LPNATE**. With an odd number of letters the last letter stays.
- **Halves reversed**: split the word in two halves and write each half backwards. MONKEY → MON | KEY → **NOM YEK**. In an odd word the middle letter stays in place.
- **First–last interchange**: only the first and last letters swap. LEMON → **NEMOL**. Sometimes the middle letters are also shifted.

### Mixed (two-step) rules
Some codes use two simple rules together:
- **Vowels one way, consonants another**: vowels (A, E, I, O, U) move +1 and consonants move −1. BASKET → **ABRJFS**.
- **Opposite then shift**: BAD → opposite YZW → +1 → **ZAX**.
- **Reverse then alternate shift**: +1, −1, +1, −1 after writing the word backwards.
- **Letters plus a number**: letters shifted, then a number such as the letter count or position sum is written after them.

Always do the steps in the same order as the sample. 'Reverse then shift' and 'shift then reverse' can give different answers when the shift changes from slot to slot.

### Must-know alphabet facts
- **EJOTY**: E=5, J=10, O=15, T=20, Y=25. Every letter is at most 2 steps from one of these.
- **Opposite pairs** (positions add to 27): A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N.
- **Wrap-around**: after Z comes A again. Y + 3 = B.

### Quick revision
- Same letters in a new order → rearrangement (pair swap, halves reversed, first–last swap).
- Different letters → subtract positions; constant = shift, sum 27 = opposite.
- Read the code backwards before trying anything complicated.
- Two-step rules: copy the order of steps from the sample.
- Always apply the rule found on the sample; never invent a new rule for the new word.
"""

PATTERNS = [
    P("cd-p1", "Pair-swap coding (adjacent letters interchanged)", "common",
      "The code has exactly the same letters as the word, and every two neighbouring letters have changed places "
      "(PLANET → LPNATE).",
      "1. Split the word into pairs from the left: PL | AN | ET.\n2. Write each pair backwards: LP | NA | TE.\n"
      "3. If the word has an odd number of letters, the last letter stays as it is.\n\n"
      "Why it works: no letter changes, only the order — so checking pairs is enough.",
      "If PLANET is written as LPNATE, how is GARDEN written?",
      f"Pairs GA | RD | EN → AG | DR | NE → **{pair_swap('GARDEN')}**."),
    P("cd-p2", "Halves reversed (each half written backwards)", "common",
      "Same letters as the word, but the first half and the second half each appear backwards "
      "(MONKEY → NOMYEK).",
      "1. Split the word into two equal halves (odd length: the middle letter stays).\n"
      "2. Reverse the first half, then reverse the second half.\n3. Apply any extra shift only after this, "
      "if the sample shows one.\n\nWhy it works: reading each half backwards in the sample shows the original halves.",
      "If MONKEY is written as NOMYEK, how is GINGER written?",
      f"GIN | GER → NIG | REG → **{halves_rev('GINGER')}**."),
    P("cd-p3", "First and last letters interchanged", "occasional",
      "Only the end letters look different: the first letter of the word is at the end of the code and the last "
      "letter is at the front. Middle letters are same or shifted by a fixed amount.",
      "1. Swap the first and last letters.\n2. Check the middle letters against the sample: unchanged, or each "
      "moved by the same k?\n3. Apply both steps to the new word.\n\nWhy it works: the middle part tells you "
      "whether a second rule is present.",
      "If LEMON is written as NEMOL, how is GRAPE written?",
      f"Swap first and last letters: G…E → E…G, middle RAP unchanged → **{first_last('GRAPE')}**."),
    P("cd-p4", "Vowel–consonant rule (different change for vowels and consonants)", "occasional",
      "Differences are not constant: vowels all move one way (say +1) while consonants move another way (say −1, "
      "or not at all).",
      "1. Write the sample's differences under each letter.\n2. Group them: what happened to the vowels? what "
      "happened to the consonants?\n3. Code the new word letter by letter, first asking 'vowel or consonant?'.\n\n"
      "Why it works: the examiner uses the letter type, not the slot, to decide the change.",
      "If BASKET is written as ABRJFS, how is PENCIL written?",
      f"Vowels +1 (A→B, E→F), consonants −1 (B→A, S→R, K→J, T→S). PENCIL → P−1, E+1, N−1, C−1, I+1, L−1 = "
      f"**{vc_rule('PENCIL', 1, -1)}**."),
    P("cd-p5", "Multi-step mixed coding", "common",
      "One simple rule does not explain the sample: e.g. letters are opposite AND shifted, or reversed AND shifted "
      "+1/−1 alternately, or letters are followed by a number.",
      "1. Test the simple rules first (shift, opposite, reverse).\n2. If a rule 'almost' works, the remaining "
      "difference is the second step (e.g. opposite letters that are all one step further).\n3. Apply the steps "
      "to the new word in the same order.\n4. For letter+number codes, solve the letters and the number separately.\n\n"
      "Why it works: every mixed rule is two basic rules in a row.",
      "If BAD is written as ZAX, how is CUP written?",
      f"Opposite of BAD = YZW; +1 → ZAX ✓. CUP → opposite {opp('CUP')} → +1 → **{shift(opp('CUP'), 1)}**."),
]
assert pair_swap("PLANET") == "LPNATE" and halves_rev("MONKEY") == "NOMYEK"
assert first_last("LEMON") == "NEMOL" and vc_rule("BASKET", 1, -1) == "ABRJFS"
assert shift(opp("BAD"), 1) == "ZAX"

qs = []
S = SUB

# ---- cd-p1 pair swap ----
w = "GARDEN"
qs.append(Q(f"{S}-p01", "In a certain code, **PLANET** is written as **LPNATE**. How is **GARDEN** written in that code?",
            pair_swap(w), ["AGDREN", "NEDRAG", "AGRDNE"],
            f"PLANET → PL | AN | ET → LP | NA | TE: each pair of letters is swapped. GARDEN → {pairs(w)} → "
            f"**{pair_swap(w)}**.",
            "Same letters in the code = rearrangement. Swap in pairs from the left.",
            "easy", S, "cd-p1", 30, check=pair_swap(w)))
w = "WINDOW"
assert pair_swap("SPORT") == "PSROT"
qs.append(Q(f"{S}-p02", "In a certain code, **SPORT** is written as **PSROT**. How is **WINDOW** written in that code?",
            pair_swap(w), ["IWNDWO", "WODNIW", "IWDNOW"],
            f"SPORT → SP | OR | T → PS | RO | T (pairs swapped, last odd letter stays). WINDOW → {pairs(w)} → "
            f"**{pair_swap(w)}**.",
            "Odd sample, even target: every pair is swapped, nothing is left over.",
            "medium", S, "cd-p1", 40, check=pair_swap(w)))
assert pair_swap("CANDLE") == "ACDNEL"
qs.append(Q(f"{S}-p03", "In a certain code, **CANDLE** is written as **ACDNEL**. Which word is written as "
            f"**{pair_swap('SILVER')}** in that code?",
            "SILVER", ["SLIVER", "LIVERS", "SILVRE"],
            f"CANDLE → CA | ND | LE → AC | DN | EL: pairs swapped. Swapping pairs again undoes the code: "
            f"{pairs(pair_swap('SILVER'))} → SI | LV | ER → **SILVER**.",
            "A pair swap is its own reverse — apply the same swap to the code to get the word.",
            "medium", S, "cd-p1", 40, check=pair_swap(pair_swap("SILVER"))))
assert pair_swap("SLIVER") != pair_swap("SILVER")

# ---- cd-p2 halves reversed ----
w = "GINGER"
qs.append(Q(f"{S}-p04", "In a certain code, **MONKEY** is written as **NOMYEK**. How is **GINGER** written in that code?",
            halves_rev(w), ["REGNIG", "IGNEGR", "NIGERG"],
            f"MONKEY → MON | KEY → NOM | YEK: each half written backwards. GINGER → GIN | GER → NIG | REG → "
            f"**{halves_rev(w)}**.",
            "Read each half of the code backwards — you get MON and KEY.",
            "easy", S, "cd-p2", 30, check=halves_rev(w)))
w = "TIGER"
assert halves_rev("CAMEL") == "ACMLE"
qs.append(Q(f"{S}-p05", "In a certain code, **CAMEL** is written as **ACMLE**. How is **TIGER** written in that code?",
            halves_rev(w), ["ITERG", "REGIT", "ITGER"],
            f"CAMEL → CA | M | EL → AC | M | LE: the middle letter stays, each half is reversed. "
            f"TIGER → TI | G | ER → IT | G | RE → **{halves_rev(w)}**.",
            "Odd length: keep the middle letter fixed and flip the two sides.",
            "medium", S, "cd-p2", 40, check=halves_rev(w)))
ms = shift(halves_rev("MOTHER"), 1)
w = "SISTER"
ans = shift(halves_rev(w), 1)
qs.append(Q(f"{S}-p06", f"In a certain code, **MOTHER** is written as **{ms}**. How is **SISTER** written in that code?",
            ans, [halves_rev(w), shift(w, 1), shift(halves_rev(w), -1)],
            f"MOTHER → halves reversed = {halves_rev('MOTHER')}; then each letter +1 → {ms} ✓. "
            f"SISTER → SIS | TER → {halves_rev(w)} → +1 → **{ans}**.",
            "Two steps: flip each half, then +1 on every letter. The code starts with U = T+1, and T is the last "
            "letter of the first half MOT — proof that the halves were flipped first.",
            "hard", S, "cd-p2", 60, check=ans))

# ---- cd-p3 first-last ----
w = "GRAPE"
qs.append(Q(f"{S}-p07", "In a certain code, **LEMON** is written as **NEMOL**. How is **GRAPE** written in that code?",
            first_last(w), ["EPARG", "ERAPE", "GRAPE"[::-1][0] + "RPAG"],
            f"In LEMON → NEMOL only the first and last letters (L, N) have changed places. GRAPE → **{first_last(w)}**.",
            "Middle letters unchanged → only the ends swap.",
            "easy", S, "cd-p3", 30, check=first_last(w)))
samp = "PENCIL"
sc = samp[-1] + shift(samp[1:-1], 1) + samp[0]
w = "MARKET"
ans = w[-1] + shift(w[1:-1], 1) + w[0]
qs.append(Q(f"{S}-p08", f"In a certain code, **{samp}** is written as **{sc}**. How is **{w}** written in that code?",
            ans, [first_last(w), w[-1] + shift(w[1:-1], -1) + w[0], w[0] + shift(w[1:-1], 1) + w[-1]],
            f"{samp} → {sc}: the first and last letters are interchanged (P…L → L…P) and the middle letters ENCI "
            f"each move +1 → FODJ. {w}: T…M at the ends, middle ARKE +1 → {shift(w[1:-1], 1)} → **{ans}**.",
            "Two jobs: swap the ends, shift the middle by the same +1.",
            "medium", S, "cd-p3", 45, check=ans))

# ---- cd-p4 vowel/consonant ----
w = "PENCIL"
ans = vc_rule(w, 1, -1)
qs.append(Q(f"{S}-p09", "In a certain code, **BASKET** is written as **ABRJFS**. How is **PENCIL** written in that code?",
            ans, [shift(w, -1), vc_rule(w, -1, 1), vc_rule(w, 1, 1)],
            f"BASKET → ABRJFS: {tup('BASKET', 'ABRJFS')}. Vowels (A, E) move +1, consonants move −1. "
            f"PENCIL: P−1 = O, E+1 = F, N−1 = M, C−1 = B, I+1 = J, L−1 = K → **{ans}**.",
            "Mark vowels first; they are the only letters that go forward.",
            "medium", S, "cd-p4", 50, check=ans))
samp = "MANGO"
sc = vc_rule(samp, 0, 2)
w = "RIVER"
ans = vc_rule(w, 0, 2)
qs.append(Q(f"{S}-p10", f"In a certain code, **{samp}** is written as **{sc}**. How is **{w}** written in that code?",
            ans, [shift(w, 2), vc_rule(w, 2, 0), vc_rule(w, 0, 1)],
            f"{samp} → {sc}: {tup(samp, sc)}. Vowels (A, O) stay the same; each consonant moves +2. "
            f"{w}: R+2 = T, I stays, V+2 = X, E stays, R+2 = T → **{ans}**.",
            "Vowels unchanged in the sample → keep them unchanged; shift only consonants.",
            "medium", S, "cd-p4", 45, check=ans))
samp = "STONE"
sc = vc_rule(samp, -1, 1)
w = "TULIP"
ans = vc_rule(w, -1, 1)
qs.append(Q(f"{S}-p11", f"In a certain code, **{samp}** is written as **{sc}**. Which of the following is the code for **{w}**?",
            ans, [vc_rule(w, 1, -1), shift(w, 1), vc_rule(w, -1, 2)],
            f"{samp} → {sc}: {tup(samp, sc)}. Vowels move −1, consonants move +1. "
            f"{w}: T+1 = U, U−1 = T, L+1 = M, I−1 = H, P+1 = Q → **{ans}**.",
            "The vowels are the letters that went backwards — spot them first.",
            "hard", S, "cd-p4", 50, check=ans))

# ---- cd-p5 multi-step ----
w = "CUP"
ans = shift(opp(w), 1)
qs.append(Q(f"{S}-p12", "In a certain code, **BAD** is written as **ZAX**. How is **CUP** written in that code?",
            ans, [opp(w), shift(opp(w), -1), shift(w, 1)],
            f"Opposite letters of BAD are Y, Z, W; each +1 gives Z, A, X ✓. CUP → opposites {opp(w)} → +1 → **{ans}**.",
            "When the code is 'almost opposite', the gap is the second step.",
            "medium", S, "cd-p5", 50, check=ans))
alt = [1, -1]
samp = "FORM"
sc = shift(rev(samp), alt)
w = "SALT"
ans = shift(rev(w), alt)
qs.append(Q(f"{S}-p13", f"In a certain code, **{samp}** is written as **{sc}**. How is **{w}** written in that code?",
            ans, [shift(w, alt), shift(rev(w), [-1, 1]), shift(rev(w), 1)],
            f"{samp} backwards = {rev(samp)}; then +1, −1, +1, −1 → {sc} ✓. {w} backwards = {rev(w)}; "
            f"+1, −1, +1, −1 → **{ans}**.",
            "Reverse first, then the alternating shift — the sample's first code letter N = M+1 comes from the "
            "last letter M, which proves the reversal came first.",
            "hard", S, "cd-p5", 60, check=ans))
samp = "LAMP"
sc = shift(samp, 2) + str(2 * len(samp))
w = "TABLE"
ans = shift(w, 2) + str(2 * len(w))
qs.append(Q(f"{S}-p14", f"In a certain code, **{samp}** is written as **{sc}**. How is **{w}** written in that code?",
            ans, [shift(w, 2) + "8", shift(w, 1) + "10", shift(w, 2) + str(psum(w))],
            f"Letter part: {tup(samp, shift(samp, 2))} → +2 each. Number part: 8 = 2 × (4 letters). "
            f"{w}: letters +2 → {shift(w, 2)}; number = 2 × 5 = 10 → **{ans}**.",
            "Solve letters and number separately; recompute the number for the new word.",
            "medium", S, "cd-p5", 50, check=ans))

set_sub(d, SUB, notes=NOTES.strip(), patterns=PATTERNS)
upsert(d["practice"], qs)
finish(T, d)
