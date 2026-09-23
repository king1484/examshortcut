from gacommon import Q, save_topic

S = []

# ---------------------------------------------------------------- 1. Classical dances
S.append({
"id": "classical-dances",
"title": "Classical Dances & Their Exponents",
"concept": """**Basics you must know:** The **Sangeet Natak Akademi** recognises **8 classical dances**. The Ministry of Culture also lists **Chhau** as classical, which makes 9.

| Dance | State | Signature points | Famous exponents |
|---|---|---|---|
| **Bharatanatyam** | Tamil Nadu | Oldest; temple *devadasi* roots; *Natya Shastra* based | **Rukmini Devi Arundale** (founded **Kalakshetra**, 1936), Padma Subrahmanyam, Yamini Krishnamurthy, Mrinalini Sarabhai |
| **Kathak** | Uttar Pradesh / north India | Only classical dance linked with the **Mughal courts**; *chakkars* (spins) and *tatkar* (footwork); Lucknow, Jaipur & Banaras gharanas | **Pt. Birju Maharaj**, Sitara Devi, Shovana Narayan |
| **Kathakali** | **Kerala** | Dance-drama; heavy make-up — green *pacha* for noble roles; Ramayana/Mahabharata stories | **Vallathol Narayana Menon** (founded **Kerala Kalamandalam**, 1930), Kalamandalam Gopi |
| **Mohiniyattam** | Kerala | Solo, graceful "dance of the enchantress" (Mohini) | Kalamandalam Kalyanikutty Amma, Bharati Shivaji |
| **Kuchipudi** | **Andhra Pradesh** | Named after **Kuchipudi village (Krishna district)**; **Tarangam** — dancing on the rim of a brass plate | **Vempati Chinna Satyam**, Raja & Radha Reddy |
| **Odissi** | Odisha | *Tribhanga* posture; temple sculpture roots (Konark) | **Kelucharan Mohapatra**, Sonal Mansingh, Sanjukta Panigrahi |
| **Manipuri** | Manipur | **Ras Lila** of Radha–Krishna; soft, no ankle bells | **Guru Bipin Singh**, Jhaveri sisters |
| **Sattriya** | Assam | Created by **Sankardeva** (15th–16th c.) in the sattras; recognised in **2000** | Guru Jatin Goswami |

**Chhau** (Seraikela – Jharkhand, Mayurbhanj – Odisha, Purulia – West Bengal; masks used in Seraikela & Purulia) is on UNESCO's ICH list (2010).""",
"formulas": [],
"tricks": [
 {"title": "Kerala has two, the rest one each",
  "body": "**K**erala = **K**athakali + Mohiniyattam. Every other classical dance has one home state: TN-Bharatanatyam, AP-Kuchipudi, Odisha-Odissi, Manipur-Manipuri, Assam-Sattriya, UP-Kathak.",
  "example": {"q": "Which state is home to two of the eight classical dances?", "solution": "**Kerala** — Kathakali and Mohiniyattam."}},
 {"title": "Exponent hooks",
  "body": "**B**irju = **B**ol of Kathak · **K**elucharan = Odissi (**K**onark poses) · **R**ukmini Devi = **R**evived Bharatanatyam (Kalakshetra) · **V**empati = **V**illage Kuchipudi · **V**allathol = Kerala Kalamandalam (Kathakali)."}
],
"mistakes": [
 "Kuchipudi is from **Andhra Pradesh**, not Tamil Nadu.",
 "Mohiniyattam (Kerala) ≠ Manipuri (Manipur) — both are 'M' dances.",
 "SNA lists **8** classical dances; 9 only if Chhau is counted (Ministry of Culture)."
]
})

