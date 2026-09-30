"""Readable rewrite of GA > Medieval History (all 7 subtopics).

Plain English, facts kept exactly as in the previous notes/concept, reorganised into tables and short lists.
Patterns = question types with a method and a worked example built only from facts in the notes.
Run: python medieval_history.py  (patches content/core/topics/ga/medieval-history.json in place)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "medieval-history.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": None,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


def mk(wrong, right):
    return {"wrong": wrong, "right": right}


S = {}

# ---------------------------------------------------------------- early-medieval
S["early-medieval"] = dict(
    concept=(
        "After Harsha, north India broke into many kingdoms. Three big powers fought for Kannauj: the Palas, "
        "the Gurjara-Pratiharas and the Rashtrakutas. Then came the Arab, Ghaznavid and Ghori attacks in the north-west. "
        "In the far south, the Cholas built a strong empire with a famous system of village self-government."
    ),
    notes=r"""### The three powers and the fight for Kannauj
From the 8th century, three kingdoms fought for the city of **Kannauj**. This is the **tripartite struggle**.

| Power | Region | Key facts |
|---|---|---|
| **Palas** | Bengal and Bihar | **Gopala** was chosen king by the chiefs (c. 750). **Dharmapala** founded **Vikramashila** and revived **Nalanda**. Buddhist patrons. |
| **Gurjara-Pratiharas** | Malwa and Rajasthan (west) | **Nagabhata I** stopped the Arab advance. **Mihira Bhoja** (Adivaraha coins) is the best-known ruler. |
| **Rashtrakutas** | Deccan | Founder **Dantidurga**. Capital **Manyakheta**. **Krishna I** built the **Kailasa temple at Ellora**. **Amoghavarsha I** wrote *Kavirajamarga* in Kannada. |

> **Tip:** Say "PPR fight for K": **P**ala, **P**ratihara, **R**ashtrakuta fight for **K**annauj.

### Sindh, Ghazni and Ghori
Three attacks came from the north-west. Learn them as a short timeline.

| Who | Year | What happened |
|---|---|---|
| **Muhammad bin Qasim** | **712 CE** | Arab conquest of Sindh. He defeated **Raja Dahir**. |
| **Mahmud of Ghazni** | 1000-1027 | **17 raids**. He sacked the **Somnath** temple in **1025**. |
| **Muhammad Ghori** | **1191** | **First Battle of Tarain**. He lost to **Prithviraj Chauhan**. |
| Muhammad Ghori | **1192** | **Second Battle of Tarain**. He won. |
| Muhammad Ghori | **1194** | **Chandawar**. He defeated **Jaichand** of Kannauj (Gahadavala). |

**Al-Biruni** came with Mahmud of Ghazni. He wrote *Kitab-ul-Hind*.

> **Watch:** Somnath was raided by **Mahmud of Ghazni** (1025), not by Muhammad Ghori.

### Rajput houses and their marks
| House | Region | Remember for |
|---|---|---|
| **Chauhans** (Chahamanas) | Ajmer and Delhi | **Prithviraj III**, the two Battles of Tarain |
| **Gahadavalas** | Kannauj and Varanasi | **Jaichand** |
| **Paramaras** | Malwa (Dhar) | **Raja Bhoja**, the scholar-king; Bhojpur |
| **Chandelas** | Bundelkhand | **Khajuraho** temples |
| **Solankis** (Chalukyas of Gujarat) | Gujarat | Somnath, Dilwara (Mt Abu), Modhera Sun temple era |
| **Tomaras** | Delhi region | Founded **Dhillika** (Delhi) |
| **Senas** | Bengal | **Lakshmanasena**; his capital fell to Bakhtiyar Khalji |

Two writers of the age: **Kalhana** wrote the *Rajatarangini* (12th century), the first proper history in Sanskrit. **Chand Bardai** was Prithviraj's court poet and wrote *Prithviraj Raso*.

### The Cholas at their height
The Chola line grew strong when **Vijayalaya** captured **Thanjavur** (c. 850).

- **Rajaraja I** won Sri Lanka and the Maldives. He built the **Brihadeshwara (Rajarajeshwara) temple** at Thanjavur.
- **Rajendra I** marched to the Ganga and took the title **Gangaikonda**. He built the capital **Gangaikondacholapuram**.
- Rajendra I also sent a **naval expedition against Srivijaya**, the Shailendra kingdom of Sumatra and the Malay peninsula. The aim was to guard the China trade.

The Chola navy, the **Nataraja** bronzes and temple building mark the peak of the age.

### Village self-rule: Uttaramerur
The **Uttaramerur inscriptions** date from **Parantaka I**'s reign. They show how village committees, called **variyams**, were picked.

1. Candidates were checked for age, property and learning.
2. Names were written on tickets and drawn from a pot. This is the **kudavolai** (pot-ticket) system.
3. A member could be removed for misconduct.

Village assemblies came in three kinds: the **ur** (common villages), the **sabha** (Brahmadeya villages) and the **nagaram** (merchant towns).

> **Rule:** Uttaramerur + Parantaka I = kudavolai lottery and variyam committees.

### Other regional powers
- **Eastern Gangas** (Odisha): **Narasimhadeva I** built the **Konark Sun Temple**.
- **Hoysalas**: capital **Dorasamudra (Halebidu)**. Temples at Belur, Halebidu and Somnathpura.
- **Kakatiyas** (Warangal): ruled for a time by the woman ruler **Rani Rudramadevi**.
- **Western Chalukyas of Kalyani**: **Vikramaditya VI** fought the Cholas for the Tungabhadra doab.
- **Yadavas**: held **Devagiri** until Alauddin Khalji's raids.
""",
    tricks=[
        trick("Tripartite: PPR fight for K",
              "**P**ala, **P**ratihara, **R**ashtrakuta fight for **K**annauj. East, west and south all wanted the centre.",
              "Which of these was NOT part of the tripartite struggle: Pala, Pratihara, Chola, Rashtrakuta?",
              ["The three were Pala, Pratihara and Rashtrakuta.", "Chola is the odd one out."],
              "Chola"),
        trick("Tarain: 1 to Prithviraj, 2 to Ghori",
              "**1191**, the first battle: Prithviraj wins. **1192**, the second battle: Ghori wins. The second number goes to the invader."),
    ],
    mistakes=[
        mk("Giving the Somnath raid to Muhammad Ghori.", "Somnath was sacked by **Mahmud of Ghazni** in **1025**."),
        mk("Saying Al-Biruni came with Muhammad Ghori.", "Al-Biruni came with **Mahmud of Ghazni** and wrote *Kitab-ul-Hind*."),
        mk("Crediting the 712 conquest of Sindh to Mahmud.", "**Muhammad bin Qasim** conquered Sindh in **712 CE** and beat Raja Dahir."),
        mk("Mixing up the two Tarain results.", "1191 was won by Prithviraj. 1192 was won by Ghori."),
        mk("Placing the Brihadeshwara temple under Rajendra I.", "**Rajaraja I** built it. Rajendra I took the Gangaikonda title."),
    ],
    revision=[
        "Tripartite struggle: Pala (Bengal), Pratihara (west), Rashtrakuta (Deccan). The prize was Kannauj.",
        "Gopala was chosen Pala king (c. 750). Dharmapala founded Vikramashila.",
        "Sindh 712 (Muhammad bin Qasim). Ghazni raids 1000-1027, Somnath 1025. Tarain 1191 and 1192, Chandawar 1194.",
        "Chola chain: Vijayalaya (Thanjavur, c. 850), then Rajaraja I (Brihadeshwara), then Rajendra I (Gangaikonda, navy against Srivijaya).",
        "Uttaramerur (Parantaka I): kudavolai lottery, variyam committees. Assemblies: ur, sabha, nagaram.",
        "Capitals and temples: Hoysala at Dorasamudra, Kakatiya at Warangal, Ganga at Konark, Chandela at Khajuraho.",
    ],
    patterns=[
        pat("ga-em-p1", "Tripartite struggle and the three powers", "very common",
            "The question names Kannauj, Gopala, Dharmapala, Nagabhata I, Dantidurga or Amoghavarsha.",
            ["Place the name in its power: Pala, Pratihara or Rashtrakuta.",
             "Recall the region: Bengal-Bihar, Malwa-Rajasthan or Deccan.",
             "In statement questions, check which dynasty each fact belongs to."],
            "Each ruler belongs to exactly one of the three powers, so the region gives the answer.",
            "Which Pala ruler founded the Vikramashila monastery?\n(a) Gopala (b) Dharmapala (c) Nagabhata I (d) Dantidurga",
            ["Gopala founded the Pala line, so he is not the builder.",
             "Nagabhata I was a Pratihara and Dantidurga a Rashtrakuta.",
             "Dharmapala founded Vikramashila and revived Nalanda."],
            "(b) Dharmapala"),
        pat("ga-em-p2", "Chola rulers and their achievements", "very common",
            "Words like Thanjavur, Gangaikonda, Srivijaya, Brihadeshwara or Vijayalaya.",
            ["Recall the chain: Vijayalaya, Rajaraja I, Rajendra I.",
             "Rajaraja I: Brihadeshwara temple, Sri Lanka and Maldives.",
             "Rajendra I: Gangaikonda title, Gangaikondacholapuram, navy against Srivijaya."],
            "Each Chola ruler has one or two signature deeds, and the options mix them.",
            "Which Chola ruler sent a naval expedition against the Srivijaya kingdom?",
            ["Srivijaya was in Sumatra and the Malay peninsula.", "The raid guarded the China trade and belongs to Rajendra I."],
            "Rajendra I"),
        pat("ga-em-p3", "Chola village administration", "common",
            "Words like Uttaramerur, kudavolai, variyam, ur, sabha or nagaram.",
            ["Link Uttaramerur to Parantaka I.",
             "Kudavolai means names drawn from a pot.",
             "Match the assembly to its people: ur (common), sabha (Brahmadeya), nagaram (merchants)."],
            "The three assembly names each point to one kind of settlement.",
            "Under the Chola kudavolai system, village committee members were chosen by:",
            ["Kudavolai means pot-ticket.", "Names of eligible candidates were drawn from a pot."],
            "Drawing lots (tickets) from a pot"),
        pat("ga-em-p4", "Rajput and regional kingdoms: house, capital, ruler", "very common",
            "A dynasty, a temple or a ruler to match: Khajuraho, Konark, Rudramadevi, Bhoja, Jaichand.",
            ["Recall the table: Chauhan, Gahadavala, Paramara, Chandela, Solanki, Sena.",
             "For the south and Deccan: Kakatiya, Hoysala, Eastern Ganga.",
             "Match the temple to its builder-dynasty before you answer."],
            "Dynasty, region and monument come as a fixed set, so one known item gives the rest.",
            "Rani Rudramadevi, a rare woman ruler of the medieval age, belonged to which dynasty?",
            ["Warangal was a capital of one dynasty.", "That dynasty is the Kakatiyas."],
            "The Kakatiyas of Warangal"),
        pat("ga-em-p5", "Invasions from the north-west: who, when, where", "very common",
            "Words like 712, Somnath, 17 raids, Tarain, Chandawar, Raja Dahir or Jaichand.",
            ["Sindh 712: Muhammad bin Qasim, Raja Dahir.",
             "Ghazni: 17 raids (1000-1027), Somnath 1025.",
             "Ghori: Tarain 1191 (lost), Tarain 1192 (won), Chandawar 1194 (Jaichand).",
             "Match the year or place to its invader."],
            "The three invaders are easy to swap, but each has its own dates and places.",
            "Muhammad Ghori defeated Jaichand of Kannauj in the Battle of:\n(a) Tarain 1191 (b) Tarain 1192 (c) Chandawar (d) Somnath",
            ["Jaichand was the Gahadavala ruler of Kannauj.", "Both Tarain battles were against Prithviraj.", "The 1194 battle at Chandawar was against Jaichand."],
            "(c) Chandawar (1194)"),
        pat("ga-em-p6", "Writers and works of the age", "occasional",
            "\"Who wrote Rajatarangini / Kavirajamarga / Kitab-ul-Hind / Prithviraj Raso?\"",
            ["Kalhana: Rajatarangini (Sanskrit, Kashmir).",
             "Amoghavarsha I: Kavirajamarga (Kannada).",
             "Al-Biruni: Kitab-ul-Hind. Chand Bardai: Prithviraj Raso."],
            "Each work has one author, and the language or region usually helps you spot it.",
            "The Rajatarangini, the first proper historical work in Sanskrit, was written by:",
            ["It is a chronicle of Kashmir from the 12th century.", "Its author is Kalhana."],
            "Kalhana"),
    ],
)

# ---------------------------------------------------------------- delhi-sultanate
S["delhi-sultanate"] = dict(
    concept=(
        "The Delhi Sultanate lasted from 1206 to 1526 under five dynasties: Slave, Khalji, Tughlaq, Sayyid and Lodi. "
        "Exams ask which ruler did what, such as Alauddin's market control or Muhammad bin Tughlaq's token currency. "
        "Learn the dynasty order first. Then attach one signature fact to each ruler."
    ),
    notes=r"""### Five dynasties in order
