# Notes + per-subtopic patterns for one-word-substitution (Phase 2 deep content).
S = {}


def P(id, name, freq, spot, logic, eq, es):
    return {"id": id, "name": name, "frequency": freq, "howToSpot": spot, "formula": None, "logic": logic,
            "example": {"q": eq, "solution": es}}


S["ows-suffix-families"] = {
"notes": """### What one-word substitution means
In this question you get a group of words, such as *the killing of a king*, and you choose the single word that means the same thing: **regicide**. The exam checks whether you know the word and whether you can separate it from words that look similar.

The good news: most answer words are made of **two parts** — a root (the object) and a suffix (the family). If you know the parts, you can build the meaning even for a word you have never seen.

### The main families
| Suffix | Meaning | Examples |
|---|---|---|
| -cide | killing | regicide (king), fratricide (brother), patricide (father), matricide (mother), infanticide (infant), genocide (a whole race), homicide (a human), suicide (oneself) |
| -phobia | abnormal fear | hydrophobia (water), acrophobia (heights), claustrophobia (closed spaces), xenophobia (foreigners), nyctophobia (darkness) |
| -logy | study of | ornithology (birds), entomology (insects), seismology (earthquakes), etymology (word origins), anthropology (humankind) |
| -graphy / -grapher | writing, drawing | cartography (map-making), calligraphy (beautiful handwriting), lexicographer (dictionary maker) |
| -phile / phil- | lover of | bibliophile (books), philatelist (stamps), philanthropist (lover of mankind, gives to charity) |
| -vore / -vorous | eater of | herbivore (plants), carnivore (flesh), omnivore (both), insectivore (insects) |
| -gamy | marriage | monogamy (one spouse), polygamy (more than one spouse at a time), misogamy (hatred of marriage) |

### Roots worth knowing
- **reg** = king, **frater** = brother, **pater** = father, **mater** = mother, **geno** = race.
- **hydro** = water, **acro** = height, **xeno** = foreign, **nycto** = night.
- **ornitho** = bird, **entomo** = insect, **seismo** = earthquake, **etymo** = true meaning of a word.
- **biblio** = book, **herb** = plant, **carn** = flesh, **omni** = all, **poly** = many, **mono** = one.

Worked example: *nyctophobia* = nycto (night) + phobia (fear) → fear of darkness. You did not need to memorise it as one word.

### How the options are built
A typical question has one right word and three words from the **same or a nearby family**. For *study of insects*, you may see entomology, etymology, ornithology and seismology — all -logy words. So the family step removes nothing here; the **root** decides. Always check both parts.

In other questions the options come from different families: *fear of heights* with acrophobia, acrobat, acronym, acropolis. Here the family step (-phobia = fear) alone finds the answer.

### Look-alike traps
- **entomology** (insects) vs **etymology** (word origins) — one letter group apart.
- **patricide** (father) vs **fratricide** (brother) vs **matricide** (mother).
- **philatelist** (stamps) vs **numismatist** (coins).
- **-phobia** (fear) vs **-phile** (love).
- **astronomy** (science of stars) vs **astrology** (predicting the future from stars).

### Quick revision
| Suffix | Family |
|---|---|
| -cide | killing |
| -phobia | fear |
| -logy | study |
| -graphy / -grapher | writing, drawing, recording |
| -phile | lover |
| -vore | eater |
| -gamy | marriage |

- Split the word: root + suffix.
- Family first, then root.
- Card the look-alike pairs: entomology/etymology, patricide/fratricide, philatelist/numismatist.
""",
"patterns": [
 P("osf-p1", "Killing words (-cide)", "very common",
   "The stem says 'killing of ...' or 'murder of ...' and names a victim (king, brother, father, mother, infant, race).",
   "1. Confirm the family: killing → -cide.\n2. Match the victim to its root: reg = king, frater = brother, pater = father, mater = mother, geno = race.\n3. Choose the word with that root; reject the general 'homicide' if a specific victim is named.\n\n*Why it works:* every -cide word is victim-root + cide, so the victim decides.",
   "*The killing of an infant* — (a) infanticide (b) genocide (c) regicide (d) suicide",
   "Victim = infant → **(a) infanticide**."),
 P("osf-p2", "Fear words (-phobia)", "common",
   "The stem says 'an abnormal fear of ...'.",
   "1. Family: fear → -phobia.\n2. Match the feared thing to its root: hydro = water, acro = height, claustro = closed place, xeno = foreigner, nycto = night.\n3. Reject look-alike non-phobia words (acrobat, hydrant).\n\n*Why it works:* the root names the fear; the suffix only says it is a fear.",
   "*An abnormal fear of darkness* — (a) nyctophobia (b) hydrophobia (c) acrophobia (d) claustrophobia",
   "nycto = night → **(a) nyctophobia**."),
 P("osf-p3", "Study words (-logy)", "common",
   "The stem says 'the study of ...' or 'the science of ...'.",
   "1. Family: study → -logy.\n2. Match the subject: birds → ornithology, insects → entomology, earthquakes → seismology, word origins → etymology.\n3. Watch the entomology/etymology trap.\n\n*Why it works:* all options are usually -logy words, so only the root separates them.",
   "*The study of mankind, its origins and cultures* — (a) anthropology (b) ornithology (c) entomology (d) etymology",
   "anthropo = human → **(a) anthropology**."),
 P("osf-p4", "Lover, eater and marriage words (-phile, -vore, -gamy)", "common",
   "The stem says 'a lover/collector of ...', 'an animal that feeds on ...', or describes a marriage practice.",
   "1. Pick the family: love → phil-, eat → -vore, marriage → -gamy.\n2. Match the root: biblio = books, herb = plants, carn = flesh, mono = one, poly = many.\n3. Reject the look-alike (philatelist vs numismatist; monogamy vs polygamy).\n\n*Why it works:* the same two-part logic applies to every family.",
   "*An animal that eats both plants and flesh* — (a) omnivore (b) herbivore (c) carnivore (d) insectivore",
   "omni = all → **(a) omnivore**."),
],
}

