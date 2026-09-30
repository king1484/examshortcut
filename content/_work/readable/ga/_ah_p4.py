"""Ancient History part 4: South Indian dynasties and Ancient literature."""
from _ah_common import pat, trick, mk

S = {}

# ---------------------------------------------------------------- south-dynasties
S["south-dynasties"] = dict(
    concept=(
        "South India had the Sangam kingdoms of Chera, Chola and Pandya, then the Pallavas, Chalukyas, Rashtrakutas and Imperial Cholas. "
        "Each dynasty is remembered for its rulers, capital, temples and literature. "
        "Exams ask you to match dynasty, king, monument and emblem."
    ),
    notes=r"""### The Sangam kingdoms
| Kingdom | Capital and port | Emblem | Famous king |
|---|---|---|---|
| **Chera** | **Vanji**; ports **Muziris** and **Tondi** | **Bow** | **Senguttuvan** |
| **Chola** | **Uraiyur**; port **Puhar** | **Tiger** | **Karikala**, built the **Kallanai** dam |
| **Pandya** | **Madurai**; port **Korkai** | **Fish** | **Nedunjeliyan** |

> **Tip:** Chera bow, Chola tiger, Pandya fish. The letters B-T-F give the order.

### Sangam literature
- **Tolkappiyam**: the oldest Tamil grammar.
- **Tirukkural** by **Thiruvalluvar**: couplets on ethics.
- **Silappadikaram** by **Ilango Adigal**. **Manimekalai** by **Sittalai Sattanar**.
- **Ettuthokai** and **Pattupattu**: the eight anthologies and ten idylls.
- Poems are of two kinds: **akam** (love) and **puram** (war and praise).

### Pallavas of Kanchi
- **Mahendravarman I** was a patron of rock-cut temples.
- **Narasimhavarman I "Mamalla"** took **Vatapi** and took the title **Vatapikonda**. Mamallapuram is his city.
- **Rajasimha** built the **Shore Temple** and the **Kailasanatha temple** at Kanchi.

Their style moved from rock-cut caves to monolithic *rathas* and then to structural temples.

### Chalukyas of Badami
**Pulakeshin II** stopped Harsha on the Narmada. His temples are at **Aihole** and **Pattadakal**.

### Rashtrakutas
**Krishna I** carved the **Kailasa temple** at **Ellora**. **Amoghavarsha** wrote *Kavirajamarga*, the first Kannada poetics work.

The **tripartite struggle** for **Kannauj** was among the **Palas**, **Pratiharas** and **Rashtrakutas**.

### Imperial Cholas
Order: **Vijayalaya** (founder, Thanjavur), then **Parantaka I**, then **Rajaraja I**, then **Rajendra I**.

- **Parantaka I**: the **Uttaramerur** inscriptions describe village self-government.
- **Rajaraja I** built the **Brihadeeswara temple**, Thanjavur.
- **Rajendra I** built a new capital and took Ganga water north.
- Local bodies were the **Ur**, **Sabha** and **Nagaram**. Members were chosen by **kudavolai** (a lot system).

The Chola temples at Thanjavur, Gangaikonda Cholapuram and Darasuram are **UNESCO** sites.

### Rulers to remember
| Dynasty | Founder or best-known king | Seat |
|---|---|---|
| Pallava | Mahendravarman I | Kanchi |
| Chalukya of Badami | Pulakeshin II | Badami (Vatapi) |
| Rashtrakuta | Krishna I | Manyakheta |
| Imperial Chola | Vijayalaya | Thanjavur |

Each dynasty has one signature monument. Learn the monument with the king.

### Temple styles
| Style | Region |
|---|---|
| **Nagara** | North India |
| **Dravida** | South India |
| **Vesara** | Deccan, a mix of both |

> **Rule:** Pallava, Chola and Pandya temples are Dravida. Chalukya temples show Vesara traits.
""",
    tricks=[
        trick("B-T-F",
              "Chera **B**ow, Chola **T**iger, Pandya **F**ish."),
        trick("Imperial Cholas: V-P-R-R",
              "Vijayalaya, Parantaka, Rajaraja, Rajendra."),
    ],
    mistakes=[
        mk("Saying Rajaraja I built the Kailasa temple.", "Kailasa (Ellora) is Rashtrakuta. Rajaraja I built the Brihadeeswara temple."),
        mk("Calling the Shore Temple Chola.", "The Shore Temple is Pallava, built by Rajasimha."),
        mk("Giving the Chera emblem as fish.", "Fish is Pandya. Chera has the bow."),
        mk("Confusing Aihole with Ellora.", "Aihole and Pattadakal are Chalukya. Ellora Kailasa is Rashtrakuta."),
    ],
    revision=[
        "Sangam: Chera (Vanji, bow), Chola (Uraiyur, tiger), Pandya (Madurai, fish).",
        "Tolkappiyam is the grammar. Tirukkural is by Thiruvalluvar.",
        "Pallavas: Mahendravarman I, Narasimhavarman I Mamalla, Rajasimha (Shore Temple, Kailasanatha).",
        "Chalukyas of Badami: Pulakeshin II, Aihole and Pattadakal.",
        "Rashtrakutas: Krishna I (Kailasa, Ellora), Amoghavarsha (Kavirajamarga).",
        "Imperial Cholas: Vijayalaya, Parantaka I, Rajaraja I, Rajendra I.",
        "Tripartite struggle: Palas, Pratiharas, Rashtrakutas for Kannauj.",
    ],
    patterns=[
        pat("ga-sou-p1", "Sangam kingdoms: capital, port, emblem", "very common",
            "\"Emblem of the Pandyas\", \"capital of the Cheras\", \"port of the Cholas\".",
            ["Chera: Vanji, Muziris and Tondi, bow.",
             "Chola: Uraiyur, Puhar, tiger.",
             "Pandya: Madurai, Korkai, fish."],
            "Each kingdom has a fixed set of capital, port and emblem.",
            "Which Sangam kingdom had Madurai as its capital and the fish as its emblem?",
            ["The fish is a Pandya emblem.", "Madurai was its capital."],
            "The Pandyas"),
        pat("ga-sou-p2", "Sangam literature and authors", "common",
            "\"Tirukkural was written by\", \"oldest Tamil grammar\", Silappadikaram or Manimekalai.",
            ["Tolkappiyam: grammar. Tirukkural: Thiruvalluvar.",
             "Silappadikaram: Ilango Adigal. Manimekalai: Sittalai Sattanar.",
             "Anthologies: Ettuthokai and Pattupattu."],
            "Text and author pairs are fixed.",
            "The Tamil epic Silappadikaram was composed by:",
            ["The author was a Chera prince turned monk.", "His name is Ilango Adigal."],
            "Ilango Adigal"),
        pat("ga-sou-p3", "Pallava, Chalukya and Rashtrakuta monuments", "very common",
            "\"Shore Temple\", \"Kailasa temple\", \"Aihole and Pattadakal\", \"Vatapikonda\".",
            ["Pallava: Mahendravarman I rock-cut, Mamalla rathas, Rajasimha Shore Temple and Kailasanatha.",
             "Chalukya: Aihole and Pattadakal.",
             "Rashtrakuta: Kailasa temple, Ellora, by Krishna I."],
            "Every monument links to one dynasty and one king.",
            "Which dynasty built the monolithic Kailasa temple at Ellora?",
            ["It was carved in a single rock.", "Krishna I was the king."],
            "The Rashtrakutas"),
        pat("ga-sou-p4", "Imperial Cholas and local government", "very common",
            "\"Brihadeeswara temple builder\", Uttaramerur, Ur and Sabha, kudavolai.",
            ["Founder Vijayalaya. Then Parantaka I, Rajaraja I, Rajendra I.",
             "Rajaraja I: Brihadeeswara, Thanjavur.",
             "Local bodies: Ur, Sabha, Nagaram. The Uttaramerur inscriptions of Parantaka I describe them."],
            "The Chola chain and its local-government terms answer most questions.",
            "The Uttaramerur inscriptions of Parantaka I describe:",
            ["They are on a temple wall in Tamil Nadu.", "They tell how village bodies were chosen."],
            "Village self-government (Sabha members chosen by lot)"),
        pat("ga-sou-p5", "Temple styles and the tripartite struggle", "occasional",
            "\"Nagara, Dravida, Vesara\", \"struggle for Kannauj\".",
            ["Nagara: north. Dravida: south. Vesara: Deccan mix.",
             "Tripartite struggle: Palas, Pratiharas, Rashtrakutas.",
             "The prize was Kannauj."],
            "Style names and struggle names are asked as short lists.",
            "The tripartite struggle for Kannauj involved the Palas, Rashtrakutas and:",
            ["The third power ruled from the west and north.", "It began with the letter P."],
            "The Pratiharas"),
    ],
)