| Dynasty | Years | Founder |
|---|---|---|
| Mamluk / Slave (Ilbari) | 1206-1290 | **Qutb-ud-din Aibak** |
| Khalji | 1290-1320 | **Jalal-ud-din Khalji** |
| Tughlaq | 1320-1414 | **Ghiyas-ud-din Tughlaq** |
| Sayyid | 1414-1451 | **Khizr Khan** |
| Lodi | 1451-1526 | **Bahlol Lodi** |

The Lodis were the only Afghan dynasty.

> **Tip:** Order: **S**lave, **K**halji, **T**ughlaq, **S**ayyid, **L**odi. Start years: 1206, 1290, 1320, 1414, 1451. The end is 1526.

### The Slave dynasty
| Ruler | Signature facts |
|---|---|
| **Aibak** | Called **Lakh Baksh** (generous giver). Began the **Qutub Minar**. Built the Quwwat-ul-Islam mosque (Delhi) and Adhai Din ka Jhonpra (Ajmer). Capital **Lahore**. Died playing **chaugan (polo)**, 1210. |
| **Iltutmish** | Real consolidator. Shifted the capital to **Delhi**. Began the **iqta** system. Formed the **Turkan-i-Chahalgani** (Group of Forty). Issued the silver **tanka** and copper **jital**. Completed the Qutub Minar. Got recognition from the Abbasid Caliph (1229). |
| **Razia** | Only woman ruler of Delhi (1236-40). Daughter of Iltutmish. |
| **Balban** | "Blood and iron" policy. Court customs **sijda** and **paibos**. Started **Nauroz**. Created **Diwan-i-Arz**. Crushed the Chahalgani. |

### The Khalji dynasty
**Alauddin Khalji** is the star. His measures:

- **Market control**, with price fixing under the **Shahna-i-Mandi**.
- A **standing army** paid in cash.
- **Dagh** (branding of horses) and **chehra** (descriptive roll of soldiers).
- Land revenue of **50%**.
- **Alai Darwaza** (1311) and **Siri** Fort.
- General **Malik Kafur** raided the south.

> **Watch:** Market control was Alauddin's. Balban never fixed prices.

### The Tughlaq dynasty
| Ruler | Signature facts |
|---|---|
| **Ghiyas-ud-din** | Built **Tughlaqabad**. Died when a pavilion collapsed (1325). |
| **Muhammad bin Tughlaq** | Moved the capital to **Daulatabad (Devagiri), 1327**. Issued **token currency** in bronze and copper (1329-30). Set up **Diwan-i-Amir-Kohi** (agriculture). Ibn Battuta was his qazi of Delhi. |
| **Firoz Shah** | Dug canals (Yamuna, Sutlej). Set up **Diwan-i-Khairat** (charity) and **Diwan-i-Bandagan** (slaves). Extended **jizya to Brahmins**. Founded Firozabad, Hisar and Jaunpur. Brought **Ashokan pillars** from Topra and Meerut. |

Muhammad bin Tughlaq's tokens were forged, and both his experiments failed. **Timur** invaded in **1398**, under Nasir-ud-din Mahmud Tughlaq. His sack of Delhi broke the dynasty.

### Sayyids, Lodis and the end
- **Khizr Khan** founded the Sayyids after Timur's raid.
- **Sikandar Lodi** founded **Agra (1504)** and introduced the **Gaz-i-Sikandari** (measuring yard). His pen-name was *Gulrukhi*.
- **Ibrahim Lodi**, the last Sultan, was killed at the **First Battle of Panipat, 1526**.

### How the state ran
- **Iqta:** land revenue assigned to a noble (**muqti**). He collected tax and kept troops. It was not ownership.
- **Diwans:** **Wizarat** (finance), **Ariz** (army), **Risalat** (foreign and religious), **Qaza** (justice), **Insha** (letters).
- **Barids and munihiyan:** spies and news-writers. Persian was the court language.

> **Rule:** Iqta means revenue in return for service, not ownership of land.

### Land tax, jizya and the writers
**Kharaj** (land tax) could reach one third to one half of the produce. **Jizya** fell on non-Muslims. Firoz Shah extended it to Brahmins.

Three historians recorded the age:

