# build analogy topic
import common as C
import engines as E

subs = []

subs.append(C.sub(
    'analogy-idea', 'The idea of analogy',
    "An analogy question states one relationship and asks you to repeat it: **A : B :: C : ?** — 'A is to B as C is to what?'. The exam never tests knowledge of A, B or C; it tests whether you can *name the relationship* in one precise sentence and apply it exactly.\n\nThe relation must be copied in the **same direction** (A→B, so C→?) and at the **same level of specificity**. If 'Butterfly : Caterpillar' is adult-to-young, the answer must be adult-to-young, not merely 'animal to animal'.\n\nFour families appear in SSC CGL: **word analogy** (meaning-based), **number analogy** (operation-based), **letter analogy** (position/shift-based) and **mixed analogy** (letter-number clusters). Numbers and letters are fully checkable by arithmetic; word pairs must be matched by an exact relation sentence.",
    tricks=[C.T(
        'Speak the relation as a full sentence before touching the options',
        "Convert 'A : B' into a sentence like 'B is the young one of A' or 'each letter of B is 3 ahead of A'. Then test option pairs against the *same sentence*. Options written to look related but failing one word of the sentence are traps.",
        "**Q.** 'Doctor : Hospital' :: ? — (a) Teacher : Student (b) Judge : Court (c) Tailor : Fabric (d) Doctor : Medicine\n\n**Sol.** Sentence: 'the second is the *workplace* of the first'. Teacher : Student is teacher-to-person, Tailor : Fabric is worker-to-material, Doctor : Medicine is worker-to-object. Only **Judge : Court** is professional-to-workplace.",
        "Relation sentence kills 3 wrong options in one line — never start by comparing options with each other."),
    ],
    mistakes=[
        "Matching the *category* instead of the relation: 'Rose : Flower' and 'Car : Vehicle' are same-category pairs, but 'Rose : Flower :: Car : ?' does not give 'Vehicle' — the relation of the model pair (member to its class) applied to Car would need a class like 'Machine'.",
        "Reversing direction: if 'Chick : Hen' (young→adult) is given, the answer must also be young→adult; 'Hen : Chick' in the options is a trap.",
        "Stopping at the first option that 'sounds related' — options are built so exactly two pairs sound plausible.",
    ]))

subs.append(C.sub(
    'letter-analogy', 'Letter / letter-cluster analogy',
    "Here A, B, C are letters or clusters, and the relation is a **letter-position rule**. Convert every letter to its alphabet position (A=1 ... Z=26) and compare positions of B against A. The rule is almost always one of:\n\n1. **Constant shift**: every letter moves +k or −k (e.g. CAT → FDW is +3).\n2. **Different shifts per position**: shifts form their own pattern (+1, +2, +3, ...).\n3. **Opposite letter (Atbash)**: A↔Z, B↔Y, ... position p becomes 27−p.\n4. **Reversal**: the cluster order flips (EAT → TAE), sometimes combined with a shift.\n\n**EJOTY anchor table** — learn these five positions and every shift becomes a ±1 to ±5 jump from a familiar letter:\n\n| Letter | E | J | O | T | Y |\n|---|---|---|---|---|---|\n| Position | 5 | 10 | 15 | 20 | 25 |\n\n**Opposite pairs**: A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N.",
    formulas=[
        C.F('Shift rule', 'Q(B) = Q(A) + k \\pmod{26}', 'Q = alphabet position; k is constant for a constant-shift analogy.'),
        C.F('Opposite letter', 'Q(B) = 27 - Q(A)', 'Atbash: A↔Z, M↔N. Two-letter quick check: sum of positions = 27.'),
        C.F('Rising shift', 'Q(B_i) = Q(A_i) + i', 'Position i gets shift i — common in 4-letter clusters (BDFH from ABCD).'),
    ],
    tricks=[
        C.T(
            'Subtract positions, then copy the shift pattern',
            "Write positions of A under A, positions of B under B, subtract slot by slot. The shift tuple you get (e.g. +3, +3, +3) is the whole question. Apply the same tuple to C and read the answer with EJOTY.",
            "**Q.** 'GKM' : 'IQN' :: 'SUX' : ?\n\n**Sol.** G(7)→I(9): +2; K(11)→Q(17): +6; M(13)→N(14): +1. Shift tuple (+2, +6, +1). S(19)+2=U(21), U(21)+6=A(27→A), X(24)+1=Y(25) → **UAY**.",
            "One subtraction row is faster than 'feeling' the pattern; shifts never lie."),
        C.T(
            'Spot Atbash by the 27-sum',
            "If corresponding letters of A and B always add to 27 (C=3, X=24 → 27), the rule is opposite letters. Then answer = opposite of each letter of C — no shifting at all.",
            "**Q.** 'HE' : 'SV' :: 'GO' : ?\n\n**Sol.** H(8)+S(19)=27, E(5)+V(22)=27 → Atbash. Opposites: G↔T, O↔L → **TL**.",
            "Opposite pairs table A-Z ... M-N applied letter by letter takes 5 seconds."),
        C.T(
            'Reversal check: read B backwards',
            "If B read backwards is a constant shift of A (or of A reversed), the rule is reversal ± shift. Apply: reverse C, then shift by the same k.",
            "**Q.** 'DEB' : 'BED' :: 'LAP' : ?\n\n**Sol.** BED is DEB reversed (no shift). So LAP reversed = **PAL**.",
            "Only two things can hide in reversal questions: pure reversal, or reversal + fixed shift — test both."),
    ],
    mistakes=[
        "Applying the shift to *positions* instead of letters (adding 3 to '26' giving '29' instead of wrapping to C). Positions wrap mod 26.",
        "Ignoring a mixed shift tuple: treating (+1, +2, +3) as 'constant +2' gives wrong cluster; check every slot.",
        "Confusing opposite-letter (Atbash) with a 13-shift: both map A to N? No — Atbash maps A to Z. Verify with the 27-sum before using the table.",
    ]))

