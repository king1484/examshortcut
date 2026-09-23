from gacommon import Q, save_topic

S = []  # subtopics

# ---------------------------------------------------------------- 1. Indus Valley
S.append({
"id": "indus-valley",
"title": "Indus Valley (Harappan) Civilisation",
"concept": """**Basics you must know**

| Point | Fact |
|---|---|
| Age | Bronze Age (copper + tin); **no iron** |
| Mature phase | c. 2600–1900 BCE (NCERT) |
| First site excavated | **Harappa, 1921** (Daya Ram Sahni) — hence "Harappan civilisation" |
| ASI Director-General then | **Sir John Marshall** (announced the discovery in 1924) |
| Script | Pictographic, written right to left (boustrophedon in places); **still undeciphered** |
| Seals | Mostly **steatite**; most common animal motif = **unicorn** (one-horned bull) |
| Religion | Mother Goddess, "Pashupati" (proto-Shiva) seal, pipal tree, phallic stones; **no temples found** |
| Crops | Wheat, barley, peas, sesame; **cotton first grown here** (Greeks later called it *Sindon*); rice husk at **Lothal & Rangpur** |
| Town plan | Grid pattern, covered drains, burnt bricks (ratio 1:2:4), citadel (west) + lower town (east) |

**Site table (most asked)**

| Site | River | Present location | Excavator (year) | Signature finds |
|---|---|---|---|---|
| **Harappa** | Ravi | Sahiwal (Montgomery) dist., Punjab, **Pakistan** | Daya Ram Sahni (1921) | Rows of granaries, red-sandstone male torso, Cemetery R-37 & H, coffin burial |
| **Mohenjo-daro** ("mound of the dead") | Indus | Larkana dist., Sindh, **Pakistan** | R.D. Banerji (1922) | **Great Bath**, Great Granary, bronze **Dancing Girl**, steatite **bearded priest**, Pashupati seal, assembly hall |
| **Chanhudaro** | Indus | Sindh, Pakistan | N.G. Majumdar (1931) | **Bead-making** workshop; the only city **without a citadel** |
| **Lothal** | Bhogava (near Sabarmati) | Ahmedabad dist., **Gujarat** | S.R. Rao (1954–55) | **Dockyard**, rice husk, fire altars, Persian Gulf seal, double burial |
| **Kalibangan** ("black bangles") | Ghaggar | Hanumangarh dist., **Rajasthan** | A. Ghosh (found 1953); B.B. Lal & B.K. Thapar (dug 1960s) | **Ploughed field**, fire altars, camel bones |
| **Banawali** | Ghaggar (Saraswati) | Fatehabad dist., **Haryana** | R.S. Bisht (1973–74) | Clay **plough model**, barley |
| **Dholavira** | Between Mansar & Manhar streams | Khadir Bet, Kutch, **Gujarat** | J.P. Joshi (found 1967–68); R.S. Bisht (dug 1990) | **Water reservoirs/conservation**, three-part city, **10-letter signboard**; UNESCO site (2021) |
| **Rakhigarhi** | Ghaggar plain | Hisar dist., **Haryana** | Amarendra Nath (1997–2000) | **Largest Harappan site in India**; ancient DNA study |
| **Surkotada** | — | Kutch, Gujarat | J.P. Joshi (1964) | Horse remains (bones) |
| **Ropar (Rupnagar)** | Sutlej | **Punjab (India)** | Y.D. Sharma (1953–55) | First site dug after Independence; dog buried with man |
| **Alamgirpur** | Hindon | Meerut, **UP** | Y.D. Sharma (1958) | **Easternmost** site |
| **Sutkagendor** | Dasht | Makran coast, Baluchistan (Pak.) | Aurel Stein (1927) | **Westernmost** site; trade post |
| **Manda** | Chenab | Jammu, **J&K** | J.P. Joshi (1982) | **Northernmost** site |
| **Daimabad** | Pravara (Godavari basin) | Ahmednagar dist., **Maharashtra** | — | **Southernmost** site; **bronze chariot** |
| **Kot Diji** | Indus | Sindh, Pakistan | F.A. Khan (1955) | Pre-Harappan fortified settlement |

**States with most sites in India:** Gujarat (Lothal, Dholavira, Surkotada, Rangpur, Rojdi), Haryana (Rakhigarhi, Banawali, Bhirrana), Rajasthan (Kalibangan), Punjab (Ropar), UP (Alamgirpur), Maharashtra (Daimabad).""",
"formulas": [],
"tricks": [
 {"title": "Four extremes — \"Many Donkeys Are Slow\"",
  "body": "**M**anda (North, J&K) · **D**aimabad (South, Maharashtra) · **A**lamgirpur (East, UP) · **S**utkagendor (West, Baluchistan).",
  "example": {"q": "The easternmost Harappan site is —", "solution": "Donkeys **A**re → **A**lamgirpur (Meerut, UP) on the Hindon."}},
 {"title": "Site-to-find pairing",
  "body": "**Lothal = Launch** (dockyard) · **Kali-bangan = Kheti** (ploughed field) · **Mohenjo = Majestic Bath** (Great Bath) · **Chanhu = Chain of beads** (bead factory) · **Dholavira = Drop of water** (reservoirs)."}
],
"mistakes": [
 "Harappa is on the **Ravi**, Mohenjo-daro on the **Indus** — do not swap.",
 "Ploughed **field** = Kalibangan; clay **plough model** = Banawali.",
 "Largest site in India = Rakhigarhi; Mohenjo-daro and Harappa are in Pakistan.",
 "Harappans knew copper/bronze and gold/silver but **not iron**; horse evidence is doubtful (only Surkotada bones)."
]
})

