"""Ancient History part 1: Indus Valley and Vedic Age."""
from _ah_common import pat, trick, mk

S = {}

# ---------------------------------------------------------------- indus-valley
S["indus-valley"] = dict(
    concept=(
        "The Harappan civilisation is India's oldest city culture. It used copper and bronze but no iron. "
        "Its towns had grid streets, covered drains and burnt bricks. "
        "Exams ask which site is famous for which find, where each site lies, and who dug it."
    ),
    notes=r"""### How it was found
Harappa was dug first, in **1921**, by **Daya Ram Sahni**. It lies on the **Ravi** in Punjab, Pakistan.

**Mohenjo-daro** ("mound of the dead") was dug in **1922** by **R.D. Banerji**. It lies on the **Indus** in Sindh.

**Sir John Marshall** announced the new civilisation in 1924. Because Harappa came first, the correct name is the **Harappan civilisation**.

| Point | Fact |
|---|---|
| Age | Bronze Age (copper and tin) |
| Iron | **Not known** |
| Mature phase | About **2600 to 1900 BCE** |
| Script | Picture signs, still **undeciphered** |

### How the cities were built
Every big city followed one plan. This plan is the most asked fact.

- A raised **citadel** stood in the **west**. It held the rulers' buildings and granaries.
- The **lower town** lay in the **east**. Ordinary people lived there.
- Streets crossed at **right angles**. This is a **grid pattern**.
- Drains ran along the streets and were **covered**.
- Bricks were **burnt**. Their ratio was **1 : 2 : 4**.

> **Tip:** Say "citadel west, town east". Do not reverse it.

The **Great Bath** of Mohenjo-daro is a public tank with steps on two sides. Its lining is waterproof bitumen. The **Great Granary** stood nearby.

### Sites and their finds
Learn each site with its one famous find.

| Site | River and place | Famous find |
|---|---|---|
| **Harappa** | Ravi, Punjab (Pakistan) | Rows of granaries, Cemetery R-37 |
| **Mohenjo-daro** | Indus, Sindh (Pakistan) | Great Bath, Dancing Girl, Pashupati seal |
| **Chanhudaro** | Indus, Sindh | Bead-making workshop; **no citadel** |
| **Lothal** | Bhogava, Gujarat | **Dockyard**, rice husk, fire altars |
| **Kalibangan** | Ghaggar, Rajasthan | **Ploughed field**, fire altars |
| **Banawali** | Ghaggar, Haryana | Clay **plough model**, barley |
| **Dholavira** | Kutch, Gujarat | **Water reservoirs**, 10-letter signboard |
| **Rakhigarhi** | Ghaggar plain, Haryana | **Largest site in India** |
| **Surkotada** | Kutch, Gujarat | Horse bones |
| **Ropar** | Sutlej, Punjab | First site dug after Independence |

> **Watch:** A ploughed **field** is Kalibangan. A clay plough **model** is Banawali.

### The four far corners
| Direction | Site | Place |
|---|---|---|
| North | **Manda** | Chenab, J&K |
| South | **Daimabad** | Pravara, Maharashtra (bronze chariot) |
| East | **Alamgirpur** | Hindon, UP |
| West | **Sutkagendor** | Dasht, Baluchistan |

The memory line is "**M**any **D**onkeys **A**re **S**low". It gives north, south, east, west.

### Who dug which site
| Site | Excavator |
|---|---|
| Harappa | Daya Ram Sahni (1921) |
| Mohenjo-daro | R.D. Banerji (1922) |
| Chanhudaro | N.G. Majumdar (1931) |
| Lothal | S.R. Rao (1954 to 55) |
| Ropar | Y.D. Sharma (1953 to 55) |
| Kalibangan | B.B. Lal and B.K. Thapar (1960s) |
| Dholavira | R.S. Bisht (1990) |

### Farming, trade and craft
- Wheat and barley were the main crops.
- **Cotton** was grown here first. The Greeks later called it *Sindon*.
- Rice husk was found at **Lothal** and **Rangpur**.
- Seals were made of **steatite**. The commonest animal on them is the **unicorn** bull.
- Craftsmen used copper, bronze, gold and silver.

> **Note:** Horse evidence is weak. Only Surkotada has horse bones.

### Belief and script
No temple has been found at any site. People honoured a **Mother Goddess**. A seal shows a cross-legged figure among animals, called **Pashupati** (proto-Shiva). The pipal tree was also sacred. The script runs right to left and nobody can read it.
""",
    tricks=[
        trick("Four corners: Many Donkeys Are Slow",
              "**M**anda is north. **D**aimabad is south. **A**lamgirpur is east. **S**utkagendor is west.",
              "The easternmost Harappan site is:",
              ["Use the line: Many Donkeys Are Slow.", "The third word gives east: Alamgirpur."],
              "Alamgirpur (Hindon, UP)"),
        trick("One site, one find",
              "**Lothal** is the dockyard. **Kalibangan** is the ploughed field. **Mohenjo-daro** is the Great Bath. "
              "**Chanhudaro** is the bead workshop. **Dholavira** is the water reservoirs."),
    ],
    mistakes=[
        mk("Swapping the rivers: Harappa on the Indus, Mohenjo-daro on the Ravi.",
           "Harappa is on the **Ravi**. Mohenjo-daro is on the **Indus**."),
        mk("Mixing Kalibangan and Banawali.",
           "Ploughed **field** is Kalibangan. Clay plough **model** is Banawali."),
        mk("Calling Mohenjo-daro the largest site in India.",
           "Mohenjo-daro and Harappa are in Pakistan. The largest site in India is **Rakhigarhi**."),
        mk("Saying Harappans used iron.",
           "They used copper, bronze, gold and silver. **Iron was unknown**."),
        mk("Choosing sun-dried bricks for the cities.",
           "The cities used **burnt** bricks in the ratio 1 : 2 : 4."),
    ],
    revision=[
        "Harappa 1921 (Daya Ram Sahni). Mohenjo-daro 1922 (R.D. Banerji). Announced by John Marshall in 1924.",
        "Bronze Age, no iron. Burnt bricks 1 : 2 : 4. Grid streets and covered drains.",
        "Citadel in the west, lower town in the east.",
        "Lothal is the dockyard. Kalibangan is the ploughed field. Dholavira has water reservoirs.",
        "Corners: Manda north, Daimabad south, Alamgirpur east, Sutkagendor west.",
        "Rakhigarhi is the largest site in India. The unicorn bull is the commonest seal animal.",
        "No temples found. Mother Goddess and Pashupati seal. Script undeciphered.",
    ],
    patterns=[
        pat("ga-iv-p1", "Harappan site and its signature find", "very common",
            "The question names a find (dockyard, Great Bath, ploughed field, bead workshop) and asks for the site. Or it gives a site and asks for the find.",
            ["Recall the one-site-one-find table.",
             "Watch near pairs: field is Kalibangan, plough model is Banawali.",
             "Great Bath is Mohenjo-daro. Rows of granaries are Harappa.",
             "Cut the options whose famous find you already know."],
            "Exam setters use the same pairs every year, so one table covers most questions.",
            "The Harappan site famous for a bead-making workshop, and the only major city without a citadel, is:",
            ["Beads point to Chanhudaro.", "Chanhudaro is in Sindh, Pakistan."],
            "Chanhudaro (dug by N.G. Majumdar in 1931)"),
        pat("ga-iv-p2", "Site with state or river, and the four corners", "very common",
            "\"In which state is\", \"the northernmost or easternmost site\", or a site-to-river match.",
            ["First split the sites into Pakistan and India.",
             "Pakistan: Harappa, Mohenjo-daro, Chanhudaro, Kot Diji, Sutkagendor.",
             "India by state: Gujarat (Lothal, Dholavira, Surkotada), Haryana (Rakhigarhi, Banawali), Rajasthan (Kalibangan), Punjab (Ropar), UP (Alamgirpur), Maharashtra (Daimabad).",
             "For the corners use Manda, Daimabad, Alamgirpur, Sutkagendor."],
            "Sorting by country and state first removes half the options.",
            "Which Harappan site lies in Hanumangarh district of Rajasthan, on the dry Ghaggar river?",
            ["Rajasthan and Ghaggar point to Kalibangan.", "Its name means \"black bangles\"."],
            "Kalibangan"),
        pat("ga-iv-p3", "Excavator and year", "common",
            "\"Who excavated\", \"discovered in which year\", \"first site dug after Independence\".",
            ["Anchor the dates: Harappa 1921, Mohenjo-daro 1922, announcement 1924.",
             "Match the excavator to the site, not to the whole civilisation.",
             "Later digs: Ropar 1953, Lothal 1954 to 55, Kalibangan 1960s, Dholavira 1990."],
            "The early dates and names are asked most often, so anchor them first.",
            "Mohenjo-daro was excavated in 1922 by:",
            ["Harappa (1921) was dug by Daya Ram Sahni.", "Mohenjo-daro was dug the next year by another officer."],
            "R.D. Banerji"),
        pat("ga-iv-p4", "Town plan, materials and economy", "common",
            "Statement questions on burnt bricks, grid plans, drains, seals, crops or metals.",
            ["Plan: grid streets, covered drains, citadel west, lower town east.",
             "Bricks: burnt, ratio 1 : 2 : 4.",
             "Economy: wheat and barley, first cotton, steatite seals, unicorn bull.",
             "Metals: copper, bronze, gold, silver. Never iron."],
            "Most wrong statements swap one fact, such as burnt bricks for sun-dried bricks.",
            "Statements on Harappan town planning:\n1. Streets crossed at right angles in a grid.\n2. Houses were built mainly of sun-dried bricks.\n3. The citadel lay in the west and the lower town in the east.\nWhich are correct?",
            ["Statement 1 is true.", "Statement 2 is false. The bricks were burnt.", "Statement 3 is true."],
            "1 and 3 only"),
        pat("ga-iv-p5", "Religion, script and society", "occasional",
            "Mother Goddess, Pashupati seal, undeciphered script, burial, or \"which is NOT found\".",
            ["Remember: no temples have been found.",
             "Worship: Mother Goddess, Pashupati seal, pipal tree.",
             "Script: picture signs, right to left, undeciphered.",
             "In \"NOT found\" questions, pick a Vedic god or a temple."],
            "The civilisation is known only from objects, so the questions test what objects exist.",
            "Which of these has NOT been found at Harappan sites?\n(a) Mother Goddess figurines (b) A proto-Shiva seal (c) Temple structures (d) Pipal-tree motifs",
            ["Figurines, seal and pipal motifs are all known.", "No temple building has been found."],
            "(c) Temple structures"),
        pat("ga-iv-p6", "Odd one out or record holder", "common",
            "\"Largest site in India\", \"only city without a citadel\", \"first dug after Independence\", \"UNESCO site\".",
            ["List the record holders: Rakhigarhi largest, Chanhudaro no citadel, Ropar first after Independence, Dholavira UNESCO (2021).",
             "Match the record to the site.",
             "Drop options that are in Pakistan if the question says \"in India\"."],
            "Record titles belong to one site each, so they make easy marks.",
            "Which Harappan site in India is the largest?\n(a) Lothal (b) Rakhigarhi (c) Kalibangan (d) Ropar",
            ["Rakhigarhi is in Hisar district, Haryana.", "It is the largest Harappan site in India."],
            "(b) Rakhigarhi"),
    ],
)

