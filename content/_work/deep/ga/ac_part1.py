"""art-culture deep content — part 1: classical-dances, folk-dances, music-instruments."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub

# GA patterns carry no formula; accept 7-arg calls (id, name, frequency, howToSpot, logic, ex_q, ex_sol)
if not getattr(Sub.pattern, "_patched", False):
    _orig_pattern = Sub.pattern

    def _pattern7(self, pid, name, frequency, howToSpot, logic, ex_q, ex_sol):
        _orig_pattern(self, pid, name, frequency, howToSpot, None, logic, ex_q, ex_sol)

    _pattern7._patched = True
    Sub.pattern = _pattern7


def build_classical():
    S = Sub("classical-dances")
    S.notes = """### The nine classical dances
The **Sangeet Natak Akademi** recognises **8 classical dances**; the Ministry of Culture adds **Chhau** (making 9). Every dance is tied to one state — that pair is the core of the question.

| Dance | State | Signature | One famous name |
|---|---|---|---|
| Bharatanatyam | Tamil Nadu | Temple (devadasi) roots; oldest | Rukmini Devi Arundale |
| Kathak | UP / north | Mughal courts; chakkars, tatkar | Pt. Birju Maharaj |
| Kathakali | Kerala | Dance-drama; green (pacha) make-up | Kalamandalam Gopi |
| Mohiniyattam | Kerala | Lasya (graceful) solo of women | Sunanda Nair |
| Kuchipudi | Andhra Pradesh | Village Kuchipudi; plate (tarangam) balance | Raja & Radha Reddy |
| Odissi | Odisha | Tribhanga pose; temple dance of Jagannath | Kelucharan Mohapatra |
| Manipuri | Manipur | Raslila themes; soft, rounded movements | Jhaveri sisters |
| Sattriya | Assam | Sankaradeva's Vaishnava monasteries (sattra) | Indira P.P. Bora |
| Chhau | Odisha / Jharkhand / WB | Semi-classical martial dance | — |

Two Kerala dances and one UP dance — "Kerala has two" is the planted confusion: **Kathakali and Mohiniyattam** are Kerala; **Kathak** is the north Indian court dance.

### Exponents and revival
- **Rukmini Devi Arundale** — pulled Bharatanatyam out of its devadasi stigma and founded **Kalakshetra (1936)** at Chennai.
- **Vallathol Narayana Menon** — founded **Kerala Kalamandalam (1930)** to revive Kathakali.
- **Pt. Birju Maharaj** — Kathak of the **Lucknow gharana**; Sitara Devi was its celebrated 'Kathak queen'.
- **Kelucharan Mohapatra** — carried Odissi to the world stage.
- **Sonal Mansingh** — Odissi; Padma Vibhushan.

### Feature clues
Make-up and movement identify the dance faster than any list. **Kathakali**: elaborate green face (pacha = noble hero), codified hand language, drum-heavy. **Mohiniyattam**: white kasavu costume, lasya grace — 'the enchantress'. **Manipuri**: circular, flowing, never sharp — raslila of Radha-Krishna. **Odissi**: the **tribhanga** (three-bend) stance. **Kathak**: spinning chakkars and rhythmic footwork (tatkar), both Hindu and Mughal themes. **Sattriya**: the only classical dance born inside a monastery tradition, from **Srimanta Sankaradeva's** 15th-century Bhakti movement. **Kuchipudi**: male Brahmin theatre originally, by **Siddhendra Yogi's** codification; dancers often balance on a brass plate.

### The Chhau triangle
**Chhau** is a semi-classical masked/martial dance with three regional styles: **Mayurbhanj (Odisha — no masks)**, **Seraikella (Jharkhand — masks)** and **Purulia (West Bengal — masks)**. It entered the UNESCO Intangible Cultural Heritage list in **2010**.