S["ows-people-words"] = {
"notes": """### The biggest group: words for people
The most common one-word-substitution stem begins with **'One who ...'** or **'A person who ...'**. These words name a person by their job, habit, feeling or situation.

### Four boxes to sort people words
**1. Jobs (trades and professions).** Learn each with the object of the job.
| Word | Job |
|---|---|
| cartographer | makes maps |
| lexicographer | writes dictionaries |
| cobbler | mends shoes |
| plumber | fits and repairs water pipes |
| paediatrician | doctor for children |
| dermatologist | doctor for the skin |
| astronomer | studies stars scientifically |
| astrologer | predicts the future from stars |

**2. Habits and character.**
| Word | Meaning |
|---|---|
| teetotaller | never drinks alcohol |
| glutton | eats too much |
| miser | hoards money and hates spending |
| spendthrift | wastes money |
| gullible | easily deceived |
| sceptic | doubts everything |
| garrulous | talks too much |
| taciturn | speaks very little |

**3. Pairs and opposites.** Examiners love to put the partner word as a wrong option.
- widow (woman whose husband has died) / widower (man whose wife has died)
- novice (beginner) / veteran (very experienced)
- miser / spendthrift
- optimist (hopes for the best) / pessimist (expects the worst)

**4. Words built from roots.**
| Word | Parts | Meaning |
|---|---|---|
| polyglot | poly (many) + glot (tongue) | knows many languages |
| misanthrope | mis (hate) + anthrope (man) | hates mankind |
| philanthropist | phil (love) + anthrop (man) | loves mankind, gives to charity |
| misogynist | mis (hate) + gyn (woman) | hates women |
| somnambulist | somn (sleep) + ambul (walk) | walks in sleep |
| omniscient | omni (all) + scient (knowing) | knows everything |

### Worked examples
*One who studies the stars scientifically* → the word 'scientifically' decides → **astronomer**, not astrologer.

*A man whose wife has died* → **widower**. 'Widow' is the partner word planted as a trap.

*One who knows many languages* → poly = many → **polyglot**. 'Polymath' (knows many subjects) is the look-alike.

### How to answer
1. Underline the key detail: the object (maps, children, shoes), the habit (drinks, talks, spends), or the gender.
2. Put the stem into its box: job, habit, pair or root-word.
3. Choose the option that matches the detail exactly. Reject the partner word and the look-alike.

### Quick revision
- Learn job words with their object: cartographer–maps, lexicographer–dictionary, paediatrician–children.
- Habit words come in opposite pairs: miser/spendthrift, garrulous/taciturn, gullible/sceptic.
- Gender pairs: widow/widower.
- Roots: poly (many), mis (hate), phil (love), omni (all), somn (sleep).
""",
"patterns": [
 P("opw-p1", "Person by job or profession", "very common",
   "Stem: 'One who makes/repairs/treats/studies ...' naming an object or a field.",
   "1. Underline the object (maps, dictionaries, children, skin).\n2. Recall the job word linked to that object.\n3. Reject words from nearby jobs (cartographer vs calligrapher).\n\n*Why it works:* job words are defined by their object, so the object decides.",
   "*A doctor who treats skin diseases* — (a) dermatologist (b) paediatrician (c) cardiologist (d) neurologist",
   "derma = skin → **(a) dermatologist**."),
 P("opw-p2", "Person by habit or character", "very common",
   "Stem describes a habit or nature: never drinks, overeats, easily fooled, talks too much.",
   "1. Name the habit in one word (drinking, eating, trusting, talking).\n2. Recall the pair of words on that habit (glutton/abstemious, garrulous/taciturn).\n3. Pick the side the stem describes.\n\n*Why it works:* options often include the opposite habit word as a trap.",
   "*One who speaks very little* — (a) taciturn (b) garrulous (c) eloquent (d) loquacious",
   "Speaks little → **(a) taciturn**. Garrulous and loquacious mean the opposite."),
 P("opw-p3", "Partner-word trap (gender or opposite pairs)", "common",
   "The options contain both members of a pair: widow/widower, miser/spendthrift, novice/veteran.",
   "1. Find the deciding detail (man or woman? saves or wastes? new or old?).\n2. Choose the member of the pair that matches it.\n3. Do not pick the familiar-looking partner.\n\n*Why it works:* the examiner adds the partner so a hurried reader picks it.",
   "*One who has long experience in a field* — (a) veteran (b) novice (c) amateur (d) apprentice",
   "Long experience → **(a) veteran**. Novice is the opposite partner."),
 P("opw-p4", "Root-built person words", "common",
   "The answer is a Greek or Latin-built word: poly-, mis-, phil-, omni-, somn-.",
   "1. Split each option into prefix + root.\n2. Match the parts to the stem (many + tongue = many languages).\n3. Reject the option with a similar prefix but a different root.\n\n*Why it works:* rare person words are almost always transparent root stacks.",
   "*One who walks in sleep* — (a) somnambulist (b) somniloquist (c) insomniac (d) pedestrian",
   "somn (sleep) + ambul (walk) → **(a) somnambulist**. Somniloquist talks in sleep."),
],
}