# ---------------------------------------------------------------- 2. Folk dances
S.append({
"id": "folk-dances",
"title": "Folk Dances by State",
"concept": """| State | Folk dances (most asked in **bold**) |
|---|---|
| Gujarat | **Garba** (UNESCO ICH 2023), **Dandiya Raas**, Tippani, Padhar |
| Rajasthan | **Ghoomar**, Kalbelia, Chari, Kachchhi Ghodi, Gair |
| Punjab | **Bhangra** (men), **Giddha** (women), Jhumar |
| Haryana | Phag, Saang, Loor |
| Maharashtra | **Lavani**, Tamasha, Koli, Lezim |
| Karnataka | **Yakshagana**, **Dollu Kunitha**, Bhootha Kola |
| Kerala | **Theyyam**, Padayani, Oppana, Thiruvathirakali |
| Tamil Nadu | **Karakattam**, Kummi, Kolattam, Oyilattam |
| Andhra / Telangana | Dhimsa, Kolattam, Burrakatha, Perini Shivatandavam (Telangana) |
| Odisha | Chhau (Mayurbhanj), Dalkhai, Ghumura, Gotipua |
| West Bengal | Chhau (Purulia), Gambhira, Jatra, Baul (music) |
| Bihar | Jat-Jatin, Bidesia, Jhijhiya, Jhumar |
| Jharkhand | Chhau (Seraikela), Karma, Paika |
| Chhattisgarh | **Raut Nacha**, **Pandavani** (ballad — Teejan Bai), Gaur Maria, Karma |
| Madhya Pradesh | Jawara, Matki, Tertali |
| Uttar Pradesh | Charkula, Nautanki, Raslila |
| Uttarakhand | Chholiya, Langvir Nritya, Barada Nati |
| Himachal Pradesh | **Nati** (Kullu Nati in Guinness Records), Jhora |
| Jammu & Kashmir | **Rouf**, Dumhal, Bhand Pather |
| Assam | Bihu, **Bagurumba** (Bodo), Jhumur (tea tribes) |
| Mizoram | **Cheraw** (bamboo dance) |
| Manipur | Thang Ta (martial), Lai Haraoba |
| Meghalaya | **Nongkrem** (Khasi), **Wangala** (Garo) |
| Nagaland | Chang Lo (Sua Lua), Zeliang |
| Tripura | **Hojagiri** (balancing on a pitcher) |
| Arunachal Pradesh | Bardo Chham, Ponung |
| Sikkim | Singhi Chham (snow-lion masks) |
| Goa | Fugdi, Dekhni |""",
"formulas": [],
"tricks": [
 {"title": "North-East quick five — \"Cheraw Mizo, Hoja Tripura, Nong Khasi, Wang Garo, Bagu Bodo\"",
  "body": "**Cheraw** → Mizoram · **Hojagiri** → Tripura · **Nongkrem** → Meghalaya (Khasi) · **Wangala** → Meghalaya (Garo) · **Bagurumba** → Assam (Bodo).",
  "example": {"q": "Hojagiri, in which women balance on an earthen pitcher, is a folk dance of —", "solution": "**Tripura** (Reang community)."}},
 {"title": "Men vs women in Punjab",
  "body": "**Bh**angra = **Bh**aiya (men) · **G**iddha = **G**irls (women)."}
],
"mistakes": [
 "Yakshagana is from **Karnataka**, not Kerala.",
 "Chhau belongs to three states (Jharkhand, Odisha, West Bengal); Purulia is in West Bengal.",
 "Garba = Gujarat; Ghoomar = Rajasthan — both are circle dances, do not swap."
]
})

# ---------------------------------------------------------------- 3. Music
S.append({
"id": "music-instruments",
"title": "Music, Instruments & Maestros",
"concept": """**Two systems:** **Hindustani** (north; Persian influence; ragas tied to time of day; forms — *dhrupad* (oldest), *khayal*, *thumri*, *tappa*) and **Carnatic** (south; *kriti* composition; fixed compositions).

**Carnatic essentials**
- **Purandara Dasa** = "father (Pitamaha) of Carnatic music".
- **Trinity of Carnatic music:** **Tyagaraja**, **Muthuswami Dikshitar**, **Syama Sastri** (all 18th–19th c., Thiruvarur region, TN).
- **Tyagaraja Aradhana** festival is held at **Thiruvaiyaru**.

**Instrument → maestro**

| Instrument | Type | Maestro(s) |
|---|---|---|
| **Sitar** | String | **Pt. Ravi Shankar** (Bharat Ratna 1999), Vilayat Khan, Anoushka Shankar |
| Sarod | String | Ali Akbar Khan, Amjad Ali Khan |
| **Shehnai** | Wind | **Ustad Bismillah Khan** (Bharat Ratna 2001) |
| **Tabla** | Drum | **Zakir Hussain**, Alla Rakha, Kishan Maharaj |
| **Bansuri (flute)** | Wind | **Pt. Hariprasad Chaurasia**, Pannalal Ghosh |
| Santoor | String (struck) | Shivkumar Sharma, Rahul Sharma |
| Sarangi | Bowed string | **Pt. Ram Narayan**, Sabri Khan |
| Violin (Carnatic) | Bowed | Lalgudi Jayaraman, L. Subramaniam, N. Rajam (Hindustani) |
| Mandolin | String | U. Srinivas |
| Mridangam | Drum | Palghat Mani Iyer, Umayalpuram Sivaraman |
| Veena (Saraswati) | String | E. Gayathri, S. Balachander |

**Vocalists who won the Bharat Ratna:** **M.S. Subbulakshmi (1998, first musician)**, Pt. Ravi Shankar (1999, sitar), Lata Mangeshkar (2001), Bismillah Khan (2001), **Pt. Bhimsen Joshi (2009, Kirana gharana)**, Bhupen Hazarika (2019, posthumous).

**Classical instrument families (Natya Shastra):** *Tata* (string) · *Sushira* (wind) · *Avanaddha* (membrane/drum) · *Ghana* (solid — cymbals, ghatam).""",
"formulas": [],
"tricks": [
 {"title": "Carnatic Trinity — \"Tea, Milk, Sugar\"",
  "body": "**T**yagaraja · **M**uthuswami Dikshitar · **S**yama Sastri. **Purandara Dasa** is the *father*, not part of the trinity.",
  "example": {"q": "Who is called the Pitamaha of Carnatic music?", "solution": "**Purandara Dasa** — father, not one of the trinity."}},
 {"title": "Instrument families — \"Tata Sings, Avan Drums, Ghana Clangs\"",
  "body": "Tata = strings, Sushira = air (wind), Avanaddha = skin drums, Ghana = solid (bells, cymbals, ghatam)."}
],
"mistakes": [
 "Sarod ≠ sitar: Ravi Shankar = **sitar**; Ali Akbar Khan & Amjad Ali Khan = **sarod**.",
 "First musician to receive the Bharat Ratna = **M.S. Subbulakshmi (1998)**, not Lata Mangeshkar (2001).",
 "Hariprasad Chaurasia plays the **flute**; Shivkumar Sharma played the **santoor**."
]
})

