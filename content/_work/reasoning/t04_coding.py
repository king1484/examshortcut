# build coding-decoding topic
import common as C


def nat_word_codes(w):
    """natural numeric codings of word w -> set of ints (to keep distractors away from)"""
    pos = [C.p(c) for c in w]
    s = sum(pos)
    out = set()
    for k in range(1, 6):
        out.add(s * k)
        out.add(s + k)
        out.add(s - k)
    out.add(s)
    prod = 1
    for x in pos:
        prod *= x
    out.add(prod)
    out.add(sum(x * (i + 1) for i, x in enumerate(pos)))       # position-weighted
    out.add(sum(x * x for x in pos))                            # sum of squares
    out.add(len(pos) * s)
    return out


def check_word_code(sample, coded, probe, correct, options):
    """sample:coded reveals the rule (constant shift / atbash / reversal / reverse+shift /
    mixed per-index shift). Only one natural rule may map probe to an option."""
    assert correct in options
    rules = {}
    rules['shift'] = lambda w: C.shv(w, C.diffs(sample, coded))
    if all(C.opp(a) == b for a, b in zip(sample, coded)):
        rules['atbash'] = C.opps
    if coded == sample[::-1]:
        rules['reversal'] = lambda w: w[::-1]
    for k in range(-13, 14):
        if C.sh(sample[::-1], k) == coded:
            rules['rev+shift' + str(k)] = (lambda kk: lambda w: C.sh(w[::-1], kk))(k)
    rules['per-index'] = lambda w: C.shv(w, C.diffs(sample, coded))  # same as shift tuple
    hits = set()
    for name, f in rules.items():
        try:
            v = f(probe)
        except AssertionError:
            continue
        if v in options:
            hits.add(v)
    assert hits == {correct}, ('ambiguous word coding', name_rules(rules, probe, options), hits, correct)
    return rules


def name_rules(rules, probe, options):
    out = []
    for name, f in rules.items():
        try:
            v = f(probe)
        except AssertionError:
            continue
        if v in options:
            out.append((name, v))
    return out



def families_fit(sample_word, sample_code):
    """numeric coding families (name, fn) that reproduce the sample pair"""
    fs = []
    s = sum(C.p(c) for c in sample_word)
    if sample_code == s:
        fs.append(('sum', lambda w: sum(C.p(c) for c in w)))
    for k in range(1, 13):
        if sample_code == s + k:
            fs.append(('sum+%d' % k, lambda w, k=k: sum(C.p(c) for c in w) + k))
        if sample_code == s - k:
            fs.append(('sum-%d' % k, lambda w, k=k: sum(C.p(c) for c in w) - k))
        if sample_code == s * k:
            fs.append(('sum*%d' % k, lambda w, k=k: sum(C.p(c) for c in w) * k))
    if sample_code == sum(C.p(c) * (i + 1) for i, c in enumerate(sample_word)):
        fs.append(('weighted', lambda w: sum(C.p(c) * (i + 1) for i, c in enumerate(w))))
    if sample_code == sum((27 - C.p(c)) for c in sample_word):
        fs.append(('reverse-sum', lambda w: sum(27 - C.p(c) for c in w)))
    return fs


def check_number_coding(sample_word, sample_code, probe, correct, options):
    fs = families_fit(sample_word, sample_code)
    assert fs, 'no natural family fits the sample'
    hits = set()
    for name, f in fs:
        v = str(f(probe))
        if v in [str(o) for o in options]:
            hits.add(v)
    assert hits == {str(correct)}, ('ambiguous number coding', [(n, f(probe)) for n, f in fs], hits, correct)
    return True


subs = []