# ---------------------------------------------------------------- 2. Vedic age
S.append({
"id": "vedic-age",
"title": "Vedic Age & Vedic Literature",
"concept": """**Timeline:** Early (Rigvedic) Vedic c. 1500–1000 BCE (Sapta Sindhu region, pastoral, cattle = wealth) → Later Vedic c. 1000–600 BCE (Ganga–Yamuna doab, agriculture, iron called *shyama/krishna ayas*, Painted Grey Ware).

**The four Vedas**

| Veda | Content | Priest | Upaveda |
|---|---|---|---|
| **Rigveda** | Oldest; **10 mandalas, 1028 hymns** (suktas) of praise | Hotri | Ayurveda |
| **Samaveda** | Rigvedic hymns set to melody — **root of Indian music** | Udgatri | Gandharvaveda |
| **Yajurveda** | Sacrificial formulas; prose + verse; Shukla (white) & Krishna (black) | Adhvaryu | Dhanurveda |
| **Atharvaveda** | Charms, spells, folk medicine; calls **Sabha & Samiti "two daughters of Prajapati"** | Brahma | Shilpaveda |

**Rigveda highlights**
- **Mandala III** – **Gayatri Mantra** (to Savitri), composed by **Vishwamitra**.
- **Mandala VII** – **Battle of Ten Kings** (Dasarajna) on the **Parushni (Ravi)**; **Sudas** of the Bharata clan won.
- **Mandala IX** – wholly addressed to **Soma**.
- **Mandala X** – **Purusha Sukta** (first mention of the four varnas); Nasadiya Sukta (creation hymn).
- Most hymns: **Indra** (~250, called *Purandara*, breaker of forts), then **Agni** (~200); **Varuna** guards *rita* (cosmic order).

**Rivers — Rigvedic vs modern names**

| Rigvedic | Modern | Rigvedic | Modern |
|---|---|---|---|
| Vitasta | Jhelum | Sutudri | Sutlej |
| Asikni | Chenab | Kubha | Kabul |
| Parushni | Ravi | Krumu | Kurram |
| Vipas | Beas | Gomal | Gomati (Gomal) |
| Sindhu | Indus (most mentioned) | Saraswati | "Naditama" – holiest river |
| Drishadvati | Ghaggar/Chautang | Suvastu | Swat |

**Polity & society terms**

| Term | Meaning |
|---|---|
| Sabha | Council of elders (women attended in early period) |
| Samiti | Popular assembly of the people |
| Vidatha | Oldest tribal assembly |
| Rajan / Purohita / Senani | Chief / priest / army chief |
| Gramani | Village headman |
| Bali | Voluntary tribute → later a tax |
| Bhagadugha | Collector of taxes (later Vedic) |
| Gotra | Lineage; later Vedic rule of gotra exogamy |

**Later Vedic sacrifices:** Rajasuya (consecration), Ashvamedha (horse sacrifice for supremacy), Vajapeya (chariot race). **Four ashramas** (Brahmacharya, Grihastha, Vanaprastha, Sanyasa) — all four first listed in the **Jabala Upanishad**.

**Vedic literature layers:** Samhitas → Brahmanas (ritual prose; e.g. Aitareya, Shatapatha) → Aranyakas (forest texts) → **Upanishads** (philosophy; ~108; *Vedanta*).

| Upanishad | Why asked |
|---|---|
| **Mundaka** | Source of **"Satyameva Jayate"** (national motto) |
| **Katha** | Dialogue of **Nachiketa and Yama** (death) |
| **Brihadaranyaka** | Oldest & largest; Yajnavalkya–Gargi/Maitreyi dialogues |
| **Chandogya** | Early mention of Krishna, son of Devaki |

**Six Vedangas:** Shiksha (phonetics), Kalpa (ritual), Vyakarana (grammar), Nirukta (etymology), Chhanda (metre), Jyotisha (astronomy).

**Six schools of philosophy (Shad-darshana)**

| School | Founder |
|---|---|
| Sankhya | Kapila |
| Yoga | Patanjali |
| Nyaya | Gautama (Akshapada) |
| Vaisheshika (atomism) | Kanada |
| Purva Mimamsa | Jaimini |
| Uttara Mimamsa (Vedanta) | Badarayana |""",
"formulas": [],
"tricks": [
 {"title": "Punjab rivers west→east: \"Very Angry Parrots Visit Sutlej\"",
  "body": "**V**itasta = Jhelum → **A**sikni = Chenab → **P**arushni = Ravi → **V**ipas = Beas → **S**utudri = Sutlej. Same order as the modern **J-C-R-B-S**.",
  "example": {"q": "The Rigvedic river Asikni is today's —", "solution": "Second in the chain (V-**A**-P-V-S ↔ J-**C**-R-B-S) → **Chenab**."}},
 {"title": "Veda → priest: \"Rig-Hotri, Sama-Udgatri, Yajur-Adhvaryu, Atharva-Brahma\"",
  "body": "Think **HUAB**: **H**otri recites, **U**dgatri sings, **A**dhvaryu performs, **B**rahma supervises."},
 {"title": "Rigveda mandala anchors: 3-7-9-10",
  "body": "**3** = Gayatri, **7** = Ten Kings war, **9** = Soma, **10** = Purusha Sukta (varnas)."}
],
"mistakes": [
 "Gayatri Mantra is addressed to **Savitri** (sun deity), not to Gayatri as a goddess; it is in Mandala **III**.",
 "'Satyameva Jayate' is from the **Mundaka** Upanishad, not from the Rigveda.",
 "Most mentioned river = **Sindhu**; most sacred = **Saraswati**. Different answers.",
 "Iron appears only in the **Later** Vedic period."
]
})

# ---------------------------------------------------------------- 3. Mahajanapadas
S.append({
"id": "mahajanapadas",
"title": "Mahajanapadas & Rise of Magadha",
"concept": """**16 Mahajanapadas** (6th century BCE) are listed in the Buddhist text **Anguttara Nikaya** (Jain *Bhagavati Sutra* gives a different list).

| Mahajanapada | Capital | Present region |
|---|---|---|
| Anga | **Champa** | Bhagalpur–Munger, Bihar |
| **Magadha** | **Girivraja / Rajagriha**, later **Pataliputra** | Patna–Gaya, Bihar |
| Kashi | **Varanasi** | UP |
| Kosala | **Shravasti** (also Ayodhya/Saket) | Eastern UP |
| Vajji | **Vaishali** | North Bihar — confederacy of 8 clans incl. **Licchavis** (republic) |
| Malla | **Kushinara** & Pava | Gorakhpur area, UP (republic) |
| Chedi | Shuktimati | Bundelkhand |
| Vatsa | **Kaushambi** | Near Prayagraj, UP |
| Kuru | **Indraprastha** | Delhi–Meerut–Haryana |
| Panchala | Ahichchhatra (N) & Kampilya (S) | Rohilkhand, western UP |
| Matsya | **Viratnagar** | Jaipur–Alwar, Rajasthan |
| Surasena | **Mathura** | UP |
| **Assaka (Ashmaka)** | Potana/Potali | On the Godavari — **only one south of the Vindhyas** |
| **Avanti** | **Ujjain** (N) & **Mahishmati** (S) | Malwa, MP |
| Gandhara | **Taxila** | Rawalpindi–Peshawar, Pakistan |
| Kamboja | Rajapura | NW frontier — famous for **horses** |

**Four great powers:** Magadha, Kosala, Vatsa, Avanti → **Magadha** emerged supreme (iron mines, fertile Ganga plain, elephants, natural forts at Rajagriha).

**Magadhan dynasties**

| Dynasty | Key rulers & facts |
|---|---|
| **Haryanka** | **Bimbisara** (contemporary of Buddha & Mahavira; marriage alliances with Kosala, Licchavi, Madra; annexed Anga) · **Ajatashatru** (killed his father; fought Vajjis; **First Buddhist Council**) · **Udayin** (founded **Pataliputra** at the Ganga–Son confluence) |
| **Shishunaga** | Shishunaga (destroyed **Avanti**) · **Kalashoka/Kakavarna** (**Second Buddhist Council**, Vaishali) |
| **Nanda** | **Mahapadma Nanda** — first non-Kshatriya empire-builder, titles *Ekarat*, *Sarvakshatrantaka* · **Dhana Nanda** — last; contemporary of Alexander; overthrown by Chandragupta Maurya |

**Foreign invasions**
- **Persian (Achaemenid):** Darius I annexed Gandhara/Punjab (c. 516 BCE) — brought **Kharosthi** script (written right to left) and Aramaic influence.
- **Alexander (326 BCE):** crossed the Indus, fought **Porus (Puru)** at the **Battle of the Hydaspes (Jhelum)**; troops refused to go beyond the **Beas (Hyphasis)**; died at Babylon in 323 BCE.""",
"formulas": [],
"tricks": [
 {"title": "Capital pairs by first letter",
  "body": "**K**osala–shravasti? No: use **\"Vatsa-Kaushambi, Vajji-Vaishali\"** (both V) and **\"Avanti-Ujjain, Anga-Champa\"** (both start with A). **Kuru-Indraprastha**, **Gandhara-Taxila** (G-T like 'GT road' ending in the north-west)."},
 {"title": "Magadha order: \"Hari Shishu Nanda\"",
  "body": "**Hary**anka → **Shishu**naga → **Nanda** → Maurya. Councils: Ajatashatru (1st) is Haryanka, Kalashoka (2nd) is Shishunaga.",
  "example": {"q": "The Second Buddhist Council was held under which dynasty?", "solution": "Kalashoka → **Shishunaga** dynasty (Vaishali, 383 BCE)."}}
],
"mistakes": [
 "Pataliputra was founded by **Udayin**, not Ajatashatru (Ajatashatru fortified a small fort, Pataligrama).",
 "Assaka is the lone Mahajanapada **south** of the Vindhyas; Avanti is north (Malwa).",
 "Alexander's army mutinied at the **Beas**, not the Jhelum; the Jhelum (Hydaspes) was the battle with Porus."
]
})

