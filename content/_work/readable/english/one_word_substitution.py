"""Readable rewrite: English > One Word Substitution (5 subtopics). Idempotent. Run with Python312."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rd_common import pat, mis, trick, sub, apply  # noqa: E402

SUBS = {}

# ---------------------------------------------------------------- 1. suffix families
SUBS["ows-suffix-families"] = sub(
    concept=("In one-word substitution you get a phrase and pick the single word for it. "
             "Many answer words are two parts: a root for the object and a suffix for the family. "
             "Learn the suffix and you can build the meaning of words you have not seen."),
    notes=r"""
### The question and the two-part idea
The question gives a phrase, such as *the killing of a king*. You pick one word: **regicide**.

Most such words have two parts.
- The **root** names the object: reg = king.
- The **suffix** names the family: -cide = killing.

Join them and you get the meaning without memorising the whole word.

### Main families
| Suffix | Meaning | Examples |
|---|---|---|
| -cide | killing | regicide (king), fratricide (brother), patricide (father), infanticide (infant), genocide (a whole race), homicide (a human), suicide (oneself) |
| -phobia | abnormal fear | hydrophobia (water), acrophobia (heights), claustrophobia (closed spaces), xenophobia (foreigners), nyctophobia (darkness) |
| -ology | study of | ornithology (birds), entomology (insects), seismology (earthquakes), etymology (word origins), anthropology (humankind) |
| -graphy | writing, drawing | cartography (making maps), calligraphy (fine handwriting), demography (populations) |
| -phile | lover of | bibliophile (books), philatelist (stamps), anglophile (England) |
| -vorous | eating | herbivorous (plants), carnivorous (flesh), omnivorous (everything), insectivorous (insects) |
| -gamy | marriage | monogamy (one spouse), polygamy (several spouses), bigamy (a second marriage while still married), exogamy (outside one's group) |

> **Tip:** Learn one family a day. Say each word with its object: "reg, king, regicide".

### Roots that name the object
- **reg** king, **frater** brother, **pater** father, **geno** race.
- **hydro** water, **acro** height, **xeno** foreign, **nycto** night.
- **ornitho** bird, **entomo** insect, **seismo** earthquake, **etymo** word origin.
- **biblio** book, **herb** plant, **carn** flesh.

> **Example:** Nyctophobia = nycto (night) + phobia (fear). It means fear of darkness.

### Counting prefixes
These prefixes open many words.
| Prefix | Meaning |
|---|---|
| mono | one |
| bi, duo | two |
| tri | three |
| poly | many |
| pan, omni | all |
| semi, hemi | half |
| cent | hundred |
| milli | thousand |

Omnipotent (all-powerful), omniscient (all-knowing) and omnipresent (present everywhere) are one prefix plus one root each.

### How the options are built
A question usually has one right word and three from the same or a nearby family.
- For *study of insects*, the options may all be -ology words. The **root** decides: entomology.
- For *fear of heights*, the options may come from different families. The **suffix** decides: -phobia.

Check both parts every time.

### Look-alike pairs
- entomology (insects) and etymology (word origins).
- patricide (father), fratricide (brother), matricide (mother).
- philatelist (stamps) and numismatist (coins).
- -phobia (fear) and -phile (love).
- astronomy (science of stars) and astrology (predicting from stars).

> **Watch:** Look-alike words differ by one letter group. Read the whole word.
""",
    patterns=[
        pat("osf-p1", "Killing words (-cide)", "very common",
            "The phrase says 'killing of' or 'murder of' and names a victim: king, brother, father, mother, infant, race.",
            ["Spot the word 'killing' or 'murder'.", "Note who is killed.", "Match the root: reg = king, frater = brother, pater = father.",
             "Add -cide and pick that option."],
            "-cide is the killing suffix. The root names the victim.",
            "The murder of a king is called: (a) homicide (b) regicide (c) suicide (d) genocide",
            ["Killing means -cide.", "The victim is a king, so the root is reg.", "Reg + cide is regicide."], "(b) regicide"),
        pat("osf-p2", "Fear words (-phobia)", "very common",
            "The phrase says 'an abnormal fear of'.",
            ["Spot 'fear'.", "Note the thing feared.", "Match its root: hydro = water, acro = height, xeno = foreign, nycto = night.",
             "Pick the -phobia word with that root."],
            "-phobia is the fear suffix. The root names the thing feared.",
            "An abnormal fear of heights: (a) claustrophobia (b) hydrophobia (c) acrophobia (d) xenophobia",
            ["Fear means -phobia.", "Heights is acro.", "Acrophobia."], "(c) acrophobia"),
        pat("osf-p3", "Study words (-ology)", "very common",
            "The phrase says 'the study of' or 'the science of'.",
            ["Spot 'study'.", "Note the thing studied.", "Match its root: ornitho = birds, entomo = insects, seismo = earthquakes.",
             "Check the look-alikes before you mark."],
            "-ology is the study suffix. The root gives the subject.",
            "The study of insects: (a) entomology (b) etymology (c) ornithology (d) seismology",
            ["Study means -ology.", "Insects is entomo.", "Etymology looks alike but means word origins."], "(a) entomology"),
        pat("osf-p4", "Lover, eater and marriage words", "common",
            "The phrase says 'a lover or collector of', 'feeding on', or describes a marriage practice.",
            ["Spot 'love', 'feeding' or 'marriage'.", "Match the suffix: -phile, -vorous or -gamy.",
             "Match the root for the object.", "Pick the option with both parts."],
            "Each suffix names a family, and the root names the object.",
            "One who loves books: (a) bibliophile (b) philatelist (c) anglophile (d) philanthropist",
            ["Love means -phile.", "Books is biblio.", "Bibliophile. A philatelist loves stamps."], "(a) bibliophile"),
        pat("osf-p5", "Counting-prefix words", "occasional",
            "The phrase says 'all', 'many' or 'one' before the idea (all-powerful, all-knowing).",
            ["Find the counting idea: all, many, one, half.", "Match the prefix: omni, poly, mono, semi.",
             "Add the root for the rest of the meaning."],
            "One prefix and one root build a whole family of words.",
            "One who has power to do everything: (a) omniscient (b) omnipotent (c) omnipresent (d) omnivorous",
            ["All means omni.", "Power is potent.", "Omnipotent. Omniscient is all-knowing."], "(b) omnipotent"),
    ],
    mistakes=[
        mis("Memorising each word alone.", "Learn the suffix family and the root. Build the word from two parts."),
        mis("Marking entomology for 'word origins'.", "Entomology is insects. Etymology is word origins."),
        mis("Mixing patricide, fratricide and matricide.", "Father is pater, brother is frater, mother is mater. Check the victim."),
        mis("Confusing -phobia (fear) with -phile (love).", "Phobia means fear. Phile means love."),
        mis("Marking a word after reading only its ending.", "Check the root as well. Options often share the same suffix."),
    ],
    revision=[
        "-cide = killing, -phobia = fear, -ology = study, -graphy = writing, -phile = lover, -vorous = eating, -gamy = marriage.",
        "Roots: reg king, frater brother, pater father, hydro water, acro height, xeno foreign, nycto night.",
        "Omni = all: omnipotent, omniscient, omnipresent.",
        "Family first, then root.",
        "Look-alikes: entomology/etymology, patricide/fratricide, philatelist/numismatist.",
    ],
    tricks=[
        trick("Family first, root second",
              "Read the phrase and name the family (killing, fear, study). Then match the root. Two steps remove most options.",
              "The study of earthquakes: (a) seismology (b) geology (c) zoology (d) etymology",
              ["Study means -ology.", "Earthquakes is seismo.", "Seismology."], "(a) seismology"),
        trick("Stack two families",
              "Rare words are often two parts joined. Nycto + phobia is fear of darkness. Entomo + logy is study of insects."),
        trick("Make look-alike cards",
              "Write each look-alike pair on one card with the meaning of each word. Revise the cards every week."),
    ],
)

# ---------------------------------------------------------------- 2. people words
SUBS["ows-people-words"] = sub(
    concept=("Most one-word-substitution items start with 'One who' or 'A person who'. "
             "They name a person by a job, a habit, a feeling or a situation. "
             "Sort them into four boxes and watch out for the partner word planted as a trap."),
    notes=r"""
### The biggest group
The commonest stem begins with **One who ...** or **A person who ...**. Learn these words in four boxes.

### Box 1: jobs
Learn each job with the thing it works on.
| Word | Job |
|---|---|
| cartographer | makes maps |
| lexicographer | compiles dictionaries |
| cobbler | mends shoes |
| plumber | fits and repairs water pipes |
| surgeon | performs operations |
| dentist | treats teeth |
| oculist | treats eye disorders |
| pharmacist | prepares and sells medicines |
| astronomer | studies stars scientifically |
| astrologer | foretells events from stars |

> **Watch:** The word *scientifically* points to the astronomer. The word *foretells* points to the astrologer.

### Box 2: habits and character
| Word | Meaning |
|---|---|
| teetotaller | never drinks alcohol |
| glutton | eats too much |
| miser | hoards money |
| spendthrift | wastes money |
| gullible | believes everything easily |
| sceptic | doubts everything |
| garrulous | talks too much |
| taciturn | speaks very little |
| misanthrope | hates mankind |
| pedant | shows off his learning |

### Box 3: pairs and opposites
The examiner often puts the partner word in the options.
- widow (woman whose husband has died) and widower (man whose wife has died).
- novice (beginner) and veteran (long experience).
- miser and spendthrift.
- patriot (loves his country) and traitor (betrays it).

> **Tip:** Read the gender or direction word in the stem before you choose.

### Box 4: words built from roots
| Word | Parts | Meaning |
|---|---|---|
| polyglot | poly (many) + glot (tongue) | knows many languages |
| somnambulist | somn (sleep) + ambul (walk) | walks in sleep |
| somniloquist | somn (sleep) + loqu (speak) | talks in sleep |
| omniscient | omni (all) + scient (knowing) | knows everything |
| omnipotent | omni (all) + potent (power) | has unlimited power |
| omnipresent | omni (all) + present | present everywhere |
| philanthropist | phil (love) + anthrop (man) | loves mankind |

### More words to bank
- illiterate: cannot read or write.
- recluse: lives shut off from the world.
- martyr: gives his life for a cause.
- apostate: deserts his religion.
- vandal: deliberately damages property.
- arbitrator: hears and settles a dispute.
- biographer writes another person's life. An autobiographer writes his own.

### How to answer
1. Underline the key detail: the object, the habit or the gender.
2. Put the phrase in its box.
3. Choose the option that matches the detail exactly. Reject the partner word and the look-alike.
""",
    patterns=[
        pat("opw-p1", "Person by job", "very common",
            "The phrase says 'one who makes, mends, treats or studies' and names an object or a field.",
            ["Underline the object or field.", "Recall the job word that goes with it.",
             "Check the look-alike job words.", "Mark the exact match."],
            "Each job word is tied to one object.",
            "One who makes maps: (a) cartographer (b) lexicographer (c) calligrapher (d) geographer",
            ["The object is maps.", "Cartography is map-making.", "Lexicographers compile dictionaries."], "(a) cartographer"),
        pat("opw-p2", "Person by habit or character", "very common",
            "The phrase describes a habit or nature: never drinks, eats too much, believes anything.",
            ["Underline the habit.", "Match it to a character word.", "Reject the opposite character word."],
            "Habit words come in pairs, so the stem detail must be exact.",
            "One who never drinks alcohol: (a) glutton (b) teetotaller (c) miser (d) sceptic",
            ["The habit is not drinking alcohol.", "A glutton eats too much. A miser hoards money.", "A teetotaller never drinks."],
            "(b) teetotaller"),
        pat("opw-p3", "Partner-word trap", "common",
            "The options hold both members of a pair: widow and widower, miser and spendthrift, novice and veteran.",
            ["Find the pair in the options.", "Read the gender or direction word in the stem.",
             "Pick the member that fits."],
            "The wrong member of the pair is planted to catch quick readers.",
            "A man whose wife has died: (a) widow (b) widower (c) bachelor (d) veteran",
            ["Note the word man.", "A widow is a woman.", "A widower is a man."], "(b) widower"),
        pat("opw-p4", "Root-built person words", "common",
            "The answer is built from Greek or Latin parts: poly, mis, phil, omni, somn.",
            ["Match a root to a word in the phrase.", "Translate each part.", "Choose the option that joins the parts."],
            "Two known parts give the whole meaning.",
            "One who knows many languages: (a) polymath (b) polyglot (c) pedant (d) novice",
            ["Many is poly.", "Language is glot, tongue.", "Polyglot. A polymath knows many subjects."], "(b) polyglot"),
        pat("opw-p5", "Look-alike person words", "common",
            "Two options are one letter apart or share a field (astronomer and astrologer).",
            ["Underline the detail word: scientifically or foretells.", "Match it to the exact member.",
             "Reject the look-alike."],
            "The look-alike is the most common wrong option.",
            "One who studies the stars scientifically: (a) astrologer (b) astronomer (c) cartographer (d) psychologist",
            ["The word scientifically decides.", "An astrologer foretells events.", "An astronomer studies stars as a science."],
            "(b) astronomer"),
    ],
    mistakes=[
        mis("Choosing astrologer for 'studies the stars scientifically'.", "Scientific study is astronomer. Foretelling is astrologer."),
        mis("Ignoring the gender word (widow for a man).", "Read man or woman in the stem before you choose."),
        mis("Confusing miser and spendthrift.", "Miser hoards money. Spendthrift wastes it."),
        mis("Confusing polyglot and polymath.", "Polyglot knows many languages. Polymath knows many subjects."),
        mis("Learning words without the object.", "Learn each job word with the thing it works on."),
    ],
    revision=[
        "Jobs: cartographer maps, lexicographer dictionary, cobbler shoes, plumber pipes.",
        "Habits: miser/spendthrift, garrulous/taciturn, gullible/sceptic.",
        "Pairs: widow/widower, novice/veteran, patriot/traitor.",
        "Roots: poly many, mis hate, phil love, omni all, somn sleep.",
        "Astronomer studies stars. Astrologer foretells from stars.",
    ],
    tricks=[
        trick("Object first",
              "Underline the object or habit in the stem before you read the options. It names the family at once.",
              "One who cannot read or write: (a) illiterate (b) recluse (c) veteran (d) sceptic",
              ["The key detail is cannot read or write.", "Illiterate matches.", "A recluse lives away from people."],
              "(a) illiterate"),
        trick("Learn words in pairs",
              "Take each word with its partner. Widow goes with widower. Miser goes with spendthrift. The pair is one memory item."),
        trick("Speak the parts",
              "Say the parts aloud: somn, ambul, ist. Hearing the parts locks the meaning."),
    ],
)

# ---------------------------------------------------------------- 3. places and groups
SUBS["ows-places-collections"] = sub(
    concept=("Two question shapes are pure matching. 'A place where X is kept or done' needs a place word. "
             "'A group of X' needs a collective noun. Find the key noun in the phrase and recall its partner."),
    notes=r"""
### Two simple shapes
1. **A place where ___ is kept or done.** The answer is a place word.
2. **A group of ___.** The answer is a collective noun.

Both are matching. The phrase names the thing, and you name its place or its group.

### Places
Match the place to what is kept or done there.
| Place | What happens there |
|---|---|
| apiary | bees are kept |
| aviary | birds are kept |
| aquarium | fish are kept |
| granary | grain is stored |
| stable | horses are kept |
| kennel | dogs are kept |
| armoury | weapons are stored |
| mint | coins are made |
| hangar | aircraft are kept and repaired |
| mortuary | dead bodies are kept |
| cemetery | the dead are buried |
| abattoir | animals are killed for meat |
| monastery | monks live |
| convent | nuns live |
| orphanage | orphans live |
| museum | historical objects are shown |
| observatory | stars are studied through telescopes |

> **Example:** A place where coins are made is a **mint**. A treasury keeps money but does not make coins.

### Look-alike places
- **apiary** (bees) and **aviary** (birds). Aviary goes with aviation and flying birds.
- **monastery** (monks, men) and **convent** (nuns, women).
- **mortuary** (bodies kept) and **cemetery** (bodies buried).
- **granary** (grain) and granite (a rock). Options often plant such neighbours.

> **Watch:** The hangar for aircraft is different from a hanger for clothes. Check the spelling.

### Groups
Collective nouns are memory work, but only a few come up.
| A group of | Word |
|---|---|
| lions | pride |
| wolves, dogs | pack |
| cattle | herd |
| sheep, birds | flock |
| bees | swarm |
| fish | school, shoal |
| ships | fleet |
| islands | archipelago |
| stars in a pattern | constellation |
| worshippers | congregation |
| musicians | orchestra, band |
| experts or judges | panel |
| soldiers | troop |

> **Rule:** Ask which animal or thing the phrase names before you look at the options. The animal decides the word.

### Worked examples
- *A place where grain is stored.* The object is grain, so the word is **granary**.
- *A group of sheep.* Sheep move in a **flock**. Cattle move in a herd.
- *A place where aircraft are kept and repaired.* The word is **hangar**.

Each one takes about ten seconds once the pairs are in memory.

### How to answer
1. Find the key noun: bees, coins, wolves, islands.
2. Recall its partner place or group word.
3. Check the look-alike before you mark.

Say the pairs aloud: bees and apiary, coins and mint, wolves and pack, islands and archipelago. The exam asks for the partner, never a definition.
""",
    patterns=[
        pat("opc-p1", "Place where something is kept or made", "very common",
            "The phrase says 'a place where ___ are kept, stored or made'.",
            ["Underline the object kept or made.", "Recall the place word tied to it.", "Check the one-letter look-alike."],
            "Each place word has a single stored object.",
            "A place where bees are kept: (a) aviary (b) apiary (c) aquarium (d) granary",
            ["The object is bees.", "Aviary is for birds and aquarium for fish.", "Apiary is for bees."], "(b) apiary"),
        pat("opc-p2", "Place named by the people in it", "common",
            "The phrase says 'a place where monks live', 'where orphans live' or 'where animals are killed'.",
            ["Underline who or what is there.", "Match: monks monastery, nuns convent, orphans orphanage.",
             "Reject the partner place."],
            "The people or the activity name the place.",
            "A place where nuns live: (a) monastery (b) convent (c) orphanage (d) mortuary",
            ["The people are nuns.", "Monks live in a monastery.", "Nuns live in a convent."], "(b) convent"),
        pat("opc-p3", "Collective noun for animals", "very common",
            "The phrase says 'a group of lions, wolves, cattle, bees or sheep'.",
            ["Underline the animal.", "Recall its group word.", "Reject words that belong to other animals."],
            "The animal decides the word.",
            "A group of lions: (a) pack (b) herd (c) pride (d) swarm",
            ["The animal is the lion.", "Pack is for wolves, herd for cattle, swarm for bees.", "Lions form a pride."], "(c) pride"),
        pat("opc-p4", "Collective noun for things or people", "common",
            "The phrase says 'a group of islands, stars, ships or worshippers'.",
            ["Underline the thing grouped.", "Recall its group word.", "Check the options for a near word."],
            "Each non-animal group also has one fixed word.",
            "A group of islands: (a) archipelago (b) constellation (c) fleet (d) panel",
            ["The things are islands.", "Constellation is for stars and fleet for ships.", "Islands form an archipelago."], "(a) archipelago"),
        pat("opc-p5", "Look-alike place pairs", "common",
            "Two options are nearly the same place: mortuary and cemetery, monastery and convent, apiary and aviary.",
            ["Find the pair in the options.", "Read the detail word: kept or buried, men or women.", "Pick the member that fits."],
            "The look-alike is the planted wrong option.",
            "A place where dead bodies are kept before burial: (a) cemetery (b) mortuary (c) abattoir (d) hangar",
            ["Kept, not buried.", "A cemetery is where bodies are buried.", "A mortuary is where they are kept."], "(b) mortuary"),
    ],
    mistakes=[
        mis("Mixing apiary and aviary.", "Api goes with bees. Avi goes with aviation and birds."),
        mis("Choosing cemetery for a place where bodies are kept.", "Kept is mortuary. Buried is cemetery."),
        mis("Swapping monastery and convent.", "Monks live in a monastery. Nuns live in a convent."),
        mis("Using the wrong group word (herd for lions).", "Name the animal first. Lions form a pride."),
        mis("Learning places without the object.", "Learn each place with what it holds: coins mint, aircraft hangar."),
    ],
    revision=[
        "Places: apiary bees, aviary birds, granary grain, mint coins, hangar aircraft, mortuary bodies, abattoir slaughter.",
        "Monastery is for monks. Convent is for nuns.",
        "Groups: pride lions, pack wolves, herd cattle, flock sheep, swarm bees.",
        "Fleet ships, archipelago islands, constellation stars.",
        "Look-alikes: apiary/aviary, mortuary/cemetery, monastery/convent.",
    ],
    tricks=[
        trick("Animal decides the group",
              "Name the animal in the phrase first. Then recall its one group word.",
              "A group of wolves: (a) pack (b) pride (c) herd (d) flock",
              ["The animal is the wolf.", "Pride is lions, herd is cattle, flock is sheep.", "Wolves form a pack."], "(a) pack"),
        trick("Sound hooks",
              "Link each look-alike to a sound: api sounds like ape-bee, avi is in aviation. Hooks beat plain rote."),
        trick("Twenty and twenty",
              "About twenty place words and twenty group words cover nearly every paper. Learn them in one sitting and revise once a week."),
    ],
)

# ---------------------------------------------------------------- 4. government / science
SUBS["ows-government-science"] = sub(
    concept=("This group holds four word sets: forms of government, speech and writing, time and frequency, "
             "and 'that which cannot be ...' words. In each set the stem holds one key detail. "
             "Match the detail, then check the look-alike pair."),
    notes=r"""
### Government words: who rules?
Every government word answers one question: **who holds the power?** Find the ruler in the stem and match it.
| Ruled by | Word |
|---|---|
| the people | democracy |
| one person with total power | autocracy |
| a king or queen | monarchy |
| the rich | plutocracy |
| nobles, the upper class | aristocracy |
| a small group | oligarchy |
| paid officials | bureaucracy |
| religious leaders, in God's name | theocracy |
| the mob | mobocracy |
| ability and merit | meritocracy |
| nobody, no government | anarchy |

> **Example:** Government by the wealthy. Pluto means wealth. The word is **plutocracy**.

### Speech and writing words
These come in confusing pairs.
| Word | Meaning |
|---|---|
| elegy | a poem of mourning for the dead |
| eulogy | words of praise, often after death |
| epitaph | words written on a tomb |
| soliloquy | speaking one's thoughts aloud when alone |
| extempore | spoken without preparation |
| prologue | the opening of a play or book |
| epilogue | the closing part |
| anthology | a collection of poems or stories |

> **Tip:** Learn the three dead words as a set. Mourning is elegy, praise is eulogy, tomb writing is epitaph.

### Time words
| Word | Meaning |
|---|---|
| annual | once a year |
| biannual | twice a year |
| biennial | once in two years |
| perennial | lasting through the years |
| decade, century, millennium | 10, 100, 1000 years |
| nocturnal | active at night |
| diurnal | active by day |

> **Rule:** -ennial counts years, so biennial is every two years. -annual counts times in a year, so biannual is twice a year.

### That which cannot be ...
These start with in-, il- or im-, which mean not. The verb in the stem decides.
| Cannot be | Word |
|---|---|
| read | illegible |
| seen | invisible |
| heard | inaudible |
| believed | incredible |
| avoided | inevitable |
| conquered | invincible |
| corrected | incorrigible |
| wiped out | indelible |

> **Watch:** Illegible means cannot be read. Ineligible means not qualified. They sound alike.

### Worked examples
- *Opening part of a play.* Pro- means before. The word is **prologue**.
- *Speaking one's thoughts aloud when alone.* The word is **soliloquy**.
- *Active at night.* The word is **nocturnal**. Active by day is diurnal.
- *That which cannot be avoided.* The word is **inevitable**.

Read the key word in each stem first. It gives the answer before you look at the options.

### How to answer
1. Decide the set: government, speech and writing, time, or cannot-be.
2. Find the key word: the ruler, the kind of writing, the number of years, or the verb.
3. Match it, then check the look-alike pair.
""",
    patterns=[
        pat("ogs-p1", "Government or rule by ...", "very common",
            "The phrase says 'government by', 'rule by', or 'a state with no government'.",
            ["Underline the ruler.", "Match the ruler to the word in the table.", "Check the suffix -cracy or -archy."],
            "The ruler decides the word.",
            "Government by the wealthy: (a) aristocracy (b) plutocracy (c) democracy (d) oligarchy",
            ["The ruler is the wealthy.", "Aristocracy is nobles and democracy is the people.", "Wealth is pluto, so plutocracy."],
            "(b) plutocracy"),
        pat("ogs-p2", "Speech and literary words", "very common",
            "The phrase is about a poem, a speech, tomb writing, a life story or talking alone.",
            ["Underline the kind of writing or speech.", "Sort: mourning, praise or tomb.",
             "Pick the word for that job."],
            "Overlapping pairs make this set easy to mix up.",
            "A speech or writing that praises someone: (a) elegy (b) eulogy (c) epitaph (d) epilogue",
            ["The key idea is praise.", "Elegy is mourning. Epitaph is on a tomb.", "Eulogy is praise."], "(b) eulogy"),
        pat("ogs-p3", "Time and frequency words", "common",
            "The phrase gives how often (every two years, twice a year) or when (at night).",
            ["Underline the count or the time.", "Use -ennial for years and -annual for times a year.",
             "Pick the matching word."],
            "The word part shows what is counted.",
            "Once in two years: (a) annual (b) biannual (c) biennial (d) perennial",
            ["Every two years is a count of years.", "Biannual is twice a year.", "Biennial is once in two years."],
            "(c) biennial"),
        pat("ogs-p4", "That which cannot be ...", "common",
            "The phrase says 'that which cannot be read, seen, heard, conquered or corrected'.",
            ["Underline the verb.", "Recall the in- word for it.", "Check sound-alike pairs."],
            "The verb in the stem gives the word.",
            "That which cannot be read: (a) illegible (b) ineligible (c) inaudible (d) invisible",
            ["The verb is read.", "Inaudible is not heard and invisible is not seen.", "Ineligible sounds alike but means not qualified."],
            "(a) illegible"),
        pat("ogs-p5", "Small-group and no-government rule", "occasional",
            "The phrase names a few rulers or no ruler at all.",
            ["Underline how many rule: few or none.", "Match: a small group is oligarchy, none is anarchy.",
             "Reject monarchy and autocracy."],
            "The number of rulers is the whole clue.",
            "Rule by a small group of people: (a) anarchy (b) oligarchy (c) monarchy (d) theocracy",
            ["The ruler is a small group.", "Anarchy is no government.", "Monarchy is one king or queen."], "(b) oligarchy"),
    ],
    mistakes=[
        mis("Mixing elegy, eulogy and epitaph.", "Mourning poem is elegy. Praise is eulogy. Tomb writing is epitaph."),
        mis("Confusing biannual and biennial.", "Biannual is twice a year. Biennial is once in two years."),
        mis("Choosing ineligible for 'cannot be read'.", "Cannot be read is illegible. Ineligible is not qualified."),
        mis("Using anarchy for a small ruling group.", "Anarchy is no government. A small group is oligarchy."),
        mis("Learning government words without the ruler.", "Learn each word with its ruler: rich, nobles, people, officials."),
    ],
    revision=[
        "Ruler decides: people democracy, rich plutocracy, officials bureaucracy, God theocracy, none anarchy.",
        "Dead words: elegy mourning, eulogy praise, epitaph tomb.",
        "Biannual is twice a year. Biennial is every two years.",
        "Cannot-be: read illegible, conquer invincible, correct incorrigible, avoid inevitable.",
        "Nocturnal is by night. Diurnal is by day.",
    ],
    tricks=[
        trick("Ruler first",
              "Circle the ruler in the stem before the options. It gives the word.",
              "Government by officials: (a) bureaucracy (b) theocracy (c) anarchy (d) monarchy",
              ["The ruler is paid officials.", "Theocracy is priests and monarchy is a king.", "Bureaucracy."],
              "(a) bureaucracy"),
        trick("Three dead words",
              "Learn elegy, eulogy and epitaph as one set. One question can ask any of them."),
        trick("Link the verb",
              "Pair each cannot-be word with its verb: read illegible, see invisible, hear inaudible."),
    ],
)

# ---------------------------------------------------------------- 5. strategy
SUBS["ows-strategy"] = sub(
    concept=("One-word substitution gives one or two quick marks in most papers. "
             "It is a memory topic, so the plan is to build a word bank by category and revise it every week. "
             "In the exam, classify the phrase, remove other families, and prefer the more specific word."),
    notes=r"""
### Where it fits
Most SSC, Railway and Banking papers have one or two of these items. Each takes about 15 seconds if you know the word. It is a **memory topic**, so plan a word bank.

### Build the bank by category
Do not learn a random alphabet list. Take one category at a time.
1. Killing (-cide) and fear (-phobia) words.
2. Study (-ology) words and people words.
3. Places and groups.
4. Government, speech, time and cannot-be words.
5. Medical words.
6. Direction and contrast pairs.

Words in one category support each other. Add every new word from mock tests to a **personal sheet** under its category.

### Daily 10-minute routine
- Read 10 new words and 20 old words aloud with their meanings.
- Every weekend, take a 30-word mixed self-test.
- Any word you miss twice goes on a **weak list**. Revise it weekly.

### Four steps in the exam
1. **Classify** the phrase: killing, fear, study, person, place, group, government or medical.
2. **Remove** options from other families. Two usually go here.
3. **Match** the exact detail: bees not birds, mother not father.
4. **Prefer the specific word.** For killing one's mother, matricide beats the general homicide.

> **Rule:** When two options fit, pick the one that matches the detail in the phrase.

### Medical words
| Word | Meaning |
|---|---|
| antidote | medicine against a poison |
| antiseptic | applied to wounds to stop infection |
| anaesthetic | removes the feeling of pain |
| antibiotic | medicine that kills bacteria |
| epidemic | disease spreading widely in one area |
| pandemic | disease spreading over many countries |
| endemic | disease always present in one area |
| convalescent | recovering after an illness |

### Direction and contrast pairs
| Pair | Difference |
|---|---|
| emigrant / immigrant | leaves a country / comes into a country |
| introvert / extrovert | turned inward / outgoing |
| amateur / professional | for pleasure / for pay |
| novice / veteran | beginner / very experienced |

### A worked check
Question: *the murder of one's mother.*
1. Classify: this is a killing word, so the suffix is -cide.
2. Remove options from other families, such as -phobia or -ology words.
3. Match the detail: mother is mater, so matricide.
4. Reject homicide. It is true but too general.

### Spelling-based items
Some questions say *select the correctly spelt word*. All four options are one word with different spellings. Know the word, then check the tricky letters. Say it in syllables: con-va-les-cent, a-the-ist, ob-so-lete.

> **Watch:** If two options remain and you are unsure, guess only if the paper has no negative marking. Otherwise use the specific-detail rule first.
""",
    patterns=[
        pat("ost-p1", "Specific word beats the general word", "very common",
            "Two options fit the family. One is general (homicide) and one matches the exact detail (matricide).",
            ["Underline the detail in the phrase.", "Find the option that names that detail.", "Reject the general word."],
            "The examiner rewards the word that fits the detail.",
            "The murder of one's mother: (a) homicide (b) matricide (c) suicide (d) genocide",
            ["The detail is mother.", "Homicide is killing any human.", "Matricide names the mother."], "(b) matricide"),
        pat("ost-p2", "Medical and science words", "common",
            "The phrase is about a medicine, the spread of a disease, or recovery.",
            ["Underline what the phrase describes.", "Sort: area, world or always present for diseases.",
             "Pick the word."],
            "Epidemic, endemic and pandemic differ only by spread.",
            "A disease spreading over many countries: (a) epidemic (b) endemic (c) pandemic (d) antidote",
            ["Many countries means a very wide spread.", "Epidemic is one area and endemic is always present.", "Pandemic."],
            "(c) pandemic"),
        pat("ost-p3", "Correctly spelt substitute", "occasional",
            "The question says 'select the correctly spelt word'. All options are one word spelt in four ways.",
            ["Recall the word for the phrase.", "Say it in syllables.", "Match each syllable against the options."],
            "Syllables show which letters belong.",
            "One who is recovering after illness: (a) convalscent (b) convalescent (c) convelescent (d) convalesent",
            ["The word is convalescent.", "Say it: con-va-les-cent.", "Only option (b) has every syllable."],
            "(b) convalescent"),
        pat("ost-p4", "Direction and contrast pairs", "common",
            "Options hold both members of a pair: emigrant and immigrant, introvert and extrovert.",
            ["Find the pair.", "Read the direction or contrast in the phrase.", "Pick the correct member."],
            "The partner is planted as a wrong option.",
            "One who leaves his own country to settle in another: (a) immigrant (b) emigrant (c) extrovert (d) veteran",
            ["The person is leaving his country.", "An immigrant comes into a new country.", "An emigrant leaves."],
            "(b) emigrant"),
        pat("ost-p5", "Classify, then remove families", "very common",
            "The options come from four different families, and the phrase names only one of them.",
            ["Name the family of the phrase.", "Strike options from other families.", "Choose from what is left."],
            "Two options usually die at the classify step.",
            "One who does a job for pleasure, not pay: (a) professional (b) amateur (c) novice (d) veteran",
            ["The family is contrast pairs.", "Not for pay is the key detail.", "Amateur is for pleasure. Professional is for pay."],
            "(b) amateur"),
    ],
    mistakes=[
        mis("Learning words in one long alphabet list.", "Learn by category and keep a personal sheet."),
        mis("Choosing the general word when a specific one is offered.", "Pick the word that matches the exact detail."),
        mis("Mixing epidemic and pandemic.", "Epidemic is one area. Pandemic is many countries or the world."),
        mis("Mixing emigrant and immigrant.", "Emigrant leaves. Immigrant comes in."),
        mis("Skipping the spelling check.", "Say the word in syllables and match each part."),
    ],
    revision=[
        "Bank by category, keep a personal sheet, revise a weekly weak list.",
        "Four steps: classify, remove other families, match the detail, prefer the specific word.",
        "Epidemic is one area. Pandemic is the world. Endemic is always present.",
        "Emigrant leaves. Immigrant comes in.",
        "Amateur is for pleasure. Professional is for pay.",
        "Spelling items: break the word into syllables.",
    ],
    tricks=[
        trick("Specific beats general",
              "If both a general and a specific word fit, choose the specific one. It matches the detail the examiner gave.",
              "Killing of one's brother: (a) homicide (b) fratricide (c) patricide (d) suicide",
              ["The detail is brother.", "Homicide is too general.", "Fratricide names the brother."], "(b) fratricide"),
        trick("Weekly weak list",
              "Any word missed twice goes on a short list. Read only that list twice a week."),
        trick("Syllable check for spelling",
              "For spelling items say the word slowly in syllables and match each syllable to the option."),
    ],
)

if __name__ == "__main__":
    apply("one-word-substitution", SUBS)
