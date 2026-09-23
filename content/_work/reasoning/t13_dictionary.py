# build dictionary-order topic (topic 13)
import math
from itertools import permutations
import common as C

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def word_rank(w):
    """1-based dictionary rank of w among all arrangements of its letters."""
    rem = sorted(w)
    rank = 1
    for ch in w:
        rank += sum(1 for c in rem if c < ch) * math.factorial(len(rem) - 1)
        rem.remove(ch)
    return rank


def brute_rank(w):
    return sorted(set(permutations(w))).index(tuple(w)) + 1


subs = []

subs.append(C.sub(
    'dict-idea', 'Dictionary order rules',
    "Words sort letter by letter from the left. At the first position where two words differ, the word with the earlier alphabet comes first — everything after that position is irrelevant. Two refinements decide the tricky cases:\n\n1. **Prefix rule**: if one word runs out of letters while matching the other (SCAN vs SCANTY), the **shorter word comes first** — an ending acts like a space, and a space precedes every letter. (But SCANDAL vs SCANTY is settled at the 5th letter: D < T, so SCANDAL < SCANTY.)\n2. **No skipping**: compare position by position; a later difference never overrides an earlier one.\n\nMethod for 5-word arrangements: build the words' common prefixes on paper, sort group by group, then read off the asked slot (first / middle / last).",
    tricks=[
        C.T(
            'Find the first split point',
            "Write the words one under another and slide a finger left to right until the letters first differ. That single column decides the entire comparison — ignore all later letters.",
            "**Q.** Order: SIGN, SIGHT, SIGNAL.\n\n**Sol.** All start SIG. 4th letters: N, H, N → SIGHT (H) before the rest; SIGN vs SIGNAL: SIGN is a prefix → SIGN first. Order: SIGHT, SIGN, SIGNAL.",
            "The first differing letter settles everything; prefix pairs end shortest-first."),
    ],
    mistakes=[
        "Judging words by length instead of first-difference.",
        "Putting SCANDAL after SCANTY because 'scanty feels later' — compare D vs T.",
        "Forgetting the prefix rule: the shorter of two prefix words leads.",
    ]))

subs.append(C.sub(
    'arrange-words', 'Arranging words and picking slots',
    "Standard question: 4-6 words are given; arrange them as in a dictionary and answer which comes first, second, middle, or last. Practical pipeline:\n\n1. Group words by their first letter (usually all share one or two letters).\n2. Inside a group, repeat by the second letter, then the third — the groups shrink fast.\n3. Count down to the asked slot: 'third from the left' = the third word in the final order.\n\nAnswer options are usually the words themselves; wrong options come from comparing at the wrong position — which is exactly what the split-point method prevents.",
    tricks=[
        C.T(
            'Slot-count from the left',
            "Once sorted, number the words 1, 2, 3… and simply read the asked position. 'Comes last' = highest position; 'middle of five' = position 3.",
            "**Q.** Cable, Cabin, Cabaret, Cabbage — which comes third?\n\n**Sol.** CABA < CABB < CAB I < CABL → Cabaret, Cabbage, Cabin, Cable → third = **Cabin**.",
            "Sort once, count to the slot; never re-compare for each option."),
    ],
    mistakes=[
        "Re-sorting mentally for every option instead of fixing one order.",
        "Missing that CABINET would sit between CAB and CABLE-type words.",
    ]))

subs.append(C.sub(
    'letter-position', 'Letter positions and shifts',
    "Memorise the anchor word **EJOTY**: E=5, J=10, O=15, T=20, Y=25. Every position question becomes a small shift:\n\n- Letter at position p: read off from EJOTY, adjust by the difference.\n- p-th from the right: position = 27 − p from the left.\n- k letters to the right of position p: p + k; to the left: p − k (stay inside 1–26).\n\nFor alphabet-modification questions ('first half reversed…'), physically write the 26-letter new sequence and count — never trust mental shifting.",
    formulas=[
        C.F('Position from the right', 'p_{\\text{right}} = 27 - p_{\\text{left}}',
            'The two positions of the same letter add to 27.'),
        C.F('Shifted position', 'p' + "' = p \\pm k", 'Move right (+) or left (−) by k letters, clamped to 1–26.'),
    ],
    tricks=[
        C.T(
            'EJOTY + tiny shift',
            "Anchor at the nearest of E, J, O, T, Y and step. Position 18: T(20) − 2 = **R**. Two seconds, no counting.",
            "**Q.** Which letter is 7th to the right of the 10th letter of the alphabet?\n\n**Sol.** 10th = J; 7 right → 17 = **Q** (J at 10, O at 15, Q at 17).",
            "EJOTY converts every position into a ±few-step walk from an anchor."),
    ],
    mistakes=[
        "Using 26 instead of 27 in from-the-right conversions.",
        "Slipping past A or Z on shifts — check bounds.",
        "Confusing 'letter at position 10' with '10 letters after it'.",
    ]))