# ---------------------------------------------------------------- 4. Paintings & crafts
S.append({
"id": "paintings-crafts",
"title": "Paintings, Textiles & Handicrafts",
"concept": """**Folk & tribal painting → state**

| Painting | State | Hallmark |
|---|---|---|
| **Madhubani (Mithila)** | **Bihar** | Women's art; double-line borders, natural colours; GI tag |
| Warli | Maharashtra | White figures on mud walls |
| **Pattachitra** | **Odisha** (also West Bengal) | Cloth scroll; Jagannath themes |
| **Kalamkari** | **Andhra Pradesh** | "Pen-work" on cloth — Srikalahasti (hand-drawn) & Machilipatnam (block) |
| **Gond** | Madhya Pradesh | Dots & lines; Jangarh Singh Shyam |
| Pithora | Gujarat / MP | Rathwa & Bhil ritual walls |
| **Phad** | **Rajasthan** | Scroll of folk deities Pabuji & Devnarayan |
| Kalighat | West Bengal | 19th-c. Kolkata bazaar painting |
| **Tanjore (Thanjavur)** | **Tamil Nadu** | Gold foil, gems |
| Mysore | Karnataka | Gesso work, gold |
| Cheriyal scroll | Telangana | Narrative scrolls |
| Saura | Odisha | Tribal wall art (*idital*) |
| Thangka | Sikkim, Ladakh, Arunachal | Buddhist scroll painting |

**Miniature schools:** Mughal (Akbar's atelier — Mir Sayyid Ali, Abdus Samad) · Rajasthani (**Kishangarh — "Bani Thani"**, Mewar, Bundi) · Pahari (**Kangra**, Basohli).

**Textile / craft → place**

| Craft | Place |
|---|---|
| **Bidriware** (silver inlay on blackened metal) | **Bidar, Karnataka** |
| Chikankari (embroidery) | Lucknow, UP |
| Phulkari (embroidery) | Punjab |
| Kantha (running stitch) | West Bengal |
| Bandhani / Bandhej (tie-dye) | Gujarat & Rajasthan |
| **Patola** (double ikat silk) | **Patan, Gujarat** |
| Pochampally ikat | Telangana |
| Kanjeevaram silk | Kanchipuram, Tamil Nadu |
| Banarasi brocade | Varanasi, UP |
| Chanderi & Maheshwari | Madhya Pradesh |
| Paithani | Maharashtra |
| **Muga silk** (golden) | **Assam** |
| Pashmina | Jammu & Kashmir |
| Blue pottery | Jaipur, Rajasthan |""",
"formulas": [],
"tricks": [
 {"title": "\"Kalam in Andhra, Patta in Odisha, Phad in Rajasthan\"",
  "body": "**Kalam**kari → **A**ndhra (the pen = *kalam*) · **Patta**chitra → **O**disha (cloth = *patta*) · **Phad** → **R**ajasthan (Pabuji scroll). Madhubani → Bihar's Mithila.",
  "example": {"q": "Kalamkari art is chiefly associated with —", "solution": "**Andhra Pradesh** (Srikalahasti & Machilipatnam)."}},
 {"title": "Bidri = Bidar",
  "body": "The craft is named after its town — **Bidri**ware from **Bidar** (Karnataka). Same trick: **Patola** from **Patan**, **Chanderi** from Chanderi."}
],
"mistakes": [
 "Madhubani = **Bihar**, not Odisha; Pattachitra = **Odisha**.",
 "Patola is from **Gujarat**; Paithani is from **Maharashtra** — similar sounding, different states.",
 "Muga silk (golden) is unique to **Assam**."
]
})

