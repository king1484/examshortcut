"""ancient-history deep content — part 1: indus-valley, vedic-age, mahajanapadas, buddhism-jainism."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_indus():
    S = Sub("indus-valley")
    S.notes = """### A lost civilisation, found twice
Until the 1920s schoolbooks said Indian history began with the Vedic age. Then in **1921** Daya Ram Sahni dug at **Harappa** (on the Ravi, in Punjab, Pakistan) and in **1922** R.D. Banerji dug at **Mohenjo-daro** ("mound of the dead", on the Indus, Sindh). The finds were so alike that Sir John Marshall announced in 1924 a whole new civilisation, older than anything known in India. Because Harappa was dug first, the correct name is the **Harappan civilisation**; "Indus Valley civilisation" is the older popular name. It is a **Bronze Age** culture — copper and tin, but **no iron** — and its mature phase lasted about **2600–1900 BCE**.

### How the cities were built
Every big Harappan city follows the same plan, and that plan is the most-asked exam fact.
- The town is divided into two parts: a raised **citadel** in the **west** (for the rulers, granaries, big public buildings) and the **lower town** in the **east** (where ordinary people lived).
- Streets cut each other at **right angles** — a **grid pattern** — with covered drains along the roads. Every house had its own well and bathroom, and the waste water flowed into street drains through clay pipes.
- Buildings used **burnt bricks** of a fixed ratio **1 : 2 : 4** (width : height : length). Using standard bricks everywhere is the clearest sign of a strong central authority.
- The **Great Bath** of Mohenjo-daro is a public tank with steps on two sides and a bitumen (water-proof) lining; the **Great Granary** stood nearby.

### The site table — one find, one site
Exams test the pairing "site ↔ special find" again and again.

| Site | River / state | Signature find |
|---|---|---|
| Harappa | Ravi (Punjab, Pak.) | Rows of granaries, Cemetery R-37, coffin burial |
| Mohenjo-daro | Indus (Sindh, Pak.) | Great Bath, Great Granary, bronze Dancing Girl, Pashupati seal |
| Chanhudaro | Indus (Sindh) | Bead-making workshop; **no citadel** |
| Lothal | Bhogava (Gujarat) | **Dockyard**, rice husk, fire altars |
| Kalibangan | Ghaggar (Rajasthan) | **Ploughed field**, fire altars |
| Banawali | Ghaggar (Haryana) | Clay **plough model**, barley |
| Dholavira | Kutch (Gujarat) | **Water reservoirs**, 10-letter signboard; UNESCO 2021 |
| Rakhigarhi | Ghaggar (Haryana) | **Largest site in India** |
| Surkotada | Kutch (Gujarat) | Horse bones |
| Ropar | Sutlej (Punjab, India) | First site dug after Independence |
| Alamgirpur | Hindon (UP) | **Easternmost** site |
| Sutkagendor | Dasht (Baluchistan) | **Westernmost** site |
| Manda | Chenab (J&K) | **Northernmost** site |
| Daimabad | Pravara (Maharashtra) | **Southernmost** site; bronze chariot |

The four extremes run north-south-east-west: **Manda, Daimabad, Alamgirpur, Sutkagendor**.

### Economy and daily life
- **Agriculture:** wheat and barley were the staple crops; **cotton** was grown here for the first time in the world (Greeks later called it *sindon*, after Sindh). Rice husks appear at **Lothal and Rangpur** in Gujarat.
- **Trade:** seals of **steatite** (soapstone) with animal motifs — the **unicorn bull** is the commonest — were pressed on clay tags for bales of goods. Trade with Mesopotamia is proved by Persian Gulf and Mesopotamian finds; the **dockyard at Lothal** served sea trade.
- **Metal work:** copper and bronze tools, gold and silver ornaments; the famous **bronze Dancing Girl** of Mohenjo-daro shows lost-wax casting. **Iron was unknown.**

### Religion and society
No temple building has been found anywhere — that is a key difference from Egypt or Mesopotamia. Worship seems to have centred on the **Mother Goddess** figurines, a **proto-Shiva (Pashupati)** seal showing a figure seated cross-legged surrounded by animals, the **pipal** tree, and small stone linga-like objects. Burial was in brick chambers or pits; some graves (Lothal, Kalibangan) show **double burials**. The **script** is pictographic, read right to left (boustrophedon in places), and is **still undeciphered** — so we know the civilisation only through objects, not through its own words.

### Why it declined (standard textbook view)
Around 1900 BCE the cities thinned out. Suggested causes work together, not alone: river shifts, floods, drying of the region, overuse of land. No single cause is proved — exam options usually ask which is **not** a cause (a favourite wrong option is "Aryan invasion, proved by evidence").

