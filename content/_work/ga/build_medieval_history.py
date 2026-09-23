from gacommon import Q, save_topic

S = []

# ---------------------------------------------------------------- 1. Early medieval
S.append({
"id": "early-medieval",
"title": "Early Medieval India (c. 750–1206)",
"concept": """**Basics you must know**

| Point | Fact |
|---|---|
| Tripartite struggle | 8th–10th century fight for **Kannauj** between the **Palas** (Bengal), **Gurjara-Pratiharas** (western India) and **Rashtrakutas** (Deccan) |
| Palas | Founded by **Gopala** (c. 750, "elected" by chiefs); **Dharmapala** revived **Nalanda** and founded **Vikramashila** university |
| Gurjara-Pratiharas | **Nagabhata I** checked Arab advance; **Mihira Bhoja** (Adivaraha coins) is the best-known ruler |
| Rashtrakutas | Founder **Dantidurga**; capital **Manyakheta**; **Amoghavarsha I** wrote *Kavirajamarga* (Kannada) |
| Arab conquest of Sindh | **Muhammad bin Qasim**, **712 CE**, defeated **Raja Dahir** |
| Mahmud of Ghazni | **17 raids** (1000–1027); sacked **Somnath** temple (1025); scholar **Al-Biruni** came with him and wrote *Kitab-ul-Hind* |
| Muhammad Ghori | **First Battle of Tarain 1191** – lost to **Prithviraj Chauhan**; **Second Battle of Tarain 1192** – won; **Chandawar 1194** – defeated **Jaichand** (Gahadavala, Kannauj) |
| Kashmir chronicle | **Kalhana's *Rajatarangini*** (12th c.) — first proper historical work in Sanskrit |
| Chand Bardai | Court poet of Prithviraj; *Prithviraj Raso* |

**Rajput dynasties (quick map)**

| Dynasty | Region | Remember for |
|---|---|---|
| Chauhans (Chahamanas) | Ajmer–Delhi | Prithviraj III |
| Gahadavalas | Kannauj–Varanasi | Jaichand |
| Paramaras | Malwa (Dhar) | **Raja Bhoja** — scholar-king, Bhojpur |
| Chandelas | Bundelkhand | **Khajuraho** temples |
| Solankis (Chalukyas of Gujarat) | Gujarat | Dilwara (Mt Abu) & Modhera Sun temple era |
| Tomaras | Delhi region | Founded **Dhillika** (Delhi) |""",
"formulas": [],
"tricks": [
 {"title": "Tripartite = \"PPR fight for K\"",
  "body": "**P**ala, **P**ratihara, **R**ashtrakuta → **K**annauj. East, West and South all wanted the centre.",
  "example": {"q": "Which of these dynasties was NOT part of the tripartite struggle — Pala, Pratihara, Chola, Rashtrakuta?", "solution": "**Chola** — the three were Pala, Pratihara and Rashtrakuta."}},
 {"title": "Tarain: 1 to Prithviraj, 2 to Ghori",
  "body": "**1191 → 1st** battle → Prithviraj wins. **1192 → 2nd** battle → Ghori wins. The second number always goes to the invader."}
],
"mistakes": [
 "Somnath was raided by **Mahmud of Ghazni** (1025), not Muhammad Ghori.",
 "Al-Biruni came with **Mahmud of Ghazni**; Ibn Battuta came under **Muhammad bin Tughlaq**.",
 "Arab conquest of Sindh (712) was by **Muhammad bin Qasim**, not Mahmud."
]
})

