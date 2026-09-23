from common import q, write_topic, md_table

# ---------------------------------------------------------------- word banks
SYNONYMS = [
    # word, own-words meaning, nearest synonym
    ["Abandon", "leave something completely, giving it up", "desert"],
    ["Absolve", "officially declare someone free of blame", "exonerate"],
    ["Abundant", "existing in more than enough quantity", "plentiful"],
    ["Acumen", "sharp, accurate judgement in a field", "insight"],
    ["Adversity", "a state of hardship and trouble", "misfortune"],
    ["Affluent", "having plenty of money", "wealthy"],
    ["Agile", "able to move quickly and easily", "nimble"],
    ["Alleviate", "make pain or trouble less severe", "ease"],
    ["Amiable", "pleasant and friendly in manner", "genial"],
    ["Anonymous", "with the name not revealed", "unnamed"],
    ["Apathy", "complete lack of interest or concern", "indifference"],
    ["Arduous", "needing great effort to finish", "strenuous"],
    ["Astute", "quick to notice and understand things", "perceptive"],
    ["Audacious", "showing bold willingness to take risks", "intrepid"],
    ["Augment", "add to something to make it larger", "boost"],
    ["Authentic", "genuine, exactly what it claims to be", "real"],
    ["Baffle", "make someone unable to understand", "perplex"],
    ["Belligerent", "eager to argue or fight", "hostile"],
    ["Benevolent", "kind and wishing others well", "compassionate"],
    ["Candid", "speaking openly and honestly", "frank"],
    ["Chronic", "continuing for a very long time", "persistent"],
    ["Coerce", "make someone act by force or threats", "compel"],
    ["Commence", "set into motion, begin", "start"],
    ["Complacent", "too satisfied to notice dangers", "smug"],
    ["Condone", "treat an offence as forgivable", "excuse"],
    ["Confiscate", "take away by official authority", "impound"],
    ["Conspicuous", "standing out so as to be easily seen", "noticeable"],
    ["Contemplate", "turn something over in the mind at length", "ponder"],
    ["Copious", "available in large amounts", "ample"],
    ["Corroborate", "support a claim with extra evidence", "verify"],
    ["Culpable", "deserving blame for something", "blameworthy"],
    ["Curtail", "cut something short or reduce it", "reduce"],
    ["Decisive", "able to settle matters quickly and firmly", "resolute"],
    ["Deduce", "arrive at a conclusion by reasoning", "infer"],
    ["Deficit", "the amount by which something falls short", "shortage"],
    ["Deliberate", "done intentionally after thought", "intentional"],
    ["Demolish", "pull a building or structure down", "destroy"],
    ["Deter", "put someone off an act through fear", "dissuade"],
    ["Devout", "deeply religious in daily life", "pious"],
    ["Diligent", "working with steady, careful effort", "industrious"],
    ["Diminish", "become or make smaller", "decrease"],
    ["Discard", "get rid of as no longer useful", "reject"],
    ["Discrepancy", "a difference between things that should match", "mismatch"],
    ["Docile", "quietly obedient, easily managed", "submissive"],
    ["Dubious", "surrounded by doubt, uncertain", "questionable"],
    ["Eloquent", "speaking fluently and persuasively", "articulate"],
    ["Eminent", "famous and greatly respected in a field", "distinguished"],
    ["Endorse", "publicly express support for", "back"],
    ["Ephemeral", "lasting only a very short while", "short-lived"],
    ["Equanimity", "evenness of mind under pressure", "composure"],
    ["Exhaustive", "covering every part of a subject", "thorough"],
    ["Expedite", "make a process move faster", "hasten"],
    ["Fabricate", "make up a false story or object", "invent"],
    ["Falter", "lose strength or begin to hesitate", "waver"],
    ["Feasible", "capable of being done", "practicable"],
    ["Fluctuate", "shift up and down irregularly", "oscillate"],
    ["Frugal", "careful and sparing with money", "thrifty"],
    ["Futile", "producing no useful result", "pointless"],
    ["Genial", "cheerful, warm and sociable", "friendly"],
    ["Grievous", "very serious and severe in harm", "severe"],
    ["Gullible", "too ready to believe things", "credulous"],
    ["Hamper", "get in the way of progress", "hinder"],
    ["Haughty", "proud in an off-putting, superior way", "arrogant"],
    ["Hostile", "unfriendly and showing opposition", "antagonistic"],
    ["Illicit", "not allowed by law", "unlawful"],
    ["Imminent", "about to happen at any moment", "impending"],
    ["Impartial", "treating every side equally", "unbiased"],
    ["Impeccable", "free of any fault", "faultless"],
    ["Implicit", "meant but never directly stated", "implied"],
    ["Inaugurate", "set going by a formal act", "launch"],
    ["Indifferent", "showing no interest either way", "unconcerned"],
    ["Indispensable", "too necessary to do without", "essential"],
    ["Inevitable", "bound to happen, unavoidable", "unavoidable"],
    ["Ingenious", "showing striking cleverness in design", "inventive"],
    ["Innocuous", "completely harmless", "inoffensive"],
    ["Insolent", "disrespectful in a bold, rude way", "impudent"],
    ["Intrepid", "showing no fear", "bold"],
    ["Jubilant", "triumphantly happy", "overjoyed"],
    ["Lethal", "able to cause death", "fatal"],
    ["Lucid", "clear enough to be easily understood", "clear"],
    ["Magnanimous", "generous, especially toward a rival", "generous"],
    ["Mitigate", "soften the severity of something", "lessen"],
    ["Monotonous", "dull because never changing", "tedious"],
    ["Meticulous", "giving attention to every tiny detail", "painstaking"],
    ["Naive", "showing the innocence of inexperience", "innocent"],
    ["Nefarious", "shockingly wicked", "villainous"],
    ["Notorious", "widely known for something bad", "infamous"],
    ["Obsolete", "no longer in use or fashion", "outdated"],
    ["Obstinate", "sticking to an opinion stubbornly", "stubborn"],
    ["Ominous", "warning that trouble is coming", "threatening"],
    ["Opulent", "richly grand and luxurious", "luxurious"],
    ["Pandemonium", "wild, disorderly noise and confusion", "chaos"],
    ["Perpetual", "going on without ending", "constant"],
    ["Placate", "soothe an angry person", "appease"],
    ["Plausible", "sounding believable", "credible"],
    ["Precarious", "unsafe and likely to give way", "risky"],
    ["Precedent", "an earlier case used as a guide", "benchmark"],
    ["Preliminary", "coming before the main part", "introductory"],
    ["Profuse", "given or flowing in large quantity", "lavish"],
    ["Prudent", "careful, sensible and far-sighted", "cautious"],
    ["Rebuke", "scold sharply and officially", "reprimand"],
    ["Recluse", "one who lives shut off from others", "hermit"],
    ["Reluctant", "unwilling and hesitating", "hesitant"],
    ["Resilient", "springing back quickly from hardship", "tough"],
    ["Reticent", "keeping thoughts to oneself", "reserved"],
    ["Rigorous", "strict, demanding and thorough", "stringent"],
    ["Scarce", "present only in small supply", "rare"],
    ["Scrutinise", "examine bit by bit and closely", "inspect"],
    ["Sluggish", "moving or working slowly", "lethargic"],
    ["Sporadic", "occurring now and then, not steadily", "intermittent"],
    ["Squander", "waste money or chances carelessly", "waste"],
    ["Subtle", "so delicate it is easy to miss", "delicate"],
    ["Sundry", "made up of various unrelated items", "assorted"],
    ["Superfluous", "more than what is needed", "excess"],
    ["Tedious", "boring because too long or dull", "dull"],
    ["Tenacious", "holding on firmly and refusing to quit", "persistent"],
    ["Tentative", "not yet fixed or final", "provisional"],
    ["Timid", "shy and easily frightened", "shy"],
    ["Trivial", "of very little importance", "petty"],
    ["Turmoil", "a state of upset and confusion", "upheaval"],
    ["Verbose", "using far more words than needed", "long-winded"],
    ["Vigilant", "carefully watchful for danger", "alert"],
    ["Vindictive", "driven by a wish to take revenge", "vengeful"],
    ["Vivid", "producing sharp, lifelike images in the mind", "graphic"],
    ["Volatile", "changing suddenly and unpredictably", "unstable"],
    ["Weary", "drained of energy, very tired", "exhausted"],
    ["Wither", "dry up and lose freshness", "shrivel"],
    ["Zealous", "filled with burning enthusiasm", "passionate"],
]