# ---------------------------------------------------------------- 4. Buddhism & Jainism
S.append({
"id": "buddhism-jainism",
"title": "Buddhism & Jainism",
"concept": """**Gautama Buddha (c. 563–483 BCE, traditional dates)**

| Event | Place / fact | Symbol |
|---|---|---|
| Birth | **Lumbini** (Nepal); Shakya clan; father Suddhodana, mother Mahamaya (foster mother Prajapati Gautami) | Lotus & bull |
| Great Renunciation (*Mahabhinishkramana*) | Age 29; horse **Kanthaka**, charioteer **Channa** | Horse |
| Enlightenment (*Nirvana/Sambodhi*) | Age 35, **Bodh Gaya**, under the pipal (Bodhi) tree on the **Niranjana (Falgu)** | Bodhi tree |
| First sermon (*Dharmachakra-pravartana*) | **Sarnath** (Deer Park, Rishipatana) | Wheel |
| Death (*Mahaparinirvana*) | Age 80, **Kushinagar** (Malla republic) | Stupa |

Wife **Yashodhara**, son **Rahula**. Teachings in **Pali**. **Tri-ratna:** Buddha, Dhamma, Sangha. **Four Noble Truths** (suffering, its cause, its end, the path) and **Eightfold Path** (*Ashtangika Marga*) — the "Middle Path".

**Buddhist Councils (Sangiti)**

| Council | Year | Place | King | President | Outcome |
|---|---|---|---|---|---|
| 1st | 483 BCE | **Rajagriha** (Saptaparni cave) | **Ajatashatru** | **Mahakassapa** | Sutta (by **Ananda**) & Vinaya (by **Upali**) compiled |
| 2nd | 383 BCE | **Vaishali** | **Kalashoka** | **Sabakami** | Split: Sthaviravadins vs Mahasanghikas |
| 3rd | 250 BCE | **Pataliputra** | **Ashoka** | **Moggaliputta Tissa** | **Abhidhamma Pitaka** added; missions abroad |
| 4th | c. 72 CE | **Kundalvana, Kashmir** | **Kanishka** | **Vasumitra** (deputy **Ashvaghosha**) | Split into **Hinayana & Mahayana** |

**Tripitaka:** *Vinaya* (monastic rules), *Sutta* (discourses), *Abhidhamma* (philosophy). **Jatakas** = stories of Buddha's previous births. **Milindapanha** = dialogue of Indo-Greek king **Menander** with monk **Nagasena**. Mahayana philosopher **Nagarjuna** (Madhyamika) — "Einstein of India" (a popular tag). Future Buddha = **Maitreya**; Padmapani = **Avalokiteshvara**.

**Jainism — 24 Tirthankaras**

| No. | Tirthankara | Symbol |
|---|---|---|
| 1 | **Rishabhanatha (Adinatha)** | Bull |
| 22 | Neminatha (Arishtanemi) | Conch |
| 23 | **Parshvanatha** — prince of Varanasi (son of Ashvasena); gave **4 vows** | Snake |
| 24 | **Vardhamana Mahavira** | Lion |

**Mahavira (traditional 540–468 BCE):** born **Kundagrama** near Vaishali; father **Siddhartha** (Jnatrika clan), mother **Trishala** (Licchavi princess, sister of Chetaka); wife Yashoda, daughter Anojja (Priyadarshana). **Kaivalya** at 42 under a sal tree at **Jrimbhikagrama** on the **Rijupalika**; died at **Pavapuri** (near Rajgir) at 72. Added the **5th vow — Brahmacharya**. Titles: *Jina* (conqueror), *Nirgrantha* (free from bonds).

- **Five vows:** Ahimsa, Satya, Asteya, Aparigraha, Brahmacharya.
- **Tri-ratna (Jain):** Right faith, Right knowledge, Right conduct.
- **Sects:** **Digambara** (sky-clad; led by **Bhadrabahu**, migrated south with Chandragupta Maurya) vs **Shvetambara** (white-clad; **Sthulabhadra**).
- **Jain councils:** 1st at **Pataliputra** (c. 300 BCE, president **Sthulabhadra**; 12 Angas compiled) · 2nd at **Vallabhi**, Gujarat (5th–6th century CE, president **Devarddhi Kshamasramana**; canon finally written).
- Language: **Prakrit (Ardhamagadhi)**. *Kalpasutra* attributed to **Bhadrabahu**.
- Monuments: **Gommateshwara (Bahubali)** monolith at **Shravanabelagola** (Karnataka, c. 983 CE, by **Chamundaraya**, minister of the Western Gangas; *Mahamastakabhisheka* every 12 years); **Dilwara temples** (Mount Abu).

**Buddhist learning centres:** Nalanda (founded by Gupta king **Kumaragupta I**), **Vikramashila** (Pala king **Dharmapala**), **Odantapuri** (Pala king Gopala), Taxila.""",
"formulas": [],
"tricks": [
 {"title": "Councils — places \"Raja Vaishali Pata Kashmir\", kings alternate \"A-K-A-K\"",
  "body": "Places: **Raj**agriha → **Vaish**ali → **Pat**aliputra → **Kash**mir. Kings: **A**jatashatru, **K**alashoka, **A**shoka, **K**anishka. Presidents: **\"Maha-Saba-Moggali-Vasu\"**.",
  "example": {"q": "Who presided over the Third Buddhist Council?", "solution": "Third = Pataliputra / Ashoka → **Moggaliputta Tissa**."}},
 {"title": "Buddha's life symbols: \"Lotus → Horse → Tree → Wheel → Stupa\"",
  "body": "Birth, renunciation, enlightenment, first sermon, death — in that order."},
 {"title": "Tirthankara symbols: \"Bull begins, Lion ends\"",
  "body": "1st Rishabha = bull, 22nd = conch, 23rd Parshva = **s**nake (**S**erpent), 24th Mahavira = lion."}
],
"mistakes": [
 "Mahavira **added** Brahmacharya; the other four vows came from Parshvanatha.",
 "Enlightenment at Bodh Gaya, first sermon at **Sarnath**, death at **Kushinagar** — do not confuse Sarnath with Bodh Gaya.",
 "The 4th Buddhist Council (Kanishka) split the order into Hinayana/Mahayana; the 2nd split it into Sthaviravadin/Mahasanghika.",
 "Nalanda was founded by the **Guptas** (Kumaragupta I); Vikramashila by the **Palas**."
]
})