### Quick revision
- 1921 Harappa (Daya Ram Sahni); 1922 Mohenjo-daro (R.D. Banerji); announced by John Marshall (1924).
- Bronze Age — **no iron**; burnt bricks 1:2:4; grid streets, covered drains.
- Citadel west + lower town east; Great Bath & Great Granary — Mohenjo-daro.
- Lothal = dockyard + rice; Kalibangan = ploughed field; Dholavira = reservoirs + signboard.
- Extremes: Manda (N), Daimabad (S), Alamgirpur (E), Sutkagendor (W).
- Largest in India: Rakhigarhi (Haryana). Commonest seal motif: unicorn bull.
- No temples; Mother Goddess + Pashupati seal; script undeciphered."""
    S.pattern("ga-iv-p1", "Harappan site ↔ signature find", "very common",
        "The stem names a find — dockyard, Great Bath, ploughed field, bead factory, dancing girl — and asks for the site, or gives a site and asks what was found there.",
        None,
        "1. Recall the one-find-one-site table (Lothal = dockyard, Kalibangan = ploughed field, Chanhudaro = beads).\n2. Beware near-pairs: ploughed **field** is Kalibangan, clay plough **model** is Banawali; Great **Bath** is Mohenjo-daro, rows of **granaries** are Harappa.\n3. Eliminate sites whose famous find you already know from the options.",
        "The Harappan site famous for a bead-making workshop, and the only major city without a citadel, is —",
        "**Chanhudaro** (Sindh, Pakistan). Excavated by N.G. Majumdar in 1931.")
    S.pattern("ga-iv-p2", "Site ↔ state/river, and the four extremes", "very common",
        "'In which state is …?', 'the northernmost/easternmost Harappan site is', or a site-to-river match.",
        None,
        "1. Split sites first into Pakistan (Harappa, Mohenjo-daro, Chanhudaro, Kot Diji, Sutkagendor) and India.\n2. Indian sites by state: Gujarat (Lothal, Dholavira, Surkotada), Haryana (Rakhigarhi, Banawali), Rajasthan (Kalibangan), Punjab (Ropar), UP (Alamgirpur), Maharashtra (Daimabad), J&K (Manda).\n3. Extremes in order N-S-E-W: **Manda, Daimabad, Alamgirpur, Sutkagendor**.",
        "Which Harappan site lies in Hanumangarh district of Rajasthan, on the now-dry Ghaggar river?",
        "**Kalibangan** ('black bangles') — known for its ploughed field and fire altars.")
    S.pattern("ga-iv-p3", "Discovery ↔ excavator and year", "common",
        "'Who excavated …?', '… was discovered in which year?', 'which site was dug first after Independence?'",
        None,
        "1. Anchor dates: Harappa 1921 (Daya Ram Sahni), Mohenjo-daro 1922 (R.D. Banerji), announcement 1924 (John Marshall).\n2. Later digs: Lothal 1954-55 (S.R. Rao), Ropar 1953 (Y.D. Sharma — first after Independence), Kalibangan 1960s (B.B. Lal & B.K. Thapar), Dholavira 1990 (R.S. Bisht).\n3. Match the excavator to the site, not to the civilisation as a whole.",
        "Mohenjo-daro was excavated in 1922 by —",
        "**R.D. Banerji**. Harappa (1921) was dug by **Daya Ram Sahni**; both worked under John Marshall.")
    S.pattern("ga-iv-p4", "Town planning, materials and economy facts", "common",
        "Statement questions on burnt bricks, grid plans, drainage, seals, crops, metals or weights.",
        None,
        "1. Planning: grid streets, covered drains, citadel (west) + lower town (east), burnt bricks in ratio 1:2:4.\n2. Economy: wheat-barley staple, cotton first grown here, steatite seals, unicorn bull commonest, trade with Mesopotamia.\n3. Metals: copper, bronze, gold, silver — **never iron**. Horse evidence is doubtful (only Surkotada bones).",
        "Consider the statements about Harappan town planning:\n1. Streets cut one another at right angles in a grid pattern.\n2. Houses were built mainly of sun-dried bricks.\n3. The citadel lay to the west and the lower town to the east.\nWhich are correct?",
        "**1 and 3 only.** The Harappans used **burnt** bricks (ratio 1:2:4), not sun-dried ones — statement 2 is wrong.")
    S.pattern("ga-iv-p5", "Religion, script and society statements", "occasional",
        "Questions on Mother Goddess, Pashupati seal, undeciphered script, burial customs, or 'which deity is NOT attested'.",
        None,
        "1. No temples have been found; worship of Mother Goddess, a proto-Shiva (Pashupati) seal figure, pipal tree.\n2. Script: pictographic, right to left, **undeciphered**.\n3. In 'NOT attested' questions, look for a well-known Vedic/Puranic deity (Indra, Vishnu) — that is the answer.",
        "Which religious element has NOT been found in Harappan sites?\n(a) Mother Goddess figurines (b) A proto-Shiva seal (c) Temple structures (d) Pipal-tree motifs",
        "(c) **Temple structures** — no temple building has been found at any Harappan site.")

    S.q("ga-iv-p1", "easy", "The bronze figure called the **Dancing Girl** was found at —",
        ["Harappa", "Mohenjo-daro", "Lothal", "Kalibangan"], "Mohenjo-daro",
        "The **Dancing Girl**, a bronze statuette made by the lost-wax process, comes from **Mohenjo-daro** (Sindh, Pakistan), along with the Great Bath, the Great Granary and the bearded priest.",
        "Mohenjo-daro gives the 'people' finds: dancing girl, priest, Pashupati seal.", 20)
    S.q("ga-iv-p1", "medium", "Which Harappan site is known for its **dockyard**?",
        ["Lothal", "Chanhudaro", "Surkotada", "Ropar"], "Lothal",
        "**Lothal** (Ahmedabad district, Gujarat), excavated by S.R. Rao, has a brick basin identified as a dockyard for sea trade, plus rice husk and fire altars.",
        "Lothal = Launch (dockyard).", 20)
    S.q("ga-iv-p1", "medium", "Evidence of **rice cultivation** in the Harappan period comes mainly from —",
        ["Kalibangan and Banawali", "Lothal and Rangpur", "Harappa and Mohenjo-daro", "Manda and Ropar"], "Lothal and Rangpur",
        "Rice husk has been found at **Lothal and Rangpur** in Gujarat. The staple food of the civilisation was wheat and barley.",
        "Rice = the 'Gujarat pair' (both sites are in Gujarat).", 25)
    S.q("ga-iv-p2", "easy", "The **northernmost** Harappan site is —",
        ["Manda", "Alamgirpur", "Daimabad", "Sutkagendor"], "Manda",
        "**Manda** on the Chenab in Jammu (J&K) is the northernmost known site. The other extremes: Alamgirpur (UP) east, Daimabad (Maharashtra) south, Sutkagendor (Baluchistan) west.",
        "N-S-E-W: **M**anda, **D**aimabad, **A**lamgirpur, **S**utkagendor.", 20)
    S.q("ga-iv-p2", "medium", "The bronze **chariot**, a famous Harappan find, was discovered at —",
        ["Daimabad", "Lothal", "Dholavira", "Rakhigarhi"], "Daimabad",
        "**Daimabad** (Ahmednagar district, Maharashtra), on the Pravara river, is the southernmost Harappan site and yielded a bronze chariot.",
        "Southernmost + chariot = Daimabad.", 20)
    S.q("ga-iv-p2", "medium", "**Rakhigarhi**, the largest Harappan site in India, lies in which state?",
        ["Punjab", "Rajasthan", "Haryana", "Gujarat"], "Haryana",
        "**Rakhigarhi** is in Hisar district, **Haryana**, on the Ghaggar plain. India's other key Harappan states are Gujarat, Rajasthan, Punjab, UP and Maharashtra.",
        "Two big Haryana sites: Rakhigarhi and Banawali.", 20)
    S.q("ga-iv-p3", "easy", "The first Harappan site to be excavated, in **1921**, was —",
        ["Mohenjo-daro", "Harappa", "Lothal", "Chanhudaro"], "Harappa",
        "**Harappa**, on the Ravi in Punjab (Pakistan), was dug by **Daya Ram Sahni** in 1921; hence the civilisation is correctly called the Harappan civilisation.",
        "1921 Harappa → 1922 Mohenjo-daro.", 20)
    S.q("ga-iv-p3", "medium", "**Dholavira**, noted for its water reservoirs and a 10-letter signboard, was excavated by —",
        ["S.R. Rao", "R.S. Bisht", "B.B. Lal", "N.G. Majumdar"], "R.S. Bisht",
        "**R.S. Bisht** excavated Dholavira (Kutch, Gujarat) in the 1990s. S.R. Rao dug Lothal; B.B. Lal worked at Kalibangan; N.G. Majumdar at Chanhudaro.",
        "Bisht = Bada (big) water city Dholavira.", 25)
    S.q("ga-iv-p4", "easy", "Harappan buildings used **burnt bricks** in the ratio —",
        ["1:2:3", "1:2:4", "2:3:4", "1:3:5"], "1:2:4",
        "Bricks everywhere followed the fixed ratio **width : height : length = 1 : 2 : 4**, a sign of standardisation across the civilisation.",
        "124 — 'one-two-four, burnt bricks sure'.", 20)
    S.q("ga-iv-p4", "medium", "The most common **animal motif** on Harappan seals is the —",
        ["Humped bull", "Unicorn (one-horned bull)", "Elephant", "Tiger"], "Unicorn (one-horned bull)",
        "The **unicorn** (a one-horned bull) appears on the largest number of seals. Other motifs: humped bull, elephant, rhinoceros, tiger.",
        "Unicorn tops the seal count.", 20)
    S.q("ga-iv-p5", "medium", "The Harappan **script** is —",
        ["Written right to left and still undeciphered", "Written left to right and deciphered", "Written in Brahmi", "Written in Kharosthi"], "Written right to left and still undeciphered",
        "The Harappan script is pictographic, generally read **right to left** (boustrophedon in some longer lines), and **no one has deciphered it**. Brahmi and Kharosthi belong to later periods.",
        "Two safe words for the exam: 'undeciphered', 'boustrophedon'.", 20)
    S.q("ga-iv-p5", "hard", "Which of these has NOT been found at Harappan sites?",
        ["Fire altars at Kalibangan and Lothal", "Terracotta Mother Goddess figurines", "A temple complex with a sanctum", "The Pashupati (proto-Shiva) seal"], "A temple complex with a sanctum",
        "No temple structure has been identified at any Harappan city. Fire altars (Kalibangan, Lothal), Mother Goddess figurines and the Pashupati seal of Mohenjo-daro are all attested.",
        "'No temples' is the standard line — pick the temple option.", 25)
    return S


def build_vedic():
    S = Sub("vedic-age")
    S.notes = """### Two halves of one age