subs.append(C.sub(
    'coding-idea', 'The coding-decoding family',
    "A coding question shows you a word and its coded form, reveals the rule, and asks you to code (or decode) another word. Every CGL coding rule is mechanical — no vocabulary is tested. The five recurring rule types:\n\n1. **Letter shifting**: each letter moves +k or −k (CAT → DBU is +1).\n2. **Opposite letters (Atbash)**: each letter is replaced by its mirror in the alphabet.\n3. **Reversal / reverse+shift**: the word is written backwards, often after or before a shift.\n4. **Number coding**: the word becomes a number — sum of letter positions, position sums plus a constant, or position-weighted sums.\n5. **Substitution**: objects or words are renamed ('sky is called sea'); you answer from the renames, never from reality.\n\nMethod: compute the letter-position difference between the sample pair, slot by slot. The difference tuple IS the rule. Apply it to the asked word mechanically.",
    tricks=[C.T(
        'Difference tuple first',
        "Write the sample word and its code with positions, subtract slot by slot. A flat tuple (+1, +1, +1) is a shift; a mixed tuple is a per-index rule; a reversed tuple pattern hints at reversal. Then apply the same tuple to the new word.",
        "**Q.** If RAIN is coded **UEMQ**? No — verify: R+3=U, A+4=E, I+3=L... always finish the subtraction before coding.\n\nCorrect use: **Q.** If CAT = **FDW**, code DOG.\n\n**Sol.** C→F +3, A→D +3, T→W +3 → flat +3. D+3 = G, O+3 = R, G+3 = J → **GRJ**.",
        "The tuple you computed on the sample is guaranteed to fit — never guess a fresh rule for the probe."),
    ],
    mistakes=[
        "Coding the probe with a *different* shift than the sample revealed (the most common silly loss).",
        "Forgetting wrap-around: Y + 3 = B, not 'out of range'.",
        "Answering substitution questions from real-world facts instead of the given renames.",
    ]))

subs.append(C.sub(
    'letter-shift-coding', 'Letter shift coding',
    "The bread and butter of CGL coding. The code moves every letter by the same number of positions (or by a fixed per-index pattern). Compute the shift from the sample pair once; the same shift (or tuple) applies to the probe.\n\n**Worked skeleton**: If MANGO is coded **OCPIQ**, the tuple is (+2, +2, +2, +2, +2); so JUICE (+2 on each) = **LWKGE**. If the tuple comes out mixed — (+1, +2, +3, +1, +2) — it is still applied slot-wise exactly.\n\nShifts behave mod 26: X + 5 = C. Fluency with EJOTY anchors (E=5, J=10, O=15, T=20, Y=25) makes every jump a small hop from a known letter.",
    formulas=[
        C.F('Shift tuple', 'Q(code_i) = Q(word_i) + d_i \\pmod{26}', 'Compute d_i from the sample; apply the identical tuple to the probe.'),
        C.F('Decode = negative shift', 'Q(word_i) = Q(code_i) - d_i \\pmod{26}', 'For decoding questions subtract the tuple instead of adding.'),
    ],
    tricks=[
        C.T(
            'Anchor hops, not counting',
            "For shift +k, jump from the nearest EJOTY anchor: to shift W by 4, note W = Y − 2, so W + 4 = Y + 2 = A. Two small hops beat counting W→X→Y→Z→A.",
            "**Q.** If MANGO = OCPIQ (+2), code JUICE.\n\n**Sol.** J+2 = L, U+2 = W, I+2 = K, C+2 = E, E+2 = G → **LWKGE**.",
            "EJOTY + small hops keeps shift arithmetic error-free at speed."),
        C.T(
            'Decode questions: run the tuple backwards',
            "When a coded word is given and the original is asked, subtract the tuple instead of adding. Reverse every hop.",
            "**Q.** If MANGO = OCPIQ (+2), what does **NQWCU**? No — decode 'LCAGC' mean? Minus 2 per letter → **JAYEA**? Always write positions.\n\nClean: decode **LWKGE** with −2 → JUICE.",
            "Decoding is the same question played backwards — subtract, don't reinvent."),
    ],
    mistakes=[
        "Applying a +2 found on a 5-letter sample to only 4 letters of the probe (misalignment).",
        "Sign errors on decode questions — the shift runs the opposite way.",
        "Missing a per-index rising tuple and treating it as flat.",
    ]))