subs.append(C.sub(
    'word-analogy', 'Word analogy',
    "Both pairs are meaningful English word pairs; you must find the option whose pair shares the **same relation**, word-for-word. CGL draws from a fixed relation bank — memorise the bank, not individual questions:\n\n| Relation | Example pair |\n|---|---|\n| worker : workplace | Chef : Kitchen |\n| worker : tool | Surgeon : Scalpel |\n| adult : young one | Sheep : Lamb |\n| male : female | Colt : Filly |\n| animal : home | Horse : Stable |\n| animal : sound | Owl : Hoot |\n| country : currency | Japan : Yen |\n| instrument : quantity | Barometer : Pressure |\n| part : whole | Chapter : Book |\n| product : source | Flour : Wheat |\n| study : subject | Zoology : Animals |\n| verb : noun of act | See : Sight |\n\nWhen two options look right, add precision: Foal is any young horse, Colt only a young *male* horse — relation strength decides.",
    tricks=[
        C.T(
            'Two-question test on every option',
            "Ask (1) is the option pair the same *type* of relation? (2) is it the same *specific* relation in the same *direction*? An option surviving question 1 usually dies at question 2 — that is where the exam separates candidates.",
            "**Q.** 'Author : Novel' :: ? — (a) Poet : Poem (b) Editor : Newspaper (c) Reader : Library (d) Book : Print\n\n**Sol.** Type: creator-to-creation. Editor : Newspaper is editor-to-periodical (edits, doesn't author it); Reader : Library is user-to-place; Book : Print is thing-to-process. Only **Poet : Poem** is creator-to-literary-creation.",
            "Write the two-question answers as ticks/crosses; the option with two ticks is the answer."),
        C.T(
            'Gender/age precision check',
            "For animal pairs, decide whether the model pair is (a) adult:young, (b) male:female or (c) male-young:female-young. Options often mix a young-one with a female — only one matches the model exactly.",
            "**Q.** 'Drake : Duck' :: ? — (a) Horse : Mare (b) Bull : Ox (c) Ram : Ewe (d) Dog : Pup\n\n**Sol.** Model = male : female of one species. Horse : Mare is species:female; Bull : Ox is not male:female; Dog : Pup is adult:young. **Ram : Ewe** is male:female of sheep.",
            "Name the relation with its gender/age tag before reading options."),
    ],
    mistakes=[
        "Choosing an option from the same *topic* (both medical) instead of the same *relation* — topics are decoys; relations decide.",
        "Missing the direction: 'Hunger : Food' (cause:remedy) is not 'Food : Hunger'.",
        "Over-reading: adding a condition the pair does not state ('Judge : Court — but a judge also works in chambers'). Take the primary, standard relation.",
    ]))