The Vedic age (c. 1500–600 BCE) is named after the **Vedas**, our main source. It has two phases.
- **Early (Rigvedic) Vedic, c. 1500–1000 BCE:** people lived in the **Sapta Sindhu** (land of seven rivers — Punjab and beyond). Life was **pastoral**; cattle were the main wealth, and the word for war (*gavishthi*, 'search for cows') shows it. Pottery: ochre-coloured and then plain grey.
- **Later Vedic, c. 1000–600 BCE:** people moved into the **Ganga–Yamuna doab**. **Iron** (*shyama ayas* / *krishna ayas*, 'dark metal') appears and agriculture expands. Pottery: **Painted Grey Ware (PGW)**. Kingdoms replace tribes, and the varna system hardens.

### The four Vedas
| Veda | Content | Reciting priest |
|---|---|---|
| Rigveda | Oldest; 10 mandalas, 1028 hymns | Hotri |
| Samaveda | Rigvedic hymns set to melody — root of Indian music | Udgatri |
| Yajurveda | Sacrificial formulas (prose + verse) | Adhvaryu |
| Atharvaveda | Charms, spells, folk medicine | Brahma |

The Rigveda is the oldest text of the Indo-European world still in use as scripture. Each Veda has attached texts: the **Brahmanas** (ritual prose — Aitareya with the Rigveda, Shatapatha with the Yajurveda), then **Aranyakas** (forest teachings) and finally the **Upanishads** (philosophy, also called *Vedanta*). The six limbs of the Vedas (**Vedangas**) are Shiksha, Kalpa, Vyakarana, Nirukta, Chhanda and Jyotisha.

### Rigveda anchors
Exams love four mandalas: **III, VII, IX, X**.
- **Mandala III** — the **Gayatri Mantra**, addressed to **Savitri**, composed by **Vishwamitra**.
- **Mandala VII** — the **Battle of Ten Kings (Dasarajna)** on the river **Parushni (Ravi)**; **Sudas**, chief of the Bharatas, won.
- **Mandala IX** — entirely devoted to **Soma**.
- **Mandala X** — the **Purusha Sukta**, which first mentions the four varnas (Brahmin from the mouth, Kshatriya from arms, Vaishya from thighs, Shudra from feet).

**Indra** is praised in the most hymns (about 250; *Purandara*, 'fort-breaker'), then **Agni** (about 200), the messenger god; **Varuna** upholds *rita*, the cosmic order. The **Sindhu** is the most-mentioned river, but the **Saraswati** is called the holiest (*naditama*).

### Rivers: Rigvedic names ↔ modern names
| Rigvedic | Modern | Rigvedic | Modern |
|---|---|---|---|
| Vitasta | Jhelum | Vipas | Beas |
| Asikni | Chenab | Sutudri | Sutlej |
| Parushni | Ravi | Kubha | Kabul |
| Drishadvati | Ghaggar–Chautang | Krumu | Kurram |

### Early vs Later Vedic society and polity
| Point | Early Vedic | Later Vedic |
|---|---|---|
| Region | Sapta Sindhu | Ganga–Yamuna doab |
| Economy | Pastoral, cattle wealth | Agriculture, iron |
| Women's status | Comparatively better (Sabha open to women; poetesses like Lopamudra, Apala) | Declines; child marriage appears |
| Assemblies | Sabha, Samiti, Vidatha (all active) | Sabha & Samiti lose power to the king |
| Officers | Rajan, Purohita, Senani, Gramani | Add Bhagadugha (tax collector), Sangrahitri (treasurer) |
| Tax | **Bali** — voluntary tribute | Bali becomes a regular tax |
| Varna | Flexible | Rigid; gotra exogamy rule |

Later Vedic kings performed grand sacrifices to show power: **Rajasuya** (consecration), **Ashvamedha** (horse released to claim supremacy), **Vajapeya** (chariot race). The **four ashramas** (Brahmacharya, Grihastha, Vanaprastha, Sanyasa) are all first listed together in the **Jabala Upanishad**.

### Upanishads and the six schools (Shad-darshana)
| Upanishad | Remember for |
|---|---|
| Mundaka | Source of the national motto **'Satyameva Jayate'** |
| Katha | Dialogue of **Nachiketa** with **Yama** |
| Brihadaranyaka | Oldest and largest; **Yajnavalkya–Gargi** debate |
| Chandogya | Early mention of **Krishna, son of Devaki** |

The six orthodox schools with founders: **Sankhya–Kapila, Yoga–Patanjali, Nyaya–Gautama (Akshapada), Vaisheshika–Kanada, Purva Mimamsa–Jaimini, Uttara Mimamsa (Vedanta)–Badarayana**.