subs.append(C.sub(
    'reverse-coding', 'Reversal and reverse-plus-shift coding',
    "The code is the word written **backwards**, possibly after shifting each letter. Test for it in one move: read the coded word backwards; if you see the sample word (or a uniform shift of it), the rule is reverse (+ shift k).\n\n**Skeleton**: LOGIC → CIGOL (pure reversal). TABLE → FMCBU (reverse TABLE → ELBAT, then +1 per letter). Order matters: check 'reverse then shift' first, then 'shift then reverse' — both appear in CGL and they are *not* the same rule.",
    tricks=[C.T(
        'Backwards reading test',
        "Read the code from right to left. If it equals the sample word, code new words by writing them backwards. If it is *almost* the sample with every letter off by the same k, code new words by reverse-then-shift.",
        "**Q.** If TABLE = FMCBU (reverse + 1), code CHAIR.\n\n**Sol.** CHAIR reversed = RIAHC; shift +1 → **SJBID**.",
        "One backwards read identifies the family; the shift value falls out of the first letter."),
    ],
    mistakes=[
        "Reversing but forgetting the extra shift (or shifting before reversing when the sample did it the other way).",
        "Reversing the probe but keeping the sample's letter order in the middle letters.",
        "Applying reversal to decode questions without un-reversing the shift as well.",
    ]))

subs.append(C.sub(
    'number-coding', 'Number coding',
    "Words are coded as numbers. The code is built from alphabet positions (A=1 ... Z=26) by one of:\n\n1. **Position sum**: CAT = 3 + 1 + 20 = 24.\n2. **Sum plus/minus constant**: CAT = 24 + 5 = 29.\n3. **Sum times constant**: CAT = 24 × 2 = 48.\n4. **Position-weighted sum**: CAT = 3×1 + 1×2 + 20×3 = 65.\n5. **Reverse-position coding**: A=26 ... Z=1 (equivalently 27 − position); CAT = 24+26+7 = 57.\n\nDecode the rule by computing the position sum of the sample word and comparing it with the code: the offset (plus 5? times 2? weighted?) is usually visible in one step. Reverse-position coding is spotted when long letters give *small* codes.",
    formulas=[
        C.F('Position sum', '\\text{code} = \\sum Q(w_i)', 'Q = A1..Z26 positions.'),
        C.F('Affine code', '\\text{code} = k \\cdot \\sum Q(w_i) + r', 'Fit k and r from the sample pair.'),
        C.F('Weighted sum', '\\text{code} = \\sum i \\cdot Q(w_i)', 'Letter i multiplies its position.'),
        C.F('Reverse positions', 'Q^{rev}(c) = 27 - Q(c)', 'Z=1 ... A=26; small codes for long words.'),
    ],
    tricks=[
        C.T(
            'One sample fixes the affine code',
            "Compute the position sum S of the sample. If code = S → plain sum. If code − S is constant-looking (5, 10...) the rule is S + r. If code/S is a clean 2 or 3, the rule is k·S. If neither fits, try the weighted sum.",
            "**Q.** If SUN = 54 (19+21+14), code MOON.\n\n**Sol.** Code = plain position sum. M+O+O+N = 13+15+15+14 = **57**.",
            "Position sum first — it explains over half of CGL number codes."),
        C.T(
            'Digit-sum shortcut for 9-heavy checks',
            "Position sums reduce nicely: letters at EJOTY anchors contribute 5/10/15/20/25. Sums are easy to verify by grouping anchors instead of adding letter by letter.",
            "**Q.** Check CAT = 24? No — C(3) + A(1) + T(20): T sits on the Y anchor (Y=25, T = Y − 5 = 20) → 3+1+20 = 24 ✓.",
            "Anchors turn position lookups into ±2 adjustments — fast and reliable."),
    ],
    mistakes=[
        "Using A=0 indexing by mistake — CGL always uses A=1 unless a sample proves otherwise.",
        "Adding the constant to each letter instead of to the total (S + r per letter vs once).",
        "Ignoring the weighted variant when the plain sum is off by a non-constant amount.",
    ]))