S["ows-places-collections"] = {
"notes": """### Two simple question shapes
1. **'A place where ___ is kept / done'** → a place word.
2. **'A group of ___'** → a collective noun.
Both are pure matching: the stem names the thing, you name its place or group.

### Places: match the thing kept inside
| Place | What is kept or done there |
|---|---|
| apiary | bees |
| aviary | birds |
| aquarium | fish and water animals |
| granary | grain |
| armoury / arsenal | weapons |
| mint | coins are made |
| hangar | aircraft are kept and repaired |
| kennel | dogs |
| stable | horses |
| mortuary | dead bodies (before burial or post-mortem) |
| cemetery | burial ground |
| abattoir | animals are killed for meat |
| monastery | monks live |
| convent | nuns live |
| orphanage | orphans live |
| observatory | stars are studied through telescopes |

Worked example: *A place where coins are made* → **mint**. A treasury keeps money but does not make coins, so it is wrong.

### One-letter and look-alike traps
- **apiary** (bees) vs **aviary** (birds). Remember: *api* sounds like 'ape-bee'; *avi* as in aviation (flying birds).
- **monastery** (monks, men) vs **convent** (nuns, women).
- **mortuary** (bodies kept) vs **cemetery** (bodies buried).
- **hangar** (aircraft) vs **hanger** (for clothes) — spelling matters.

### Groups: the collective nouns
| Group of | Word |
|---|---|
| lions | pride |
| wolves, dogs | pack |
| cattle | herd |
| sheep, birds | flock |
| bees | swarm |
| fish | school / shoal |
| ships | fleet |
| islands | archipelago |
| stars in a pattern | constellation |
| flowers | bouquet |
| worshippers in a church | congregation |
| musicians | orchestra / band |

Worked example: *A group of wolves* → **pack**. Lions take pride, cattle take herd — the animal decides.

### How to answer
1. Find the key noun in the stem (bees, coins, wolves, islands).
2. Recall its partner place or group word.
3. Check the look-alike trap before you mark.

These questions are fast marks. Twenty place words and twenty group words cover almost every paper, so learn them in one sitting and revise weekly.

### Quick revision
- Places: apiary (bees), aviary (birds), granary (grain), mint (coins), hangar (aircraft), mortuary (bodies), abattoir (slaughter), monastery (monks), convent (nuns).
- Groups: pride (lions), pack (wolves), herd (cattle), flock (sheep), swarm (bees), fleet (ships), archipelago (islands), constellation (stars).
- Traps: apiary/aviary, monastery/convent, mortuary/cemetery.
""",
"patterns": [
 P("opc-p1", "Place where something is kept or made", "very common",
   "Stem: 'A place where ___ are kept / stored / made'.",
   "1. Underline the thing kept (bees, grain, coins, aircraft).\n2. Recall the place word for that thing.\n3. Check one-letter look-alikes (apiary/aviary).\n\n*Why it works:* each place word is tied to one stored thing.",
   "*A place where dogs are kept* — (a) kennel (b) stable (c) aviary (d) apiary",
   "Dogs → **(a) kennel**. Stable is for horses."),
 P("opc-p2", "Place named by the people or activity in it", "common",
   "Stem: 'A place where monks live', 'where bodies are kept', 'where animals are slaughtered'.",
   "1. Identify who lives there or what happens there.\n2. Match: monks → monastery, nuns → convent, bodies → mortuary, slaughter → abattoir.\n3. Separate close pairs (mortuary vs cemetery).\n\n*Why it works:* the activity or resident fixes one word.",
   "*A place where nuns live* — (a) convent (b) monastery (c) seminary (d) orphanage",
   "Nuns → **(a) convent**. Monastery is for monks."),
 P("opc-p3", "Collective noun for animals", "very common",
   "Stem: 'A group of lions / wolves / cattle / bees / sheep'.",
   "1. Name the animal.\n2. Recall its partner: pride, pack, herd, swarm, flock.\n3. Do not be swayed by options that fit other animals.\n\n*Why it works:* the options are the same five words shuffled; the animal decides.",
   "*A group of sheep* — (a) flock (b) pride (c) pack (d) swarm",
   "Sheep → **(a) flock**."),
 P("opc-p4", "Collective noun for things or people", "common",
   "Stem: 'A group of islands / stars / ships / flowers / worshippers'.",
   "1. Name the thing grouped.\n2. Recall the partner word: archipelago, constellation, fleet, bouquet, congregation.\n3. Reject geography or science words that are not groups (peninsula, comet).\n\n*Why it works:* each group word belongs to one kind of thing.",
   "*A bunch of flowers* — (a) bouquet (b) cluster (c) bundle (d) heap",
   "Flowers → **(a) bouquet**."),
],
}