# ---------------------------------------------------------------- 5. Mauryas
S.append({
"id": "mauryan-empire",
"title": "Mauryan Empire",
"concept": """**Rulers**

| Ruler | Reign (approx.) | Key facts |
|---|---|---|
| **Chandragupta Maurya** | 322–298 BCE | Overthrew Dhana Nanda with **Chanakya (Kautilya/Vishnugupta)**; defeated **Seleucus Nicator** (305 BCE) and got Arachosia, Gedrosia, Paropamisadae, Aria + marriage alliance; Greek name **Sandrocottus**; became a Jain, went to **Shravanabelagola** with **Bhadrabahu** and died by *sallekhana* |
| **Bindusara** | 298–273 BCE | Title **Amitraghata** ("slayer of foes"); Greek envoy **Deimachus** (of Antiochus I); followed the **Ajivika** sect |
| **Ashoka** | c. 268–232 BCE | **Kalinga war 261 BCE** (8th regnal year); turned to Buddhism (monk **Upagupta**); *Dhamma* policy; **Third Buddhist Council** |
| Brihadratha | — | **Last** Mauryan; killed by his general **Pushyamitra Shunga** (c. 185 BCE) |

**Foreign accounts**
- **Megasthenes** — ambassador of **Seleucus Nicator** at Chandragupta's court; wrote **Indica** (lost; survives in later Greek quotes). Described Pataliputra run by **6 committees of 5 members each** and Indian society in **7 "castes"**.
- **Arthashastra** by **Kautilya** — treatise on statecraft, 15 books (*adhikaranas*); rediscovered and published by **R. Shamasastry** (early 1900s).

**Ashoka's inscriptions**

| Type | Facts |
|---|---|
| **14 Major Rock Edicts** | **RE II** – medical care for humans & animals · **RE V** – appointment of **Dhamma Mahamattas** · **RE XII** – tolerance among sects · **RE XIII** – **Kalinga war**, remorse, *dhamma-vijaya* |
| **Separate Kalinga Edicts** | At **Dhauli & Jaugada** (Odisha): "All men are my children" |
| **Minor Rock Edicts** | **Maski** (Raichur, Karnataka) — first found edict that names the king as **"Ashoka"** (also Gujarra, Nittur, Udegolam) |
| **7 Pillar Edicts** | Delhi-Topra pillar has all seven; Topra & Meerut pillars were moved to Delhi by **Firoz Shah Tughlaq** |
| Scripts | Mostly **Brahmi**; **Kharosthi** at Shahbazgarhi & Mansehra (NW); **Greek & Aramaic** at Kandahar (Afghanistan) |
| Decipherment | Brahmi deciphered by **James Prinsep** (1837) |

Ashoka calls himself **"Devanampiya Piyadasi"** (beloved of the gods). **Sarnath Lion Capital** (four lions, chakra, bull–horse–elephant–lion on the abacus) → **National Emblem, adopted 26 January 1950**. Rampurva has a **bull capital**; Lauriya-Nandangarh a single lion. **Allahabad pillar** also carries Samudragupta's *Prayag Prashasti*.

**Administration & economy:** *Samaharta* – chief revenue collector; *Sannidhata* – treasurer; *Sita* – revenue from crown land; land tax usually **1/6** (*bhaga*); spies (*gudhapurushas*); provinces under princes (*kumaras*) at Taxila, Ujjain, Tosali, Suvarnagiri.

**Mauryan art:** highly **polished Chunar sandstone** pillars; **Barabar caves** (Bihar) cut for **Ajivikas** (Lomas Rishi cave); **Didarganj Yakshi** (chauri-bearer, Patna Museum).""",
"formulas": [],
"tricks": [
 {"title": "Edict numbers: \"2-Hospital, 5-Officer, 12-Tolerance, 13-Kalinga\"",
  "body": "Think of a hospital ward **2**, officer rank **5**, the **12** faiths tolerated, and the unlucky **13** (war).",
  "example": {"q": "Which Major Rock Edict records Ashoka's remorse after Kalinga?", "solution": "Unlucky **13** → **Rock Edict XIII**."}},
 {"title": "Mauryan dates chain: 322 → 185 → 73 BCE",
  "body": "Maurya starts **322**, Shunga starts **185** (Pushyamitra), Kanva starts **73** (Vasudeva Kanva)."}
],
"mistakes": [
 "Megasthenes served **Seleucus**; Deimachus served **Antiochus I** (at Bindusara's court).",
 "Chandragupta Maurya was a **Jain** at the end; Bindusara favoured **Ajivikas**; Ashoka became Buddhist.",
 "The name 'Ashoka' appears in **Maski**, not in the Major Rock Edicts, which use 'Devanampiya Piyadasi'.",
 "Brahmi was deciphered by **James Prinsep**, not by John Marshall."
]
})

# ---------------------------------------------------------------- 6. Post-Mauryan
S.append({
"id": "post-mauryan",
"title": "Post-Mauryan Age: Shungas to Kushanas",
"concept": """**Indigenous dynasties**

| Dynasty | Founder / key rulers | Facts |
|---|---|---|
| **Shunga** (c. 185–73 BCE) | **Pushyamitra Shunga** | Killed Brihadratha; performed **2 Ashvamedhas**; patron of grammarian **Patanjali**; **Agnimitra** is the hero of Kalidasa's *Malavikagnimitram*; **Bharhut** stupa railings |
| **Kanva** (c. 73–28 BCE) | **Vasudeva Kanva** | Killed last Shunga king Devabhuti; ended by the Satavahanas |
| **Satavahana** (Andhras) | Founder **Simuka**; capital **Pratishthana (Paithan)** on the Godavari | **Gautamiputra Satakarni** — greatest; destroyed the Kshaharata Shakas (**Nahapana**); praised in the **Nasik inscription** of his mother **Gautami Balashri**. **Hala** wrote *Gathasaptashati* (Prakrit). First to give **tax-free land grants to Brahmanas**; kings used **metronymics**; **lead** and potin coins; official language **Prakrit** |
| **Chedi (Kalinga)** | **Kharavela** | **Hathigumpha inscription** (Udayagiri, Odisha); Jain patron |

**Foreign dynasties**

| Group | Key ruler | Facts |
|---|---|---|
| **Indo-Greeks** | **Demetrius**, **Menander (Milinda)** — capital **Sakala (Sialkot)** | First coins that can be definitely attributed to kings; **first gold coins** in India; *Milindapanha*; roots of **Gandhara art** |
| **Shakas (Scythians)** | **Rudradaman I** (Western Kshatrapa, Ujjain) | **Junagadh (Girnar) inscription, c. 150 CE** — first long inscription in chaste **Sanskrit**; repaired the **Sudarshana lake** (built by Chandragupta Maurya's governor **Pushyagupta**) |
| **Parthians (Pahlavas)** | **Gondophernes** | Visit of **St. Thomas** (tradition); Takht-i-Bahi inscription |
| **Kushanas** (Yuezhi) | **Kujula Kadphises** → **Vima Kadphises** (large gold issues, Shiva on coins) → **Kanishka** | See below |

**Kanishka (accession 78 CE)**
- Started the **Shaka era (78 CE)** — basis of India's **National Calendar**.
- Capital **Purushapura (Peshawar)**; second centre **Mathura**.
- Convened the **4th Buddhist Council** (Kundalvana, Kashmir); patron of **Mahayana**.
- Court: **Ashvaghosha** (*Buddhacharita*), **Nagarjuna**, **Vasumitra**, physician **Charaka** (*Charaka Samhita*).
- Title *Devaputra*; **Rabatak inscription** (Afghanistan) gives Kushana genealogy.
- Art: **Gandhara school** (Greco-Roman style, grey schist) & **Mathura school** (red sandstone, indigenous).

**Eras**

| Era | Starts | Founder (tradition) |
|---|---|---|
| **Vikram Samvat** | **57 BCE** | Vikramaditya of Ujjain (after defeating Shakas) |
| **Shaka Samvat** | **78 CE** | **Kanishka** — official national calendar |
| Gupta era | 319–320 CE | Chandragupta I |
| Harsha era | 606 CE | Harshavardhana |""",
"formulas": [],
"tricks": [
 {"title": "\"57 minus, 78 plus\"",
  "body": "Vikram Samvat = **57 BCE** (subtract), Shaka = **78 CE** (add). To convert: CE = VS − 57; CE = Shaka + 78.",
  "example": {"q": "Shaka year 1948 corresponds to which CE year?", "solution": "1948 + 78 = **2026 CE** (Shaka year begins on 22 March in a normal year)."}},
 {"title": "Satavahana = \"S-P-G-H\"",
  "body": "**S**imuka founder · **P**ratishthana capital · **G**autamiputra greatest · **H**ala poet."}
],
"mistakes": [
 "Rudradaman's Junagadh inscription is in **Sanskrit**; Ashoka's inscriptions are in Prakrit.",
 "Shaka era was begun by **Kanishka** (a Kushana), not by a Shaka ruler.",
 "Charaka was Kanishka's physician; **Sushruta** is the surgeon (Sushruta Samhita)."
]
})