# ---------------------------------------------------------------- 2. Delhi Sultanate
S.append({
"id": "delhi-sultanate",
"title": "Delhi Sultanate (1206–1526)",
"concept": """**Five dynasties in order**

| Dynasty | Years | Founder |
|---|---|---|
| Mamluk / Slave (Ilbari) | 1206–1290 | **Qutb-ud-din Aibak** |
| Khalji | 1290–1320 | **Jalal-ud-din Khalji** |
| Tughlaq | 1320–1414 | **Ghiyas-ud-din Tughlaq** |
| Sayyid | 1414–1451 | Khizr Khan |
| Lodi (only Afghan dynasty) | 1451–1526 | **Bahlol Lodi** |

**Ruler → signature fact (most asked)**

| Ruler | What SSC asks |
|---|---|
| **Qutb-ud-din Aibak** | "Lakh Baksh" (generous giver); began **Qutub Minar**; Quwwat-ul-Islam mosque (Delhi) & Adhai Din ka Jhonpra (Ajmer); died falling from horse playing **chaugan (polo)** 1210; capital **Lahore** |
| **Iltutmish** | Real consolidator; shifted capital to **Delhi**; **iqta** system; **Turkan-i-Chahalgani** (Group of Forty); pure Arabic coins — silver **tanka** & copper **jital**; completed Qutub Minar; investiture from Abbasid Caliph (1229) |
| **Razia Sultan** | First and only woman ruler of Delhi (1236–40); daughter of Iltutmish |
| **Balban** | "Blood and iron" policy; **sijda** (prostration) and **paibos** (kissing feet); Persian festival **Nauroz**; created **Diwan-i-Arz** (military dept); crushed the Chahalgani |
| **Alauddin Khalji** | **Market control** (Shahna-i-Mandi, price fixing); **dagh** (branding horses) & **chehra** (descriptive roll of soldiers); standing army paid in cash; land revenue **50%**; **Alai Darwaza** (1311), Siri Fort; general **Malik Kafur** raided the south |
| **Ghiyas-ud-din Tughlaq** | Built **Tughlaqabad**; died when a pavilion collapsed (1325) |
| **Muhammad bin Tughlaq** | Capital to **Daulatabad (Devagiri) 1327**; **token currency** in bronze/copper (1329–30); **Diwan-i-Amir-Kohi** (agriculture dept); Moroccan traveller **Ibn Battuta** was his qazi of Delhi |
| **Firoz Shah Tughlaq** | Canals (Yamuna, Sutlej); **Diwan-i-Khairat** (charity), **Diwan-i-Bandagan** (slaves); jizya extended to Brahmins; founded Firozabad, Hisar, Jaunpur; brought **Ashokan pillars** from Topra and Meerut to Delhi |
| Timur's invasion | **1398**, under Nasir-ud-din Mahmud Tughlaq |
| **Sikandar Lodi** | Founded **Agra (1504)**; **Gaz-i-Sikandari** (measuring yard); pen-name *Gulrukhi* |
| **Ibrahim Lodi** | Last Sultan; killed at **First Battle of Panipat, 1526** |

**Historians of the Sultanate:** Minhaj-us-Siraj – *Tabaqat-i-Nasiri*; **Ziauddin Barani** – *Tarikh-i-Firoz Shahi*, *Fatawa-i-Jahandari*; Amir Khusrau – *Khazain-ul-Futuh*, *Tughlaqnama*.""",
"formulas": [],
"tricks": [
 {"title": "Dynasty order — \"Sabka Khana Tum Sab Lo\"",
  "body": "**S**lave → **K**halji → **T**ughlaq → **S**ayyid → **L**odi. Starting years **1206 – 1290 – 1320 – 1414 – 1451** end at **1526** (Panipat).",
  "example": {"q": "Which dynasty ruled Delhi immediately before the Lodis?", "solution": "Tum **Sab** Lo → **Sayyid** comes just before Lodi."}},
 {"title": "Who did what — first letter hooks",
  "body": "**I**ltutmish = **I**qta + **I**nvestiture; **B**alban = **B**ow down (sijda/paibos); **A**lauddin = **A**ll prices fixed; **M**uhammad bin Tughlaq = **M**ove capital + **M**oney tokens; **F**iroz = **F**ields & canals."}
],
"mistakes": [
 "Token currency and Daulatabad = **Muhammad bin Tughlaq**, not Firoz Shah.",
 "Market control = **Alauddin Khalji**; Balban never fixed prices.",
 "Qutub Minar was **begun** by Aibak but **completed** by Iltutmish.",
 "The Lodis were **Afghans**; all earlier Sultanate dynasties were Turkish (the Sayyids claimed descent from the Prophet)."
]
})

# ---------------------------------------------------------------- 3. Vijayanagara & Bahmani
S.append({
"id": "vijayanagara-bahmani",
"title": "Vijayanagara & Bahmani Kingdoms",
"concept": """**Vijayanagara empire (1336–1646)**

| Point | Fact |
|---|---|
| Founded | **1336** by brothers **Harihara I and Bukka Raya** (Sangama dynasty); capital **Hampi** on the **Tungabhadra** |
| Four dynasties | **Sangama → Saluva → Tuluva → Aravidu** |
| Greatest ruler | **Krishnadevaraya** (Tuluva, 1509–29) — wrote Telugu poem ***Amuktamalyada***; court of **Ashtadiggajas** (eight poets) incl. **Allasani Peddana** and **Tenali Ramakrishna** |
| Decline | **Battle of Talikota (Rakshasi–Tangadi), 1565** — Rama Raya killed by the combined Deccan sultanates |
| Heritage | Group of Monuments at **Hampi** — UNESCO site (1986); Vitthala temple stone chariot |

**Foreign visitors to Vijayanagara**

| Visitor | From | Ruler |
|---|---|---|
| Niccolo de Conti | Italy | Deva Raya I |
| **Abdur Razzaq** | Persia (Timurid envoy) | **Deva Raya II** |
| **Domingo Paes** | Portugal | **Krishnadevaraya** |
| Fernao Nuniz | Portugal | Achyuta Raya |

**Bahmani kingdom (1347–1527)**
- Founded **1347** by **Alauddin Hasan Bahman Shah (Hasan Gangu)**; capital **Gulbarga**, later **Bidar**.
- Minister **Mahmud Gawan** built a famous **madrasa at Bidar**.
- Split into **five Deccan Sultanates**:

| Sultanate | Dynasty | Monument to remember |
|---|---|---|
| **Bijapur** | Adil Shahi | **Gol Gumbaz** (Muhammad Adil Shah) — whispering gallery |
| **Golconda** | Qutb Shahi | **Charminar**, Hyderabad (1591, Muhammad Quli Qutb Shah) |
| **Ahmadnagar** | Nizam Shahi | Chand Bibi resisted Akbar |
| **Bidar** | Barid Shahi | — |
| **Berar** | Imad Shahi | Did **not** join the Talikota alliance |""",
"formulas": [],
"tricks": [
 {"title": "Vijayanagara dynasties — \"Some Silly Tigers Attack\"",
  "body": "**S**angama → **S**aluva → **T**uluva → **A**ravidu. Krishnadevaraya sits in the third (**T**uluva — \"Top king\").",
  "example": {"q": "Krishnadevaraya belonged to which dynasty of Vijayanagara?", "solution": "Top king → **T**uluva dynasty."}},
 {"title": "Deccan five — \"BiG AB B\"",
  "body": "**Bi**japur (Adil), **G**olconda (Qutb), **A**hmadnagar (Nizam), **B**idar (Barid), **B**erar (Imad). The first letters of the dynasty names: A-Q-N-B-I."}
],
"mistakes": [
 "Hampi is on the **Tungabhadra**, not the Krishna.",
 "Abdur Razzaq visited **Deva Raya II**, not Krishnadevaraya.",
 "Gol Gumbaz is in **Bijapur**; Charminar is in **Hyderabad** (Golconda kingdom)."
]
})