subs.append(C.sub(
    'number-analogy', 'Number analogy',
    "A : B gives a numeric operation; repeat it on C. The operation is always simple and always **uniform** — the same expression turns a into b. Rank the usual suspects:\n\n1. **Linear**: b = k·a + r (e.g. ×3 + 2). Most common by far.\n2. **Square/cube based**: b = a² ± r, b = a³, (a+1)², a(a+1), etc.\n3. **Digit based**: b = (sum of digits) × k ± r, or reversal of digits.\n4. **Powers**: b = 2^a ± r or 3^a ± r.\n\n**Uniqueness habit**: one pair (a, b) admits many rules, so the exam keeps distractors away from every *natural* rule. When your computed answer is missing from the options, your rule is wrong — drop to the next suspect, don't force-fit.",
    formulas=[
        C.F('Linear rule', 'b = k a + r', 'Solve k and r mentally from a and b; verify on the pair before applying to c.'),
        C.F('Square family', 'b \\in \\{a^2,\\ a^2 \\pm r,\\ (a{+}1)^2,\\ a(a{+}1)\\}', 'Test squares first when b is close to a².'),
        C.F('Digit sum rule', 'b = k \\cdot S(a) + r', 'S(a) = digit sum; common when b is much smaller than a.'),
    ],
    tricks=[
        C.T(
            'Size test picks the family instantly',
            "Compare b with a: if b is a few times a → linear; if b ≈ a² → square family; if b is 10-40 → digit rule when a is 2-digit; if b is small with big a → digit sum.",
            "**Q.** '7 : 50' :: '9' : ?\n\n**Sol.** 50 ≈ 7² = 49, so square +1. 9² + 1 = **82**.",
            "Size test → family → one-line arithmetic."),
        C.T(
            'Verify the rule on the model pair before the probe',
            "Whatever rule you guess, check it reproduces b from a exactly. Guessing ×4+1 from 12 : 49 fails instantly (12×4+1 = 49 passes!) — then apply to c. The 2-second check prevents half the errors.",
            "**Q.** '6 : 42' :: '8' : ?\n\n**Sol.** Guess a(a+1): 6×7 = 42 ✓. Then 8×9 = **72**.",
            "Model-pair verification is the cheapest correctness check in the paper."),
    ],
    mistakes=[
        "Forcing a rule that ignores the model pair's exact value (fitting 12:49 with ×4+1 is right, but with ×4+0 it is wrong — check!).",
        "Mixing two different rules for the two pairs (using squares for the model and cubes for the probe).",
        "Digit-reversal missed: 27 : 72 looks like ×2+18 but the intended relation is reversal; if reversal reproduces b, prefer it.",
    ]))

subs.append(C.sub(
    'mixed-analogy', 'Mixed clusters and same-relation selection',
    "Two CGL variants sit outside the classic three:\n\n1. **Mixed cluster analogy**: A : B :: C : ? where A and B contain both letters and numbers ('B3D : E6J'). Each component follows its own mini-rule (letters shift, number doubles, etc.). Solve component-wise and assemble the answer.\n2. **Same-relation selection**: four complete pairs are given; pick the pair whose relation matches a stated model pair (or pick the pair that does NOT belong, when asked). Test all four pairs with the same relation sentence from the model.\n\nFor mixed clusters, never solve the cluster as a whole — split by character type and solve each track separately.",
    tricks=[
        C.T(
            'Solve tracks, then assemble',
            "In a mixed cluster make one column for letters (positions/shifts) and one for numbers (their own series). Fill the answer character by character — each column is independent, so an error stays inside one column.",
            "**Q.** 'A5C' : 'D10F' :: 'G15I' : ?\n\n**Sol.** Letters: A→D (+3), C→F (+3); numbers: 5→10 (×2). Apply: G+3=J, I+3=L, 15×2=30 → **J30L**.",
            "Component-wise solving turns 1 hard cluster into 2 easy columns."),
        C.T(
            'One sentence for all four pairs',
            "In same-relation selection, form the relation sentence once from the model pair and tick/cross every option against the *same* sentence, in the same order. The first option that passes both halves is the answer.",
            "**Q.** 'Sword : Sheath' :: pick the same-relation pair — (a) Rifle : Trigger (b) Knife : Blade (c) Rose : Petal (d) Blade : Cover is not; use (d) Bullet : Barrel\n\n**Sol.** Sentence: 'second is the container/cover of the first when stored'. Trigger, Blade, Petal are parts, not containers. **Bullet : Barrel** — barrel houses the bullet.",
            "Container–thing, worker–tool, cause–effect: name the abstract frame, then match frames."),
    ],
    mistakes=[
        "Assuming the number track follows the letter track's rule — the two tracks are independent.",
        "In same-relation selection, matching only the first half of the relation (both 'container' pairs) without checking the second half (what is contained).",
        "Missing an embedded digit rule like 'number = position of the first letter' (B3D → 3 is C's position... actually A=1; check the model, don't assume).",
    ]))