# ---------------------------------------------------------------- 7. Gupta & Harsha
S.append({
"id": "gupta-harsha",
"title": "Gupta Age & Harshavardhana",
"concept": """**Gupta rulers**

| Ruler | Facts |
|---|---|
| Sri Gupta | Founder |
| Ghatotkacha | Second ruler |
| **Chandragupta I** (c. 319–335) | First *Maharajadhiraja*; married Licchavi princess **Kumaradevi**; **Gupta era 319–320 CE** |
| **Samudragupta** (c. 335–375) | **Prayag Prashasti** on the Allahabad pillar, composed by court poet **Harishena**; called **"Napoleon of India"** by V.A. Smith; *Kaviraja*; coins show him **playing the veena**; Ashvamedha; Sri Lankan king **Meghavarman** sought permission for a monastery at Bodh Gaya |
| **Chandragupta II "Vikramaditya"** (c. 375–415) | Defeated the Western Kshatrapas (Shakas); daughter **Prabhavatigupta** married Vakataka **Rudrasena II**; **Fa-Hien** visited; **Navaratnas**; **Mehrauli Iron Pillar** (rust-free; inscription of king "Chandra"); first Gupta **silver coins**; Ujjain as second capital |
| **Kumaragupta I** | Founded **Nalanda Mahavihara**; title *Mahendraditya* |
| **Skandagupta** | Repulsed the **Hunas**; repaired the **Sudarshana lake** (Junagadh inscription) |

Later: **Huna** chiefs **Toramana** and **Mihirakula**; Mihirakula was defeated by **Yashodharman** of Malwa. Gupta gold coins = **dinara**; silver = *rupaka*. **Agrahara** grants to Brahmanas.

**Navaratnas of Chandragupta II (traditional list):** **Kalidasa**, **Amarasimha** (*Amarakosha*), Dhanvantari (medicine), Vararuchi (grammar), Varahamihira (astronomy), Shanku (architecture), Kshapanaka, Vetala Bhatta, Ghatakarpara.

**Science**

| Scholar | Work | Contribution |
|---|---|---|
| **Aryabhata** (b. 476 CE, Kusumapura) | **Aryabhatiya** (499 CE) | Earth rotates on its axis; eclipses due to shadows; π ≈ 3.1416; place value — India's **first satellite (1975)** named after him |
| **Varahamihira** | *Brihat Samhita*, *Pancha Siddhantika* | Encyclopaedia of astrology, astronomy, botany |
| **Brahmagupta** | *Brahmasphuta Siddhanta* (628 CE) | Rules for operating with **zero** |
| Vagbhata | *Ashtanga Hridaya* | Medicine |

**Gupta art & architecture:** **Dashavatara temple, Deogarh** (Lalitpur, UP — early *shikhara*, panchayatana), **Bhitargaon** brick temple (Kanpur), **Udayagiri caves** (Varaha panel, Vidisha), Sarnath school of Buddha images, several **Ajanta** caves (Vakataka patronage). Gupta age called the **"Classical/Golden Age"**.

**Chinese pilgrims**

| Pilgrim | Period / ruler | Account |
|---|---|---|
| **Fa-Hien (Faxian)** | 399–414 CE, **Chandragupta II** | *Fo-kwo-ki* (Record of Buddhist Kingdoms) |
| **Hiuen Tsang (Xuanzang)** | c. 630–645 CE, **Harsha** (also Pulakeshin II's Deccan, Pallava Kanchi) | ***Si-Yu-Ki***; studied at **Nalanda**; "Prince of Pilgrims" |
| **I-Tsing (Yijing)** | 671–695 CE | Studied at Nalanda |

**Harshavardhana (606–647 CE)**
- **Pushyabhuti (Vardhana)** dynasty; capital **Thanesar → Kannauj**; **Harsha era 606 CE**.
- Court poet **Banabhatta** — ***Harshacharita*** and ***Kadambari***.
- Harsha himself wrote Sanskrit plays **Nagananda, Ratnavali, Priyadarshika**.
- Defeated on the **Narmada** by Chalukya **Pulakeshin II** (recorded in the **Aihole inscription** by **Ravikirti**).
- Held the **Kannauj assembly (643 CE)** honouring Hiuen Tsang and the five-yearly **Prayag assembly** (*Mahamoksha Parishad*).""",
"formulas": [],
"tricks": [
 {"title": "Gupta sequence: \"Sri Ghat, Chandra-Samudra-Chandra, Kumar-Skand\"",
  "body": "Sri Gupta → Ghatotkacha → **Chandragupta I** → **Samudragupta** → **Chandragupta II** → **Kumaragupta I** → **Skandagupta**."},
 {"title": "Prashasti authors: \"H for Samudra, R for Pulakeshin\"",
  "body": "**H**arishena → Allahabad (Prayag) Prashasti of Samudragupta. **R**avikirti → Aihole inscription of Pulakeshin II. **B**anabhatta → Harshacharita (biography, not an inscription).",
  "example": {"q": "Who composed the Aihole inscription?", "solution": "Pulakeshin II → **Ravikirti** (a Jain poet)."}},
 {"title": "Pilgrims in order: \"Fa → Hiuen → I\" (F-H-I)",
  "body": "Fa-Hien (Chandragupta II) → Hiuen Tsang (Harsha) → I-Tsing (after Harsha). Alphabetical and chronological together."}
],
"mistakes": [
 "Fa-Hien came under **Chandragupta II**, Hiuen Tsang under **Harsha** — the most common swap.",
 "Harishena praised **Samudragupta**, not Chandragupta II.",
 "Iron Pillar at Mehrauli is Gupta (king Chandra), although it stands in the Qutub complex.",
 "Aryabhatiya was written in **499 CE**; Aryabhata was born 476 CE."
]
})