# ---------------------------------------------------------------- 4. Mughals & Sur
S.append({
"id": "mughals",
"title": "Mughal Empire & Sher Shah Suri",
"concept": """**Emperor table**

| Ruler | Years | Key facts |
|---|---|---|
| **Babur** | 1526–30 | **First Battle of Panipat (21 April 1526)** vs Ibrahim Lodi — first use of field guns in India; Khanwa 1527, Chanderi 1528 (Medini Rai), Ghaghra 1529; memoir ***Tuzuk-i-Baburi / Baburnama*** in **Turki** |
| **Humayun** | 1530–40, 1555–56 | Lost to Sher Shah at **Chausa (1539)** and **Kannauj/Bilgram (1540)**; regained Delhi 1555; died falling from the stairs of his library (**Sher Mandal**) |
| **Sher Shah Suri** | 1540–45 | Silver **rupiya** & copper **dam**; rebuilt **Grand Trunk Road** (Sonargaon–Peshawar); sarais; land measurement; tomb at **Sasaram (Bihar)**; died at **Kalinjar** |
| **Akbar** | 1556–1605 | **Second Battle of Panipat (1556)** vs **Hemu** (regent **Bairam Khan**); **Mansabdari** system; abolished pilgrim tax & **jizya (1564)**; **Ibadat Khana** at Fatehpur Sikri (1575); **Din-i-Ilahi (1582)**; revenue system **Zabti/Dahsala** by **Raja Todar Mal**; **Buland Darwaza** marks the Gujarat conquest; **Haldighati (1576)** – Mughal army under **Man Singh** vs **Maharana Pratap** |
| **Jahangir** | 1605–27 | **Chain of justice** (Zanjir-i-Adl); **Nur Jahan**; English envoys **William Hawkins (1608)** and **Sir Thomas Roe (1615)**; executed **Guru Arjan Dev (1606)**; memoir *Tuzuk-i-Jahangiri* |
| **Shah Jahan** | 1628–58 | **Taj Mahal** (for Mumtaz Mahal), **Red Fort** & **Jama Masjid**, Delhi (Shahjahanabad); **Peacock Throne**; golden age of Mughal architecture |
| **Aurangzeb** | 1658–1707 | Re-imposed **jizya (1679)**; executed **Guru Tegh Bahadur (1675)**; long Deccan wars; died at Ahmednagar, buried at **Khuldabad** |
| Later Mughals | — | **Nadir Shah** (Persia) invaded **1739** (Battle of Karnal) under Muhammad Shah "Rangila" and took the **Peacock Throne** and **Koh-i-Noor** |

**Administration terms**

| Term | Meaning |
|---|---|
| Mansab | Rank fixed by **zat** (personal rank) and **sawar** (cavalry count) |
| Jagir | Revenue assignment given to a mansabdar in lieu of salary |
| Subah / Sarkar / Pargana | Province / district / sub-district |
| Diwan / Mir Bakshi | Finance / military pay & intelligence |

**Architecture quick pairs:** Humayun's Tomb (Delhi) – first garden-tomb on the Indian subcontinent; **Itimad-ud-Daulah** (Agra) – built by **Nur Jahan** for her father, early pietra dura in white marble; Fatehpur Sikri – Akbar's city (Panch Mahal, Jodha Bai palace).""",
"formulas": [],
"tricks": [
 {"title": "Mughal order — \"Bahut Hi Accha Jalebi Shahi Aur\"",
  "body": "**B**abur → **H**umayun → **A**kbar → **J**ahangir → **S**hah Jahan → **A**urangzeb. Sher Shah sits between Humayun's two reigns (1540–55).",
  "example": {"q": "Which ruler came between Humayun's two reigns?", "solution": "**Sher Shah Suri** (and his Sur successors), 1540–1555."}},
 {"title": "Three Panipats — 26, 56, 61",
  "body": "**1526** Babur beats Ibrahim Lodi · **1556** Akbar (Bairam Khan) beats Hemu · **1761** Ahmad Shah Abdali beats the Marathas. Gap pattern: +30 years, then +205 years."}
],
"mistakes": [
 "Rupiya was introduced by **Sher Shah**, not Akbar.",
 "Din-i-Ilahi = **1582**, Ibadat Khana = **1575** — do not swap.",
 "Haldighati Mughal commander = **Man Singh**, not Akbar in person.",
 "Taj Mahal = Shah Jahan; Itimad-ud-Daulah = **Nur Jahan**."
]
})

