from common import q, write_topic, md_table

# ---------------------------------------------------------------- word banks
SUFFIX_ROWS = [
    # suffix family, sense, words (word – own-words meaning)
    ["-cide", "the act of killing", "Regicide – killing a king | Genocide – killing a whole race or community | Fratricide – killing one's own brother | Infanticide – killing an infant | Patricide – killing one's father | Suicide – killing oneself | Homicide – killing a human being | Sororicide – killing one's sister"],
    ["-phobia", "an abnormal fear of", "Hydrophobia – fear of water | Claustrophobia – fear of confined spaces | Acrophobia – fear of heights | Xenophobia – fear or dislike of foreigners | Nyctophobia – fear of darkness | Haematophobia – fear of blood | Triskaidekaphobia – fear of the number thirteen | Photophobia – abnormal sensitivity to light"],
    ["-ology", "the study of", "Anthropology – study of humankind's development | Ornithology – study of birds | Entomology – study of insects | Zoology – study of animals | Philology – study of languages and their history | Etymology – study of word origins | Geology – study of the earth's rocks | Psychology – study of the mind | Sociology – study of society | Seismology – study of earthquakes"],
    ["-graphy / -grapher", "writing/recording, or its practitioner", "Geography – study of the earth's surface | Demography – statistical study of populations | Calligraphy – the art of fine handwriting | Cartography – the making of maps | Hagiography – writing of saints' lives | Lexicographer – one who compiles dictionaries"],
    ["-cracy / -crat", "rule or power", "Democracy – government by the people | Autocracy – rule by one absolute ruler | Bureaucracy – government by paid officials | Aristocracy – rule by the noble class | Theocracy – rule in the name of God | Plutocracy – rule by the wealthy | Mobocracy – rule by the mob | Meritocracy – rule by ability and merit"],
    ["-phile / -phile words", "one who loves", "Bibliophile – a lover of books | Philatelist – a lover and collector of stamps | Anglophile – a lover of England or English ways | Philanthropist – one who loves humankind through charity"],
    ["-vore / -phagous", "feeding on", "Carnivorous – flesh-eating | Herbivorous – plant-eating | Insectivorous – insect-eating | Omnivorous – eating everything"],
    ["-gamy / -gamy words", "marriage patterns", "Monogamy – marriage to one person at a time | Polygamy – marriage to several spouses | Bigamy – marrying while legally married to another | Exogamy – marriage outside one's own group"],
]

PEOPLE_ROWS = [
    ["One who talks in sleep", "Somniloquist"],
    ["One who walks in sleep", "Somnambulist"],
    ["One who cannot read or write", "Illiterate"],
    ["One who knows many languages", "Polyglot"],
    ["One who lives shut off from the world", "Recluse (or Hermit)"],
    ["One who spends beyond his means to impress", "Extravagant (a spendthrift)"],
    ["One who is extremely careful with money", "Miser"],
    ["One who never drinks alcohol", "Teetotaller"],
    ["One who deals in cattle", "Drover"],
    ["One who mends shoes", "Cobbler"],
    ["One who cuts and sells men's clothing", "Tailor (a men's outfitter)"],
    ["One who sells medicines and prepares them", "Pharmacist (or Chemist)"],
    ["One who performs surgical operations", "Surgeon"],
    ["One who fits and repairs water pipes", "Plumber"],
    ["One who makes maps", "Cartographer"],
    ["One who compiles a dictionary", "Lexicographer"],
    ["One who writes the life history of another", "Biographer"],
    ["One who writes his own life story", "Autobiographer"],
    ["One who studies the human mind", "Psychologist"],
    ["One who treats eye disorders", "Oculist (or Optometrist)"],
    ["One who treats teeth", "Dentist"],
    ["One who foretells events by the stars", "Astrologer"],
    ["One who studies the stars scientifically", "Astronomer"],
    ["One who travels in space", "Astronaut (or Cosmonaut)"],
    ["One who is new to a profession", "Novice (or Tyro)"],
    ["One who has long experience of a field", "Veteran"],
    ["A person appointed to hear and decide a dispute", "Arbitrator"],
    ["One who deliberately damages property", "Vandal"],
    ["One who incites others to violence", "Firebrand"],
    ["A person who loves his country deeply", "Patriot"],
    ["One who betrays his country", "Traitor"],
    ["A person of great courage", "Valiant (a gallant)"],
    ["One unable to speak", "Dumb (speech-impaired)"],
    ["One unable to hear", "Deaf"],
    ["One who is present everywhere", "Omnipresent"],
    ["One who knows everything", "Omniscient"],
    ["One with unlimited power", "Omnipotent"],
    ["A woman whose husband has died", "Widow"],
    ["A man whose wife has died", "Widower"],
    ["One who has just been married", "Newly-wed (bride/groom)"],
    ["One who eats too much", "Glutton"],
    ["One who talks too much", "Garrulous (or Loquacious)"],
    ["One who speaks little", "Taciturn (or Reserved)"],
    ["One who believes everything easily", "Gullible"],
    ["One who doubts everything", "Sceptic"],
    ["One who hates humankind", "Misanthrope"],
    ["One who sacrifices life for a cause", "Martyr"],
    ["One who deserts his religion", "Apostate"],
    ["One who avoids company and merriment", "Introvert (a recluse)"],
    ["One who shows off his learning", "Pedant"],
]