### Quick revision
- SNA: 8 classical; +Chhau = 9. Kerala: Kathakali + Mohiniyattam; UP: Kathak.
- Bharatanatyam—TN; Kuchipudi—AP; Odissi—Odisha; Manipuri—Manipur; Sattriya—Assam.
- Rukmini Devi = Kalakshetra 1936; Vallathol = Kalamandalam 1930.
- Odissi = tribhanga; Kathak = chakkars; Sattriya = sattra/Sankaradeva.
- Chhau: Mayurbhanj (no mask), Seraikella + Purulia (masks); UNESCO ICH 2010."""
    S.pattern("ga-cd-p1", "Dance ↔ state", "very common",
      "A dance is named and four states given, or a 'correctly matched pair' question mixes classical and folk forms.",
      "Fix the nine classical pairs first (TN-Bharatanatyam, UP-Kathak, Kerala-Kathakali+Mohiniyattam, AP-Kuchipudi, Odisha-Odissi, Manipur-Manipuri, Assam-Sattriya), then eliminate; 'Kerala has two' is the usual trap.",
      "Kuchipudi is a classical dance of —",
      "**Andhra Pradesh**, named after the village Kuchipudi in Krishna district.")
    S.pattern("ga-cd-p2", "Exponent ↔ dance", "very common",
      "A dancer's name (Birju Maharaj, Rukmini Devi, Kelucharan Mohapatra…) with four dance options.",
      "One name per dance is enough: Arundale-Bharatanatyam, Birju Maharaj-Kathak, Mohapatra-Odissi, Gopi-Kathakali, Reddy duo-Kuchipudi, Jhaveri sisters-Manipuri.",
      "Pt. Birju Maharaj was a maestro of —",
      "**Kathak** — of the Lucknow gharana.")
    S.pattern("ga-cd-p3", "Dance ↔ feature or theme", "very common",
      "A clue is described — green make-up, tribhanga pose, raslila, plate balance, chakkars — and the dance asked.",
      "Map clue to dance: green make-up = Kathakali; tribhanga = Odissi; raslila = Manipuri; plate balance = Kuchipudi; chakkars = Kathak; lasya = Mohiniyattam; sattra origin = Sattriya.",
      "The **tribhanga** (three-bend) posture is characteristic of —",
      "**Odissi**, the temple dance of Odisha.")
    S.pattern("ga-cd-p4", "Institutions and recognition", "common",
      "'Kalakshetra was founded by', 'Kerala Kalamandalam year', or when a dance got classical status.",
      "Two revivals to memorise: Kerala Kalamandalam (Vallathol, 1930) for Kathakali; Kalakshetra (Rukmini Devi Arundale, 1936) for Bharatanatyam. Sattriya got classical recognition in 2000.",
      "**Kalakshetra**, the famous arts institution, was founded in 1936 by —",
      "**Rukmini Devi Arundale**, at Chennai, for Bharatanatyam.")

    S.q("ga-cd-p1", "easy", "The classical dance **Kathakali** belongs to —",
        ["Kerala", "Karnataka", "Tamil Nadu", "Andhra Pradesh"], "Kerala",
        "**Kathakali** is Kerala's story-dance; Vallathol founded Kerala Kalamandalam (1930) to revive it.",
        "Kathakali = Kerala.", 15)
    S.q("ga-cd-p1", "easy", "**Mohiniyattam**, the 'dance of the enchantress', is a classical dance of —",
        ["Kerala", "Odisha", "Manipur", "Assam"], "Kerala",
        "**Mohiniyattam** — Kerala's graceful lasya solo; Kerala thus has two classical dances, Kathakali and Mohiniyattam.",
        "Mohiniyattam = Kerala.", 15)
    S.q("ga-cd-p1", "medium", "Which classical dance is associated with the state of **Assam**?",
        ["Sattriya", "Manipuri", "Odissi", "Kuchipudi"], "Sattriya",
        "**Sattriya** was created by Srimanta Sankaradeva's Vaishnava tradition and preserved in the **sattra** monasteries of Assam.",
        "Sattriya = Assam (sattra).", 25)
    S.q("ga-cd-p1", "medium", "Which of the following is a classical dance of **North-East India** other than Sattriya?",
        ["Manipuri", "Cheraw", "Bihu", "Hojagiri"], "Manipuri",
        "**Manipuri** (Manipur) is classical — themed on the **raslila**; Bihu, Cheraw and Hojagiri are folk dances.",
        "Classical NE pair: Sattriya + Manipuri.", 25)
    S.q("ga-cd-p2", "easy", "The dancer **Kalamandalam Gopi** is a legendary performer of —",
        ["Kathakali", "Kathak", "Bharatanatyam", "Odissi"], "Kathakali",
        "**Kalamandalam Gopi** — a stellar Kathakali artiste from the Kerala Kalamandalam tradition.",
        "Kalamandalam = Kerala = Kathakali.", 20)
    S.q("ga-cd-p2", "easy", "**Raja and Radha Reddy** are renowned exponents of —",
        ["Kuchipudi", "Kathak", "Mohiniyattam", "Manipuri"], "Kuchipudi",
        "The **Reddy duo** carried Kuchipudi to world stages and run an academy in Delhi.",
        "Reddy = Kuchipudi.", 20)
    S.q("ga-cd-p2", "medium", "**Sonal Mansingh**, a Padma Vibhushan dancer, is associated mainly with —",
        ["Odissi", "Bharatanatyam", "Kathakali", "Sattriya"], "Odissi",
        "**Sonal Mansingh** — an Odissi (and Bharatanatyam) dancer, honoured with the Padma Vibhushan.",
        "Sonal Mansingh = Odissi.", 25)
    S.q("ga-cd-p3", "easy", "The elaborate **green face make-up (pacha)** is characteristic of —",
        ["Kathakali", "Kuchipudi", "Kathak", "Chhau"], "Kathakali",
        "In Kathakali, **pacha (green)** marks noble characters; knife characters wear red, demons black.",
        "Green = noble hero = Kathakali.", 15)
    S.q("ga-cd-p3", "medium", "Balancing on a **brass plate (tarangam)** while dancing is a specialty of —",
        ["Kuchipudi", "Odissi", "Mohiniyattam", "Manipuri"], "Kuchipudi",
        "The **tarangam** — dancing on the rim of a brass plate, sometimes with a pot on the head — is a Kuchipudi showpiece.",
        "Plate balance = Kuchipudi.", 25)
    S.q("ga-cd-p3", "medium", "The **raslila** theme of Radha and Krishna is central to which classical dance?",
        ["Manipuri", "Kathak", "Kuchipudi", "Bharatanatyam"], "Manipuri",
        "**Manipuri** dance grew out of the Vaishnava raslila tradition of Manipur; its movements are soft and circular.",
        "Raslila = Manipuri.", 25)
    S.q("ga-cd-p3", "hard", "Match the pose/feature with the dance:\n1. Chakkars (spins) — Kathak\n2. Lasya grace — Mohiniyattam\n3. Chauka stance — Odissi\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are correct: Kathak's spins, Mohiniyattam's lasya, and Odissi's square **chauka** stance (alongside tribhanga).",
        "Spin-lasya-chauka: Kathak-Mohiniyattam-Odissi.", 30)
    S.q("ga-cd-p4", "easy", "**Kerala Kalamandalam**, founded in 1930 to revive Kathakali, was set up by —",
        ["Vallathol Narayana Menon", "Rukmini Devi Arundale", "E. Krishna Iyer", "Rabindranath Tagore"], "Vallathol Narayana Menon",
        "Poet **Vallathol Narayana Menon** founded Kalamandalam in 1930; Rukmini Devi's Kalakshetra came six years later.",
        "Vallathol 1930; Arundale 1936.", 20)
    S.q("ga-cd-p4", "hard", "Consider the statements:\n1. Sattriya received classical dance status in 2000.\n2. Chhau is on UNESCO's Intangible Cultural Heritage list.\n3. Kathak has three major gharanas — Lucknow, Jaipur and Banaras.\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three hold: Sattriya was recognised classical in **2000**; Chhau entered the UNESCO ICH list in **2010**; Kathak's gharanas are Lucknow, Jaipur and Banaras.",
        "2000-2010-three gharanas: all true.", 30)
    return S


def build_folk():
    S = Sub("folk-dances")
    S.notes = """### Folk dances by state — the core table