# ---------------------------------------------------------------- 5. Marathas & Sikhs
S.append({
"id": "marathas-sikhs",
"title": "Marathas & Sikh Gurus",
"concept": """**Shivaji & the Marathas**

| Point | Fact |
|---|---|
| Shivaji | Born **1630** at **Shivneri**; Treaty of **Purandar (1665)** with Raja Jai Singh; coronation **1674 at Raigad**, title **Chhatrapati** |
| Taxes | **Chauth** = 1/4 (25%) and **Sardeshmukhi** = extra 10% of revenue |
| First Peshwa of the Bhat family | **Balaji Vishwanath** (1713) |
| Baji Rao I | Greatest cavalry general among the Peshwas |
| **Third Battle of Panipat** | **14 January 1761** — **Ahmad Shah Abdali** defeated the Marathas under **Sadashivrao Bhau** (Peshwa then: Balaji Baji Rao / Nana Saheb) |

**Ashtapradhan (Shivaji's council of eight)**

| Post | Portfolio |
|---|---|
| **Peshwa** | Prime Minister |
| **Amatya (Majumdar)** | Finance / accounts |
| Mantri (Waqia-navis) | Daily records, king's diary |
| Sachiv (Shurunavis) | Royal correspondence |
| **Sumant (Dabir)** | **Foreign affairs** |
| Senapati (Sar-i-Naubat) | Army |
| Panditrao | Religious matters |
| Nyayadhish | Justice |

**Ten Sikh Gurus**

| # | Guru | Remember for |
|---|---|---|
| 1 | **Guru Nanak** | Founder; born **Talwandi (Nankana Sahib)** 1469 |
| 2 | Guru Angad | Standardised **Gurmukhi** script |
| 3 | Guru Amar Das | Manji system; strengthened langar |
| 4 | Guru Ram Das | Founded **Amritsar** (Ramdaspur) |
| 5 | **Guru Arjan Dev** | Compiled **Adi Granth (1604)**; built Harmandir Sahib; executed by **Jahangir (1606)** |
| 6 | Guru Hargobind | **Akal Takht**; militarisation |
| 7 | Guru Har Rai | — |
| 8 | Guru Har Krishan | Youngest guru |
| 9 | **Guru Tegh Bahadur** | Executed by **Aurangzeb (1675)** in Delhi |
| 10 | **Guru Gobind Singh** | Founded the **Khalsa (1699)** at **Anandpur Sahib**; declared the Granth the eternal Guru |

**Maharaja Ranjit Singh:** Sukerchakia misl; took **Lahore in 1799**; "Sher-e-Punjab".""",
"formulas": [],
"tricks": [
 {"title": "Guru order — \"Nana Aur Amar Ram Arjun, Har-Har-Har Tegh Gobind\"",
  "body": "**N**anak, **A**ngad, **Amar** Das, **Ram** Das, **Arjan** → the three Hars (**Har**gobind, **Har** Rai, **Har** Krishan) → **Tegh** Bahadur → **Gobind** Singh.",
  "example": {"q": "Who was the ninth Sikh Guru?", "solution": "After the three Hars (6, 7, 8) comes **Tegh Bahadur** (9)."}},
 {"title": "Chauth vs Sardeshmukhi",
  "body": "**Ch**auth = **Ch**aar ana in the rupee (**1/4**); **Sardeshmukhi = 10%** — the Sardeshmukh claimed a 'tenth' as hereditary head."}
],
"mistakes": [
 "Adi Granth compiled by **Guru Arjan Dev**; Khalsa founded by **Guru Gobind Singh**.",
 "Guru Arjan was executed by **Jahangir**; Guru Tegh Bahadur by **Aurangzeb**.",
 "Third Panipat winner = **Ahmad Shah Abdali (Durrani)**, not Nadir Shah (who invaded in 1739)."
]
})