subs.append(C.sub(
    'word-formation', 'Dictionary rank and word surgery',
    "Two specialist questions:\n\n1. **Rank of a word** (e.g. the dictionary rank of MACHINE among arrangements of its letters): step letter by letter. At each step count how many *unused* letters are smaller than the current letter — multiply that count by (remaining letters − 1)! and add. Add 1 at the end. This is 'how many words start with earlier letters' accumulation.\n2. **Letter surgery**: rearranging a word's letters alphabetically, counting letters that keep their place, or rebuilding words from selected positions — always write the derived sequence out.\n\nFor words with repeated letters, treat identical letters as interchangeable (the rank algorithm handles this automatically since 'smaller letters' are counted, not equal ones).",
    formulas=[
        C.F('Rank of a word', '\\text{rank} = 1 + \\sum_i c_i \\times (r_i)!',
            'At each letter: c_i = unused letters smaller than it, r_i = letters remaining after it.'),
    ],
    tricks=[
        C.T(
            'Count smaller unused letters',
            "Freeze the sorted letter list, and for each letter of the word (left to right) ask: how many still-unused letters are SMALLER? Multiply by the factorial of what remains, sum, +1.",
            "**Q.** Rank of CAB among ABC arrangements?\n\n**Sol.** C: A,B smaller → 2×2! = 4. A: none smaller → 0. B: none → 0. Rank = 4 + 0 + 0 + 1 = **5**.",
            "Per-letter contribution = smaller-unused × (remaining)!."),
    ],
    mistakes=[
        "Forgetting the final +1 (the word itself is not counted by the sums).",
        "Using the original remaining count instead of the shrinking one.",
        "Rearranging letters alphabetically but comparing with the original word wrongly.",
    ]))

patterns = [
    C.P('Arrange and pick slot', 'very common',
        "4-6 words; find first / second / middle / last in dictionary order.",
        "Sort by first split point; count to the slot."),
    C.P('Prefix vs later-letter battle', 'common',
        "Word pairs sharing long prefixes (SCANDAL/SCANTY).",
        "First differing letter wins; a true prefix ends before its extension."),
    C.P('Letter position arithmetic', 'very common',
        "Position from left/right, shifts left/right, between-counts.",
        "EJOTY anchors + p±k shifts; right-side = 27 − p."),
    C.P('Modified alphabet sequence', 'occasional',
        "First half reversed, every 2nd letter dropped, etc.",
        "Write out the new 26-letter line; count on paper."),
    C.P('Dictionary rank of a word', 'common',
        "Rank of MACHINE among its letter arrangements.",
        "Smaller-unused × remaining! summed, plus 1."),
    C.P('Same-position count', 'occasional',
        "After alphabetical rearrangement, letters keeping their slot.",
        "Write both versions aligned and tick matches."),
]

examples = []

# ex1
e1 = sorted(['cable', 'cabin', 'cabaret', 'cabbage'])
assert e1 == ['cabaret', 'cabbage', 'cabin', 'cable'], e1
examples.append(C.Q(
    'rsn-dictionary-ex1',
    "Arrange as in a dictionary: **Cable, Cabin, Cabaret, Cabbage.** Which word comes **second**?",
    ['Cabbage', 'Cabin', 'Cable', 'Cabaret'], 'Cabbage',
    "All share CAB. 4th letters: A (Cabaret), B (Cabbage), I (Cabin), L (Cable). Order: Cabaret, Cabbage, Cabin, Cable → second = **Cabbage**.",
    sc="First split point: the 4th letter decides everything here.",
    d='easy', sub='arrange-words', pat='arrange and pick slot', t=30))

# ex2
assert 14 + 6 == 20 and ALPHA[20 - 1] == 'T'
examples.append(C.Q(
    'rsn-dictionary-ex2',
    "Which letter is **6th to the right of the 14th letter** from the left of the English alphabet?",
    ['T', 'U', 'S', 'V'], 'T',
    "14 + 6 = 20 → the **20th letter = T** (EJOTY: T is 20).",
    sc="Pure shift: p + k.",
    d='easy', sub='letter-position', pat='letter position arithmetic', t=25))

