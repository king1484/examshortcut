from common import q, write_topic, md_table

# ---------------------------------------------------------------- idiom banks
ANIMAL_ROWS = [
    ["Let the cat out of the bag", "reveal a secret carelessly"],
    ["Rain cats and dogs", "rain very heavily"],
    ["Smell a rat", "suspect that something dishonest is going on"],
    ["Take the bull by the horns", "confront a difficulty directly and boldly"],
    ["Hold your horses", "stop and be patient for a moment"],
    ["Kill two birds with one stone", "achieve two aims with a single action"],
    ["The lion's share", "the biggest portion of anything"],
    ["A wild-goose chase", "a pointless search for something unattainable"],
    ["Put the cart before the horse", "do things in the wrong order"],
    ["Crocodile tears", "sorrow that is pretended, not felt"],
    ["Count your chickens before they hatch", "depend on gains that are not yet certain"],
    ["A dark horse", "a competitor whose real ability stays hidden until he wins"],
    ["A cash cow", "a business or product that yields steady easy profit"],
    ["A fish out of water", "a person uncomfortable in strange surroundings"],
    ["Fish in troubled waters", "profit from other people's difficulties"],
    ["Bell the cat", "take the first great risk for everyone's benefit"],
]

BODY_ROWS = [
    ["Turn a deaf ear", "refuse to listen deliberately"],
    ["Pull someone's leg", "tease or joke with someone playfully"],
    ["Keep an eye on", "watch something carefully"],
    ["See eye to eye", "agree fully with someone"],
    ["Pay through the nose", "pay far more than a fair price"],
    ["Cost an arm and a leg", "be extremely expensive"],
    ["Give the cold shoulder", "treat someone with deliberate unfriendliness"],
    ["Bite the dust", "be defeated or fail completely"],
    ["Bury the hatchet", "end a quarrel and make peace"],
    ["Get cold feet", "lose courage at the last moment"],
    ["Stick your neck out", "risk criticism by speaking or acting boldly"],
    ["Wash your hands of", "refuse any further responsibility for a matter"],
    ["Heart in your mouth", "extremely nervous or frightened"],
    ["Lend a hand", "give help"],
    ["Keep at arm's length", "avoid becoming friendly or intimate with"],
    ["Have your hands full", "be extremely busy with work"],
    ["Follow in someone's footsteps", "carry on the work or path of an elder"],
    ["Put your foot down", "take a firm, unyielding stand"],
]

COLOUR_ROWS = [
    ["A white elephant", "a possession that is costly to keep but useless"],
    ["A black sheep", "the disgraced or disreputable member of a group"],
    ["Once in a blue moon", "very rarely, almost never"],
    ["A red-letter day", "an important day worth remembering"],
    ["See red", "become suddenly very angry"],
    ["Red tape", "excessive official rules and delays"],
    ["Out of the blue", "completely unexpectedly"],
    ["A grey area", "a matter unclear in law or morality"],
    ["Green with envy", "strongly jealous"],
    ["Born with a silver spoon in one's mouth", "born into a rich family"],
]

FOOD_ROWS = [
    ["A piece of cake", "a task needing almost no effort"],
    ["A hard nut to crack", "a stubborn problem or a difficult person"],
    ["The salt of the earth", "a thoroughly good and dependable person"],
    ["Butter someone up", "flatter someone for one's own gain"],
    ["Food for thought", "something that deserves serious thinking"],
    ["Cry over spilt milk", "waste regret on what cannot be undone"],
    ["In a pickle", "in an awkward difficulty"],
    ["The apple of one's eye", "a person cherished above everyone else"],
    ["Spill the beans", "divulge a secret"],
    ["A hot potato", "a touchy issue everyone avoids handling"],
    ["Add fuel to the fire", "make an angry situation worse"],
    ["Make a mountain of a molehill", "blow a trivial matter out of proportion"],
    ["Carry coals to Newcastle", "supply something to a place that already has plenty"],
    ["Set the Thames on fire", "achieve something sensational (usually said in the negative)"],
]