# ---------------------------------------------------------------- 6. Bhakti & Sufi
S.append({
"id": "bhakti-sufi",
"title": "Bhakti & Sufi Movements",
"concept": """**Bhakti saints**

| Saint | Region | Remember for |
|---|---|---|
| Alvars / Nayanars | Tamil Nadu (6th–9th c.) | Vishnu / Shiva devotion |
| **Ramanuja** | Tamil Nadu | **Vishishtadvaita** (qualified non-dualism) |
| **Madhvacharya** | Karnataka | **Dvaita** (dualism) |
| **Basavanna** | Karnataka (12th c.) | **Virashaiva / Lingayat** movement; *vachanas* |
| **Ramananda** | North India | Guru of **Kabir** and **Ravidas** |
| **Kabir** | Varanasi | Dohas collected in ***Bijak***; attacked idol worship and ritual |
| **Chaitanya Mahaprabhu** | Bengal / Odisha (Puri) | Gaudiya Vaishnavism; **sankirtan** |
| **Tulsidas** | UP | ***Ramcharitmanas*** in **Awadhi** |
| **Surdas** | Braj | ***Sursagar*** (Krishna) in **Braj Bhasha** |
| **Mirabai** | Rajasthan (Mewar) | Krishna bhajans |
| Jnaneshwar | Maharashtra | ***Jnaneshwari*** — Marathi commentary on the Gita |
| Namdev, **Tukaram** | Maharashtra | Warkari tradition; Tukaram's **abhangas** |
| **Sankardeva** | Assam | **Ekasarana dharma**; founded **sattras** and namghars |

**Sufi orders (silsilas)**

| Order | Key saint | Centre |
|---|---|---|
| **Chishti** | **Khwaja Moinuddin Chishti** (came c. 1192) | **Ajmer** |
| Chishti | Qutbuddin Bakhtiyar Kaki | Delhi (Qutub Minar named after him) |
| Chishti | **Baba Farid** (Fariduddin Ganj-i-Shakar) | Pakpattan — verses in the **Adi Granth** |
| Chishti | **Nizamuddin Auliya** | Delhi — disciple **Amir Khusrau** |
| **Suhrawardi** | Bahauddin Zakariya | **Multan** |
| **Naqshbandi** | **Shaikh Ahmad Sirhindi** | Orthodox; opposed Akbar's liberal policies |

**Amir Khusrau:** called *Tuti-i-Hind* ("Parrot of India"); credited with shaping **qawwali**; wrote in Persian and Hindavi.""",
"formulas": [],
"tricks": [
 {"title": "Philosophy trio — \"RaVi MaD\"",
  "body": "**Ra**manuja → **Vi**shishtadvaita · **Ma**dhva → **D**vaita · (Shankara → Advaita).",
  "example": {"q": "Dvaita philosophy was propounded by —", "solution": "Ma**D**hva → **D**vaita."}},
 {"title": "Language of the epic",
  "body": "Tulsidas = **A**wadhi (**A** for Ayodhya's Ram) · Surdas = **B**raj (**B**al-Krishna)."}
],
"mistakes": [
 "Ramcharitmanas is in **Awadhi**, not Sanskrit or Braj.",
 "Moinuddin Chishti = **Ajmer**; Nizamuddin Auliya = **Delhi**.",
 "Sankardeva is from **Assam**; Chaitanya from **Bengal**."
]
})

# ---------------------------------------------------------------- 7. Sources & travellers
S.append({
"id": "sources-travellers",
"title": "Medieval Books & Foreign Travellers",
"concept": """**Book → author**

| Book | Author | Note |
|---|---|---|
| *Kitab-ul-Hind (Tahqiq-i-Hind)* | **Al-Biruni** | India under Mahmud of Ghazni |
| *Tabaqat-i-Nasiri* | Minhaj-us-Siraj | Dedicated to Nasiruddin Mahmud |
| *Tarikh-i-Firoz Shahi* | **Ziauddin Barani** | Sultanate history |
| *Rihla* | **Ibn Battuta** | Travels incl. Muhammad bin Tughlaq's India |
| *Padmavat* | **Malik Muhammad Jayasi** | Awadhi epic (1540) |
| *Humayun-nama* | **Gulbadan Begum** | Babur's daughter |
| ***Akbarnama* & *Ain-i-Akbari*** | **Abul Fazl** | Ain is the third volume of the Akbarnama |
| *Muntakhab-ut-Tawarikh* | Abdul Qadir **Badauni** | Critical of Akbar |
| *Razmnama* | Translation team under Akbar | Persian **Mahabharata** |
| *Padshahnama* | Abdul Hamid Lahori | Shah Jahan's reign |
| *Majma-ul-Bahrain*, *Sirr-i-Akbar* | **Dara Shikoh** | Confluence of Sufism & Vedanta; Persian Upanishads |

**Traveller → ruler visited**

| Traveller | Country | Ruler / period |
|---|---|---|
| Al-Biruni | Central Asia (Khwarazm) | Mahmud of Ghazni |
| **Marco Polo** | Venice (Italy) | Kakatiya queen **Rudramadevi** (late 13th c.) |
| **Ibn Battuta** | **Morocco** | **Muhammad bin Tughlaq** |
| Abdur Razzaq | Persia | Deva Raya II (Vijayanagara) |
| Domingo Paes | Portugal | Krishnadevaraya |
| William Hawkins | England | Jahangir (1608) |
| **Sir Thomas Roe** | England (envoy of James I) | **Jahangir (1615)** |
| **François Bernier** | France | Shah Jahan & Aurangzeb |
| Jean-Baptiste Tavernier | France | Shah Jahan (diamond merchant) |""",
"formulas": [],
"tricks": [
 {"title": "Mughal chroniclers — \"Abul = Ain, Badauni = Bitter\"",
  "body": "**Abul** Fazl wrote the official, praising **A**kbarnama/**A**in; **B**adauni wrote the **b**itter, critical *Muntakhab*.",
  "example": {"q": "Which historian wrote a critical account of Akbar's religious policy?", "solution": "**B**itter → **B**adauni (*Muntakhab-ut-Tawarikh*)."}},
 {"title": "Travellers by century",
  "body": "11th Al-Biruni → 13th Marco Polo → 14th Ibn Battuta → 15th Conti & Abdur Razzaq → 16th Paes & Nuniz → 17th Hawkins, Roe, Bernier, Tavernier."}
],
"mistakes": [
 "Ibn Battuta was **Moroccan**, not Persian.",
 "Humayun-nama was written by **Gulbadan Begum**, not Humayun.",
 "Marco Polo visited the **Kakatiya** kingdom in the south, not the Delhi Sultanate."
]
})