ANTONYMS = [
    # word, own-words meaning, opposite
    ["Abundant", "in plentiful supply", "scarce"],
    ["Accept", "take willingly", "reject"],
    ["Advance", "move forward", "retreat"],
    ["Ancient", "belonging to the far past", "modern"],
    ["Artificial", "made by humans, not nature", "natural"],
    ["Benevolent", "kind and well-wishing", "malevolent"],
    ["Bold", "daring and confident", "timid"],
    ["Candid", "open and direct", "evasive"],
    ["Compress", "press into less space", "expand"],
    ["Conceal", "keep out of sight", "reveal"],
    ["Condemn", "declare wrong and harshly criticise", "praise"],
    ["Confirm", "establish as true", "deny"],
    ["Consent", "agree to", "refuse"],
    ["Cordial", "warm and friendly", "hostile"],
    ["Cruel", "causing needless pain", "kind"],
    ["Deficit", "a shortfall in amount", "surplus"],
    ["Deliberate", "done on purpose", "accidental"],
    ["Despair", "complete loss of hope", "hope"],
    ["Diligent", "hardworking", "lazy"],
    ["Discord", "lack of agreement", "harmony"],
    ["Diminish", "grow smaller", "increase"],
    ["Dismiss", "send away from service", "retain"],
    ["Elevate", "lift to a higher place", "lower"],
    ["Famous", "known to many", "obscure"],
    ["Flexible", "able to bend or change", "rigid"],
    ["Fragile", "easily broken", "sturdy"],
    ["Humble", "modest about oneself", "proud"],
    ["Ignore", "refuse to notice", "notice"],
    ["Include", "take in as a part", "exclude"],
    ["Innocent", "free of guilt", "guilty"],
    ["Liberty", "freedom from restraint", "bondage"],
    ["Majority", "the larger number", "minority"],
    ["Maximum", "the greatest possible", "minimum"],
    ["Mourn", "grieve for", "rejoice"],
    ["Native", "belonging by birth", "foreign"],
    ["Optimist", "one who expects the best", "pessimist"],
    ["Permanent", "lasting without change", "temporary"],
    ["Praise", "express strong approval", "criticise"],
    ["Private", "meant for one person or group", "public"],
    ["Profit", "financial gain", "loss"],
    ["Punctual", "exactly on time", "late"],
    ["Rare", "seldom found", "common"],
    ["Remember", "keep in memory", "forget"],
    ["Rural", "of the countryside", "urban"],
    ["Sacred", "holy, devoted to religion", "profane"],
    ["Scatter", "throw about in all directions", "gather"],
    ["Shallow", "not deep", "deep"],
    ["Sharp", "having a fine cutting edge", "blunt"],
    ["Strengthen", "add force or power to", "weaken"],
    ["Superior", "higher in rank or quality", "inferior"],
    ["Transparent", "letting light through", "opaque"],
    ["Uniform", "the same throughout", "varied"],
    ["Vacant", "empty, unoccupied", "occupied"],
    ["Virtue", "moral goodness", "vice"],
    ["Voluntary", "done of free choice", "compulsory"],
    ["Wealthy", "possessing much money", "poor"],
    ["Wild", "living untamed in nature", "tame"],
    ["Withdraw", "pull back or take out", "advance"],
]

