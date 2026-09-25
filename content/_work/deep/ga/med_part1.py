"""medieval-history deep content — part 1: early-medieval, delhi-sultanate, vijayanagara-bahmani, mughals."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_early():
    S = Sub("early-medieval")
    S.notes = """### After Harsha: a mosaic of kingdoms
From the 8th century north India split among the **Palas** (Bengal-Bihar), the **Gurjara-Pratiharas** (Malwa-Rajasthan) and the **Rashtrakutas** (Deccan), all three fighting for **Kannauj** — the famous **tripartite struggle**. The **Palas** began when **Gopala** was elected king (c. 750); **Dharmapala** founded the **Vikramashila** monastery and revived Nalanda, and the dynasty patronised Buddhism. The Pratiharas under **Nagabhata I** turned back Arab raids; **Mihira Bhoja** was their best-known ruler. The Rashtrakutas (founder **Dantidurga**) gave India the **Kailasa temple, Ellora (Krishna I)** and the *Kavirajamarga* (Amoghavarsha). Rajput clans filled the rest of the north: the **Chauhans** (Delhi-Ajmer — **Prithviraj III**, the two Battles of **Tarain**, 1191 and 1192), **Gahadavalas** (Kannauj — Jaichand), **Paramaras** (Malwa — the scholar-king **Bhoja** of Dhara), **Chandellas** (Khajuraho temples), **Solankis** (Somnath, Dilwara), and the **Senas** of Bengal (Lakshmanasena, the last old-order king, whose capital fell to Bakhtiyar Khalji).

### The Cholas at their height
The imperial line began when **Vijayalaya** captured **Thanjavur** (c. 850). **Rajaraja I** conquered Sri Lanka and the Maldives and built the great **Brihadeshwara (Rajarajeshwara) temple at Thanjavur**. His son **Rajendra I** marched to the Ganga (taking the title **Gangaikonda**, and building the capital **Gangaikondacholapuram**) and sent a **naval expedition against Srivijaya** (Shailendra kingdom of Sumatra-Malaya peninsula) to guard the China trade. The Chola navy, the bronzes (**Nataraja**) and temple building mark the age's peak.

### Village self-rule: the Uttaramerur inscriptions
The Cholas' most-quoted contribution is **local self-government**. The **Uttaramerur inscriptions** (of **Parantaka I**'s reign) record how village committees (**variyams**) were chosen by the **kudavolai** (pot-ticket) system — candidates were screened for age, property and learning, names were drawn from a pot, and members could be removed for misconduct. Village assemblies had three forms: the **ur** (common villages), the **sabha** (Brahmadeya, Brahmana-grant villages) and the **nagaram** (merchant towns).

### Other regional powers
Eastern **Gangas** of Odisha — **Narasimhadeva I** built the **Konark Sun Temple**. **Hoysalas** (capital **Dorasamudra/Halebidu**, temples at Belur-Halebidu-Somnathpura). **Kakatiyas** of Warangal — ruled briefly by the woman ruler **Rani Rudramadevi**. **Western Chalukyas of Kalyani** (Vikramaditya VI) fought the Cholas for the Tungabhadra doab; **Yadavas** held Devagiri until Alauddin Khalji's raids.