# ---------------------------------------------------------------- PYQ patterns
P = [
 {"pattern": "Ruler ↔ reform/innovation", "frequency": "very common",
  "howToSpot": "Stem names a reform (token currency, market control, sijda, Mansabdari, rupiya) and asks who introduced it.",
  "approach": "Use the first-letter hooks: Iltutmish-Iqta, Balban-Bow, Alauddin-All prices, MbT-Move & Money, Firoz-Fields, Sher Shah-Silver rupiya, Akbar-Mansab."},
 {"pattern": "Battle ↔ year/parties", "frequency": "very common",
  "howToSpot": "Tarain, Panipat, Talikota, Haldighati, Chausa, Kannauj named with a year or a participant blank.",
  "approach": "Memorise the chain 1191–1192–1526–1527–1556–1565–1576–1761; eliminate options that belong to a different battle in the chain."},
 {"pattern": "Book ↔ author / traveller ↔ ruler", "frequency": "common",
  "howToSpot": "\"Who wrote…\", \"… visited the court of …\".",
  "approach": "Tables in the last subtopic; sort travellers by century and the ruler follows."},
 {"pattern": "Saint ↔ region/philosophy/text", "frequency": "common",
  "howToSpot": "Bhakti/Sufi name with Dvaita, Ajmer, Bijak, Ramcharitmanas, sattra, etc.",
  "approach": "Tie each saint to one region and one text; Sufi orders to one city."},
 {"pattern": "Monument ↔ builder", "frequency": "occasional",
  "howToSpot": "Alai Darwaza, Buland Darwaza, Gol Gumbaz, Charminar, Itimad-ud-Daulah.",
  "approach": "Remember the ruler plus the occasion (Buland = Gujarat victory; Itimad = Nur Jahan's father)."},
]

# ---------------------------------------------------------------- solved examples
SE = [
 Q("med-ex01", "Arrange the following battles in chronological order:\n1. Battle of Talikota\n2. Second Battle of Panipat\n3. First Battle of Tarain\n4. Battle of Haldighati",
   ["3, 2, 1, 4", "3, 1, 2, 4", "2, 3, 1, 4", "3, 2, 4, 1"], 0,
   "Tarain I = **1191**; Panipat II = **1556**; Talikota = **1565**; Haldighati = **1576**. So the order is 3 → 2 → 1 → 4.",
   "Only 3 can come first (12th century) → options A, B, D remain; 1556 < 1565 puts Panipat II before Talikota → A.",
   "medium", "mughals", "Chronology of battles", 40),
 Q("med-ex02", "Which of the following traveller–ruler pairs is **NOT** correctly matched?",
   ["Al-Biruni — Mahmud of Ghazni", "Marco Polo — Rudramadevi", "Abdur Razzaq — Krishnadevaraya", "Sir Thomas Roe — Jahangir"], 2,
   "Abdur Razzaq, the envoy of the Timurid ruler Shah Rukh, visited **Deva Raya II** (1440s). The Portuguese **Domingo Paes** is the visitor linked with Krishnadevaraya. The other three pairs are correct.",
   "15th-century Persian envoy ≠ 16th-century king — the dates alone expose the wrong pair.",
   "medium", "sources-travellers", "Traveller ↔ ruler (odd pair)", 35),
 Q("med-ex03", "The **Mansabdari** system, in which every officer held a rank defined by *zat* and *sawar*, was introduced by —",
   ["Babur", "Sher Shah Suri", "Akbar", "Shah Jahan"], 2,
   "**Akbar** introduced the Mansabdari system (1570s). *Zat* fixed the personal rank and salary; *sawar* fixed the number of horsemen to be maintained. Mansabdars were usually paid through **jagirs**.",
   "Mansab = rank → Akbar built the Mughal bureaucracy; Babur and Humayun had no time to.",
   "easy", "mughals", "Ruler ↔ reform", 20),
 Q("med-ex04", "In Shivaji's **Ashtapradhan**, the minister in charge of **foreign affairs** was the —",
   ["Amatya", "Sumant", "Sachiv", "Panditrao"], 1,
   "The **Sumant (Dabir)** handled foreign affairs and relations with other states. Amatya = finance/accounts; Sachiv = royal correspondence; Panditrao = religious affairs.",
   "**S**umant = **S**tates abroad.",
   "medium", "marathas-sikhs", "Institution ↔ function", 25),
]