assert len(SYNONYMS) + len(ANTONYMS) >= 150, f"word bank too small: {len(SYNONYMS)}+{len(ANTONYMS)}"

syn_table = "| Word | Meaning | Nearest synonym |\n|---|---|---|\n" + "\n".join(
    f"| **{w}** | {m} | {s} |" for w, m, s in SYNONYMS)
ant_table = "| Word | Meaning | Opposite |\n|---|---|---|\n" + "\n".join(
    f"| **{w}** | {m} | {o} |" for w, m, o in ANTONYMS)

root_table = md_table(
    ["Root", "Sense", "Examples"],
    [
        ["bene-", "good, well", "benevolent, benefit, benign, benefactor"],
        ["mal-/male-", "bad", "malevolent, malice, malfunction, malnutrition"],
        ["bon-/eu-", "good", "bona fide, euphoria, eulogy"],
        ["loqu / locut", "speak", "eloquent, loquacious, elocution, soliloquy"],
        ["dict", "say, declare", "dictate, contradict, verdict, predict"],
        ["voc / vok", "call, voice", "vocal, revoke, advocate, invoke"],
        ["cred", "believe", "credible, credulous, incredible, credit"],
        ["mit / miss", "send", "transmit, emissary, remit, missile"],
        ["path", "feeling, suffering", "sympathy, apathy, empathy, pathological"],
        ["sens / sent", "feel", "sensitive, sentiment, consensus, dissent"],
        ["morph", "shape, form", "amorphous, metamorphosis, morpheme"],
        ["chron", "time", "chronic, chronology, synchronise, anachronism"],
        ["temp", "time", "temporary, contemporary, temporal"],
        ["ego", "self", "egocentric, egoist, alter ego"],
        ["ambi / amphi", "both, around", "ambiguous, ambidextrous, amphibious"],
        ["am / amic", "love, friend", "amiable, amicable, amity, amorous"],
        ["anthrop", "human", "anthropology, philanthropy, misanthrope"],
        ["phil", "love", "philanthropy, philosopher, bibliophile"],
        ["phob", "fear", "phobia, hydrophobia, acrophobia"],
        ["gen", "birth, kind", "genius, generate, genocide, congenital"],
        ["graph / scrib / script", "write", "autograph, describe, manuscript, scribble"],
        ["spec / spect", "look", "inspect, spectator, circumspect, perspective"],
        ["vis / vid", "see", "visible, evident, vision, provident"],
        ["aud", "hear", "audible, audience, auditorium"],
        ["port", "carry", "transport, portable, export, deport"],
        ["duc / duct", "lead", "conduct, educate, deduce, aqueduct"],
        [" tract", "pull, draw", "attract, extract, retract, tractable"],
        ["press", "press, push", "compress, depress, impression"],
        ["pos / pon", "place", "position, postpone, deposit, component"],
        ["sequ / secut", "follow", "sequence, consequence, execute, sequel"],
        ["cert", "sure", "certain, certify, ascertain"],
        ["cur / curs", "run", "current, excursion, cursory, cursive"],
        ["rupt", "break", "rupture, interrupt, bankrupt, erupt"],
        ["fid", "faith", "confide, fidelity, diffident, confident"],
        ["greg", "flock, group", "gregarious, segregate, aggregate"],
        ["jur / jud", "law, judge", "jury, justice, prejudice, adjudicate"],
        ["leg / lex", "law, read", "legal, legislate, legacy, lexicon"],
        ["sol", "alone / sun", "solitude, solitary, solo / solar, solstice"],
        ["ver", "truth", "verify, veracity, verdict, veritable"],
        ["grad / gress", "step, go", "gradual, progress, digress, egress"],
    ],
)