# ---------------------------------------------------------------- ancient-literature
S["ancient-literature"] = dict(
    concept=(
        "Ancient Indian literature includes Sanskrit epics and plays, Pali and Ardhamagadhi religious texts and Tamil Sangam works. "
        "Foreign accounts and inscriptions add to the record. "
        "Exams mostly ask you to match a book with its author."
    ),
    notes=r"""### Sanskrit works and authors
| Work | Author |
|---|---|
| *Ramayana* | **Valmiki** |
| *Mahabharata* | **Vyasa** |
| *Ashtadhyayi* | **Panini** |
| *Mahabhashya* | **Patanjali** |
| *Arthashastra* | **Kautilya** |
| *Natyashastra* | **Bharata** |
| *Buddhacharita* | **Ashvaghosha** |
| *Shakuntalam*, *Meghaduta*, *Raghuvamsha* | **Kalidasa** |
| *Mudrarakshasa* | **Vishakhadatta** |
| *Mrichchhakatika* | **Shudraka** |
| *Swapnavasavadatta* | **Bhasa** |
| *Kamasutra* | **Vatsyayana** |
| *Panchatantra* | **Vishnu Sharma** |
| *Hitopadesha* | **Narayana Pandit** |
| *Amarakosha* | **Amarasimha** |
| *Harshacharita*, *Kadambari* | **Banabhatta** |
| *Kiratarjuniya* | **Bharavi** |
| *Shishupalavadha* | **Magha** |
| *Dashakumaracharita* | **Dandin** |
| *Rajatarangini* | **Kalhana** |
| *Brihatkatha* | **Gunadhya** |

> **Note:** *Manusmriti* is a law text. *Rajatarangini* is the first history book of Kashmir.

### Science and medicine
- **Charaka** wrote on medicine.
- **Sushruta** wrote on surgery.
- **Aryabhata**, **Varahamihira** and **Brahmagupta** wrote on astronomy and maths.
- **Vagbhata** wrote *Ashtanga Hridaya*.

### Religious literature
- The Buddhist canon is the **Tripitaka**, in **Pali**.
- The Jain canon is in **Ardhamagadhi**.
- **Deepavamsha** and **Mahavamsha** are Sri Lankan chronicles that mention Ashoka.

### Foreign accounts
| Source | Author |
|---|---|
| *Indica* | **Megasthenes** |
| *Fo-kwo-ki* | **Fa-Hien** |
| *Si-Yu-Ki* | **Hiuen Tsang** |
| *Periplus of the Erythraean Sea* | Unknown Greek sailor |

Pliny and Ptolemy also described India.

### Other texts to know
| Text | Note |
|---|---|
| *Manusmriti* | Law text of the Manu tradition |
| *Milindapanha* | Dialogue of Menander and the monk Nagasena |
| *Gathasaptashati* | Prakrit verses by the Satavahana king **Hala** |
| *Kavirajamarga* | Early Kannada poetics by **Amoghavarsha** |
| *Tirukkural* | Tamil couplets by **Thiruvalluvar** |
| *Silappadikaram* | Tamil epic by **Ilango Adigal** |

The Vedas, Brahmanas, Upanishads and Puranas are religious and philosophical texts. Use them with care as history.

> **Watch:** A Sangam text is Tamil. A Pali text is Buddhist. Do not mix the language with the region.

### Inscriptions and coins
**James Prinsep** deciphered **Brahmi** in **1837**. The **Hathigumpha** inscription tells of **Kharavela**.

> **Tip:** Coin ladder: punch-marked coins came first. The Indo-Greeks issued portrait coins. The Kushanas issued gold. The Guptas issued dinaras.
""",
    tricks=[
        trick("Kalidasa's three K-words",
              "Kalidasa wrote **M**eghaduta, **R**aghuvamsha, **K**umarasambhava, **S**hakuntalam. Shakuntalam is his most famous play."),
        trick("Two chroniclers",
              "**Kalhana** wrote the history of Kashmir. **Banabhatta** wrote Harsha's life."),
    ],
    mistakes=[
        mk("Giving Kautilya as author of the Mudrarakshasa.", "Kautilya wrote the Arthashastra. **Vishakhadatta** wrote the Mudrarakshasa."),
        mk("Attributing Panchatantra to Narayana Pandit.", "Panchatantra is by **Vishnu Sharma**. Narayana Pandit wrote the Hitopadesha."),
        mk("Confusing Charaka and Sushruta.", "Charaka is for medicine. Sushruta is for surgery."),
        mk("Placing Prinsep's decipherment of Brahmi before 1800.", "Prinsep deciphered Brahmi in 1837."),
    ],
    revision=[
        "Ramayana: Valmiki. Mahabharata: Vyasa. Ashtadhyayi: Panini. Arthashastra: Kautilya.",
        "Kalidasa: Shakuntalam, Meghaduta, Raghuvamsha, Kumarasambhava.",
        "Mudrarakshasa: Vishakhadatta. Mrichchhakatika: Shudraka. Swapnavasavadatta: Bhasa.",
        "Rajatarangini: Kalhana. Harshacharita and Kadambari: Banabhatta.",
        "Indica: Megasthenes. Fo-kwo-ki: Fa-Hien. Si-Yu-Ki: Hiuen Tsang.",
        "Buddhist canon: Pali Tripitaka. Jain canon: Ardhamagadhi.",
        "Prinsep deciphered Brahmi in 1837.",
    ],
    patterns=[
        pat("ga-lit-p1", "Match the Sanskrit book with its author", "very common",
            "A book title in the stem and four author names in the options.",
            ["Recall the author table row by row.",
             "Group plays: Bhasa, Shudraka, Vishakhadatta, Kalidasa.",
             "Group prose: Banabhatta, Dandin."],
            "The same author-book pairs repeat in exams.",
            "The Mrichchhakatika is a play by:",
            ["It is a social play about a merchant and a courtesan.", "Its author is Shudraka."],
            "Shudraka"),
        pat("ga-lit-p2", "Historical value of texts", "common",
            "\"Which book is a history of Kashmir\", \"biography of Harsha\", \"Sri Lankan chronicles\".",
            ["Rajatarangini: Kalhana, Kashmir.",
             "Harshacharita: Banabhatta, Harsha.",
             "Deepavamsha and Mahavamsha: Sri Lanka."],
            "Each historical work has one subject.",
            "Kalhana's Rajatarangini is a chronicle of:",
            ["It is the first history text of its kind.", "It concerns a northern region."],
            "Kashmir"),
        pat("ga-lit-p3", "Foreign accounts", "very common",
            "\"Indica\", \"Fo-kwo-ki\", \"Si-Yu-Ki\", \"Periplus\".",
            ["Megasthenes: Indica.",
             "Fa-Hien: Fo-kwo-ki. Hiuen Tsang: Si-Yu-Ki.",
             "Periplus: an unknown Greek sailor."],
            "Each account has one author or one pilgrim.",
            "The book Fo-kwo-ki is an account by:",
            ["The traveller was Chinese.", "He came under Chandragupta II."],
            "Fa-Hien"),
        pat("ga-lit-p4", "Scientific writers", "common",
            "\"Father of Indian surgery\", \"Aryabhatiya\", \"Brahmasphuta Siddhanta\".",
            ["Charaka: medicine. Sushruta: surgery.",
             "Aryabhata: Aryabhatiya. Varahamihira: Brihat Samhita. Brahmagupta: Brahmasphuta Siddhanta.",
             "Vagbhata: Ashtanga Hridaya."],
            "Each scholar has one field and one book.",
            "The Brahmasphuta Siddhanta was written by:",
            ["It dates to 628 CE.", "Its author gave rules for zero."],
            "Brahmagupta"),
        pat("ga-lit-p5", "Religious canons and inscriptions", "occasional",
            "\"Language of the Tripitaka\", \"Jain canon\", \"Who deciphered Brahmi\", \"Hathigumpha\".",
            ["Buddhist canon: Tripitaka in Pali.",
             "Jain canon: Ardhamagadhi.",
             "Prinsep deciphered Brahmi in 1837. Hathigumpha: Kharavela."],
            "Each source pairs with one language or person.",
            "The Buddhist Tripitaka was written in which language?",
            ["It is not Sanskrit.", "It is the language of the early Buddhist canon."],
            "Pali"),
    ],
)