| State | Dances (most asked in **bold**) |
|---|---|
| Gujarat | **Garba** (UNESCO ICH 2023), **Dandiya Raas**, Tippani |
| Rajasthan | **Ghoomar**, **Kalbelia** (ICH 2010), Chari, Kachchhi Ghodi |
| Punjab | **Bhangra** (men), **Giddha** (women) |
| Maharashtra | **Lavani**, Dhangari Gaja |
| Karnataka | **Yakshagana** (dance-drama) |
| Kerala | **Theyyam** (ritual), Ottam Thullal |
| Assam | **Bihu** |
| Mizoram | **Cheraw** (bamboo dance) |
| Tripura | **Hojagiri** (Reang balancing feats) |
| Meghalaya | **Nongkrem** (Khasi), Wangala (Garo) |
| Chhattisgarh | Karma, Panthi |
| Jharkhand | Karma, Chhau (Saraikela) |
| West Bengal | Chhau (Purulia) |

The North-East cluster (Cheraw–Hojagiri–Nongkrem) is a favourite match-the-column set: bamboo = Mizoram, balancing = Tripura, Khasi = Meghalaya.

### Feature and occasion clues
**Garba** — a circular women's dance of Navratri with clapping; **Dandiya Raas** uses sticks. **Ghoomar** — Bhil-origin, adopted by Rajasthan's royal houses, women in swirling ghagras. **Kalbelia** — of the snake-charmer Kalbelia community; imitative serpent movements; UNESCO ICH **2010**. **Bhangra/Giddha** — Baisakhi harvest. **Lavani** — fast tempo, dholki accompaniment, grown inside the **tamasha** theatre of Maharashtra. **Yakshagana** — Karnataka's night-long dance-drama with huge headgear; don't confuse it with Kathakali (Kerala). **Theyyam** — Kerala ritual where performers embody village goddesses, mostly male performers. **Bihu** — spring (Rongali) festival dance of Assam. **Cheraw** — dancers step between crossed bamboo staves clapped in rhythm. **Hojagiri** — Reang women balancing on pots and bottles. **Nongkrem** — Khasi thanksgiving dance. **Karma** — Karma-devi tree worship dance of Chhattisgarh-Jharkhand belt.