### Quick revision
- Tripartite struggle = Pala vs Pratihara vs Rashtrakuta, prize **Kannauj**; Gopala = elected Pala founder; Dharmapala = Vikramashila.
- Rajput houses: Chauhan-Prithviraj (Tarain 1191/1192), Paramara-Bhoja, Chandella-Khajuraho, Solanki-Somnath, Gahadavala-Jaichand, Sena-Lakshmanasena.
- Chola chain: Vijayalaya (850, Thanjavur) → Rajaraja I (Brihadeshwara) → Rajendra I (Gangaikonda; navy vs Srivijaya).
- Uttaramerur (Parantaka I): kudavolai lottery, variyam committees; assemblies = ur, sabha, nagaram.
- Regional capitals: Hoysala-Dorasamudra, Kakatiya-Warangal, Ganga-Konark."""
    S.pattern("ga-em-p1", "Tripartite struggle and the three powers", "common",
        "'Who won the tripartite struggle', Pala-Pratihara-Rashtrakuta founder or university or temple links.",
        None,
        "1. Powers: **Palas = Bengal-Bihar (Buddhist)**, Gurjara-Pratiharas = Malwa-Rajasthan, Rashtrakutas = Deccan; prize = **Kannauj**.\n2. Anchors: Gopala (elected Pala), Dharmapala (Vikramashila), Nagabhata I (Arab raids), Krishna I (Kailasa Ellora), Amoghavarsha (Kavirajamarga).\n3. In statement questions, check which dynasty each fact belongs to before judging.",
        "Which Pala ruler founded the **Vikramashila** monastery?",
        "**Dharmapala** — the Palas were the great Buddhist patrons of Bengal-Bihar.")
    S.pattern("ga-em-p2", "Chola rulers ↔ achievements", "very common",
        "'Gangaikonda was the title of', who built the Brihadeshwara temple, the naval expedition against Srivijaya, order of Chola rulers.",
        None,
        "1. Chain: Vijayalaya (founder, Thanjavur) → Rajaraja I → Rajendra I.\n2. Rajaraja I = **Brihadeshwara temple, Thanjavur**; Rajendra I = **Gangaikonda** title, **Gangaikondacholapuram**, **navy vs Srivijaya (Shailendra)**.\n3. The Srivijaya raid was to protect the **China trade route** — a favourite 'why' question.",
        "Which Chola ruler sent a naval expedition against the **Srivijaya** kingdom?",
        "**Rajendra I** — to secure the sea route to China; he also marched to the Ganga (title Gangaikonda).")
    S.pattern("ga-em-p3", "Chola village administration: Uttaramerur and kudavolai", "very common",
        "'The kudavolai system', which inscription records village committees, ur vs sabha vs nagaram, eligibility rules.",
        None,
        "1. Source: **Uttaramerur inscriptions**, reign of **Parantaka I**.\n2. System: **kudavolai (pot-ticket)** — names drawn from a pot; committees called **variyam**; eligibility rules on age, property, learning.\n3. Assemblies: **ur** = common villages, **sabha** = Brahmadeya (Brahmana) villages, **nagaram** = merchant towns.",
        "Under the **kudavolai** system of the Cholas, village committee members were chosen by —",
        "Drawing **lots (tickets) from a pot** — hence 'pot-ticket' — under rules recorded in the Uttaramerur inscriptions.")
    S.pattern("ga-em-p4", "Rajput and regional kingdoms: houses ↔ capitals & rulers", "common",
        "'Which dynasty ruled Warangal', 'Rani Rudramadevi belonged to', Konark-Halebidu-Khajuraho builder links, Tarain facts.",
        None,
        "1. Houses: Chauhan-Delhi-Ajmer (Prithviraj, Tarain), Paramara-Malwa (Bhoja), Chandella-Khajuraho, Solanki-Gujarat (Somnath), Gahadavala-Kannauj (Jaichand), Sena-Bengal (Lakshmanasena).\n2. Deccan-south: Kakatiya-Warangal (Rudramadevi), Hoysala-Dorasamudra (Belur-Halebidu), Eastern Ganga-Odisha (Narasimhadeva I, Konark).\n3. Match the temple to its builder-dynasty before answering.",
        "**Rani Rudramadevi**, a rare woman ruler of the medieval age, belonged to which dynasty?",
        "The **Kakatiyas** of Warangal (Telangana-Andhra).")

    S.q("ga-em-p1", "easy", "The founder of the **Pala dynasty** of Bengal, said to have been elected by the people, was —",
        ["Dharmapala", "Gopala", "Devapala", "Mahipala"], "Gopala",
        "**Gopala** (c. 750) was chosen as king by the people to end anarchy — a rare elected foundation in Indian history.",
        "Gopala = the elected one.", 20)
    S.q("ga-em-p1", "medium", "**Nagabhata I**, who repelled Arab invaders, was a ruler of which dynasty?",
        ["Palas", "Gurjara-Pratiharas", "Rashtrakutas", "Chauhans"], "Gurjara-Pratiharas",
        "**Nagabhata I** of the **Gurjara-Pratihara** dynasty (Avanti-Malwa) checked the Arab advance from Sind; the Pratiharas later held Kannauj.",
        "Pratihara = 'door-keeper' against Arabs.", 25)
    S.q("ga-em-p2", "easy", "The imperial **Chola** dynasty's line at Thanjavur began with —",
        ["Rajaraja I", "Vijayalaya", "Rajendra I", "Parantaka I"], "Vijayalaya",
        "**Vijayalaya** captured Thanjavur (c. 850) and founded the imperial line; Rajaraja I and Rajendra I carried it to its height.",
        "Vijayalaya = the founder (850).", 20)
    S.q("ga-em-p2", "easy", "The **Brihadeshwara (Rajarajeshwara) temple** at Thanjavur was built by —",
        ["Rajendra I", "Rajaraja I", "Vijayalaya", "Kulottunga"], "Rajaraja I",
        "**Rajaraja I** built the Brihadeshwara temple (c. 1010) — a UNESCO-listed masterpiece of Dravida architecture with a 13-storey vimana.",
        "Rajaraja-Rajarajeshwara name match.", 20)
    S.q("ga-em-p2", "medium", "Rajendra I took the title **'Gangaikonda'** after —",
        ["Defeating the Pandyas", "A march to the river Ganga", "Conquering Sri Lanka", "The Srivijaya expedition"], "A march to the river Ganga",
        "'Gangaikonda' = 'bringer of the Ganga' — after his northward march to the Ganga; he then built **Gangaikondacholapuram** as a new capital.",
        "Ganga-konda = 'took the Ganga'.", 25)
    S.q("ga-em-p3", "medium", "The Chola village committees chosen under the **kudavolai** system were called —",
        ["Ur", "Sabha", "Variyam", "Nagaram"], "Variyam",
        "The elected committees were called **variyams** (e.g. garden, tank, justice committees). 'Ur', 'sabha' and 'nagaram' are the types of village assemblies.",
        "Variyam = committee; ur/sabha/nagaram = assemblies.", 25)
    S.q("ga-em-p3", "medium", "The **Uttaramerur inscriptions**, which detail Chola village elections, belong to the reign of —",
        ["Rajaraja I", "Parantaka I", "Rajendra I", "Vijayalaya"], "Parantaka I",
        "The Uttaramerur records of village committee elections date to **Parantaka I**'s reign (10th century) — earlier than the famous imperial pair.",
        "Uttaramerur = Parantaka I (before Rajaraja).", 25)
    S.q("ga-em-p3", "hard", "In Chola administration, the assembly of a **Brahmadeya** (Brahmana-grant) village was called the —",
        ["Ur", "Sabha", "Nagaram", "Variyam"], "Sabha",
        "**Sabha** = assembly of Brahmadeya villages; **ur** = ordinary villages; **nagaram** = market/merchant towns. The sabha's working is the best documented (Uttaramerur).",
        "Brahmana village = sabha.", 30)
    S.q("ga-em-p4", "easy", "The **Konark Sun Temple** was built by —",
        ["Narasimhadeva I", "Anantavarman Chodaganga", "Krishnadevaraya", "Vishnuvardhana"], "Narasimhadeva I",
        "**Narasimhadeva I** of the **Eastern Ganga** dynasty built Konark (13th century) — a chariot-shaped Sun temple, a UNESCO site.",
        "Konark = Eastern Ganga king.", 20)
    S.q("ga-em-p4", "medium", "The **Hoysala** capital **Dorasamudra** is today known as —",
        ["Belur", "Halebidu", "Warangal", "Devagiri"], "Halebidu",
        "Dorasamudra is modern **Halebidu** (Karnataka); the Hoysaleswara temple stands there, and Belur's Chennakeshava temple is nearby.",
        "Dorasamudra = Halebidu ('old capital').", 25)
    S.q("ga-em-p4", "medium", "**Prithviraj Chauhan** ruled from Delhi and —",
        ["Kannauj", "Ajmer", "Gwalior", "Ujjain"], "Ajmer",
        "The Chauhan kingdom had two centres — **Delhi and Ajmer**. Jaichand's Gahadavalas held Kannauj.",
        "Chauhan pair: Delhi + Ajmer.", 25)
    S.q("ga-em-p4", "hard", "Consider the statements:\n1. The Cholas traded actively with Song China.\n2. Chola bronzes are famous for the Nataraja form.\n3. The Chola land survey formed the basis of the revenue assessment.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three are standard Chola facts: embassies and trade with Song China, the superb **Nataraja bronzes**, and a careful land survey for revenue.",
        "Chola administration + trade + art — all three usually appear together as true statements.", 30)
    return S


def build_sultanate():
    S = Sub("delhi-sultanate")
    S.notes = """### Five dynasties, 320 years (1206–1526)
