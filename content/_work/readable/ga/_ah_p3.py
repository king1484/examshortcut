"""Ancient History part 3: Post-Mauryan Age, Gupta Age and Harsha."""
from _ah_common import pat, trick, mk

S = {}

# ---------------------------------------------------------------- post-mauryan
S["post-mauryan"] = dict(
    concept=(
        "After the Mauryas, north India saw the Shungas and Kanvas, while the Satavahanas ruled the Deccan. "
        "Groups from Central Asia also entered the north-west: Indo-Greeks, Shakas, Parthians and Kushanas. "
        "Kanishka was the greatest Kushana. "
        "Exams ask about rulers, coins, eras and Indo-Roman trade."
    ),
    notes=r"""### Shungas and Kanvas
| Dynasty | Key facts |
|---|---|
| **Shunga** (c. 185 to 73 BCE) | **Pushyamitra Shunga** killed Brihadratha. He performed **2 Ashvamedhas**. **Patanjali** lived in his age. Agnimitra is the hero of Kalidasa's *Malavikagnimitram*. Bharhut stupa railings date here. |
| **Kanva** (c. 73 to 28 BCE) | **Vasudeva Kanva** killed the last Shunga king. The Satavahanas ended the Kanvas. |

### Foreign dynasties in the north-west
Learn them in order of arrival: Indo-Greeks, Shakas, Parthians, Kushanas.

| Group | Key ruler | Facts |
|---|---|---|
| **Indo-Greeks** | **Menander (Milinda)**, capital **Sakala (Sialkot)** | First coins with a king's portrait; *Milindapanha*; roots of Gandhara art |
| **Shakas** | **Rudradaman I** (Ujjain) | **Junagadh inscription**: first long inscription in chaste **Sanskrit**; repaired **Sudarshana lake** |
| **Parthians** | **Gondophernes** | Tradition links him with St. Thomas |
| **Kushanas** | Kujula Kadphises, Vima Kadphises, **Kanishka** | See below |

The Sudarshana lake was first built under Chandragupta Maurya's governor **Pushyagupta**.

### The Kushanas
**Vima Kadphises** issued large gold coins with Shiva on them.

**Kanishka** began the **Shaka era** in **78 CE**. It is the base of India's **National Calendar**.

- Capital: **Purushapura (Peshawar)**. Second centre: **Mathura**.
- He held the **Fourth Buddhist Council** at Kundalvana, Kashmir. He backed **Mahayana**.
- His court: **Ashvaghosha** (*Buddhacharita*), **Nagarjuna**, **Vasumitra**, physician **Charaka**.
- Two art schools grew. **Gandhara** used grey schist and a Greco-Roman style. **Mathura** used red sandstone and Indian style.

> **Watch:** The Shaka era was begun by Kanishka, a Kushana, not by a Shaka ruler.

### The Satavahanas
The Satavahanas ruled the Deccan. **Simuka** founded the dynasty. The capital was **Pratishthana (Paithan)** on the Godavari.

- **Gautamiputra Satakarni** was the greatest king. He destroyed the Kshaharata Shakas under **Nahapana**.
- His mother **Gautami Balashri**'s **Nasik inscription** praises him.
- **Hala** wrote *Gathasaptashati* in Prakrit.
- They gave the first **tax-free land grants to Brahmanas**.
- Their coins were of **lead** and potin. Their language was **Prakrit**.

**Kharavela** of Kalinga was a Jain patron. His record is the **Hathigumpha inscription** at Udayagiri, Odisha.

### Eras
| Era | Starts | Linked with |
|---|---|---|
| **Vikram Samvat** | **57 BCE** | Vikramaditya of Ujjain |
| **Shaka Samvat** | **78 CE** | **Kanishka** |
| Gupta era | 319 to 320 CE | Chandragupta I |
| Harsha era | 606 CE | Harshavardhana |

> **Tip:** Vikram Samvat: subtract 57 to get CE. Shaka: add 78.

### Indo-Roman trade
Yavana (Roman) traders came to Indian ports.

- **Tamralipti** in the east.
- **Bharuch** and **Sopara** in the west.
- **Muziris** in Kerala.
- **Arikamedu** near Pondicherry, where Roman pottery, lamps and beads were found.

Large hoards of **Roman gold coins** show that trade favoured India. The guide *Periplus of the Erythraean Sea* describes these ports.
""",
    tricks=[
        trick("57 minus, 78 plus",
              "Vikram Samvat is **57 BCE**, so subtract. Shaka is **78 CE**, so add.",
              "Shaka year 1948 matches which CE year?",
              ["Add 78 to the Shaka year.", "1948 + 78 = 2026."],
              "2026 CE"),
        trick("Satavahana: S-P-G-H",
              "**S**imuka founder. **P**ratishthana capital. **G**autamiputra greatest. **H**ala poet."),
    ],
    mistakes=[
        mk("Giving Rudradaman's Junagadh inscription in Prakrit.",
           "Ashoka's edicts are Prakrit. Rudradaman's Junagadh inscription is in **Sanskrit**."),
        mk("Saying a Shaka ruler began the Shaka era.", "**Kanishka**, a Kushana, began it in 78 CE."),
        mk("Confusing Charaka with Sushruta.", "Charaka was Kanishka's physician. Sushruta is the surgeon."),
        mk("Placing the Kanvas before the Shungas.", "Order: Shunga (185 BCE), then Kanva (73 BCE)."),
    ],
    revision=[
        "Heartland order: Shunga (185 to 73 BCE), then Kanva (73 to 28 BCE).",
        "North-west order: Indo-Greeks, Shakas, Parthians, Kushanas.",
        "Menander and Nagasena wrote the Milindapanha. Indo-Greeks gave the first portrait coins.",
        "Rudradaman I: Junagadh inscription, chaste Sanskrit, Sudarshana lake.",
        "Kanishka: Shaka era 78 CE, Peshawar and Mathura, Fourth Council, Gandhara and Mathura art.",
        "Satavahanas: Simuka, Pratishthana, Gautamiputra Satakarni, first Brahmana land grants, lead coins.",
        "Ports: Tamralipti, Bharuch, Sopara, Muziris. Arikamedu has Roman finds.",
    ],
    patterns=[
        pat("ga-post-p1", "Post-Mauryan dynasties and their kings", "very common",
            "\"Which dynasty came after the Shungas\", \"Rudradaman belonged to\", or an order of dynasties.",
            ["Heartland chain: Shunga, then Kanva.",
             "North-west chain: Indo-Greeks, Shakas, Parthians, Kushanas.",
             "King hooks: Menander Indo-Greek, Rudradaman Shaka, Gondophernes Parthian, Kanishka Kushana."],
            "Each king has one dynasty, so the king names the dynasty.",
            "Who repaired the Sudarshana lake and issued the first long inscription in chaste Sanskrit?",
            ["The inscription is at Junagadh.", "The Shaka ruler of Ujjain issued it."],
            "Rudradaman I"),
        pat("ga-post-p2", "Kanishka and the Kushanas", "very common",
            "\"The Shaka era was started by\", Kanishka's capitals, Gandhara and Mathura art, scholars at his court.",
            ["Kanishka: 78 CE Shaka era; Peshawar and Mathura.",
             "He held the Fourth Council. Hinayana and Mahayana split.",
             "Court: Ashvaghosha, Charaka, Vasumitra, Nagarjuna.",
             "Art: Gandhara (grey schist) and Mathura (red sandstone)."],
            "Kanishka collects many separate facts, so the era and the capitals are the anchors.",
            "Which Kushana ruler struck large gold issues showing Shiva on the coins?",
            ["Kanishka's predecessor issued them.", "He was Vima Kadphises."],
            "Vima Kadphises"),
        pat("ga-post-p3", "Satavahanas: rulers, capital and customs", "common",
            "\"Capital of the Satavahanas\", Gautamiputra Satakarni, first land grants, lead coins.",
            ["Founder Simuka. Capital Pratishthana (Paithan) on the Godavari.",
             "Greatest king: Gautamiputra Satakarni. Evidence: the Nasik inscription of his mother.",
             "Firsts: tax-free land grants to Brahmanas. Coins of lead and potin. Language Prakrit."],
            "The Satavahana facts are few and fixed.",
            "The greatest Satavahana ruler, whose deeds are told in his mother's Nasik inscription, was:",
            ["His mother was Gautami Balashri.", "His name begins with Gautami."],
            "Gautamiputra Satakarni"),
        pat("ga-post-p4", "Indo-Roman trade", "common",
            "\"Arikamedu is famous for\", \"the main east-coast port\", Roman gold hoards, the Periplus.",
            ["Ports: Tamralipti east; Bharuch and Sopara west; Muziris in Kerala; Arikamedu near Pondicherry.",
             "Arikamedu gave Roman pottery, lamps and beads.",
             "Roman gold hoards show a trade surplus for India."],
            "Each port has one direction, so the direction helps.",
            "Which post-Mauryan site near Pondicherry is famous for Roman pottery and trade goods?",
            ["The site is on the south-east coast.", "Its finds include Roman lamps and beads."],
            "Arikamedu"),
        pat("ga-post-p5", "Eras and their founders", "common",
            "\"Vikram Samvat began in\", \"Shaka era started in\", \"Gupta era\", \"Harsha era\".",
            ["Vikram Samvat 57 BCE. Shaka 78 CE. Gupta 319 to 320 CE. Harsha 606 CE.",
             "To change a Vikram Samvat year to CE, subtract 57.",
             "To change a Shaka year to CE, add 78."],
            "Four dates cover all era questions.",
            "The Shaka Samvat, used in India's National Calendar, began in:\n(a) 57 BCE (b) 78 CE (c) 319 CE (d) 606 CE",
            ["57 BCE is Vikram Samvat.", "319 CE is the Gupta era and 606 CE the Harsha era."],
            "(b) 78 CE"),
    ],
)