SITUATION_ROWS = [
    ["A blessing in disguise", "a misfortune that turns out to be beneficial"],
    ["Burn the midnight oil", "work or study late into the night"],
    ["At the drop of a hat", "instantly and without any excuse or delay"],
    ["In hot water", "in serious trouble"],
    ["Make both ends meet", "live within a limited income"],
    ["A bolt from the blue", "a sudden, completely unexpected shock"],
    ["Leave no stone unturned", "try every possible means"],
    ["Move heaven and earth", "make the greatest possible effort"],
    ["On cloud nine", "extremely happy"],
    ["Under the weather", "slightly ill"],
    ["Turn over a new leaf", "begin a better way of living"],
    ["A storm in a teacup", "furious argument about a trivial thing"],
    ["Carry the day", "win, prevail"],
    ["Play second fiddle", "accept a subordinate position"],
    ["Rest on one's laurels", "be complacent with past achievements"],
    ["Behind bars", "in prison"],
    ["In the pipeline", "being planned or prepared"],
    ["By leaps and bounds", "very rapidly"],
    ["On the spur of the moment", "suddenly, without earlier planning"],
    ["In cold blood", "deliberately and without pity"],
    ["Off and on", "irregularly, now and then"],
    ["Out of the frying pan into the fire", "from a bad situation into a worse one"],
    ["Cut a long story short", "come directly to the point"],
    ["Against all odds", "despite every difficulty and discouragement"],
    ["Face the music", "accept the unpleasant consequences of one's acts"],
    ["Throw in the towel", "admit defeat and give up"],
    ["Get the sack", "be dismissed from employment"],
    ["Pass the buck", "shift blame or duty to someone else"],
    ["Steal a march on", "gain an advantage over someone secretly"],
    ["Turn the tables", "reverse one's position against an opponent"],
    ["Take to one's heels", "run away quickly"],
    ["Feather one's nest", "enrich oneself by misusing one's position"],
    ["End in smoke", "come to nothing after much effort"],
    ["Play havoc with", "cause great disorder or damage to"],
    ["Bear the palm", "win the first prize or highest honour"],
]

PEOPLE_ROWS = [
    ["An Achilles' heel", "one weak point in an otherwise strong person or system"],
    ["A man of straw", "a person of no substance or influence"],
    ["A man of letters", "a learned writer or scholar"],
    ["A man of his word", "one who always keeps his promises"],
    ["A fair-weather friend", "a friend who disappears in your bad days"],
    ["A snake in the grass", "a treacherous enemy hiding as a friend"],
    ["A wolf in sheep's clothing", "a dangerous person disguised as harmless"],
    ["Odd man out", "the one member unlike all the others"],
    ["A cog in the machine", "an insignificant worker in a vast system"],
    ["A tower of strength", "a person who gives firm support in crisis"],
    ["A jack of all trades", "one who does many kinds of work, master of none"],
    ["Have a finger in every pie", "meddle in everyone's business"],
    ["Wear your heart on your sleeve", "display your feelings openly"],
    ["Keep your chin up", "stay brave and cheerful in hardship"],
    ["Keep the wolf from the door", "earn just enough to avoid hunger"],
    ["Keep body and soul together", "barely manage to survive"],
    ["Take someone to task", "scold or criticise someone severely"],
    ["Be all ears", "listen with complete eagerness"],
    ["Be in two minds", "be unable to decide between options"],
    ["Sit on the fence", "avoid taking sides in a dispute"],
    ["Keep your fingers crossed", "hope anxiously that things will go well"],
    ["Break the ice", "start conversation among strangers"],
    ["Hit the nail on the head", "describe a situation with exact correctness"],
    ["A foregone conclusion", "a result obvious in advance"],
    ["At daggers drawn", "in open, bitter hostility"],
    ["In the doldrums", "low in spirits or activity"],
    ["Not mince matters", "speak plainly without softening words"],
    ["Take to task", "reprimand for a fault"],
]