subs.append(C.sub(
    'substitution-coding', 'Substitution and sentence coding',
    "Two formats, no arithmetic:\n\n1. **Object renaming**: 'sky is called sea, sea is called water...' — answer from the renaming chain, never from reality. If fish live in the sea and sea is called water, fish live in **water**.\n2. **Sentence code matching**: 'red light = pa ka', 'green light = ka na' — align words to code-words across sentences. Words repeated across sentences keep the same code-word; eliminate to decode singletons.\n\nMethod for sentence codes: list code-words per sentence side by side; the shared word's code appears in both lists; whatever remains is unique by elimination.",
    tricks=[C.T(
        'Elimination table',
        "Write each sentence and its code as two aligned rows. Common words are common code-words — tick them. The word asked about then either appears directly or is the lone unmatched item.",
        "**Q.** 'red light' = pa ka; 'green light' = ka na. Code for **red**?\n\n**Sol.** 'light' is common to both sentences → light = ka. In sentence 1, red is the other word → red = **pa**.",
        "Cross out matched pairs; the answer is whatever is left unpaired."),
    ],
    mistakes=[
        "Answering from real-world knowledge ('fish live in water') instead of the renaming chain.",
        "Assuming code-word order matches word order — sentence codes often reverse it; alignment is by elimination, not position.",
        "Missing a repeated word because of a plural/singular change (light vs lights) — check word stems.",
    ]))

patterns = [
    C.P('Direct letter-shift coding of a new word',
        'very common',
        "'If CAT is coded FDW, how is DOG coded?' — a flat shift revealed by the sample pair.",
        "Compute the shift tuple once from the sample; apply it slot-wise to the probe with EJOTY hops."),
    C.P('Coding by position sum (number coding)',
        'very common',
        "'If SUN is 54, how is MOON coded?' — code built from A=1...Z=26 positions.",
        "Position sum of the sample; identify the affine tweak (k, r or weighted); compute for the probe."),
    C.P('Reversal or reverse+shift coding',
        'common',
        "The coded word read backwards is the sample word (or a uniform shift of it).",
        "Backwards reading test; then reverse the probe and apply the same shift."),
    C.P('Opposite-letter (Atbash) coding',
        'common',
        "Sample letters pair with their alphabet mirrors (A↔Z, M↔N; position sum 27).",
        "Confirm the 27-sum, then convert the probe through the opposite-pairs table."),
    C.P('Mixed per-index shift coding',
        'common',
        "The shift tuple rises or cycles: +1, +2, +3... or +1, +2, +1, +2.",
        "Subtract slot-wise; apply the identical tuple to the probe — never average the tuple."),
    C.P('Substitution (renaming) questions',
        'common',
        "'Sky is called sea...' — one object's name is reassigned through a chain.",
        "Follow the renames literally; two-step chains need the second rename applied."),
    C.P('Sentence code matching by elimination',
        'common',
        "Two or three sentence-code pairs; find the code of one word.",
        "Align sentences with codes; common word = common code-word; eliminate for the rest."),
    C.P('Decoding (reverse direction)',
        'common',
        "The coded form is given; the original word is asked.",
        "Run the discovered tuple backwards (subtract shifts, un-reverse, un-opposite)."),
]

# ---------------------------------------------------------------- solved examples
examples = []
ans_ex1 = C.sh('DELHI', 1)
assert ans_ex1 == 'EFMIJ'
assert all(o == ans_ex1 or o not in [C.sh('DELHI', k) for k in range(-13, 14)]
           for o in [ans_ex1, 'EFMIK', 'DELIH', 'CFMIJ'])