S["ows-government-science"] = {
"notes": """### Government words: who rules?
Every government word answers one question: **who holds the power?** Find the ruler in the stem, then match it.

| Ruled by | Word |
|---|---|
| the people (through elected members) | democracy |
| one person with total power | autocracy / dictatorship |
| a king or queen | monarchy |
| the rich | plutocracy |
| nobles, the upper class | aristocracy |
| a small group | oligarchy |
| officials in government offices | bureaucracy |
| religious leaders, in God's name | theocracy |
| nobody (no government, no law) | anarchy |

Worked example: *Government by the wealthy* → pluto = wealth → **plutocracy**.

### Speech and writing words
These words about speaking and writing come in confusing pairs.
| Word | Meaning |
|---|---|
| elegy | a sad poem mourning the dead |
| eulogy | a speech or writing praising someone (often after death) |
| epitaph | words written on a tomb |
| soliloquy | speaking one's thoughts aloud when alone (as in a play) |
| extempore | spoken without preparation |
| prologue / epilogue | opening part / closing part of a play or book |
| biography / autobiography | life story written by another / by oneself |
| anthology | a collection of poems or stories |

**The three 'dead' words:** mourning poem → elegy, praise → eulogy, tomb writing → epitaph. Learn them as a set of three.

### Time words
| Word | Meaning |
|---|---|
| annual | once a year |
| biannual | twice a year |
| biennial | once in two years |
| perennial | lasting through the years |
| centenary | 100th anniversary |
| decade / century / millennium | 10 / 100 / 1000 years |
| nocturnal | active at night |
| diurnal | active in the daytime |

Memory tip: **-ennial** counts years (biennial = every 2 years); **-annual** counts times in a year (biannual = 2 times a year).

### 'That which cannot be ___' words
These start with *in-*, *il-* or *im-* (meaning 'not'). The verb in the stem gives the answer.
| Cannot be ... | Word |
|---|---|
| read (handwriting) | illegible |
| seen | invisible |
| heard | inaudible |
| believed | incredible |
| avoided | inevitable |
| conquered | invincible |
| corrected or reformed | incorrigible |
| wiped out or removed (a mark) | indelible |

Trap: **illegible** (cannot be read) vs **ineligible** (not qualified). They sound alike but mean totally different things.

### How to answer
1. Decide the type: government, speech/writing, time, or 'cannot be'.
2. Find the key word in the stem: the ruler, the kind of writing, the number of years, or the verb.
3. Match it, then check the look-alike pair.

### Quick revision
- Ruler decides: people → democracy, rich → plutocracy, officials → bureaucracy, God → theocracy, none → anarchy.
- Dead words: elegy (mourning), eulogy (praise), epitaph (tomb).
- Biannual = twice a year; biennial = every two years.
- Cannot-be: read → illegible, conquer → invincible, correct → incorrigible, avoid → inevitable.
""",
"patterns": [
 P("ogs-p1", "Government or rule by ...", "common",
   "Stem: 'Government by ...', 'Rule by ...', or 'A state with no government'.",
   "1. Underline the ruler (people, rich, officials, God, nobody).\n2. Match to the -cracy or -archy word.\n3. Reject words whose ruler differs.\n\n*Why it works:* the first part of each word names the ruler.",
   "*Government by a small group of powerful people* — (a) oligarchy (b) monarchy (c) democracy (d) anarchy",
   "oligo = few → **(a) oligarchy**."),
 P("ogs-p2", "Speech and literary words", "common",
   "Stem is about a poem, speech, tomb writing, life story or talking alone.",
   "1. Decide what the writing does (mourns, praises, marks a tomb, tells a life).\n2. Match: mourns → elegy, praises → eulogy, tomb → epitaph, own life → autobiography, alone → soliloquy.\n3. Double-check the elegy/eulogy pair.\n\n*Why it works:* the options are usually drawn from this small, confusing set.",
   "*A collection of poems by different writers* — (a) anthology (b) biography (c) epilogue (d) elegy",
   "Collection → **(a) anthology**."),
 P("ogs-p3", "Time and frequency words", "occasional",
   "Stem mentions how often (every two years, twice a year) or when (at night, 100th anniversary).",
   "1. Note the exact number and unit.\n2. Apply the rule: -ennial counts years, -annual counts per year.\n3. For day/night use diurnal/nocturnal.\n\n*Why it works:* the options differ only in the counting, so precise reading wins.",
   "*Happening twice a year* — (a) biannual (b) biennial (c) annual (d) perennial",
   "Twice a year → **(a) biannual**. Biennial is every two years."),
 P("ogs-p4", "'That which cannot be ___' words", "common",
   "Stem: 'That which cannot be read / seen / conquered / corrected'.",
   "1. Find the verb in the stem.\n2. Recall the in-/il- word built on that verb.\n3. Watch the sound-alike (illegible vs ineligible).\n\n*Why it works:* each negative word is built on exactly one verb.",
   "*That which cannot be heard* — (a) inaudible (b) invisible (c) illegible (d) indelible",
   "Heard → audio → **(a) inaudible**."),
],
}