- **Minhaj-us-Siraj:** *Tabaqat-i-Nasiri*.
- **Ziauddin Barani:** *Tarikh-i-Firoz Shahi* and *Fatawa-i-Jahandari*.
- **Amir Khusrau:** *Khazain-ul-Futuh* and *Tughlaqnama*.
""",
    tricks=[
        trick("Who did what: first-letter hooks",
              "**I**ltutmish = **I**qta. **B**alban = **B**ow down (sijda, paibos). **A**lauddin = **A**ll prices fixed. **M**uhammad bin Tughlaq = **M**ove capital and **M**oney tokens. **F**iroz = **F**ields and canals.",
              "Which sultan is linked with token currency and the shift of capital to Daulatabad?",
              ["Token money and a new capital are the two experiments of one ruler.", "He is Muhammad bin Tughlaq."],
              "Muhammad bin Tughlaq"),
        trick("Dynasty order: Sabka Khana Tum Sab Lo",
              "**S**lave, **K**halji, **T**ughlaq, **S**ayyid, **L**odi. \"Tum **Sab** Lo\": Sayyid comes just before Lodi."),
    ],
    mistakes=[
        mk("Giving token currency and Daulatabad to Firoz Shah.", "Both belong to **Muhammad bin Tughlaq**."),
        mk("Crediting Balban with market control.", "Market control was **Alauddin Khalji's**."),
        mk("Saying Iltutmish built the whole Qutub Minar.", "Aibak **began** it and Iltutmish **completed** it."),
        mk("Thinking every Sultanate dynasty was Turkish.", "The **Lodis were Afghans**. The Sayyids claimed descent from the Prophet."),
        mk("Placing Timur's invasion at the start of Tughlaq rule.", "Timur came in **1398**, near the end, and it led to the Sayyids."),
    ],
    revision=[
        "Slave 1206, Khalji 1290, Tughlaq 1320, Sayyid 1414, Lodi 1451, end 1526 (Panipat).",
        "Iltutmish: tanka and jital, Chahalgani, Qutub Minar. Balban: sijda, paibos, blood and iron.",
        "Alauddin: chehra and dagh, market reforms (Shahna-i-Mandi), Malik Kafur's raids, Siri.",
        "Muhammad bin Tughlaq: Daulatabad shift and token currency. Both failed.",
        "Firoz Shah: canals, Diwan-i-Khairat, Diwan-i-Bandagan, jizya on Brahmins.",
        "Iqta is revenue for service. Diwan-i-Ariz runs the army. Timur came in 1398.",
    ],
    patterns=[
        pat("ga-ds-p1", "Dynasty, founder and landmark chain", "very common",
            "\"Which dynasty came after...\", \"founder of...\", or a ruler matched to a dynasty.",
            ["Write the ladder with start years.",
             "Attach the founder: Aibak, Jalal-ud-din, Ghiyas-ud-din, Khizr Khan, Bahlol Lodi.",
             "Pick the option that fits both the position and the founder."],
            "The dynasty order never changes, so position alone often decides the answer.",
            "Which dynasty ruled Delhi immediately before the Lodis?\n(a) Tughlaq (b) Khalji (c) Sayyid (d) Slave",
            ["The order is Slave, Khalji, Tughlaq, Sayyid, Lodi.", "The Sayyids (1414-1451) came just before the Lodis."],
            "(c) Sayyid"),
        pat("ga-ds-p2", "Administration and economy: iqta, diwans, market control", "very common",
            "Words like iqta, muqti, Diwan-i-Ariz, Shahna-i-Mandi, chehra or dagh.",
            ["Iqta means revenue assignment for service, not ownership.",
             "Diwans: Wizarat finance, Ariz army, Risalat foreign and religious, Qaza justice, Insha letters.",
             "Alauddin's army tools: chehra (roll), dagh (horse branding)."],
            "Each department and each term has one meaning that the options test.",
            "Which department of the Delhi Sultanate looked after the army?",
            ["Ariz means the military branch.", "The department is Diwan-i-Ariz."],
            "Diwan-i-Ariz"),
        pat("ga-ds-p3", "Sultans' landmark acts and experiments", "very common",
            "\"Token currency\", \"capital shift\", \"canals\", \"jizya on Brahmins\", \"Qutub Minar completed\".",
            ["Name the act, then recall its ruler from the table.",
             "Muhammad bin Tughlaq: Daulatabad (1327), token currency (1329-30).",
             "Firoz Shah: canals, charity and slave departments, jizya on Brahmins."],
            "Each big act belongs to one ruler, and neighbours in the list are the traps.",
            "Muhammad bin Tughlaq's token currency failed mainly because:",
            ["Tokens were made of copper and bronze.", "They were easily forged, so the scheme was withdrawn."],
            "Copper tokens were easily forged"),
        pat("ga-ds-p4", "Foreign invasions and the Sultanate's end", "common",
            "Words like Timur, 1398, Siri, Mongol, Panipat or 1526.",
            ["Mongols: Alauddin built Siri against them.",
             "Timur 1398: sacked Delhi, broke the Tughlaqs, then the Sayyids came.",
             "1526: First Battle of Panipat ends the Sultanate."],
            "Three events mark the ends of the story: Mongol pressure, Timur and Panipat.",
            "Which sultan built the fort of Siri as a shelter against the Mongols?",
            ["Siri is linked with the Khalji dynasty.", "The builder was Alauddin Khalji."],
            "Alauddin Khalji"),
        pat("ga-ds-p5", "Which ruler did this? (signature fact match)", "very common",
            "A list of rulers on one side and famous facts on the other, or \"Lakh Baksh\", \"blood and iron\".",
            ["Tick the sure matches first: Aibak-Lakh Baksh, Razia-woman ruler, Balban-blood and iron.",
             "Then place Alauddin (market), MBT (tokens) and Firoz (canals).",
             "Cross out the options that repeat a ruler."],
            "Sure matches shrink the list, so the last pairs fall into place.",
            "Which Sultan is known as \"Lakh Baksh\" and began the Qutub Minar?",
            ["Lakh Baksh means generous giver.", "The first Slave ruler began the Qutub Minar."],
            "Qutb-ud-din Aibak"),
        pat("ga-ds-p6", "Historians and their books", "common",
            "\"Tabaqat-i-Nasiri\", \"Tarikh-i-Firoz Shahi\", \"Khazain-ul-Futuh\" or a match-the-column list.",
            ["Minhaj-us-Siraj: Tabaqat-i-Nasiri.",
             "Barani: Tarikh-i-Firoz Shahi, Fatawa-i-Jahandari.",
             "Amir Khusrau: Khazain-ul-Futuh, Tughlaqnama."],
            "Three authors cover the whole set, so learn each with its two books.",
            "Who wrote the Tarikh-i-Firoz Shahi?",
            ["The book is named after Firoz Shah.", "Its author is Ziauddin Barani."],
            "Ziauddin Barani"),
    ],
)

# ---------------------------------------------------------------- vijayanagara-bahmani
S["vijayanagara-bahmani"] = dict(
    concept=(
        "Vijayanagara was a great Hindu empire in south India on the Tungabhadra river. "
        "The Bahmani kingdom was its Muslim neighbour and rival in the Deccan. "
        "Later the Bahmani kingdom split into five sultanates, and they crushed Vijayanagara at Talikota in 1565."
    ),
    notes=r"""### City of victory on the Tungabhadra
**Vijayanagara** means "city of victory". It ran from **1336 to 1646**.

- Founded in **1336** at **Hampi**, on the **Tungabhadra**, by the brothers **Harihara I and Bukka Raya** (Sangama dynasty).
- The guru **Vidyaranya** blessed them.
- Four dynasties ruled in turn: **Sangama, Saluva, Tuluva, Aravidu**.
- Its wealth rested on the fertile **Raichur doab** (land between the Krishna and the Tungabhadra), diamond and spice trade, and cavalry fed by Portuguese horses.

> **Tip:** "Some Silly Tigers Attack" gives **S**angama, **S**aluva, **T**uluva, **A**ravidu.

### Krishnadevaraya (1509-1529)
He belonged to the **Tuluva** dynasty and was the greatest Vijayanagara ruler.

- He defeated the Bahmanis and the Odisha (Gajapati) king.
- He won the **Battle of Raichur** (1520), using Portuguese muskets.
- His titles include **Andhra Bhoja**. Another title is "establisher of Yavana rule".
- He wrote the Telugu classic **Amuktamalyada**.
- His court had the **Ashtadiggajas** (eight poets, "elephants of learning"). The greatest was **Allasani Peddana**, author of *Manucharitam*, honoured as "Andhra Kavita Pitamaha". **Tenali Ramakrishna** was also in this court.

Portuguese visitors **Domingo Paes** and **Duarte Barbosa** described his capital. They wrote about the **Virupaksha** and **Vittala** temples (with the stone chariot), the Hazara Rama temple and bazaars of pearls.

### Foreign visitors to Vijayanagara
| Visitor | From | Ruler |
|---|---|---|
| Niccolo de Conti | Italy | Deva Raya I |
| **Abdur Razzaq** | Persia (Timurid envoy) | **Deva Raya II** |
| **Domingo Paes** | Portugal | **Krishnadevaraya** |
| Fernao Nuniz | Portugal | Achyuta Raya |

> **Watch:** Abdur Razzaq visited **Deva Raya II**, not Krishnadevaraya.

### The Bahmani kingdom and its five heirs
The Bahmani kingdom began in **1347** and lasted to **1527**.

- Founder: **Alauddin Hasan Bahman Shah (Hasan Gangu)**.
- Capital: **Gulbarga**, later **Bidar**.
- The able minister **Mahmud Gawan** built a famous **madrasa at Bidar**. Court factions executed him in **1481**.
- After that, the kingdom split into five sultanates.

| Sultanate | Dynasty | Monument or fact |
|---|---|---|
| **Bijapur** | Adil Shahi | **Gol Gumbaz** (Muhammad Adil Shah), the whispering gallery |
| **Golconda** | Qutb Shahi | **Charminar**, Hyderabad (1591, Muhammad Quli Qutb Shah) |
| **Ahmadnagar** | Nizam Shahi | **Chand Bibi** resisted Akbar |
| **Bidar** | Barid Shahi | none to remember |
| **Berar** | Imad Shahi | Did **not** join the Talikota alliance |

### Rivalry and the fall
Vijayanagara and the Bahmanis fought almost without a break. The fights were over the Raichur doab, the Krishna-Godavari delta and the horse trade.

In **1565** came the **Battle of Talikota** (also called Rakshasa-Tangadi).

1. The combined Deccan sultanates crushed Vijayanagara.
2. **Rama Raya**, the real ruler (Aravidu), was captured and executed.
3. Hampi was sacked and left empty.

The dynasty lingered from Penukonda and Chandragiri. Nayak kingdoms took over the south.