### Quick revision
- Early Vedic = pastoral, Sapta Sindhu, flexible society; Later Vedic = iron + agriculture, doab, PGW, rigid varna.
- Veda-priest pairs: Rig-Hotri, Sama-Udgatri, Yajur-Adhvaryu, Atharva-Brahma.
- Mandalas: 3 Gayatri, 7 Ten Kings, 9 Soma, 10 Purusha Sukta.
- Rivers: Vitasta-Jhelum, Asikni-Chenab, Parushni-Ravi, Vipas-Beas, Sutudri-Sutlej.
- 'Satyameva Jayate' — Mundaka Upanishad. Oldest Upanishad — Brihadaranyaka.
- Darshana founders: Kapila, Patanjali, Gautama, Kanada, Jaimini, Badarayana."""
    S.pattern("ga-ved-p1", "Veda ↔ priest / upaveda / content", "very common",
        "'Which Veda is called…', 'the priest who recites the Samaveda', 'Dhanurveda is attached to which Veda'.",
        None,
        "1. Recall the four Vedas with their priests: Rig-Hotri, Sama-Udgatri, Yajur-Adhvaryu, Atharva-Brahma.\n2. Upavedas: Ayurveda-Rig, Gandharvaveda-Sama, Dhanurveda-Yajur, Shilpaveda-Atharva.\n3. Trap: the Atharvaveda is the 'Veda of magical formulas', and is the latest addition to the Vedic corpus.",
        "Which Veda is partly in prose and partly in verse, and contains sacrificial formulas?",
        "The **Yajurveda** — its Shukla (white) and Krishna (black) recensions mix verse and prose ritual formulas.")
    S.pattern("ga-ved-p2", "Rigveda mandala ↔ content; deities of hymns", "very common",
        "Gayatri Mantra, Battle of Ten Kings, Soma, Purusha Sukta, 'maximum hymns to which god'.",
        None,
        "1. Anchor mandalas: **3 = Gayatri (Vishwamitra, to Savitri)**, **7 = Battle of Ten Kings**, **9 = Soma**, **10 = Purusha Sukta (four varnas)**.\n2. Hymn counts: Indra most (~250), Agni next (~200), Varuna guards rita.\n3. Dasarajna details: river Parushni (Ravi), winner Sudas of the Bharatas.",
        "The Gayatri Mantra of the Rigveda was composed by —",
        "**Rishi Vishwamitra**; it occurs in **Mandala III** and is addressed to **Savitri** (the solar deity).")
    S.pattern("ga-ved-p3", "Rigvedic river ↔ modern name", "common",
        "A Rigvedic river name (Vitasta, Asikni, Parushni, Vipas, Sutudri) with modern rivers as options, or the reverse.",
        None,
        "1. Learn the west-to-east chain: Vitasta-Jhelum, Asikni-Chenab, Parushni-Ravi, Vipas-Beas, Sutudri-Sutlej.\n2. Order trick: the Rigvedic names run in the same order as the modern J-C-R-B-S.\n3. Extras: Kubha = Kabul, Krumu = Kurram, Drishadvati = Ghaggar-Chautang.",
        "The Rigvedic river **Vitasta** is known today as —",
        "The **Jhelum**. Vitasta is still the Kashmiri name of the Jhelum (Vyeth).")
    S.pattern("ga-ved-p4", "Early vs Later Vedic life and polity terms", "common",
        "Statement comparisons (early vs later Vedic) or single-term questions on Bali, Vidatha, sabha-samiti, iron, PGW.",
        None,
        "1. Direction of change: pastoral → agricultural; Sapta Sindhu → doab; assemblies weaken → kings strengthen; Bali voluntary → regular tax.\n2. Terms: Vidatha = oldest assembly; Bali = tribute; Bhagadugha = tax collector; Gramani = village head.\n3. Iron in Later Vedic = shyama/krishna ayas; pottery = Painted Grey Ware.",
        "In the Rigvedic period, **Bali** was —",
        "A **voluntary tribute** offered by the people to the chief; only in Later Vedic times did it become a regular tax.")
    S.pattern("ga-ved-p5", "Upanishad ↔ content; darshana ↔ founder", "common",
        "'Satyameva Jayate is taken from', 'the founder of the Nyaya school', 'Nachiketa appears in'.",
        None,
        "1. Upanishad anchors: Mundaka = 'Satyameva Jayate'; Katha = Nachiketa-Yama; Brihadaranyaka = oldest, Gargi-Yajnavalkya; Chandogya = Krishna Devaki-putra mention.\n2. Darshana founders: Sankhya-Kapila, Yoga-Patanjali, Nyaya-Gautama, Vaisheshika-Kanada, Mimamsa-Jaimini, Vedanta-Badarayana.\n3. All six schools accept Vedic authority — that is what 'orthodox (astika)' means.",
        "The philosophical school of **Vaisheshika**, known for its atomic theory, was founded by —",
        "**Kanada** (also called Uluka). The Nyaya school of logic was founded by Gautama (Akshapada).")

    S.q("ga-ved-p1", "easy", "Which Veda is regarded as the **root of Indian music**, its hymns being set to melody?",
        ["Rigveda", "Samaveda", "Yajurveda", "Atharvaveda"], "Samaveda",
        "The **Samaveda** ('Veda of melodies') sets Rigvedic hymns to music; its reciting priest is the **Udgatri**. Its upaveda is Gandharvaveda.",
        "Sama = sur (melody).", 20)
    S.q("ga-ved-p1", "medium", "**Dhanurveda**, the upaveda of archery/warfare, is attached to which Veda?",
        ["Rigveda", "Samaveda", "Yajurveda", "Atharvaveda"], "Yajurveda",
        "Upaveda pairs: Rig-Ayurveda, Sama-Gandharvaveda, **Yajur-Dhanurveda**, Atharva-Shilpaveda.",
        "Yajur is the sacrificial Veda — war formulas fit it.", 25)
    S.q("ga-ved-p2", "easy", "The **Battle of Ten Kings (Dasarajna)** of Rigvedic tradition was fought on the river —",
        ["Vitasta", "Parushni", "Vipas", "Sutudri"], "Parushni",
        "The Dasarajna (Mandala VII) was fought on the **Parushni = Ravi**. **Sudas** of the Bharata clan defeated a confederacy of ten kings.",
        "Parushni = Ravi = 'battle river'.", 20)
    S.q("ga-ved-p2", "medium", "To which deity are the **largest number of Rigvedic hymns** addressed?",
        ["Agni", "Varuna", "Indra", "Soma"], "Indra",
        "**Indra** (~250 hymns; called *Purandara*, breaker of forts) leads, followed by **Agni** (~200). Varuna guards cosmic order (rita); Soma has Mandala IX.",
        "Indra first, Agni second — keep the order.", 20)
    S.q("ga-ved-p2", "medium", "The **Purusha Sukta**, which gives the first mention of the four varnas, occurs in —",
        ["Mandala II", "Mandala VII", "Mandala IX", "Mandala X"], "Mandala X",
        "The Purusha Sukta is in **Mandala X**, the last book of the Rigveda. It describes the four varnas emerging from the sacrifice of primeval Purusha.",
        "Anchors 3-7-9-10: Gayatri, Ten Kings, Soma, Purusha.", 20)
    S.q("ga-ved-p3", "medium", "The Rigvedic river **Asikni** is the modern —",
        ["Jhelum", "Chenab", "Ravi", "Beas"], "Chenab",
        "**Asikni = Chenab**. Full chain: Vitasta-Jhelum, Asikni-Chenab, Parushni-Ravi, Vipas-Beas, Sutudri-Sutlej.",
        "Second in both chains (V-A-P-V-S and J-C-R-B-S) → Chenab.", 25)
    S.q("ga-ved-p3", "hard", "Which Rigvedic name corresponds to the modern river **Beas**?",
        ["Sutudri", "Vipas", "Kubha", "Drishadvati"], "Vipas",
        "**Vipas = Beas** — the river beyond which Alexander's army later refused to march (Hyphasis). Sutudri = Sutlej; Kubha = Kabul; Drishadvati = Ghaggar-Chautang.",
        "Vipas ↔ Beas — both short names in the middle of the chain.", 25)
    S.q("ga-ved-p4", "easy", "The use of **iron** first appears in India during the —",
        ["Harappan age", "Early Vedic period", "Later Vedic period", "Mauryan period"], "Later Vedic period",
        "Iron (*shyama ayas* or *krishna ayas*, 'dark metal') appears in Later Vedic texts (c. 1000–600 BCE) and helped clear the doab forests for farming. The Harappans had no iron.",
        "Iron = Later Vedic = Painted Grey Ware.", 20)
    S.q("ga-ved-p4", "medium", "Which assembly of the Rigvedic period is considered the **oldest**?",
        ["Sabha", "Samiti", "Vidatha", "Paura"], "Vidatha",
        "**Vidatha** is regarded as the oldest tribal assembly; it also handled religious and distributive functions. The Atharvaveda calls Sabha and Samiti 'two daughters of Prajapati'.",
        "V for Vintage — Vidatha is the oldest.", 25)
    S.q("ga-ved-p5", "easy", "The national motto **'Satyameva Jayate'** is taken from —",
        ["Rigveda", "Mundaka Upanishad", "Bhagavad Gita", "Manusmriti"], "Mundaka Upanishad",
        "'Satyameva Jayate' ('truth alone triumphs') is the closing line of the **Mundaka Upanishad** and appears below the Lion Capital in the national emblem.",
        "Motto = Mundaka (both M).", 20)
    S.q("ga-ved-p5", "medium", "The dialogue between **Nachiketa and Yama**, the god of death, occurs in the —",
        ["Kena Upanishad", "Katha Upanishad", "Isa Upanishad", "Mandukya Upanishad"], "Katha Upanishad",
        "The **Katha Upanishad** is built around young Nachiketa's questions to Yama about death and the soul. The Brihadaranyaka Upanishad has the Yajnavalkya-Gargi debate.",
        "Katha = Kahani of Nachiketa.", 25)
    S.q("ga-ved-p5", "hard", "Match the school of philosophy with its founder:\n1. Sankhya  2. Nyaya  3. Purva Mimamsa\nWhich is correctly matched with **Kapila, Gautama and Jaimini** respectively?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are right: **Sankhya-Kapila, Nyaya-Gautama (Akshapada), Purva Mimamsa-Jaimini**. The full set: Yoga-Patanjali, Vaisheshika-Kanada, Vedanta-Badarayana.",
        "Darshana first letters: Kapila-Sankhya, Kanada-Vaisheshika, Jaimini-Mimamsa.", 30)
    return S


def build_maha():
    S = Sub("mahajanapadas")
    S.notes = """### From tribes to territories