patterns = [
    C.P('Letter-cluster analogy with constant shift',
         'very common',
         "'Cluster1 : Cluster2 :: Cluster3 : ?' where every letter of Cluster2 is the same number of positions ahead of/behind Cluster1.",
         "Subtract positions of cluster2 from cluster1 slot-wise; confirm the tuple is constant; add it to cluster3. EJOTY makes the arithmetic oral."),
    C.P('Word analogy from the standard relation bank',
         'very common',
         "Two English word pairs; a third pair with a blank. Relations come from the fixed bank (worker-workplace, adult-young, country-currency, instrument-quantity).",
         "Name the relation as a sentence, then apply the two-question test to every option."),
    C.P('Number analogy (linear / square / cube)',
         'very common',
         "'n1 : n2 :: n3 : ?' where n2 = k·n1 + r, a square/cube offset, a(a+1) or a² ± r.",
         "Size test picks the family; verify the rule on the model pair; then one line of arithmetic on the probe."),
    C.P('Opposite-letter (Atbash) analogy',
         'common',
         "Corresponding letters of the model pair always sum to position 27 (A↔Z, M↔N).",
         "Confirm the 27-sum on two letters, then convert the probe cluster straight through the opposite-pairs table."),
    C.P('Rising-shift letter analogy',
         'common',
         "Shifts increase by a fixed amount per slot: +1, +2, +3, +4 (ABCD → BDFH is the template).",
         "Compute the shift tuple explicitly; it must itself form a simple series; apply slot-wise."),
    C.P('Mixed letter-number cluster analogy',
         'common',
         "Clusters like 'B3D : E6J :: H12N : ?' mixing letters and numbers, each with an independent mini-rule.",
         "Split into letter track and number track; solve each; assemble left to right."),
    C.P('Select the pair with the same relation',
         'common',
         "A model pair followed by four complete pairs — choose the one with the same relation (or the one that breaks it).",
         "One relation sentence from the model; test all four options against the identical sentence; precision decides ties."),
]

# ---------------------------------------------------------------- solved examples
examples = []
examples.append(C.Q(
    'rsn-analogy-ex1',
    "Select the related letters: **CAT : FDW :: PIN : ?**",
    C.sh('PIN', 3) and ['SLQ', 'QLS', 'RMQ', 'SLP'],
    C.sh('PIN', 3),
    "C(3)→F(6), A(1)→D(4), T(20)→W(23): every letter shifts **+3**. Apply +3 to PIN: P(16)→S(19), I(9)→L(12), N(14)→Q(17) → **SLQ**.",
    sc="Position subtraction row: (+3, +3, +3). Copy the tuple onto the probe — no letter-by-letter guessing.",
    d='easy', sub='letter-analogy', pat='letter-cluster analogy with constant shift', t=35))

examples.append(C.Q(
    'rsn-analogy-ex2',
    "Select the related word: **Surgeon : Scalpel :: Carpenter : ?**",
    ['Saw', 'Wood', 'Nail', 'Furniture'],
    'Saw',
    "Relation: worker to his **cutting tool**. Wood is material, Nail is fastener (not the carpenter's cutting tool), Furniture is product. **Saw** is the carpenter's cutting tool.",
    sc="Worker-tool pairs: match *what the tool does* — the surgeon's scalpel cuts, the carpenter's saw cuts.",
    d='easy', sub='word-analogy', pat='word analogy from the standard relation bank', t=30))

examples.append(C.Q(
    'rsn-analogy-ex3',
    "Select the related number: **4 : 20 :: 7 : ?**",
    [56, 49, 63, 42],
    56,
    "4 × 5 = 20 suggests ×5, but 7 × 5 = 35 is absent — so test the next family: 4(4+1) = 20 ✓. Then 7(7+1) = **56**. (49 = 7² is the square trap; the model pair is not 4 : 16.)",
    sc="When the linear guess (×5) misses the options, try n(n+1) — the second most common number-analogy rule.",
    d='medium', sub='number-analogy', pat='number analogy (linear / square / cube)', t=45))