> **Note:** The **Group of Monuments at Hampi** is a UNESCO World Heritage site (1986). The Vitthala temple stone chariot is its best-known sight.
""",
    tricks=[
        trick("Vijayanagara dynasties: Some Silly Tigers Attack",
              "**S**angama, **S**aluva, **T**uluva, **A**ravidu. Krishnadevaraya sits third, in the **T**uluva line.",
              "Krishnadevaraya belonged to which dynasty of Vijayanagara?",
              ["The order is Sangama, Saluva, Tuluva, Aravidu.", "He is the third."],
              "Tuluva"),
        trick("Deccan five: BiG AB B",
              "**Bi**japur (Adil), **G**olconda (Qutb), **A**hmadnagar (Nizam), **B**idar (Barid), **B**erar (Imad)."),
    ],
    mistakes=[
        mk("Placing Hampi on the Krishna river.", "Hampi is on the **Tungabhadra**."),
        mk("Saying Abdur Razzaq visited Krishnadevaraya.", "He visited **Deva Raya II**. Domingo Paes visited Krishnadevaraya."),
        mk("Putting Charminar in Bijapur.", "**Gol Gumbaz** is in Bijapur. **Charminar** is in Hyderabad (Golconda kingdom)."),
        mk("Saying all five sultanates fought at Talikota.", "**Berar** did not join the Talikota alliance."),
    ],
    revision=[
        "1336: Harihara and Bukka (Sangama) at Hampi. Guru: Vidyaranya.",
        "Dynasties: Sangama, Saluva, Tuluva, Aravidu.",
        "Krishnadevaraya (Tuluva): Raichur 1520, Ashtadiggajas, Allasani Peddana, Amuktamalyada.",
        "Bahmani: Hasan Gangu, 1347, Gulbarga then Bidar. Mahmud Gawan was executed in 1481.",
        "Five sultanates: Bijapur, Ahmadnagar, Golconda, Berar, Bidar.",
        "1565 Talikota: Rama Raya killed, Hampi sacked. Hampi is now a UNESCO site.",
    ],
    patterns=[
        pat("ga-vg-p1", "Vijayanagara: founders and the four dynasties", "very common",
            "Words like 1336, Harihara, Bukka, Vidyaranya, Sangama, Tuluva or Aravidu.",
            ["Founders: Harihara and Bukka, 1336, Hampi on the Tungabhadra.",
             "Dynasty order: Sangama, Saluva, Tuluva, Aravidu.",
             "Krishnadevaraya is Tuluva. Rama Raya is Aravidu."],
            "The dynasty order and the two key names cover most questions.",
            "Vijayanagara was founded on the banks of which river?\n(a) Krishna (b) Godavari (c) Tungabhadra (d) Kaveri",
            ["Hampi, the capital, stands on one river.", "That river is the Tungabhadra."],
            "(c) Tungabhadra"),
        pat("ga-vg-p2", "Krishnadevaraya: conquests, court and classics", "very common",
            "Words like Ashtadiggajas, Amuktamalyada, Raichur 1520, Andhra Bhoja or Peddana.",
            ["Court: Ashtadiggajas, chief poet Allasani Peddana (Manucharitam).",
             "His own Telugu work: Amuktamalyada. Title: Andhra Bhoja.",
             "Battle: Raichur 1520. Visitor: Domingo Paes."],
            "Every fact about this ruler ties to a book, a poet or a battle.",
            "Who was the greatest of the Ashtadiggajas at Krishnadevaraya's court?",
            ["Ashtadiggajas were eight poets.", "The greatest was the author of Manucharitam."],
            "Allasani Peddana"),
        pat("ga-vg-p3", "Bahmani kingdom: founder, capital, five sultanates", "very common",
            "Words like Hasan Gangu, Gulbarga, Bidar, Mahmud Gawan, Adil Shahi or Qutb Shahi.",
            ["Founder: Hasan Gangu, 1347. Capital: Gulbarga, then Bidar.",
             "Recall the five: Bijapur (Adil), Ahmadnagar (Nizam), Golconda (Qutb), Berar (Imad), Bidar (Barid).",
             "Match the dynasty name to the city."],
            "The five dynasty names and cities form one fixed list.",
            "The Bahmani kingdom broke into five sultanates. Which house ruled Golconda?",
            ["Bijapur was Adil Shahi and Ahmadnagar was Nizam Shahi.", "Golconda belonged to the Qutb Shahis."],
            "The Qutb Shahi dynasty"),
        pat("ga-vg-p4", "Hampi and the decisive battles", "common",
            "Words like Talikota, Rakshasa-Tangadi, Rama Raya, Raichur doab, UNESCO or stone chariot.",
            ["The Raichur doab was the long war zone.",
             "Talikota 1565: sultanates beat Vijayanagara. Rama Raya was executed.",
             "Hampi is a UNESCO site. The stone chariot is at the Vitthala temple."],
            "One battle (Talikota) and one man (Rama Raya) end the empire.",
            "Who led Vijayanagara at the Battle of Talikota (1565) and was executed after defeat?",
            ["Talikota was fought in 1565.", "The Aravidu regent Rama Raya was captured and executed."],
            "Rama Raya"),
        pat("ga-vg-p5", "Monuments of the Deccan sultanates", "common",
            "\"Gol Gumbaz is in\", \"Charminar was built by\", \"Chand Bibi\".",
            ["Bijapur: Gol Gumbaz (Muhammad Adil Shah), whispering gallery.",
             "Golconda: Charminar, Hyderabad, 1591 (Muhammad Quli Qutb Shah).",
             "Ahmadnagar: Chand Bibi resisted Akbar."],
            "Each sultanate has one famous monument or person.",
            "The Gol Gumbaz, with its whispering gallery, is in which city?",
            ["Gol Gumbaz was built by Muhammad Adil Shah.", "The Adil Shahis ruled Bijapur."],
            "Bijapur"),
        pat("ga-vg-p6", "Foreign visitors to Vijayanagara", "common",
            "\"Who visited the court of...\" with names such as Razzaq, Paes, Conti or Nuniz.",
            ["Conti (Italy): Deva Raya I.",
             "Abdur Razzaq (Persia): Deva Raya II.",
             "Paes (Portugal): Krishnadevaraya. Nuniz (Portugal): Achyuta Raya."],
            "Each traveller pairs with one ruler, so the country also helps.",
            "Which foreign visitor came as a Persian envoy to Deva Raya II?",
            ["Persia narrows the list.", "The Timurid envoy was Abdur Razzaq."],
            "Abdur Razzaq"),
    ],
)

# ---------------------------------------------------------------- mughals
S["mughals"] = dict(
    concept=(
        "The Mughal empire began with Babur's win at Panipat in 1526. Sher Shah Suri broke it for a few years, "
        "then Akbar built it up. Shah Jahan gave it great buildings, and Aurangzeb's long wars weakened it. "
        "Exams ask which emperor did what, plus the key battles and revenue terms."
    ),
    notes=r"""### Babur and Humayun (1526-1556)
| Ruler | Years | Key facts |
|---|---|---|
| **Babur** | 1526-30 | **First Battle of Panipat** (21 April 1526) against **Ibrahim Lodi**. First use of field guns in India. Also **Khanwa** (1527, against **Rana Sanga**), **Chanderi** (1528, Medini Rai) and **Ghaghra** (1529). Wrote the *Baburnama* (*Tuzuk-i-Baburi*) in **Turki**. |
| **Humayun** | 1530-40, 1555-56 | Lost to Sher Shah at **Chausa (1539)** and **Kannauj / Bilgram (1540)**. Won Delhi back in 1555. Died falling from the stairs of his library, **Sher Mandal**. |

Babur was a Chagatai Timurid from Fergana. At Panipat he used artillery and the *tulughma* (encircling) tactic. Humayun wandered for 15 years and returned with help from Persia.

### Sher Shah Suri (1540-1545)
He was an Afghan from Sasaram. He ruled well in only five years.

- Issued the silver **rupiya** and the copper **dam**.
- Rebuilt the **Grand Trunk Road** from Sonargaon in Bengal to Peshawar, with **sarais** (rest houses) at stages.
- Set up land measurement, **patta** (title deed) and **qabuliyat** (agreement deed).
- Ran a spy-based administration.
- His tomb is at **Sasaram (Bihar)**. He died at **Kalinjar**.

> **Watch:** The rupiya came from **Sher Shah**, not Akbar.

### Akbar (1556-1605)
**Bairam Khan**, the regent, won the **Second Battle of Panipat (1556)** against **Hemu**. Then Akbar acted on many fronts.

- **Conquests:** Malwa, Chittor (1568), Ranthambhor, Gujarat and Bengal. **Buland Darwaza** marks the Gujarat win.
- **Haldighati (1576):** Mughal army under **Man Singh** against **Maharana Pratap**.
- **Rajput policy:** alliances and marriages with Amber. Man Singh and Todar Mal served at high rank.
- **Tolerance:** abolished the pilgrim tax and **jizya (1564)**.
- **Religion:** **Ibadat Khana** at Fatehpur Sikri (1575). **Din-i-Ilahi** (1582), a mixed order.
- **Court:** the **Navaratna** circle included Birbal, Todar Mal, Abul Fazl, Faizi, Tansen and Man Singh.

> **Tip:** Ibadat Khana comes first (**1575**). Din-i-Ilahi follows (**1582**).

### Akbar's system
| Term | Meaning |
|---|---|
| **Mansab** | Rank fixed by **zat** (personal rank) and **sawar** (cavalry count) |
| **Jagir** | Revenue assignment given to a mansabdar instead of salary |
| **Zabti / Dahsala** | Revenue system of **Raja Todar Mal**, based on a 10-year average |
| **Subah / Sarkar / Pargana** | Province / district / sub-district |
| **Diwan / Mir Bakshi** | Finance / military pay and intelligence |

### Jahangir, Shah Jahan, Aurangzeb
| Ruler | Years | Key facts |
|---|---|---|
| **Jahangir** | 1605-27 | **Chain of justice** (Zanjir-i-Adl). **Nur Jahan** ran the court. English envoys **Hawkins (1608)** and **Sir Thomas Roe (1615)**. Executed **Guru Arjan Dev (1606)**. *Tuzuk-i-Jahangiri*. |
| **Shah Jahan** | 1628-58 | **Taj Mahal** for Mumtaz Mahal. **Red Fort** and **Jama Masjid**, Delhi (Shahjahanabad). **Peacock Throne**. |
| **Aurangzeb** | 1658-1707 | Re-imposed **jizya (1679)**. Executed **Guru Tegh Bahadur (1675)**. Fought the Marathas in the Deccan for 25 years. Died at Ahmednagar, buried at **Khuldabad**. |

### Buildings in pairs
- **Humayun's Tomb** (Delhi): first garden-tomb on the subcontinent.
- **Itimad-ud-Daulah** (Agra): built by **Nur Jahan** for her father. Early pietra dura in white marble.
- **Fatehpur Sikri:** Akbar's city, with the Panch Mahal and Jodha Bai palace.