# ---------------------------------------------------------------- 5. Architecture
S.append({
"id": "architecture",
"title": "Temple & Rock-cut Architecture",
"concept": """**Three temple styles**

| Style | Region | Hallmarks | Examples |
|---|---|---|---|
| **Nagara** | North India | Curvilinear **shikhara** over the sanctum; no boundary wall; *amalaka* on top | Khajuraho (Chandela), Lingaraja (Bhubaneswar), Konark, Modhera Sun Temple |
| **Dravida** | South India | Pyramidal **vimana**; huge **gopuram** gateways; enclosure wall; temple tank | Brihadeeswara (Thanjavur), Meenakshi (Madurai), Mahabalipuram |
| **Vesara** | Deccan (Karnataka) | Mix of Nagara & Dravida; star-shaped plans | **Hoysala** temples of Belur, Halebidu, Somnathapura; later Chalukya temples |

**Odisha temples:** **Konark Sun Temple** — **Narasimhadeva I (Eastern Ganga)**, 13th c., chariot with 24 wheels, "Black Pagoda", UNESCO 1984. **Jagannath Temple, Puri** — Anantavarman Chodaganga, "White Pagoda". Lingaraja, Bhubaneswar.

**Rock-cut & cave sites**

| Site | State | Faith / feature |
|---|---|---|
| **Bhimbetka** | Madhya Pradesh | **Prehistoric rock shelters & paintings** (UNESCO 2003) |
| **Ajanta** | Maharashtra | **Buddhist**; 29–30 caves; famous **murals** (Padmapani) |
| **Ellora** | Maharashtra | 34 caves — **Buddhist, Hindu and Jain** |
| Elephanta | Maharashtra (Mumbai harbour) | Shaiva; **Trimurti (Maheshmurti)** sculpture |
| Udayagiri–Khandagiri | Odisha | Jain caves (Kharavela) |
| Barabar | Bihar | Oldest rock-cut caves (Mauryan, Ajivikas) |

**Colonial / Indo-Saracenic:** Victoria Memorial (Kolkata), Gateway of India (Mumbai, 1924), Chhatrapati Shivaji Maharaj Terminus (UNESCO 2004, Gothic-Revival).""",
"formulas": [],
"tricks": [
 {"title": "\"Shikhara North, Gopuram South, Vesara in Between\"",
  "body": "See a **gopuram** → Dravida. See a **curved shikhara** → Nagara. A star-shaped Hoysala plan → Vesara (Deccan).",
  "example": {"q": "The towering gateway called 'gopuram' is a feature of which style?", "solution": "**Dravida** (south Indian) style."}},
 {"title": "Odisha pagodas",
  "body": "**Black** Pagoda = Konark (dark stone, Sun temple) · **White** Pagoda = Puri (whitewashed Jagannath)."}
],
"mistakes": [
 "Ellora has caves of **three** faiths; Ajanta is **only Buddhist**.",
 "Konark was built by **Narasimhadeva I**; Puri's Jagannath temple by **Anantavarman Chodaganga**.",
 "Hoysala temples are **Vesara**, not Dravida."
]
})

# ---------------------------------------------------------------- 6. Festivals & fairs
S.append({
"id": "festivals-fairs",
"title": "Festivals & Fairs",
"concept": """| Festival / fair | State | Note |
|---|---|---|
| **Onam** | Kerala | Harvest; King Mahabali; Vallam Kali (snake-boat race) |
| **Pongal** | Tamil Nadu | Harvest, mid-January; Jallikattu |
| Makar Sankranti / Lohri | Many / Punjab | Lohri the night before Sankranti |
| Baisakhi | Punjab | Harvest & Khalsa foundation (1699) |
| **Hornbill Festival** | **Nagaland** | **1–10 December**, Kisama Heritage Village — "festival of festivals" |
| Sangai Festival | Manipur | Named after the brow-antlered deer |
| Chapchar Kut | Mizoram | Spring, after jhum clearing |
| Wangala | Meghalaya | Garo harvest ("100 drums") |
| Losar | Ladakh, Sikkim, Arunachal | Tibetan New Year |
| **Hemis** | Ladakh | Birth of Guru Padmasambhava; masked Cham dance |
| Ugadi | Andhra, Telangana, Karnataka | New Year |
| Gudi Padwa | Maharashtra | New Year |
| **Bonalu, Bathukamma** | **Telangana** | Mahakali / floral festival |
| Nuakhai | Odisha | New rice |
| **Chhath** | Bihar | Sun worship, fasting at riverbanks |
| Thrissur Pooram | Kerala | Elephant pageant |
| Hareli | Chhattisgarh | First festival of the farming year |
| Kharchi Puja | Tripura | Fourteen deities |
| Moatsu / Sekrenyi | Nagaland | Ao / Angami festivals |

**Fairs:** **Pushkar Fair** (Rajasthan, camel fair, Kartik Purnima) · **Sonepur Mela** (**Bihar**, Gandak–Ganga confluence — among Asia's largest cattle fairs) · **Kumbh Mela** (Prayagraj, Haridwar, Ujjain, Nashik; UNESCO ICH 2017) · **Ambubachi Mela** (Kamakhya, Assam) · **Rath Yatra** (Puri) · Suraj Kund Crafts Mela (Haryana).""",
"formulas": [],
"tricks": [
 {"title": "Nagaland December — \"Hornbill closes the year\"",
  "body": "**Hornbill** Festival runs **1–10 December** (Nagaland Statehood Day is 1 December).",
  "example": {"q": "The Hornbill Festival is held every year in —", "solution": "**Nagaland**, 1–10 December."}},
 {"title": "Two cattle fairs",
  "body": "**P**ushkar = **P**ink city state (Rajasthan) camels; **S**onepur = **S**aran/Bihar cattle & elephants."}
],
"mistakes": [
 "Bonalu and Bathukamma are **Telangana** festivals, not Andhra Pradesh.",
 "Sonepur Mela is in **Bihar**; Pushkar is in **Rajasthan**.",
 "Hemis is a **Ladakh** monastery festival; Losar is the Tibetan New Year."
]
})