examples.append(C.Q(
    'rsn-coding-ex1',
    "In a certain code, **CAT is written as DBU**. How is **DELHI** written in that code?",
    [ans_ex1, 'EFMIK', 'DELIH', 'CFMIJ'],
    ans_ex1,
    "CAT → DBU: every letter moves **+1** (C→D, A→B, T→U). DELHI + 1 = D→E, E→F, L→M, H→I, I→J → **EFMIJ**.",
    sc="Flat shift found on the sample; run the probe through the same +1 in one pass.",
    d='easy', sub='letter-shift-coding', pat='direct letter-shift coding of a new word', t=35))

_ex2_ans = 'GPSYH'
assert C.sh('CLOUD', 4) == _ex2_ans
assert all(o == _ex2_ans or o not in [C.sh('CLOUD', k) for k in range(-13, 14)]
           for o in [_ex2_ans, 'GPTYI', 'GQTYH', 'GQSYH'])
examples.append(C.Q(
    'rsn-coding-ex2',
    "In a certain code, **RAIN is written as VEMR**. How is **CLOUD** written in that code?",
    [_ex2_ans, 'GPTYI', 'GQTYH', 'GQSYH'],
    _ex2_ans,
    "R→V = +4, A→E = +4, I→M = +4, N→R = +4: flat **+4**. CLOUD + 4 = C→G, L→P, O→S, U→Y, D→H → **GPSYH**.",
    sc="One subtraction row gives +4; C jumps to G via the E anchor (E−2 = C, G = E+2).",
    d='easy', sub='letter-shift-coding', pat='direct letter-shift coding of a new word', t=35))

_ex3_ans = 'NVZG'
assert C.opps('MEAT') == _ex3_ans and C.opps('FLOW') == 'UOLD'
examples.append(C.Q(
    'rsn-coding-ex3',
    "In a certain code, **FLOW is written as UOLD**. How is **MEAT** written in that code?",
    [_ex3_ans, 'NVZI', 'NFZG', 'MUZG'],
    _ex3_ans,
    "F(6)→U(21): 6+21 = 27 ✓; L(12)→O(15): 27 ✓ — opposite letters (Atbash). M↔N, E↔V, A↔Z, T↔G → **NVZG**.",
    sc="Position sums of 27 confirm Atbash; read the probe straight through the opposite-pairs table.",
    d='easy', sub='letter-shift-coding', pat='opposite-letter (Atbash) coding', t=35))

examples.append(C.Q(
    'rsn-coding-ex4',
    "If **SUN is coded 54**, how is **MOON** coded? (code = sum of alphabet positions)",
    [57, 55, 61, 46],
    57,
    "Position sum: S(19) + U(21) + N(14) = 54 ✓ — the code is the plain position sum. MOON = 13 + 15 + 15 + 14 = **57**.",
    sc="Group anchors: O = 15 each; M = J+3 = 13; N = O−1 = 14. Two O's make the sum quick.",
    d='easy', sub='number-coding', pat='coding by position sum (number coding)', t=35))

# ---------------------------------------------------------------- practice
pr = []

# 1 shift +2 via sample CUP=EWR
assert C.sh('CUP', 2) == 'EWR' and C.sh('BOX', 2) == 'DQZ'
assert all(o == 'DQZ' or o not in [C.sh('BOX', k) for k in range(-13, 14)]
           for o in ['DQZ', 'DQY', 'EQZ', 'CPZ'])
pr.append(C.Q('rsn-coding-1',
              "In a certain code, **CUP is written as EWR**. How is **BOX** written in that code?",
              ['DQZ', 'DQY', 'EQZ', 'CPZ'],
              'DQZ',
              "C→E = +2, U→W = +2, P→R = +2: flat **+2**. B+2 = D, O+2 = Q, X+2 = Z → **DQZ**.",
              sc="Shift +2 read from the sample; X wraps? No — X(24)+2 = Z(26), no wrap needed.",
              d='easy', sub='letter-shift-coding', pat='direct letter-shift coding of a new word', t=30))