# ---------------------------------------------------------------- 8. South India
S.append({
"id": "south-dynasties",
"title": "Sangam Age & South Indian Dynasties",
"concept": """**Sangam age (c. 3rd century BCE – 3rd century CE)** — three Tamil assemblies (*sangams*) held under **Pandya** patronage at Madurai; 1st presided (tradition) by **Agastya**, 3rd by **Nakkirar**.

| Sangam kingdom | Capital | Port(s) | Emblem | Famous ruler |
|---|---|---|---|---|
| **Chera** | Vanji (Karur) | **Muziris**, Tondi | Bow | **Senguttuvan** (Red Chera) — started **Pattini (Kannagi) cult** |
| **Chola** | **Uraiyur**, Puhar | **Puhar (Kaveripattinam)** | Tiger | **Karikala** — built the **Kallanai (Grand Anicut)** on the Kaveri |
| **Pandya** | **Madurai** | **Korkai** | Fish (carp) | Nedunjeliyan |

**Sangam literature**

| Work | Author | Note |
|---|---|---|
| **Tolkappiyam** | Tolkappiyar | Earliest Tamil **grammar** |
| **Tirukkural** | **Thiruvalluvar** | "Tamil Veda"; ethics in 1330 couplets |
| **Silappadikaram** | **Ilango Adigal** | Epic of **Kannagi & Kovalan** (anklet) |
| **Manimekalai** | **Sittalai Sattanar** | Buddhist epic; sequel to Silappadikaram |
| Jivaka Chintamani | Tiruttakkadevar | Jain epic |
| Ettuthokai & Pattupattu | Various | Eight anthologies & ten idylls |

**Later southern dynasties**

| Dynasty | Capital | Founder | Key rulers & monuments |
|---|---|---|---|
| **Pallava** | **Kanchipuram** | Simhavishnu (imperial line) | **Mahendravarman I** (*Mattavilasa Prahasana*; rock-cut shrines) · **Narasimhavarman I "Mamalla"** — killed **Pulakeshin II**, took Vatapi (*Vatapikonda*); **Pancha Rathas** at Mamallapuram · **Narasimhavarman II (Rajasimha)** — **Shore Temple**, **Kailasanatha temple (Kanchi)** · Nandivarman II — Vaikuntha Perumal temple |
| **Chalukya of Badami (Vatapi)** | **Vatapi (Badami)** | **Pulakeshin I** | **Pulakeshin II** — defeated Harsha (Narmada), **Aihole inscription (Ravikirti)** · Vikramaditya II — **Virupaksha temple, Pattadakal** built by queen **Lokamahadevi** · **Aihole** = "cradle of Indian temple architecture" |
| **Rashtrakuta** | **Manyakheta (Malkhed)** | **Dantidurga** | **Krishna I** — **Kailasa temple (Cave 16), Ellora** · **Amoghavarsha I** — *Kavirajamarga* (Kannada poetics) · Krishna III — last great |
| **Chola (imperial)** | **Thanjavur**, then **Gangaikondacholapuram** | **Vijayalaya** (c. 850) | **Parantaka I** — **Uttaramerur inscriptions** (village assemblies) · **Rajaraja I** (985–1014) — **Brihadeeswara temple, Thanjavur**; conquered N. Sri Lanka & Maldives · **Rajendra I** (1014–44) — *Gangaikonda*, naval raid on **Srivijaya** (SE Asia) |
| Kadamba | Banavasi | Mayurasharma | — |
| Western Ganga | Talakad | — | Chamundaraya — Gommateshwara, Shravanabelagola |

**Chola local self-government:** **Ur** (general village assembly), **Sabha/Mahasabha** (Brahmin villages — *agrahara*), **Nagaram** (merchants); members chosen by lot (**kudavolai** system).

**UNESCO "Great Living Chola Temples":** Brihadisvara (Thanjavur, Rajaraja I), Gangaikondacholisvaram (Rajendra I), **Airavatesvara (Darasuram, Rajaraja II)**.""",
"formulas": [],
"tricks": [
 {"title": "Sangam emblems: \"Bow-Tiger-Fish = Chera-Chola-Pandya\" (C-C-P)",
  "body": "Alphabetical **B**ow, **T**iger... simpler: **Ch**era **B**ow (cheer with a bow), **Ch**ola **T**iger (roar), **P**andya **F**ish (Madurai's Meenakshi = 'fish-eyed')."},
 {"title": "Temple ↔ dynasty quick map",
  "body": "**Kailasa Ellora = Rashtrakuta (Krishna I)** · **Kailasanatha Kanchi = Pallava (Rajasimha)** · **Brihadeeswara = Chola (Rajaraja I)** · **Virupaksha Pattadakal = Chalukya**. Note 'Kailasa' vs 'Kailasanatha'.",
  "example": {"q": "Kailasanatha temple at Kanchipuram was built by —", "solution": "Kanchi → Pallava → **Narasimhavarman II (Rajasimha)**. (Ellora's Kailasa is Rashtrakuta.)"}},
 {"title": "Imperial Cholas: \"VAPRR\"",
  "body": "**V**ijayalaya → **A**ditya I → **P**arantaka I → **R**ajaraja I → **R**ajendra I."}
],
"mistakes": [
 "Kailasa temple at **Ellora** (Rashtrakuta) ≠ Kailasanatha temple at **Kanchipuram** (Pallava).",
 "Pulakeshin II **defeated** Harsha but was later **killed** by Pallava Narasimhavarman I.",
 "Silappadikaram (Ilango Adigal) ≠ Manimekalai (Sittalai Sattanar).",
 "Uttaramerur inscriptions belong to **Parantaka I**, not Rajaraja I."
]
})

# ---------------------------------------------------------------- 9. Literature
S.append({
"id": "ancient-literature",
"title": "Ancient Literature & Authors",
"concept": """**Sanskrit classics**

| Work | Author | Note |
|---|---|---|
| Ramayana | Valmiki | *Adi Kavya* |
| Mahabharata | Ved Vyasa | Originally *Jaya*; Bhagavad Gita is part of the Bhishma Parva |
| **Ashtadhyayi** | **Panini** | Sanskrit grammar |
| **Mahabhashya** | **Patanjali** | Commentary on Panini (Shunga age); also *Yoga Sutra* |
| **Arthashastra** | **Kautilya** | Statecraft |
| **Natyashastra** | **Bharata Muni** | Drama, dance, music |
| **Buddhacharita** | **Ashvaghosha** | Life of Buddha |
| **Abhijnanashakuntalam**, Meghadutam, Raghuvamsham, Kumarasambhavam, Malavikagnimitram, Vikramorvasiyam, Ritusamhara | **Kalidasa** | Gupta court |
| **Mudrarakshasa**, Devichandraguptam | **Vishakhadatta** | Mudrarakshasa = rise of Chandragupta Maurya |
| **Mrichchhakatika** ("Little Clay Cart") | **Shudraka** | Social drama |
| **Swapnavasavadatta** | **Bhasa** | Udayana–Vasavadatta story |
| **Kamasutra** | **Vatsyayana** | — |
| **Panchatantra** | **Vishnu Sharma** | Animal fables |
| Hitopadesha | Narayana Pandit | Fables |
| **Amarakosha** | **Amarasimha** | Sanskrit thesaurus |
| **Harshacharita**, Kadambari | **Banabhatta** | Harsha's court |
| Nagananda, Ratnavali, Priyadarshika | **Harshavardhana** | — |
| Kiratarjuniya | Bharavi | — |
| Shishupalavadha | Magha | — |
| Dashakumaracharita, Kavyadarsha | Dandin | — |
| Manusmriti | Manu | Law book |
| Brihatkatha | Gunadhya | In Paishachi Prakrit |
| Gathasaptashati | Hala (Satavahana) | Prakrit poems |
| Kavirajamarga | Amoghavarsha I | Kannada |
| Mattavilasa Prahasana | Mahendravarman I | Pallava farce |

**Science & medicine**

| Work | Author |
|---|---|
| **Charaka Samhita** | **Charaka** (medicine) |
| **Sushruta Samhita** | **Sushruta** (surgery, "father of surgery") |
| **Aryabhatiya** | **Aryabhata** |
| **Brihat Samhita**, Pancha Siddhantika | **Varahamihira** |
| **Brahmasphuta Siddhanta** | **Brahmagupta** |
| Ashtanga Hridaya | Vagbhata |

**Foreign accounts:** *Indica* – Megasthenes · *Fo-kwo-ki* – Fa-Hien · *Si-Yu-Ki* – Hiuen Tsang · *Periplus of the Erythraean Sea* – anonymous Greek sailor (1st century CE, Indo-Roman trade) · *Natural History* – Pliny the Elder · *Geography* – Ptolemy.""",
"formulas": [],
"tricks": [
 {"title": "Drama trio: \"Shudraka's Cart, Bhasa's Dream, Vishakha's Seal\"",
  "body": "*Mrichchhakatika* = little clay **cart** (Shudraka) · *Swapnavasavadatta* = **dream** of Vasavadatta (Bhasa) · *Mudrarakshasa* = Rakshasa's **seal/ring** (Vishakhadatta).",
  "example": {"q": "Which play deals with Chanakya outwitting the Nanda minister Rakshasa?", "solution": "'Seal of Rakshasa' → **Mudrarakshasa** by **Vishakhadatta**."}},
 {"title": "Medicine pair: \"Charaka Cures, Sushruta Stitches\"",
  "body": "Charaka Samhita = general medicine (Kanishka's physician); Sushruta Samhita = surgery (plastic surgery, cataract)."}
],
"mistakes": [
 "Patanjali wrote both the *Mahabhashya* (grammar) and is credited with the *Yoga Sutra* — Panini wrote the *Ashtadhyayi*.",
 "Harshacharita is by **Banabhatta**; Harsha's own works are Nagananda, Ratnavali, Priyadarshika.",
 "Amarakosha (Amarasimha) is a dictionary, not a Buddhist text."
]
})