# ---------------------------------------------------------------- 7. UNESCO & institutions
S.append({
"id": "unesco-institutions",
"title": "UNESCO Heritage & Cultural Institutions",
"concept": """**India's UNESCO World Heritage Sites — 45 (as of Sept 2026)** = 37 cultural + 7 natural + 1 mixed (**Khangchendzonga NP**, Sikkim).

| No. | Recent inscription | Year |
|---|---|---|
| 39 | Ramappa (Rudreswara) Temple, Telangana | 2021 |
| 40 | Dholavira, Gujarat | 2021 |
| 41 | **Santiniketan**, West Bengal | 2023 |
| 42 | **Sacred Ensembles of the Hoysalas** (Belur, Halebidu, Somnathapura), Karnataka | 2023 |
| 43 | **Moidams of Charaideo** (Ahom mound burials), Assam | 2024 |
| 44 | Maratha Military Landscapes (12 forts) | 2025 |
| 45 | Ancient Buddhist Site of **Sarnath**, UP | 2026 |

**Intangible Cultural Heritage (ICH) — 16 Indian elements**

| Year | Elements |
|---|---|
| 2008 | **Koodiyattam** (Sanskrit theatre, Kerala), Ramlila, Vedic chanting |
| 2009 | **Ramman** (religious festival, Garhwal, Uttarakhand) |
| 2010 | Mudiyettu (Kerala), Kalbelia (Rajasthan), Chhau |
| 2012 | Buddhist chanting of Ladakh |
| 2013 | Sankirtana of Manipur |
| 2014 | Brass & copper craft of the Thatheras of Jandiala Guru (Punjab) |
| 2016 | **Yoga**; Nowruz (multinational) |
| 2017 | **Kumbh Mela** |
| 2021 | **Durga Puja in Kolkata** |
| 2023 | **Garba of Gujarat** |
| 2025 | **Deepavali** (16th) |

**Cultural institutions**

| Body | Set up | Note |
|---|---|---|
| Archaeological Survey of India | 1861 | **Alexander Cunningham** first DG |
| **Sangeet Natak Akademi** | 1952 | Music, dance, drama |
| **Sahitya Akademi** | 1954 | Literature; awards in 24 languages |
| **Lalit Kala Akademi** | 1954 | Visual arts |
| National School of Drama | 1959 | New Delhi |
| Kalakshetra | 1936 | Rukmini Devi Arundale, Chennai |
| Kerala Kalamandalam | 1930 | Vallathol Narayana Menon |""",
"formulas": [],
"tricks": [
 {"title": "WHS count ladder",
  "body": "Remember the last few by year: **2021 → 40** (Dholavira), **2023 → 42** (Hoysala), **2024 → 43** (Moidams), **2025 → 44** (Maratha forts), **2026 → 45** (Sarnath).",
  "example": {"q": "The Moidams of Charaideo belong to which state?", "solution": "**Assam** — royal mound burials of the Ahom dynasty (2024)."}},
 {"title": "Three Akademis — \"Sangeet first, then Sahitya & Lalit together\"",
  "body": "**SNA 1952**, then **Sahitya** and **Lalit Kala** both in **1954**."}
],
"mistakes": [
 "The only **mixed** WHS in India is **Khangchendzonga** (Sikkim).",
 "Yoga is an **intangible** heritage element, not a World Heritage Site.",
 "Ramman is from **Uttarakhand**, Mudiyettu from **Kerala**."
]
})