examples.append(C.Q(
    'rsn-analogy-ex4',
    "Select the related letters: **HE : SV :: GO : ?**",
    [C.opp('G') + C.opp('O'), 'TN', 'SM', 'UP'],
    C.opp('G') + C.opp('O'),
    "H(8)+S(19) = 27 and E(5)+V(22) = 27, so the rule is **opposite letters** (Atbash). Opposite of G is T, opposite of O is L → **TL**.",
    sc="Sum 27 confirms Atbash; read the answer straight off the opposite-pairs table A-Z, B-Y, ..., G-T, O-L.",
    d='easy', sub='letter-analogy', pat='opposite-letter (Atbash) analogy', t=35))

# ---------------------------------------------------------------- practice
pr = []
# 1 letter constant shift
_d = C.diffs('DOG', 'GRJ')
assert _d == [3, 3, 3], _d
_pr1_ans = C.shv('CAT', _d)
assert _pr1_ans == 'FDW'
pr.append(C.Q('rsn-analogy-1',
              "Select the related letters: **DOG : GRJ :: CAT : ?**",
              [_pr1_ans, 'CEW', 'DBX', 'BZV'],
              _pr1_ans,
              "G−D = +3, R−O = +3, J−G = +3 (positions). The rule is a constant **+3** shift. C(3)+3 = F(6), A(1)+3 = D(4), T(20)+3 = W(23) → **FDW**.",
              sc="One subtraction row gives (+3, +3, +3); add to the probe cluster using EJOTY anchors.",
              d='easy', sub='letter-analogy', pat='letter-cluster analogy with constant shift', t=35))
C.check_letter_analogy('DOG', 'GRJ', 'CAT', _pr1_ans, pr[0]['options'])

# 2 letter rising shift
pairs2 = ('ABCD', 'BDFH')
_d2 = C.diffs(*pairs2)
assert _d2 == [1, 2, 3, 4], _d2
_ans2 = C.shv('MNOP', _d2)
assert _ans2 == 'NPRT'
pr.append(C.Q('rsn-analogy-2',
              "Select the related letters: **ABCD : BDFH :: MNOP : ?**",
              [_ans2, 'MOQS', 'NQSV', 'MQSV'],
              _ans2,
              "A→B = +1, B→D = +2, C→F = +3, D→H = +4: the shifts themselves rise by 1. Apply (+1, +2, +3, +4) to MNOP: M+1=N, N+2=P, O+3=R, P+4=T → **NPRT**.",
              sc="If constant shift fails, check whether the shift tuple itself is a series (+1,+2,+3,...) — the next most common rule.",
              d='medium', sub='letter-analogy', pat='rising-shift letter analogy', t=40))
C.check_letter_analogy('ABCD', 'BDFH', 'MNOP', _ans2, pr[1]['options'])

# 3 Atbash
_ans3 = C.opps('SUN')
assert _ans3 == 'HFM'
pr.append(C.Q('rsn-analogy-3',
              "Select the related letters: **CAT : XZG :: SUN : ?**",
              [_ans3, 'UFO', 'FWI', 'GIM'],
              _ans3,
              "C(3)+X(24) = 27, A(1)+Z(26) = 27, T(20)+G(7) = 27 → opposite letters. S↔H, U↔F, N↔M → **HFM**.",
              sc="Position sum 27 = Atbash; convert through the opposite-pairs table in one pass.",
              d='easy', sub='letter-analogy', pat='opposite-letter (Atbash) analogy', t=35))
C.check_letter_analogy('CAT', 'XZG', 'SUN', _ans3, pr[3 - 1]['options'])

# 4 reversal + shift
# model: 'EAT' -> 'WBU'? keep pure reversal: 'DOT':'TOD' :: 'RAT': 'TAR'
_ans4 = 'TAR'
pr.append(C.Q('rsn-analogy-4',
              "Select the related letters: **DOT : TOD :: RAT : ?**",
              [_ans4, 'ATR', 'RTA', 'TRA'],
              _ans4,
              "TOD is DOT **reversed**. Reversing RAT gives T-A-R → **TAR**.",
              sc="Read the second cluster backwards; if it equals the first (or a constant shift of it), reverse the probe.",
              d='easy', sub='letter-analogy', pat='reversal letter analogy', t=30))