By the 6th century BCE (the age of the Buddha and Mahavira), north India had moved from tribe-based society to **territorial states**. The Buddhist text **Anguttara Nikaya** lists **16 mahajanapadas** (great kingdoms/republics); the Jain *Bhagavati Sutra* gives a slightly different list. Settled agriculture, iron tools and rising trade made bigger states possible, and a new **punch-marked silver coinage** made taxes and trade easier.

### The sixteen — the ones exams ask
| Mahajanapada | Capital | Note |
|---|---|---|
| Magadha | Girivraja (Rajagriha), later Pataliputra | Became the empire of the age |
| Anga | Champa | Annexed by Bimbisara |
| Kosala | Shravasti (also Ayodhya) | Fought Magadha over Kashi |
| Kashi | Varanasi | Absorbed by Kosala/Magadha |
| Vajji | Vaishali | Republic of 8 clans incl. Licchavis |
| Malla | Kushinara, Pava | Republic; Buddha died here |
| Vatsa | Kaushambi | King Udayana of legend |
| Kuru | Indraprastha | — |
| Panchala | Ahichchhatra, Kampilya | — |
| Matsya | Viratnagar | Jaipur-Alwar region |
| Surasena | Mathura | — |
| Chedi | Shuktimati | Bundelkhand |
| Avanti | Ujjain (N), Mahishmati (S) | Malwa; rival of Magadha |
| Assaka (Ashmaka) | Potana | **Only one south of the Vindhyas** |
| Gandhara | Taxila | North-west |
| Kamboja | Rajapura | Noted for horses |

### Why Magadha won
The four great powers of the day were **Magadha, Kosala, Vatsa and Avanti**. Magadha beat all of them because it had: (1) **iron ores** (south Bihar) for weapons and ploughs; (2) the fertile, rain-fed **middle Ganga plain**; (3) **elephants** from the forests for the army; (4) cheap river transport; and (5) naturally defended capitals (Rajagriha ringed by five hills, then Pataliputra girt by rivers). Ambitious, unorthodox rulers also helped — Magadha did not care for the old rules of 'righteous' war.

### The Magadhan dynasties in order
| Dynasty | Rulers and events |
|---|---|
| **Haryanka** | **Bimbisara** — contemporary of **both Buddha and Mahavira**; marriage alliances; annexed Anga; capital Rajagriha. **Ajatashatru** — killed his father; defeated the Vajji confederacy (after 16 years of war); **First Buddhist Council** held under him. **Udayin** — founded **Pataliputra** at the Ganga–Son confluence |
| **Shishunaga** | **Shishunaga** — finally destroyed **Avanti** (its old rival). **Kalashoka** — shifted capital to Pataliputra; **Second Buddhist Council** at Vaishali under him |
| **Nanda** | **Mahapadma Nanda** — 'first empire builder', called *Ekarat* (sole sovereign) and *Sarvakshatrantaka* (destroyer of Kshatriyas); a low-born (non-Kshatriya) ruler. **Dhana Nanda** — last Nanda; contemporary of **Alexander**; overthrown by Chandragupta Maurya with Chanakya |

### Foreign intrusions of the same era
- **Persians (Achaemenids):** Darius I (c. 516 BCE) annexed Sind, Gandhara and western Punjab. Persian contact brought the **Kharosthi script** (written right to left) used in some Ashokan edicts.
- **Alexander of Macedon (326 BCE):** crossed the Indus, defeated **Porus (Puru)** at the **Battle of the Hydaspes (Jhelum)** — but was so impressed by Porus that he restored his kingdom. At the **Beas (Hyphasis)** his war-weary troops **refused to march further** east (fear of the mighty Nanda army). Alexander went back and died at Babylon in 323 BCE. His invasion opened the land route to Europe and Greek accounts of India.