prefix_table = md_table(
    ["Prefix", "Effect", "Examples"],
    [
        ["un-", "not / reverse", "unfair, unwell, undo, untie"],
        ["in- / im- / il- / ir-", "not", "inactive, impossible, illogical, irregular"],
        ["dis-", "opposite, apart", "disagree, disorder, disconnect, discredit"],
        ["non-", "not", "nonsense, nonstop, nonviolent"],
        ["mis-", "wrongly", "misjudge, misplace, misinterpret"],
        ["de-", "down, reverse", "decrease, deflate, decompose"],
        ["anti-", "against", "antisocial, antidote, antiseptic"],
        ["counter-", "against, opposite", "counteract, counterclaim"],
        ["-less", "without", "harmless, restless, speechless"],
        ["-ful / -ous", "full of (builds the positive)", "harmful, dangerous, famous"],
    ],
)

SUBTOPICS = [
    {
        "id": "syn-root-word-method",
        "title": "The root-word method: decode words you have never seen",
        "concept": f"""SSC vocabulary questions recycle the same few thousand words, but every year a couple of words are new to almost everyone. The root-word method converts such words from guesses into deductions: most English 'hard' words are built from Latin and Greek parts, and knowing 40 roots covers hundreds of exam words.

{root_table}

**How to deploy it in the exam.** When you meet an unknown word, split it:
- *MALEVOLENT* = male- (bad) + vol (wish) + -ent → 'wishing bad' → hostile. Even without recalling *vol*, 'male-' alone rules out friendly options.
- *CIRCUMSPECT* = circum- (around) + spect (look) → 'looking around' → cautious.
- *SOLILOQUY* = soli (alone) + loqu (speak) → 'speaking alone' → a monologue.

Prefixes and suffixes also reveal the part of speech even when meaning stays dark: *-ous/-ful* build adjectives (*dangerous*), *-tion/-ment* build nouns (*creation*), *-ise/-fy* build verbs (*simplify*). Knowing the class alone eliminates two of four options in synonym questions, because options usually mix classes.

**Build the habit:** whenever you learn a new word, spend ten seconds finding its root. The root then pays out on every relative of that word — learn *credulous* and *incredible, credible, creed, credential* all come free.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Split-then-eliminate",
                "body": "Chop the unknown word at its joins (bene-vol-ent), translate the parts you know, and eliminate options contradicting them. One confident root kills two options.",
                "example": {
                    "q": "BENEVOLENT means: cruel / kindly / generous-sized / talkative.",
                    "solution": "*Bene-* = good → the kind option. *Malevolent* (male- = bad) would be the antonym — options often plant it as a decoy.",
                },
            },
            {
                "title": "Family clustering",
                "body": "Learn words in root families, not alphabetical order: dict family (dictate, verdict, indomitable? no — edict, indict), loqu family (eloquent, loquacious). One sitting per family.",
            },
            {
                "title": "Positive/negative split",
                "body": "Roots carry emotional charge: bene-, eu-, am- are warm; mal-, dys-, phob-, mis- are cold. When stuck, mark the word's charge and choose an option of matching charge.",
            },
        ],
        "mistakes": [
            "Confusing look-alike roots: *malevolent* (bad) vs *magnanimous* (great-souled, generous).",
            "Trusting the first familiar half ('understand' contains 'stand' but is not about standing).",
            "Ignoring suffixes and losing the part-of-speech elimination.",
            "Learning alphabetical lists; root families stick, alphabet lists evaporate.",
        ],
    },
    {
        "id": "syn-elimination",
        "title": "Choosing the nearest meaning: elimination by class, degree, charge",
        "concept": f"""A synonym question asks for the word closest in meaning. Options are engineered around three axes — fix them in order:

**1. Part of speech.** Decide whether the given word is a noun, verb or adjective; options that are not the same class are out immediately. *AFFECT* (verb) cannot have 'affection' (noun) as a synonym even though it looks closest.

**2. Degree.** The nearest synonym matches the *intensity*. *WEARY* (very tired) is closer to *exhausted* than to *tired*; *FUTILE* (completely fruitless) is closer to *pointless* than to *difficult*. When two options both fit, take the one at the same temperature.

**3. Connotation and register.** A word's emotional colour must match. *NOTORIOUS* (famous for bad reasons) pairs with *infamous*, not with *celebrated*, even though both mean 'widely known'. *SLIM* and *skinny* both mean thin, but *slim* is approving and *skinny* is not — synonym options are chosen across this line.

**Practical routine for 20 seconds:**
1. Say the given word's meaning in your own simple words.
2. Translate each option into its own simple meaning.
3. Keep the option whose simple meaning overlaps most — overlap, not association. (*Cinema* associates with *film* but is not its synonym.)

**No sentence is given in SSC's format** — so context cannot rescue you. This is the one topic where the answer must be known, which is exactly why the word banks in this topic deserve daily 15-minute revision rather than a single reading.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Overlap test",
                "body": "The right synonym shares the core idea, not the neighbourhood. Ask 'can one replace the other in most sentences?' — if the sentence changes meaning, it is an associate, not a synonym.",
                "example": {
                    "q": "ELOQUENT: quiet / articulate / wealthy / careless.",
                    "solution": "*Eloquent* = speaking fluently and movingly = **articulate**. 'Quiet' is a near-antonym planted for sound-alike confusion.",
                },
            },
            {
                "title": "Charge matching",
                "body": "Label the given word + or − (notorious −, celebrated +) and pick the option of the same sign. Half of synonym options fall to charge alone.",
            },
            {
                "title": "Degree ruler",
                "body": "Place the word and both surviving options on an intensity line (mild → extreme). The option at the same mark is the answer.",
            },
        ],
        "mistakes": [
            "Choosing the option that merely sounds academic ('utilise' is fine, but 'effectuate' for 'do' is not SSC's style).",
            "Picking a word of the wrong part of speech that shares a root with the answer.",
            "Treating associates (cricket–sport) as synonyms.",
            "Forgetting the negative flip: 'famous for good deeds' ≠ notorious.",
        ],
    },
    {
        "id": "ant-prefix-flip",
        "title": "Antonyms: prefix flips and real opposites",
        "concept": f"""An antonym is a word opposite in meaning. Two skills cover SSC antonym questions.

**Skill 1 — the opposite, not the absence.** The correct antonym reverses the meaning; it does not merely differ. For *BRAVE* the antonym is *cowardly*, not *careful*. For *PRAISE* it is *criticise*, not *ignore* — ignoring is not the opposite of praising. Test each option by making a mini-sentence pair: 'He praised the plan / He criticised the plan' — clean contradiction.

**Skill 2 — build the flip.** Most adjectives flip with a prefix:

{prefix_table}

Prefix knowledge works in both directions: meet *irreversible*, know it means *reversible* negated; need the opposite of *conformity*, answer *nonconformity* or *defiance*. Watch the four-way *in- / im- / il- / ir-* spelling split — it follows the next sound (impossible, illegal, irregular) and decides spelling questions as a bonus.

**Antonym families to bank together:** agree/disagree, appear/disappear, increase/decrease, superior/inferior, permanent/temporary, expand/contract, vacant/occupied, sacred/profane, native/foreign, optimist/pessimist. SSC antonyms usually come straight from these families.

**Degree opposites:** gradable pairs sit on one line — hot↔cold, abundant↔scarce, shallow↔deep. Complementary pairs allow no middle — alive↔dead, guilty↔innocent. Both types appear; recognising the type prevents choosing a merely-different word.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Mini-sentence contradiction",
                "body": "Put the word and each candidate in the same short sentence ('The manager praised / criticised the report'). The option producing a genuine contradiction is the antonym.",
                "example": {
                    "q": "Antonym of CORDIAL: warm / polite / hostile / sincere.",
                    "solution": "'A cordial welcome' ↔ 'a hostile welcome' — real opposites. 'Polite' and 'sincere' can coexist with cordial, so neither contradicts it.",
                },
            },
            {
                "title": "Prefix flip check",
                "body": "Before scanning options, guess the flip yourself (conformity → nonconformity). If your guess is among the options, mark it — the options are built around the same flip.",
            },
            {
                "title": "Absence is not opposition",
                "body": "Kill options that merely lack the quality ('careful' for 'brave'). An antonym fights the word; it does not stand beside it.",
            },
        ],
        "mistakes": [
            "Choosing a word from a different part of speech ('arrive' as antonym of 'departure').",
            "Taking a near-neutral word ('polite') as the opposite of a warm word ('cordial').",
            "Missing spelled-out flips: *irrational*, *illogical*, *immature* all = 'not + word'.",
            "Opposing the wrong sense of a polysemous word ('fresh' = new vs unwilted; SSC picks the listed sense).",
        ],
    },
    {
        "id": "syn-ant-strategy",
        "title": "Exam strategy for vocabulary questions",
        "concept": f"""Tier 1 typically carries only 1 synonym + 1 antonym, and Tier 2 a similar sprinkle — low volume, but each is a 15-second mark with none of grammar's ambiguity. The strategy is therefore about *conversion rate*, not time.

**The conversion system:**
- **Daily 15 minutes** on the word bank in this topic: 10 words a day, meanings read aloud, each used in one sentence of your own. Production, not recognition, fixes recall.
- **Weekly mixed test:** 30 random words from the bank — synonym for half, antonym for half. Target 26+.
- **PYQ mining:** note every vocabulary word from past papers into a personal sheet; the same words return within 2–4 years.
- **Root of the day:** one root and its five relatives. Forty days completes the root table.

**In the exam:** vocabulary items should take 15–20 seconds each. If a word is unknown, split it for roots; if still dark, judge its charge (+/−) from the shape and pick a matching-charge option — this beats random guessing. There is no negative marking on one skipped item's worth of time saved, but never leave an SSC vocabulary item blank: an educated 50-50 is positive expected value, and pure instinct in English correlates surprisingly well with correctness.

**Do not sacrifice** grammar or RC time for vocabulary — the return per minute is far higher there. Vocabulary is a background process: daily small doses, permanent retention.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Two-pass vocabulary",
                "body": "Answer every certain vocabulary item in the first pass (15 s each); in the second pass, return to unknowns and root-split them with the remaining time.",
            },
            {
                "title": "Charge guess with options",
                "body": "Options reveal the axis: if options are (kind, cruel, wealthy, talkative), the axis is temperament — now guess the word's charge from its sound (mal-, dys- negative; bene-, eu- positive) and pick accordingly.",
            },
            {
                "title": "The 2-4 year echo",
                "body": "Words repeat across years. Solving the last 5 years' synonym/antonym questions is the single highest-yield vocabulary exercise — the bank above already encodes that history.",
            },
        ],
        "mistakes": [
            "Cramming 500 words the night before; retention needs spaced daily doses.",
            "Spending five minutes on one unknown word worth one mark.",
            "Leaving vocabulary blank instead of making an educated charge-based choice.",
            "Learning meanings without using the word in a sentence — recognition without recall.",
        ],
    },
]