| Dynasty | Period | Remember |
|---|---|---|
| **Slave (Mamluk/Ilbari)** | 1206–1290 | Qutbuddin Aibak founded; Iltutmish consolidated; Razia (only woman); Balban (kingship theory) |
| **Khalji** | 1290–1320 | Alauddin: market control, standing army, southern raids |
| **Tughlaq** | 1320–1414 | MBT's experiments; Firoz Shah's works |
| **Sayyid** | 1414–1451 | Khizr Khan (after Timur's sack) |
| **Lodi** | 1451–1526 | First Afghan house; Ibrahim Lodi fell at Panipat 1526 |

**Iltutmish** (real founder) introduced the **silver tanka** and copper **jital**, completed the Qutub Minar, and formed the **Chahalgani ('the Forty')** group of Turani nobles. **Balban** stressed royal dignity — **sijda** and **paibos** — and ruled by 'blood and iron'. **Alauddin Khalji** ran a **standing army** (soldiers identified by **chehra** descriptive rolls, horses by **daag** branding), fixed **market prices** (Shahna-i-Mandi supervising), and sent **Malik Kafur** into the far south. **Muhammad bin Tughlaq** tried the **capital shift to Daulatabad** and **token copper currency** (forged, and failed). **Firoz Shah Tughlaq** built canals, rest houses, Diwan-i-Khairat (charity) and Diwan-i-Bandagan (slaves), and **extended jizya to Brahmanas**. **Timur's** sack of Delhi (**1398**) broke the Tughlaqs; the Lodis' **Sikandar** founded **Agra**, and **Ibrahim Lodi** lost to Babur at **Panipat (1526)** — the Sultanate's end.

### The machinery of the state
- **Iqta system:** revenue assignments (**iqta**) to nobles (**muqti/iqtadar**) who collected tax and kept troops — the Sultanate's revenue-military base.
- **Diwans:** **Wizarat** (finance), **Ariz** (military), **Risalat** (foreign/religious), **Qaza** (justice), **Insha** (correspondence).
- **Barids and munihiyan:** intelligence and secret agents. The ulema's opinion weighed in state matters; Persian was the court language.

### Economy and society
Land tax (**kharaj**) could reach a third to a half of produce; **jizya** fell on non-Muslims (as a state practice from Firoz Shah, on Brahmanas too). Craft and markets thrived (Alauddin's price control is the classic case); Persianate culture, calligraphy and mosque-arch architecture (arch and dome, Alai Darwaza, Tughlaq sloping walls) took root.

### Quick revision
- Dynasty ladder: Slave 1206 → Khalji 1290 → Tughlaq 1320 → Sayyid 1414 → Lodi 1451 → ends 1526 (Panipat).
- Iltutmish: tanka-jital, Chahalgani, Qutub Minar; Balban: sijda-paibos, blood & iron.
- Alauddin: chehra-daag, market reforms (Shahna-i-Mandi), Malik Kafur's southern raids, Siri.
- MBT: Daulatabad shift + token currency (both failed); Firoz Shah: canals, charity departments, jizya on Brahmanas.
- Iqta = revenue-for-service; Diwan-i-Ariz = army; Timur 1398 → Sayyids; 1526 ends it all."""
    S.pattern("ga-ds-p1", "Dynasty ↔ founder ↔ landmark chain", "very common",
        "'Which dynasty ruled when', founder questions, Razia as first woman ruler, 'the Forty'.",
        None,
        "1. Ladder with dates: Slave 1206, Khalji 1290, Tughlaq 1320, Sayyid 1414, Lodi 1451, end 1526.\n2. Anchors: Aibak founded, Iltutmish consolidated (tanka, Forty), Razia = first and only woman sultan, Balban = blood & iron.\n3. Sayyids came after Timur's 1398 sack; Lodis were the first Afghan house.",
        "The group of forty leading slaves of Iltutmish, which dominated court politics, was called —",
        "**Chahalgani (Turkan-i-Chihalgani), 'the Forty'** — it set up and pulled down sultans after Iltutmish.")
    S.pattern("ga-ds-p2", "Administration and economy: iqta, diwans, market control", "very common",
        "'The iqta system meant', Diwan-i-Ariz/Wizarat functions, chehra-daag, price control machinery, kharaj-jizya.",
        None,
        "1. **Iqta**: revenue assignment to a muqti in return for troops and service — not ownership.\n2. Diwans: **Wizarat = finance**, **Ariz = army**, **Risalat = foreign/religious**, **Qaza = justice**, **Insha = correspondence**.\n3. Alauddin's army tools: **chehra** (descriptive roll), **daag** (horse branding); market control under the **Shahna-i-Mandi**.",
        "Which department of the Delhi Sultanate looked after the **army**?",
        "**Diwan-i-Ariz** — the military department (headed by the Ariz-i-Mumalik).")
    S.pattern("ga-ds-p3", "Sultans' landmark acts and famous experiments", "common",
        "Daulatabad shift, token currency, canals and charity departments of Firoz Shah, jizya extensions, Qutub Minar.",
        None,
        "1. MBT's pair of failures: **Daulatabad capital shift** and **token copper currency** (forgery killed it); also Khorasan and Qarachil expeditions.\n2. Firoz Shah: **canals**, Diwan-i-Khairat & Diwan-i-Bandagan, Firoz Shah Kotla, and **jizya extended to Brahmanas**.\n3. Qutub Minar begun by Aibak, completed by Iltutmish.",
        "Muhammad bin Tughlaq's **token currency** failed mainly because —",
        "**Copper tokens were easily forged** by the public; the treasury had to redeem them at face value, and the scheme was withdrawn.")
    S.pattern("ga-ds-p4", "Foreign invasions and the Sultanate's end", "common",
        "Mongol threat and Siri, Timur's sack and the Sayyids, Bakhtiyar Khalji in Bihar-Bengal, First Battle of Panipat.",
        None,
        "1. Mongols: repelled by Balban's stern policy; **Alauddin built Siri** and met them at the gates of Delhi.\n2. **Timur, 1398** — sacked Delhi, ended Tughlaq power, led to the Sayyids.\n3. **1526, First Battle of Panipat** — Babur beat Ibrahim Lodi; Sultanate ends, Mughals begin.",
        "Which sultan built the **fort of Siri** as a shelter against the Mongols?",
        "**Alauddin Khalji** — Mongol invasions pressed Delhi repeatedly in his reign.")

    S.q("ga-ds-p1", "medium", "Who is regarded as the **real consolidator** of the Delhi Sultanate among the Slave rulers?",
        ["Qutbuddin Aibak", "Iltutmish", "Balban", "Aram Shah"], "Iltutmish",
        "**Iltutmish** (1211–1236) saved the infant state from rivals, organised the iqta system, issued tanka-jital and formed the Chahalgani.",
        "Aibak founded, Iltutmish consolidated, Balban dignified.", 25)
    S.q("ga-ds-p1", "easy", "The **first and only woman** to rule Delhi was —",
        ["Noor Jahan", "Razia Sultan", "Chand Bibi", "Rani Durgavati"], "Razia Sultan",
        "**Razia** (1236–1240), daughter of Iltutmish, was the first and only woman sultan of Delhi.",
        "Razia = Delhi's only woman sultan.", 20)
    S.q("ga-ds-p2", "medium", "Under the **iqta system**, the holder of the iqta was expected mainly to —",
        ["Own the land outright", "Collect revenue and maintain troops for the Sultan", "Stay at court as a hostage", "Trade the land's produce"], "Collect revenue and maintain troops for the Sultan",
        "The **muqti** collected the assigned revenue and kept a fixed body of troops for royal service — revenue assignment for service, not land ownership.",
        "Iqta = revenue + soldiers, not ownership.", 25)
    S.q("ga-ds-p2", "easy", "Alauddin Khalji identified horses by **branding (daag)** and soldiers by —",
        ["Uniform colour", "Descriptive rolls (chehra)", "Facial tattoos", "Family seals"], "Descriptive rolls (chehra)",
        "**Chehra** (descriptive roll of the soldier) and **daag** (branding of horses) were Alauddin's tools to stop the ghost-soldier fraud in his standing army.",
        "Chehra-daag pair — man and horse.", 20)
    S.q("ga-ds-p3", "easy", "Which Sultan shifted his court's perception of royal dignity by enforcing **sijda and paibos**?",
        ["Iltutmish", "Balban", "Alauddin Khalji", "Sikandar Lodi"], "Balban",
        "**Balban** introduced Persian court customs — **sijda** (prostration) and **paibos** (kissing the feet) — to overawe the nobles with royal majesty.",
        "Balban = theory of kingship.", 20)
    S.q("ga-ds-p3", "medium", "**Firoz Shah Tughlaq** is remembered for all of the following EXCEPT —",
        ["Digging canals for irrigation", "Setting up Diwan-i-Khairat for charity", "Extending jizya to Brahmanas", "Introducing token copper currency"], "Introducing token copper currency",
        "The **token currency** was Muhammad bin Tughlaq's failed experiment. Firoz Shah built canals, charity institutions and extended jizya.",
        "MBT = experiments; Firoz = welfare works.", 25)
    S.q("ga-ds-p4", "medium", "**Timur's** invasion, which crippled the Delhi Sultanate, took place in —",
        ["1298", "1398", "1498", "1526"], "1398",
        "**Timur** sacked Delhi in **1398**; the Tughlaqs never recovered, and the **Sayyid** dynasty (Khizr Khan) followed.",
        "1398 Timur → Sayyids; 1526 Babur → Mughals.", 25)
    S.q("ga-ds-p4", "medium", "Bakhtiyar Khalji's destruction of the great Buddhist monasteries of **Bihar** happened during —",
        ["Balban's reign", "Alauddin Khalji's reign", "Qutbuddin Aibak's reign", "Firoz Shah's reign"], "Qutbuddin Aibak's reign",
        "Ikhtiyaruddin **Bakhtiyar Khalji** swept through Bihar and Bengal in the early 1200s (Aibak's period), destroying Nalanda, Odantapuri and Vikramashila's remnants.",
        "Bakhtiyar = the Bihar-Bengal raider.", 25)
    return S


def build_vijaya():
    S = Sub("vijayanagara-bahmani")
    S.notes = """### City of victory on the Tungabhadra
**Vijayanagara** ('city of victory') was founded in **1336** on the Tungabhadra bank at **Hampi** by the Sangama brothers **Harihara and Bukka**, blessed by the guru **Vidyaranya**. Four dynasties ruled it in turn: **Sangama → Saluva → Tuluva → Aravidu**. Its economy rested on the fertile **Raichur doab** (the doab of the Krishna-Tungabhra rivers, long contested with the Bahmanis), diamond and spice trade, and a powerful cavalry fed by Portuguese horse imports.

### Krishnadevaraya, the greatest ruler (1509–1529)
Of the **Tuluva** dynasty, he defeated the Bahmanis and the Odisha (Gajapati) king, and won the **Battle of Raichur** (1520, with Portuguese muskets). Titles: **Andhra Bhoja**, 'establisher of Yavana rule' and more. His court had the **Ashtadiggajas** (eight elephants of learning), the greatest being **Allasani Peddana** (*Manucharitam*, honoured as 'Andhra Kavita Pitamaha'); Krishnadevaraya himself wrote the Telugu classic **Amuktamalyada**. Portuguese visitors **Domingo Paes** and **Duarte Barbosa** describe his glittering capital — the **Virupaksha** and **Vittala** temples (the famous stone chariot), the Hazara Rama temple, and bazaars of pearls.

### The Bahmani kingdom and its five heirs
The **Bahmani kingdom** was founded in **1347** by **Alauddin Hasan Bahman Shah (Hasan Gangu)** with its capital at **Gulbarga** (later **Bidar**). Its able wazir **Mahmud Gawan** was executed by court factions (1481) — after which the kingdom split into **five sultanates**: **Bijapur (Adil Shahi), Ahmadnagar (Nizam Shahi), Golconda (Qutb Shahi), Berar (Imad Shahi) and Bidar (Barid Shahi)**.

### Rivalry and the fall
Vijayanagara and the Bahmanis fought almost continuously over the Raichur doab, the Krishna-Godavara delta and horse trade. In **1565**, at the **Battle of Talikota (Rakshasa-Tangadi)**, a coalition of the Deccan sultanates crushed Vijayanagara; the de facto ruler **Rama Raya** (Aravidu) was captured and executed, and Hampi was sacked and abandoned. The dynasty lingered from Penukonda-Chandragiri; Nayak kingdoms took over the south. The ruins are the **Hampi** UNESCO World Heritage site — 'a city of victory in stone'.

### Quick revision
- 1336, Harihara-Bukka (Sangama), guru Vidyaranya; dynasties Sangama-Saluva-Tuluva-Aravidu.
- Krishnadevaraya (Tuluva): Raichur win, Ashtadiggajas, Allasani Peddana, Amuktamalyada, visitor Paes.
- Bahmani: Hasan Gangu, 1347, Gulbarga → Bidar; Mahmud Gawan executed; five sultanates (B-A-G-B-B).
- 1565 Talikota: five sultanates beat Rama Raya; Hampi sacked; today = UNESCO site."""
    S.pattern("ga-vg-p1", "Vijayanagara: founders and the four dynasties", "very common",
        "'Who founded Vijayanagara and when', which dynasty Krishnadevaraya belonged to, guru Vidyaranya, order of dynasties.",
        None,
        "1. **1336, Hampi on the Tungabhadra; Harihara & Bukka (Sangama brothers)**, guru **Vidyaranya**.\n2. Dynasties in order: **Sangama → Saluva → Tuluva → Aravidu**.\n3. Krishnadevaraya = **Tuluva**; Rama Raya of Talikota = **Aravidu**.",
        "Vijayanagara was founded on the banks of which river?",
        "The **Tungabhadra** — at Hampi, by Harihara and Bukka in 1336.")
    S.pattern("ga-vg-p2", "Krishnadevaraya: conquests, court and classics", "very common",
        "Ashtadiggajas, Allasani Peddana, Amuktamalyada, Battle of Raichur, Portuguese visitors, titles.",
        None,
        "1. Court: **Ashtadiggajas**; chief poet **Allasani Peddana** (*Manucharitam*, 'Andhra Kavita Pitamaha').\n2. His own Telugu work: **Amuktamalyada**; title **Andhra Bhoja**.\n3. Battles and visitors: **Raichur 1520** win; **Domingo Paes** (and Duarte Barbosa) left accounts of Hampi.",
        "Who was the greatest of the **Ashtadiggajas** at Krishnadevaraya's court?",
        "**Allasani Peddana**, author of *Manucharitam* — honoured as 'Andhra Kavita Pitamaha'.")
    S.pattern("ga-vg-p3", "Bahmani kingdom: founder, capital, five sultanates", "common",
        "'The Bahmani kingdom was founded by', its capital, Mahmud Gawan, the five successor sultanates and their houses.",
        None,
        "1. **1347, Alauddin Hasan Bahman Shah (Hasan Gangu)**; capital **Gulbarga**, later **Bidar**.\n2. Mahmud Gawan — the great wazir, executed in faction politics (1481).\n3. Five sultanates: **Bijapur-Adil Shahi, Ahmadnagar-Nizam Shahi, Golconda-Qutb Shahi, Berar-Imad Shahi, Bidar-Barid Shahi**.",
        "The Bahmani kingdom broke up into five sultanates. Which house ruled **Golconda**?",
        "The **Qutb Shahi** dynasty (Bijapur = Adil Shahi, Ahmadnagar = Nizam Shahi).")
    S.pattern("ga-vg-p4", "Hampi and the decisive battles", "common",
        "Raichur doab rivalry, Talikota 1565 and Rama Raya, Hampi ruins as heritage, stone chariot.",
        None,
        "1. Long war zone: the **Raichur doab** (Krishna-Tungabhadra) — Bahmanis vs Vijayanagara.\n2. **Talikota (Rakshasa-Tangadi), 1565**: five sultanates defeated Vijayanagara; **Rama Raya** executed; Hampi sacked.\n3. Hampi = UNESCO site; landmarks: Vittala temple **stone chariot**, Virupaksha temple.",
        "Who led Vijayanagara at the **Battle of Talikota** (1565) and was executed after the defeat?",
        "**Rama Raya** — the aged Aravidu regent; the empire never recovered.")

    S.q("ga-vg-p1", "easy", "**Vijayanagara** was founded in 1336 by —",
        ["Krishnadevaraya and Timmarusu", "Harihara and Bukka", "Deva Raya and Saluva", "Rama Raya and Tirumala"], "Harihara and Bukka",
        "The Sangama brothers **Harihara and Bukka** founded Vijayanagara at Hampi in **1336**, guided by the guru **Vidyaranya**.",
        "Founders = the two Sangama brothers.", 20)
    S.q("ga-vg-p1", "medium", "Which dynasty did **Krishnadevaraya** belong to?",
        ["Sangama", "Saluva", "Tuluva", "Aravidu"], "Tuluva",
        "Krishnadevaraya was the greatest ruler of the **Tuluva** dynasty (1509–1529), the third of Vijayanagara's four houses.",
        "Order S-S-T-A; Krishnadevaraya = third.", 25)
    S.q("ga-vg-p2", "medium", "Krishnadevaraya wrote the Telugu classic **Amuktamalyada** on —",
        ["War strategy", "Devotion to God (Andal's story) and governance", "Horse breeding", "Temple architecture"], "Devotion to God (Andal's story) and governance",
        "*Amuktamalyada* (in Telugu) tells the story of the Vaishnava saint **Andal** and also contains Krishnadevaraya's famous sections on **governance**.",
        "His book = Amuktamalyada; his title = Andhra Bhoja.", 25)
    S.q("ga-vg-p2", "medium", "Which Portuguese traveller left a vivid account of **Krishnadevaraya's** Vijayanagara?",
        ["Ibn Battuta", "Domingo Paes", "Marco Polo", "Athanasius Nikitin"], "Domingo Paes",
        "**Domingo Paes** (and Duarte Barbosa) visited Vijayanagara in Krishnadevaraya's time and praised its bazaars and grandeur. Nikitin came to the Bahmani kingdom earlier; Ibn Battuta to the Sultanate.",
        "Paes = Krishnadevaraya's Hampi.", 25)
    S.q("ga-vg-p2", "medium", "The title **'Andhra Bhoja'** was earned by —",
        ["Allasani Peddana", "Krishnadevaraya", "Deva Raya II", "Harihara"], "Krishnadevaraya",
        "**Krishnadevaraya** was called 'Andhra Bhoja' for his patronage of Telugu letters (like the great Bhoja).",
        "Bhoja-title = scholar-king = Krishnadevaraya.", 25)
    S.q("ga-vg-p3", "easy", "The **Bahmani kingdom** was founded in 1347 by —",
        ["Mahmud Gawan", "Hasan Gangu", "Firoz Shah Bahmani", "Nizam Shah"], "Hasan Gangu",
        "**Alauddin Hasan Bahman Shah (Hasan Gangu)** founded the Bahmani kingdom in 1347, with the capital at Gulbarga.",
        "1347 + Hasan Gangu = Bahmani.", 20)
    S.q("ga-vg-p3", "medium", "The five sultanates born from the Bahmani breakup include **Berar**, ruled by the —",
        ["Adil Shahi house", "Imad Shahi house", "Barid Shahi house", "Qutb Shahi house"], "Imad Shahi house",
        "Five heirs: **Bijapur (Adil Shahi), Ahmadnagar (Nizam Shahi), Golconda (Qutb Shahi), Berar (Imad Shahi), Bidar (Barid Shahi)**.",
        "Berar = Imad Shahi.", 25)
    S.q("ga-vg-p4", "easy", "The ruined city of **Hampi**, capital of Vijayanagara, stands on the bank of the —",
        ["Krishna", "Kaveri", "Tungabhadra", "Godavari"], "Tungabhadra",
        "Hampi sits on the **Tungabhadra** (a Krishna tributary); the site is a UNESCO World Heritage property.",
        "Hampi-Tungabhadra is the fixed pair.", 20)
    S.q("ga-vg-p4", "medium", "The **Raichur doab**, long contested between Vijayanagara and the Bahmanis, lies between the rivers —",
        ["Krishna and Tungabhadra", "Godavari and Krishna", "Kaveri and Vaigai", "Narmada and Tapti"], "Krishna and Tungabhadra",
        "The doab (land between two rivers) of the **Krishna and Tungabhadra** was the empire's bone of contention — won decisively at the Battle of Raichur (1520).",
        "Doab = 'two rivers' land: Krishna-Tungabhadra.", 25)
    S.q("ga-vg-p4", "hard", "At the Battle of Talikota, Vijayanagara faced a coalition of —",
        ["The five Deccan sultanates", "The Mughals and the Lodis", "The Marathas and the Portuguese", "Bahmani and Mughal forces"], "The five Deccan sultanates",
        "In 1565 the five successor sultanates (Bijapur, Ahmadnagar, Golconda, Berar, Bidar) united at **Talikota (Rakshasa-Tangadi)**, crushed Vijayanagara and executed Rama Raya.",
        "Talikota = five heirs of Bahmani united.", 30)
    return S


def build_mughals():
    S = Sub("mughals")
    S.notes = """### Founding the empire (1526–1556)
**Babur**, a Chagatai Timurid from Fergana, won the **First Battle of Panipat (1526)** against **Ibrahim Lodi** using artillery and the *tulughma* encircling tactics. In **1527** he beat **Rana Sanga** of Mewar at **Khanwa**; Chanderi followed (1528). His memoir, the **Baburnama (Tuzuk-i-Baburi)**, is in **Turkish** — a candid classic. **Humayun** lost the empire to **Sher Shah Sur** at **Chausa (1539)** and **Kannauj (1540)**, wandered 15 years (Persia's help), returned in 1555, and died within months.
### Sher Shah Sur (1540–1545), the gap-filler
An Afghan of Sasaram, Sher Shah ran the empire better than many kings: he issued the **rupiya** (silver) and dam (copper), rebuilt the **Grand Trunk Road** (Sonargaon in Bengal to the north-west) with **sarais** at stages, standardised **patta** (title deed) and **qabuliyat** (deed of agreement) in revenue, and organized a spy-run administration. His tomb at **Sasaram** is a landmark.
### Akbar (1556–1605): the empire takes shape
Regent **Bairam Khan** won the **Second Battle of Panipat (1556)** over **Hemu**. Akbar then: conquered Malwa, Chittor (1568) and Ranthambhor, Gujarat and Bengal; pursued a **Rajput policy of alliance** (marriages with Amber's house; Raja Man Singh and Todar Mal in high service); abolished the **pilgrimage tax** and **jizya**; and built **Fatehpur Sikri** with the **Buland Darwaza**. Finance minister **Raja Todar Mal** set the **dahsala (zabti) system** — revenue fixed on a 10-year average. The **mansabdari** system graded officers by **zat** (personal rank) and **sawar** (cavalry). In 1582 he promulgated **Din-i-Ilahi**, a syncretic order; **Ibadat Khana** at Fatehpur Sikri hosted debates. The **Navaratna** circle: Birbal, Todar Mal, Abul Fazl, Faizi, Tansen, Man Singh and others.
### Jahangir, Shah Jahan, Aurangzeb
**Jahangir** (1605–27): the 'chain of justice', paintings peak, **Sir Thomas Roe** (James I's ambassador, 1615); **Nur Jahan** ran the court. **Shah Jahan** (1628–58): the **Peacock Throne (Takht-i-Taus)**, **Taj Mahal** (for **Mumtaz Mahal**), Red Fort, Jama Masjid — the monument age. **Aurangzeb** (1658–1707): reimposed **jizya (1679)**, executed **Guru Tegh Bahadur (1675)**, fought the Marathas for 25 years in the Deccan — the drain that hollowed the empire.
### Later Mughals
Successors were puppets (the **Sayyid brothers** as king-makers). **Nadir Shah's** invasion (1739, **Battle of Karnal**) stripped the **Kohinoor** and Peacock Throne from **Muhammad Shah 'Rangeela'**; **Ahmad Shah Abdali** raided repeatedly. The empire shrank to Delhi before 1857's end.
### Quick revision
- Babur: Panipat 1526 → Khanwa 1527; Baburnama in Turkish. Humayun: Chausa 1539, Kannauj 1540.
- Sher Shah: rupiya, GT road + sarais, patta-qabuliyat; Sasaram tomb.
- Akbar: 2nd Panipat (Hemu), Todar Mal's dahsala, zat-sawar mansab, Din-i-Ilahi 1582, jizya abolished, Fatehpur Sikri.
- Jahangir-Roe; Shah Jahan-Peacock Throne/Taj; Aurangzeb-jizya 1679, Tegh Bahadur 1675.
- 1739 Nadir Shah (Karnal) under Muhammad Shah 'Rangeela'."""
    S.pattern("ga-mu-p1", "Babur, Humayun and Sher Shah: battles and reforms", "very common",
        "First/Second Panipat, Khanwa, Chausa-Kannauj, Sher Shah's rupiya/road/patta, Baburnama language.",
        None,
        "1. Babur: **Panipat 1526 (Ibrahim Lodi) → Khanwa 1527 (Rana Sanga)**; wrote **Baburnama in Turkish**.\n2. Humayun lost at **Chausa 1539** and **Kannauj 1540** to Sher Shah.\n3. Sher Shah: **rupiya**, GT road with sarais, **patta-qabuliyat**, tomb at Sasaram.",
        "The **Grand Trunk Road** revived by Sher Shah connected the north-west with —",
        "**Sonargaon in Bengal** — with sarais (rest houses) and trees along the stages.")
    S.pattern("ga-mu-p2", "Akbar: conquests, administration and Din-i-Ilahi", "very common",
        "Second Panipat, Rajput policy, Todar Mal's dahsala, zat-sawar, Din-i-Ilahi, jizya abolition, Navaratna.",
        None,
        "1. **2nd Panipat 1556**: Bairam Khan's regency beat Hemu.\n2. Revenue: **Todar Mal's dahsala/zabti** (10-year average); officers graded by **zat-sawar** (mansabdari).\n3. Ideology: **Din-i-Ilahi (1582)**, Sulh-i-kul, Ibadat Khana; **jizya and pilgrimage tax abolished**; Rajput alliances (Amber's house).",
        "Who devised the **dahsala (zabti)** revenue system of Akbar's reign?",
        "**Raja Todar Mal** — assessments based on a ten-year average yield and prices.")
    S.pattern("ga-mu-p3", "Jahangir–Shah Jahan–Aurangzeb: courts, monuments, policies", "very common",
        "Chain of justice, Sir Thomas Roe, Peacock Throne, Taj Mahal, jizya reimposed, execution of Guru Tegh Bahadur.",
        None,
        "1. Jahangir: 'chain of justice', **Sir Thomas Roe (1615)**, Nur Jahan's influence, Tuzuk-i-Jahangiri.\n2. Shah Jahan: **Peacock Throne**, Taj Mahal (Mumtaz), Red Fort, Jama Masjid.\n3. Aurangzeb: **jizya reimposed (1679)**, **Guru Tegh Bahadur executed (1675)**, endless Deccan war.",
        "Who came as the ambassador of England's James I to **Jahangir's** court (1615)?",
        "**Sir Thomas Roe** — securing trading concessions that led to the East India Company's factories.")
    S.pattern("ga-mu-p4", "Later Mughals and the empire's decline", "common",
        "Nadir Shah's invasion and loot, Muhammad Shah 'Rangeela', Sayyid brothers, Abdali raids, shrinking to Delhi.",
        None,
        "1. **Nadir Shah, 1739**: won at **Karnal** under **Muhammad Shah 'Rangeela'**; took the **Kohinoor and Peacock Throne**.\n2. **Sayyid brothers** = 'king-makers' of the later Mughals.\n3. **Ahmad Shah Abdali's** raids (Third Panipat 1761) finished Mughal hopes in the north.",
        "Nadir Shah invaded India in 1739 during the reign of —",
        "**Muhammad Shah 'Rangeela'** — after the Battle of Karnal, Delhi was sacked and the Peacock Throne and Kohinoor carried off.")

    S.q("ga-mu-p1", "easy", "In the **Battle of Khanwa (1527)**, Babur defeated —",
        ["Ibrahim Lodi", "Rana Sanga", "Hemu", "Sher Khan"], "Rana Sanga",
        "**Khanwa (1527)**: Babur beat the Rajput confederacy of **Rana Sanga** of Mewar; Panipat (1526) had already finished Ibrahim Lodi.",
        "Panipat-Lodi, Khanwa-Sanga.", 20)
    S.q("ga-mu-p1", "medium", "Babur wrote his memoirs, the **Tuzuk-i-Baburi (Baburnama)**, in —",
        ["Persian", "Arabic", "Turkish", "Urdu"], "Turkish",
        "The Baburnama is in **Chagatai Turkish**, Babur's mother tongue (it was later translated into Persian).",
        "Babur's own language = Turkish.", 25)
    S.q("ga-mu-p1", "medium", "Humayun lost his empire to Sher Shah at the battles of **Chausa** and —",
        ["Panipat", "Kannauj", "Khanwa", "Buxar"], "Kannauj",
        "**Chausa (1539)** and **Kannauj (Bilgram, 1540)** — both against Sher Khan (Sher Shah Sur); Humayun then wandered 15 years.",
        "Chausa-Kannauj pair, 1539-40.", 25)
    S.q("ga-mu-p2", "easy", "**Din-i-Ilahi**, the syncretic creed, was promulgated by —",
        ["Babur", "Humayun", "Akbar", "Jahangir"], "Akbar",
        "**Akbar** announced Din-i-Ilahi in **1582** as a discipleship order of sulh-i-kul (universal peace); Birbal was its most famous acceptor.",
        "Din-i-Ilahi = Akbar, 1582.", 20)
    S.q("ga-mu-p2", "medium", "The **Second Battle of Panipat (1556)** was won by Akbar's forces against —",
        ["Sher Shah", "Hemu", "Rana Sanga", "Daud Khan"], "Hemu",
        "Regent **Bairam Khan** led the young Akbar's army against **Hemu**, the wazir of the Surs, who had taken Delhi; Hemu was struck down and killed.",
        "2nd Panipat = Akbar vs Hemu.", 25)
    S.q("ga-mu-p2", "medium", "In the **mansabdari** system, 'zat' fixed personal rank and pay; 'sawar' fixed —",
        ["Land revenue", "Cavalry to be maintained", "Court seating", "Grain storage"], "Cavalry to be maintained",
        "**Zat** = personal rank and pay; **sawar** = number of horsemen the mansabdar had to maintain.",
        "Zat = rank, sawar = horses.", 25)
    S.q("ga-mu-p3", "easy", "The **Taj Mahal** was built by Shah Jahan in memory of —",
        ["Nur Jahan", "Mumtaz Mahal", "Jahanara", "Ladli Begum"], "Mumtaz Mahal",
        "**Mumtaz Mahal** (Arjumand Banu Begum), Shah Jahan's wife, is commemorated by the Taj on the Yamuna at Agra.",
        "Taj = Mumtaz Mahal.", 20)
    S.q("ga-mu-p3", "easy", "The jewelled **Peacock Throne (Takht-i-Taus)** was made for —",
        ["Akbar", "Jahangir", "Shah Jahan", "Aurangzeb"], "Shah Jahan",
        "The **Peacock Throne** was made under **Shah Jahan** (by goldsmith Bebadal Khan) — taken away by Nadir Shah in 1739.",
        "Peacock Throne = Shah Jahan → Nadir Shah.", 20)
    S.q("ga-mu-p4", "medium", "Which Mughal emperor had **Guru Tegh Bahadur** executed in 1675?",
        ["Shah Jahan", "Aurangzeb", "Jahangir", "Bahadur Shah I"], "Aurangzeb",
        "**Aurangzeb** executed Guru Tegh Bahadur (the 9th Sikh Guru) in Delhi in **1675**; Guru Arjan Dev had been executed under Jahangir (1606).",
        "Arjan-Jahangir (1606), Tegh Bahadur-Aurangzeb (1675).", 25)
    S.q("ga-mu-p4", "hard", "Consider the statements about the later Mughals:\n1. The Sayyid brothers were called 'king-makers'.\n2. Nadir Shah won the Battle of Karnal (1739).\n3. The Kohinoor was taken to Persia after 1739.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three are standard: the **Sayyid brothers** placed and removed emperors, **Karnal (1739)** opened Delhi to Nadir Shah, and the **Kohinoor** (with the Peacock Throne) went to Persia.",
        "Later-Mughal misery in one chain: Sayyids → Karnal → loot.", 30)
    return S