# ---------------------------------------------------------------- PYQ patterns
P = [
 {"pattern": "Harappan site ↔ river / state / excavator / signature find", "frequency": "very common",
  "howToSpot": "Stem names a find (dockyard, Great Bath, ploughed field, dancing girl) or asks which state a site is in.",
  "approach": "Use the site table; first split India vs Pakistan sites, then Gujarat vs Haryana vs Rajasthan."},
 {"pattern": "Buddhist / Jain councils — place, king, president", "frequency": "very common",
  "howToSpot": "'Which council was presided by…' or 'held at Vaishali…'.",
  "approach": "Recall the A-K-A-K king chain and Raj-Vaish-Pat-Kash place chain; presidents Maha-Saba-Moggali-Vasu."},
 {"pattern": "Book ↔ author (Sanskrit, Sangam, scientific)", "frequency": "very common",
  "howToSpot": "'… was written by' / 'author of'.",
  "approach": "Group by court: Kalidasa & Amarasimha (Gupta), Banabhatta (Harsha), Ashvaghosha & Charaka (Kanishka)."},
 {"pattern": "Dynasty founder / capital / greatest ruler", "frequency": "common",
  "howToSpot": "'Capital of the Satavahanas', 'founder of the Rashtrakutas'.",
  "approach": "Memorise the south-dynasty table row-wise: capital-founder-temple."},
 {"pattern": "Ashokan edicts & Prashasti authors", "frequency": "common",
  "howToSpot": "Rock edict number, script, 'Devanampiya', Prayag/Aihole/Junagadh inscription.",
  "approach": "2-5-12-13 edict anchors; Harishena–Samudragupta, Ravikirti–Pulakeshin II, Rudradaman–Sanskrit."},
 {"pattern": "Foreign traveller / ambassador ↔ Indian ruler", "frequency": "common",
  "howToSpot": "Megasthenes, Deimachus, Fa-Hien, Hiuen Tsang, I-Tsing in the stem or options.",
  "approach": "M-D for Mauryas (Chandragupta, Bindusara); F-H-I in chronological order for Chinese pilgrims."},
 {"pattern": "Vedic texts — mandala contents, Upanishad sources, river names", "frequency": "common",
  "howToSpot": "Gayatri, Soma, Purusha Sukta, Satyameva Jayate, Parushni/Vitasta.",
  "approach": "Mandala anchors 3-7-9-10; V-A-P-V-S river chain."},
 {"pattern": "Mahajanapada ↔ capital", "frequency": "occasional",
  "howToSpot": "Direct pair or 'which is correctly matched'.",
  "approach": "Know the 6 tricky ones: Avanti-Ujjain, Vatsa-Kaushambi, Kosala-Shravasti, Anga-Champa, Assaka-Potana, Matsya-Viratnagar."}
]

# ---------------------------------------------------------------- Solved examples
SE = [
 Q("anc-ex01", "At which Harappan site has evidence of a **dockyard** been found?",
   ["Kalibangan", "Lothal", "Dholavira", "Banawali"], 1,
   "**Lothal** (Ahmedabad district, Gujarat), on the Bhogava river, has a large brick basin identified as a **dockyard** — proof of Harappan maritime trade. It was excavated by **S.R. Rao**.\n\nAlso remember: Kalibangan – ploughed field; Dholavira – water reservoirs; Banawali – clay plough model.",
   "Mnemonic: **L**othal = **L**aunch (boats). Eliminate Kalibangan (field) and Dholavira (water tanks) at once.",
   "easy", "indus-valley", "Harappan site ↔ signature find", 20),
 Q("anc-ex02", "The **Fourth Buddhist Council** held in Kashmir under Kanishka was presided over by —",
   ["Mahakassapa", "Moggaliputta Tissa", "Vasumitra", "Sabakami"], 2,
   "The 4th Council (c. 72 CE, **Kundalvana, Kashmir**) was held under **Kanishka** with **Vasumitra** as president and **Ashvaghosha** as vice-president. Buddhism split into **Hinayana and Mahayana**.\n\n- 1st – Mahakassapa (Rajagriha, Ajatashatru)\n- 2nd – Sabakami (Vaishali, Kalashoka)\n- 3rd – Moggaliputta Tissa (Pataliputra, Ashoka)",
   "Presidents in order: **Maha-Saba-Moggali-Vasu** → 4th = **Vasu**mitra.",
   "medium", "buddhism-jainism", "Buddhist council ↔ president", 25),
 Q("anc-ex03", "Who wrote the **Harshacharita**, the biography of king Harshavardhana?",
   ["Harishena", "Banabhatta", "Ravikirti", "Kalhana"], 1,
   "**Banabhatta**, court poet of Harsha, wrote **Harshacharita** and the prose romance **Kadambari**.\n\nTraps: Harishena wrote Samudragupta's *Prayag Prashasti*; Ravikirti wrote Pulakeshin II's *Aihole inscription*; Kalhana wrote *Rajatarangini* (Kashmir, 12th century).",
   "Court-poet pairs: Harsha–**Bana**, Samudragupta–Harishena, Pulakeshin II–Ravikirti.",
   "easy", "gupta-harsha", "Book ↔ author", 20),
 Q("anc-ex04", "The river called **Parushni** in the Rigveda is known today as —",
   ["Beas", "Chenab", "Ravi", "Jhelum"], 2,
   "Rigvedic names: Vitasta = Jhelum, Asikni = Chenab, **Parushni = Ravi**, Vipas = Beas, Sutudri = Sutlej. The **Battle of Ten Kings** was fought on the Parushni, where **Sudas** of the Bharatas won.",
   "\"Very Angry Parrots Visit Sutlej\" ↔ J-C-R-B-S: the 3rd letter **P** matches the 3rd river **R**avi.",
   "medium", "vedic-age", "Rigvedic river ↔ modern name", 25),
]