PATTERNS = [
    {
        "pattern": "Direct synonym ('nearest in meaning')",
        "frequency": "very common",
        "howToSpot": "A capitalised word with four options, stem asks the closest meaning.",
        "approach": "Say the meaning in your own words, then match overlap, degree and charge; split unknown words by root.",
    },
    {
        "pattern": "Direct antonym ('opposite in meaning')",
        "frequency": "very common",
        "howToSpot": "Same format, stem asks the word most opposite.",
        "approach": "Build the mini-sentence contradiction for each surviving option; try the prefix flip first.",
    },
    {
        "pattern": "Synonym/antonym of a word inside a phrase",
        "frequency": "common",
        "howToSpot": "The word appears quoted from a short sentence or phrase ('gave up', 'broke out').",
        "approach": "Take the meaning from the phrase's usage first, then match options to that specific sense.",
    },
    {
        "pattern": "Vocabulary hidden inside cloze/fill-in items",
        "frequency": "occasional",
        "howToSpot": "A blank whose options are near-synonyms differing in register or degree.",
        "approach": "Use the sentence's tone to pick the matching register and degree — the synonym skill in context.",
    },
]

SE = [
    q("eng-sa-s01", "Select the word which is nearest in meaning to the given word.\n\nBENEVOLENT",
      ["compassionate", "malevolent", "miserly", "talkative"], 0,
      "*Benevolent* = bene (good) + vol (wishing) = wishing others well → **compassionate**. The root instantly disposes of *malevolent* (male- = bad), which is its antonym and a planted decoy; *miserly* is about money and *talkative* about speech.",
      "Split the word: bene- = good → pick the warm option; the male- option is the trap.",
      "easy", "syn-root-word-method", "root-word deduction", 30),
    q("eng-sa-s02", "Select the word which is nearest in meaning to the given word.\n\nFRUGAL",
      ["thrifty", "lavish", "hostile", "fertile"], 0,
      "*Frugal* means careful and sparing with money → **thrifty**. *Lavish* is its direct opposite (spending freely), and the other two are topic-shifters. Degree also confirms it: both 'frugal' and 'thrifty' sit at the same moderate mark of careful spending.",
      "Meaning in your words ('spends carefully') → match, then check that the strongest-sounding option is not the antonym.",
      "easy", "syn-elimination", "synonym match", 30),
    q("eng-sa-s03", "Select the word which is most opposite in meaning to the given word.\n\nCORDIAL",
      ["hostile", "polite", "sincere", "formal"], 0,
      "*Cordial* = warm and friendly. The genuine contradiction is **hostile**. *Polite* and *sincere* both coexist with cordiality (a cordial host is also polite), so neither opposes it; *formal* describes style, not warmth.",
      "Mini-sentence test: 'a cordial welcome' vs 'a ___ welcome' — only one option truly flips the meaning.",
      "easy", "ant-prefix-flip", "antonym selection", 30),
]

