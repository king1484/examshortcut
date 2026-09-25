# New practice questions for one-word-substitution. In every item opts[0] is the correct answer;
# QA() moves it to a deterministic position. TARGET records the word each question asks, so the
# build script can check that no word is asked twice in practice.
from _lib import QA

TARGET = {}
SUB = "Select the option that can substitute the given group of words.\n\n"
SPELL = "Select the correctly spelt word that can substitute the given group of words.\n\n"


def mk(qid, sub, pat, target, q, opts, solution, shortcut=None, diff="medium", t=25):
    TARGET[qid] = target.lower()
    return QA(qid, sub, pat, q, opts, solution, shortcut=shortcut, diff=diff, t=t)


def QS_OWS():
    qs = []
    A = qs.append
    F = "ows-suffix-families"
    PW = "ows-people-words"
    PC = "ows-places-collections"
    GS = "ows-government-science"
    ST = "ows-strategy"

    # ---------------- ows-suffix-families (osf) ----------------
    A(mk("ows-suffix-families-p01", F, "osf-p1", "matricide", SUB + "The killing of one's own mother",
         ["matricide", "patricide", "fratricide", "genocide"],
         "mater = mother, so killing of the mother = **matricide**. Patricide is the father, fratricide the brother; no special victim is named in genocide.",
         "Victim root decides: mater = mother.", "hard", 25))
    A(mk("ows-suffix-families-p02", F, "osf-p1", "genocide", SUB + "The killing of a whole race or community",
         ["genocide", "homicide", "fratricide", "infanticide"],
         "geno = race, so killing of a whole race = **genocide**. Homicide is a general killing of a human being; the stem names a race.",
         "geno = race.", "medium", 25))
    A(mk("ows-suffix-families-p03", F, "osf-p2", "acrophobia", SUB + "An abnormal fear of heights",
         ["acrophobia", "hydrophobia", "xenophobia", "agoraphobia"],
         "acro = height, so fear of heights = **acrophobia**. Hydrophobia is fear of water, xenophobia of foreigners, agoraphobia of open or crowded places.",
         "acro = high place.", "easy", 20))
    A(mk("ows-suffix-families-p04", F, "osf-p2", "hydrophobia", SUB + "An abnormal fear of water",
         ["hydrophobia", "acrophobia", "nyctophobia", "photophobia"],
         "hydro = water, so fear of water = **hydrophobia**. Nyctophobia is fear of darkness, photophobia fear of light.",
         "hydro = water.", "easy", 20))
    A(mk("ows-suffix-families-p05", F, "osf-p3", "entomology", SUB + "The scientific study of insects",
         ["entomology", "etymology", "anthropology", "ornithology"],
         "entomo = insect, so the study of insects = **entomology**. Etymology (word origins) is the classic one-letter-group trap; ornithology is birds.",
         "ENTO = iNSEcts; ETYM = words.", "hard", 30))
    A(mk("ows-suffix-families-p06", F, "osf-p3", "seismology", SUB + "The scientific study of earthquakes",
         ["seismology", "anthropology", "archaeology", "etymology"],
         "seismo = earthquake, so **seismology**. Archaeology studies the past by digging; anthropology studies humankind.",
         "seismo = shake.", "medium", 25))
    A(mk("ows-suffix-families-p07", F, "osf-p4", "polygamy", SUB + "The practice of having more than one spouse at the same time",
         ["polygamy", "monogamy", "misogamy", "misogyny"],
         "poly = many + gamy = marriage → **polygamy**. Monogamy is one spouse; misogamy is hatred of marriage, misogyny hatred of women.",
         "poly = many, mono = one.", "medium", 25))
    A(mk("ows-suffix-families-p08", F, "osf-p4", "philatelist", SUB + "One who collects stamps as a hobby",
         ["philatelist", "numismatist", "bibliophile", "philanderer"],
         "A stamp collector = **philatelist**. A numismatist collects coins; a bibliophile loves books; a philanderer is a man who flirts.",
         "Numismatist = coins.", "hard", 30))

    # ---------------- ows-people-words (opw) ----------------
    A(mk("ows-people-words-p01", PW, "opw-p1", "cartographer", SUB + "One who draws maps",
         ["cartographer", "calligrapher", "choreographer", "cinematographer"],
         "Maps → **cartographer**. The -grapher options are job words for other objects: beautiful writing, dance movements and films.",
         "All -graphers; match the object.", "easy", 20))
    A(mk("ows-people-words-p02", PW, "opw-p1", "paediatrician", SUB + "A doctor who treats diseases of children",
         ["paediatrician", "dermatologist", "cardiologist", "psychiatrist"],
         "Children → **paediatrician**. The others treat skin, heart and the mind.",
         "paed = child.", "easy", 20))
    A(mk("ows-people-words-p03", PW, "opw-p1", "lexicographer", SUB + "One who compiles a dictionary",
         ["lexicographer", "cartographer", "calligrapher", "demographer"],
         "lexicon = dictionary, so its maker is a **lexicographer**. A demographer studies population statistics.",
         "lexico = wordbook.", "medium", 25))
    A(mk("ows-people-words-p04", PW, "opw-p2", "teetotaller", SUB + "One who never drinks alcohol",
         ["teetotaller", "glutton", "spendthrift", "ascetic"],
         "Total abstainer from alcohol = **teetotaller**. A glutton overeats; a spendthrift wastes money; an ascetic lives a strict simple life, which is broader than abstaining from drink.",
         "T for Total abstainer.", "easy", 20))
    A(mk("ows-people-words-p05", PW, "opw-p2", "gullible", SUB + "One who is easily cheated or deceived",
         ["gullible", "sceptic", "cynic", "pessimist"],
         "One who believes too readily and is easily fooled = **gullible**. A sceptic doubts everything — almost the opposite; a cynic expects selfish motives; a pessimist expects the worst.",
         "Gullible = gulps any story.", "medium", 25))
    A(mk("ows-people-words-p06", PW, "opw-p3", "widow", SUB + "A woman whose husband has died",
         ["widow", "widower", "spinster", "matron"],
         "The man who has lost his wife is a widower; the woman is a **widow**. The pair word is the planted trap.",
         "Gender pair: widow / widower.", "easy", 20))
    A(mk("ows-people-words-p07", PW, "opw-p3", "spendthrift", SUB + "One who spends money wastefully",
         ["spendthrift", "miser", "hoarder", "steward"],
         "Wasteful spender = **spendthrift**. A miser saves excessively and hates spending — the opposite partner; a hoarder piles things up; a steward manages another's household.",
         "Spend + thriftless.", "medium", 25))
    A(mk("ows-people-words-p08", PW, "opw-p4", "polyglot", SUB + "One who can speak many languages",
         ["polyglot", "polymath", "polygamist", "monoglot"],
         "poly = many + glot = tongue → **polyglot**. A polymath knows many subjects, not languages; a monoglot speaks only one — the planted opposite.",
         "glot = tongue.", "medium", 25))
    A(mk("ows-people-words-p09", PW, "opw-p4", "misogynist", SUB + "One who hates women",
         ["misogynist", "misanthrope", "misogamist", "feminist"],
         "mis = hate + gyn = woman → **misogynist**. A misanthrope hates mankind in general; a misogamist hates marriage.",
         "gyn = woman (as in gynaecology).", "medium", 25))

    # ---------------- ows-places-collections (opc) ----------------
    A(mk("ows-places-collections-p01", PC, "opc-p1", "granary", SUB + "A place where grain is stored",
         ["granary", "aviary", "apiary", "arsenal"],
         "Grain → **granary**. Aviary is for birds, apiary for bees, arsenal for weapons — all stored-thing places for other things.",
         "gran = grain.", "easy", 20))
    A(mk("ows-places-collections-p02", PC, "opc-p1", "hangar", SUB + "A place where aircraft are kept and repaired",
         ["hangar", "hanger", "garage", "dockyard"],
         "Aircraft → **hangar**. 'Hanger' (one who/that which hangs clothes) is the spelling trap; a dockyard serves ships.",
         "Hangar with -ar for aircraft.", "medium", 25))
    A(mk("ows-places-collections-p03", PC, "opc-p1", "arsenal", SUB + "A place where weapons and ammunition are stored",
         ["arsenal", "granary", "mortuary", "mint"],
         "Weapons → **arsenal**. A mortuary keeps dead bodies; a mint makes coins.",
         "Arsenal = arms.", "easy", 20))
    A(mk("ows-places-collections-p04", PC, "opc-p2", "monastery", SUB + "A place where monks live as a community",
         ["monastery", "convent", "seminary", "orphanage"],
         "Monks (men) → **monastery**; nuns (women) → convent. A seminary trains priests; an orphanage houses orphans.",
         "Monks → monastery.", "easy", 20))
    A(mk("ows-places-collections-p05", PC, "opc-p2", "mint", SUB + "A place where coins are manufactured",
         ["mint", "treasury", "granary", "refinery"],
         "Coins are made at a **mint**. A treasury keeps public money but does not make coins; a refinery processes oil or ore.",
         "Coins → mint.", "medium", 25))
    A(mk("ows-places-collections-p06", PC, "opc-p2", "observatory", SUB + "A place where stars and planets are studied with telescopes",
         ["observatory", "planetarium", "laboratory", "aquarium"],
         "Stars studied through telescopes → **observatory**. A planetarium is a domed hall that shows an artificial sky; it is not a study place.",
         "observe → observatory.", "medium", 25))
    A(mk("ows-places-collections-p07", PC, "opc-p3", "swarm", SUB + "A large group of bees flying together",
         ["swarm", "flock", "herd", "pack"],
         "Bees → **swarm**. Flock is for sheep or birds, herd for cattle, pack for wolves or dogs.",
         "Bees swarm.", "easy", 20))
    A(mk("ows-places-collections-p08", PC, "opc-p3", "pack", SUB + "A group of wolves",
         ["pack", "herd", "pride", "swarm"],
         "Wolves hunt in a **pack**. Lions take pride, cattle take herd, bees swarm.",
         "Wolves → pack.", "medium", 20))
    A(mk("ows-places-collections-p09", PC, "opc-p4", "constellation", SUB + "A group of stars forming a fixed pattern",
         ["constellation", "galaxy", "planetarium", "archipelago"],
         "A fixed pattern of stars = a **constellation** (like the Great Bear). A galaxy is a vast system of millions of stars, not a named pattern.",
         "Pattern of stars.", "hard", 30))
    A(mk("ows-places-collections-p10", PC, "opc-p4", "fleet", SUB + "A group of ships sailing together",
         ["fleet", "flock", "bouquet", "heap"],
         "Ships → **fleet**. Flock is for birds or sheep; a bouquet is a bunch of flowers.",
         "Navy fleet.", "easy", 20))
    A(mk("ows-places-collections-p11", PC, "opc-p4", "archipelago", SUB + "A group of islands lying close together",
         ["archipelago", "peninsula", "constellation", "continent"],
         "A cluster of islands = **archipelago**. A peninsula is land almost surrounded by water — the planted geography look-alike.",
         "Islands cluster.", "medium", 25))

    # ---------------- ows-government-science (ogs) ----------------
    A(mk("ows-government-science-p01", GS, "ogs-p1", "plutocracy", SUB + "Government by the rich",
         ["plutocracy", "democracy", "autocracy", "bureaucracy"],
         "pluto = wealth → rule by the rich = **plutocracy**. Democracy is rule by the people, autocracy by one person, bureaucracy by officials.",
         "pluto = wealth.", "medium", 25))
    A(mk("ows-government-science-p02", GS, "ogs-p1", "theocracy", SUB + "Government by religious leaders who claim to rule in the name of God",
         ["theocracy", "monarchy", "democracy", "anarchy"],
         "theo = God → **theocracy**. Monarchy is rule by a king; anarchy is the absence of any rule.",
         "theo = God.", "medium", 25))
    A(mk("ows-government-science-p03", GS, "ogs-p1", "anarchy", SUB + "A state of society with no government and no law",
         ["anarchy", "monarchy", "oligarchy", "autonomy"],
         "an = without + archy = rule → **anarchy**, lawlessness. Oligarchy is rule by a few; autonomy is self-rule of a region within a state.",
         "an = not.", "medium", 25))
    A(mk("ows-government-science-p04", GS, "ogs-p2", "elegy", SUB + "A poem of mourning for the dead",
         ["elegy", "eulogy", "epithet", "epilogue"],
         "A sad poem mourning the dead = **elegy**. A eulogy is a speech or writing that praises the dead — mourns vs praises is the trap.",
         "Elegy = sobs; eulogy = praises.", "hard", 30))
    A(mk("ows-government-science-p05", GS, "ogs-p2", "autobiography", SUB + "The story of a person's life written by the person himself",
         ["autobiography", "biography", "anthology", "almanac"],
         "auto = self → written by oneself = **autobiography**. A biography is written by another person; an anthology is a collection of poems or stories; an almanac is a yearly book of dates and facts.",
         "auto = self.", "easy", 20))
    A(mk("ows-government-science-p06", GS, "ogs-p3", "biennial", SUB + "Happening once in two years",
         ["biennial", "biannual", "annual", "perennial"],
         "The -ennial family counts years: once in two years = **biennial**. Biannual means twice in one year — the classic trap.",
         "-ennial = years, -annual = per year.", "hard", 30))
    A(mk("ows-government-science-p07", GS, "ogs-p3", "nocturnal", SUB + "Animals that remain active at night",
         ["nocturnal", "diurnal", "aquatic", "arboreal"],
         "Active at night = **nocturnal** (owl, bat). Diurnal animals are active by day; aquatic live in water; arboreal live in trees.",
         "Noct = night.", "easy", 20))
    A(mk("ows-government-science-p08", GS, "ogs-p4", "illegible", SUB + "Handwriting that cannot be read",
         ["illegible", "ineligible", "illiterate", "inaudible"],
         "Cannot be read = **illegible**. Ineligible means not qualified — the sound-alike trap; illiterate means unable to read or write; inaudible cannot be heard.",
         "il- + legible (readable).", "easy", 20))
    A(mk("ows-government-science-p09", GS, "ogs-p4", "invincible", SUB + "That which cannot be conquered or defeated",
         ["invincible", "invisible", "inevitable", "incorrigible"],
         "vinc = conquer (as in victory) → cannot be conquered = **invincible**. Invisible cannot be seen; inevitable cannot be avoided; incorrigible cannot be corrected.",
         "vinc = conquer.", "medium", 25))

    # ---------------- ows-strategy (ost) ----------------
    A(mk("ows-strategy-p01", ST, "ost-p1", "homicide", SUB + "The killing of one human being by another",
         ["homicide", "genocide", "regicide", "suicide"],
         "No special victim is named, only 'a human being' (homi = man), so the general word **homicide** is right. The stem is not about a race, king or oneself.",
         "No victim named → general -cide.", "medium", 25))
    A(mk("ows-strategy-p02", ST, "ost-p1", "pandemic", SUB + "A disease that spreads over many countries and the whole world",
         ["pandemic", "epidemic", "endemic", "quarantine"],
         "pan = all → world-wide spread = **pandemic**. An epidemic spreads fast but stays within one area; endemic is always present in one area; quarantine is a period of isolation, not a disease word.",
         "pan = all the world.", "hard", 30))
    A(mk("ows-strategy-p03", ST, "ost-p1", "orphan", SUB + "A child whose parents are dead",
         ["orphan", "widow", "bereaved", "hermit"],
         "The exact single word is **orphan**. 'Bereaved' only means having lost someone — the general word the specific-word rule beats; a widow lost a husband; a hermit lives alone by choice.",
         "Specific word beats general.", "easy", 20))
    A(mk("ows-strategy-p04", ST, "ost-p2", "antibiotic", SUB + "A medicine that destroys bacteria inside the body",
         ["antibiotic", "antidote", "antiseptic", "anaesthetic"],
         "**Antibiotics** are taken to kill bacteria within. An antidote works against a poison, an antiseptic cleans wounds from outside, an anaesthetic removes the feeling of pain.",
         "anti + bio (life) = against germs.", "medium", 25))
    A(mk("ows-strategy-p05", ST, "ost-p2", "endemic", SUB + "A disease that is always present in a particular area or among a particular people",
         ["endemic", "epidemic", "pandemic", "contagious"],
         "en = in → always present within one area = **endemic**. Epidemic and pandemic describe sudden spread, not constant presence; contagious means spreading by contact.",
         "en = inside one area.", "hard", 30))
    A(mk("ows-strategy-p06", ST, "ost-p2", "anaesthetic", SUB + "A drug that takes away the feeling of pain during an operation",
         ["anaesthetic", "antiseptic", "antibiotic", "antidote"],
         "an = without + aisthesis = feeling → **anaesthetic** removes sensation. The other anti- words fight germs or poison, not pain.",
         "Removes feeling, not germs.", "medium", 25))
    A(mk("ows-strategy-p07", ST, "ost-p3", "atheist", SPELL + "A person who does not believe in the existence of God",
         ["atheist", "athiest", "atheest", "athaist"],
         "The correct spelling is **atheist**: athe + ist. The other options swap the ie/ei letters or distort the syllables.",
         "athe + ist, 'the' inside.", "easy", 25))
    A(mk("ows-strategy-p08", ST, "ost-p3", "convalescent", SPELL + "One who is recovering health after an illness",
         ["convalescent", "convelescent", "convalessant", "convalescant"],
         "**Convalescent** — say it in syllables: con-va-les-cent. The ending is -escent, and the third syllable keeps the s before c.",
         "con-va-LES-cent.", "hard", 35))
    A(mk("ows-strategy-p09", ST, "ost-p4", "extrovert", SUB + "A person who is outgoing and mixes freely with others",
         ["extrovert", "introvert", "recluse", "misanthrope"],
         "extro = outward → interested in what is outside = **extrovert**. An introvert is turned inward; a recluse and a misanthrope avoid people altogether.",
         "extro = out.", "medium", 25))
    A(mk("ows-strategy-p10", ST, "ost-p4", "immigrant", SUB + "One who comes into a foreign country to live there permanently",
         ["immigrant", "emigrant", "expatriate", "traveller"],
         "im/in = in → one who comes IN = **immigrant**. An emigrant leaves his own country (e-/ex- = out); the same person is an emigrant there and an immigrant here.",
         "im = in, e = out.", "medium", 25))

    return qs