### The classical-folk border
**Chhau** sits on the border — semi-classical, martial, with three styles (Mayurbhanj, Seraikella, Purulia). **Yakshagana** is a folk dance-drama, not a classical dance. **Jatra** (Bengal) is folk theatre, not a dance. Exam setters swap these with classical names, so the state dance must be pinned before answering.

### Recognition to remember
- **Garba** — inscribed on UNESCO's ICH list in **2023** (India's newest dance element then).
- **Kalbelia, Chhau, Mudiyettu** — all inscribed in **2010**.
- **Durga Puja of Kolkata** (a festival, not a dance) — ICH **2021**.

### Quick revision
- Gujarat: Garba (ICH 2023) + Dandiya; Rajasthan: Ghoomar + Kalbelia (ICH 2010).
- Punjab: Bhangra/Giddha; Maharashtra: Lavani (tamasha); Karnataka: Yakshagana.
- Cheraw = Mizoram bamboo; Hojagiri = Tripura balancing; Nongkrem = Meghalaya Khasi.
- Theyyam = Kerala ritual; Bihu = Assam spring; Karma = Chhattisgarh-Jharkhand.
- 2010 ICH trio: Kalbelia, Chhau, Mudiyettu."""
    S.pattern("ga-fd-p1", "State ↔ folk dance", "very common",
      "A folk dance with four states as options, or a match-the-column of states and dances (often NE India).",
      "Run the state table; for the North-East use the feature mnemonic — bamboo = Cheraw (Mizoram), balancing = Hojagiri (Tripura), Khasi = Nongkrem (Meghalaya).",
      "**Cheraw**, the bamboo dance, belongs to —",
      "**Mizoram** — dancers step in and out of clapped bamboo staves.")
    S.pattern("ga-fd-p2", "Dance ↔ feature / community", "common",
      "A described feature — sticks, snake-like movements, dholki, goddess possession — and the dance asked.",
      "Garba = clapping circle of Navratri; Dandiya = sticks; Kalbelia = snake-charmer community; Lavani = dholki/tamasha; Theyyam = ritual possession.",
      "The **Kalbelia** dance, with its serpent-like movements, is performed by a community traditionally of —",
      "Snake charmers — the Kalbelia community of Rajasthan.")
    S.pattern("ga-fd-p3", "Dance ↔ occasion / season", "common",
      "Which dance is performed during Baisakhi/Navratri/Bihu — or a festival-dance pairing.",
      "Baisakhi = Bhangra/Giddha; Navratri = Garba/Dandiya; Rongali Bihu = Bihu dance; Kartik Purnima = Chhau season in Purulia.",
      "The **Bhangra** is traditionally performed during the festival of —",
      "**Baisakhi**, the Punjab harvest festival.")
    S.pattern("ga-fd-p4", "Classical-folk border traps", "common",
      "'Which of the following is NOT a classical dance', or a semi-classical form (Chhau, Yakshagana) slipped into a classical list.",
      "Chhau = semi-classical martial (three styles); Yakshagana = folk dance-drama of Karnataka; Jatra = Bengali folk theatre. Spot these before answering 'classical' questions.",
      "Which of these is a **semi-classical martial dance** rather than a fully classical form?",
      "**Chhau** — with Mayurbhanj, Seraikella and Purulia styles.")

    S.q("ga-fd-p1", "easy", "**Garba**, inscribed on UNESCO's Intangible Cultural Heritage list in 2023, is a folk dance of —",
        ["Gujarat", "Rajasthan", "Maharashtra", "Madhya Pradesh"], "Gujarat",
        "**Garba** is Gujarat's Navratri circle dance; it entered the UNESCO ICH list in **2023**.",
        "Garba = Gujarat, ICH 2023.", 15)
    S.q("ga-fd-p1", "easy", "**Bhangra** and **Giddha** are folk dances of —",
        ["Punjab", "Haryana", "Rajasthan", "Uttar Pradesh"], "Punjab",
        "**Bhangra** is the men's dance and **Giddha** the women's — both Punjabi, tied to the Baisakhi harvest.",
        "Bhangra (men) + Giddha (women) = Punjab.", 15)
    S.q("ga-fd-p1", "medium", "The **Hojagiri** dance, famous for balancing on pots and bottles, belongs to —",
        ["Tripura", "Manipur", "Mizoram", "Nagaland"], "Tripura",
        "**Hojagiri** — performed by Reang women of Tripura with astonishing balancing feats.",
        "Hojagiri = Tripura (Reang).", 25)
    S.q("ga-fd-p1", "medium", "**Nongkrem**, a thanksgiving folk dance, is performed by the Khasi community of —",
        ["Meghalaya", "Assam", "Arunachal Pradesh", "Tripura"], "Meghalaya",
        "**Nongkrem** — the Khasi harvest-thanksgiving dance of Meghalaya.",
        "Nongkrem = Khasi = Meghalaya.", 25)
    S.q("ga-fd-p1", "hard", "Match the North-East dances:\n1. Cheraw — Mizoram\n2. Hojagiri — Tripura\n3. Nongkrem — Nagaland\nWhich are correct?",
        ["1 and 2 only", "1, 2 and 3", "1 and 3 only", "2 and 3 only"], "1 and 2 only",
        "**Nongkrem** belongs to **Meghalaya** (Khasi), not Nagaland — Nagaland's famous festival is Hornbill.",
        "Nongkrem is Khasi — Meghalaya, not Nagaland.", 30)
    S.q("ga-fd-p2", "easy", "The **Lavani** dance, performed to the beats of the dholki, belongs to —",
        ["Maharashtra", "Gujarat", "Karnataka", "Andhra Pradesh"], "Maharashtra",
        "**Lavani** grew inside the **tamasha** folk theatre of Maharashtra; the dholki drives its tempo.",
        "Lavani + dholki + tamasha = Maharashtra.", 15)
    S.q("ga-fd-p2", "medium", "**Theyyam**, a ritual dance in which performers embody village deities, is practised in —",
        ["Kerala", "Tamil Nadu", "Karnataka", "Goa"], "Kerala",
        "**Theyyam** — north Kerala's ritual art where (mostly male) performers are possessed by the goddess; not a classical dance.",
        "Theyyam = Kerala ritual.", 25)
    S.q("ga-fd-p2", "medium", "**Yakshagana**, the spectacular night-long dance-drama with huge headgear, comes from —",
        ["Karnataka", "Kerala", "Andhra Pradesh", "Odisha"], "Karnataka",
        "**Yakshagana** is Karnataka's folk dance-drama — the Keralite counterpart is Kathakali (a classical form).",
        "Yakshagana = Karnataka; Kathakali = Kerala.", 25)
    S.q("ga-fd-p3", "easy", "**Bihu**, danced during the Rongali festival in April, belongs to —",
        ["Assam", "Bengal", "Odisha", "Bihar"], "Assam",
        "**Rongali (Bohag) Bihu** marks the Assamese new year and spring; the Bihu dance accompanies it.",
        "Bihu = Assam, April.", 15)
    S.q("ga-fd-p3", "medium", "The **Karma** dance, worshipping the Karma tree, is common to the tribal belts of —",
        ["Chhattisgarh and Jharkhand", "Punjab and Haryana", "Kerala and Karnataka", "Gujarat and Rajasthan"], "Chhattisgarh and Jharkhand",
        "**Karma** — an adivasi dance of the Chhattisgarh-Jharkhand (and adjoining MP) belt, danced around a sal/Karma branch.",
        "Karma = central tribal belt.", 25)
    S.q("ga-fd-p4", "easy", "Which of the following is **NOT** a folk dance of Rajasthan?",
        ["Ghoomar", "Kalbelia", "Chari", "Garba"], "Garba",
        "**Garba** is Gujarati; Ghoomar, Kalbelia and Chari are Rajasthani.",
        "Garba crosses the border — it's Gujarat's.", 15)
    S.q("ga-fd-p4", "hard", "Consider the statements:\n1. Garba was inscribed on the UNESCO ICH list in 2023.\n2. Kalbelia, Chhau and Mudiyettu were inscribed in 2010.\n3. Yakshagana is recognised as a classical dance of India.\nWhich are correct?",
        ["1 and 2 only", "1, 2 and 3", "2 and 3 only", "1 and 3 only"], "1 and 2 only",
        "**Yakshagana is a folk dance-drama** — not one of the recognised classical dances. The two ICH statements are correct.",
        "Yakshagana is folk — statement 3 fails.", 30)
    return S


def build_music():
    S = Sub("music-instruments")
    S.notes = """### Two systems of classical music