PRACTICE = [
    q("eng-sa-p01", "Select the word which is nearest in meaning to the given word.\n\nABUNDANT",
      ["plentiful", "scarce", "hidden", "tiny"], 0,
      "*Abundant* = existing in more than enough quantity → **plentiful**. *Scarce* is its antonym and is planted first-position bait; 'hidden' and 'tiny' shift to other dimensions altogether.",
      "Own words first ('more than enough') → match.",
      "easy", "syn-elimination", "synonym", 25),
    q("eng-sa-p02", "Select the word which is nearest in meaning to the given word.\n\nFUTILE",
      ["pointless", "useful", "fertile", "fragile"], 0,
      "*Futile* = producing no result → **pointless**. 'Useful' is the opposite pole; 'fertile' and 'fragile' share the -ile ending to punish shape-readers.",
      "Kill same-suffix decoys, keep the meaning match.",
      "easy", "syn-elimination", "synonym", 25),
    q("eng-sa-p03", "Select the word which is nearest in meaning to the given word.\n\nIMMINENT",
      ["impending", "delayed", "distant", "unnecessary"], 0,
      "*Imminent* = about to happen at any moment → **impending**. 'Delayed/distant' push the event away in time — the opposite direction.",
      "Time word: 'about to happen' → pick the option meaning 'on its way'.",
      "medium", "syn-elimination", "synonym", 25),
    q("eng-sa-p04", "Select the word which is nearest in meaning to the given word.\n\nNOTORIOUS",
      ["infamous", "renowned", "celebrated", "popular"], 0,
      "*Notorious* is famous **for bad reasons** → **infamous**. 'Renowned/celebrated/popular' all carry a positive charge — the charge mismatch is the entire test here.",
      "Charge matching: a negative word needs a negative option.",
      "medium", "syn-elimination", "synonym with connotation", 25),
    q("eng-sa-p05", "Select the word which is nearest in meaning to the given word.\n\nINDISPENSABLE",
      ["essential", "optional", "inferior", "temporary"], 0,
      "*Indispensable* = too necessary to do without → **essential**. 'Optional' flips the meaning; the others shift axes. Prefix logic agrees: in- (not) + dispensable (able to be let go).",
      "Prefix flip: not dispensable → must be kept → essential.",
      "easy", "syn-root-word-method", "prefix deduction", 25),
    q("eng-sa-p06", "Select the word which is nearest in meaning to the given word.\n\nMITIGATE",
      ["lessen", "aggravate", "prolong", "conceal"], 0,
      "*Mitigate* = soften the severity of something → **lessen**. *Aggravate* is the planted antonym; 'prolong' and 'conceal' change the action, not its intensity.",
      "Root family: mit/miss (send) — 'send away the severity' → lessen.",
      "medium", "syn-root-word-method", "root-word deduction", 25),
    q("eng-sa-p07", "Select the word which is nearest in meaning to the given word.\n\nVIGILANT",
      ["alert", "careless", "drowsy", "hostile"], 0,
      "*Vigilant* = carefully watchful for danger → **alert**. 'Careless' and 'drowsy' are opposite-directed; 'hostile' shifts to temperament.",
      "Meaning first ('watchful') → match.",
      "easy", "syn-elimination", "synonym", 25),
    q("eng-sa-p08", "Select the word which is nearest in meaning to the given word.\n\nSQUANDER",
      ["waste", "save", "multiply", "donate"], 0,
      "*Squander* = spend or use carelessly → **waste**. 'Save' is its opposite; 'donate' is controlled giving, not waste; 'multiply' changes the direction entirely.",
      "Own words ('careless spending') → match.",
      "easy", "syn-elimination", "synonym", 25),
    q("eng-sa-p09", "Select the word which is nearest in meaning to the given word.\n\nTENACIOUS",
      ["persistent", "fragile", "generous", "sluggish"], 0,
      "*Tenacious* = holding on firmly, refusing to quit → **persistent**. 'Fragile' and 'sluggish' are the planted opposite-temperament options.",
      "Charge + meaning: 'keeps gripping' → persistent.",
      "medium", "syn-root-word-method", "synonym", 25),
    q("eng-sa-p10", "Select the word which is nearest in meaning to the given word.\n\nLUCID",
      ["clear", "murky", "lengthy", "loud"], 0,
      "*Lucid* = easy to understand, transparent in expression → **clear**. 'Murky' is the opposite direction; 'lengthy/loud' are sound-shape decoys sharing the u-c sound.",
      "Expression words cluster: lucid–clear–coherent.",
      "easy", "syn-elimination", "synonym", 25),
    q("eng-sa-p11", "Select the word which is most opposite in meaning to the given word.\n\nHUMBLE",
      ["proud", "modest", "gentle", "polite"], 0,
      "*Humble* = modest about one's worth. The genuine opposite is **proud**. 'Modest' is a synonym planted as bait; 'gentle/polite' describe manner, not self-regard.",
      "Mini-sentence: 'a humble officer' vs 'a ___ officer' — only one option truly inverts it.",
      "easy", "ant-prefix-flip", "antonym", 25),
    q("eng-sa-p12", "Select the word which is most opposite in meaning to the given word.\n\nPUNCTUAL",
      ["late", "early", "regular", "prompt"], 0,
      "*Punctual* = exactly on time. Its opposite is **late**. 'Early' is not the opposite — arriving early is still not punctual in the strict sense, and SSC's key follows 'late'; 'prompt/regular' are near-synonyms.",
      "Time-axis test: on time ↔ behind time.",
      "easy", "ant-prefix-flip", "antonym", 25),
    q("eng-sa-p13", "Select the word which is most opposite in meaning to the given word.\n\nTRANSPARENT",
      ["opaque", "visible", "lucid", "brittle"], 0,
      "*Transparent* = letting light through; its standard opposite is **opaque**. 'Visible/lucid' move in a different dimension; 'brittle' is physical weakness.",
      "Physical sense here: see-through ↔ not see-through.",
      "easy", "ant-prefix-flip", "antonym", 25),
    q("eng-sa-p14", "Select the word which is most opposite in meaning to the given word.\n\nLIBERTY",
      ["bondage", "freedom", "licence", "leisure"], 0,
      "*Liberty* = freedom from restraint → opposite **bondage**. 'Freedom' is the synonym bait; 'licence' is unrestrained permission, not captivity; 'leisure' is free time.",
      "The synonym is always the first option to kill in antonym questions.",
      "easy", "ant-prefix-flip", "antonym", 25),
    q("eng-sa-p15", "Select the word which is most opposite in meaning to the given word.\n\nVIRTUE",
      ["vice", "value", "virtuosity", "vigour"], 0,
      "*Virtue* = moral goodness → its standard opposite is **vice** (moral fault). 'Value' drifts to worth, and the v-initial 'virtuosity/vigour' are shape decoys.",
      "Kill the v-initial decoys; pick the genuine moral opposite.",
      "medium", "ant-prefix-flip", "antonym", 25),
]

topic = {
    "id": "synonyms-antonyms",
    "sectionId": "english",
    "title": "Synonyms & Antonyms",
    "order": 6,
    "importance": "medium",
    "avgQuestions": {"tier1": 2, "tier2": 2},
    "summary": "One synonym and one antonym in a typical Tier 1 shift — two fast marks that reward a word bank, not guesswork. The root-word method decodes unknown words; degree and charge matching settle the rest. Below: 100 high-frequency synonyms and 60 antonyms with meanings, written for revision in daily 15-minute doses.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