# ex3: rank of WORD
assert word_rank('WORD') == brute_rank('WORD') == 22
examples.append(C.Q(
    'rsn-dictionary-ex3',
    "If the letters of the word **WORD** are arranged in all possible ways, what is the **dictionary rank** of the word WORD itself?",
    ['22', '24', '20', '18'], '22',
    "Sorted letters: D, O, R, W. W: 3 smaller → 3×3! = 18. O: 1 smaller left (D) → 1×2! = 2. R: 1 smaller left (D) → 1×1! = 1. D: 0. Rank = 18+2+1+0+1 = **22**.",
    sc="Smaller-unused × remaining! per letter, then +1.",
    d='medium', sub='word-formation', pat='dictionary rank of a word', t=60))

# ex4
assert 22 - 10 - 1 == 11
examples.append(C.Q(
    'rsn-dictionary-ex4',
    "How many letters are there in the English alphabet **between J and V**?",
    ['11', '12', '10', '13'], '11',
    "J = 10, V = 22 → 22 − 10 − 1 = **11** letters strictly between.",
    sc="Difference minus one.",
    d='easy', sub='letter-position', pat='letter position arithmetic', t=25))

# ---------------------------------------------------------------- practice
pr = []

# 1
assert 16 - 4 - 1 == 11
pr.append(C.Q(
    'rsn-dictionary-1',
    "How many letters of the English alphabet are there **between D and P** (not counting D and P)?",
    ['11', '12', '10', '13'], '11',
    "D = 4, P = 16 → 16 − 4 − 1 = **11**.",
    sc="Positions differ by 12; strictly-between is one less.",
    d='easy', sub='letter-position', pat='letter position arithmetic', t=25))

# 2
assert 27 - 23 == 4
pr.append(C.Q(
    'rsn-dictionary-2',
    "What is the position of the letter **W from the right** of the English alphabet?",
    ['4th', '5th', '3rd', '6th'], '4th',
    "W = 23 from the left → 27 − 23 = **4th** from the right (Z 1st, Y 2nd, X 3rd, W 4th).",
    sc="From-right position = 27 − from-left position.",
    d='easy', sub='letter-position', pat='letter position arithmetic', t=25))

# 3
p20 = 27 - 20
assert p20 == 7 and p20 - 5 == 2 and ALPHA[2 - 1] == 'B'
pr.append(C.Q(
    'rsn-dictionary-3',
    "Which letter is **5th to the left of the 20th letter from the right** of the English alphabet?",
    ['B', 'C', 'A', 'D'], 'B',
    "20th from the right = 27 − 20 = 7th from the left = G. Five to the left: 7 − 5 = 2 = **B**.",
    sc="Convert from-right to from-left, then shift left.",
    d='medium', sub='letter-position', pat='letter position arithmetic', t=40))

# 4
new_seq = list(reversed('ABCDEFGHIJKLM')) + list('NOPQRSTUVWXYZ')
assert len(new_seq) == 26
assert new_seq[17 - 1] == 'Q' and new_seq[17 - 7 - 1] == 'E'
pr.append(C.Q(
    'rsn-dictionary-4',
    "If the **first half of the English alphabet is written in reverse order** (so the sequence begins N, M, L, …) and the rest kept as usual, which letter is **7th to the left of the letter that is 10th from the right** in this new sequence?",
    ['E', 'F', 'D', 'G'], 'E',
    "New sequence: N M L K J I H G F E D C B A O P Q R S T U V W X Y Z. 10th from the right = Q (position 17). Seven to its left = position 10 = **E**.",
    sc="Write the full 26-letter line once; all counting happens on paper.",
    d='hard', sub='letter-position', pat='modified alphabet sequence', t=70))

# 5
w5 = sorted(['naughty', 'nautical', 'nation', 'native', 'nature'])
assert w5 == ['naughty', 'nautical', 'nation', 'native', 'nature'], w5
pr.append(C.Q(
    'rsn-dictionary-5',
    "Arrange as in a dictionary: **Nation, Native, Nature, Nautical, Naughty.** Which word comes **third**?",
    ['Nation', 'Native', 'Nautical', 'Nature'], 'Nation',
    "N-words split at the 3rd letter: U-group (Naughty, Nautical) first, then T-group: NATI (Nation, Native) vs NATU (Nature) — I before U. Order: Naughty, Nautical, Nation, Native, Nature → third = **Nation**.",
    sc="Group by the first split letter: AU < AT, then I < U.",
    d='medium', sub='arrange-words', pat='arrange and pick slot', t=40))

# 6
w6 = sorted(['borrow', 'border', 'borne', 'bore', 'borough'])
assert w6 == ['bore', 'border', 'borne', 'borrow', 'borough'], w6
pr.append(C.Q(
    'rsn-dictionary-6',
    "Which word would come **last** in the dictionary: **Borrow, Border, Borne, Bore, Borough**?",
    ['Borrow', 'Borough', 'Borne', 'Border'], 'Borrow',
    "Common prefix BOR. 4th letters: E (Bore), D (Border), N (Borne), R (Borrow), O (Borough). D < E < N < O < R → order: Bore, Border, Borne, Borough, Borrow. Last = **Borrow**.",
    sc="Split at BOR + 4th letter: D E N O R.",
    d='medium', sub='arrange-words', pat='arrange and pick slot', t=45))