**Hindustani** (north) — Persian influence; ragas tied to the time of day; older form *dhrupad*, then *khayal*, *thumri*, *tappa*; musicians belong to **gharanas**. **Carnatic** (south) — *kriti* compositions; the **Trinity: Tyagaraja, Muthuswami Dikshitar, Syama Sastri**; **Purandara Dasa** is the 'father (Pitamaha) of Carnatic music'. **Tansen**, at Akbar's court (one of the Navaratnas), is the fountainhead of Hindustani music.

### Instruments — the four-fold classification
| Class | Meaning | Examples |
|---|---|---|
| **Tat** (stringed) | strings vibrated | sitar, veena, sarod, santoor, violin |
| **Sushir** (wind) | air column | flute (bansuri), shehnai, nadaswaram |
| **Avanaddha** (membrane) | skin struck | tabla, mridangam, pakhawaj, dholak |
| **Ghana** (solid) | struck/struck solid | ghatam, kanjira, manjira, jal tarang |

Quick sort: **shehnai = wind**, **santoor = stringed** (100 strings struck with mallets), **tabla = membranophone**, **ghatam = clay-pot idiophone**.

### Maestros ↔ instruments
| Maestro | Instrument |
|---|---|
| Ustad Bismillah Khan | Shehnai (Bharat Ratna 2001) |
| Pt. Ravi Shankar | Sitar (Bharat Ratna 1999) |
| Ustad Amjad Ali Khan / Ali Akbar Khan | Sarod |
| Ustad Zakir Hussain | Tabla |
| Pt. Shivkumar Sharma | Santoor |
| Pt. Hariprasad Chaurasia | Flute |
| Pt. Vishwa Mohan Bhatt | Mohan veena (slide guitar) |
| Ustad Allah Rakha | Tabla (Zakir's father) |
| M.S. Subbulakshmi | Carnatic vocal (first musician Bharat Ratna, 1998) |
| Pt. Bhimsen Joshi | Hindustani vocal (Kirana gharana; Bharat Ratna 2008) |
| Ustad Allauddin Khan | Sarod/raga architect — Maihar gharana; teacher of Ravi Shankar and Ali Akbar Khan |

**M.S. Subbulakshmi** (1998) was the **first musician** to get the Bharat Ratna; Ravi Shankar followed in 1999. Lata Mangeshkar (2001) and Bhimsen Joshi (2008) complete the musician Bharat Ratnas.

### Gharanas (Hindustani)
**Gwalior** is the oldest khayal gharana. Others: **Kirana** (Bhimsen Joshi's line via Abdul Karim Khan), **Jaipur-Atrauli**, **Agra**, **Patiala** (Bade Ghulam Ali Khan), **Banaras** (tabla and thumri). Tabla gharanas: Lucknow, Farrukhabad, Banaras, Punjab, Delhi. In Kathak, gharanas are Lucknow, Jaipur and Banaras.

### The violin in Carnatic music
The European violin was absorbed into Carnatic music around the 18th–19th century (credited to **Baluswami Dikshitar**, brother of Muthuswami); it is now indispensable as an accompaniment. The **nadaswaram** (wind) leads temple processions in the south, paired with the **thavil** drum.

### Quick revision
- Purandara Dasa = Carnatic Pitamaha; Trinity = Tyagaraja, Dikshitar, Syama Sastri.
- Tat-sushir-avanaddha-ghana: sitar-shehnai-tabla-ghatam.
- Bismillah Khan = shehnai (BR 2001); Ravi Shankar = sitar (BR 1999); MS 1998 = first musician BR.
- Shivkumar Sharma = santoor; Chaurasia = flute; Zakir Hussain = tabla.
- Gwalior = oldest gharana; Allauddin Khan = Maihar."""
    S.pattern("ga-mu-p1", "Instrument ↔ class", "common",
      "'Shehnai is what kind of instrument', or odd-one-out among wind/string/percussion instruments.",
      "Use the four classes: tat (stringed), sushir (wind), avanaddha (membrane drum), ghana (solid). Flute/shehnai/nadaswaram = wind; tabla/mridangam = drum; ghatam/kanjira = solid; sitar/sarod/santoor = string.",
      "The **shehnai** is classified as —",
      "A **wind (sushir) instrument** — sound from a vibrating air column.")
    S.pattern("ga-mu-p2", "Maestro ↔ instrument", "very common",
      "A musician's name (Bismillah Khan, Zakir Hussain, Shivkumar Sharma…) with four instruments.",
      "One-to-one map: Bismillah Khan-shehnai, Ravi Shankar-sitar, Amjad Ali Khan/Ali Akbar Khan-sarod, Zakir Hussain/Allah Rakha-tabla, Shivkumar Sharma-santoor, Chaurasia-flute, Vishwa Mohan Bhatt-mohan veena.",
      "Ustad **Zakir Hussain** is a virtuoso of —",
      "The **tabla** — son of the legendary Ustad Allah Rakha.")
    S.pattern("ga-mu-p3", "Hindustani vs Carnatic", "very common",
      "'Father of Carnatic music', the Carnatic Trinity, Tansen's court, or a statement-pair about the two systems.",
      "North = Hindustani (dhrupad/khayal, gharanas, Tansen); South = Carnatic (kriti, Trinity, Purandara Dasa). Any 'Pitamaha' question points to Purandara Dasa.",
      "The **Carnatic Trinity** consists of —",
      "**Tyagaraja, Muthuswami Dikshitar and Syama Sastri**.")
    S.pattern("ga-mu-p4", "Bharat Ratna musicians & gharanas", "common",
      "'First musician to get the Bharat Ratna', which gharana a singer belongs to, the oldest gharana.",
      "Order of musician Bharat Ratnas: M.S. Subbulakshmi (1998), Ravi Shankar (1999), Lata Mangeshkar (2001), Bismillah Khan (2001), Bhimsen Joshi (2008). Gwalior = oldest khayal gharana; Maihar = Allauddin Khan's school.",
      "Who was the **first musician** to be awarded the Bharat Ratna?",
      "**M.S. Subbulakshmi** (1998) — the Carnatic vocalist.")

    S.q("ga-mu-p1", "easy", "The **tabla** is classified as which type of instrument?",
        ["Membranophone (avanaddha)", "Wind (sushir)", "Stringed (tat)", "Solid (ghana)"], "Membranophone (avanaddha)",
        "The tabla produces sound from a struck skin — an **avanaddha vadya**.",
        "Struck skin = avanaddha.", 15)
    S.q("ga-mu-p1", "medium", "Which of the following is a **wind** instrument?",
        ["Nadaswaram", "Veena", "Mridangam", "Ghatam"], "Nadaswaram",
        "**Nadaswaram** — the south Indian temple wind instrument, usually paired with the thavil drum.",
        "Nadaswaram = wind (sushir).", 25)
    S.q("ga-mu-p1", "medium", "The **santoor**, once a Kashmiri folk instrument, is classed as —",
        ["A stringed (tat) instrument", "A wind instrument", "A membranophone", "A solid idiophone"], "A stringed (tat) instrument",
        "The santoor has around **100 strings** struck with light mallets — a stringed instrument taken to the concert stage by Shivkumar Sharma.",
        "100 struck strings = tat.", 25)
    S.q("ga-mu-p2", "easy", "Ustad **Amjad Ali Khan** is a maestro of the —",
        ["Sarod", "Sitar", "Shehnai", "Santoor"], "Sarod",
        "**Amjad Ali Khan** — sarod; the senia-maihar lineage of his family is famous for it.",
        "Amjad Ali = sarod.", 15)
    S.q("ga-mu-p2", "easy", "**Pt. Shivkumar Sharma**, who took a Kashmiri folk instrument to the classical stage, played the —",
        ["Santoor", "Flute", "Tabla", "Sarangi"], "Santoor",
        "**Shivkumar Sharma** = santoor; Hariprasad Chaurasia is the flute maestro of the same era.",
        "Shivkumar = santoor.", 15)
    S.q("ga-mu-p2", "medium", "**Pt. Vishwa Mohan Bhatt** won a Grammy (1994) for playing the —",
        ["Mohan veena (slide guitar)", "Veena", "Sitar", "Rudra veena"], "Mohan veena (slide guitar)",
        "His redesigned **slide guitar — the mohan veena** — won the 1994 Grammy with Ry Cooder for *A Meeting by the River*.",
        "Mohan veena = slide guitar.", 25)
    S.q("ga-mu-p2", "medium", "Ustad **Allah Rakha**, doyen of the Punjab gharana, was a master of the —",
        ["Tabla", "Sarod", "Shehnai", "Pakhawaj"], "Tabla",
        "**Allah Rakha** was the great tabla player — father and first teacher of **Zakir Hussain**.",
        "Allah Rakha = tabla (Zakir's father).", 25)
    S.q("ga-mu-p3", "easy", "Who is called the **'Pitamaha (father) of Carnatic music'**?",
        ["Purandara Dasa", "Tyagaraja", "Tansen", "Syama Sastri"], "Purandara Dasa",
        "**Purandara Dasa** systematised Carnatic teaching (sarali varisai onwards); the Trinity came after him.",
        "Purandara Dasa = Carnatic father.", 15)
    S.q("ga-mu-p3", "medium", "**Tansen**, one of the Navaratnas, adorned the court of —",
        ["Akbar", "Shah Jahan", "Krishnadeva Raya", "Sher Shah Suri"], "Akbar",
        "**Tansen** — Akbar's court musician, the fountainhead of Hindustani music and the Miyan ki Malhar raga lore.",
        "Tansen = Akbar's Navaratna.", 20)
    S.q("ga-mu-p3", "medium", "Which raga-family statement is correct about **Hindustani** music?",
        ["Ragas are traditionally tied to times of the day", "It uses only fixed kritis", "It has no gharana system", "The violin is its lead instrument"], "Ragas are traditionally tied to times of the day",
        "Hindustani ragas carry time-of-day (and seasonal) associations; fixed kriti composition is the Carnatic hallmark.",
        "Time-bound ragas = Hindustani.", 25)
    S.q("ga-mu-p4", "easy", "**Pt. Bhimsen Joshi**, Bharat Ratna 2008, was a vocalist of which gharana?",
        ["Kirana", "Gwalior", "Patiala", "Agra"], "Kirana",
        "**Bhimsen Joshi** sang in the **Kirana** gharana line; the oldest khayal gharana is Gwalior.",
        "Bhimsen Joshi = Kirana.", 15)
    S.q("ga-mu-p4", "medium", "Which is regarded as the **oldest khayal gharana** of Hindustani music?",
        ["Gwalior", "Jaipur-Atrauli", "Banaras", "Delhi"], "Gwalior",
        "**Gwalior** gharana is the oldest of the khayal gharanas; Patiala is famous for Bade Ghulam Ali Khan.",
        "Oldest = Gwalior.", 25)
    S.q("ga-mu-p4", "hard", "Arrange the musician **Bharat Ratnas** chronologically:\n1. Ravi Shankar\n2. M.S. Subbulakshmi\n3. Lata Mangeshkar\n4. Bhimsen Joshi",
        ["2, 1, 3, 4", "1, 2, 3, 4", "2, 1, 4, 3", "3, 1, 2, 4"], "2, 1, 3, 4",
        "MS (1998) → Ravi Shankar (1999) → Lata + Bismillah (2001) → Bhimsen Joshi (2008).",
        "1998-1999-2001-2008.", 30)
    return S