# 2 decode: subtract shift
_ans = 'BLACK'
_coded = C.sh(_ans, 2)
assert _coded == 'DNCEM'
assert [k for k in range(-13, 14) if C.sh('BLACK', k) == _coded] == [2]
assert all(C.sh(w, 2) != _coded for w in ['CLACK', 'BLAKC', 'ALBCK'])
pr.append(C.Q('rsn-coding-2',
              "In a certain code, **CUP is written as EWR**. Which word is coded as **DNCEM**?",
              ['BLACK', 'CLACK', 'BLAKC', 'ALBCK'],
              'BLACK',
              "CUP → EWR is **+2** per letter, so decoding means −2. DNCEM − 2: D→B, N→L, C→A, E→C, M→K → **BLACK**.",
              sc="Decode = subtract the tuple; run the letters in one pass and the option word appears.",
              d='medium', sub='letter-shift-coding', pat='decoding (reverse direction)', t=40))

# 3 rising tuple coding
_probe = 'BLADE'
_tup = [1, 2, 3, 4, 5]
_a3 = C.shv(_probe, _tup)
assert _a3 == 'CNDHJ'
_a3_sample = C.shv('CROWN', _tup)
assert _a3_sample == 'DTRAS'
pr.append(C.Q('rsn-coding-3',
              "In a certain code, **CROWN is written as DTRAS**. How is **BLADE** written in that code?",
              ['CNDHJ', 'CNDJH', 'CM DHJ'.replace(' ', ''), 'DNCHJ'],
              'CNDHJ',
              "C→D = +1, R→T = +2, O→R = +3, W→A = +4 (wrap), N→S = +5: tuple (+1, +2, +3, +4, +5). BLADE: B+1 = C, L+2 = N, A+3 = D, D+4 = H, E+5 = J → **CNDHJ**.",
              sc="Rising tuple — apply slot by slot; the W→A wrap is just (23+4)−26 = 1 = A.",
              d='medium', sub='letter-shift-coding', pat='mixed per-index shift coding', t=45))

# 4 atbash coding
_a4 = C.opps('GOAT')
assert _a4 == 'TLZG' and C.opps('HIDE') == 'SRWV'
pr.append(C.Q('rsn-coding-4',
              "In a certain code, **HIDE is written as SRWV**. How is **GOAT** written in that code?",
              ['TLZG', 'TLZT', 'SLZG', 'TMZG'],
              'TLZG',
              "H(8)+S(19) = 27, I(9)+R(18) = 27 — **opposite letters**. G↔T, O↔L, A↔Z, T↔G → **TLZG**.",
              sc="27-sum check, then the opposite-pairs table does the whole question.",
              d='easy', sub='letter-shift-coding', pat='opposite-letter (Atbash) coding', t=30))

# 5 reversal
_a5 = 'NOSAER'
assert 'LOGIC'[::-1] == 'CIGOL' and 'REASON'[::-1] == _a5
pr.append(C.Q('rsn-coding-5',
              "In a certain code, **LOGIC is written as CIGOL**. How is **REASON** written in that code?",
              ['NOSAER', 'NOSARE', 'RAESON', 'NOSAER'][:4] if False else ['NOSAER', 'NOSEAR', 'RAESON', 'SOAERN'],
              'NOSAER',
              "CIGOL read backwards is LOGIC — **pure reversal**. REASON reversed = **NOSAER**.",
              sc="Backwards-read test: code reversed = sample ⇒ just reverse the probe.",
              d='easy', sub='reverse-coding', pat='reversal or reverse+shift coding', t=30))

# 6 reverse + shift
_a6 = C.sh('RIAHC', 1)
assert _a6 == 'SJBID' and C.sh('TABLE'[::-1], 1) == 'FMCBU'
pr.append(C.Q('rsn-coding-6',
              "In a certain code, **TABLE is written as FMCBU**. How is **CHAIR** written in that code?",
              ['SJBID', 'RIAHC', 'TJ BJE'.replace(' ', ''), 'SBIDJ'],
              'SJBID',
              "TABLE reversed = ELBAT; each letter +1 → FMCBU ✓ (rule: **reverse, then +1**). CHAIR reversed = RIAHC; +1 → **SJBID**.",
              sc="Reverse first, then shift — keep the order the sample used.",
              d='medium', sub='reverse-coding', pat='reversal or reverse+shift coding', t=45))