### Later Mughals
Later kings were puppets. The **Sayyid brothers** made and unmade them. **Nadir Shah** of Persia invaded in **1739** (Battle of **Karnal**) under **Muhammad Shah "Rangila"**. He took the **Peacock Throne** and the **Koh-i-Noor**. **Ahmad Shah Abdali** raided again and again.
""",
    tricks=[
        trick("Mughal order: Bahut Hi Accha Jalebi Shahi Aur",
              "**B**abur, **H**umayun, **A**kbar, **J**ahangir, **S**hah Jahan, **A**urangzeb. Sher Shah sits between Humayun's two reigns (1540-55).",
              "Which ruler came between Humayun's two reigns?",
              ["Humayun lost in 1540 and returned in 1555.", "Sher Shah ruled in between."],
              "Sher Shah Suri"),
        trick("Three Panipats: 26, 56, 61",
              "**1526** Babur beats Ibrahim Lodi. **1556** Akbar's side (Bairam Khan) beats Hemu. **1761** Ahmad Shah Abdali beats the Marathas."),
    ],
    mistakes=[
        mk("Crediting Akbar with the rupiya.", "**Sher Shah** issued the silver rupiya and copper dam."),
        mk("Swapping Din-i-Ilahi and Ibadat Khana dates.", "Ibadat Khana = **1575**. Din-i-Ilahi = **1582**."),
        mk("Saying Akbar himself led at Haldighati.", "The Mughal commander was **Man Singh**."),
        mk("Giving Itimad-ud-Daulah to Shah Jahan.", "**Nur Jahan** built it. The Taj Mahal is Shah Jahan's."),
        mk("Placing Chausa and Kannauj under Babur.", "Both are **Humayun's** defeats by Sher Shah (1539, 1540)."),
    ],
    revision=[
        "Babur: Panipat 1526, Khanwa 1527. Baburnama in Turki. Humayun: Chausa 1539, Kannauj 1540.",
        "Sher Shah: rupiya, dam, Grand Trunk Road with sarais, patta and qabuliyat, tomb at Sasaram.",
        "Akbar: Second Panipat 1556, jizya abolished 1564, Ibadat Khana 1575, Din-i-Ilahi 1582.",
        "Todar Mal: dahsala (zabti). Mansab has zat and sawar.",
        "Jahangir: chain of justice, Roe 1615. Shah Jahan: Peacock Throne, Taj. Aurangzeb: jizya 1679, Tegh Bahadur 1675.",
        "1739: Nadir Shah at Karnal, under Muhammad Shah Rangila.",
    ],
    patterns=[
        pat("ga-mu-p1", "Babur, Humayun and Sher Shah: battles and reforms", "very common",
            "Words like Panipat 1526, Khanwa, Chausa, Kannauj, rupiya, Grand Trunk Road or Sasaram.",
            ["Babur: Panipat 1526 (Lodi), Khanwa 1527 (Rana Sanga).",
             "Humayun lost to Sher Shah at Chausa 1539 and Kannauj 1540.",
             "Sher Shah: rupiya, dam, GT Road with sarais, patta-qabuliyat."],
            "The battles form a chain, and Sher Shah's reforms sit between Humayun's two reigns.",
            "The Grand Trunk Road revived by Sher Shah connected the north-west with:",
            ["It ran to Peshawar in the north-west.", "The other end was Sonargaon in Bengal."],
            "Sonargaon in Bengal"),
        pat("ga-mu-p2", "Akbar: conquests, administration and Din-i-Ilahi", "very common",
            "Words like Hemu, dahsala, zat, sawar, Ibadat Khana, Din-i-Ilahi, jizya or Todar Mal.",
            ["Second Panipat 1556: Bairam Khan beat Hemu.",
             "Revenue: Todar Mal's dahsala. Ranks: zat and sawar.",
             "Ideas: Din-i-Ilahi 1582, Ibadat Khana 1575, jizya abolished 1564."],
            "Each Akbar reform has one name and one year, and options swap them.",
            "Who devised the dahsala (zabti) revenue system of Akbar's reign?",
            ["Dahsala means ten-year average.", "Akbar's finance minister set it."],
            "Raja Todar Mal"),
        pat("ga-mu-p3", "Jahangir, Shah Jahan and Aurangzeb", "very common",
            "Words like chain of justice, Roe, Peacock Throne, Taj Mahal, jizya 1679 or Tegh Bahadur.",
            ["Jahangir: chain of justice, Roe 1615, Nur Jahan, Guru Arjan 1606.",
             "Shah Jahan: Peacock Throne, Taj Mahal, Red Fort, Jama Masjid.",
             "Aurangzeb: jizya 1679, Guru Tegh Bahadur 1675, Deccan wars."],
            "Each of the three emperors has a clear set of signature facts.",
            "Who came as ambassador of England's James I to Jahangir's court in 1615?",
            ["Hawkins came earlier, in 1608.", "The 1615 envoy was Sir Thomas Roe."],
            "Sir Thomas Roe"),
        pat("ga-mu-p4", "Later Mughals and the empire's decline", "common",
            "Words like Nadir Shah, Karnal, Rangila, Sayyid brothers, Koh-i-Noor or Abdali.",
            ["Nadir Shah, 1739: won at Karnal, took Koh-i-Noor and Peacock Throne.",
             "The ruler then was Muhammad Shah Rangila.",
             "Sayyid brothers were king-makers. Abdali raided repeatedly."],
            "One invasion (1739) and one ruler (Muhammad Shah) answer most questions.",
            "Nadir Shah invaded India in 1739 during the reign of:",
            ["Battle of Karnal was in 1739.", "The Mughal king was Muhammad Shah Rangila."],
            "Muhammad Shah Rangila"),
        pat("ga-mu-p5", "Mughal administration terms", "common",
            "Words like mansab, zat, sawar, jagir, subah, sarkar, pargana or Mir Bakshi.",
            ["Mansab = rank. Zat = personal rank. Sawar = cavalry count.",
             "Jagir = revenue assignment instead of salary.",
             "Order of areas: subah (province), sarkar (district), pargana (sub-district)."],
            "The terms come in small sets, and the options mix their meanings.",
            "In the Mughal mansabdari system, \"sawar\" stood for:",
            ["Zat was personal rank.", "Sawar was the number of cavalry."],
            "The cavalry count"),
        pat("ga-mu-p6", "Buildings and their builders", "common",
            "\"Taj Mahal\", \"Itimad-ud-Daulah\", \"Buland Darwaza\", \"Humayun's Tomb\", \"Sher Mandal\".",
            ["Shah Jahan: Taj Mahal, Red Fort, Jama Masjid.",
             "Nur Jahan: Itimad-ud-Daulah. Akbar: Fatehpur Sikri, Buland Darwaza.",
             "Sasaram tomb: Sher Shah. Humayun's Tomb: first garden-tomb."],
            "Each monument has one patron, and the options swap them.",
            "Itimad-ud-Daulah at Agra was built by Nur Jahan for:",
            ["It honours her father.", "It shows early pietra dura in white marble."],
            "Her father"),
    ],
)

# ---------------------------------------------------------------- marathas-sikhs
S["marathas-sikhs"] = dict(
    concept=(
        "Shivaji built the Maratha state in the 1600s with hill forts and fast cavalry. "
        "After him the Peshwas led a confederacy until the British ended it in 1818. "
        "The ten Sikh Gurus shaped the Sikh faith, and Ranjit Singh built a Sikh kingdom at Lahore."
    ),
    notes=r"""### Shivaji builds a kingdom
**Shivaji** was born in **1630** at **Shivneri**. His father was Shahaji and his mother **Jijabai**. He built a state out of Bijapur's Deccan land with hill forts and light cavalry.

| Year | Event |
|---|---|
| **1659** | Killed Bijapur general **Afzal Khan** at **Pratapgarh** |
| **1665** | **Treaty of Purandar** with **Raja Jai Singh**. He gave up 23 forts. |
| **1666** | Visit to Agra and escape |
| **1674** | Crowned **Chhatrapati** at **Raigad**. Gaga Bhatt led the rituals. |

Forts of note: Torna, Rajgad, Sinhagad. **Tanaji Malusare** fell at Sinhagad. Shivaji also raided Surat and humbled Shaista Khan at Pune.

Revenue used **kathi** assessment. The army was paid in cash. Two taxes are asked often: **chauth** (**1/4**, 25% of revenue) and **sardeshmukhi** (an extra **10%**).

### Shivaji's Ashtapradhan
| Post | Portfolio |
|---|---|
| **Peshwa** | Prime Minister |
| **Amatya** (Majumdar) | Finance and accounts |
| **Mantri** (Waqia-navis) | Daily records, the king's diary |
| **Sachiv** (Shurunavis) | Royal letters |
| **Sumant** (Dabir) | **Foreign affairs** |
| **Senapati** (Sar-i-Naubat) | Army |
| **Panditrao** | Religious matters |
| **Nyayadhish** | Justice |

> **Tip:** Chauth = **Ch**aar ana in a rupee (1/4). Sardeshmukhi is 10%.

### The Peshwas and the confederacy
- **Balaji Vishwanath** was the first Peshwa of the Bhat family (1713).
- **Baji Rao I** (1720-40) was the greatest cavalry general. He took Maratha arms to Malwa, Bundelkhand and Delhi's gates.
- **Balaji Baji Rao** (Nana Saheb) saw the **Third Battle of Panipat (14 January 1761)**. **Ahmad Shah Abdali** beat the Marathas under **Sadashivrao Bhau**.

After that, power lay with the confederacy houses under the Peshwa at Pune.

| House | Seat |
|---|---|
| **Scindia** | Gwalior |
| **Holkar** | Indore |
| **Gaekwad** | Baroda |
| **Bhonsle** | Nagpur |

Three Anglo-Maratha wars followed. The **Treaty of Salbai (1782)** ended the first. **Baji Rao II** signed the **Treaty of Bassein (1802)**, a subsidiary alliance, and the second war began. The third war (1817-18) ended Maratha power.