PLACE_ROWS = [
    ["A place where bees are kept", "Apiary"],
    ["A place where birds are kept", "Aviary"],
    ["A place where fish are kept", "Aquarium"],
    ["A place where grains are stored", "Granary"],
    ["A place where horses are kept", "Stable"],
    ["A place where money is coined", "Mint"],
    ["A place where weapons are stored", "Armoury"],
    ["A place where dead bodies are kept", "Mortuary"],
    ["A place where orphans live", "Orphanage"],
    ["A place where historical objects are displayed", "Museum"],
    ["A place where aircraft are kept and repaired", "Hangar"],
    ["A place where novels, poems etc. are produced", "Publishing house (or Press)"],
    ["A place for public speaking and debate", "Podium (the speaker's platform)"],
    ["A burial place outside a church", "Cemetery"],
    ["A place where monks live together", "Monastery"],
    ["A place where nuns live together", "Convent"],
    ["A building where goods are made by hand or machine", "Factory (or Workshop)"],
    ["A place where animals are slaughtered", "Abattoir"],
]

GROUP_ROWS = [
    ["A group of lions", "Pride"],
    ["A group of wolves", "Pack"],
    ["A group of bees", "Swarm"],
    ["A group of sheep", "Flock"],
    ["A group of cattle", "Herd"],
    ["A group of fish", "School (or Shoal)"],
    ["A group of stars forming a pattern", "Constellation"],
    ["A group of islands", "Archipelago"],
    ["A group of skilled judges or experts", "Panel"],
    ["A group of worshippers", "Congregation"],
    ["A group of musicians playing together", "Orchestra (or Band)"],
    ["A group of soldiers", "Troop (or Platoon)"],
    ["A group of ships sailing together", "Fleet"],
    ["A group of hairs growing together", "Tuft"],
]

SPEECH_ROWS = [
    ["A speech delivered without preparation", "Extempore speech"],
    ["A speech delivered to oneself aloud", "Soliloquy"],
    ["A long speech by one speaker", "Monologue"],
    ["A conversation between two or more people", "Dialogue"],
    ["A speech at the end of a play", "Epilogue"],
    ["An introduction to a literary work", "Prologue"],
    ["Words of praise for the dead, written or spoken", "Eulogy"],
    ["An inscription on a tomb", "Epitaph"],
    ["A poem of mourning for the dead", "Elegy"],
    ["A short witty saying", "Epigram (or Aphorism)"],
    ["A mild word replacing a harsh one", "Euphemism"],
    ["A word opposite in sense to another", "Antonym"],
    ["A word similar in sense to another", "Synonym"],
    ["Speech that cannot be understood", "Jargon (or Gibberish)"],
    ["A formal proposal for discussion", "Motion (a resolution)"],
]