# ---------------------------------------------------------------- gupta-harsha
S["gupta-harsha"] = dict(
    concept=(
        "The Guptas ruled north India from about 320 CE and their age is called the classical or golden age. "
        "Harshavardhana was the last great northern king before the early medieval age. "
        "Exams ask about each ruler's title, scholars, books, Chinese pilgrims and Harsha's reign."
    ),
    notes=r"""### The Gupta line
| Ruler | Facts |
|---|---|
| Sri Gupta, Ghatotkacha | First two rulers |
| **Chandragupta I** | First *Maharajadhiraja*; married Licchavi princess **Kumaradevi**; **Gupta era 319 to 320 CE** |
| **Samudragupta** (c. 335 to 375) | **Prayag Prashasti** by **Harishena**; "**Napoleon of India**"; *Kaviraja* (veena on coins) |
| **Chandragupta II "Vikramaditya"** (c. 375 to 415) | Beat the Western Kshatrapas; **Navaratnas**; visited by **Fa-Hien**; Mehrauli Iron Pillar |
| **Kumaragupta I** | Founded **Nalanda** |
| **Skandagupta** | Stopped the **Hunas**; repaired **Sudarshana lake** |

The Prayag Prashasti is on the Allahabad pillar. It says Samudragupta uprooted nine kings of Aryavarta. It says he defeated but reinstated twelve rulers of Dakshinapatha.

Chandragupta II's daughter **Prabhavatigupta** married the Vakataka **Rudrasena II**. The Huns **Toramana** and **Mihirakula** came later. **Yashodharman** of Malwa defeated Mihirakula.

Gupta gold coins were called **dinaras**.

### Why it is called a golden age
**Science**

| Scholar | Work |
|---|---|
| **Aryabhata** | *Aryabhatiya* (499 CE): the earth rotates; eclipses come from shadows; place value |
| **Varahamihira** | *Brihat Samhita*, *Pancha Siddhantika* |
| **Brahmagupta** | *Brahmasphuta Siddhanta* (628 CE): rules for zero |
| Vagbhata | *Ashtanga Hridaya* (medicine) |

**Literature**

- **Kalidasa:** *Abhijnanashakuntalam*, *Meghaduta*, *Raghuvamsha*, *Kumarasambhava*, *Malavikagnimitram*.
- **Vishnu Sharma:** *Panchatantra*. **Amarasimha:** *Amarakosha*.
- **Dandin:** *Dashakumaracharita*. **Bharavi:** *Kiratarjuniya*.

**Art**

- **Dashavatara temple, Deogarh** shows an early shikhara.
- **Bhitargaon** brick temple, near Kanpur.
- **Udayagiri caves** near Vidisha have a Varaha panel.
- **Ajanta** murals reached their peak.

> **Watch:** Fa-Hien noted untouchability. The Eran inscription (510 CE) gives the first proof of sati.

### Chinese pilgrims
| Pilgrim | Years | Ruler | Book |
|---|---|---|---|
| **Fa-Hien** | 399 to 414 CE | Chandragupta II | *Fo-kwo-ki* |
| **Hiuen Tsang** | c. 630 to 645 CE | Harsha | *Si-Yu-Ki* |
| **I-Tsing** | 671 to 695 CE | After Harsha | Studied at Nalanda |

> **Tip:** F-H-I: Fa-Hien, Hiuen Tsang, I-Tsing. This is alphabetical and also the order in time.

### Harshavardhana
Harsha ruled from **606 to 647 CE**. He belonged to the **Pushyabhuti (Vardhana)** house of **Thanesar**. He moved his capital to **Kannauj**. The **Harsha era** starts in 606 CE.

- **Banabhatta** wrote *Harshacharita* and *Kadambari*.
- Harsha wrote three plays: *Nagananda*, *Ratnavali*, *Priyadarshika*.
- **Pulakeshin II** stopped him on the **Narmada**. The Aihole inscription by **Ravikirti** records this.
- He held an assembly at **Kannauj** in 643 CE to honour Hiuen Tsang.
- Every five years he held the **Prayag** assembly (*Mahamoksha Parishad*).

Hiuen Tsang studied at Nalanda and was called the "Prince of Pilgrims".
""",
    tricks=[
        trick("Gupta order",
              "Sri Gupta, Ghatotkacha, then **Chandragupta I**, **Samudragupta**, **Chandragupta II**, **Kumaragupta I**, **Skandagupta**."),
        trick("Inscription authors: H, R, B",
              "**H**arishena wrote the Prayag Prashasti of Samudragupta. **R**avikirti wrote the Aihole inscription of Pulakeshin II. "
              "**B**anabhatta wrote Harsha's biography.",
              "Who composed the Aihole inscription?",
              ["Aihole belongs to Pulakeshin II.", "Its poet was Ravikirti."],
              "Ravikirti"),
        trick("Pilgrims: F-H-I",
              "Fa-Hien (Chandragupta II), then Hiuen Tsang (Harsha), then I-Tsing."),
    ],
    mistakes=[
        mk("Saying Fa-Hien came in Harsha's time.", "Fa-Hien came under **Chandragupta II**. Hiuen Tsang came under **Harsha**."),
        mk("Saying Harishena praised Chandragupta II.", "Harishena praised **Samudragupta**."),
        mk("Calling the Mehrauli Iron Pillar a Sultanate work.", "It is Gupta. It bears the name of king Chandra."),
        mk("Giving Aryabhata's birth year for the Aryabhatiya.", "Aryabhata was born in 476 CE. The *Aryabhatiya* is of 499 CE."),
    ],
    revision=[
        "Chain: Chandragupta I, Samudragupta, Chandragupta II, Kumaragupta I, Skandagupta.",
        "Samudragupta: Prayag Prashasti by Harishena, Napoleon of India, Kaviraja.",
        "Chandragupta II: Vikramaditya, beat the Shakas, Navaratnas with Kalidasa, Fa-Hien.",
        "Kumaragupta I founded Nalanda. Skandagupta stopped the Huns and repaired Sudarshana lake.",
        "Aryabhata wrote the Aryabhatiya. Varahamihira wrote the Brihat Samhita.",
        "Harsha: Thanesar, then Kannauj; Banabhatta; three plays; stopped by Pulakeshin II.",
    ],
    patterns=[
        pat("ga-gup-p1", "Gupta ruler and achievement or title", "very common",
            "\"Napoleon of India\", who defeated the Shakas or Huns, Prashasti facts, founder of Nalanda.",
            ["Samudragupta: Prayag Prashasti, Kaviraja, Napoleon of India.",
             "Chandragupta II: Vikramaditya, beat the Western Shakas, Navaratnas.",
             "Kumaragupta I: Nalanda. Skandagupta: Huns and Sudarshana lake."],
            "Each ruler has one clear title or deed.",
            "Which Gupta ruler took the title Vikramaditya after destroying the Western Shakas?",
            ["Fa-Hien visited during his reign.", "He was the son of Samudragupta."],
            "Chandragupta II"),
        pat("ga-gup-p2", "Science and literature of the Gupta age", "very common",
            "\"The Aryabhatiya was written by\", \"which work is by Kalidasa\", author pairs.",
            ["Science: Aryabhata (Aryabhatiya), Varahamihira (Brihat Samhita).",
             "Kalidasa: Shakuntalam, Meghaduta, Raghuvamsha, Kumarasambhava, Malavikagnimitram.",
             "Pairs: Panchatantra-Vishnu Sharma, Amarakosha-Amarasimha, Dashakumaracharita-Dandin, Kiratarjuniya-Bharavi."],
            "Setters use only these author and book pairs.",
            "The Panchatantra, a collection of animal fables, is attributed to:",
            ["It is a Sanskrit fable book.", "Its author's name begins with Vishnu."],
            "Vishnu Sharma"),
        pat("ga-gup-p3", "Harsha: capital, assemblies and court", "common",
            "Kannauj, Banabhatta, Harsha's plays, the Kannauj and Prayag assemblies, defeat on the Narmada.",
            ["Harsha of Thanesar ruled from Kannauj; title Siladitya.",
             "Banabhatta wrote Harshacharita and Kadambari. Harsha wrote Nagananda, Ratnavali, Priyadarshika.",
             "Assemblies at Kannauj and Prayag. Pulakeshin II checked him on the Narmada."],
            "Harsha's facts come in small sets of two or three.",
            "Harshavardhana shifted his capital from Thanesar to:",
            ["The new capital became the prize of later struggles.", "It is Kannauj."],
            "Kannauj"),
        pat("ga-gup-p4", "Visitors and the rulers they met", "very common",
            "Match Megasthenes, Fa-Hien, Hiuen Tsang, I-Tsing (and Deimachus, Dionysius) to the courts they saw.",
            ["Megasthenes with Chandragupta Maurya. Deimachus with Bindusara. Dionysius with Ashoka.",
             "Fa-Hien with Chandragupta II. Hiuen Tsang with Harsha. I-Tsing after Harsha.",
             "Books: Indica (Megasthenes), Si-Yu-Ki (Hiuen Tsang)."],
            "One list of visitor and ruler pairs answers every match question.",
            "Which Chinese pilgrim visited India after Harsha's death and studied in its monasteries from 671 to 695?",
            ["Fa-Hien came in the Gupta age.", "Hiuen Tsang came in Harsha's reign."],
            "I-Tsing"),
        pat("ga-gup-p5", "Gupta art, coins and temples", "occasional",
            "\"Dashavatara temple\", \"dinara\", \"Udayagiri\", \"Bhitargaon\", \"Ajanta\".",
            ["Dashavatara temple is at Deogarh. Bhitargaon is a brick temple.",
             "Udayagiri caves (Vidisha) have the Varaha panel.",
             "Gupta gold coins were dinaras."],
            "Each site has one signature feature.",
            "Gupta gold coins were known as:",
            ["The name is like the Roman denarius.", "The Gupta term is dinara."],
            "Dinaras"),
        pat("ga-gup-p6", "Dark side of the golden age", "occasional",
            "\"First epigraphic proof of sati\", \"untouchability noted by\", \"status of women\".",
            ["Eran inscription, 510 CE: first proof of sati.",
             "Fa-Hien noted untouchability.",
             "Women's status fell in this age."],
            "Setters use the golden-age label to trap you with the negatives.",
            "The first epigraphic proof of sati comes from which Gupta-age inscription?",
            ["The site is in central India.", "The year is 510 CE."],
            "The Eran inscription (510 CE)"),
    ],
)