# 7 number coding plain sum
_a7 = 4 + 15 + 7  # DOG
assert C.p('S') + C.p('U') + C.p('N') == 54 and _a7 == 26
opts7 = ['26', '28', '24', '30']
check_number_coding('SUN', 54, 'DOG', 26, opts7)
pr.append(C.Q('rsn-coding-7',
              "In a certain code, **SUN is coded 54** (sum of alphabet positions). How is **DOG** coded?",
              opts7,
              '26',
              "S+U+N = 19+21+14 = 54 ✓ plain sum. D+O+G = 4+15+7 = **26**.",
              sc="Position sum via anchors: G = E+2 = 7, O = 15, D = E−1 = 4.",
              d='easy', sub='number-coding', pat='coding by position sum (number coding)', t=35))

# 8 number coding affine: sum + 10
_a8 = (C.p('C') + C.p('A') + C.p('B')) + 10
assert (3 + 1 + 2) + 10 == 16 and (C.p('P') + C.p('E') + C.p('N')) + 10 == 45
opts8 = ['45', '55', '52', '48']
check_number_coding('CAB', 16, 'PEN', 45, opts8)
pr.append(C.Q('rsn-coding-8',
              "In a certain code, **CAB is coded 16**. How is **PEN** coded in that code?",
              opts8,
              '45',
              "C+A+B = 3+1+2 = 6; the code is 16 = 6 + **10**. PEN = 16 + 5 + 14 = 35; 35 + 10 = **45**.",
              sc="Sample sum 6 vs code 16 reveals the +10 offset; add it once to the probe's sum.",
              d='medium', sub='number-coding', pat='coding by position sum (number coding)', t=40))

# 9 weighted sum coding
_w = lambda w: sum(C.p(c) * (i + 1) for i, c in enumerate(w))
assert _w('BAG') == 2 * 1 + 1 * 2 + 7 * 3 == 25 and _w('DEAF') == 4 * 1 + 5 * 2 + 1 * 3 + 6 * 4 == 41
opts9 = ['41', '14', '42', '47']
check_number_coding('BAG', 25, 'DEAF', 41, opts9)
pr.append(C.Q('rsn-coding-9',
              "In a certain code, **BAG is coded 25**: each letter's position is multiplied by its place in the word and added. How is **DEAF** coded?",
              opts9,
              '41',
              "BAG = B×1 + A×2 + G×3 = 2 + 2 + 21 = 25 ✓. DEAF = 4×1 + 5×2 + 1×3 + 6×4 = 4 + 10 + 3 + 24 = **41**.",
              sc="Weighted coding: multiply each letter by 1st, 2nd, 3rd... place, then add.",
              d='hard', sub='number-coding', pat='coding by position sum (number coding)', t=50))

# 10 reverse-position coding
_r = lambda c: 27 - C.p(c)
assert _r('C') + _r('A') + _r('T') == 24 + 26 + 7 == 57
assert _r('D') + _r('O') + _r('G') == 23 + 12 + 20 == 55
opts10 = ['55', '26', '45', '52']
check_number_coding('CAT', 57, 'DOG', 55, opts10)
pr.append(C.Q('rsn-coding-10',
              "In a certain code, **CAT is coded 57** (A=26, B=25, ... Z=1). How is **DOG** coded?",
              opts10,
              '55',
              "Reverse positions: C = 24, A = 26, T = 7 → 57 ✓. D = 23, O = 12, G = 20 → 23+12+20 = **55**.",
              sc="Reverse-position coding = 27 − position per letter; Z=1, A=26.",
              d='medium', sub='number-coding', pat='coding by position sum (number coding)', t=45))