# ---------------------------------------------------------------- PYQ patterns
P = [
 {"pattern": "Dance ↔ state", "frequency": "very common",
  "howToSpot": "A classical or folk dance named with four states as options (or \"which pair is correctly matched\").",
  "approach": "Classical: 'Kerala has two'. Folk: use the state table; NE dances with the Cheraw–Hojagiri–Nongkrem mnemonic."},
 {"pattern": "Artist ↔ instrument / dance", "frequency": "very common",
  "howToSpot": "A Padma/Bharat Ratna maestro's name with instruments or dance forms as options.",
  "approach": "Memorise the instrument–maestro table; watch sitar/sarod and flute/santoor swaps."},
 {"pattern": "Painting / craft ↔ state", "frequency": "common",
  "howToSpot": "Madhubani, Kalamkari, Pattachitra, Phad, Bidri, Patola…",
  "approach": "Place-name crafts (Bidri–Bidar, Patola–Patan); painting hooks (Kalam–Andhra, Patta–Odisha)."},
 {"pattern": "Festival / fair ↔ state", "frequency": "common",
  "howToSpot": "Regional festival name + states.",
  "approach": "Group by region; NE festivals and Telangana's Bonalu/Bathukamma are frequent traps."},
 {"pattern": "UNESCO list / temple builder", "frequency": "occasional",
  "howToSpot": "\"inscribed on UNESCO list\", \"built by\", temple style questions.",
  "approach": "Know the last five WHS by year, the 16 ICH elements and the Nagara–Dravida–Vesara features."},
]

# ---------------------------------------------------------------- solved examples
SE = [
 Q("art-ex01", "Which of the following classical dance–state pairs is **NOT** correctly matched?",
   ["Mohiniyattam — Kerala", "Manipuri — Manipur", "Odissi — Odisha", "Kuchipudi — Tamil Nadu"], 3,
   "**Kuchipudi** is from **Andhra Pradesh** (Kuchipudi village, Krishna district). Tamil Nadu's classical dance is Bharatanatyam. The other three pairs are correct.",
   "Only Kerala has two classical dances; Tamil Nadu has just one (Bharatanatyam), so the Kuchipudi pair must be wrong.",
   "easy", "classical-dances", "Dance ↔ state (odd pair)", 20),
 Q("art-ex02", "**Pandit Hariprasad Chaurasia** is renowned as a player of the —",
   ["Bansuri (flute)", "Sitar", "Sarangi", "Tabla"], 0,
   "**Hariprasad Chaurasia** is India's best-known **bansuri** (bamboo flute) player (Padma Vibhushan 2000). Sitar – Ravi Shankar; sarangi – Ram Narayan; tabla – Zakir Hussain.",
   "Chaurasia's 'Call of the Valley' pairs **flute** with Shivkumar Sharma's santoor.",
   "easy", "music-instruments", "Artist ↔ instrument", 20),
 Q("art-ex03", "Which of the following is **NOT** on UNESCO's list of India's Intangible Cultural Heritage?",
   ["Yoga", "Kumbh Mela", "Garba of Gujarat", "Onam"], 3,
   "Yoga (2016), Kumbh Mela (2017) and Garba (2023) are inscribed. **Onam** is not on the list (India's festival entries are Ramman, Kumbh Mela, Durga Puja and Deepavali).",
   "Recall the 2016–2025 run: Yoga, Kumbh, Durga Puja, Garba, Deepavali — Onam is missing.",
   "medium", "unesco-institutions", "UNESCO list — odd one out", 30),
 Q("art-ex04", "The Ellora caves in Maharashtra contain rock-cut shrines of which religious traditions?",
   ["Buddhist only", "Hindu and Jain only", "Buddhist, Hindu and Jain", "Buddhist and Hindu only"], 2,
   "Ellora's **34 caves** (c. 6th–10th century) include 12 Buddhist, 17 Hindu (including the Kailasa temple, Cave 16) and 5 Jain caves. Ajanta, by contrast, is purely Buddhist.",
   "Ellora = **E**veryone (three faiths); **A**janta = **A**ll Buddhist.",
   "medium", "architecture", "Cave ↔ religion", 25),
]