S["ows-strategy"] = {
"notes": """### Where one-word substitution fits
Most papers in SSC, Railway and Banking exams have one or two one-word-substitution questions. Each takes about 15 seconds if you know the word. It is a **memory topic**, so your plan should be about building and revising a word bank.

### Build the bank by category
Do not learn a random alphabetical list. Learn one category at a time:
1. Killing words (-cide) and fear words (-phobia).
2. Study words (-logy) and people words (jobs, habits).
3. Places and groups.
4. Government, speech, time and 'cannot be' words.
5. Medical words (anti-, epi-/pan-/endemic).
6. Direction and contrast pairs (emigrant/immigrant, introvert/extrovert, amateur/professional).

Words in one category support each other in memory. When you meet a new word in a mock test, add it to a **personal sheet** under its category.

### Daily 10-minute routine
- 10 new words + 20 old words, read aloud with the meaning.
- Every weekend: a 30-word mixed self-test.
- Any word you miss twice goes on a **weak list** that you revise every week.

### The four-step method in the exam
1. **Classify the stem:** killing? fear? study? person? place? group? government? medical?
2. **Remove other families:** options from a different family are usually wrong.
3. **Match the exact detail:** bees, not birds; mother, not father; whole world, not one area.
4. **Prefer the specific word:** if two options fit, choose the one that matches the stem's detail. For *killing of one's mother*, **matricide** beats the general *homicide*.

### Medical and science words
| Word | Meaning |
|---|---|
| antidote | medicine against a poison |
| antiseptic | substance applied to wounds to stop infection |
| anaesthetic | substance that removes the feeling of pain |
| antibiotic | medicine that kills bacteria inside the body |
| epidemic | disease spreading widely in one area at one time |
| pandemic | disease spreading over many countries or the whole world |
| endemic | disease always present in a particular area |
| convalescent | recovering after an illness |

### Direction and contrast pairs
| Pair | Difference |
|---|---|
| emigrant / immigrant | leaves his country / comes into a new country |
| introvert / extrovert | turned inward, shy / outgoing, sociable |
| amateur / professional | does it for pleasure / does it as a paid job |
| novice / veteran | beginner / very experienced |

### Spelling-based questions
Newer papers sometimes say *'Select the correctly spelt word that can substitute ...'*. All four options are the same word spelt differently. Know the word, then check its tricky letters: con-va-les-**cent**, athe-**ist**, obso-**lete**. Say the word in syllables and match each part.

### Never leave it blank?
If you have removed two options and are sure the answer is in the remaining two, choose using the specific-detail rule. If you have no idea at all, remember that most exams have negative marking — a blind guess is not wise.

### Quick revision
- Category-wise bank + personal sheet from mocks + weekly weak list.
- Four steps: classify → remove other families → match the detail → prefer the specific word.
- Medical: epidemic (one area), pandemic (world), endemic (always in an area).
- Pairs: emigrant/immigrant, introvert/extrovert, amateur/professional.
- Spelling items: break the word into syllables.
""",
"patterns": [
 P("ost-p1", "Specific word beats the general word", "common",
   "Two options fit the family; one is general (homicide, epidemic) and one matches the stem's exact detail (matricide, pandemic).",
   "1. Underline the exact detail in the stem (mother, whole world, new to the job).\n2. Test each in-family option against that detail.\n3. Pick the one that matches it exactly.\n\n*Why it works:* one-word substitution always wants the most precise single word.",
   "*The killing of a human being by another* — (a) homicide (b) genocide (c) suicide (d) regicide",
   "No special victim is named, only 'a human being' → **(a) homicide**."),
 P("ost-p2", "Medical and science words", "common",
   "Stem is about a medicine, a disease's spread, or recovery.",
   "1. Decide the job: against poison, against germs on a wound, removes pain, kills bacteria inside.\n2. For diseases decide the spread: one area now (epidemic), world (pandemic), always in one area (endemic).\n3. Match and check the anti- look-alikes.\n\n*Why it works:* the anti- and -demic words differ by one precise idea.",
   "*A medicine that kills bacteria inside the body* — (a) antibiotic (b) antidote (c) antiseptic (d) anaesthetic",
   "Kills bacteria, taken into the body → **(a) antibiotic**."),
 P("ost-p3", "Correctly spelt one-word substitute", "occasional",
   "Stem says 'Select the correctly spelt word ...'; all four options are one word in different spellings.",
   "1. Recall the word from the meaning.\n2. Break it into syllables and check each part.\n3. Watch common slips: -ent/-ant, -ie-/-ei-, single/double letters.\n\n*Why it works:* only one spelling is standard; the rest differ in one tricky syllable.",
   "Correctly spelt word for *a person who does not believe in God*: (a) atheist (b) athiest (c) atheest (d) aithiest",
   "athe + ist → **(a) atheist**."),
 P("ost-p4", "Direction and contrast pairs", "common",
   "Options contain both members of a pair (emigrant/immigrant, introvert/extrovert, amateur/professional).",
   "1. Find the direction or contrast in the stem (leaving or entering? inward or outward? pleasure or pay?).\n2. Choose the matching member.\n3. Use the prefix: e-/ex- = out, im-/in- = in.\n\n*Why it works:* the prefix encodes the direction, so it decides the pair.",
   "*A person who is outgoing and enjoys the company of others* — (a) extrovert (b) introvert (c) recluse (d) misanthrope",
   "extro = outward → **(a) extrovert**."),
],
}