### The ten Sikh Gurus
| # | Guru | Remember for |
|---|---|---|
| 1 | **Nanak** | Founder. Born 1469 at **Talwandi** (Nankana Sahib). One God, **langar**, honest work. |
| 2 | **Angad** | Standardised the **Gurmukhi** script |
| 3 | **Amar Das** | Manji system; strengthened langar |
| 4 | **Ram Das** | Founded **Amritsar** (Ramdaspur) |
| 5 | **Arjan Dev** | Compiled the **Adi Granth (1604)**. Built Harmandir Sahib. Executed by **Jahangir (1606)**. |
| 6 | **Hargobind** | **Akal Takht**; Miri-Piri, the armed saint |
| 7 | **Har Rai** | none to remember |
| 8 | **Har Krishan** | Youngest guru |
| 9 | **Tegh Bahadur** | Executed by **Aurangzeb (1675)** in Delhi |
| 10 | **Gobind Singh** | Founded the **Khalsa (1699)** at **Anandpur Sahib** on Baisakhi. Declared the Granth the eternal Guru. |

> **Watch:** Arjan Dev compiled the Adi Granth. Gobind Singh founded the Khalsa. Arjan died under Jahangir, Tegh Bahadur under Aurangzeb.

### After the tenth Guru
**Banda Bahadur** carried on the Khalsa fight and was executed in **1716**. Sikh **misls** (confederacies) followed. **Maharaja Ranjit Singh** of the **Sukerchakia misl** took **Lahore in 1799**. He ruled Punjab until 1839 and was called **Sher-e-Punjab**. The Khalsa's five K's are kesh, kangha, kara, kachchha and kirpan.
""",
    tricks=[
        trick("Guru order: Nana Aur Amar Ram Arjun, Har-Har-Har Tegh Gobind",
              "**N**anak, **A**ngad, **Amar** Das, **Ram** Das, **Arjan**, then the three Hars (Har**gobind**, **Har** Rai, **Har** Krishan), then **Tegh** Bahadur, then **Gobind** Singh.",
              "Who was the ninth Sikh Guru?",
              ["The three Hars are 6, 7 and 8.", "Tegh Bahadur comes next."],
              "Guru Tegh Bahadur"),
        trick("Chauth vs Sardeshmukhi",
              "**Ch**auth = **Ch**aar ana in the rupee (1/4). Sardeshmukhi = 10%, the tenth claimed by the hereditary head."),
    ],
    mistakes=[
        mk("Giving the Adi Granth to Guru Gobind Singh.", "**Guru Arjan Dev** compiled it. Gobind Singh founded the **Khalsa**."),
        mk("Saying Jahangir executed Guru Tegh Bahadur.", "Jahangir executed **Arjan Dev** (1606). **Aurangzeb** executed Tegh Bahadur (1675)."),
        mk("Naming Nadir Shah as the winner at Third Panipat.", "The winner was **Ahmad Shah Abdali**. Nadir Shah invaded in 1739."),
        mk("Mixing chauth and sardeshmukhi.", "Chauth is **25%**. Sardeshmukhi is an extra **10%**."),
    ],
    revision=[
        "Shivaji: Pratapgarh 1659, Purandar 1665, Agra escape 1666, crowned at Raigad 1674.",
        "Ashtapradhan: Peshwa first of eight. Sumant handles foreign affairs.",
        "Peshwas: Balaji Vishwanath, Baji Rao I, Balaji Baji Rao (Panipat 1761). Salbai 1782, Bassein 1802.",
        "Houses: Scindia (Gwalior), Holkar (Indore), Gaekwad (Baroda), Bhonsle (Nagpur).",
        "Gurus: Nanak (Talwandi), Arjan (Adi Granth, executed 1606), Tegh Bahadur (1675), Gobind (Khalsa 1699).",
        "After Gobind: Banda Bahadur (1716), misls, Ranjit Singh (Lahore 1799).",
    ],
    patterns=[
        pat("ga-mr-p1", "Shivaji: conquests, treaty, coronation, Ashtapradhan", "very common",
            "Words like Afzal Khan, Purandar, Raigad, Chhatrapati, Ashtapradhan or Sumant.",
            ["Chain: Pratapgarh 1659, Purandar 1665, Agra 1666, Raigad 1674.",
             "Purandar was with Jai Singh (23 forts).",
             "Ashtapradhan: Peshwa, Senapati, Amatya, Sumant (foreign), Nyayadhish."],
            "The four dates make one story, and each has one place.",
            "Shivaji was crowned Chhatrapati in 1674 at:\n(a) Pratapgarh (b) Raigad (c) Purandar (d) Shivneri",
            ["Shivneri was his birthplace.", "Pratapgarh was the Afzal Khan fight and Purandar the treaty.", "The coronation was at Raigad."],
            "(b) Raigad"),
        pat("ga-mr-p2", "Peshwas, confederacy houses and Anglo-Maratha wars", "very common",
            "Words like Balaji Vishwanath, Baji Rao, Scindia, Holkar, Salbai or Bassein.",
            ["Peshwa order: Balaji Vishwanath, Baji Rao I, Balaji Baji Rao.",
             "Houses: Scindia-Gwalior, Holkar-Indore, Gaekwad-Baroda, Bhonsle-Nagpur.",
             "Wars: Salbai 1782 ends the first; Bassein 1802 starts the second; 1818 ends the third."],
            "Names, seats and treaties each come as a fixed set.",
            "Which Maratha confederacy house was based at Gwalior?",
            ["Holkar was at Indore.", "Gaekwad was at Baroda.", "Gwalior belonged to the Scindias."],
            "The Scindias"),
        pat("ga-mr-p3", "Sikh Gurus in order and their landmarks", "very common",
            "\"Which Guru...\" with words like Gurmukhi, Amritsar, Adi Granth, Miri-Piri or Khalsa.",
            ["Recall the list by number.",
             "Nanak-Talwandi, Angad-Gurmukhi, Ram Das-Amritsar, Arjan-Adi Granth, Hargobind-Miri-Piri.",
             "Tegh Bahadur executed 1675; Gobind Singh Khalsa 1699."],
            "Each Guru has one landmark, and the number in the list gives the order.",
            "Who compiled the Adi Granth, the original Sikh scripture?",
            ["It was compiled in 1604.", "The compiler was the fifth Guru, executed in 1606."],
            "Guru Arjan Dev"),
        pat("ga-mr-p4", "After the tenth Guru: Banda Bahadur to Ranjit Singh", "common",
            "Words like Banda Bahadur, misl, Sukerchakia, Lahore 1799 or five K's.",
            ["Banda Bahadur led the Khalsa after 1708. He was executed in 1716.",
             "Misls were Khalsa confederacies.",
             "Ranjit Singh of the Sukerchakia misl took Lahore in 1799."],
            "The chain Banda, misls, Ranjit Singh follows the tenth Guru in order.",
            "Maharaja Ranjit Singh belonged to which Sikh misl?",
            ["He captured Lahore in 1799.", "His misl was the Sukerchakia."],
            "The Sukerchakia misl"),
        pat("ga-mr-p5", "Third Battle of Panipat (1761)", "common",
            "\"Third Panipat\", \"1761\", \"Sadashivrao Bhau\", \"Ahmad Shah Abdali\".",
            ["Date: 14 January 1761.",
             "Winner: Ahmad Shah Abdali. Loser: the Marathas under Sadashivrao Bhau.",
             "The Peshwa at that time was Balaji Baji Rao."],
            "A few names and one date solve every question on this battle.",
            "In the Third Battle of Panipat (1761), the Marathas were defeated by:",
            ["Nadir Shah invaded in 1739, so he is wrong.", "The winner was Ahmad Shah Abdali."],
            "Ahmad Shah Abdali"),
        pat("ga-mr-p6", "Revenue terms and posts of the Marathas", "occasional",
            "\"Chauth\", \"Sardeshmukhi\", \"Sumant\", \"Amatya\", \"Nyayadhish\".",
            ["Chauth is 25%. Sardeshmukhi is an extra 10%.",
             "Peshwa: prime minister. Amatya: finance. Sumant: foreign affairs.",
             "Senapati: army. Nyayadhish: justice."],
            "Each term has one number or one portfolio.",
            "In the Ashtapradhan, which minister looked after foreign affairs?",
            ["Peshwa was Prime Minister.", "Sumant (Dabir) handled foreign affairs."],
            "Sumant"),
    ],
)

# ---------------------------------------------------------------- bhakti-sufi
S["bhakti-sufi"] = dict(
    concept=(
        "The Bhakti and Sufi movements gave the medieval period a religion of love and devotion. "
        "Saints sang in the people's own languages and quietly weakened caste barriers. "
        "Exams ask which saint belongs to which region, work, language or Sufi order."
    ),
    notes=r"""### Two roads to the same God
Bhakti (Hindu devotion) and Sufism (Islamic mysticism) both answered heavy ritual with love and devotion. Both used the people's languages. Both quietly attacked caste.

### Bhakti in the south first
The **Alvars** (devotees of **Vishnu**) and the **Nayanars** (devotees of **Shiva**) sang between the 6th and 9th centuries.

- The **Tevaram** hymns belong to the Nayanars (Appar, Sambandar, Sundarar).
- **Andal** is the woman Alvar.

Four schools of philosophy are often asked:

| Teacher | School |
|---|---|
| **Shankaracharya** | **Advaita** (non-dualism) |
| **Ramanuja** | **Vishishtadvaita** (qualified non-dualism) |
| **Madhvacharya** | **Dvaita** (dualism) |
| **Vallabhacharya** | **Shuddhadvaita** |

**Basavanna** (Karnataka, 12th century) began the **Virashaiva / Lingayat** movement and its *vachanas*.