# ---------------------------------------------------------------- practice
PR = [
 Q("med-q01", "The **tripartite struggle** among the Palas, Gurjara-Pratiharas and Rashtrakutas was fought for control over —",
   ["Kannauj", "Pataliputra", "Ujjain", "Delhi"], 0,
   "From the 8th to the 10th century the three powers fought for **Kannauj**, the symbol of supremacy over north India after Harsha.",
   "PPR fight for **K**annauj.", "easy", "early-medieval", "Event ↔ place", 20),
 Q("med-q02", "Prithviraj Chauhan was defeated and the way to Turkish rule in north India was opened at the **Second Battle of Tarain (1192)**. Who won that battle?",
   ["Mahmud of Ghazni", "Muhammad Ghori", "Qutb-ud-din Aibak", "Iltutmish"], 1,
   "**Muhammad Ghori** (Muizzuddin Muhammad bin Sam), beaten in 1191, returned in 1192 and defeated Prithviraj. Mahmud of Ghazni had died in 1030; Aibak was Ghori's general.",
   "Tarain: 1st to Prithviraj, **2nd to Ghori**.", "easy", "early-medieval", "Battle ↔ victor", 20),
 Q("med-q03", "Which Delhi Sultan introduced the silver **tanka** and the copper **jital**?",
   ["Balban", "Alauddin Khalji", "Iltutmish", "Qutb-ud-din Aibak"], 2,
   "**Iltutmish** issued the standard Arabic coins — silver tanka and copper jital — and also organised the **iqta** system and the Group of Forty.",
   "**I**ltutmish = **I**qta + **I**deal coins.", "medium", "delhi-sultanate", "Ruler ↔ reform", 20),
 Q("med-q04", "The Persian court customs of **sijda** (prostration) and **paibos** (kissing the monarch's feet) were introduced by —",
   ["Iltutmish", "Razia Sultan", "Alauddin Khalji", "Balban"], 3,
   "**Balban** raised the prestige of the crown with sijda, paibos and the Nauroz festival, and followed a policy of 'blood and iron'.",
   "**B**alban = **B**ow down.", "medium", "delhi-sultanate", "Ruler ↔ reform", 20),
 Q("med-q05", "Price control in the markets of Delhi, supervised by the **Shahna-i-Mandi**, was a reform of —",
   ["Alauddin Khalji", "Firoz Shah Tughlaq", "Muhammad bin Tughlaq", "Sikandar Lodi"], 0,
   "**Alauddin Khalji** fixed prices of grain, cloth, horses and slaves so that he could pay a large standing army in cash. He also started **dagh** and **chehra**.",
   "**A**lauddin = **A**ll prices fixed.", "easy", "delhi-sultanate", "Ruler ↔ reform", 20),
 Q("med-q06", "Which Sultan shifted his capital from Delhi to **Daulatabad (Devagiri)** in 1327?",
   ["Firoz Shah Tughlaq", "Muhammad bin Tughlaq", "Ghiyas-ud-din Tughlaq", "Alauddin Khalji"], 1,
   "**Muhammad bin Tughlaq** moved the capital to Daulatabad to control the Deccan, but soon had to return. He also issued the unsuccessful **token currency**.",
   "**M**bT = **M**ove the capital + **M**oney tokens.", "easy", "delhi-sultanate", "Ruler ↔ event", 20),
 Q("med-q07", "The city of **Agra** was founded in 1504 by —",
   ["Bahlol Lodi", "Ibrahim Lodi", "Sikandar Lodi", "Sher Shah Suri"], 2,
   "**Sikandar Lodi** founded Agra and made it his second capital. He also introduced the **Gaz-i-Sikandari**, a standard measuring yard.",
   "Sikandar → **A**gra + **G**az (A-G, like 'Agra Gaz').", "medium", "delhi-sultanate", "Ruler ↔ city", 20),
 Q("med-q08", "The Telugu work ***Amuktamalyada*** was written by which Vijayanagara ruler?",
   ["Harihara I", "Deva Raya II", "Rama Raya", "Krishnadevaraya"], 3,
   "**Krishnadevaraya** (Tuluva dynasty) wrote *Amuktamalyada*, about the Alvar saint Andal. His court had the eight poets called **Ashtadiggajas**.",
   "The poet-king of Vijayanagara = Krishnadevaraya.", "medium", "vijayanagara-bahmani", "Book ↔ author", 20),
 Q("med-q09", "The **Battle of Talikota**, after which the city of Vijayanagara was sacked, was fought in —",
   ["1526", "1556", "1565", "1576"], 2,
   "In **January 1565** the combined forces of Bijapur, Ahmadnagar, Golconda and Bidar defeated Vijayanagara; Rama Raya was killed. 1526 and 1556 are the first two Panipats; 1576 is Haldighati.",
   "Chain 26–56–**65**–76: Talikota is the '65' link.", "medium", "vijayanagara-bahmani", "Battle ↔ year", 20),
 Q("med-q10", "The silver coin called **rupiya** was first introduced by —",
   ["Sher Shah Suri", "Akbar", "Babur", "Muhammad bin Tughlaq"], 0,
   "**Sher Shah Suri** (1540–45) issued the silver rupiya and the copper dam, which the Mughals continued. He also rebuilt the Grand Trunk Road.",
   "**S**her **S**hah = **S**ilver rupiya.", "easy", "mughals", "Ruler ↔ reform", 20),
 Q("med-q11", "In the **Battle of Haldighati (1576)**, the Mughal army that fought Maharana Pratap was commanded by —",
   ["Bairam Khan", "Raja Man Singh", "Raja Todar Mal", "Abdul Rahim Khan-i-Khanan"], 1,
   "**Raja Man Singh** of Amber led Akbar's army at Haldighati. Bairam Khan was Akbar's regent at Panipat II; Todar Mal was the revenue expert.",
   "Haldighati = Rajput vs Rajput: Pratap vs **Man Singh**.", "medium", "mughals", "Battle ↔ commander", 25),
 Q("med-q12", "***Ain-i-Akbari***, the detailed account of Akbar's administration, was written by —",
   ["Badauni", "Faizi", "Abul Fazl", "Nizamuddin Ahmad"], 2,
   "**Abul Fazl** wrote the *Akbarnama*, whose third volume is the *Ain-i-Akbari*. Faizi was his brother (poet); Badauni wrote the critical *Muntakhab-ut-Tawarikh*.",
   "**A**bul = **A**in = **A**kbarnama.", "easy", "sources-travellers", "Book ↔ author", 20),
 Q("med-q13", "The **Khalsa** was founded at Anandpur Sahib in 1699 by —",
   ["Guru Nanak", "Guru Arjan Dev", "Guru Tegh Bahadur", "Guru Gobind Singh"], 3,
   "**Guru Gobind Singh**, the tenth Guru, founded the Khalsa on Baisakhi 1699 and later declared the Granth Sahib the eternal Guru.",
   "The **last** Guru created the **last** big institution — Khalsa.", "easy", "marathas-sikhs", "Guru ↔ contribution", 20),
 Q("med-q14", "In the **Third Battle of Panipat (1761)**, the Marathas were defeated by —",
   ["Ahmad Shah Abdali", "Nadir Shah", "Timur", "Muhammad Ghori"], 0,
   "**Ahmad Shah Abdali (Durrani)** of Afghanistan defeated the Maratha army under **Sadashivrao Bhau** on 14 January 1761. Nadir Shah invaded in 1739 and Timur in 1398.",
   "Invaders by year: Timur 1398 → Nadir 1739 → **Abdali 1761**.", "easy", "marathas-sikhs", "Battle ↔ victor", 20),
 Q("med-q15", "The traveller **Ibn Battuta**, who served as qazi of Delhi under Muhammad bin Tughlaq, came from —",
   ["Persia", "Morocco", "Italy", "Portugal"], 1,
   "**Ibn Battuta** was from **Tangier, Morocco**. He reached India in 1333 and described it in his travel book *Rihla*.",
   "**B**attuta — **B**erber North Africa → Morocco.", "medium", "sources-travellers", "Traveller ↔ origin", 20),
 Q("med-q16", "Tulsidas composed the ***Ramcharitmanas*** in which language?",
   ["Sanskrit", "Braj Bhasha", "Awadhi", "Maithili"], 2,
   "*Ramcharitmanas* (16th century) is in **Awadhi**. Surdas wrote *Sursagar* in Braj Bhasha; Vidyapati wrote in Maithili.",
   "Tulsi = **A**wadhi (**A**yodhya's Ram); Sur = **B**raj.", "medium", "bhakti-sufi", "Text ↔ language", 20),
 Q("med-q17", "**Amir Khusrau**, the poet called *Tuti-i-Hind*, was a disciple of which Sufi saint?",
   ["Moinuddin Chishti", "Nizamuddin Auliya", "Bahauddin Zakariya", "Shaikh Ahmad Sirhindi"], 1,
   "Amir Khusrau was the devoted disciple of **Nizamuddin Auliya** of the Chishti order in Delhi; both are buried in the Nizamuddin dargah complex. Bahauddin Zakariya was a Suhrawardi saint of Multan; Sirhindi was Naqshbandi.",
   "Both are in Delhi's **Nizamuddin** — the disciple rests beside his master.", "medium", "bhakti-sufi", "Saint ↔ disciple", 20),
]

topic = {
 "id": "medieval-history",
 "sectionId": "ga",
 "title": "Medieval Indian History",
 "order": 2,
 "importance": "medium",
 "avgQuestions": {"tier1": 1, "tier2": 1},
 "summary": "From the tripartite struggle to the Third Battle of Panipat: Delhi Sultanate reforms, Vijayanagara and the Deccan sultanates, the Mughals and Sher Shah, Marathas, Sikh Gurus, Bhakti–Sufi saints, and the books and travellers of the period. SSC asks 1–2 questions per shift, nearly always a pairing (ruler–reform, battle–year, book–author, traveller–ruler), so the tables here cover most of them.",
 "subtopics": S,
 "pyqPatterns": P,
 "solvedExamples": SE,
 "practice": PR,
}

if __name__ == "__main__":
    save_topic(topic)