C.check_letter_analogy('DOT', 'TOD', 'RAT', _ans4, pr[-1]['options'])

# 5 two-slot letter with different shifts
_d5 = C.diffs('PM', 'SO')  # P->S +3, M->O +2
assert _d5 == [3, 2], _d5
_a5 = C.shv('KY', _d5)
assert _a5 == 'NA'
pr.append(C.Q('rsn-analogy-5',
              "Select the related letters: **PM : SO :: KY : ?**",
              [_a5, 'NR', 'MP', 'OQ'],
              _a5,
              "P(16)→S(19) is +3, M(13)→O(15) is +2: tuple (+3, +2). K(11)+3 = N(14), Y(25)+2 = 27 → A(1) → **NA**.",
              sc="Per-slot shifts can differ; always subtract slot-wise, never assume one k for all slots.",
              d='medium', sub='letter-analogy', pat='letter-cluster analogy with constant shift', t=40))
C.check_letter_analogy('PM', 'SO', 'KY', _a5, pr[-1]['options'])

# 6 word: adult-young
pr.append(C.Q('rsn-analogy-6',
              "Select the related word: **Sheep : Lamb :: Goat : ?**",
              ['Kid', 'Cub', 'Foal', 'Puppy'],
              'Kid',
              "Relation: adult animal to its **young one**. The young of a goat is a **kid**. Cub → lion/tiger/bear, Foal → horse, Puppy → dog.",
              sc="Young-ones bank: sheep-lamb, goat-kid, horse-foal, cow-calf, dog-puppy, lion-cub, deer-fawn.",
              d='easy', sub='word-analogy', pat='word analogy from the standard relation bank', t=30))

# 7 word: country-currency
pr.append(C.Q('rsn-analogy-7',
              "Select the related word: **Japan : Yen :: Bangladesh : ?**",
              ['Taka', 'Rial', 'Dinar', 'Kyat'],
              'Taka',
              "Relation: country to its **currency**. Bangladesh's currency is the **taka**. Rial → Oman/Saudi Arabia, Dinar → Kuwait/Jordan, Kyat → Myanmar.",
              sc="Currency bank: Japan-yen, Bangladesh-taka, Myanmar-kyat, Mongolia-tugrik, Vietnam-dong.",
              d='easy', sub='word-analogy', pat='word analogy from the standard relation bank', t=30))

# 8 word: instrument-quantity
pr.append(C.Q('rsn-analogy-8',
              "Select the related word: **Barometer : Pressure :: Odometer : ?**",
              ['Distance', 'Speed', 'Temperature', 'Current'],
              'Distance',
              "Relation: instrument to the quantity it **measures**. An odometer measures **distance** travelled. Speed → speedometer, Temperature → thermometer, Current → ammeter.",
              sc="Instrument bank: barometer-pressure, odometer-distance, sphygmomanometer-blood pressure, hygrometer-humidity.",
              d='easy', sub='word-analogy', pat='word analogy from the standard relation bank', t=30))

# 9 word: worker-workplace (same-relation selection)
pr.append(C.Q('rsn-analogy-9',
              "Chef : Kitchen — choose the pair with the **same** relation:",
              ['Judge : Court', 'Tailor : Fabric', 'Teacher : Student', 'Doctor : Medicine'],
              'Judge : Court',
              "Relation: professional to the **place of work**. Judge works in a court ✓. Tailor : Fabric is worker-material, Teacher : Student is worker-person served, Doctor : Medicine is worker-object used.",
              sc="Same-relation selection: test every option against one sentence — 'second is where the first works'.",
              d='easy', sub='word-analogy', pat='select the pair with the same relation', t=30))

# 10 word: study-subject
pr.append(C.Q('rsn-analogy-10',
              "Select the related word: **Zoology : Animals :: Entomology : ?**",
              ['Insects', 'Birds', 'Fishes', 'Soil'],
              'Insects',
              "Relation: branch of study to its **subject**. Entomology is the study of **insects**. (Ornithology → birds, Ichthyology → fishes, Pedology → soil.)",
              sc="Study bank: entomology-insects, ornithology-birds, ichthyology-fishes, etymology-word origins.",
              d='medium', sub='word-analogy', pat='word analogy from the standard relation bank', t=35))