# ---------------------------------------------------------------- Practice (15)
PR = [
 Q("anc-q01", "The **Great Bath** of the Indus Valley Civilisation was found at —",
   ["Mohenjo-daro", "Harappa", "Lothal", "Ropar"], 0,
   "The **Great Bath**, a brick tank with steps at both ends and a water-proof bitumen lining, is at **Mohenjo-daro** (Larkana, Sindh). Mohenjo-daro also gave the Great Granary, the bronze dancing girl and the bearded priest.",
   "Mohenjo = **M**ajestic bath.", "easy", "indus-valley", "Harappan site ↔ signature find", 20),
 Q("anc-q02", "Evidence of a **ploughed field** belonging to the Harappan period has been discovered at —",
   ["Banawali", "Chanhudaro", "Kalibangan", "Surkotada"], 2,
   "**Kalibangan** (Hanumangarh, Rajasthan, on the Ghaggar) shows a ploughed field with criss-cross furrows, plus fire altars. The name means 'black bangles'.\n\nTrap: Banawali (Haryana) has a **clay model** of a plough, not a field.",
   "**Kali**bangan = **Kheti** (field). Model plough → Banawali.", "medium", "indus-valley", "Harappan site ↔ signature find", 25),
 Q("anc-q03", "Which mandala of the Rigveda is **entirely devoted to Soma**?",
   ["Third mandala", "Seventh mandala", "Tenth mandala", "Ninth mandala"], 3,
   "The **Ninth mandala** of the Rigveda is wholly addressed to **Soma** (the sacred drink/deity). Mandala III has the Gayatri Mantra, VII the Battle of Ten Kings, X the Purusha Sukta.",
   "Anchors **3-7-9-10** → Gayatri, Ten Kings, **Soma**, Purusha Sukta.", "medium", "vedic-age", "Rigveda mandala contents", 25),
 Q("anc-q04", "What was the capital of the **Avanti** Mahajanapada (northern part)?",
   ["Kaushambi", "Ujjain", "Shravasti", "Champa"], 1,
   "Avanti (Malwa) had two capitals — **Ujjain** in the north and **Mahishmati** in the south. Kaushambi = Vatsa, Shravasti = Kosala, Champa = Anga.",
   "**A**vanti ↔ Ujjain; the other A-kingdom, **A**nga ↔ Champa.", "easy", "mahajanapadas", "Mahajanapada ↔ capital", 20),
 Q("anc-q05", "Gautama Buddha delivered his **first sermon** at —",
   ["Bodh Gaya", "Kushinagar", "Sarnath", "Lumbini"], 2,
   "The first sermon (*Dharmachakra-pravartana*, 'turning the wheel of law') was given at the Deer Park, **Sarnath**, near Varanasi. Birth – Lumbini; enlightenment – Bodh Gaya; death – Kushinagar.",
   "Life order L-B-S-K: **L**umbini, **B**odh Gaya, **S**arnath, **K**ushinagar.", "easy", "buddhism-jainism", "Buddha's life — places", 15),
 Q("anc-q06", "Who was the **23rd Tirthankara** of Jainism?",
   ["Parshvanatha", "Rishabhanatha", "Neminatha", "Mahavira"], 0,
   "**Parshvanatha**, a prince of Varanasi (son of king Ashvasena), was the 23rd Tirthankara; his symbol is the **snake** and he preached four vows. Mahavira (24th) added Brahmacharya.",
   "Symbols: 1 bull, 22 conch, 23 **snake**, 24 lion.", "easy", "buddhism-jainism", "Tirthankara identification", 15),
 Q("anc-q07", "Megasthenes came to the court of Chandragupta Maurya as the ambassador of —",
   ["Antiochus I", "Alexander", "Seleucus Nicator", "Darius I"], 2,
   "**Megasthenes** was sent by **Seleucus Nicator** after the treaty of 305 BCE and wrote ***Indica***. Deimachus came from **Antiochus I** to Bindusara's court.",
   "**M**egasthenes ↔ **M**aurya founder ↔ **S**eleucus (the defeated general). Deimachus ↔ Bindusara.", "easy", "mauryan-empire", "Foreign envoy ↔ Indian ruler", 20),
 Q("anc-q08", "Which of Ashoka's **Major Rock Edicts** describes the Kalinga war and the king's remorse?",
   ["Rock Edict II", "Rock Edict XII", "Rock Edict V", "Rock Edict XIII"], 3,
   "**Rock Edict XIII** records the conquest of Kalinga (c. 261 BCE), the deaths and deportations, Ashoka's repentance and his preference for *dhamma-vijaya*. RE II – medical care; RE V – Dhamma Mahamattas; RE XII – religious tolerance.",
   "Unlucky **13** = war.", "medium", "mauryan-empire", "Ashokan edict content", 25),
 Q("anc-q09", "In which inscription is the Mauryan emperor mentioned by his personal name **'Ashoka'** rather than as 'Devanampiya Piyadasi'?",
   ["Maski", "Dhauli", "Girnar", "Kalsi"], 0,
   "The **Maski** minor rock edict (Raichur district, Karnataka), found in 1915, was the first to name the king as **Ashoka**; the name also appears at Gujarra, Nittur and Udegolam. Dhauli, Girnar and Kalsi carry Major Rock Edicts that use *Devanampiya Piyadasi*.",
   "Major Rock Edict sites (Girnar, Kalsi, Dhauli) never use the name — pick the **minor** edict site.", "hard", "mauryan-empire", "Ashokan inscription facts", 30),
 Q("anc-q10", "The **Shaka era**, used for India's national calendar, was started in 78 CE by —",
   ["Rudradaman I", "Menander", "Kanishka", "Gautamiputra Satakarni"], 2,
   "The Shaka Samvat (78 CE) is traditionally credited to the Kushana king **Kanishka**. It was adopted as the base of India's **National Calendar** (from 22 March 1957). Vikram Samvat starts in 57 BCE.",
   "\"57 minus, 78 plus\" — 78 CE = Kanishka's accession.", "medium", "post-mauryan", "Era ↔ founder", 20),
 Q("anc-q11", "The capital of the **Satavahana** kingdom was —",
   ["Vatapi", "Pratishthana", "Manyakheta", "Kanchipuram"], 1,
   "The Satavahanas ruled from **Pratishthana (Paithan)** on the Godavari (Maharashtra). Vatapi = Chalukyas of Badami; Manyakheta = Rashtrakutas; Kanchipuram = Pallavas.",
   "Satavahana = **S-P-G-H** (Simuka, **P**ratishthana, Gautamiputra, Hala).", "medium", "post-mauryan", "Dynasty ↔ capital", 20),
 Q("anc-q12", "The **Prayag Prashasti** inscribed on the Allahabad pillar, praising Samudragupta, was composed by —",
   ["Ravikirti", "Banabhatta", "Kalidasa", "Harishena"], 3,
   "**Harishena**, Samudragupta's court poet and minister, composed the Prayag Prashasti (Allahabad pillar, which also carries Ashokan edicts). It lists Samudragupta's campaigns in the north and the south.",
   "**H**arishena → Samudragupta's **H**onour roll; Ravikirti → Aihole.", "medium", "gupta-harsha", "Prashasti ↔ composer", 25),
 Q("anc-q13", "The Chinese pilgrim **Fa-Hien** visited India during the reign of —",
   ["Chandragupta II", "Harshavardhana", "Samudragupta", "Kumaragupta I"], 0,
   "**Fa-Hien (Faxian)** travelled in India c. 399–414 CE in the reign of **Chandragupta II Vikramaditya** and wrote *Fo-kwo-ki*. Hiuen Tsang came under Harsha (7th century).",
   "F-H-I order: **F**a-Hien is the earliest → Gupta peak (Chandragupta II).", "medium", "gupta-harsha", "Foreign traveller ↔ ruler", 20),
 Q("anc-q14", "Consider the following statements:\n1. The Kailasa temple at Ellora was built by the Rashtrakuta king Krishna I.\n2. The Shore Temple at Mahabalipuram was built by the Pallava king Narasimhavarman II (Rajasimha).\n3. The Brihadeeswara temple at Thanjavur was built by Rajendra I.\n\nWhich of the statements given above is/are correct?",
   ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 1,
   "1 ✔ — Kailasa (Cave 16), Ellora: **Krishna I** (Rashtrakuta).\n2 ✔ — Shore Temple: **Narasimhavarman II (Rajasimha)**.\n3 ✘ — Brihadeeswara, Thanjavur: **Rajaraja I** (c. 1010). His son Rajendra I built the temple at **Gangaikondacholapuram**.",
   "Statement 3 swaps father and son — once it is wrong, options C and D go; 1 is the well-known fact, so choose **1 and 2**.",
   "hard", "south-dynasties", "Temple ↔ dynasty/king (statement type)", 40),
 Q("anc-q15", "The Sanskrit play **Mrichchhakatika** ('The Little Clay Cart') was written by —",
   ["Bhasa", "Shudraka", "Vishakhadatta", "Dandin"], 1,
   "**Shudraka** wrote *Mrichchhakatika*, a social drama about the Brahmin Charudatta and the courtesan Vasantasena. Bhasa – *Swapnavasavadatta*; Vishakhadatta – *Mudrarakshasa*; Dandin – *Dashakumaracharita*.",
   "\"Shudraka's **Cart**, Bhasa's Dream, Vishakha's Seal\".", "hard", "ancient-literature", "Book ↔ author", 25),
]

topic = {
 "id": "ancient-history",
 "sectionId": "ga",
 "title": "Ancient Indian History",
 "order": 1,
 "importance": "medium",
 "avgQuestions": {"tier1": 1, "tier2": 1},
 "summary": "From the Harappan cities to the Cholas: sites and finds, Vedic texts, Buddhism & Jainism, Mauryas, Guptas, Harsha and the southern dynasties. SSC asks 1–2 direct fact questions per shift — mostly pairings (site–find, council–king, book–author, dynasty–capital), so tables and mnemonics give quick marks.",
 "subtopics": S,
 "pyqPatterns": P,
 "solvedExamples": SE,
 "practice": PR,
}

if __name__ == "__main__":
    save_topic(topic)
