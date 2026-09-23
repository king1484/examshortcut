from common import q, write_topic, md_table

# ------------------------------------------------------------- word banks
IE_ROWS = [
    ["believe", "beleive", "i before e when it rhymes with 'long e' (bel-eve)"],
    ["achieve", "acheive", "same rule: -ieve"],
    ["friend", "freind", "exception remembered as: fr-I-End — it ends with END"],
    ["mischief", "mischeif", "short-i sound, still ie: -mischief"],
    ["receive", "recieve", "after c the order flips: e before i"],
    ["deceive", "decieve", "c + eive"],
    ["perceive", "percieva", "c + eive"],
    ["conceive", "concieve", "c + eive"],
    ["ceiling", "cieling", "c + eiling"],
    ["ceiling fan", "cieling fan", "the c governs: ei"],
    ["weird", "wierd", "famous exception: ei, no c needed"],
    ["seize", "sieze", "exception: seize the ei"],
    ["height", "hieght", "exception: h-eight (compare weight)"],
    ["weight", "waight", "ei like height — they rhyme and match"],
    ["foreign", "foriegn", "exception: foreign keeps ei"],
    ["sovereign", "soveriegn", "same family as foreign: -reign"],
    ["leisure", "liesure", "exception: lei-sure"],
    ["either", "iether", "ei family"],
    ["neither", "niether", "ei family"],
    ["their", "thier", "possessive of they: ei (th-eir)"],
]

DOUBLE_ROWS = [
    ["accommodate", "accomodate", "room for double c AND double m — the biggest room in spelling"],
    ["occurrence", "occurence", "double c, double r, then -ence"],
    ["occurred", "occured", "occur → occurred: double r, single-ended"],
    ["committee", "comittee", "double m, double t, double e: com-mit-tee"],
    ["embarrass", "embarass", "double r and double s: em-barr-ass"],
    ["beginning", "begining", "be-GIN → beGinning: the g doubles (gin is stressed)"],
    ["planned", "planed", "plan → planned (planed means smoothed wood)"],
    ["referring", "refering", "refer → referring: r doubles"],
    ["preferred", "prefered", "prefer → preferred: r doubles"],
    ["controlled", "controled", "control → controlled: l doubles (British)"],
    ["benefited", "benifitted", "benefit → benefited: only ONE t (stress not on -fit)"],
    ["targeted", "targetted", "target → targeted: ONE t"],
    ["visited", "vissited", "visit → visited: ONE t"],
    ["answered", "anwsered", "answer keeps its w: an-swer-ed"],
]

SUFFIX_ROWS = [
    ["independent", "independant", "ends -ENT (like dependent, consistent)"],
    ["dependent", "dependant", "ends -ENT (note: 'dependant' is the British noun for a reliant person — SSC prefers dependent in adjectival use)"],
    ["persistent", "persistant", "persist + ent"],
    ["resistant", "resistent", "resist + ant"],
    ["arrogant", "arrogent", "arrog- + ant"],
    ["prominent", "prominant", "promin- + ent"],
    ["existence", "existance", "exist + ence"],
    ["persistence", "persistense", "persist + ence"],
    ["resistance", "resistence", "resist + ance"],
    ["maintenance", "maintainance", "maintain → maintenance (the 'ai' shortens)"],
    ["appearance", "appearence", "appear + ance"],
    ["allegiance", "allegience", "allegi- + ance"],
    ["nuisance", "nuisence", "nuis- + ance"],
    ["hindrance", "hindrence", "keep the d: hindrance (from hinder)"],
    ["accessible", "accessable", "-IBLE after 'cess'"],
    ["irresistible", "irresistable", "-IBLE (re + sist + ible)"],
    ["feasible", "feasable", "-IBLE"],
    ["noticeable", "noticable", "keep the e: notice + able (e saves the soft c)"],
    ["changeable", "changable", "keep the e before -able"],
    ["manageable", "managable", "keep the e"],
    ["courageous", "couragous", "keep the e before -ous"],
    ["outrageous", "outragous", "keep the e"],
    ["sufficient", "sufficent", "-CIENT (like efficient, ancient)"],
    ["efficient", "efficent", "-CIENT"],
    ["efficient", "efficiant", "-CIENT, not -iant"],
    ["ancient", "anciant", "-CIENT"],
    ["science", "sceince", "sci + ence"],
    ["conscience", "concience", "con + science — science is hiding inside"],
    ["magnificent", "magnificant", "-CENT at the end"],
    ["questionnaire", "questionaire", "double n, then -naire (French 'naire')"],
    ["millennium", "millenium", "double l AND double n: mil-lenn-ium"],
]