MISC_ROWS = [
    ["That which cannot be avoided", "Inevitable"],
    ["That which cannot be believed", "Incredible"],
    ["That which cannot be seen", "Invisible"],
    ["That which cannot be heard", "Inaudible"],
    ["That which cannot be conquered", "Invincible"],
    ["That which cannot be read", "Illegible"],
    ["That which cannot be explained", "Inexplicable"],
    ["That which cannot be corrected", "Incorrigible"],
    ["That which cannot be surpassed", "Unsurpassable (matchless)"],
    ["A medicine that counteracts poison", "Antidote"],
    ["A medicine that prevents infection by killing germs", "Antiseptic"],
    ["A substance that removes pain", "Anaesthetic (or Analgesic)"],
    ["A substance that speeds a chemical change", "Catalyst"],
    ["A remedy for all diseases", "Panacea"],
    ["The study of the origin of words", "Etymology"],
    ["A life history written by oneself", "Autobiography"],
    ["A story told in pictures", "Cartoon (a graphic narrative)"],
    ["An account of a journey", "Travelogue"],
    ["A list of books", "Catalogue (of books)"],
    ["A period of one hundred years", "Century"],
    ["A period of ten years", "Decade"],
    ["Occurring once a year", "Annual"],
    ["Occurring every two years", "Biennial"],
    ["Occurring twice a year", "Biannual (or Half-yearly)"],
    ["Occurring every day", "Diurnal (daily)"],
    ["Animals that live by night", "Nocturnal"],
    ["A word formed from the initials of other words", "Acronym"],
    ["The act of killing oneself", "Suicide"],
    ["A child born after the death of its father", "Posthumous child"],
    ["A place full of confusion and noise", "Pandemonium"],
    ["A doctor who delivers babies", "Obstetrician"],
    ["A government by the officials", "Bureaucracy"],
    ["A government by the rich", "Plutocracy"],
    ["A government by a king or queen", "Monarchy"],
    ["A government by the people through elected representatives", "Democracy"],
    ["A state without government or law", "Anarchy"],
    ["A system where one has absolute power", "Autocracy (or Dictatorship)"],
]

TOTAL = sum(len(r[2].split("|")) for r in SUFFIX_ROWS) + len(PEOPLE_ROWS) + len(PLACE_ROWS) + len(GROUP_ROWS) + len(SPEECH_ROWS) + len(MISC_ROWS)
assert TOTAL >= 120, f"OWS bank too small: {TOTAL}"

def multi_table(title, rows):
    head = f"**{title}**\n\n| One-word substitution | Meaning |\n|---|---|\n"
    return head + "\n".join(f"| **{w}** | {m} |" for w, m in rows)

suffix_block = "\n\n".join(
    f"**{fam} — {sense}**\n\n" + "\n".join("• " + w.strip() for w in cells.split("|"))
    for fam, sense, cells in SUFFIX_ROWS
)