# 11 number: linear k,r
C.check_num_analogy([(12, 26)], 20, 42, [42, 40, 44, 38])
pr.append(C.Q('rsn-analogy-11',
              "Select the related number: **12 : 26 :: 20 : ?**",
              [42, 40, 44, 38],
              42,
              "26 = 12 × 2 + 2, so the rule is **double and add 2**. 20 × 2 + 2 = **42**.",
              sc="For two-digit pairs where b ≈ 2a, test 'k·a + r' with small k first; 12×2+2=26 verifies in one line.",
              d='easy', sub='number-analogy', pat='number analogy (linear / square / cube)', t=35))

# 12 number: cube
C.check_num_analogy([(2, 8)], 3, 27, [27, 24, 29, 33])
pr.append(C.Q('rsn-analogy-12',
              "Select the related number: **2 : 8 :: 3 : ?**",
              [27, 24, 29, 33],
              27,
              "8 = 2³, so the relation is **cube**. 3³ = **27**. (×4 would give 12 and square-plus-4 gives 13 — neither is offered; the cube reading is the intended, and only surviving, rule.)",
              sc="When b = a² or a³ exactly, the answer is the same power of the probe — 8 and 27 scream cubes.",
              d='easy', sub='number-analogy', pat='number analogy (linear / square / cube)', t=30))

# 13 number: n(n+1)
C.check_num_analogy([(6, 42), (4, 20)], 8, 72, [72, 64, 80, 56])
pr.append(C.Q('rsn-analogy-13',
              "Select the related number: **4 : 20 :: 6 : 42 :: 8 : ?**",
              [72, 64, 80, 56],
              72,
              "4(4+1) = 20 and 6(6+1) = 42 confirm the rule **n(n+1)**. Then 8(8+1) = **72**.",
              sc="Two model pairs pin the rule exactly — with n(n+1) confirmed, no other reading competes.",
              d='medium', sub='number-analogy', pat='number analogy (linear / square / cube)', t=40))

# 14 number: digit sum
C.check_num_analogy([(25, 49)], 34, 49, [49, 47, 52, 45])
pr.append(C.Q('rsn-analogy-14',
              "Select the related number: **25 : 49 :: 34 : ?**",
              [49, 47, 52, 45],
              49,
              "Digit sum of 25 is 2+5 = 7 and 7² = 49. Digit sum of 34 is 3+4 = 7, and 7² = **49**. Both members share digit sum 7 — the answer is its square again.",
              sc="When a and b look unrelated, compute the digit sum: many CGL analogies are (digit sum)² or (digit sum)×k.",
              d='medium', sub='number-analogy', pat='number analogy digit operation', t=45))

# 15 mixed cluster
# model: B3D : E6J ; letters +3, number = position of second letter? B->3 is C? let's design: number = 3 * (position of first letter)? B=2 ->6? model first B3D: number 3.
# design cleanly: number = position of middle? no middle. Use: number = p(first)+p(last)? B+D=2+4=6? but model number is 3.
# simplest: letters shift +3, number doubles: B3D:E6J (3->6). probe H12N -> ?
_a15 = 'K' + '24' + 'Q'
assert C.shv('HN', [3, 3]) == 'KQ'
pr.append(C.Q('rsn-analogy-15',
              "Select the related cluster: **B3D : E6J :: H12N : ?**",
              [_a15, 'K15Q', 'K24M', 'J24Q'],
              _a15,
              "Letters: B→E and D→J are both **+3** (B=2→5=E, D=4→10=J). Number: 3→6 is **×2**. Apply to H12N: H+3 = K, N+3 = Q, 12×2 = 24 → **K24Q**.",
              sc="Mixed clusters: solve the letter track (+3, +3) and the number track (×2) separately, then assemble.",
              d='hard', sub='mixed-analogy', pat='mixed letter-number cluster analogy', t=50))

topic_obj = C.topic(
    'analogy', 'Analogy', 'high', {'tier1': 3, 'tier2': 4},
    "Analogy questions give you one pair (of words, numbers or letter clusters) and ask you to repeat its relationship on a second pair. CGL typically asks 3-5. The skill is naming the relationship precisely — as a one-line sentence or a shift tuple — and testing every option against it.",
    subs, patterns, examples, pr)

C.write_topic(topic_obj)
print('OK analogy')