TRAP_ROWS = [
    ["privilege", "priviledge", "no 'd' anywhere: priv-i-lege"],
    ["rhythm", "rythm", "no vowel except y: Rh-y-th-m — 'Rhythm Helps Your Two Hips Move'"],
    ["government", "goverment", "the n of 'govern' survives: govern + ment"],
    ["environment", "enviroment", "the n of 'environ' survives: environ + ment"],
    ["separate", "seperate", "there's 'a rat' in sePArATE"],
    ["desperate", "desparate", "despERate — it ends -ERate"],
    ["definite", "definate", "ends -INITE (finite inside: def-inite)"],
    ["definitely", "definately", "definite + ly"],
    ["restaurant", "restaraunt", "rest-au-rant: the AU sits in the middle"],
    ["truly", "truely", "true loses its e: tru-ly"],
    ["argument", "arguement", "argue loses its e: argu-ment"],
    ["ninth", "nineth", "nine → ninth: the e drops (unlike nine + th = ninety is different)"],
    ["forty", "fourty", "forty has NO u (four does)"],
    ["publicly", "publically", "public + ly — no extra 'al' (unlike tragically)"],
    ["finally", "fianlly", "final + ly: one l in the middle, one at the end"],
    ["mischievous", "mischevious", "ends -VOUS, three syllables: MIS-chi-vous"],
    ["queue", "queu", "q-u-e-u-e: five letters, only Q speaks"],
    ["vacuum", "vaccum", "double u: vac-uum"],
    ["potato", "potatoe", "no e at the end"],
    ["tomatoes", "tomatos", "es after o in the plural"],
    ["embarrassment", "embarrasment", "embarrass + ment keeps both doubles"],
    ["supersede", "superceed", "the only -ede in English: super-sede"],
    ["proceed", "procede", "-CEED: proceed, succeed, exceed"],
    ["succeed", "suckseed", "proceed family"],
    ["exceed", "excede", "proceed family"],
    ["concede", "concied", "-CEDE (different from the -CEED three)"],
    ["guarantee", "gaurantee", "gua first, then rantee"],
    ["parallel", "paralell", "double r in the middle, double l at the end"],
    ["harass", "harrass", "ONE r, double s — opposite of embarrass (which has double r)"],
    ["collectible", "collectable", "-IBLE (both exist, but 'collectible' is the standard noun)"],
    ["calendar", "calender", "ends -DAR (the machine is a calender; the dates are a calendar)"],
    ["camaraderie", "comradery", "camara- + derie"],
    ["silhouette", "silohuette", "sil-hou-ette: double t"],
    ["bureaucracy", "buerocracy", "bureau + cracy"],
    ["connoisseur", "conoisseur", "double n, -sseur"],
    ["liaison", "liason", "the first i is silent in sound but present in spelling: lia-ison"],
    ["weird", "wiered", "exception word"],
    ["grateful", "greatful", "grate + ful — 'great' is NOT inside it"],
    ["a lot", "alot", "always two words"],
    ["all right", "alright", "formal spelling is two words"],
    ["skiing", "skiing", "i-i collision is correct here"],
    ["radii", "radiuses", "plural of radius: radi-i"],
    ["criterion", "criterias", "plural is criteria (no s on criteria)"],
    ["phenomenon", "phenomenas", "plural is phenomena"],
    ["stimulus", "stimuluses", "plural is stimuli"],
    ["analysis", "analysises", "plural is analyses"],
    ["crisis", "crisises", "plural is crises"],
    ["cactus", "cactuses", "classical plural is cacti"],
]