> **Tip:** "RaVi MaD": **Ra**manuja is **Vi**shishtadvaita. **Ma**dhva is **D**vaita.

### North and west India
| Saint | Region | Remember for |
|---|---|---|
| **Ramananda** | North India (Varanasi) | Opened bhakti to all castes. Guru of **Kabir** and **Ravidas**. |
| **Kabir** | Varanasi | Weaver. Sayings in the ***Bijak***. Attacked idol worship and ritual on both sides. |
| **Guru Nanak** | Punjab | Founded what became Sikhism. |
| **Chaitanya** | Bengal and Odisha (Puri) | **Gaudiya Vaishnavism**. **Sankirtan**. |
| **Tulsidas** | Uttar Pradesh | ***Ramcharitmanas*** in **Awadhi** |
| **Surdas** | Braj | ***Sursagar*** on Krishna, in **Braj Bhasha** |
| **Mirabai** | Rajasthan (Mewar) | Krishna bhajans |
| **Jnaneshwar** | Maharashtra | ***Jnaneshwari***, a Marathi commentary on the Gita |
| **Namdev, Tukaram** | Maharashtra | **Warkari** tradition. Tukaram's **abhangas**. Worship of **Vithoba at Pandharpur**. |
| **Sankardeva** | Assam | **Ekasarana dharma**. Set up **sattras** and namghars. |

> **Watch:** Ramcharitmanas is in **Awadhi**, not Sanskrit or Braj.

### Sufism: Islamic mysticism
Sufi orders are called **silsilas**, meaning "chains" of teacher to student. The bond is **pir-murid**. Practice includes **zikr** (recitation) and **sama** (musical gatherings). Sama is the root of **qawwali**.

| Order | Key saint | Centre and note |
|---|---|---|
| **Chishti** | **Khwaja Moinuddin Chishti** (came c. 1192) | **Ajmer** |
| Chishti | **Qutbuddin Bakhtiyar Kaki** | Delhi. The Qutub Minar is named after him. |
| Chishti | **Baba Farid** | Pakpattan. His verses are in the **Adi Granth**. |
| Chishti | **Nizamuddin Auliya** | Delhi. Disciple: **Amir Khusrau**. |
| **Suhrawardi** | **Bahauddin Zakariya** | **Multan**. Accepted state service. |
| **Naqshbandi** | **Shaikh Ahmad Sirhindi** | Revivalist. Opposed Akbar's liberal policies. |
| **Qadiri** | none to remember | Oldest order. Later linked to Dara Shikoh's leanings. |

The Chishtis stayed away from the court and served all communities. Saints' tombs became **dargahs**, centres of pilgrimage (ziyarat).

**Amir Khusrau** was called *Tuti-i-Hind* ("Parrot of India"). He is credited with shaping qawwali. He wrote in Persian and Hindavi.

### What they changed
- Local languages grew: the Bijak, the Manas, the abhangas.
- Caste lines weakened inside devotional groups.
- Shrines such as Ajmer, Pandharpur and the dargahs of Delhi became shared spaces.
""",
    tricks=[
        trick("Philosophy trio: RaVi MaD",
              "**Ra**manuja gives **Vi**shishtadvaita. **Ma**dhva gives **D**vaita. Shankara gives Advaita.",
              "Dvaita philosophy was taught by:",
              ["MaD: Madhva gives Dvaita.", "Ramanuja is Vishishtadvaita."],
              "Madhvacharya"),
        trick("Language of the epic",
              "Tulsidas = **A**wadhi (**A** for Ayodhya's Ram). Surdas = **B**raj (**B**al-Krishna)."),
    ],
    mistakes=[
        mk("Calling the Ramcharitmanas a Sanskrit or Braj work.", "It is in **Awadhi**."),
        mk("Placing Moinuddin Chishti in Delhi.", "Moinuddin Chishti = **Ajmer**. Nizamuddin Auliya = **Delhi**."),
        mk("Saying Sankardeva is from Bengal.", "**Sankardeva** is from **Assam**. **Chaitanya** is from Bengal."),
        mk("Thinking all Sufi orders avoided the court.", "The **Suhrawardis** accepted state service. The Chishtis stayed away."),
    ],
    revision=[
        "Alvars worship Vishnu. Nayanars worship Shiva. Tevaram is Nayanar hymns. Andal is the woman Alvar.",
        "Advaita: Shankara. Vishishtadvaita: Ramanuja. Dvaita: Madhva.",
        "Kabir: Bijak. Tulsidas: Awadhi. Surdas: Braj. Tukaram: Marathi abhangas (Warkari, Vithoba of Pandharpur).",
        "Chishti: Moinuddin, then Nizamuddin. Suhrawardi: Bahauddin Zakariya. Naqshbandi: Sirhindi. Qadiri.",
        "Sama is music. Pir-murid is teacher and student. A dargah is a tomb-shrine.",
    ],
    patterns=[
        pat("ga-bs-p1", "Alvars, Nayanars and the Acharyas", "very common",
            "Words like Alvar, Nayanar, Tevaram, Andal, Advaita, Vishishtadvaita or Dvaita.",
            ["Alvars are for Vishnu. Nayanars are for Shiva.",
             "Tevaram belongs to the Nayanars. Andal is the woman Alvar.",
             "Schools: Shankara-Advaita, Ramanuja-Vishishtadvaita, Madhva-Dvaita, Vallabha-Shuddhadvaita."],
            "Two pairs, Alvar-Vishnu and Nayanar-Shiva, plus four schools, cover this whole area.",
            "The Alvars of south India were devotees of:\n(a) Shiva (b) Vishnu (c) Durga (d) Surya",
            ["Nayanars were the Shiva devotees.", "Alvars were their Vishnu counterparts."],
            "(b) Vishnu"),
        pat("ga-bs-p2", "North Indian saints: sect, language and work", "very common",
            "A saint matched to a language, a book or a place: Tulsidas, Sur, Tukaram, Chaitanya, Kabir.",
            ["Language anchors: Tulsidas-Awadhi, Sur-Braj, Tukaram and Namdev-Marathi, Chaitanya-Bengal.",
             "Works: Kabir-Bijak, Tulsidas-Ramcharitmanas, Sur-Sursagar.",
             "Sect: Varkari means Vithoba of Pandharpur."],
            "Every saint carries one work or language, which the options test.",
            "Tukaram's abhangas are composed in which language?",
            ["Tukaram belongs to the Varkari sect of Pandharpur.", "Varkari saints sang in Marathi."],
            "Marathi"),
        pat("ga-bs-p3", "Sufi silsilas, founders and saints", "very common",
            "Words like Chishti, Suhrawardi, Naqshbandi, Qadiri, Ajmer, Multan or Nizamuddin Auliya.",
            ["Chishti chain: Moinuddin (Ajmer), Qutbuddin Bakhtiyar Kaki, Baba Farid, Nizamuddin Auliya.",
             "Suhrawardi: Bahauddin Zakariya (Multan). Naqshbandi: Ahmad Sirhindi. Qadiri: oldest.",
             "Terms: silsila = chain, sama = music, dargah = tomb-shrine."],
            "Order, saint and city come together in one line each.",
            "The Suhrawardi silsila in India is linked with which saint?",
            ["Chishti saints avoided state service.", "The Suhrawardi saint of Multan was Bahauddin Zakariya."],
            "Bahauddin Zakariya"),
        pat("ga-bs-p4", "Shared features of Bhakti and Sufi movements", "common",
            "\"Which is common to both movements?\" or a statement question about them.",
            ["List the common ground: devotion above ritual, local languages, guru at the centre.",
             "Add: criticism of caste and equality in devotion.",
             "Do not accept extreme claims such as 'both opposed all temples'."],
            "Statement questions test whether you judge each claim, not a slogan.",
            "Which feature was common to both the Bhakti and Sufi movements?",
            ["Both used the people's languages.", "Both offered a devotional path open to all castes and communities."],
            "Use of local languages and a devotional path open to all"),
        pat("ga-bs-p5", "Regional saints: place and work", "common",
            "\"Which saint founded Ekasarana / Lingayat / Gaudiya...?\" or a saint-region match.",
            ["Sankardeva: Assam, Ekasarana dharma, sattras.",
             "Basavanna: Karnataka, Lingayat, vachanas.",
             "Chaitanya: Bengal-Odisha, Gaudiya Vaishnavism. Jnaneshwar: Maharashtra, Jnaneshwari."],
            "Each saint has a home region, which removes most wrong options.",
            "Ekasarana dharma, with its sattras and namghars, was spread in Assam by:",
            ["Sattras are Vaishnava monastery-centres.", "The Assam saint is Sankardeva."],
            "Sankardeva"),
    ],
)

# ---------------------------------------------------------------- sources-travellers
S["sources-travellers"] = dict(
    concept=(
        "Our knowledge of medieval India comes from court chronicles, memoirs, poems and the reports of foreign travellers. "
        "Exams ask which author wrote which book, and which traveller visited which ruler. "
        "Learn each book with its author, and each traveller with his country and ruler."
    ),
    notes=r"""### Chronicles of the court
| Book | Author | Note |
|---|---|---|
| *Kitab-ul-Hind (Tahqiq-i-Hind)* | **Al-Biruni** | India under Mahmud of Ghazni |
| *Tabaqat-i-Nasiri* | **Minhaj-us-Siraj** | Dedicated to Nasiruddin Mahmud |
| *Tarikh-i-Firoz Shahi* | **Ziauddin Barani** | Sultanate history. He also wrote *Fatawa-i-Jahandari*, advice to kings. |
| *Rihla* | **Ibn Battuta** | Travels, including Muhammad bin Tughlaq's India |
| *Padmavat* | **Malik Muhammad Jayasi** | Awadhi epic (1540) |
| *Humayun-nama* | **Gulbadan Begum** | Babur's daughter |
| *Akbarnama* and *Ain-i-Akbari* | **Abul Fazl** | Ain is the third volume of the Akbarnama |
| *Muntakhab-ut-Tawarikh* | **Abdul Qadir Badauni** | Critical of Akbar |
| *Razmnama* | Translation team under Akbar | Persian Mahabharata |
| *Padshahnama* (*Badshahnama*) | **Abdul Hamid Lahori** | Shah Jahan's reign |
| *Majma-ul-Bahrain*, *Sirr-i-Akbar* | **Dara Shikoh** | Sufism and Vedanta meet; Persian Upanishads |