### Quick revision
- Source list of 16 mahajanapadas: **Anguttara Nikaya** (Buddhist).
- Capital pairs to master: Avanti-Ujjain, Vatsa-Kaushambi, Kosala-Shravasti, Anga-Champa, Gandhara-Taxila, Matsya-Viratnagar.
- Assaka = only mahajanapada **south of the Vindhyas**.
- Dynasty chain: **Haryanka → Shishunaga → Nanda → Maurya**.
- Bimbisara (contemporary of Buddha and Mahavira) → Ajatashatru (1st Council) → Udayin (founded Pataliputra) → Shishunaga (ended Avanti) → Kalashoka (2nd Council) → Mahapadma Nanda (Ekarat) → Dhana Nanda (last).
- Persians under Darius I brought Kharosthi; Alexander beat Porus at the Jhelum (326 BCE) and stopped at the Beas."""
    S.pattern("ga-mah-p1", "Mahajanapada ↔ capital", "very common",
        "A capital or mahajanapada given with four options, or 'which pair is correctly matched'.",
        None,
        "1. Master the six traps: Avanti-Ujjain, Vatsa-Kaushambi, Kosala-Shravasti, Anga-Champa, Gandhara-Taxila, Matsya-Viratnagar.\n2. Republics had cities, not 'capitals' in the royal sense: Vajji-Vaishali, Malla-Kushinara/Pava.\n3. Magadha had two capitals in sequence: Rajagriha (Girivraja), then Pataliputra from Udayin's time.",
        "The capital of the Vatsa mahajanapada was —",
        "**Kaushambi**, near present-day Prayagraj in UP; its famous king was Udayana.")
    S.pattern("ga-mah-p2", "Magadhan dynasty ↔ ruler and event", "very common",
        "'Who founded Pataliputra?', 'under which dynasty was the Second Council held?', ordering of Haryanka-Shishunaga-Nanda rulers.",
        None,
        "1. Dynasty chain: **Haryanka (Bimbisara, Ajatashatru, Udayin) → Shishunaga (Shishunaga, Kalashoka) → Nanda (Mahapadma, Dhana)**.\n2. Anchor events: Bimbisara annexed Anga; Ajatashatru beat the Vajjis + 1st Council; Udayin founded Pataliputra; Shishunaga destroyed Avanti; Kalashoka 2nd Council; Mahapadma Nanda = Ekarat; Dhana Nanda met Alexander.\n3. Council hooks: councils 1-2 go with Ajatashatru (Haryanka) and Kalashoka (Shishunaga).",
        "Who founded **Pataliputra** on the confluence of the Ganga and the Son?",
        "**Udayin**, the Haryanka successor of Ajatashatru. The earlier capital was Rajagriha (Girivraha).")
    S.pattern("ga-mah-p3", "Sixteen mahajanapadas — source text and odd facts", "common",
        "'The list of 16 mahajanapadas occurs in', 'which mahajanapada was a republic', 'the only one south of the Vindhyas'.",
        None,
        "1. Source: **Anguttara Nikaya** (Buddhist); Jain list (Bhagavati Sutra) differs.\n2. Republics (gana-sanghas): **Vajji** (with Licchavis) and **Malla**; also later Shakya and Licchavi clans.\n3. Geography extremes: Assaka south of the Vindhyas; Kamboja farthest north-west, famous for horses.",
        "The list of sixteen mahajanapadas appears in which Buddhist text?",
        "The **Anguttara Nikaya**, part of the Sutta Pitaka. The Jain Bhagavati Sutra gives a different list of sixteen.")
    S.pattern("ga-mah-p4", "Persian and Alexander's invasions", "common",
        "Questions on Darius I, Kharosthi script, the Hydaspes battle with Porus, the mutiny at the Beas.",
        None,
        "1. Persians: **Darius I, c. 516 BCE** annexed Gandhara/west Punjab; gift to India = the **Kharosthi script** (right to left).\n2. Alexander, **326 BCE**: crossed the Indus; **beat Porus at the Hydaspes (Jhelum)** and restored him.\n3. Mutiny at the **Beas (Hyphasis)** — not the Jhelum; died at Babylon **323 BCE**.",
        "Alexander's army refused to march beyond which river?",
        "The **Beas (Hyphasis)** — the soldiers, tired and hearing of the vast Nanda army beyond, mutinied and forced the return march.")

    S.q("ga-mah-p1", "easy", "The capital of the **Kosala** mahajanapada was —",
        ["Kaushambi", "Shravasti", "Champa", "Ujjain"], "Shravasti",
        "**Shravasti** (Sahet-Mahet, UP) was Kosala's chief city; its king Prasenajit was a contemporary of the Buddha. Kaushambi = Vatsa; Champa = Anga; Ujjain = Avanti.",
        "Kosala-Shravasti, Vatsa-Kaushambi — don't swap.", 20)
    S.q("ga-mah-p1", "medium", "Which of the following pairs is correctly matched?",
        ["Gandhara — Kapilavastu", "Avanti — Mahishmati", "Matsya — Champa", "Anga — Viratnagar"], "Avanti — Mahishmati",
        "Avanti had two capitals — **Ujjain** (north) and **Mahishmati** (south). Gandhara's capital was Taxila, Matsya's was Viratnagar, Anga's was Champa.",
        "Check every pair against the six-trap list.", 25)
    S.q("ga-mah-p1", "medium", "The mahajanapada whose capital was **Taxila** was —",
        ["Kamboja", "Kuru", "Gandhara", "Panchala"], "Gandhara",
        "**Gandhara** (Rawalpindi-Peshawar region) had **Taxila** as its capital — later famous as a seat of learning. Kamboja lay further north; its capital was Rajapura.",
        "Taxila sits on the GT road's north-west end → Gandhara.", 20)
    S.q("ga-mah-p2", "easy", "Which Magadha ruler was a **contemporary of both the Buddha and Mahavira**?",
        ["Ajatashatru", "Bimbisara", "Udayin", "Shishunaga"], "Bimbisara",
        "**Bimbisara** (Haryanka dynasty) befriended both teachers, annexed Anga and used marriage alliances to expand Magadha.",
        "B for Both, Bimbisara.", 20)
    S.q("ga-mah-p2", "medium", "The **Second Buddhist Council** at Vaishali was held during the reign of —",
        ["Ajatashatru", "Kalashoka", "Mahapadma Nanda", "Ashoka"], "Kalashoka",
        "The 2nd Council (Vaishali, 383 BCE) was held under **Kalashoka** of the **Shishunaga** dynasty. Ajatashatru (Haryanka) had hosted the 1st at Rajagriha; Ashoka the 3rd at Pataliputra.",
        "Kings A-K-A-K; 2nd = K = Kalashoka.", 25)
    S.q("ga-mah-p2", "medium", "Which ruler is described by the titles **'Ekarat' and 'Sarvakshatrantaka'**?",
        ["Bimbisara", "Mahapadma Nanda", "Dhana Nanda", "Chandragupta Maurya"], "Mahapadma Nanda",
        "**Mahapadma Nanda**, founder of the Nanda dynasty, was called *Ekarat* ('sole sovereign') and *Sarvakshatrantaka* ('destroyer of all Kshatriyas'); he is regarded as the first great non-Kshatriya empire builder.",
        "Nanda = the 'destroyer of Kshatriyas' titles.", 25)
    S.q("ga-mah-p2", "hard", "Arrange in order of rule in Magadha:\n1. Kalashoka  2. Ajatashatru  3. Dhana Nanda  4. Udayin",
        ["2, 4, 1, 3", "4, 2, 1, 3", "2, 1, 4, 3", "1, 2, 3, 4"], "2, 4, 1, 3",
        "Ajatashatru (Haryanka) → Udayin (Haryanka, founded Pataliputra) → Kalashoka (Shishunaga) → Dhana Nanda (last Nanda).",
        "Chain: Hari(Hari) - Shishu - Nanda; Ajatashatru before Udayin.", 30)
    S.q("ga-mah-p3", "easy", "Which one of the sixteen mahajanapadas lay **south of the Vindhyas**?",
        ["Avanti", "Assaka (Ashmaka)", "Chedi", "Matsya"], "Assaka (Ashmaka)",
        "**Assaka (Ashmaka)**, on the Godavari with capital Potana (Potali), was the only mahajanapada south of the Vindhyas. Avanti (Malwa) is north of the range.",
        "South = the odd southern one, Assaka.", 20)
    S.q("ga-mah-p3", "medium", "Which two mahajanapadas were ruled as **republics (gana-sanghas)**?",
        ["Magadha and Anga", "Vajji and Malla", "Kashi and Kosala", "Avanti and Vatsa"], "Vajji and Malla",
        "**Vajji** (a confederacy of eight clans, the best-known being the **Licchavis** of Vaishali) and **Malla** (Kushinara-Pava) were republics; Buddha died in Malla territory.",
        "Republics = Vajji + Malla, both in Bihar-UP belt.", 25)
    S.q("ga-mah-p3", "medium", "The mahajanapada famous for its **horses** in the far north-west was —",
        ["Gandhara", "Kamboja", "Kuru", "Panchala"], "Kamboja",
        "**Kamboja** (capital Rajapura) was renowned for its horses. Gandhara, its neighbour, was famous for Taxila and trade.",
        "Kamboja = cavalry of the 16.", 25)
    S.q("ga-mah-p4", "easy", "Alexander defeated **Porus** at the Battle of the Hydaspes. The Hydaspes is the modern river —",
        ["Beas", "Ravi", "Jhelum", "Chenab"], "Jhelum",
        "The **Hydaspes = Jhelum (Vitasta)**; the battle took place in **326 BCE**. Alexander restored Porus to his kingdom after the battle.",
        "Hydaspes = Jhelum; mutiny at Beas.", 20)
    S.q("ga-mah-p4", "medium", "The **Kharosthi script**, used in some north-western Ashokan edicts, entered India through contact with —",
        ["Greeks", "Persians (Achaemenids)", "Scythians", "Kushanas"], "Persians (Achaemenids)",
        "After **Darius I** annexed Gandhara and Sind (c. 516 BCE), the Aramaic-based **Kharosthi** script (written right to left) came into use in the north-west; Ashoka used it at Shahbazgarhi and Mansehra.",
        "Kharosthi = Persian gift.", 25)
    S.q("ga-mah-p4", "hard", "Consider the statements about Alexander's invasion (326 BCE):\n1. He fought Porus on the banks of the Jhelum.\n2. His army mutinied at the Beas.\n3. He annexed Magadha before returning.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is wrong — Alexander **never entered Magadha**; the mutiny at the Beas turned the army back, and he died at Babylon in 323 BCE.",
        "The Beas mutiny is the 'turn-back' point — no Magadha for Alexander.", 30)
    return S


def build_buddh():
    S = Sub("buddhism-jainism")
    S.notes = """### Two protest faiths of the 6th century BCE
Buddhism and Jainism began in the same age, in the same belt (Magadha-Vaishali), and for similar reasons: rising taxes and animal sacrifice in ritual religion, Sanskrit scriptures closed to ordinary people, and a new trading class (sethis) looking for simpler, ethical faiths. Both rejected Vedic ritual's authority, preached **ahimsa** and used the people's language (**Pali** for early Buddhism, **Prakrit/Ardhamagadhi** for Jainism). Both were supported by kings and merchants alike.