SUBTOPICS = [
    {
        "id": "ows-suffix-families",
        "title": "Suffix families: decode the word by its ending",
        "concept": f"""One-word-substitution items rarely need a giant dictionary — the ending of the answer already tells you its *family*, and options are built one per family. Learn the suffix, and every member of the family is within reach.

{suffix_block}

**How the family method wins.** The stem 'murder of a king' invites four options, usually one -cide word, one -ology word, one -phobia word, one person-word. Knowing -cide = killing filters to the candidates, and then plain sense (rex = king → regicide) finishes. You never needed to memorise 'regicide' as a whole.

**Stack two families for rare words.** *Nyctophobia* = nycto (night) + phobia (fear) → fear of darkness. *Entomology* = entomo (insect) + logy (study). Rare SSC words are nearly always transparent stacks — the examiner picks words that reward this decoding.

**TheGreek/Latin counting prefixes** multiply coverage: mono (one), bi/duo (two), tri (three), quad (four), poly (many), pan (all), omni (all), semi (half), hemi (half), cent (hundred), milli (thousand). *Omnipotent/omniscient/omnipresent* are one prefix + one root each.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Family filter",
                "body": "Classify the stem first: is it a killing word, a fear, a study, a ruler-system, a person-type, a place? Reject every option from a different family before reading further.",
                "example": {
                    "q": "Murder of a king: homicide / regicide / ornithology / hydrophobia.",
                    "solution": "Killing stem → -cide family only → regicide (rex/reg = king). Homicide kills 'a human' generally — the specific stem wins.",
                },
            },
            {
                "title": "Root + suffix stack",
                "body": "Split rare answers: nycto-phobia, entomo-logy, carto-grapher. Two known parts beat one memorised word.",
            },
            {
                "title": "Counting-prefix drill",
                "body": "One evening per prefix set: mono-, bi-, tri-, poly-, pan-, omni-. Write each with three familiar words and the family stays for life.",
            },
        ],
        "mistakes": [
            "Confusing fratricide (brother) with patricide (father) — the family root carries the relation.",
            "Mixing -phobia (fear) with -phile (love) under exam pressure.",
            "Choosing astrology for a 'scientific study of stars' stem — astronomy is the science, astrology the belief system.",
            "Memorising isolated words instead of suffix families; the family is what survives pressure.",
        ],
    },
    {
        "id": "ows-people-words",
        "title": "One word for people: traits, trades and types",
        "concept": f"""The largest OWS category names a *person by what they do, feel or suffer*. Four sub-buckets organise the bank:

**1. Trades and professions** (learn with the tool or object of the trade): cobbler–shoes, plumber–pipes, cartographer–maps, lexicographer–dictionaries, obstetrician–childbirth, astronomer–stars (science), astrologer–stars (prediction).

**2. Character and conduct:** miser (hoards money), spendthrift (wastes it), teetotaller (never drinks), glutton (overeats), garrulous (overtalkative), taciturn (speaks little), gullible (believes easily), sceptic (doubts), novice (beginner), veteran (long-experienced).

**3. Loyalty and betrayal:** patriot/traitor, martyr (dies for a cause), apostate (abandons his religion), vandal (destroys property for pleasure), firebrand (stirs up unrest).

**4. Omnipotence set:** omnipotent (all-powerful), omniscient (all-knowing), omnipresent (present everywhere) — three words, one prefix, endlessly reused.

{multi_table("People bank (revise in five-word batches)", PEOPLE_ROWS)}

**Sensory and status pairs** are quick marks: dumb/speech-impaired, deaf, widow/widower, newly-wed. Note the gender-symmetric pairs — SSC loves the widow/widower switch under time pressure.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Object-anchor the trade",
                "body": "Never learn 'cobbler' alone — learn 'cobbler → shoes'. Stems name the object ('one who repairs shoes'), and your anchor matches it instantly.",
            },
            {
                "title": "Contrast pairs together",
                "body": "Store opposites and neighbours in one card: garrulous ↔ taciturn; miser ↔ spendthrift; novice ↔ veteran. The stem often points to one side of a pair.",
            },
            {
                "title": "Omni-triplet",
                "body": "One prefix (omni- = all), three endings: -potent (power), -scient (knowing), -present (place). One card covers all three SSC favourites.",
            },
        ],
        "mistakes": [
            "Swapping astrologer and astronomer — decide by 'scientific' or 'prediction' in the stem.",
            "Using 'mediator' where the stem demands an authorised decider — arbitrator decides, a mediator facilitates.",
            "Mixing spendthrift (wastes) with miser (hoards).",
            "Answering with an adjective when the stem's pattern expects the person-word.",
        ],
    },
    {
        "id": "ows-places-collections",
        "title": "One word for places and groups",
        "concept": f"""**Places.** The stem pattern is 'a place where X is kept/stored/done'. Anchor each place to its stored object:

{multi_table("Places bank", PLACE_ROWS)}

Watch the near-pairs: *apiary* (bees) vs *aviary* (birds) differ by one letter; *granary* (grain) vs *granite* (rock) — the exam plants exactly these neighbours as options.

**Groups (collective nouns).** The stem pattern is 'a group of X':

{multi_table("Groups bank", GROUP_ROWS)}

Collective nouns are pure memorisation but tiny in number — twenty cover nearly every paper. Note the precision points: lions come in a *pride* (not a herd), wolves in a *pack*, fish in a *school*, islands in an *archipelago* (not a chain of villages!).

**Choosing between group options** is a one-letter game under pressure: swarm (bees/insects), flock (sheep/birds), herd (cattle), pride (lions), pack (wolves/dogs). Ask which animal the stem names before touching the options.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Stored-object anchor",
                "body": "Places are defined by what is inside: bees→apiary, birds→aviary, grain→granary, coins→mint, corpses→mortuary. Match the object, not the sound.",
                "example": {
                    "q": "A place where bees are kept: aviary / apiary / aquarium / granary.",
                    "solution": "Bees → **apiary**. 'Aviary' differs by one letter — the deliberate neighbour-trap.",
                },
            },
            {
                "title": "Animal-first matching",
                "body": "For group stems, name the animal first, then recall its partner noun. Options scramble the five common pairs; the animal decides.",
            },
            {
                "title": "Near-pair cards",
                "body": "Make cards for one-letter pairs: apiary/aviary, granary/granite, monastery/convent (men/women). These are where marks leak.",
            },
        ],
        "mistakes": [
            "Choosing 'aviary' for bees (one-letter trap).",
            "Calling a lion group a 'herd' — lions take 'pride'.",
            "Confusing monastery (men) and convent (women).",
            "Using 'army' for a group of soldiers in the collective-noun sense when the stem wants 'troop/platoon'.",
        ],
    },
    {
        "id": "ows-government-science",
        "title": "Government systems, studies and word-craft",
        "concept": f"""**Government by whom?** The stem always names the ruler — match the ruler to the suffix -cracy or the classical root:

- by the **people** → democracy; by **officials** → bureaucracy; by the **rich** → plutocracy; by the **nobles** → aristocracy; by **God/clergy** → theocracy; by **one** → autocracy/dictatorship; by **the mob** → mobocracy (or ochlocracy); **no government** → anarchy; **rule by a king/queen** → monarchy.

**Studies and -graphy words:** geography (earth's surface), demography (populations), cartography (maps), calligraphy (beautiful writing), hagiography (saints' lives), etymology (word origins), philology (language history). The stem 'study of ___' names the object; the -ology/-graphy suffix names the family.

**Speech and writing words** form their own tight set — prologue/epilogue (start/end of a literary work), epitaph (tomb inscription), elegy (mourning poem), eulogy (words of praise for the dead), euphemism (mild substitute for a harsh word), soliloquy (talking to oneself), extempore (unprepared). Two overlapping pairs are the classic traps: *elegy vs eulogy* (both about the dead: mourning vs praise) and *epitaph vs epilogue* (tomb vs play's end).

**Time and frequency words:** century (100 years), decade (10), annual (yearly), biennial (every two years), biannual (twice a year), diurnal (daily/by day), nocturnal (by night). The biannual/biennial pair decides itself: -ennial counts years, -annual counts per year.

**That-which-cannot-be set:** inevitable, incredible, invisible, inaudible, illegible, incorrigible, inexplicable — all 'in-/il- + verb of perception or action'. The stem names the verb ('read' → illegible), so link each to its verb: believe→incredible, see→invisible, hear→inaudible, read→illegible, avoid→inevitable, correct→incorrigible.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Ruler-first matching",
                "body": "Underline WHO rules in the stem (people, rich, officials, one, God) and match to democracy/plutocracy/bureaucracy/autocracy/theocracy. The stem hands you the answer's head word.",
            },
            {
                "title": "Verb-link the negatives",
                "body": "Chain each 'cannot-be' word to its verb: read→illegible, believe→incredible, see→invisible. Stems always quote the verb.",
            },
            {
                "title": "Dead-word precision",
                "body": "About the dead: praise → eulogy, mourning-poem → elegy, tomb-writing → epitaph. Three cards, three certain marks.",
            },
        ],
        "mistakes": [
            "Choosing 'astrology' for a scientific study of stars.",
            "Swapping biannual (twice a year) and biennial (every two years).",
            "Using 'elegy' where praise of the dead is asked (that is 'eulogy').",
            "Confusing anarchy (no government) with autocracy (one ruler).",
        ],
    },
    {
        "id": "ows-strategy",
        "title": "Exam strategy for one-word substitution",
        "concept": f"""Tier 1 gives 1–2 OWS items; Tier 2 a few more. Like vocabulary, these are 15-second marks governed by recall — so the strategy is a *banking* strategy.

**Bank in categories, not lists.** One day: all -cide words. Next: fear words. Next: places. Categories cross-link (regicide joins reg- king with -cide killing), and cross-linked memories survive exam stress.

**Daily 10-minute rotation:** 10 new words + 20 old words read aloud. Weekend: 30-word mixed self-test. Every OWS word you meet in mocks goes into the personal sheet — repeats are frequent.

**In the exam:**
1. Read the stem and classify the family (killing? fear? study? person? place? group? government? cannot-be?).
2. Reject options from other families — usually two die here.
3. Match the stem's exact object (bees not birds; king not brother; praise not mourning).
4. If two options remain in-family, take the more specific one — OWS stems reward specificity (regicide beats homicide for 'murder of a king').

**Never leave it blank.** Even at 50-50 within a family, choose — no negative marking economics justify a skip on a recall item.

**Do not over-invest.** OWS is worth a couple of marks; the bank in this topic (150+ words) plus your mock sheet is sufficient. Beyond that, hours belong to RC and grammar.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Specificity rule",
                "body": "When two options fit the family, the stem's detail decides: 'brother' → fratricide, not homicide; 'twice a year' → biannual, not annual.",
            },
            {
                "title": "Stem-object underline",
                "body": "Underline the noun the word must carry (bees, grain, king, tomb). One underline removes half the options.",
            },
            {
                "title": "Mock-word ledger",
                "body": "Keep one running sheet titled 'OWS from mocks'. Most repeats come from your own past mistakes, not from unknown words.",
            },
        ],
        "mistakes": [
            "Reading the OWS bank once and expecting recall a month later.",
            "Choosing a same-family but wrong-object word under time pressure.",
            "Skipping the item when two options confuse, instead of applying specificity.",
            "Spending entire revision days on OWS while grammar and RC — the real marks — wait.",
        ],
    },
]

PATTERNS = [
    {
        "pattern": "Person by trait or trade",
        "frequency": "very common",
        "howToSpot": "Stem: 'One who ___' / 'A person who ___'.",
        "approach": "Anchor the object or trait (shoes, stars-scientific, overeats) and match; kill same-family neighbours by object.",
    },
    {
        "pattern": "Killing / fear / study words (suffix families)",
        "frequency": "common",
        "howToSpot": "Stems like 'murder of ___', 'fear of ___', 'study of ___'.",
        "approach": "Match suffix family first, then the root object (king→regicide, water→hydrophobia, insects→entomology).",
    },
    {
        "pattern": "Places and groups",
        "frequency": "common",
        "howToSpot": "Stems: 'A place where ___ is kept' / 'A group of ___'.",
        "approach": "Stored-object anchor for places; animal-first matching for groups; beware one-letter pairs (apiary/aviary).",
    },
    {
        "pattern": "Government / ruling systems",
        "frequency": "occasional",
        "howToSpot": "Stems: 'Government by ___' / 'Rule by ___' / 'A state without ___'.",
        "approach": "Underline the ruler noun and map to democracy, plutocracy, bureaucracy, autocracy, theocracy, monarchy, anarchy.",
    },
    {
        "pattern": "'Cannot be ___' words",
        "frequency": "occasional",
        "howToSpot": "Stems: 'That which cannot be seen/read/avoided…'.",
        "approach": "Link the verb to its negative word: see→invisible, read→illegible, believe→incredible, avoid→inevitable.",
    },
    {
        "pattern": "Speech / literary terms",
        "frequency": "occasional",
        "howToSpot": "Stems about speeches, tomb writings, mourning poems, unprepared talks.",
        "approach": "Keep the triple cards straight: praise→eulogy, mourning→elegy, tomb→epitaph; unprepared→extempore.",
    },
]

SE = [
    q("eng-ows-s01", "Select the option that can substitute the given group of words.\n\nMurder of a king",
      ["regicide", "homicide", "genocide", "infanticide"], 0,
      "The stem is a killing word (-cide family). Within the family, the object decides: rex/reg = king → **regicide**. *Homicide* is killing of a human in general, *genocide* of a race, *infanticide* of an infant — all real words planted as family-mates.",
      "Family first (-cide), then the root object (rex = king).",
      "easy", "ows-suffix-families", "suffix family method", 30),
    q("eng-ows-s02", "Select the option that can substitute the given group of words.\n\nA place where bees are kept",
      ["apiary", "aviary", "aquarium", "granary"], 0,
      "Place stems are anchored by the stored object: bees → **apiary**. *Aviary* is the one-letter neighbour (birds), *aquarium* holds fish, *granary* grain.",
      "Stored-object anchor: bees → apiary. Watch the aviary trap.",
      "easy", "ows-places-collections", "place-word anchor", 30),
    q("eng-ows-s03", "Select the option that can substitute the given group of words.\n\nA medicine that counteracts poison",
      ["antidote", "antibiotic", "antiseptic", "anaesthetic"], 0,
      "The anti- options form the family; the function decides: counteracts poison → **antidote**. *Antibiotic* kills bacteria, *antiseptic* prevents infection on wounds, *anaesthetic* removes sensation.",
      "Function matching within the anti- family.",
      "medium", "ows-strategy", "family + function", 30),
]

PRACTICE = [
    q("eng-ows-p01", "Select the option that can substitute the given group of words.\n\nOne who loves books",
      ["bibliophile", "philatelist", "lexicographer", "philanthropist"], 0,
      "Biblio = book + phile = lover → **bibliophile**. *Philatelist* collects stamps, *lexicographer* compiles dictionaries, *philanthropist* loves humankind through charity.",
      "Root stack: biblio (book) + phile (love).",
      "easy", "ows-suffix-families", "suffix family", 25),
    q("eng-ows-p02", "Select the option that can substitute the given group of words.\n\nA person who talks in his sleep",
      ["somniloquist", "somnambulist", "insomniac", "euphemist"], 0,
      "Somni = sleep + loqui = speak → **somniloquist**. *Somnambulist* walks in sleep (ambul = walk) — the classic sibling trap; *insomniac* cannot sleep at all.",
      "somni- (sleep) + verb root decides: walk vs speak.",
      "medium", "ows-suffix-families", "root stack", 25),
    q("eng-ows-p03", "Select the option that can substitute the given group of words.\n\nGovernment by the people through their elected representatives",
      ["democracy", "autocracy", "bureaucracy", "aristocracy"], 0,
      "Demos = people + cracy = rule → **democracy**. The stem names the ruler ('the people'); the other options name one ruler, officials, and nobles respectively.",
      "Ruler-first matching: people → democracy.",
      "easy", "ows-government-science", "government systems", 25),
    q("eng-ows-p04", "Select the option that can substitute the given group of words.\n\nOne who can use both hands with equal ease",
      ["ambidextrous", "ambivalent", "amphibious", "omnipresent"], 0,
      "Ambi = both + dextr = right hand/skill → **ambidextrous**. *Ambivalent* means having mixed feelings, *amphibious* means living on land and water — the ambi-/amphi- family tempts, the dextr root decides.",
      "ambi (both) + dextr (hand) → ambidextrous.",
      "easy", "ows-people-words", "person-word", 25),
    q("eng-ows-p05", "Select the option that can substitute the given group of words.\n\nA place where bees are kept",
      ["apiary", "aviary", "aquarium", "granary"], 0,
      "Bees are kept in an **apiary**; *aviary* (one letter away) keeps birds, *aquarium* fish, *granary* grain.",
      "Stored-object anchor; the aviary trap is deliberate.",
      "easy", "ows-places-collections", "place-word", 25),
    q("eng-ows-p06", "Select the option that can substitute the given group of words.\n\nThe act of killing one's own brother",
      ["fratricide", "patricide", "regicide", "genocide"], 0,
      "Frater = brother → **fratricide**. *Patricide* kills the father, *regicide* the king, *genocide* a whole community — all -cide family-mates separated by the relation root.",
      "Family root decides the relation: frater = brother.",
      "easy", "ows-suffix-families", "cide family", 25),
    q("eng-ows-p07", "Select the option that can substitute the given group of words.\n\nA speech delivered without any preparation",
      ["extempore", "epilogue", "monologue", "elocution"], 0,
      "Unprepared speech = **extempore**. *Epilogue* closes a play, *monologue* is a long one-person speech (prepared or not), *elocution* is the art of clear speaking.",
      "Speech-set matching: unprepared → extempore.",
      "easy", "ows-government-science", "speech words", 25),
    q("eng-ows-p08", "Select the option that can substitute the given group of words.\n\nOne who studies the stars and other heavenly bodies scientifically",
      ["astronomer", "astrologer", "cosmonaut", "geologist"], 0,
      "The word 'scientifically' fixes **astronomer** — the scientist of the sky. *Astrologer* predicts fates from star positions; *cosmonaut* travels; *geologist* studies the earth.",
      "Science vs prediction: astronomer vs astrologer — the stem's adjective decides.",
      "easy", "ows-people-words", "trade word", 25),
    q("eng-ows-p09", "Select the option that can substitute the given group of words.\n\nAn abnormal fear of enclosed spaces",
      ["claustrophobia", "hydrophobia", "acrophobia", "xenophobia"], 0,
      "Claustro = enclosed → **claustrophobia**. The family: hydro- water, acro- heights, xeno- foreigners — the stem names the feared object and the suffix names the family.",
      "phobia family; match the feared object.",
      "easy", "ows-suffix-families", "phobia family", 25),
    q("eng-ows-p10", "Select the option that can substitute the given group of words.\n\nWords inscribed on a tomb",
      ["epitaph", "epilogue", "elegy", "epigram"], 0,
      "Tomb inscription = **epitaph**. *Epilogue* ends a play, *elegy* mourns in verse, *epigram* is a witty short saying — the epi- family is planted wholesale.",
      "Dead-word triple: praise→eulogy, mourning→elegy, tomb→epitaph.",
      "medium", "ows-government-science", "literary word", 25),
    q("eng-ows-p11", "Select the option that can substitute the given group of words.\n\nA person appointed to hear both sides and settle a dispute",
      ["arbitrator", "agitator", "dictator", "philanthropist"], 0,
      "An **arbitrator** is the authorised settler of disputes. *Agitator* stirs trouble, *dictator* rules absolutely, *philanthropist* gives to charity — different families entirely.",
      "Stem verb 'settle' → the deciding person-word.",
      "medium", "ows-people-words", "person-word", 25),
    q("eng-ows-p12", "Select the option that can substitute the given group of words.\n\nA group of lions",
      ["pride", "herd", "swarm", "flock"], 0,
      "Lions live in a **pride**. *Herd* suits cattle, *swarm* bees, *flock* sheep or birds — the four collective options are swapped around in every paper.",
      "Animal first: lion → pride.",
      "easy", "ows-places-collections", "collective noun", 25),
    q("eng-ows-p13", "Select the option that can substitute the given group of words.\n\nOne who is present everywhere at the same time",
      ["omnipresent", "omnipotent", "omniscient", "omnivorous"], 0,
      "Omni = all + present → **omnipresent**. The omni-triplet: -potent (power), -scient (knowledge), -present (place) — the stem names the dimension.",
      "Omni- family: match the ending to the stem's dimension (place → present).",
      "easy", "ows-people-words", "omni-triplet", 25),
    q("eng-ows-p14", "Select the option that can substitute the given group of words.\n\nA medicine that counteracts the effects of poison",
      ["antidote", "antibiotic", "antiseptic", "anaesthetic"], 0,
      "Counteracts poison = **antidote**. *Antibiotic* attacks bacteria, *antiseptic* prevents wound infection, *anaesthetic* kills sensation during surgery.",
      "anti- family; function match: poison → antidote.",
      "easy", "ows-strategy", "medicine words", 25),
    q("eng-ows-p15", "Select the option that can substitute the given group of words.\n\nThat which cannot be avoided",
      ["inevitable", "invincible", "invisible", "incredible"], 0,
      "Cannot be avoided = **inevitable**. Link each option to its verb: conquer→invincible, see→invisible, believe→incredible. The stem's verb ('avoided') picks its partner.",
      "Verb-link: avoid → inevitable.",
      "easy", "ows-strategy", "cannot-be words", 25),
]

topic = {
    "id": "one-word-substitution",
    "sectionId": "english",
    "title": "One Word Substitution",
    "order": 7,
    "importance": "medium",
    "avgQuestions": {"tier1": 2, "tier2": 3},
    "summary": "A phrase such as 'murder of a king' must be replaced by one word (regicide). Options are built from suffix families —cide, -phobia, -logy, -cracy, -phile — so classifying the family first kills half the options. The bank below carries 150+ exam-frequency substitutions grouped for daily revision.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