# 7
w7 = sorted(['signal', 'sight', 'silly', 'sign', 'silent'])
assert w7 == ['sight', 'sign', 'signal', 'silent', 'silly'], w7
pr.append(C.Q(
    'rsn-dictionary-7',
    "Arrange as in a dictionary: **Signal, Sight, Silly, Sign, Silent.** Which word is **exactly in the middle**?",
    ['Signal', 'Silent', 'Sign', 'Silly'], 'Signal',
    "SIG group: 4th letter H (Sight) before N (Sign, Signal); Sign is a prefix of Signal → Sign first. SIL group: Silent (I) before Silly (L). Full order: Sight, Sign, Signal, Silent, Silly → middle (3rd) = **Signal**.",
    sc="Two prefix-clusters: SIG and SIL; settle each, then splice.",
    d='hard', sub='arrange-words', pat='prefix vs later-letter battle', t=55))

# 8
w8 = sorted(['amber', 'amble', 'anger', 'angel', 'angle'])
assert w8 == ['amber', 'amble', 'angel', 'anger', 'angle'], w8
pr.append(C.Q(
    'rsn-dictionary-8',
    "Arrange as in a dictionary: **Angel, Angle, Anger, Amble, Amber.** Which word comes **fourth**?",
    ['Anger', 'Angel', 'Angle', 'Amber'], 'Anger',
    "AM group first (Amber, Amble; B < L), then the ANG group at the 4th letter: Angel (E) and Anger (E) precede Angle (L). Angel vs Anger splits at the 5th: L < R. Order: Amber, Amble, Angel, Anger, Angle → fourth = **Anger**.",
    sc="First-letter split (AM/AN), then compare at the first difference only.",
    d='medium', sub='arrange-words', pat='arrange and pick slot', t=45))

# 9
w9 = sorted(['scan', 'scant', 'scandal'])
assert w9 == ['scan', 'scandal', 'scant'], w9
pr.append(C.Q(
    'rsn-dictionary-9',
    "Arrange as in a dictionary: **Scant, Scan, Scandal.** Which word comes **second**?",
    ['Scandal', 'Scant', 'Scan', 'Cannot be determined'], 'Scandal',
    "SCANDAL vs SCANT: at the 5th letter D < T, so Scandal precedes Scant, and Scan (a prefix) precedes both. Order: Scan, Scandal, Scant → second = **Scandal**.",
    sc="Prefix rule puts SCAN first; then D vs T decides the rest — never compare by length.",
    d='medium', sub='dict-idea', pat='prefix vs later-letter battle', t=45))

# 10
w10 = sorted(['song', 'son', 'sonar', 'sone', 'soon'])
assert w10 == ['son', 'sonar', 'song', 'sone', 'soon'], w10
pr.append(C.Q(
    'rsn-dictionary-10',
    "Arrange as in a dictionary: **Song, Son, Sonar, Sone, Soon.** Which word comes **fourth**?",
    ['Sone', 'Song', 'Sonar', 'Soon'], 'Sone',
    "SON is a prefix of Sonar → Son first. Then compare at the 3rd letter: SONAR (A) < SONG (G) < SONE (N) < SOON (O). Order: Son, Sonar, Song, Sone, Soon → fourth = **Sone**.",
    sc="Prefix first, then the 3rd letter: A < G < N < O.",
    d='medium', sub='arrange-words', pat='prefix vs later-letter battle', t=45))

# 11
vr = word_rank('MACHINE')
assert vr == brute_rank('MACHINE')
assert vr == 3610, vr
pr.append(C.Q(
    'rsn-dictionary-11',
    "If the letters of the word **MACHINE** are arranged in all possible ways and the arrangements are listed as in a dictionary, what is the **rank of the word MACHINE**?",
    ['3610', '3612', '3608', '3606'], '3610',
    "Sorted letters: A, C, E, H, I, M, N. Letter-by-letter 'smaller-unused × remaining!': M → 5×6! = 3600; A → 0; C → 0; H → 1×3! = 6 (only E is smaller-unused); I → 1×2! = 2 (E again); N → 1×1! = 1 (E); E → 0. Sum 3600+6+2+1, plus 1 for the word itself = **3610**.",
    sc="Smaller-unused × remaining! per letter, then +1.",
    d='hard', sub='word-formation', pat='dictionary rank of a word', t=110))