### The life of the Buddha — five stations
| Event | Place | Symbol |
|---|---|---|
| Birth (563 BCE, traditional) | **Lumbini** (Nepal) | Lotus & bull |
| Renunciation (Mahabhinishkramana, age 29) | Left Kapilavastu on horse Kanthaka with charioteer Channa | Horse |
| Enlightenment (age 35) | **Bodh Gaya**, under the Bodhi tree by the Niranjana (Falgu) | Bodhi tree |
| First sermon (Dharmachakra-pravartana) | **Sarnath** (Deer Park) | Wheel |
| Death (Mahaparinirvana, age 80) | **Kushinagar** (Malla republic) | Stupa |

Born a **Shakya** prince (father Suddhodana, mother Mahamaya), he married Yashodhara (son Rahul). The teaching: **Four Noble Truths** (the world is sorrow; desire causes sorrow; sorrow can end; the Eightfold Path ends it) and the **Eightfold Path** — the **Middle Path** between luxury and severe austerity. **Tri-ratna** of Buddhism: Buddha, Dhamma, Sangha. Teachings were compiled in **Pali** into the **Tripitaka** — *Vinaya Pitaka* (monastic rules), *Sutta Pitaka* (discourses), *Abhidhamma Pitaka* (philosophy). The **Jatakas** are stories of the Buddha's former births.

### The four Buddhist Councils
| Council | Place | King | President | Result |
|---|---|---|---|---|
| 1st (483 BCE) | Rajagriha (Saptaparni cave) | Ajatashatru | Mahakassapa | Sutta (Ananda) & Vinaya (Upali) compiled |
| 2nd (383 BCE) | Vaishali | Kalashoka | Sabakami | Split: Sthaviravadins vs Mahasanghikas |
| 3rd (250 BCE) | Pataliputra | Ashoka | Moggaliputta Tissa | Abhidhamma Pitaka added; missions sent |
| 4th (c. 72 CE) | Kundalvana, Kashmir | Kanishka | Vasumitra (deputy Ashvaghosha) | Split into Hinayana & Mahayana |

Learn the chains: places **Raj-Vaish-Pat-Kash**, kings **A-K-A-K**, presidents **Maha-Saba-Moggali-Vasu**.

### Jainism — the 24 Tirthankaras
Jainism claims **24 Tirthankaras** (ford-makers). The exam set: **1st Rishabhanatha (Adinatha, symbol bull)**; 22nd Neminatha (conch); **23rd Parshvanatha** (prince of Varanasi, son of Ashvasena; symbol snake; gave **four vows** — ahimsa, satya, asteya, aparigraha); **24th Vardhamana Mahavira** (symbol lion).

**Mahavira** (traditional 540–468 BCE) was born at **Kundagrama** near Vaishali (father Siddhartha of the Jnatrika clan; mother Trishala, sister of the Licchavi chief Chetaka). He attained **kaivalya** (omniscience) at 42 under a sal tree at Jrimbhikagrama and died at **Pavapuri** at 72. He **added the fifth vow, Brahmacharya**. His titles: *Jina* (conqueror — hence 'Jain'), *Nirgrantha* (free of bonds). The **Tri-ratna of Jainism** is Right Faith, Right Knowledge, Right Conduct.

**Sects:** after the great famine, **Digambaras** (sky-clad; leader **Bhadrabahu**, who went south with Chandragupta Maurya) vs **Shvetambaras** (white-clad; **Sthulabhadra**). **Councils:** 1st at **Pataliputra** (c. 300 BCE, Sthulabhadra; 12 Angas compiled), 2nd at **Vallabhi** (Gujarat, 5th–6th century CE, **Devarddhi**; canon written down). The *Kalpasutra* is attributed to Bhadrabahu.

### Texts, sects and monuments
- **Milindapanha** — dialogue of Indo-Greek king **Menander (Milinda)** with the monk **Nagasena**.
- **Mahayana** philosopher **Nagarjuna** (Madhyamika school); future Buddha **Maitreya**; Padmapani = Avalokiteshvara.
- Monuments: **Gommateshwara (Bahubali)** statue, **Shravanabelagola** (Karnataka, c. 983 CE, built by Chamundaraya, minister of the Western Ganga kings; Mahamastakabhisheka every 12 years); **Dilwara** Jain temples, Mount Abu.
- Monasteries: **Nalanda** (founded by Gupta king **Kumaragupta I**), **Vikramashila** (Pala king **Dharmapala**), **Odantapuri** (Pala king Gopala).