Other writers: **Amir Khusrau**, the "Parrot of India", wrote in Persian (*Khamsa*, *Tughlaq Nama*). **Isami** wrote *Futuh-us-Salatin*. **Babur** wrote the *Baburnama* in Turkish. **Jahangir** wrote the *Tuzuk-i-Jahangiri*.

> **Tip:** **Abul** Fazl wrote the praising Akbarnama and Ain. **Badauni** wrote the **b**itter, critical *Muntakhab*.

### The travellers' ladder
| Traveller | From | Visited | Note |
|---|---|---|---|
| **Al-Biruni** | Central Asia (Khwarazm) | Mahmud of Ghazni | *Kitab-ul-Hind* |
| **Marco Polo** | Venice | Pandya coast (1290s) | Pearl fishery accounts |
| **Ibn Battuta** | Morocco | Muhammad bin Tughlaq's Delhi | Qazi of Delhi. Book: *Rihla*. |
| **Nicolo Conti** | Venice | Vijayanagara (Deva Raya I) | |
| **Abdur Razzaq** | Persia (Timurid) | Vijayanagara (Deva Raya II) | Hampi's splendour |
| **Athanasius Nikitin** | Russia | Bahmani kingdom | *Voyage to India* |
| **Domingo Paes, Duarte Barbosa** | Portugal | Krishnadevaraya's court | Bazaars of Hampi |
| **Ralph Fitch** | England | Akbar's reign (1583) | First English merchant |
| **Hawkins, Sir Thomas Roe** | England | Jahangir (1608, 1615) | Roe = envoy of James I |
| **Bernier** | France | Shah Jahan and Aurangzeb | |
| **Tavernier** | France | Shah Jahan | Diamond merchant |
| **Manucci** | Italy | Mughal India (17th century) | |

> **Watch:** Ibn Battuta was **Moroccan**, not Persian.

### Vernacular classics
The medieval literary map is many-languaged.

- **Padmavat** by Jayasi: an Awadhi Sufi romance of Alauddin and Padmini.
- **Bijak, Manas, abhangas:** Kabir, Tulsidas (Awadhi), Sur (Braj) and Tukaram (Marathi).
- **Amuktamalyada:** Krishnadevaraya's Telugu classic.

Each book is also a source. The *Padmavat* shows Sufi storytelling. The *Ain* records prices and rules. The *Rihla* shows daily life in Delhi under Muhammad bin Tughlaq.

### What each source is best for
- **Administration:** the **Ain-i-Akbari** (mansabs, provinces, prices).
- **Daily life and courts:** Ibn Battuta's *Rihla*, Paes on Hampi, Bernier on Delhi.
- **Trade:** Tavernier on diamonds, Marco Polo on pearls, Nikitin on Bahmani markets.
- **Court politics:** Barani on the Tughlaqs. Badauni against Abul Fazl's praise of Akbar.

> **Note:** Court histories praise their patrons. Cross-check them with coins, inscriptions and foreign travellers.
""",
    tricks=[
        trick("Mughal chroniclers: Abul praises, Badauni bites",
              "**Abul** Fazl wrote the official, praising *Akbarnama* and *Ain*. **Badauni** wrote the **b**itter, critical *Muntakhab-ut-Tawarikh*.",
              "Which historian wrote a critical account of Akbar's religious policy?",
              ["Critical and bitter points to Badauni.", "His book is Muntakhab-ut-Tawarikh."],
              "Abdul Qadir Badauni"),
        trick("Travellers by century",
              "11th Al-Biruni, 13th Marco Polo, 14th Ibn Battuta, 15th Conti and Abdur Razzaq, 16th Paes and Nuniz, 17th Hawkins, Roe, Bernier and Tavernier."),
    ],
    mistakes=[
        mk("Calling Ibn Battuta a Persian traveller.", "He was **Moroccan** and served as qazi of Delhi."),
        mk("Saying Humayun wrote the Humayun-nama.", "**Gulbadan Begum**, Babur's daughter, wrote it."),
        mk("Treating the Ain-i-Akbari as a separate book.", "It is the **third volume** of the Akbarnama."),
        mk("Thinking Al-Biruni came with Muhammad Ghori.", "He came with **Mahmud of Ghazni**."),
        mk("Mixing Hawkins and Roe.", "**Hawkins** came in 1608. **Roe** came in 1615 as envoy of James I."),
    ],
    revision=[
        "Barani: Tarikh-i-Firoz Shahi. Abul Fazl: Akbarnama (Ain is vol. 3). Lahori: Badshahnama. Babur: Turkish memoir.",
        "Travellers: Marco Polo (Pandya), Ibn Battuta (Muhammad bin Tughlaq), Conti and Paes (Vijayanagara), Razzaq (Deva Raya II).",
        "Nikitin: Bahmani. Fitch: Akbar. Roe: Jahangir (1615).",
        "Jayasi: Padmavat (Awadhi). Khusrau wrote chiefly in Persian.",
        "Court histories praise patrons, so exams love the question \"who visited whom\".",
    ],
    patterns=[
        pat("ga-st-p1", "Chronicle and author (Sultanate and Mughal)", "very common",
            "A book title to match with its author, or a match-the-column list.",
            ["Sultanate: Barani (Tarikh-i-Firoz Shahi), Minhaj (Tabaqat-i-Nasiri).",
             "Mughal: Abul Fazl (Akbarnama), Lahori (Badshahnama), Gulbadan (Humayun-nama).",
             "Match the emperor to the historian before you answer."],
            "Each book has exactly one author, and an emperor's name in the title helps.",
            "The Tarikh-i-Firoz Shahi, a history of the Tughlaq age, was written by:",
            ["The title names Firoz Shah.", "Its author is Ziauddin Barani."],
            "Ziauddin Barani"),
        pat("ga-st-p2", "Foreign travellers and the courts they visited", "very common",
            "\"Who visited the court of...\" or a traveller-country-ruler match.",
            ["Use the ladder: Ibn Battuta-Muhammad bin Tughlaq, Razzaq-Deva Raya II, Paes-Krishnadevaraya.",
             "Then: Nikitin-Bahmani, Fitch-Akbar, Roe-Jahangir.",
             "The traveller's country is a strong clue."],
            "Each traveller pairs with one ruler, and the country removes wrong options.",
            "Who visited the court of Deva Raya II of Vijayanagara as an envoy of Persia?",
            ["Persia narrows the list.", "The Timurid envoy was Abdur Razzaq."],
            "Abdur Razzaq"),
        pat("ga-st-p3", "Regional and vernacular classics", "common",
            "\"Padmavat\", \"Humayun-nama\", \"Amuktamalyada\" or a language question.",
            ["Jayasi: Padmavat, Awadhi.",
             "Gulbadan Begum: Humayun-nama, a woman chronicler.",
             "Krishnadevaraya: Amuktamalyada, Telugu."],
            "Each classic has a language and an author, which the options test.",
            "The Padmavat, an Awadhi Sufi romance, was written by:",
            ["It was written in 1540.", "The author is Malik Muhammad Jayasi."],
            "Malik Muhammad Jayasi"),
        pat("ga-st-p4", "Mughal court literature and memoirs", "common",
            "Words like Baburnama, Tuzuk-i-Jahangiri, Ain-i-Akbari, Badshahnama.",
            ["Two royal memoirs: Babur (Turkish) and Jahangir (Tuzuk-i-Jahangiri).",
             "Ain-i-Akbari is the third volume of the Akbarnama.",
             "Abdul Hamid Lahori wrote on Shah Jahan."],
            "Emperor, book and volume form a short fixed set.",
            "The Ain-i-Akbari is which part of Abul Fazl's Akbarnama?",
            ["The Akbarnama has three volumes.", "The Ain is the third."],
            "The third volume"),
        pat("ga-st-p5", "Best source for what?", "occasional",
            "\"Which source tells us about prices / daily life / trade / court politics?\"",
            ["Administration and prices: Ain-i-Akbari.",
             "Daily life: Rihla, Paes, Bernier. Trade: Tavernier, Marco Polo, Nikitin.",
             "Court politics: Barani (Tughlaqs), Badauni against Abul Fazl."],
            "The question type asks you to match a source to its strength.",
            "Which source is best for Akbar's mansabs, provinces and prices?",
            ["It is an administrative gazetteer.", "It forms the third volume of the Akbarnama."],
            "The Ain-i-Akbari"),
    ],
)

# ---------------------------------------------------------------- apply
data = json.loads(TOPIC.read_text(encoding="utf-8"))
by_id = {s["id"]: s for s in data["subtopics"]}
assert set(S) == set(by_id), (set(S) ^ set(by_id))
new_ids = [p["id"] for s in S.values() for p in s["patterns"]]
assert len(new_ids) == len(set(new_ids)), "duplicate pattern id"
for sid, new in S.items():
    sub = by_id[sid]
    old = {p["id"] for p in sub.get("patterns", [])}
    assert old <= {p["id"] for p in new["patterns"]}, (sid, old)
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sid, len(n))
    sub.update(concept=new["concept"], notes=n, patterns=new["patterns"], mistakes=new["mistakes"],
               revision=new["revision"], tricks=new["tricks"])
    print(f"{sid}: notes {len(n)} chars, {len(new['patterns'])} patterns (was {len(old)})")
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