TOTAL_IDIOMS = len(ANIMAL_ROWS) + len(BODY_ROWS) + len(COLOUR_ROWS) + len(FOOD_ROWS) + len(SITUATION_ROWS) + len(PEOPLE_ROWS)
assert TOTAL_IDIOMS >= 120, f"idiom bank too small: {TOTAL_IDIOMS}"

def bank_table(title, rows):
    return f"**{title}**\n\n| Idiom | Meaning |\n|---|---|\n" + "\n".join(
        f"| *{i}* | {m} |" for i, m in rows)

ANIMAL_T = bank_table("Animals, birds and fish", ANIMAL_ROWS)
BODY_T = bank_table("Body-part idioms", BODY_ROWS)
COLOUR_T = bank_table("Colour idioms", COLOUR_ROWS)
FOOD_T = bank_table("Food idioms", FOOD_ROWS)

SUBTOPICS = [
    {
        "id": "idiom-literal-trap",
        "title": "Why literal meaning is always wrong — and how to find the picture",
        "concept": f"""An idiom is a frozen picture: the words describe an *image*, and the exam question is what that image stands for. Every wrong option in SSC idiom items is built the same way — one or two options restate the literal words ('reveal a secret' vs 'buy a cat and free it'), one option is a related-but-different figurative meaning, and one is the true meaning.

**The method:**
1. **Ban the literal.** Any option that can be pictured physically ('open the bag') is a decoy — eliminate on sight. In nearly every SSC item, at least one option is purely literal.
2. **Find the picture.** Ask what the image shows: letting a cat escape from a bag → something hidden escapes → *revealing a secret*. Crocodiles were believed to weep while eating prey → fake tears → *pretended sorrow*.
3. **Tone check.** Note whether the idiom is positive, negative or comic. 'Smell a rat' is suspicion (negative but not violent) — 'to be certain of theft' overshoots; 'to suspect trickery' sits at the right temperature.
4. **Plug back.** Substitute the option into a mini-sentence: 'He let the cat out of the bag about the surprise party' → 'He ___ about the surprise party'. Only 'revealed the secret' completes it naturally.

{ANIMAL_T}

**Degree and verdict precision** decide close pairs: 'bite the dust' = be *defeated* (a verdict), not 'be wounded'; 'end in smoke' = come to *nothing*, not 'cause pollution' (the literal smoke!). When two options both look figurative, ask which one states the *outcome* the idiom actually records.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Literal-first elimination",
                "body": "Scan the options and kill every one you could photograph. The remaining two or three are the true contest.",
                "example": {
                    "q": "To let the cat out of the bag: to buy a pet / to reveal a secret carelessly / to free animals / to make a noise.",
                    "solution": "Three options are photographable → dead. What survives: reveal a secret — and the picture agrees (the hidden thing escaped).",
                },
            },
            {
                "title": "Picture-to-abstract translation",
                "body": "Name the picture's key action in the abstract: escape→reveal, cold water→trouble, midnight oil→late work, blue (sky)→unexpected.",
            },
            {
                "title": "Plug-back sentence",
                "body": "Fit each surviving option into your own sentence using the idiom. The one that sounds like ordinary English is the key.",
            },
        ],
        "mistakes": [
            "Choosing the literal option because it matches two of the idiom's words.",
            "Picking a neighbouring figurative meaning ('turn a deaf ear' → 'to hear badly' instead of 'refuse to listen').",
            "Overreading intensity ('in hot water' = in trouble, not in mortal danger).",
            "Confusing paired idioms: 'spill the beans' (secret) vs 'cry over spilt milk' (useless regret).",
        ],
    },
    {
        "id": "idiom-animal-body",
        "title": "Animal and body-part idioms",
        "concept": f"""SSC's favourite idiom reservoirs are animals and body parts. The animal usually supplies the *character* and the body part supplies the *function* — decode along those lines.

{BODY_T}

**Animal logic:** the bull (charge head-on), rat (sneaky wrongdoing), cat (hidden, escapes), horse (speed/impulse — hold your horses), wolf (hunger/predation — keep the wolf from the door), sheep (harmless disguise), lion (share/size), goose (futility — wild-goose chase), crocodile (fake tears).

**Body-part logic:** ear → listening (turn a deaf ear), eye → watching/agreement (see eye to eye), leg → playful force (pull one's leg), shoulder → reception (cold shoulder), neck → risk (stick your neck out), feet → nerve (get cold feet), heart → courage/nervousness, hand → help (lend a hand), foot → firmness (put your foot down).

Most animal/body idioms are *transparent under this logic* — even a half-remembered idiom yields to the picture. The handful of opaque ones (bite the dust, cold shoulder, crocodile tears) deserve one flash card each.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Animal-character match",
                "body": "Recall each animal's stock character (rat = cheat, wolf = hunger, bull = force). The idiom's meaning is the animal's character plus the verb.",
            },
            {
                "title": "Body-function match",
                "body": "Ear = listen, eye = watch, foot = stand firm, hand = help/work. Map the named part to its function before reading options.",
            },
            {
                "title": "Opaque-idiom cards",
                "body": "Ten idioms have lost their logic (bite the dust, cold shoulder, red tape). Card them separately — they are the only real memory load.",
            },
        ],
        "mistakes": [
            "Reading 'pull someone's leg' as causing injury — the tone is playful.",
            "Taking 'cold shoulder' as an illness option planted in papers ('feel cold').",
            "Mixing 'smell a rat' (suspect) with 'a rat race' (fierce competition).",
            "Forgetting 'heart in your mouth' means fear, not surprise.",
        ],
    },
    {
        "id": "idiom-colour-food",
        "title": "Colour and food idioms",
        "concept": f"""**Colours** carry fixed associations — the colour predicts the meaning family:

{COLOUR_T}

Colour logic: white → useless-grand (white elephant), black → disgrace (black sheep), blue → unexpected (once in a blue moon, out of the blue, bolt from the blue), red → anger/officialdom (see red, red tape, red-letter day is the exception — a day marked in red ink, hence memorable), green → envy, grey → unclear, silver → inherited wealth.

**Food idioms** pair an eating image with an abstract judgement: easy (piece of cake), stubborn (hard nut), flattery (butter up), thought (food for thought), cherished (apple of the eye), secret (spill the beans), exaggeration (mountain of a molehill), useless supply-shifting (coals to Newcastle), trivial storm (storm in a teacup), controversy (hot potato).

{FOOD_T}

**Close pairs inside these banks:** 'spill the beans' (reveal a secret) vs 'cry over spilt milk' (vain regret); 'a white elephant' (costly, useless) vs 'the lion's share' (the biggest part); 'red tape' (official delay) vs 'red-letter day' (memorable day). The exam draws options from inside these pairs — learn each pair as a unit.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Colour association",
                "body": "Blue = surprise, red = anger or bureaucracy, green = envy, white = useless grandness, black = disgrace. Half the colour idioms decode from this alone.",
            },
            {
                "title": "Food-judgement fit",
                "body": "Food idioms are judgements in disguise: cake→easy, nut→stubborn, pickle→difficulty, potato→controversy. Match the judgement, not the ingredient.",
            },
            {
                "title": "Pair-learning",
                "body": "Learn confusable idioms in pairs on one card: beans/milk, elephant/lion's share, red tape/red-letter day. The option list usually contains both members.",
            },
        ],
        "mistakes": [
            "Reading 'red-letter day' negatively because 'red' suggests danger.",
            "Taking 'hot potato' to mean a tasty offer instead of a touchy issue.",
            "Mixing 'in a pickle' (awkward spot) with 'in a nutshell' (in brief).",
            "Confusing 'born with a silver spoon' (rich) with 'every cloud has a silver lining' (hope in trouble).",
        ],
    },
    {
        "id": "idiom-situations-people",
        "title": "Idioms for situations and types of people",
        "concept": f"""The biggest blocks describe *situations* (trouble, effort, suddenness) and *people* (types, loyalties, weaknesses).

{bank_table("Situations and events", SITUATION_ROWS)}

{bank_table("People and character", PEOPLE_ROWS)}

**Situation families:** trouble (in hot water, in a pickle, in the doldrums), effort (move heaven and earth, leave no stone unturned, burn the midnight oil), suddenness (a bolt from the blue, out of the blue, at the drop of a hat, on the spur of the moment, off and on is the exception — irregularity), defeat and quitting (throw in the towel, bite the dust, get the sack, end in smoke), improvement (turn over a new leaf, bury the hatchet), blame-shifting (pass the buck, steal a march, turn the tables).

**People families:** the weak (man of straw, cog in the machine), the treacherous (snake in the grass, wolf in sheep's clothing, fair-weather friend), the reliable (man of his word, tower of strength, salt of the earth), the mixed-ability (jack of all trades), the famous weak-spot (Achilles' heel).

Cluster-learning pays double here: when the stem says 'a sudden and unexpected event', the whole suddenness family surfaces, and the options — usually drawn one per family — separate instantly.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Family surfacing",
                "body": "Classify the stem's demand: sudden? trouble? effort? defeat? person-type? Recall the family's four members; the right one is usually among the options, and the wrong options are from *other* families.",
            },
            {
                "title": "Allusion anchors",
                "body": "A few idioms hide a story: Achilles' heel (the hero's one weak spot), bell the cat (the mouse that dared), pass the buck (shifting the deal-marker). One-line stories fix meanings permanently.",
            },
            {
                "title": "Outcome test",
                "body": "For action idioms, ask what changes at the end: throw in the towel → the fight stops (give up); turn the tables → positions reverse; face the music → consequences arrive.",
            },
        ],
        "mistakes": [
            "Reading 'steal a march' as theft — it means to gain a secret advantage.",
            "Taking 'pass the buck' as giving money; the buck is the marker of responsibility.",
            "Confusing 'in the doldrums' (depressed/inactive) with 'in the dumps' — same sense, but options plant 'a boring place'.",
            "Reading 'against all odds' as 'very unfair odds' instead of 'despite difficulties'.",
        ],
    },
    {
        "id": "idiom-strategy",
        "title": "Exam strategy: banking 300 idioms in 30 days",
        "concept": f"""Tier 1 carries exactly one idiom item in most shifts; Tier 2 occasionally uses idioms inside cloze and RC. The topic is pure bank-and-recall, and a 300-idiom working bank covers years of papers.

**The 30-day plan:**
- **Days 1–10:** 10 new idioms a day from the banks in this topic, each used in one sentence of your own. Sentence-production is what survives exam pressure; recognition alone melts.
- **Days 11–20:** 10 new + 15 old daily. Group by family (animals, colours, situations) — clusters recall better than alphabetical lists.
- **Days 21–30:** 10 new + 25 old + one 20-item mixed self-test. Anything failed twice goes onto a separate 'bleeder list' of 15–20 items that gets one extra revision weekly.

**In the exam:** 20 seconds. Kill literal options, translate the picture, plug back. If unknown, judge polarity (does it sound positive?) and pick the same-polarity option — instinct on familiar-sounding idioms is right far more than chance.

**Total time budget for the whole topic: about 5 hours spread over a month** — the best time-to-mark ratio in the English section, provided sentences are produced and the bleeder list exists. Do not chase exhaustive dictionaries; the SSC idiom pool is surprisingly small and heavily recycled.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Sentence production",
                "body": "For every idiom, speak a sentence about your own life ('I burned the midnight oil before my SSC mock'). Personal sentences are recalled under pressure; list-readings are not.",
            },
            {
                "title": "Family-first revision",
                "body": "Revise by bank (animals → body → colours → food → situations → people). Each bank is one mental room; in the exam you 'enter the room' and the members appear.",
            },
            {
                "title": "Bleeder list",
                "body": "Fail an idiom twice in self-tests? It goes to a 15-item list revised weekly. Most permanent marks come from this list, not from new words.",
            },
        ],
        "mistakes": [
            "Learning idioms as word-pairs without ever producing a sentence.",
            "Revising alphabetically; families and pairs are the recall units.",
            "Chasing rare literary idioms — SSC recycles a small common pool.",
            "Ignoring tone: options often mix one positive and three negative meanings, or vice versa.",
        ],
    },
]

PATTERNS = [
    {
        "pattern": "Meaning of a common idiom",
        "frequency": "very common",
        "howToSpot": "A single idiom quoted; options include at least one literal restatement.",
        "approach": "Kill literal options, translate the picture, plug the survivor back into a sentence.",
    },
    {
        "pattern": "Idiom inside a sentence",
        "frequency": "common",
        "howToSpot": "The idiom appears inside a short sentence; you pick its meaning or a substitute phrase.",
        "approach": "Use the sentence's subject and tone to confirm the figurative meaning before matching options.",
    },
    {
        "pattern": "Fill in the idiom",
        "frequency": "occasional",
        "howToSpot": "A sentence with a blank where an idiom belongs; options are four idioms.",
        "approach": "Judge the sentence's demand (suddenness, trouble, effort) and pick the idiom from that family.",
    },
    {
        "pattern": "Opposite of an idiom's sense",
        "frequency": "occasional",
        "howToSpot": "Stem asks for the phrase most nearly opposite in meaning.",
        "approach": "Fix the idiom's meaning first, then build its true contradiction — 'made peace' ↔ 'declared war', not 'felt sad'.",
    },
]

SE = [
    q("eng-id-s01", "Select the most appropriate meaning of the given idiom.\n\nTo smell a rat",
      ["to suspect that something wrong is happening", "to suffer from a foul smell", "to chase away rodents", "to detect a dead animal"], 0,
      "The picture: a rat hiding somewhere, betrayed by its smell — something hidden and dishonest. Hence **to suspect wrongdoing**. The literal options (foul smell, rodents, dead animal) die on the photograph test, and each can be photographed.",
      "Kill what you can photograph; translate the picture: hidden rat = hidden wrongdoing.",
      "easy", "idiom-literal-trap", "literal-elimination", 30),
    q("eng-id-s02", "Select the most appropriate meaning of the given idiom.\n\nA blessing in disguise",
      ["a misfortune that turns out to be beneficial", "a gift bought secretly", "a religious disguise", "a blessing said in a low voice"], 0,
      "The picture: a blessing that arrived wearing the *disguise* of trouble. The abstract meaning: an apparent misfortune that proves beneficial. Options about gifts, costumes or whispers are literal translations of 'disguise' and die at once.",
      "Split the idiom: blessing = good outcome, in disguise = looked bad first.",
      "easy", "idiom-colour-food", "picture translation", 30),
    q("eng-id-s03", "Select the most appropriate meaning of the given idiom.\n\nTo pass the buck",
      ["to shift responsibility to someone else", "to pay money quickly", "to win a bet", "to move a heavy object"], 0,
      "From card-playing: the 'buck' (a marker) showed whose turn to deal; passing it handed the duty to another. Hence **shifting one's responsibility to someone else**. Money and betting options trade on the word 'pass' — both are decoys built on the surface vocabulary.",
      "Allusion anchor: the buck = the marker of responsibility; passing it = escaping duty.",
      "medium", "idiom-situations-people", "allusion idiom", 35),
]

PRACTICE = [
    q("eng-id-p01", "Select the most appropriate meaning of the given idiom.\n\nOnce in a blue moon",
      ["very rarely", "every month", "on a full-moon night", "during the rainy season"], 0,
      "A blue moon (a second full moon in a month) hardly ever occurs → **very rarely**. 'Every month' and 'on a full-moon night' are literal moon options — photographable decoys.",
      "Rare astronomical event → rare occurrence.",
      "easy", "idiom-colour-food", "colour idiom", 25),
    q("eng-id-p02", "Select the most appropriate meaning of the given idiom.\n\nTo burn the midnight oil",
      ["to work or study late into the night", "to waste fuel", "to light lamps for a festival", "to set something on fire at night"], 0,
      "Before electricity, lamps burned oil; burning it at midnight meant **working late**. The image survives as an idiom for late effort.",
      "Picture: oil lamp at midnight → late-night work.",
      "easy", "idiom-situations-people", "effort idiom", 25),
    q("eng-id-p03", "Select the most appropriate meaning of the given idiom.\n\nA white elephant",
      ["a costly but useless possession", "a rare and valuable gift", "a sacred animal", "an expensive racehorse"], 0,
      "Kings once gifted white elephants whose upkeep ruined the receiver — grand to own, ruinous to keep → **a costly, useless possession**. The sacred/rare options take the colour literally.",
      "Upkeep test: does keeping it drain you? That is the white elephant.",
      "medium", "idiom-colour-food", "colour idiom", 30),
    q("eng-id-p04", "Select the most appropriate meaning of the given idiom.\n\nTo beat about the bush",
      ["to avoid coming to the point", "to search carefully in a forest", "to criticise someone mildly", "to make a garden"], 0,
      "Hunters beat *around* bushes to flush game without striking it — skirting the centre. Hence **avoiding the main topic**.",
      "Picture: striking the edges, never the centre → dodging the point.",
      "easy", "idiom-animal-body", "action idiom", 25),
    q("eng-id-p05", "Select the most appropriate meaning of the given idiom.\n\nTo bite the bullet",
      ["to endure a painful situation bravely", "to chew tobacco", "to fire a gun angrily", "to swallow a pill"], 0,
      "Soldiers once bit a bullet during surgery without anaesthesia — **to bear pain with courage**. 'To give up easily' inverts the meaning; the rest are literal.",
      "Old surgery picture → brave endurance.",
      "medium", "idiom-situations-people", "courage idiom", 30),
    q("eng-id-p06", "Select the most appropriate meaning of the given idiom.\n\nTo turn a deaf ear",
      ["to ignore deliberately", "to suffer hearing loss", "to listen carefully", "to shout at someone"], 0,
      "The ear that 'turns away' refuses to hear — **deliberate ignoring**, not physical deafness ('hearing loss' is the literal decoy).",
      "Body-function logic: ear = listening; turned away = refusing to listen.",
      "easy", "idiom-animal-body", "body idiom", 25),
    q("eng-id-p07", "Select the most appropriate meaning of the given idiom.\n\nIn hot water",
      ["in serious trouble", "enjoying a bath", "feeling very angry", "in a warm climate"], 0,
      "Trouble scalds; being 'in hot water' = **in difficulty or disfavour**. Bath, anger and weather options are temperature-literal.",
      "Water temperature = trouble scale: hot water = trouble.",
      "easy", "idiom-situations-people", "trouble idiom", 25),
    q("eng-id-p08", "Select the most appropriate meaning of the given idiom.\n\nTo make both ends meet",
      ["to live within one's income", "to join two ropes", "to finish a task", "to reconcile two friends"], 0,
      "One's two 'ends' — income and expense — must touch: **to manage on a limited income**. Ropes, tasks and friendships are literal decoys for 'ends'.",
      "Ends = income and expense; making them meet = balancing a budget.",
      "easy", "idiom-situations-people", "money idiom", 25),
    q("eng-id-p09", "Select the most appropriate meaning of the given idiom.\n\nAchilles' heel",
      ["a weak point despite overall strength", "a foot injury", "a Greek custom", "a swift runner"], 0,
      "The hero Achilles was invulnerable except where his mother held him — his heel. Hence **the one weakness in a strong person or system**.",
      "Allusion anchor: the great hero's single vulnerable spot.",
      "easy", "idiom-situations-people", "allusion idiom", 25),
    q("eng-id-p10", "Select the most appropriate meaning of the given idiom.\n\nTo spill the beans",
      ["to reveal a secret", "to waste food", "to cook carelessly", "to lose a game"], 0,
      "An upturned jar of beans cannot be taken back — the secret is out → **reveal a secret**. Note the sibling idiom 'cry over spilt milk' (vain regret); papers plant one as the other's decoy.",
      "Irreversible spill → an undoable revelation.",
      "easy", "idiom-colour-food", "food idiom", 25),
    q("eng-id-p11", "Select the most appropriate meaning of the given idiom.\n\nTo pull someone's leg",
      ["to tease someone playfully", "to trip someone", "to beg for help", "to drag a heavy load"], 0,
      "A playful tug at the leg = **to joke at someone's expense**. The tone is friendly — 'to cheat' and 'to injure' overshoot the idiom's mildness.",
      "Tone check: the act is a joke, not an attack.",
      "easy", "idiom-animal-body", "body idiom", 25),
    q("eng-id-p12", "Select the most appropriate meaning of the given idiom.\n\nAt the drop of a hat",
      ["instantly, without hesitation", "with great reluctance", "after much planning", "only on special occasions"], 0,
      "A dropped hat was the instant signal to begin a fight or race → **immediately, without needing any reason**. 'Reluctance' and 'planning' contradict the idiom's whole point.",
      "Signal picture: hat drops, action starts.",
      "easy", "idiom-situations-people", "suddenness idiom", 25),
    q("eng-id-p13", "Select the most appropriate meaning of the given idiom.\n\nTo keep the wolf from the door",
      ["to avoid starvation and poverty", "to guard a house at night", "to keep animals outside", "to shut the door in anger"], 0,
      "The wolf at the door is hunger; keeping it out means **earning barely enough to live**. House-guarding and pet options are literal.",
      "Wolf = hunger; keeping it away = basic survival income.",
      "medium", "idiom-animal-body", "animal idiom", 30),
    q("eng-id-p14", "Select the most appropriate meaning of the given idiom.\n\nTo smell a rat",
      ["to suspect some deceit", "to dislike pets", "to find a hiding place", "to feel hungry"], 0,
      "A hidden rat betrayed by its smell = a hidden deceit betrayed by signs → **to suspect trickery**. 'To detect a thief red-handed' overshoots — smelling a rat is suspicion, not proof.",
      "Degree check: suspicion, not certainty.",
      "easy", "idiom-literal-trap", "animal idiom", 25),
    q("eng-id-p15", "Select the most appropriate meaning of the given idiom.\n\nTo hit the nail on the head",
      ["to state exactly the right thing", "to hurt oneself while working", "to complete a job quickly", "to strike someone hard"], 0,
      "One clean, accurate blow — a description or answer perfectly on target → **to speak with exact correctness**.",
      "Accuracy picture: the blow lands precisely.",
      "easy", "idiom-animal-body", "precision idiom", 25),
]

topic = {
    "id": "idioms-phrases",
    "sectionId": "english",
    "title": "Idioms & Phrases",
    "order": 8,
    "importance": "medium",
    "avgQuestions": {"tier1": 1, "tier2": 2},
    "summary": "One idiom per shift, four meanings, and the literal option always planted as bait. Idioms are frozen pictures — animals, body parts, colours, food — and every bank below decodes them into families so that even a half-remembered idiom yields its meaning. 130+ idioms with meanings written for daily 15-minute banking.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