### Quick revision
- Life chain: Lumbini → (renunciation) → Bodh Gaya → Sarnath → Kushinagar; symbols lotus-horse-tree-wheel-stupa.
- Councils: Rajagriha, Vaishali, Pataliputra, Kashmir; kings A-K-A-K; presidents Maha-Saba-Moggali-Vasu.
- 4th Council (Kanishka) = Hinayana/Mahayana split; 2nd = Sthaviravada/Mahasanghika split.
- Tirthankaras: 1 bull, 22 conch, 23 snake (Parshva, 4 vows), 24 lion (Mahavira, added 5th vow).
- Jain sects Digambara/Shvetambara; councils Pataliputra & Vallabhi; Gommateshwara at Shravanabelagola.
- Nalanda = Kumaragupta I (Gupta); Vikramashila = Dharmapala (Pala)."""
    S.pattern("ga-bud-p1", "Buddha's life events ↔ places and symbols", "very common",
        "'Where did the Buddha attain enlightenment?', 'the symbol of Mahaparinirvana', ordering of life events.",
        None,
        "1. Life chain: Lumbini (birth) → renunciation (age 29) → Bodh Gaya (enlightenment, 35) → Sarnath (first sermon) → Kushinagar (death, 80).\n2. Symbols in order: lotus-bull, horse, Bodhi tree, wheel, stupa.\n3. River and helpers: Niranjana (Falgu) at Bodh Gaya; horse Kanthaka, charioteer Channa; wife Yashodhara, son Rahul.",
        "Where did Gautama Buddha attain **Mahaparinirvana**?",
        "At **Kushinagar** (Kasia, UP), in the territory of the Malla republic, at the age of 80.")
    S.pattern("ga-bud-p2", "Buddhist councils ↔ place, king, president, outcome", "very common",
        "'The Fourth Council was held under…', 'which council added the Abhidhamma Pitaka', matching council-president pairs.",
        None,
        "1. Places: Rajagriha → Vaishali → Pataliputra → Kashmir (Kundalvana).\n2. Kings: Ajatashatru → Kalashoka → Ashoka → Kanishka (A-K-A-K).\n3. Presidents: Mahakassapa → Sabakami → Moggaliputta Tissa → Vasumitra (Maha-Saba-Moggali-Vasu).\n4. Outcomes: 2nd = first split (Sthaviravada/Mahasanghika); 3rd = Abhidhamma added; 4th = Hinayana/Mahayana split.",
        "Which Buddhist council resulted in the split into **Hinayana and Mahayana**?",
        "The **Fourth Council** (c. 72 CE, Kundalvana, Kashmir) under **Kanishka**, with **Vasumitra** as president and **Ashvaghosha** as deputy.")
    S.pattern("ga-bud-p3", "Jainism: Tirthankaras, Mahavira's life and vows", "common",
        "'Who was the 23rd Tirthankara', 'which vow was added by Mahavira', 'Mahavira attained kaivalya at'.",
        None,
        "1. Number set: 1 Rishabha (bull), 22 Neminatha (conch), 23 Parshvanatha (snake, four vows), 24 Mahavira (lion).\n2. Mahavira's chain: Kundagrama birth → kaivalya at 42 (Jrimbhikagrama, Rijupalika river) → death at Pavapuri at 72.\n3. Vows: Parshva gave four (ahimsa, satya, asteya, aparigraha); Mahavira **added Brahmacharya** (celibacy) as the fifth.",
        "Which vow of Jainism was **added by Mahavira** to the four preached by Parshvanatha?",
        "**Brahmacharya** (celibacy). The four older vows were ahimsa, satya, asteya and aparigraha.")
    S.pattern("ga-bud-p4", "Buddhist/Jain texts, sects and monuments", "common",
        "'Milindapanha is a dialogue between', 'Gommateshwara statue is at', 'Vikramashila was founded by', Digambara vs Shvetambara.",
        None,
        "1. Texts: Tripitaka (Vinaya, Sutta, Abhidhamma), Jatakas (previous births), Milindapanha (Menander-Nagasena), Buddhacharita (Ashvaghosha).\n2. Jain monuments: Gommateshwara at Shravanabelagola (Chamundaraya, c. 983 CE); Dilwara temples, Mount Abu.\n3. Monasteries: Nalanda = Kumaragupta I (Gupta); Vikramashila = Dharmapala (Pala); Odantapuri = Gopala (Pala).",
        "The *Milindapanha* records a dialogue between the monk Nagasena and which king?",
        "The Indo-Greek king **Menander (Milinda)**, who ruled from Sakala (Sialkot).")

    S.q("ga-bud-p1", "easy", "Gautama Buddha attained **enlightenment** at —",
        ["Sarnath", "Lumbini", "Bodh Gaya", "Kushinagar"], "Bodh Gaya",
        "Enlightenment came at **Bodh Gaya** (Bihar) under the pipal (Bodhi) tree on the bank of the Niranjana (Falgu) river, at age 35. Sarnath = first sermon; Lumbini = birth; Kushinagar = death.",
        "Life order L-B-S-K: Lumbini, Bodh Gaya, Sarnath, Kushinagar.", 20)
    S.q("ga-bud-p1", "medium", "Which **symbol** is associated with the Buddha's first sermon at Sarnath?",
        ["Bodhi tree", "Wheel (Dharmachakra)", "Lotus", "Horse"], "Wheel (Dharmachakra)",
        "The first sermon is called **Dharmachakra-pravartana** ('turning of the wheel of law'), so its symbol is the **wheel** — seen on the Sarnath Lion Capital.",
        "Wheel = sermon; tree = enlightenment; stupa = death.", 20)
    S.q("ga-bud-p1", "hard", "At the time of his **Great Renunciation**, the Buddha left home on the horse —",
        ["Kanthaka, with charioteer Channa", "Kanthaka, with charioteer Vasudeva", "Mangala, with charioteer Channa", "Chetak, with charioteer Channa"], "Kanthaka, with charioteer Channa",
        "Prince Siddhartha left Kapilavastu on his horse **Kanthaka** with his charioteer **Channa** (who later joined the Sangha).",
        "Kanthaka-Channa is the fixed pair.", 25)
    S.q("ga-bud-p2", "medium", "The **Third Buddhist Council** (250 BCE, Pataliputra) is remembered for —",
        ["The first split of the Sangha", "Adding the Abhidhamma Pitaka to the canon", "The split into Hinayana and Mahayana", "Writing down the canon in Pali"], "Adding the Abhidhamma Pitaka to the canon",
        "Under **Ashoka**, with **Moggaliputta Tissa** presiding, the **Abhidhamma Pitaka** was added, completing the Tripitaka, and missions were sent abroad (e.g. Mahendra-Sanghamitra to Sri Lanka).",
        "3rd = Abhidhamma; 4th = Mahayana split.", 25)
    S.q("ga-bud-p2", "medium", "The **First Buddhist Council** was presided over by —",
        ["Ananda", "Upali", "Mahakassapa", "Sabakami"], "Mahakassapa",
        "**Mahakassapa** presided at Rajagriha (483 BCE) under Ajatashatru; within it, **Ananda** recited the Suttas and **Upali** the Vinaya rules.",
        "President Maha; reciters Ananda (Sutta) and Upali (Vinaya).", 25)
    S.q("ga-bud-p2", "hard", "Arrange the councils chronologically and pick the correct set of kings:\n1. Vaishali  2. Pataliputra  3. Rajagriha  4. Kashmir",
        ["3, 1, 2, 4 — Ajatashatru, Kalashoka, Ashoka, Kanishka", "1, 2, 3, 4 — Ajatashatru, Ashoka, Kalashoka, Kanishka", "3, 2, 1, 4 — Kalashoka, Ashoka, Ajatashatru, Kanishka", "3, 1, 4, 2 — Ajatashatru, Kalashoka, Kanishka, Ashoka"], "3, 1, 2, 4 — Ajatashatru, Kalashoka, Ashoka, Kanishka",
        "Councils: Rajagriha (483 BCE) → Vaishali (383 BCE) → Pataliputra (250 BCE) → Kashmir (c. 72 CE); kings Ajatashatru → Kalashoka → Ashoka → Kanishka (A-K-A-K).",
        "Places Raj-Vaish-Pat-Kash and kings A-K-A-K march together.", 35)
    S.q("ga-bud-p3", "easy", "The **first** Tirthankara of Jainism was —",
        ["Parshvanatha", "Rishabhanatha (Adinatha)", "Neminatha", "Mahavira"], "Rishabhanatha (Adinatha)",
        "**Rishabhanatha (Adinatha)**, symbol the **bull**, is the first of the 24 Tirthankaras. Mahavira is the 24th and last.",
        "1 bull — 24 lion.", 20)
    S.q("ga-bud-p3", "medium", "Mahavira passed away at the age of 72 at —",
        ["Kundagrama", "Jrimbhikagrama", "Pavapuri", "Vaishali"], "Pavapuri",
        "Mahavira attained **nirvana at Pavapuri** (near Rajgir, Bihar), at age 72. Kundagrama = birthplace; Jrimbhikagrama = where he attained kaivalya at 42.",
        "Kaivalya 42 (Jrimbhika) → death 72 (Pavapuri).", 25)
    S.q("ga-bud-p3", "medium", "Mahavira belonged to which **clan**?",
        ["Shakya", "Jnatrika", "Licchavi", "Malla"], "Jnatrika",
        "Mahavira was a prince of the **Jnatrika** clan; his mother **Trishala** was a Licchavi princess (sister of chief Chetaka). The Buddha belonged to the Shakya clan.",
        "Buddha-Shakya, Mahavira-Jnatrika.", 25)
    S.q("ga-bud-p4", "medium", "The **Gommateshwara (Bahubali)** monolith at Shravanabelagola was installed by —",
        ["Chandragupta Maurya", "Bhadrabahu", "Chamundaraya", "Kharavela"], "Chamundaraya",
        "**Chamundaraya**, minister of the Western Ganga kings, installed the 57-foot statue (c. 983 CE); the **Mahamastakabhisheka** bath festival is held every 12 years.",
        "Minister-Chamundaraya, not a king.", 25)
    S.q("ga-bud-p4", "medium", "The **Vallabhi council** of Jainism, where the canon was finally written down, was held in —",
        ["Bihar", "Gujarat", "Karnataka", "Odisha"], "Gujarat",
        "The second Jain council met at **Vallabhi (Gujarat)** in the 5th–6th century CE under **Devarddhi Kshamasramana**; the first (c. 300 BCE, Pataliputra, Sthulabhadra) had compiled the 12 Angas.",
        "Jain councils: Pataliputra → Vallabhi (Gujarat).", 25)
    S.q("ga-bud-p4", "hard", "The Buddhist monastery **Vikramashila** was founded by —",
        ["Kumaragupta I", "Gopala", "Dharmapala", "Kanishka"], "Dharmapala",
        "**Dharmapala** of the Pala dynasty founded Vikramashila (Bhagalpur, Bihar). Nalanda was founded by the Gupta **Kumaragupta I**; Odantapuri by the Pala **Gopala**.",
        "Nalanda-Gupta, Vikramashila/Odantapuri-Pala.", 30)
    return S