# ---------------------------------------------------------------- vedic-age
S["vedic-age"] = dict(
    concept=(
        "The Vedic age is named after the Vedas, our main source. "
        "Early Vedic life was pastoral and lived around the Punjab rivers. "
        "Later Vedic life used iron, farmed the Ganga-Yamuna doab and had rigid varnas. "
        "Exams ask about the four Vedas, Rigveda mandalas, river names, the Upanishads and the six schools."
    ),
    notes=r"""### Two halves of one age
The Vedic age runs from about **1500 to 600 BCE**. It has two phases.

| Point | Early Vedic (1500 to 1000 BCE) | Later Vedic (1000 to 600 BCE) |
|---|---|---|
| Region | **Sapta Sindhu** (land of seven rivers) | **Ganga-Yamuna doab** |
| Economy | Cattle herding; cattle were wealth | Farming; **iron** appears |
| Pottery | Ochre and plain grey | **Painted Grey Ware** |
| Women | Better position; Sabha was open to them | Position falls; child marriage appears |
| Assemblies | Sabha, Samiti, Vidatha all active | They lose power to the king |
| Officers | Rajan, Purohita, Senani, Gramani | Add Bhagadugha (tax collector), Sangrahitri (treasurer) |
| Bali | Voluntary gift | Regular tax |
| Varna | Flexible | Rigid; gotra exogamy rule |

Iron was called *shyama ayas* or *krishna ayas*, meaning "dark metal".

### The four Vedas
| Veda | Content | Priest |
|---|---|---|
| **Rigveda** | Oldest; 10 mandalas, 1028 hymns | Hotri |
| **Samaveda** | Rigvedic hymns set to melody; root of Indian music | Udgatri |
| **Yajurveda** | Sacrificial formulas in prose and verse | Adhvaryu |
| **Atharvaveda** | Charms, spells, folk medicine | Brahma |

> **Tip:** Say "Rig-Hotri, Sama-Udgatri, Yajur-Adhvaryu, Atharva-Brahma".

Each Veda has later layers: **Brahmanas** (ritual prose), then **Aranyakas** (forest texts), then **Upanishads** (philosophy). Aitareya goes with the Rigveda. Shatapatha goes with the Yajurveda.

The six Vedangas are Shiksha, Kalpa, Vyakarana, Nirukta, Chhanda and Jyotisha.

### Rigveda anchors
Four mandalas are asked again and again.

| Mandala | Content |
|---|---|
| **III** | **Gayatri Mantra**, to **Savitri**, by **Vishwamitra** |
| **VII** | **Battle of Ten Kings** on the Parushni (Ravi); **Sudas** of the Bharatas won |
| **IX** | Wholly to **Soma** |
| **X** | **Purusha Sukta**, the first mention of the four varnas |

**Indra** gets the most hymns (about 250). He is called *Purandara*, the fort-breaker. **Agni** comes next (about 200). **Varuna** guards *rita*, the cosmic order.

The **Sindhu** is the most-named river. The **Saraswati** is the holiest (*naditama*).

> **Watch:** Gayatri Mantra is addressed to Savitri, not to a goddess named Gayatri.

### Rigvedic river names
| Rigvedic | Modern |
|---|---|
| Vitasta | Jhelum |
| Asikni | Chenab |
| Parushni | Ravi |
| Vipas | Beas |
| Sutudri | Sutlej |
| Kubha | Kabul |
| Krumu | Kurram |
| Drishadvati | Ghaggar-Chautang |

The first five run west to east. The modern names follow the same order: Jhelum, Chenab, Ravi, Beas, Sutlej.

### Terms of polity and ritual
- **Sabha** is the council of elders. **Samiti** is the people's assembly. **Vidatha** is the oldest assembly.
- **Gramani** is the village headman. **Bali** is tribute.
- Later Vedic kings held big sacrifices. **Rajasuya** is a consecration. **Ashvamedha** is a horse sacrifice for supremacy. **Vajapeya** is a chariot race.
- The four ashramas are Brahmacharya, Grihastha, Vanaprastha and Sanyasa. The **Jabala Upanishad** lists all four.

### Upanishads and six schools
| Upanishad | Remember for |
|---|---|
| **Mundaka** | "Satyameva Jayate" |
| **Katha** | Nachiketa and Yama |
| **Brihadaranyaka** | Oldest and largest; Yajnavalkya and Gargi |
| **Chandogya** | Early mention of Krishna, son of Devaki |

| School | Founder |
|---|---|
| Sankhya | Kapila |
| Yoga | Patanjali |
| Nyaya | Gautama (Akshapada) |
| Vaisheshika | Kanada |
| Purva Mimamsa | Jaimini |
| Uttara Mimamsa (Vedanta) | Badarayana |
""",
    tricks=[
        trick("Punjab rivers: Very Angry Parrots Visit Sutlej",
              "**V**itasta is Jhelum, **A**sikni is Chenab, **P**arushni is Ravi, **V**ipas is Beas, **S**utudri is Sutlej. "
              "Modern order: J-C-R-B-S.",
              "The Rigvedic river Asikni is today's:",
              ["Asikni is second in the chain V-A-P-V-S.", "Second in J-C-R-B-S is Chenab."],
              "Chenab"),
        trick("Veda and priest: HUAB",
              "**H**otri with Rig, **U**dgatri with Sama, **A**dhvaryu with Yajur, **B**rahma with Atharva."),
        trick("Mandalas 3-7-9-10",
              "**3** Gayatri. **7** Ten Kings. **9** Soma. **10** Purusha Sukta."),
    ],
    mistakes=[
        mk("Saying the Gayatri Mantra is to a goddess Gayatri.",
           "It is addressed to **Savitri**, the sun god, in Mandala **III**."),
        mk("Saying \"Satyameva Jayate\" comes from the Rigveda.",
           "It comes from the **Mundaka** Upanishad."),
        mk("Treating the most-mentioned river and the holiest river as one.",
           "Most mentioned is the **Sindhu**. Holiest is the **Saraswati**."),
        mk("Placing iron in the Early Vedic period.",
           "Iron appears only in the **Later** Vedic period."),
    ],
    revision=[
        "Early Vedic: cattle, Sapta Sindhu, flexible society. Later Vedic: iron, doab, Painted Grey Ware, rigid varna.",
        "Veda and priest: Rig-Hotri, Sama-Udgatri, Yajur-Adhvaryu, Atharva-Brahma.",
        "Mandalas: 3 Gayatri, 7 Ten Kings, 9 Soma, 10 Purusha Sukta.",
        "Rivers: Vitasta Jhelum, Asikni Chenab, Parushni Ravi, Vipas Beas, Sutudri Sutlej.",
        "Satyameva Jayate is from the Mundaka Upanishad. Brihadaranyaka is the oldest Upanishad.",
        "Founders: Kapila, Patanjali, Gautama, Kanada, Jaimini, Badarayana.",
    ],
    patterns=[
        pat("ga-ved-p1", "Veda with priest, upaveda or content", "very common",
            "\"Which Veda is called\", \"the priest who recites the Samaveda\", \"Dhanurveda belongs to which Veda\".",
            ["Recall the four Vedas with priests: Rig-Hotri, Sama-Udgatri, Yajur-Adhvaryu, Atharva-Brahma.",
             "Upavedas: Ayurveda-Rig, Gandharvaveda-Sama, Dhanurveda-Yajur, Shilpaveda-Atharva.",
             "Atharvaveda is the Veda of charms and spells."],
            "Each Veda has one fixed set of links, so a table settles every option.",
            "Which Veda has sacrificial formulas in both prose and verse?",
            ["Prose and verse together points to one Veda.", "It has Shukla (white) and Krishna (black) forms."],
            "The Yajurveda"),
        pat("ga-ved-p2", "Rigveda mandala and hymn facts", "very common",
            "Gayatri Mantra, Battle of Ten Kings, Soma, Purusha Sukta, \"most hymns to which god\".",
            ["Anchor: 3 Gayatri, 7 Ten Kings, 9 Soma, 10 Purusha Sukta.",
             "Most hymns: Indra (about 250), then Agni (about 200).",
             "Ten Kings: river Parushni (Ravi), winner Sudas of the Bharatas."],
            "Only four mandalas are asked, so memorise those four.",
            "The Gayatri Mantra of the Rigveda was composed by:",
            ["It is in Mandala III.", "The composer is Vishwamitra."],
            "Rishi Vishwamitra (addressed to Savitri)"),
        pat("ga-ved-p3", "Rigvedic river and modern name", "common",
            "A Rigvedic river name with modern rivers as options, or the reverse.",
            ["Learn the chain west to east: Vitasta, Asikni, Parushni, Vipas, Sutudri.",
             "Match it with Jhelum, Chenab, Ravi, Beas, Sutlej.",
             "Extras: Kubha Kabul, Krumu Kurram, Drishadvati Ghaggar-Chautang."],
            "The two chains run in the same order, so one list gives the other.",
            "The Rigvedic river Vitasta is known today as:",
            ["Vitasta is first in the west-to-east chain.", "The first modern name is Jhelum."],
            "The Jhelum"),
        pat("ga-ved-p4", "Early and Later Vedic life and terms", "common",
            "A comparison of early and later Vedic society, or one term such as Bali, Vidatha, PGW.",
            ["Note the direction of change: cattle to farming, Sapta Sindhu to doab.",
             "Assemblies weaken and kings gain power.",
             "Bali moves from voluntary gift to tax.",
             "Iron and Painted Grey Ware belong to the Later Vedic age."],
            "Every later change points one way, so you can guess the direction.",
            "In the Rigvedic period, Bali was:",
            ["Bali is a payment to the chief.", "In Rigvedic times it was voluntary."],
            "A voluntary tribute to the chief"),
        pat("ga-ved-p5", "Upanishad and school of philosophy", "occasional",
            "\"Satyameva Jayate is taken from\", \"founder of the Nyaya school\", \"Nachiketa appears in\".",
            ["Upanishads: Mundaka Satyameva Jayate, Katha Nachiketa, Brihadaranyaka oldest, Chandogya Krishna.",
             "Founders: Sankhya Kapila, Yoga Patanjali, Nyaya Gautama, Vaisheshika Kanada, Mimamsa Jaimini, Vedanta Badarayana.",
             "All six schools accept the Vedas as authority."],
            "There are only four Upanishads and six founders to learn.",
            "The Vaisheshika school, known for its atomic theory, was founded by:",
            ["Vaisheshika teaches atoms.", "Its founder is Kanada."],
            "Kanada"),
        pat("ga-ved-p6", "Sacrifices, ashramas and later Vedic terms", "occasional",
            "\"Horse sacrifice\", \"chariot race\", \"four ashramas\", \"Vedangas\".",
            ["Rajasuya is consecration, Ashvamedha is horse sacrifice, Vajapeya is chariot race.",
             "Ashramas: Brahmacharya, Grihastha, Vanaprastha, Sanyasa (Jabala Upanishad).",
             "Vedangas: Shiksha, Kalpa, Vyakarana, Nirukta, Chhanda, Jyotisha."],
            "Each term has one plain meaning that the option list repeats.",
            "The Vajapeya sacrifice of the Later Vedic age was a:",
            ["Rajasuya was a consecration.", "Ashvamedha was a horse sacrifice.", "Vajapeya is the remaining one."],
            "Chariot race"),
    ],
)