TOTAL = len(IE_ROWS) + len(DOUBLE_ROWS) + len(SUFFIX_ROWS) + len(TRAP_ROWS)
assert TOTAL >= 80, f"spelling bank too small: {TOTAL}"

def bank_table(title, rows):
    return f"**{title}**\n\n| Correct | Trap spelling | Hook |\n|---|---|---|\n" + "\n".join(
        f"| **{c}** | ~~{t}~~ | {h} |" for c, t, h in rows)

SUBTOPICS = [
    {
        "id": "spell-ie-rule",
        "title": "i before e — and the exceptions that fill the paper",
        "concept": f"""**The rule:** write *i* before *e* when both spell the long 'ee' sound (bel**ie**ve, ach**ie**ve, gr**ie**f, f**ie**ld, sh**ie**ld); after the letter **c**, flip it — *e* before *i* (re**cei**ve, de**cei**ve, per**cei**ve, con**cei**ve, **cei**ling). Extended mnemonic: *i before e except after c, or when sounded like 'ay' as in neighbour and weigh* (n**ei**ghbour, w**ei**gh, h**ei**ght is the 'ay'-sound family too).

**But the SSC paper lives in the exceptions.** The high-frequency exceptions are: **weird, seize, height, foreign, sovereign, leisure, either, neither, their, counterfeit, surplus-free words like protein** — memorise as a 10-word list; they appear as options constantly.

{bank_table("i/e and e/i words", IE_ROWS)}

**Exam shape:** four spellings of the same word, one letter shifted. Read the options letter by letter — the difference is almost always one vowel pair: recieve/receive, wierd/weird. If the word follows 'c', demand 'ei'; if it doesn't, demand 'ie' — then check the exception list.""",
        "formulas": [],
        "tricks": [
            {
                "title": "The c-test",
                "body": "Is there a c right before the pair? c → 'ei' (receive). No c → usually 'ie' (believe). Ten exceptions override: weird, seize, height, foreign, sovereign, leisure, either, neither, their, protein.",
            },
            {
                "title": "Rhyme-anchor pairs",
                "body": "height–weight rhyme and must match; believe–achieve match; receive–deceive match. Fix one of each pair forever and its partner comes free.",
            },
            {
                "title": "Say it in syllables",
                "body": "Pronounce the word slowly in your head — be-lieve, re-ceive. The mouth half-confirms what the eye doubts.",
            },
        ],
        "mistakes": [
            "Applying the rule to 'height' and writing 'hieght' — it is on the exception list.",
            "Writing 'sciense' — after c comes 'ie' here only because the c is in 'sci' pronounced 's' + long i: memorise con-science = con + science.",
            "Missing that 'friend' is ie, not ei — it does not rhyme with 'long e' but the spelling is still ie.",
            "Trusting sound alone: 'receve' sounds right but has lost the i entirely.",
        ],
    },
    {
        "id": "spell-doubling",
        "title": "Doubling consonants and one-letter betrayals",
        "concept": f"""**When does the final consonant double before a suffix?** Three conditions, all true:
1. The word ends **consonant–vowel–consonant** (CVC: be**gin**, o**ccur**, re**fer**).
2. The suffix begins with a **vowel** (-ing, -ed, -ance, -ence…).
3. The **stress** falls on that last syllable (be**GIN** → beginning; pre**FER** → preferred).

If stress is elsewhere, no doubling: **BENefit** → benefited (one t), **VISit** → visited, **TARget** → targeted, **ANSwer** → answered.

{bank_table("Doubling and one-letter traps", DOUBLE_ROWS)}

**The fixed doubles** — words where the doubling is simply part of the word: accommodate (c+m), committee (m+t+e), embarrass (r+s), occurrence/occurred (c+r), millennium (l+n), questionnaire (n), silhouette (t), parallel (r at middle… l at end).

**Benefited/targeted/visited** are gold: papers plant 'benefitted' and 'targetted' as plausible options, and they are always wrong.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Stress decides doubling",
                "body": "Say the word. If the last syllable is stressed, double before a vowel-suffix (begin→beginning, occur→occurred). If not, don't (benefit→benefited).",
            },
            {
                "title": "Double-double checklist",
                "body": "Five words need TWO doubled letters: accommodate (c,m), committee (m,t), embarrass (r,s), occurrence (c,r), millennium (l,n). Count them.",
            },
            {
                "title": "Letter census",
                "body": "In the options, count the repeated letters. accommodate must show 2 c's and 2 m's; embarrass 2 r's and 2 s's. Eliminate on census failure.",
            },
        ],
        "mistakes": [
            "Writing 'benefitted' by analogy with 'preferred' — benefit is stress-initial.",
            "One double in 'accommodate' (accomodate / acommodate) — both doubles required.",
            "Writing 'ocurrence' — the c doubles AND the r doubles.",
            "Spelling 'planed' for 'planned' — planed is a different word (smoothed wood).",
        ],
    },
    {
        "id": "spell-suffix-endings",
        "title": "-able / -ible, -ance / -ence, -ant / -ent",
        "concept": f"""Three suffix pairs account for a third of SSC spelling items. There is no perfect rule — but there are reliable family anchors:

**-ance vs -ence:** trace the word to its root. persist → persist**ence** (though resist → resist**ance**!). Reliable set: -ence after **fer** (reference, preference, difference, inference), and exist**ence**, independ**ence** (noun) / independ**ent**, depend**ent**, consist**ent**, promin**ent**, magnific**ent**. -ance in: maintain**ance**, appear**ance**, resist**ance**, allegi**ance**, nuis**ance**, hindr**ance** (keep the d), assist**ance**.

**-able vs -ible:** -ible after word-ends in **-cess** (accessible), **-sist** is mixed (resistible → irresist**ible**, but …). Practical set: access**ible**, irresist**ible**, feas**ible**, audit**ible**, vis**ible**, terr**ible**, horror+horr**ible**. -able in: notice**able**, change**able**, manage**able** (keep the e!), comfort**able**, accept**able**, remark**able**, avail**able**.

{bank_table("Suffix families", SUFFIX_ROWS)}

**Memory economics:** don't learn 'rules' — learn the 30-word families above as units. In the options, the three wrong spellings each break a different letter, so ONE remembered family member settles the item.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Root trace",
                "body": "Strip the suffix and look at the root: exist→exist-ence, maintain→maintenance (ai shortens), resist→resist-ance, persist→persist-ence. The root's own spelling decides.",
            },
            {
                "title": "-fer always -ence",
                "body": "Words from 'fer' nouns take -ence: reference, preference, difference, inference. Verbs keep one f or double by stress: refer→referring, but reference.",
            },
            {
                "title": "Scient family",
                "body": "One family handles four words: sufficient, efficient, ancient, science (and conscience = con + science). All -cient/-ience.",
            },
        ],
        "mistakes": [
            "Writing 'persistant' by analogy with 'resistant' — the pair split: persist-ence, resist-ance.",
            "Dropping the e in 'noticeable' — the e protects the soft c.",
            "Writing 'maintainance' — maintain's 'ai' shortens to 'e'.",
            "Writing 'magnificant' — it ends -cent.",
        ],
    },
    {
        "id": "spell-trap-words",
        "title": "The trap-word bank: silent letters and inherited mistakes",
        "concept": f"""These words are misspelt the same way by lakhs of candidates, which is exactly why examiners choose them. Each carries one hidden letter or one missing letter:

{bank_table("Trap words", TRAP_ROWS)}

**Groups inside the bank:**
- **Silent letters preserved:** government (n), environment (n), rhythm (no vowel but y), queue, vacuum (uu), liaison (i), silhouette (t,h).
- **Missing-letter classics:** truly (no e), argument (argue drops e), ninth (nine drops e), forty (no u), publicly (no 'al'), definite (not -ate).
- **Foreign borrowings:** restaurant (au), guarantee (gua), bureaucracy (eau), connoisseur, camaraderie, questionnaire, millennium.
- **-ceed vs -cede:** only THREE words take -ceed: proceed, succeed, exceed. Everything else takes -cede: concede, recede, precede. And one loner: **supersede** is the only -sede in English.
- **Plurals:** criteria (not criterias), phenomena (not phenomenas), stimuli, analyses, crises — plural already means many; adding s doubles it wrongly.

Revise this bank weekly; it is the single highest-yield page in the topic.""",
        "formulas": [],
        "tricks": [
            {
                "title": "The n-test for -ment words",
                "body": "government = govern+ment, environment = environ+ment: the root's final n must survive. Ask 'what is the root?' — the letter reappears.",
            },
            {
                "title": "Three -ceed, one -sede",
                "body": "proceed, succeed, exceed = the only -ceed words; supersede = the only -sede. All other 'seed-sound' words are -cede.",
            },
            {
                "title": "No- doubling plurals",
                "body": "criteria, phenomena, stimuli, data already are plurals — any option adding -s to them is instantly wrong.",
            },
        ],
        "mistakes": [
            "Writing 'gaurantee' — swap of a and u; gua-rantee.",
            "Writing 'greatful' — grate + ful; 'great' is not in the word.",
            "Writing 'alot' — it is always two words: a lot.",
            "Writing 'calender' for the date-chart — the machine spelling.",
        ],
    },
    {
        "id": "spell-strategy",
        "title": "Exam strategy: how to judge a spelling you have never seen",
        "concept": f"""The item shows four spellings of one word and asks for the correct one. Even when the word is unfamiliar, four elimination moves settle most items:

1. **Find the difference.** Scan the four options letter by letter; they differ in one or two spots (recie-ve / recei-ve / rece-ve). Concentrate only on the differing spot.
2. **Apply the rule that spot obeys.** c before the pair → ei. Root -fer → -ence noun. CVC stressed → doubling. If no rule applies, it is a bank word — the weekly bank revision answers it.
3. **Say each option.** The mouth knows rhythm: 'mis-CHEE-vious' (4 syllables) is wrong because mischievous has 3.
4. **Syllable-split check.** Split into syllables and confirm no letter is missing or doubled: res-tau-rant → rest-au-rant needs the au.

**Daily plan (15 minutes):** 10 new bank words + rewrite yesterday's 10 from memory, marking every miss. Self-dictation — write sentences containing bank words, then re-check spelling a day later — converts seeing into spelling.

**In the exam:** 25–35 seconds. Most SSC spelling items are bank words; the rest yield to the c-test and the stress rule. Never leave it blank — there is no penalty pattern that favours skipping over one informed guess among four.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Difference-first reading",
                "body": "Don't read four full words — read the one letter-position where they differ. Options are built to differ in a single spot; that spot is the entire question.",
            },
            {
                "title": "Syllable count",
                "body": "Count syllables: mischievous (3), restaurant (2-3 as res-tau-rant), rhythm (2). A wrong spelling often forces a syllable that cannot be pronounced.",
            },
            {
                "title": "Write-from-memory drill",
                "body": "Recognition is not recall. Cover the bank, write the words, mark misses, repeat tomorrow — misses halve each cycle.",
            },
        ],
        "mistakes": [
            "Choosing the option that 'looks nicer' — options are engineered so the wrong one looks smoother.",
            "Skipping letter-by-letter comparison; one letter is the whole item.",
            "Ignoring AmE/BrE traps — SSC follows British spelling, so favour travelled/colour/centre forms when they appear.",
            "Guessing on bank words instead of trusting the weekly revision — these are the free marks.",
        ],
    },
]

PATTERNS = [
    {
        "pattern": "Choose the correctly spelt word",
        "frequency": "very common",
        "howToSpot": "Four spellings of one word; find the correct one.",
        "approach": "Find the differing letter-spot, apply the relevant rule (c-test, stress-doubling, suffix family), else recall from the bank.",
    },
    {
        "pattern": "Find the wrongly spelt word",
        "frequency": "common",
        "howToSpot": "Four words in a sentence or list; three are right, one carries a trap letter.",
        "approach": "Scan each word for its silent-letter/double-letter signature; the odd one out fails its own census.",
    },
    {
        "pattern": "Spelling inside a sentence",
        "frequency": "occasional",
        "howToSpot": "A sentence with four underlined words; pick the misspelt one.",
        "approach": "Same census method; read the underlined words one by one, not the sentence flow.",
    },
    {
        "pattern": "Plural/derived form spelling",
        "frequency": "occasional",
        "howToSpot": "The stem offers plural or derived forms (criteria/criterias, analyses/analysises).",
        "approach": "Recall the classical plural bank (criteria, phenomena, stimuli, analyses, crises) — an added -s is instantly wrong.",
    },
]

SE = [
    q("eng-spell-s01", "Select the correctly spelt word.",
      ["Occurence", "Occurrance", "Occurrence", "Ocurrence"], 2,
      "The word from 'occur' doubles **both** c and r and ends **-ence**: occurrence. Census: two c's, two r's. Occurence (one r), Occurrance (-ance), Ocurrence (one c) all fail.",
      "Census test: occur → cc + rr + ence.",
      "easy", "spell-doubling", "double-letter census", 25),
    q("eng-spell-s02", "Select the correctly spelt word.",
      ["Priviledge", "Privelege", "Privillege", "Privilege"], 3,
      "Privilege has **no d** and **no double l**: priv-i-lege. The 'd' in 'priviledge' is the classic planted error — there is no 'd' sound in careful speech either.",
      "No-d test: privilege contains no letter d at all.",
      "easy", "spell-trap-words", "bank word", 25),
    q("eng-spell-s03", "Select the correctly spelt word.",
      ["Maintainance", "Maintenance", "Maintenence", "Maintanance"], 1,
      "From 'maintain', the **'ai' shortens to 'e'** and the ending is **-ance**: maintenance. So Maintainance (keeps ai), Maintenence (-ence), Maintanance (drops the i) are all wrong.",
      "Root trace: maintain → maintenance (ai → e, end -ance).",
      "medium", "spell-suffix-endings", "root trace", 30),
]

PRACTICE = [
    q("eng-spell-p01", "Select the correctly spelt word.",
      ["Embarrass", "Embarass", "Embarras", "Embarress"], 0,
      "Embarrass carries **double r and double s** — em-barr-ass. Each distractor drops exactly one of the doubles.",
      "Double-double word: r and s both doubled.",
      "easy", "spell-doubling", "census", 25),
    q("eng-spell-p02", "Select the correctly spelt word.",
      ["Rythm", "Rhythem", "Rhythm", "Rythmn"], 2,
      "Rhythm has **no vowel except y**: Rh-y-th-m. Mnemonic: Rhythm Helps Your Two Hips Move. Rhythem plants a fake e; Rythm drops the h.",
      "No-vowel word — count letters: r-h-y-t-h-m (6).",
      "medium", "spell-trap-words", "bank word", 30),
    q("eng-spell-p03", "Select the correctly spelt word.",
      ["Indepandent", "Independant", "Indipendent", "Independent"], 3,
      "Independent ends **-ent** (same family as dependent, consistent, persistent). Every distractor swaps the final vowel pair.",
      "The -ent family: independent, dependent, consistent.",
      "easy", "spell-suffix-endings", "suffix family", 25),
    q("eng-spell-p04", "Select the correctly spelt word.",
      ["Comittee", "Commitee", "Committe", "Committee"], 3,
      "Committee doubles **m, t and e**: com-mit-tee. The census needs mm, tt, ee — only the fourth option shows all three.",
      "Triple-double word: m, t, e.",
      "easy", "spell-doubling", "census", 25),
    q("eng-spell-p05", "Select the correctly spelt word.",
      ["Seperate", "Saperate", "Separate", "Separete"], 2,
      "Separate: remember there is **'a rat' in sePArATE** — the middle vowel is a, not e. This is the most-failed word in the bank.",
      "'A rat' hides inside sePArATE.",
      "easy", "spell-trap-words", "mnemonic", 25),
    q("eng-spell-p06", "Select the correctly spelt word.",
      ["Questionnaire", "Questionaire", "Questionnair", "Questionierre"], 0,
      "From French questionnaire: **double n** and the ending **-naire**. Questionaire loses an n; Questionnair drops the final e.",
      "French -naire with double n.",
      "medium", "spell-trap-words", "bank word", 30),
    q("eng-spell-p07", "Select the correctly spelt word.",
      ["Suficient", "Sufficient", "Sufficent", "Sufficiant"], 1,
      "The **-cient family**: sufficient, efficient, ancient. The spelling needs ff + ie + nt.",
      "Scient family: -cient.",
      "easy", "spell-suffix-endings", "family", 25),
    q("eng-spell-p08", "Select the correctly spelt word.",
      ["Millenium", "Millenneum", "Millennium", "Millanneum"], 2,
      "Millennium doubles **l and n**: mil-lenn-ium (from Latin mille + annus). The distractors each drop or move one double.",
      "Double-double: l and n.",
      "medium", "spell-doubling", "census", 30),
    q("eng-spell-p09", "Select the correctly spelt word.",
      ["Desparate", "Desperate", "Desperete", "Disperate"], 1,
      "Desperate ends **-perate**: desp-ER-ate. 'Desparate' (the common swap to -ara-) is the planted error.",
      "Ends -ERate: desperate.",
      "easy", "spell-trap-words", "bank word", 25),
    q("eng-spell-p10", "Select the correctly spelt word.",
      ["Restaurant", "Restaraunt", "Restarant", "Restauraunt"], 0,
      "Restaurant = **rest-au-rant**: the 'au' sits between rest and rant. Restaraunt reverses to 'ar'; Restauraunt adds a phantom u.",
      "rest-AU-rant: au in the middle.",
      "easy", "spell-trap-words", "bank word", 25),
    q("eng-spell-p11", "Select the correctly spelt word.",
      ["Mischevious", "Mischevous", "Mischievous", "Mischievious"], 2,
      "Mischievous has **three syllables** (MIS-chi-vous) and ends **-vous**. Mischevious/mischievious insert an extra syllable — the classic error.",
      "Syllable count: 3 — MIS-chi-vous.",
      "medium", "spell-trap-words", "syllables", 30),
    q("eng-spell-p12", "Select the correctly spelt word.",
      ["Noticeable", "Noticable", "Noticeble", "Notessible"], 0,
      "Keep the **e** before -able: noticeable. The e protects the soft 'c' sound (notice → notice-able). Noticable is the planted drop.",
      "Keep-e rule: soft c needs its e.",
      "easy", "spell-suffix-endings", "keep-e rule", 25),
    q("eng-spell-p13", "Select the correctly spelt word.",
      ["Occurance", "Occurrence", "Occurence", "Ocurrance"], 1,
      "Occurrence: double c, double r, **-ence** ending. Occurance/Ocurrance take -ance; Occurence drops an r.",
      "cc + rr + ence.",
      "easy", "spell-doubling", "census", 25),
    q("eng-spell-p14", "Select the correctly spelt word.",
      ["Goverment", "Government", "Governmant", "Govermant"], 1,
      "The root **govern** keeps its n before -ment: government. Dropping the n is the single most common misspelling in this family.",
      "Root n survives: govern + ment.",
      "easy", "spell-trap-words", "root trace", 25),
    q("eng-spell-p15", "Select the correctly spelt word.",
      ["Truely", "Truelly", "Truly", "Trufully"], 2,
      "True drops its final e before -ly: **truly** (like duly). Truely keeps a phantom e; Truelly doubles an l that was never there.",
      "Drop-e: true → truly, due → duly.",
      "easy", "spell-trap-words", "drop-e rule", 25),
]

topic = {
    "id": "spelling",
    "sectionId": "english",
    "title": "Spelling",
    "order": 9,
    "importance": "medium",
    "avgQuestions": {"tier1": 2, "tier2": 3},
    "summary": "Two spelling items per shift, and they come from a predictable trap list: i/e flip-flops, double-letter failures, suffix endings and 90+ famous misspells. A rules layer (c-test, stress-doubling, keep-e) plus a weekly revised bank makes these near-guaranteed marks — the fastest scoring topic in Tier 1 English.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