# ---------------------------------------------------------------- practice
PR = [
 Q("art-q01", "**Kathakali**, the dance-drama known for its elaborate green face make-up, is a classical dance of —",
   ["Kerala", "Karnataka", "Tamil Nadu", "Andhra Pradesh"], 0,
   "**Kathakali** is from **Kerala**; the poet Vallathol founded Kerala Kalamandalam (1930) to revive it. Karnataka's comparable dance-drama is Yakshagana (a folk form).",
   "**K**athakali = **K**erala.", "easy", "classical-dances", "Dance ↔ state", 15),
 Q("art-q02", "The classical dance **Kuchipudi** takes its name from a village in which state?",
   ["Tamil Nadu", "Andhra Pradesh", "Odisha", "Karnataka"], 1,
   "Kuchipudi village is in the **Krishna district of Andhra Pradesh**. The dance is known for *Tarangam*, performed on the rim of a brass plate.",
   "**V**empati – **V**illage Kuchipudi – Andhra.", "easy", "classical-dances", "Dance ↔ state", 15),
 Q("art-q03", "**Pandit Birju Maharaj** was a celebrated exponent of —",
   ["Odissi", "Bharatanatyam", "Kathak", "Manipuri"], 2,
   "**Birju Maharaj** (1938–2022) of the **Lucknow (Kalka-Bindadin) gharana** was the leading figure of **Kathak** and received the Padma Vibhushan.",
   "**B**irju = **B**ol and chakkar of Kathak.", "easy", "classical-dances", "Artist ↔ dance", 15),
 Q("art-q04", "**Guru Kelucharan Mohapatra** is associated with the revival of which dance?",
   ["Kuchipudi", "Mohiniyattam", "Sattriya", "Odissi"], 3,
   "**Kelucharan Mohapatra** (1926–2004) shaped modern **Odissi**; he was the first Odia to receive the Padma Vibhushan.",
   "**K**elucharan – **K**onark poses – Odissi.", "easy", "classical-dances", "Artist ↔ dance", 15),
 Q("art-q05", "**Garba**, inscribed on UNESCO's Intangible Cultural Heritage list in 2023, is a dance form of —",
   ["Gujarat", "Rajasthan", "Maharashtra", "Madhya Pradesh"], 0,
   "**Garba of Gujarat** is performed around a lamp (*garbo*) during Navratri. It became India's 15th ICH element in December 2023.",
   "**G**arba = **G**ujarat.", "easy", "folk-dances", "Dance ↔ state", 15),
 Q("art-q06", "**Cheraw**, the bamboo dance in which dancers step in and out of clapping bamboo poles, belongs to —",
   ["Nagaland", "Mizoram", "Manipur", "Tripura"], 1,
   "**Cheraw** is the traditional bamboo dance of **Mizoram**, often performed at Chapchar Kut. Tripura's well-known dance is Hojagiri.",
   "NE five: **Cheraw Mizo**, Hoja Tripura, Nong Khasi, Wang Garo, Bagu Bodo.", "medium", "folk-dances", "Dance ↔ state", 20),
 Q("art-q07", "Which of the following is **NOT** one of the 'Trinity' of Carnatic music?",
   ["Tyagaraja", "Muthuswami Dikshitar", "Purandara Dasa", "Syama Sastri"], 2,
   "The Trinity is **Tyagaraja, Muthuswami Dikshitar and Syama Sastri**. **Purandara Dasa** (16th century) is honoured as the *Pitamaha* (father) of Carnatic music.",
   "Tea, Milk, Sugar = T, M, S — no 'P'.", "medium", "music-instruments", "Group — odd one out", 20),
 Q("art-q08", "**Ustad Bismillah Khan**, awarded the Bharat Ratna in 2001, was a maestro of the —",
   ["Sitar", "Sarod", "Tabla", "Shehnai"], 3,
   "**Bismillah Khan** of Varanasi took the **shehnai** from wedding music to the concert stage and played it at the Red Fort on 15 August 1947.",
   "Shehnai = wind instrument of Varanasi ghats = Bismillah.", "easy", "music-instruments", "Artist ↔ instrument", 15),
 Q("art-q09", "Who was the first musician to be awarded the **Bharat Ratna**?",
   ["M.S. Subbulakshmi", "Lata Mangeshkar", "Pandit Ravi Shankar", "Pandit Bhimsen Joshi"], 0,
   "Carnatic vocalist **M.S. Subbulakshmi** received the Bharat Ratna in **1998**. Ravi Shankar followed in 1999, Lata Mangeshkar in 2001 and Bhimsen Joshi in 2009.",
   "Order: **M**S (98) → Ravi (99) → Lata & Bismillah (01) → Bhimsen (09).", "medium", "music-instruments", "First to …", 20),
 Q("art-q10", "**Madhubani** painting, traditionally drawn by women of the Mithila region, belongs to —",
   ["Odisha", "Bihar", "West Bengal", "Jharkhand"], 1,
   "Madhubani (Mithila) painting is from **Bihar**, marked by double-line borders and natural colours. It has a GI tag. Odisha's scroll art is Pattachitra.",
   "Mithila → Madhubani district → Bihar.", "easy", "paintings-crafts", "Painting ↔ state", 15),
 Q("art-q11", "**Kalamkari**, the art of hand-painting or block-printing cotton textiles with natural dyes, is chiefly associated with —",
   ["Rajasthan", "Gujarat", "Andhra Pradesh", "Karnataka"], 2,
   "Kalamkari ('pen-work') is practised at **Srikalahasti** (free-hand) and **Machilipatnam** (block-printed) in **Andhra Pradesh**.",
   "**Kalam** in **A**ndhra.", "medium", "paintings-crafts", "Craft ↔ state", 20),
 Q("art-q12", "**Bidriware**, a metal craft with silver inlay on a blackened alloy, originated in —",
   ["Moradabad", "Jaipur", "Kutch", "Bidar"], 3,
   "Bidri work takes its name from **Bidar in Karnataka**, where it developed under the Bahmani sultans. Moradabad is known for brassware.",
   "The craft carries its town's name: **Bidri** → **Bidar**.", "easy", "paintings-crafts", "Craft ↔ place", 15),
 Q("art-q13", "The **Sun Temple at Konark** was built by —",
   ["Narasimhadeva I", "Anantavarman Chodaganga", "Rajaraja I", "Kharavela"], 0,
   "The Eastern Ganga king **Narasimhadeva I** built Konark in the 13th century as a giant chariot of the Sun god with 24 wheels. Anantavarman Chodaganga built the Jagannath temple at Puri; Kharavela is linked with the Hathigumpha inscription.",
   "Konark = **N**arasimha (the **N**-for-**N**ew Sun chariot); Puri = Anantavarman.", "medium", "architecture", "Monument ↔ builder", 25),
 Q("art-q14", "Towering gateways called **gopurams** are a characteristic feature of which temple style?",
   ["Nagara", "Dravida", "Vesara", "Indo-Saracenic"], 1,
   "In the **Dravida** style the sanctum is topped by a pyramidal **vimana**, and later temples have huge **gopurams** in the enclosure walls (e.g. Meenakshi temple, Madurai). Nagara temples have a curved shikhara and no gopuram.",
   "Gopuram → South → Dravida.", "easy", "architecture", "Style ↔ feature", 15),
 Q("art-q15", "The **Hornbill Festival**, called the 'festival of festivals', is held every December in —",
   ["Assam", "Arunachal Pradesh", "Nagaland", "Meghalaya"], 2,
   "The Hornbill Festival is held from **1 to 10 December** at Kisama Heritage Village near Kohima, **Nagaland**, showcasing all Naga tribes.",
   "Hornbill = Naga headgear feathers = Nagaland.", "easy", "festivals-fairs", "Festival ↔ state", 15),
 Q("art-q16", "The **Sonepur Mela**, one of Asia's largest cattle fairs, is held at the confluence of the Gandak and the Ganga in —",
   ["Rajasthan", "Uttar Pradesh", "West Bengal", "Bihar"], 3,
   "Sonepur (Saran district, **Bihar**) hosts the fair from Kartik Purnima. Rajasthan's famous camel fair is at Pushkar.",
   "**S**onepur = **S**aran, Bihar; **P**ushkar = Rajasthan.", "easy", "festivals-fairs", "Fair ↔ state", 15),
 Q("art-q17", "**Ramman**, a religious festival and ritual theatre inscribed on UNESCO's Intangible Cultural Heritage list in 2009, is performed in —",
   ["Himachal Pradesh", "Uttarakhand", "Sikkim", "Jammu & Kashmir"], 1,
   "Ramman is performed in the Saloor-Dungra villages of **Chamoli district (Garhwal), Uttarakhand**, in honour of the local deity Bhumiyal Devta.",
   "Ramman – Garhwal – Uttarakhand (2009, right after the 2008 first batch).", "hard", "unesco-institutions", "UNESCO element ↔ state", 20),
 Q("art-q18", "The **Sacred Ensembles of the Hoysalas**, inscribed as a UNESCO World Heritage Site in 2023, are located in —",
   ["Tamil Nadu", "Andhra Pradesh", "Karnataka", "Kerala"], 2,
   "The ensemble covers the Hoysala temples at **Belur, Halebidu and Somnathapura** in **Karnataka**. It became India's 42nd World Heritage Site.",
   "Hoysala = Vesara = Karnataka.", "medium", "unesco-institutions", "WHS ↔ state", 20),
]

topic = {
 "id": "art-culture",
 "sectionId": "ga",
 "title": "Art & Culture",
 "order": 4,
 "importance": "medium",
 "avgQuestions": {"tier1": 1, "tier2": 1},
 "summary": "Classical and folk dances, music and maestros, paintings and crafts, temple architecture, festivals and fairs, and India's UNESCO lists. SSC asks 1–2 culture questions in almost every shift. Nearly all are pairings: dance–state, artist–instrument, craft–state or festival–state. The tables below cover almost all of them.",
 "subtopics": S,
 "pyqPatterns": P,
 "solvedExamples": SE,
 "practice": PR,
}

if __name__ == "__main__":
    save_topic(topic)