# 11 substitution chain
pr.append(C.Q('rsn-coding-11',
              "If **sky is called sea**, **sea is called water**, **water is called air**, and **air is called cloud**, where do **fishes** live?",
              ['Water', 'Sea', 'Air', 'Cloud'],
              'Water',
              "Fishes live in the **sea** (reality). But 'sea' is called **water** in this code → fishes live in **water**.",
              sc="Find the real answer first, then apply the rename — one substitution step.",
              d='easy', sub='substitution-coding', pat='substitution (renaming) questions', t=30))

# 12 two-step substitution
pr.append(C.Q('rsn-coding-12',
              "If **white is called blue**, **blue is called red**, **red is called green**, **green is called black**, **black is called yellow** — what is the colour of **clear daylight sky**?",
              ['Red', 'Blue', 'Green', 'Yellow'],
              'Red',
              "The sky's real colour is **blue**; 'blue' is called **red** in this code → **Red**.",
              sc="Two-step rename: reality → real colour → code name of that colour.",
              d='easy', sub='substitution-coding', pat='substitution (renaming) questions', t=30))

# 13 sentence elimination
pr.append(C.Q('rsn-coding-13',
              "In a code language, **'red light' is written as 'pa ka'** and **'green light' is written as 'ka na'**. What is the code for **red**?",
              ['pa', 'ka', 'na', 'pa or na'],
              'pa',
              "'light' is common to both sentences and 'ka' is the common code-word → light = ka. In sentence 1 the remaining word 'red' takes the remaining code **pa**.",
              sc="Common word ↔ common code-word; the leftover pair is your answer.",
              d='easy', sub='substitution-coding', pat='sentence code matching by elimination', t=35))

# 14 three-sentence elimination
pr.append(C.Q('rsn-coding-14',
              "**'birds fly high' = 'lo pe ni'**, **'high skies shine' = 'ni ta co'**, **'birds shine bright' = 'pe co ra'**. What is the code for **birds**?",
              ['pe', 'ni', 'co', 'ra'],
              'pe',
              "Sentence 1: birds fly high → lo pe ni. Sentence 3: birds shine bright → pe co ra. 'birds' is common to 1 and 3, whose common code-word is **pe** ('high' = ni sits in sentences 1-2; 'shine' = co in 2-3) → birds = **pe**.",
              sc="Overlap coding: the code-word shared by exactly the sentences sharing the word.",
              d='medium', sub='substitution-coding', pat='sentence code matching by elimination', t=45))

# 15 mixed word+number coding
assert C.sh('LEAF', 1) == 'MFBG' and 12 + 5 + 1 + 6 == 24 and C.sh('TREE', 1) == 'USFF' and 20 + 18 + 5 + 5 == 48
pr.append(C.Q('rsn-coding-15',
              "In a certain code, **'TREE' is written as 'USFD48'** — each letter moves one step right (TREE→USFD) and the word's position sum (20+18+5+5 = 48) is appended. How is **LEAF** written?",
              ['MFBG24', 'MFBG52', 'MFAG24', 'MFBG48'],
              'MFBG24',
              "Letter part: LEAF +1 → M, F, B, G = **MFBG**. Number part: L(12)+E(5)+A(1)+F(6) = **24**. Code = **MFBG24**.",
              sc="Two-part code: shift the letters once; recompute the number from the probe — never reuse the sample's number.",
              d='hard', sub='number-coding', pat='mixed per-index shift coding', t=50))

topic_obj = C.topic(
    'coding-decoding', 'Coding - Decoding', 'high', {'tier1': 4, 'tier2': 4},
    "Coding questions reveal how a word (or sentence) is transformed into a code and ask you to apply the same transformation to a new word. CGL asks 3-5 per shift. Rules are mechanical: letter shifts, opposites, reversal, position sums, renames. Compute the rule from the sample pair, then apply it without creativity.",
    subs, patterns, examples, pr)

C.write_topic(topic_obj)
print('OK coding-decoding')
