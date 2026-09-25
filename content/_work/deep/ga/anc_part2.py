"""ancient-history deep content — part 2: mauryan, post-mauryan, gupta-harsha, south, literature."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_mauryan():
    S = Sub("mauryan-empire")
    S.notes = """### The first all-India empire
In **322 BCE** **Chandragupta Maurya**, guided by his guru **Kautilya (Chanakya)** — author of the *Arthashastra* on statecraft — overthrew **Dhana Nanda** and founded the Mauryan empire with its capital at **Pataliputra**. At his court lived the Greek ambassador **Megasthenes**, whose book *Indica* (surviving in fragments) describes Pataliputra, the army and the absence of slavery in the Greek sense. In **305 BCE** Chandragupta faced **Seleucus Nicator**, Alexander's general; the treaty gave Seleucus **500 war elephants** while Chandragupta received the eastern satrapies (Kabul–Kandahar–Herat–Makran belt) and a marriage alliance. **Bindusara** ('slayer of foes', *Amitraghata*) kept the Greek envoy **Deimachus** at court. **Ashoka** (c. 268–232 BCE) fought the **Kalinga war in 261 BCE** (his 8th regnal year); the horror of it turned him to **Dhamma** — not a new religion, but a code of ethics: tolerance, ahimsa, kindness to servants and animals, respect for all sects, welfare works (roads, wells, rest houses).

### The edicts
Ashoka's messages are carved on rocks and polished pillars in **Prakrit**, mostly in the **Brahmi script** (Kharosthi in the north-west; a Greek–Aramaic bilingual at Kandahar). They were deciphered by **James Prinsep in 1837**. Key items:
- **Major Rock Edict XIII** — the Kalinga war and the king's remorse; names five Greek kings as neighbours in Dhamma.
- **Major Rock Edict XII** — tolerance and respect for all sects.
- **Bhabru (Bairat) edict** — the Buddha, Dhamma and Sangha.
- **Rummindei pillar** — visit to Lumbini (the Buddha's birthplace); village tax reduced to one-eighth.
- **Schism edicts** — unity of the Sangha.
- **Dhamma Mahamatras** — special officers appointed (RE V) to spread Dhamma.

### Administration — a machine state
The king stood at the top, advised by the **mantriparishad** (council of ministers). Provinces (Taxila, Ujjain, Tosali, Suvarnagiri, Pataliputra) were headed by princes (**Kumara**/**Aryaputra**). Revenue officers: **Samaharta** (collection), **Sannidhata** (treasurer–storekeeper), yuktas as accountants; district level **Pradeshika**, **Rajuka** (survey) and **Sthanika**; the village head was the **gramika**. A spy network of **gudhapurusha** ran in two wings — *sanstha* (stationary) and *sanchara* (wandering). Megasthenes counted an army of about 6 lakh infantry, 30,000 cavalry and 9,000 elephants. The state monopolised **mines, salt and liquor** and ran irrigation and roads.

### Mauryan art and architecture
Court art is monolithic and polished: **pillars of Chunar sandstone** with animal capitals — the **Sarnath Lion Capital** (four lions back to back, wheel on the abacus) became India's **National Emblem** on 26 January 1950. Stupa cores at **Sanchi** and the Dharmarajika date to Ashoka; the **Barabar (and Nagarjuni) hill caves** were gifted to the **Ajivika** sect — India's earliest rock-cut caves (Lomas Rishi's chaitya-arch facade). Folk art produced the **Yaksha–Yakshini** statues (e.g. the Didarganj Yakshini with a fly-whisk).

### Decline
Later rulers (Dasharatha onwards) were weak. The empire broke under money trouble, over-centralisation, Greek pressure on the north-west and religious reaction. The last Mauryan king, **Brihadratha**, was killed by his commander **Pushyamitra Sunga in 185 BCE**, who founded the Sunga dynasty.

### Quick revision
- 322 BCE Chandragupta + Chanakya end the Nandas; Megasthenes (*Indica*) at court; Deimachus under Bindusara.
- Seleucus treaty 305 BCE: 500 elephants for eastern satrapies + marriage alliance.
- Kalinga 261 BCE → Dhamma; edicts in Prakrit/Brahmi; deciphered by Prinsep (1837).
- RE XIII = Kalinga remorse; RE XII = tolerance; Bhabru = Buddha-Dhamma-Sangha; Rummindei = Lumbini tax cut.
- Officers: Samaharta (collection), Sannidhata (treasury), Rajuka (survey), gudhapurusha spies (sanstha/sanchara).
- Sarnath Lion Capital = National Emblem; Barabar caves = Ajivikas; 185 BCE Brihadratha → Pushyamitra Sunga."""
    S.pattern("ga-mau-p1", "Ashoka's edicts: which edict carries which message", "very common",
        "'Which edict describes the Kalinga war', 'where does Ashoka's personal name appear', 'what does the Bhabru edict say', script/language of inscriptions.",
        None,
        "1. Anchor edicts: **RE XIII = Kalinga remorse**, **RE XII = tolerance**, **Bhabru = Buddha-Dhamma-Sangha**, **Rummindei = Lumbini + tax remission**.\n2. Ashoka's personal name appears only in **Maski, Gujarra, Nettur, Udegolam** (Minor Rock Edicts); elsewhere 'Devanampiya Piyadasi'.\n3. Language/script: Prakrit + Brahmi mostly; Kharosthi in the north-west; Greek-Aramaic at Kandahar; deciphered by James Prinsep (1837).",
        "Which Ashokan edict records the king's faith in the **Buddha, Dhamma and Sangha**?",
        "The **Bhabru (Bairat) edict** — a Minor Rock Edict found near Jaipur, Rajasthan.")
    S.pattern("ga-mau-p2", "Mauryan administration: officers and machinery", "common",
        "'Who was Samaharta/Sannidhata', spy wings sanstha-sanchara, provincial governors, Dhamma Mahamatras.",
        None,
        "1. Revenue pair: **Samaharta = collector**, **Sannidhata = treasurer/storekeeper**.\n2. Field officers: Pradeshika (district), Rajuka (survey/revenue), Sthanika, Gramika (village).\n3. Spies: gudhapurusha — sanstha (stationary) and sanchara (wandering); provinces under Kumara princes.",
        "In Mauryan administration, the officer responsible for the **collection of revenue** was the —",
        "**Samaharta**; the **Sannidhata** kept the treasury and storehouses.")
    S.pattern("ga-mau-p3", "Chandragupta, Chanakya and the Greeks", "common",
        "Founding of the empire, the Arthashastra, the Seleucus treaty terms, Megasthenes' Indica.",
        None,
        "1. 322 BCE: Chandragupta + Kautilya end Dhana Nanda's rule.\n2. Seleucus treaty (305 BCE): **500 elephants ↔ eastern satrapies + marriage alliance**.\n3. Visitors: Megasthenes (Chandragupta, *Indica*), Deimachus (Bindusara), Ptolemy's ambassador Dionysius (Ashoka).",
        "Under the Maurya–Seleucus treaty (305 BCE), Chandragupta handed over to Seleucus —",
        "**500 war elephants**; in return he received the eastern satrapies (Kabul–Kandahar–Herat–Makran) and a marriage alliance.")
    S.pattern("ga-mau-p4", "Mauryan art, architecture and the dynasty's end", "common",
        "Lion Capital and National Emblem, Barabar caves, polished pillars, stupa cores, Brihadratha–Pushyamitra Sunga.",
        None,
        "1. Court art: polished Chunar-sandstone pillars; **Sarnath Lion Capital = National Emblem** (26 Jan 1950).\n2. **Barabar caves = Ajivika sect** — earliest rock-cut caves; Sanchi stupa core is Mauryan.\n3. End: **Brihadratha killed by Pushyamitra Sunga, 185 BCE** → Sunga dynasty.",
        "The Barabar hill caves, excavated in the Mauryan period, were dedicated to which sect?",
        "The **Ajivika** sect — they are the oldest surviving rock-cut caves of India, with the Lomas Rishi chaitya-arch facade.")

    S.q("ga-mau-p1", "easy", "Which **Major Rock Edict** of Ashoka preaches tolerance and respect for all sects?",
        ["Rock Edict II", "Rock Edict XII", "Rock Edict VII", "Rock Edict XIV"], "Rock Edict XII",
        "**Rock Edict XII** urges every sect to honour the other — the classic statement of Ashoka's religious tolerance. Rock Edict XIII carries the Kalinga remorse.",
        "XIII = Kalinga; XII = tolerance.", 20)
    S.q("ga-mau-p1", "easy", "The Mauryan inscriptions were mostly written in which **language and script**?",
        ["Sanskrit in Brahmi", "Prakrit in Brahmi", "Pali in Kharosthi", "Prakrit in Greek"], "Prakrit in Brahmi",
        "Most inscriptions are in **Prakrit** using the **Brahmi** script; Kharosthi appears in the north-west and a Greek–Aramaic bilingual at Kandahar.",
        "Prakrit-Brahmi is the default pair.", 20)
    S.q("ga-mau-p1", "medium", "The **Rummindei Pillar inscription** of Ashoka records —",
        ["The Kalinga war and its aftermath", "His visit to Lumbini and reduction of the village's tax", "Instructions to his provincial governors", "The prohibition of animal sacrifice"], "His visit to Lumbini and reduction of the village's tax",
        "The Rummindei (Niglihawa-related site) pillar records Ashoka's visit to **Lumbini**, the Buddha's birthplace, and the village's **bali tax cut to one-eighth**.",
        "Rummindei = Lumbini = tax cut to 1/8.", 25)
    S.q("ga-mau-p2", "easy", "Which Mauryan officer kept charge of the **treasury and storehouses**?",
        ["Samaharta", "Sannidhata", "Rajuka", "Gramika"], "Sannidhata",
        "The **Sannidhata** was treasurer–storekeeper; the **Samaharta** collected revenue; **Rajukas** measured land; **Gramika** headed the village.",
        "Samaharta = 'takes in' revenue; Sannidhata = 'keeps' it.", 20)
    S.q("ga-mau-p2", "hard", "Match the Mauryan officers with their work:\n1. Rajuka — land survey and revenue\n2. Pradeshika — district head\n3. Sanchara — wandering spy\nWhich pairs are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three are correct: **Rajuka** surveyed land and fixed revenue, **Pradeshika** headed the district administration, and **sanchara** gudhapurushas were the wandering spies (sanstha = stationary).",
        "Every pairing here is straight from the Mauryan officer list — check, don't guess.", 30)
    S.q("ga-mau-p3", "easy", "The Mauryan empire was founded in **322 BCE** when Chandragupta Maurya overthrew —",
        ["Ajatashatru", "Dhana Nanda", "Kalashoka", "Seleucus Nicator"], "Dhana Nanda",
        "Chandragupta Maurya, helped by **Chanakya (Kautilya)**, overthrew **Dhana Nanda**, the last Nanda ruler of Magadha, in **322 BCE**.",
        "Nanda in, Maurya out — 322 BCE.", 20)
    S.q("ga-mau-p3", "medium", "Which Greek ambassador came to **Bindusara's** court?",
        ["Megasthenes", "Deimachus", "Dionysius", "Ptolemy"], "Deimachus",
        "**Deimachus** was sent by the Syrian king Antiochus I to Bindusara. Megasthenes came to Chandragupta; Dionysius was sent to Ashoka by Ptolemy II.",
        "Chandragupta-Megasthenes, Bindusara-Deimachus, Ashoka-Dionysius.", 25)
    S.q("ga-mau-p4", "easy", "The Lion Capital found at **Sarnath** was adopted as India's **National Emblem** in —",
        ["1947", "1950", "1952", "1956"], "1950",
        "Ashoka's **Sarnath Lion Capital** became the National Emblem on **26 January 1950**, with 'Satyameva Jayate' (Mundaka Upanishad) below it.",
        "Republic Day 1950 = emblem adopted.", 20)
    S.q("ga-mau-p4", "medium", "The last Mauryan ruler **Brihadratha** was killed by his Brahmana commander —",
        ["Vasumitra", "Pushyamitra Sunga", "Agnimitra", "Patanjali"], "Pushyamitra Sunga",
        "In **185 BCE** **Pushyamitra Sunga** murdered Brihadratha at an army review and founded the **Sunga dynasty**. Agnimitra was his son; Vasumitra his grandson.",
        "185 BCE — Maurya out, Sunga in.", 25)
    return S


def build_post():
    S = Sub("post-mauryan")
    S.notes = """### After the Mauryas — a crowd of dynasties
Pushyamitra Sunga (185–73 BCE) ruled from Pataliputra with Vidisha as a second centre; the grammarian **Patanjali** (*Mahabhashya*) adorned his age, and existing stupas (Sanchi, Bharhut railings) were expanded. The **Kanvas** (73–28 BCE) succeeded briefly. Then wave after wave of Central-Asian people entered through the north-west.
- **Indo-Greeks (Bactrian Greeks):** best king **Menander (Milinda)**, whose dialogues with the monk **Nagasena** form the *Milindapanha*; they were the **first to issue coins bearing kings' portraits**.
- **Shakas:** five branches; the western branch of Ujjain produced **Rudradaman I** (c. 130 CE), whose **Junagadh rock inscription** is the **first long inscription in chaste Sanskrit** and records the repair of **Sudarshana lake**.
- **Parthians (Pahlavas):** **Gondophernes** is linked in tradition with St Thomas's arrival.
- **Kushanas:** the greatest of them all.

### The Kushanas
**Kujula Kadphises** united the five Yuezhi clans; **Vima Kadphises** issued India's **first gold coins**; **Kanishka** (from **78 CE**, the **Shaka era** used in India's national calendar) ruled from **Purushpura (Peshawar)** with **Mathura** as a second capital. Kanishka patronised the **Fourth Buddhist Council** (Kashmir) — after which Buddhism split into **Hinayana and Mahayana** — and scholars **Ashvaghosha** (*Buddhacharita*), **Charaka** (*Charaka Samhita*), **Vasumitra** and **Nagarjuna**. Two art schools flowered: **Gandhara** (Greco-Buddhist style, grey schist) and **Mathura** (indigenous, red sandstone). Kushana control of the **Silk Road** fed the economy.

### The Satavahanas of the Deccan
Founded by **Simuka** (c. 1st century BCE), with the capital at **Pratishthana (Paithan on the Godavari)**; their coins say 'Andhra'. The greatest ruler **Gautamiputra Satakarni** — 'destroyer of Kshatriyas', 'lord of the Andhra race' — is known chiefly from the **Nasik inscription of his mother, Gautami Balashri**. The Satavahanas were the **first dynasty to make land grants to Brahmanas** (tax-free), a seed of the feudal age; they issued **lead and potin coins** and used **Prakrit**. Their ports (Kalyan, Sopara) carried the Roman trade; their society shows **nahapana-erased coins** and, in some areas, cross-cousin marriage and mothers named on coins (a non-Sanskritic touch).

### Indo-Roman trade
The *Periplus of the Erythraean Sea* and Sangam poems describe Yavana traders at Indian ports: **Tamralipti** (Ganga delta, east), **Bharuch (Bhrigukachchha)** and Sopara (west), **Muziris** (Kerala) and **Arikamedu** (near Pondicherry — arretine Roman pottery, beads, Roman lamps). Big hoards of **Roman gold coins** show the trade balance ran in India's favour — Pliny complained that Rome drained gold for pepper, pearls and textiles.

### Quick revision
- Order of NW entries: Indo-Greeks → Shakas → Parthians → Kushanas; Sunga → Kanva in the heartland.
- Menander-Nagasena = Milindapanha; Indo-Greeks = first portrait coins; Rudradaman = first chaste-Sanskrit inscription + Sudarshana lake.
- Kushana chain: Kujula → **Vima Kadphises (first gold)** → **Kanishka (78 CE Shaka era; Peshawar + Mathura)**.
- Kanishka's circle: Ashvaghosha, Charaka, Vasumitra, Nagarjuna; Gandhara & Mathura art.
- Satavahanas: Simuka → Pratishthana; Gautamiputra Satakarni (mother's Nasik inscription); first Brahmana land grants; lead-potin coins.
- Trade ports: Tamralipti (E), Bharuch (W), Muziris, Arikamedu (Roman finds)."""
    S.pattern("ga-post-p1", "Post-Mauryan dynasties in order and their kings", "very common",
        "'Which dynasty came after the Sungas', 'Rudradaman belonged to', ordering Sunga-Kanva-Indo-Greek-Shaka-Parthian-Kushana.",
        None,
        "1. Heartland chain: **Sunga (185-73 BCE) → Kanva (73-28 BCE)**; NW entries in order **Indo-Greeks → Shakas → Parthians → Kushanas**.\n2. King hooks: Menander = Indo-Greek; Rudradaman I = Shaka (Ujjain); Gondophernes = Parthian; Kanishka = Kushana.\n3. Rudradaman's Junagadh inscription = first long chaste-Sanskrit record + Sudarshana lake repair.",
        "Who repaired the **Sudarshana lake** and issued the first long inscription in chaste Sanskrit?",
        "**Rudradaman I**, the Shaka ruler of Ujjain — his Junagadh rock inscription (c. 130 CE).")
    S.pattern("ga-post-p2", "Kushanas: Kanishka and his age", "very common",
        "'The Shaka era was started by', first gold coins, Kanishka's capitals, Gandhara vs Mathura art, scholars at his court.",
        None,
        "1. Coin chain: Indo-Greeks = portraits; **Vima Kadphises = first gold**; Satavahanas = lead/potin; Kushanas = gold dynasty.\n2. Kanishka: **78 CE = Shaka era**; capitals **Purushpura (Peshawar)** + Mathura; 4th Council; Hinayana/Mahayana split.\n3. Court circle: Ashvaghosha, Charaka, Vasumitra, Nagarjuna; art: Gandhara (Greco-Buddhist) and Mathura (red sandstone).",
        "Which Kushana ruler first issued **gold coins** in India?",
        "**Vima Kadphises** — Kanishka's father; Kanishka continued the gold coinage on Roman-standard weights.")
    S.pattern("ga-post-p3", "Satavahanas: rulers, capital and social practice", "common",
        "'Capital of the Satavahanas', Gautamiputra Satakarni's titles, first land grants, lead-potin coins, Prakrit language.",
        None,
        "1. Founders and place: **Simuka**; capital **Pratishthana (Paithan)** on the Godavari.\n2. Greatest king **Gautamiputra Satakarni** — 'destroyer of Kshatriyas'; evidence = mother **Gautami Balashri's Nasik inscription**.\n3. Firsts: **first land grants to Brahmanas**; coins in **lead and potin**; language Prakrit.",
        "The greatest Satavahana ruler, called the 'destroyer of Kshatriyas', was —",
        "**Gautamiputra Satakarni**, known from his mother **Gautami Balashri's** inscription at Nasik.")
    S.pattern("ga-post-p4", "Indo-Roman trade: ports, goods, coins", "common",
        "'Arikamedu is famous for', 'the main east-coast port', Roman gold hoards, Periplus of the Erythraean Sea.",
        None,
        "1. Ports: **Tamralipti** (east, Ganga delta), **Bharuch/Bhrigukachchha** and Sopara (west), **Muziris** (Kerala), **Arikamedu** (Coromandel).\n2. Arikamedu = arretine Roman pottery, lamps, beads — a Roman trading post.\n3. Roman gold coin hoards = trade surplus for India; *Periplus of the Erythraean Sea* is the Greek sailing guide.",
        "Which post-Mauryan coastal site in the south is famous for **Roman pottery** and trade goods?",
        "**Arikamedu** (near Pondicherry) — arretine ware, Roman lamps and beads prove direct Indo-Roman trade.")

    S.q("ga-post-p1", "easy", "Which dynasty was founded in **185 BCE** after the fall of the Mauryas?",
        ["Kanva", "Sunga", "Satavahana", "Indo-Greek"], "Sunga",
        "**Pushyamitra Sunga** killed Brihadratha in 185 BCE and founded the **Sunga dynasty**. The Kanvas followed (73–28 BCE).",
        "Maurya → Sunga → Kanva.", 20)
    S.q("ga-post-p1", "hard", "Arrange the north-western foreign dynasties in the order they entered India:\n1. Kushanas  2. Indo-Greeks  3. Parthians  4. Shakas",
        ["2, 4, 3, 1", "4, 2, 1, 3", "2, 3, 4, 1", "4, 3, 2, 1"], "2, 4, 3, 1",
        "Order of entry: **Indo-Greeks → Shakas → Parthians → Kushanas**.",
        "Mnemonic 'I Shall Prefer Kushanas' — Indo-Greek, Shaka, Parthian, Kushana.", 30)
    S.q("ga-post-p2", "easy", "Kanishka ruled from **Purushpura**; his second capital in India was —",
        ["Ujjain", "Mathura", "Taxila", "Kannauj"], "Mathura",
        "Kanishka's capitals were **Purushpura (Peshawar)** and **Mathura**. The Mathura art school also flourished under the Kushanas.",
        "Peshawar + Mathura, the Kushana pair.", 20)
    S.q("ga-post-p2", "medium", "Which art school shows the Buddha with **Greek-Roman features** (wavy hair, drapery like a Greek toga)?",
        ["Mathura school", "Gandhara school", "Amaravati school", "Mauryan court art"], "Gandhara school",
        "The **Gandhara school** (grey schist, Hellenistic influence) shows Greco-Roman realism; **Mathura** used red sandstone with indigenous style; **Amaravati** worked in white marble on narrative panels.",
        "Greek features = Gandhara.", 25)
    S.q("ga-post-p2", "medium", "Which scholar of Kanishka's court wrote the **Charaka Samhita**, a classic of Ayurveda?",
        ["Nagarjuna", "Ashvaghosha", "Charaka", "Vasumitra"], "Charaka",
        "**Charaka**, the court physician of Kanishka, compiled the *Charaka Samhita*. Ashvaghosha wrote *Buddhacharita*; Vasumitra presided over the 4th Council; Nagarjuna founded the Madhyamika school.",
        "Charaka = medicine; Ashvaghosha = poetry.", 25)
    S.q("ga-post-p3", "easy", "The Satavahana kingdom was founded by —",
        ["Gautamiputra Satakarni", "Simuka", "Hala", "Pulomavi"], "Simuka",
        "**Simuka** founded the Satavahana line (c. 1st century BCE); its greatest ruler was Gautamiputra Satakarni; king Hala compiled the *Gathasaptasati* in Prakrit.",
        "Simuka starts the line.", 20)
    S.q("ga-post-p3", "medium", "Which dynasty was the **first to grant tax-free land to Brahmanas**, a practice that grew in later centuries?",
        ["Mauryas", "Satavahanas", "Kushanas", "Indo-Greeks"], "Satavahanas",
        "The **Satavahanas** made the first recorded **land grants to Brahmanas** — an early step towards the feudal pattern. Their inscriptions are in Prakrit; their coins were of lead and potin.",
        "Land-grant firsts = Satavahanas.", 25)
    S.q("ga-post-p4", "easy", "Which was the major **east-coast** port of the post-Mauryan trade?",
        ["Bharuch", "Sopara", "Tamralipti", "Muziris"], "Tamralipti",
        "**Tamralipti** (in the Ganga delta, Bengal) was the great eastern port; Bharuch and Sopara faced the west coast, Muziris lay in Kerala.",
        "Tamralipti = the eastern gate.", 20)
    S.q("ga-post-p4", "medium", "The *Periplus of the Erythraean Sea*, a guide to India's trade, was written by —",
        ["Megasthenes", "An anonymous Greek sailor", "Ptolemy", "Pliny"], "An anonymous Greek sailor",
        "The *Periplus* (1st century CE) was composed by an **anonymous Greek-speaking sailor** of the Roman trade world; it lists Indian ports from Bharuch to Arikamedu.",
        "Periplus = no known author — a sailor's handbook.", 25)
    S.q("ga-post-p4", "hard", "Large hoards of **Roman gold coins** found in south India indicate that —",
        ["India paid tribute to Rome", "India had an unfavourable trade balance", "India exported more than it imported", "Rome minted coins in India"], "India exported more than it imported",
        "Roman gold flowing into India (and Pliny's complaints about it) shows Rome **paid gold for Indian exports** — pepper, pearls, textiles — i.e. India ran a trade **surplus**.",
        "Follow the gold: gold comes to the exporter.", 30)
    return S


def build_gupta():
    S = Sub("gupta-harsha")
    S.notes = """### The Gupta line (c. 320–550 CE)
**Chandragupta I** (c. 320 CE) started the **Gupta era** and took the title **Maharajadhiraja**. His son **Samudragupta** is described on the **Allahabad (Prayag) pillar prashasti composed by Harishena**: he uprooted nine kings of Aryavarta in the north, defeated but reinstated twelve rulers of Dakshinapatha, and received tribute from frontier states and Sri Lanka; a veena-player on his coins earned him the title **Kaviraja** — V.A. Smith called him the **'Napoleon of India'**. **Chandragupta II 'Vikramaditya'** destroyed the Western Shaka (Kshatrapa) power, ruled via Pataliputra and Ujjain, and kept the **Navaratna** circle of scholars including **Kalidasa**; the Chinese pilgrim **Fa-Hien** (399–414 CE) travelled in his reign. **Kumaragupta I** founded **Nalanda**. **Skandagupta** repelled the **Huna** invasion and repaired **Sudarshana lake** (Junagadh inscription). After the Huns ground on, the empire faded by c. 550.

### Why it is called the golden age
- **Science:** **Aryabhata's Aryabhatiya** — place value and zero in use, the earth rotates, eclipses explained, an accurate value of pi; **Varahamihira's Brihatsamhita**; Sushruta's surgery and Charaka's medicine were the classics in use.
- **Literature:** **Kalidasa** — *Abhijnanashakuntalam*, *Meghaduta*, *Raghuvamsha*, *Malavikagnimitram* (his play on the Sunga king Agnimitra); **Vishnu Sharma's Panchatantra** fables; Amarasimha's *Amarakosha*; Dandin's *Dashakumaracharita*; Bharavi's *Kiratarjuniya*.
- **Art:** Ajanta murals peak (Bodhisattva Padmapani); Dashavatara temple at Deogarh; the **Nagara temple style** takes shape; Mathura school's standing Buddhas.
- **Coins:** the finest **gold dinaras** of ancient India.
- **The shadow side (asked as often):** women's status fell — the **first epigraphic proof of sati (Eran inscription, 510 CE)**, early devadasi references, no property rights; caste hardened; **untouchability** is noticed by Fa-Hien (chandalas living outside town).

### Harsha (606–647 CE)
A ruler of the Pushyabhuti (Vardhana) house of **Thanesar**, Harsha shifted his seat to **Kannauj** and bore the titles **Siladitya** and 'lord of the whole north'. **Banabhatta** wrote his biography, the *Harshacharita* (and the novel *Kadambari*); Harsha himself wrote three plays — *Nagananda*, *Ratnavali*, *Priyadarshika*. He was **checked by Pulakesin II on the Narmada** (recorded in the Aihole inscription). Two grand assemblies: at **Kannauj** (where **Hiuen Tsang** was honoured) and the quinquennial **Prayag (Moksha parishad)** gift-giving. **Hiuen Tsang** stayed 630–645, studied at Nalanda and recorded India in the **Si-yu-ki**; **I-tsing** followed (671–695). After Harsha, Kannauj went to **Yashovarman**, and the tripartite struggle of the early-medieval age began.

### Quick revision
- Chain: Chandragupta I (Gupta era 320) → Samudragupta (Prashasti-Harishena; Napoleon) → Chandragupta II Vikramaditya (Shakas; Navaratna; Fa-Hien) → Kumaragupta I (Nalanda) → Skandagupta (Huns; Sudarshana lake).
- Science: Aryabhatiya (Aryabhata); Brihatsamhita (Varahamihira).
- Kalidasa's four: Shakuntalam, Meghaduta, Raghuvamsha, Malavikagnimitram.
- Golden-age dark spots: Eran sati (510 CE), untouchability noted by Fa-Hien.
- Harsha: Thanesar → Kannauj; Banabhatta biographer; 3 plays; assemblies at Kannauj & Prayag; stopped by Pulakesin II."""
    S.pattern("ga-gup-p1", "Gupta rulers ↔ achievements and titles", "very common",
        "'Napoleon of India', who defeated the Shakas/Huns, Prashasti facts, Nalanda's founder.",
        None,
        "1. Samudragupta = Allahabad Prashasti (Harishena), Kaviraja, 'Napoleon of India' (V.A. Smith).\n2. Chandragupta II = 'Vikramaditya', ended Western Shakas, Navaratna with Kalidasa, Fa-Hien's host.\n3. Kumaragupta I founded Nalanda; Skandagupta beat the Huns and repaired Sudarshana lake.",
        "Which Gupta ruler took the title **'Vikramaditya'** after destroying the Western Shakas?",
        "**Chandragupta II** — his court hosted the Navaratna, including Kalidasa.")
    S.pattern("ga-gup-p2", "Gupta golden age: science and literature", "very common",
        "'Aryabhatiya was written by', 'which work is by Kalidasa', Panchatantra-Amarakosha author pairs.",
        None,
        "1. Science: **Aryabhata (Aryabhatiya)** — zero/place value, earth's rotation, eclipses, pi; **Varahamihira (Brihatsamhita)**.\n2. Kalidasa's set: Shakuntalam, Meghaduta, Raghuvamsha, Kumarasambhava, Malavikagnimitram.\n3. Other pairs: Panchatantra-Vishnu Sharma, Amarakosha-Amarasimha, Dashakumaracharita-Dandin, Kiratarjuniya-Bharavi.",
        "The *Panchatantra*, the famous collection of animal fables, is attributed to —",
        "**Vishnu Sharma**, who is said to have composed it to teach statecraft to princes.")
    S.pattern("ga-gup-p3", "Harsha: capital, assemblies and visitors", "common",
        "Kannauj capital, Banabhatta, Harsha's plays, Kannauj-Prayag assemblies, defeat on the Narmada.",
        None,
        "1. Harsha of Thanesar ruled from **Kannauj** (titles Siladitya, Shakalottara).\n2. Biographer **Banabhatta** (*Harshacharita*, *Kadambari*); plays *Nagananda*, *Ratnavali*, *Priyadarshika*.\n3. Assemblies at **Kannauj** (Hiuen Tsang honoured) and **Prayag** (Moksha parishad, every 5 years); checked by **Pulakesin II** on the Narmada.",
        "Harshavardhana shifted his capital from Thanesar to —",
        "**Kannauj** (Kanyakubja), which then became the prize of the later tripartite struggle.")
    S.pattern("ga-gup-p4", "Chinese travellers and Greek envoys ↔ the reigns they visited", "common",
        "Matching Megasthenes, Fa-Hien, Hiuen Tsang, I-tsing (and Deimachus, Dionysius) to the courts they saw.",
        None,
        "1. The chain: **Megasthenes–Chandragupta Maurya**, Deimachus–Bindusara, Dionysius–Ashoka, **Fa-Hien–Chandragupta II**, **Hiuen Tsang–Harsha**, **I-tsing–post-Harsha**.\n2. Books: *Indica* (Megasthenes), *Si-yu-ki* (Hiuen Tsang).\n3. Fa-Hien stayed 399–414 and noted untouchability; Hiuen Tsang studied at Nalanda (630–645).",
        "Which Chinese pilgrim visited India **after** Harsha's death and studied its monasteries (671–695)?",
        "**I-tsing** — after Fa-Hien (Gupta age) and Hiuen Tsang (Harsha's reign).")

    S.q("ga-gup-p1", "easy", "Which Gupta ruler is called the **'Napoleon of India'** by historians?",
        ["Chandragupta I", "Samudragupta", "Chandragupta II", "Skandagupta"], "Samudragupta",
        "**Samudragupta** — for his vast digvijaya described in the Allahabad Prashasti (by Harishena); the label was given by V.A. Smith. His veena-type coins earned him 'Kaviraja'.",
        "Napoleon = Samudragupta (Smith's phrase).", 20)
    S.q("ga-gup-p1", "medium", "**Nalanda** university was founded during the reign of —",
        ["Chandragupta II", "Kumaragupta I", "Skandagupta", "Harshavardhana"], "Kumaragupta I",
        "**Kumaragupta I** founded Nalanda (later expanded by Harsha and the Palas). Harsha patronised it but did not found it.",
        "Nalanda = Kumaragupta I (Gupta).", 25)
    S.q("ga-gup-p1", "hard", "Consider the statements:\n1. Samudragupta reinstated the defeated Dakshinapatha rulers after defeating them.\n2. The Allahabad Prashasti was composed by Vasubandhu.\n3. Skandagupta's Junagadh inscription records the repair of Sudarshana lake.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 3 only",
        "Statements 1 and 3 are correct. Statement 2 is wrong — the Prashasti was composed by **Harishena** (Vasubandhu was a Buddhist scholar, not its author).",
        "Prashasti composer = Harishena; southern kings were left on their thrones as tribute-paying allies.", 30)
    S.q("ga-gup-p2", "easy", "The **Aryabhatiya**, a landmark of ancient Indian mathematics and astronomy, was written by —",
        ["Brahmagupta", "Varahamihira", "Aryabhata", "Bhaskara"], "Aryabhata",
        "**Aryabhata** wrote the *Aryabhatiya* (c. 499 CE): place value with zero, the earth's rotation, eclipse explanations and a close value of pi.",
        "Book title carries the author's name here.", 20)
    S.q("ga-gup-p2", "medium", "Which of the following works was **NOT** written by Kalidasa?",
        ["Abhijnanashakuntalam", "Meghaduta", "Kiratarjuniya", "Raghuvamsha"], "Kiratarjuniya",
        "*Kiratarjuniya* is a court epic by **Bharavi**. Kalidasa wrote Shakuntalam, Meghaduta, Raghuvamsha, Kumarasambhava and Malavikagnimitram.",
        "Kalidasa's set vs Bharavi's Kiratarjuniya — keep them apart.", 25)
    S.q("ga-gup-p2", "easy", "The fable collection **Panchatantra** is attributed to —",
        ["Vishnu Sharma", "Narayana Pandit", "Somadeva", "Gunadhya"], "Vishnu Sharma",
        "**Vishnu Sharma** composed the *Panchatantra*, said to be for teaching prudence to princes; its stories travelled the world as Aesop-like fables.",
        "Panchatantra = Vishnu Sharma.", 20)
    S.q("ga-gup-p3", "easy", "Harsha's court poet and biographer, author of the **Harshacharita**, was —",
        ["Harishena", "Banabhatta", "Ravikirti", "Vasubandhu"], "Banabhatta",
        "**Banabhatta (Bana)** wrote the *Harshacharita* and the prose romance *Kadambari*. Harishena composed Samudragupta's Prashasti; Ravikirti wrote the Aihole inscription.",
        "Harsha-Bana; Samudragupta-Harishena; Pulakesin-Ravikirti.", 20)
    S.q("ga-gup-p3", "medium", "Harsha held two great assemblies described by Hiuen Tsang — at Kannauj and at —",
        ["Thanesar", "Prayag", "Varanasi", "Nalanda"], "Prayag",
        "Besides the **Kannauj** assembly (where Hiuen Tsang's scholarship was honoured), Harsha held the quinquennial **Prayag (Moksha parishad)**, where he gave away his accumulated treasure.",
        "Kannauj = debate; Prayag = charity fair.", 25)
    S.q("ga-gup-p4", "medium", "**Fa-Hien's** travel account is important because it —",
        ["Describes Harsha's assemblies", "Records society and Buddhism under Chandragupta II but skips the king's name", "Describes the Kalinga war", "Lists Ashoka's edicts"], "Records society and Buddhism under Chandragupta II but skips the king's name",
        "Fa-Hien (399–414) hardly mentions Chandragupta II by name; his value is the **social record** — mild administration, prosperity, and the treatment of **chandalas (untouchability)**.",
        "Fa-Hien = society-first, king-unnamed.", 25)
    S.q("ga-gup-p4", "hard", "Which pair of visitor and ruler is **correctly matched**?",
        ["Megasthenes — Bindusara", "Deimachus — Chandragupta Maurya", "Hiuen Tsang — Chandragupta II", "I-tsing — Harsha"], "Megasthenes — Bindusara",
        "None of those: the correct chain is **Megasthenes–Chandragupta Maurya**, **Deimachus–Bindusara**, **Fa-Hien–Chandragupta II**, **Hiuen Tsang–Harsha**, and I-tsing visited **after** Harsha. (If an option pairs a visitor wrongly on purpose, check against this chain.)",
        "One ladder, five rungs: M-CM, D-B, D-A, F-CGII, H-H, I-tsing later.", 30)
    S.q("ga-gup-p4", "easy", "Hiuen Tsang's travel record of India is titled —",
        ["Indica", "Si-yu-ki", "Rajatarangini", "Periplus"], "Si-yu-ki",
        "**Si-yu-ki** ('Records of the Western World') is Hiuen Tsang's account; *Indica* was Megasthenes' book and the *Periplus* a Greek trade guide.",
        "Hiuen Tsang = Si-yu-ki; Megasthenes = Indica.", 20)
    return S


def build_south():
    S = Sub("south-dynasties")
    S.notes = """### The Sangam age (c. 300 BCE – 300 CE)
The far south was divided among three 'crowned kings' (muvendar), each with a fixed emblem, capital and port:

| Kingdom | Capital | Port | Emblem | Greatest king |
|---|---|---|---|---|
| **Chera** (Keralaputras) | Vanji (Karur) | Muziris, Tondi | **Bow** | Senguttuvan |
| **Chola** | Uraiyur | Puhar (Kaveripoompattinam) | **Tiger** | Karikala |
| **Pandya** | Madurai | Korkai (pearls) | **Fish** | Nedunjeliyan |

**Karikala Chola** won the **Battle of Venni** against Chera-Pandya powers and built the **Kallanai (Grand Anicut)** across the Kaveri — among the world's oldest water-regulators still in use. **Senguttuvan** (Chera) is credited with starting the **Pattini (Kannagi) cult**. Roman traders ('Yavanas') appear throughout the Sangam poems; wine, gold and lamps came in, pepper and pearls went out.

### Sangam literature
The corpus was compiled by three **Sangams** (poets' academies) held at **Madurai under Pandya patronage**. Main collections: **Ettutogai** (Eight Anthologies) and **Pattuppattu** (Ten Idylls); grammar codified in the **Tolkappiyam by Tolkappiyar**. Poems divide into **akam** (love, interior life) and **puram** (war, public life). *Purananuru* is a puram anthology; *Maduraikkanchi* describes Pandya Madurai. After this age came the **Kalabhra interregnum**, when Buddhist- and Jain-leaning Kalabhras displaced the old kings.

### Pallavas of Kanchi vs Chalukyas of Badami
- **Pallavas** (c. 600–750): **Mahendravarman I** — pioneer of **rock-cut temples**, author of the farce *Mattavilasa Prahasana*; **Narasimhavarman I Mamalla** — defeated and killed **Pulakesin II**, occupied **Vatapi** (title **Vatapikonda**); Hiuen Tsang visited **Kanchi**; **Narasimhavarman II Rajasimha** — built the **Shore Temple at Mamallapuram** and the **Kailasanatha temple at Kanchi**; the rathas of Mamallapuram (Draupadi to Arjuna ratha) belong to this age.
- **Chalukyas of Badami** (6th–8th century): **Pulakesin II** — **Aihole inscription in Sanskrit by the poet Ravikirti** (a Jain); defeated Harsha on the **Narmada**. Their temples — the **Durga temple, Aihole** (apsidal), Badami cave shrines and the group at **Pattadakal** — show the **Vesara** blend of north and south styles.
- **Rashtrakutas of Manyakheta:** **Krishna I** excavated the monolithic **Kailasa temple at Ellora**; Amoghavarsha wrote (or inspired) the *Kavirajamarga*, the earliest Kannada poetics.

### Temple styles at a glance
**Dravida** (south: pyramidal vimana, gopuram gateway — Pallavas onward), **Nagara** (north: curvilinear shikhara), **Vesara** (Deccan blend — Chalukyas, later Hoysalas).

### Quick revision
- Chera-bow, Chola-tiger, Pandya-fish; capitals Vanji, Uraiyur, Madurai; ports Muziris, Puhar, Korkai.
- Karikala = Venni + Kallanai; Senguttuvan = Kannagi cult.
- Sangam = 3 academies at Madurai (Pandya); Tolkappiyam = grammar; akam vs puram.
- Pallavas: Mahendra (rock-cut) → Mamalla (Vatapikonda) → Rajasimha (Shore Temple).
- Chalukyas: Pulakesin II (Aihole inscription, stopped Harsha); Durga temple Aihole; Vesara style.
- Rashtrakuta Krishna I = Kailasa temple, Ellora."""
    S.pattern("ga-sou-p1", "Chera ↔ Chola ↔ Pandya: emblems, capitals, ports, kings", "very common",
        "'The emblem of the Cholas was', 'the Pandya port famous for pearls', 'who built the Kallanai', match-the-column across the three kingdoms.",
        None,
        "1. Emblems: **Chera = bow, Chola = tiger, Pandya = fish**.\n2. Capital-port pairs: Chera Vanji–Muziris; Chola Uraiyur–Puhar; Pandya Madurai–Korkai (pearls).\n3. Kings: Karikala (Chola) = Venni + Kallanai; Senguttuvan (Chera) = Kannagi cult; Nedunjeliyan (Pandya) of Maduraikkanchi.",
        "Which Sangam-age king built the **Kallanai (Grand Anicut)** across the Kaveri?",
        "**Karikala Chola** — also the victor of the Battle of Venni.")
    S.pattern("ga-sou-p2", "Sangam literature: assemblies, texts, grammar", "common",
        "'Sangam literature was compiled under which patronage', Tolkappiyam as grammar, akam vs puram, Ettutogai-Pattuppattu.",
        None,
        "1. Three Sangams at **Madurai under the Pandyas**.\n2. Grammar: **Tolkappiyam** (Tolkappiyar); collections **Ettutogai** (8 anthologies) + **Pattuppattu** (10 idylls).\n3. Theme split: **akam = love**, **puram = war/public life** (Purananuru is puram).",
        "The Sangam poets' academies were held under the patronage of which kingdom?",
        "The **Pandyas**, at **Madurai** — three Sangams compiled the corpus.")
    S.pattern("ga-sou-p3", "Pallava ↔ Chalukya ↔ Rashtrakuta rulers and temples", "very common",
        "'Vatapikonda was the title of', 'the Aihole inscription was composed by', 'Shore Temple built by', 'Kailasa temple at Ellora'.",
        None,
        "1. Pallava chain: **Mahendravarman I** (rock-cut, Mattavilasa) → **Narasimhavarman I Mamalla** (Vatapikonda) → **Narasimhavarman II Rajasimha** (Shore Temple, Kailasanatha Kanchi).\n2. Chalukya: **Pulakesin II** — Aihole inscription by **Ravikirti**, stopped Harsha on the Narmada; Durga temple Aihole; Pattadakal group.\n3. Rashtrakuta: **Krishna I** — Kailasa temple Ellora; Amoghavarsha — Kavirajamarga.",
        "Which Pallava king took the title **'Vatapikonda'**?",
        "**Narasimhavarman I (Mamalla)** — after capturing the Chalukya capital Vatapi and killing Pulakesin II.")
    S.pattern("ga-sou-p4", "Temple styles (Dravida-Nagara-Vesara) and the tripartite struggle", "common",
        "Matching style to dynasty and site; statements on who fought whom for Kannauj; Pattadakal-Aihole-Mamallapuram site pairs.",
        None,
        "1. Styles: **Dravida = Pallavas onward (south)**; **Nagara = north**; **Vesara = Deccan blend (Chalukyas, later Hoysalas)**.\n2. Site-style pairs: Mamallapuram rathas + Shore Temple (Dravida); Durga temple Aihole & Pattadakal (Vesara).\n3. Tripartite struggle: **Palas (Bengal) vs Gurjara-Pratiharas (Malwa-Rajasthan) vs Rashtrakutas (Deccan)**, prize = Kannauj.",
        "The **Vesara** temple style, blending Nagara and Dravida elements, is associated with —",
        "The **Chalukyas of Badami** — Durga temple (Aihole), Badami caves and the Pattadakal group.")

    S.q("ga-sou-p1", "easy", "The royal **emblem of the Cholas** was the —",
        ["Bow", "Fish", "Tiger", "Elephant"], "Tiger",
        "Chola = **tiger**; Pandya = **fish (carp)**; Chera = **bow and arrow**.",
        "Tiger-Chola, fish-Pandya, bow-Chera.", 20)
    S.q("ga-sou-p1", "medium", "Which Pandya port was famous for its **pearls**?",
        ["Puhar", "Muziris", "Korkai", "Tondi"], "Korkai",
        "**Korkai** (at the Tamraparni mouth) was the Pandya pearl port. Puhar = Chola; Muziris and Tondi = Chera ports.",
        "Korkai = pearls (Pandya).", 25)
    S.q("ga-sou-p1", "medium", "The Sangam-age Chera king associated with the **Kannagi (Pattini) cult** is —",
        ["Karikala", "Senguttuvan", "Nedunjeliyan", "Ariyappadaikadanda"], "Senguttuvan",
        "**Senguttuvan** (the 'red Chera') is credited with instituting the **Pattini cult** of the chaste heroine Kannagi, as described in the *Silappadikaram*'s later tradition.",
        "Senguttuvan = Kannagi temple starter.", 25)
    S.q("ga-sou-p2", "easy", "The **Tolkappiyam** is a work on —",
        ["Tamil grammar and poetics", "Medicine", "War ethics", "Agriculture"], "Tamil grammar and poetics",
        "The **Tolkappiyam by Tolkappiyar** is the oldest surviving Tamil **grammar**, and it codifies the akam-puram division of poetry.",
        "Tolkappiyam = grammar.", 20)
    S.q("ga-sou-p2", "medium", "Sangam poems are grouped into **akam** and **puram**. *Purananuru* belongs to —",
        ["akam — love poetry", "puram — war and public life", "grammar", "hymns to Vishnu"], "puram — war and public life",
        "*Purananuru* is a **puram** anthology — heroic deeds, generosity and public life; akam deals with love.",
        "Purananuru = puram (the names rhyme).", 25)
    S.q("ga-sou-p3", "easy", "The capital of the **Pallava** kingdom was —",
        ["Vatapi", "Kanchipuram", "Madurai", "Manyakheta"], "Kanchipuram",
        "The Pallavas ruled from **Kanchipuram** (Hiuen Tsang visited it); Vatapi (Badami) was the Chalukya capital, Manyakheta the Rashtrakuta seat.",
        "Pallava = Kanchi.", 20)
    S.q("ga-sou-p3", "medium", "The **Aihole inscription**, a eulogy of Pulakesin II, was composed by —",
        ["Harishena", "Ravikirti", "Banabhatta", "Vasubandhu"], "Ravikirti",
        "**Ravikirti**, a Jain poet in Pulakesin II's court, wrote the Aihole inscription (Sanskrit). It also records Pulakesin II's victory over **Harsha** on the Narmada.",
        "Ravikirti-Aihole; Harishena-Allahabad.", 25)
    S.q("ga-sou-p3", "medium", "Which Pallava ruler built the **Shore Temple** at Mamallapuram?",
        ["Mahendravarman I", "Narasimhavarman I", "Narasimhavarman II Rajasimha", "Simhavishnu"], "Narasimhavarman II Rajasimha",
        "**Narasimhavarman II Rajasimha** built the Shore Temple at Mamallapuram and the Kailasanatha temple at Kanchi. Mahendravarman I began rock-cut temples; Mamalla added the rathas.",
        "Shore temple = Rajasimha (temple-builder name).", 25)
    S.q("ga-sou-p4", "medium", "Which temple group is the classic example of the **Vesara** style?",
        ["Mamallapuram rathas", "Durga temple, Aihole and Pattadakal group", "Konark Sun Temple", "Khajuraho temples"], "Durga temple, Aihole and Pattadakal group",
        "The **Chalukya** monuments at Aihole, Badami and **Pattadakal** blend north (Nagara) and south (Dravida) forms — the **Vesara** style. Konark and Khajuraho are Nagara; the rathas are early Dravida.",
        "Vesara = Deccan = Chalukya country.", 25)
    S.q("ga-sou-p4", "hard", "The **tripartite struggle** of the early medieval period was fought for control of —",
        ["Kanchipuram, among Pallavas, Cholas and Pandyas", "Kannauj, among Palas, Gurjara-Pratihara and Rashtrakuta", "Vatapi, among Chalukyas, Pallavas and Rashtrakutas", "Madurai, among Pandyas, Cholas and Cheras"], "Kannauj, among Palas, Gurjara-Pratihara and Rashtrakuta",
        "The tripartite struggle was for **Kannauj** — **Palas** (Bengal), **Gurjara-Pratiharas** (Malwa-Rajasthan) and **Rashtrakutas** (Deccan) fought for nearly two centuries.",
        "Kannauj triangle: Pala-Pratihara-Rashtrakuta.", 30)
    S.q("ga-sou-p4", "hard", "Consider the statements:\n1. Hiuen Tsang visited Kanchipuram during Narasimhavarman I's reign.\n2. The Kailasa temple at Ellora was excavated under the Rashtrakuta Krishna I.\n3. Amoghavarsha is associated with the Kavirajamarga.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three are standard: Hiuen Tsang reached **Kanchi** under the Pallavas (Narasimhavarman I's reign), **Krishna I** excavated the Ellora Kailasa temple, and **Amoghavarsha** is linked to the *Kavirajamarga* (earliest Kannada poetics).",
        "One south-India sweep: Pallava, Rashtrakuta, Kannada.", 30)
    return S


def build_lit():
    S = Sub("ancient-literature")
    S.notes = """### Four language streams, one story
Ancient Indian writing survives in four main streams: **Sanskrit** (Brahmanical texts and court poetry), **Pali** (the Buddhist canon), **Prakrit/Ardhamagadhi** (Jain canon, Satavahana records) and **Tamil** (Sangam corpus). Inscriptions and coins complete the picture — they are history's own documents, and travellers' accounts supply the outside view.

### Sanskrit anchors — text ↔ author
| Text | Author | Remember for |
|---|---|---|
| Arthashastra | Kautilya | Statecraft, revenue, spies |
| Mudrarakshasa | Vishakhadatta | Drama on Chandragupta Maurya's rise |
| Mrichchhakatika | Shudraka | 'The Little Clay Cart' |
| Malavikagnimitram | Kalidasa | Play on Sunga king Agnimitra |
| Panchatantra | Vishnu Sharma | Animal fables |
| Amarakosha | Amarasimha | Sanskrit lexicon |
| Kiratarjuniya | Bharavi | Court epic (Arjuna-Shiva) |
| Dashakumaracharita | Dandin | Ten princes |
| Rajatarangini | Kalhana | 'River of kings' — chronicle of Kashmir |
| Harshacharita, Kadambari | Banabhatta | Harsha's biography; prose romance |
| Gathasaptasati | Hala (Satavahana king) | Prakrit love verses |

### Buddhist and Jain texts
The Buddhist canon, the **Tripitaka**, is in **Pali**: *Vinaya Pitaka* (rules), *Sutta Pitaka* (dialogues), *Abhidhamma Pitaka* (philosophy). Around them: the **Jatakas** (stories of the Buddha's former births — a mine of social history), the **Milindapanha** (Menander–Nagasena dialogue), **Ashvaghosha's Buddhacharita** (life of the Buddha, in Sanskrit), and Sri Lanka's **Deepavamsha–Mahavamsha** chronicles. The Jain canon is in **Ardhamagadhi Prakrit**: 12 **Angas**, compiled at the Pataliputra council (Sthulabhadra) and written down at **Vallabhi (Devarddhi)**; the **Kalpasutra** is credited to **Bhadrabahu**. Both faiths chose the **people's language** on purpose — which is why their texts are also social documents.

### Tamil classics
The twin epics: **Silappadikaram** ('the lay of the anklet') by **Ilango Adigal** — Kovalan and Kannagi's tragedy — and the Buddhist **Manimekalai** by Sittalai Sattanar as its sequel. Grammar stands in the **Tolkappiyam**; *Purananuru* (puram — war and public life) and *Ahananuru* (akam — love) are the classic anthologies; *Maduraikkanchi* paints Pandya Madurai; the *Gathasaptasati* of the Satavahana king **Hala** shows Prakrit's southern reach.

### Inscriptions and coins as history
**James Prinsep deciphered Brahmi (1837)**, unlocking Ashoka. Flagship records: Ashoka's edicts (Prakrit-Brahmi); the **Hathigumpha inscription of Kharavela** (Chedi king of Kalinga); Rudradaman's Junagadh (first long chaste Sanskrit); the Allahabad Prashasti (Harishena on Samudragupta); the Aihole inscription (Ravikirti on Pulakesin II). Coins: earliest **punch-marked silver** pieces; Indo-Greeks first put **royal portraits**; **Kushanas first issued gold**; Satavahanas used **lead and potin**; Guptas struck the finest gold dinaras. Travellers: Megasthenes (*Indica*), Fa-Hien, Hiuen Tsang (*Si-yu-ki*), I-tsing.

### Quick revision
- Statecraft = Arthashastra (Kautilya); Chandragupta's story = Mudrarakshasa (Vishakhadatta).
- Buddhist canon = Tripitaka in **Pali**; Jain canon in **Ardhamagadhi**; Buddhacharita = Ashvaghosha.
- Tamil twin epics: Silappadikaram (Ilango Adigal) + Manimekalai.
- Prinsep deciphered Brahmi in 1837; Hathigumpha = Kharavela.
- Coin ladder: punch-marked silver → portrait (Indo-Greek) → gold (Kushana) → lead-potin (Satavahana) → dinaras (Gupta)."""
    S.pattern("ga-lit-p1", "Sanskrit text ↔ author pairing", "very common",
        "'Who wrote X' or match-the-column across kavyas, dramas and smritis.",
        None,
        "1. Court-and-state set: Arthashastra-Kautilya, Mudrarakshasa-Vishakhadatta, Rajatarangini-Kalhana.\n2. Drama set: Mrichchhakatika-Shudraka, Malavikagnimitram-Kalidasa, Harshacharita-Banabhatta (prose).\n3. Distractors are always other authors' books — eliminate by pair memory, not guesswork.",
        "The drama **Mudrarakshasa**, on the rise of Chandragupta Maurya, was written by —",
        "**Vishakhadatta** — it shows Chanakya outwitting the Nandas and installing Chandragupta.")
    S.pattern("ga-lit-p2", "Buddhist and Jain literature and languages", "common",
        "'The Tripitaka is in which language', 'Buddhacharita was written by', Jain canon language, Kalpasutra attribution.",
        None,
        "1. Buddhist: Tripitaka in **Pali**; Jatakas (birth stories); Milindapanha (Menander-Nagasena); Buddhacharita-Ashvaghosha (Sanskrit).\n2. Jain: canon in **Ardhamagadhi**; 12 Angas; Kalpasutra-Bhadrabahu; written down at Vallabhi (Devarddhi).\n3. Sri Lankan Pali chronicles: Deepavamsha, Mahavamsha.",
        "In which language is the Buddhist canonical collection **Tripitaka** written?",
        "**Pali** — the language of the people of the middle Ganga plain in the Buddha's time.")
    S.pattern("ga-lit-p3", "Tamil/Sangam works ↔ author and type", "common",
        "'Silappadikaram was written by', twin epics, Tolkappiyam as grammar, akam-puram classification of anthologies.",
        None,
        "1. Twin epics: **Silappadikaram-Ilango Adigal**, **Manimekalai-Sittalai Sattanar** (Buddhist).\n2. Grammar: **Tolkappiyam**; anthologies: Purananuru (puram), Ahananuru (akam).\n3. The two epics are 'kavya' epics — separate them from the grammar and the anthologies.",
        "The Tamil epic **Silappadikaram** ('the lay of the anklet') was composed by —",
        "**Ilango Adigal**; its Buddhist sequel, the *Manimekalai*, was written by Sittalai Sattanar.")
    S.pattern("ga-lit-p4", "Inscriptions and coins ↔ rulers and scripts", "common",
        "'Hathigumpha inscription belongs to', 'who deciphered Brahmi', earliest coins, first gold coins, first Sanskrit inscription.",
        None,
        "1. Records: Hathigumpha-**Kharavela**; Junagadh-Rudradaman (first chaste Sanskrit); Allahabad-Harishena/Samudragupta; Aihole-Ravikirti/Pulakesin II.\n2. **James Prinsep deciphered Brahmi (1837)**.\n3. Coin ladder: **punch-marked silver** earliest → Indo-Greek portraits → **Kushana gold** → Satavahana lead-potin → Gupta dinaras.",
        "The **Hathigumpha inscription** belongs to which king?",
        "**Kharavela**, the Chedi (Mahameghavahana) king of Kalinga — recorded in a Jain cave at Udayagiri, Odisha.")

    S.q("ga-lit-p1", "medium", "Kalidasa's play based on the life of the **Sunga king Agnimitra** is —",
        ["Vikramorvashiyam", "Malavikagnimitram", "Raghuvamsha", "Kumarasambhava"], "Malavikagnimitram",
        "**Malavikagnimitram** is Kalidasa's first play, set at the court of **Agnimitra**, the second Sunga king. Raghuvamsha and Kumarasambhava are his epics; Vikramorvashiyam is another of his plays.",
        "Agni-mitra inside the title: Malavika + Agnimitra.", 25)
    S.q("ga-lit-p1", "easy", "The **Arthashastra**, a treatise on statecraft and economy, is attributed to —",
        ["Banabhatta", "Kautilya", "Vishakhadatta", "Nagarjuna"], "Kautilya",
        "The *Arthashastra* is attributed to **Kautilya (Chanakya)**, Chandragupta Maurya's minister; it covers taxation, espionage, diplomacy and administration.",
        "Artha-economy-Kautilya.", 20)
    S.q("ga-lit-p1", "hard", "Match:\n1. Rajatarangini — Kalhana\n2. Dashakumaracharita — Dandin\n3. Kiratarjuniya — Bharavi\nWhich pairs are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All correct: **Rajatarangini** (Kalhana) is the chronicle of Kashmir, **Dashakumaracharita** (Dandin) tells of ten princes, **Kiratarjuniya** (Bharavi) sings of Arjuna's combat with Shiva.",
        "Three classic pairs — all true; read carefully before doubting.", 30)
    S.q("ga-lit-p2", "easy", "The **Buddhacharita**, a Sanskrit epic on the Buddha's life, was composed by —",
        ["Nagasena", "Ashvaghosha", "Nagarjuna", "Vasumitra"], "Ashvaghosha",
        "**Ashvaghosha**, the scholar-poet at Kanishka's court, wrote the *Buddhacharita*. Nagasena is the Milindapanha monk; Vasumitra presided at the 4th Council.",
        "Buddha's biography = Ashvaghosha (Kanishka's court).", 20)
    S.q("ga-lit-p2", "easy", "The Jain canonical texts (the 12 **Angas**) are written in —",
        ["Sanskrit", "Pali", "Ardhamagadhi Prakrit", "Tamil"], "Ardhamagadhi Prakrit",
        "The Jain canon is in **Ardhamagadhi Prakrit**; the Buddhist canon is in Pali; the earliest Jain council compiled them at Pataliputra and the canon was written down at Vallabhi.",
        "Jain = Ardhamagadhi; Buddhist = Pali.", 20)
    S.q("ga-lit-p2", "hard", "Which pair is correctly matched?",
        ["Milindapanha — dialogue of Ashoka with Upagupta", "Kalpasutra — credited to Bhadrabahu", "Mahavamsha — a Jain canonical text", "Jatakas — sermons of Mahavira"], "Kalpasutra — credited to Bhadrabahu",
        "The **Kalpasutra** is credited to **Bhadrabahu**. The Milindapanha is Menander's dialogue with **Nagasena**; the Mahavamsha is a **Buddhist** chronicle of Sri Lanka; the Jatakas are the **Buddha's** birth stories.",
        "Check the religion of each text before matching.", 30)
    S.q("ga-lit-p3", "medium", "The Tamil epic **Silappadikaram** tells the tragic story of —",
        ["Manimekala and Udayakumara", "Kovalan and Kannagi", "Senguttuvan and the Cheras", "Karikala at Venni"], "Kovalan and Kannagi",
        "**Silappadikaram** ('the lay of the anklet') by **Ilango Adigal** follows merchant **Kovalan** and his chaste wife **Kannagi** in Madurai; its sequel is the Buddhist *Manimekalai*.",
        "Kannagi's anklet = Silappadikaram.", 25)
    S.q("ga-lit-p3", "easy", "The twin epics of Tamil literature are **Silappadikaram** and —",
        ["Tolkappiyam", "Manimekalai", "Purananuru", "Maduraikkanchi"], "Manimekalai",
        "The twin epics are **Silappadikaram** (Jain-leaning, by Ilango Adigal) and **Manimekalai** (Buddhist, by Sittalai Sattanar). Tolkappiyam is grammar; Purananuru an anthology.",
        "Twins: anklet + Manimekalai.", 20)
    S.q("ga-lit-p4", "easy", "Who deciphered the **Brahmi script** in 1837, opening up Ashoka's inscriptions?",
        ["William Jones", "James Prinsep", "John Marshall", "Alexander Cunningham"], "James Prinsep",
        "**James Prinsep**, an officer of the East India Company, deciphered Brahmi in **1837**, allowing Ashoka's edicts to be read for the first time in centuries.",
        "Prinsep = the key to Brahmi.", 20)
    S.q("ga-lit-p4", "medium", "The **Hathigumpha inscription** of Kharavela is carved at —",
        ["Girnar", "Udayagiri (Odisha)", "Junagadh fort", "Dhauli"], "Udayagiri (Odisha)",
        "Kharavela's **Hathigumpha inscription** sits in the Jain caves at **Udayagiri, Odisha**. Girnar and Junagadh carry Rudradaman-Ashoka records; Dhauli has Ashoka's Kalinga edicts.",
        "Hathigumpha = elephant cave, Udayagiri.", 25)
    S.q("ga-lit-p4", "easy", "The earliest coins of India, the **punch-marked** pieces, were made mainly of —",
        ["Gold", "Silver", "Copper", "Lead"], "Silver",
        "The earliest indigenous coins were **punch-marked silver** pieces (often called 'punch-marked karshapana'), used by the mahajanapadas and the Mauryas.",
        "Punch-marked = silver.", 20)
    return S
