"""art-culture deep content — part 2: paintings-crafts, architecture, festivals-fairs, unesco-institutions."""
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


def build_paintings():
    S = Sub("paintings-crafts")
    S.notes = """### Folk and tribal paintings → state
| Painting | State | Hallmark |
|---|---|---|
| **Madhubani (Mithila)** | **Bihar** | Women's wall art; double-line work; GI tag |
| **Warli** | Maharashtra | White rice-paste stick figures on mud walls |
| **Pattachitra** | Odisha (also WB) | Cloth/palm-leaf scrolls of Jagannath iconography |
| **Phad** | Rajasthan | Long cloth scrolls of Pabuji/Devnarayan epics |
| **Kalamkari** | Andhra Pradesh / Telangana | Pen-drawn (Srikalahasti) or block-printed (Machilipatnam) |
| **Gond** | Madhya Pradesh | Tribal dot-and-dash pattern painting |
| **Thangka** | Ladakh / Sikkim | Buddhist cloth scrolls used in worship |
| **Cheriyal** | Telangana | Brightly coloured story scrolls |
| **Pichwai** | Rajasthan (Nathdwara) | Backdrop paintings of Srinathji (Krishna) |

### Miniature schools
**Mughal** painting — founded under **Akbar** (*Hamzanama* workshops), peaked under **Jahangir** (portraits, naturalism). **Rajasthani** schools (Mewar, Kishangarh — the Bani-Thani style). **Pahari** schools of the Himalayan foothills — **Kangra** is the most celebrated, with Radha-Krishna themes. **Company paintings** (late 18th–19th c.) were made for British patrons. The **Bengal School** — **Abanindranath Tagore** (his *Bharat Mata*, 1905), backed by E.B. Havell and carried by **Nandalal Bose** — answered Western academic style with an Asian idiom. **Raja Ravi Varma** — Kerala's oil painter who fused European realism with Indian subjects through mass lithographs.

### Crafts ↔ place
| Craft | Place |
|---|---|
| **Bidriware** (silver on blackened alloy) | Bidar, Karnataka |
| **Pochampally ikat** | Telangana |
| **Kanjeevaram silk** | Tamil Nadu |
| **Bandhani** (tie-dye) | Rajasthan and Gujarat |
| **Chikankari** (shadow embroidery) | Lucknow |
| **Phulkari** (flower work) | Punjab |
| **Channapatna lacquer toys** | Karnataka |
| **Blue pottery** | Jaipur |
| **Pashmina** shawls | Kashmir |
| **Brass ware** | Moradabad, UP |

### Memory hooks
Wall-women-Mithila = Madhubani (Bihar). White-on-mud = Warli. Jagannath scroll = Pattachitra. Silver-on-black = Bidri. Tie-dye = Bandhani. Kalamkari literally = pen-work (kalam = pen). Nathdwara backdrop = Pichwai.

### Quick revision
- Madhubani-Bihar; Warli-Maharashtra; Pattachitra-Odisha; Phad-Rajasthan; Gond-MP; Thangka-Ladakh.
- Mughal: Akbar founds (Hamzanama), Jahangir peaks; Kangra = Pahari gem.
- Bengal School: Abanindranath Tagore (Bharat Mata 1905), Nandalal Bose.
- Bidri-Bidar; Chikankari-Lucknow; Phulkari-Punjab; Pochampally-Telangana."""
    S.pattern("ga-pa-p1", "Painting ↔ state", "very common",
      "A folk painting (Madhubani, Warli, Pattachitra, Phad) with four states, or a match-the-column of paintings and states.",
      "Fix the big five: Madhubani-Bihar, Warli-Maharashtra, Pattachitra-Odisha, Phad-Rajasthan, Gond-Madhya Pradesh; Thangka points to the Buddhist Himalaya (Ladakh/Sikkim).",
      "**Madhubani (Mithila)** painting is native to —",
      "**Bihar** — the Mithila region; traditionally women's wall art.")
    S.pattern("ga-pa-p2", "Craft ↔ place / GI tag", "very common",
      "A craft with a place question — Bidriware, Chikankari, Pochampally, Channapatna — or a GI-tag pairing.",
      "Bidriware-Bidar (Karnataka), Chikankari-Lucknow, Phulkari-Punjab, Pochampally ikat-Telangana, Channapatna toys-Karnataka, Blue pottery-Jaipur, Kanjeevaram-Tamil Nadu.",
      "**Bidriware**, with silver inlay on blackened metal, comes from —",
      "**Bidar, Karnataka** — the craft is named after the town.")
    S.pattern("ga-pa-p3", "Painting ↔ feature / theme", "common",
      "A described hallmark — white stick figures, Jagannath scrolls, Pabuji epic cloth, pen-work cotton.",
      "Warli = white rice-paste figures; Pattachitra = Jagannath iconography on cloth/palm leaf; Phad = Pabuji epic scroll; Kalamkari = kalam (pen) work; Pichwai = Srinathji backdrop.",
      "White rice-paste **stick figures** on mud walls identify —",
      "**Warli** painting of Maharashtra.")
    S.pattern("ga-pa-p4", "Miniature schools & painters", "common",
      "Mughal painting under which emperor, the Kangra school, Bengal School painters, Raja Ravi Varma's medium.",
      "Mughal: Akbar founds (Hamzanama), Jahangir peaks. Pahari: Kangra. Bengal School: Abanindranath Tagore + Nandalal Bose. Ravi Varma = oil + lithography.",
      "The ***Hamzanama*** series of paintings was produced under —",
      "**Akbar** — the founding commission of Mughal painting.")

    S.q("ga-pa-p1", "easy", "**Pattachitra**, scroll painting with Jagannath iconography, belongs mainly to —",
        ["Odisha", "Kerala", "Gujarat", "Punjab"], "Odisha",
        "**Pattachitra** — Odisha's cloth and palm-leaf painting tradition centred on Puri's Jagannath cult.",
        "Pattachitra = Odisha.", 15)
    S.q("ga-pa-p1", "easy", "**Gond** tribal painting is associated with —",
        ["Madhya Pradesh", "Bihar", "Rajasthan", "West Bengal"], "Madhya Pradesh",
        "**Gond** painting — the dot-and-line tribal art of the Gond community of central India (MP).",
        "Gond = MP (central India).", 15)
    S.q("ga-pa-p1", "medium", "**Thangka** paintings, used as devotional objects in monasteries, belong to the tradition of —",
        ["Buddhist Himalayan regions", "Deccan sultanates", "Chola temples", "Maratha courts"], "Buddhist Himalayan regions",
        "**Thangka** — consecrated cloth scrolls of Ladakh, Sikkim and the Tibetan Buddhist world.",
        "Thangka = Buddhist Himalaya.", 25)
    S.q("ga-pa-p1", "medium", "**Phad**, the painted narrative scroll of the Pabuji epic, is a tradition of —",
        ["Rajasthan", "Maharashtra", "Telangana", "Odisha"], "Rajasthan",
        "**Phad** — Rajasthan's bhopa priests unroll the painted scroll while singing the Pabuji/Devnarayan epic.",
        "Phad = Rajasthan scroll.", 25)
    S.q("ga-pa-p2", "easy", "**Chikankari**, the shadow-work embroidery, is a craft of —",
        ["Lucknow", "Jaipur", "Surat", "Mysuru"], "Lucknow",
        "**Chikankari** — Lucknow's whitework embroidery, once associated with Mughal court dress.",
        "Chikankari = Lucknow.", 15)
    S.q("ga-pa-p2", "medium", "**Pochampally**, famous for ikat weave with GI status, is in —",
        ["Telangana", "Karnataka", "Andhra Pradesh", "Odisha"], "Telangana",
        "**Pochampally ikat** — the Telangana village whose tie-and-dye weave carries a GI tag.",
        "Pochampally = Telangana ikat.", 25)
    S.q("ga-pa-p2", "easy", "**Channapatna**, known for lacquered wooden toys, lies in —",
        ["Karnataka", "Tamil Nadu", "Kerala", "Maharashtra"], "Karnataka",
        "**Channapatna** (Ramanagara district, Karnataka) — 'toy town' with a GI-tagged lacquer-ware tradition.",
        "Channapatna toys = Karnataka.", 15)
    S.q("ga-pa-p3", "medium", "The name **Kalamkari** literally refers to —",
        ["Pen-work (kalam) on cloth", "Flower motif work", "Stone inlay", "Tie-dye"], "Pen-work (kalam) on cloth",
        "**Kalam** = pen: the Srikalahasti style is hand-drawn with a bamboo pen; the Machilipatnam style uses block prints.",
        "Kalamkari = pen work.", 25)
    S.q("ga-pa-p3", "medium", "**Pichwai** paintings, made as backdrops for the deity Srinathji, belong to —",
        ["Nathdwara, Rajasthan", "Puri, Odisha", "Madurai, Tamil Nadu", "Nalanda, Bihar"], "Nathdwara, Rajasthan",
        "**Pichwai** — Nathdwara's painted curtains/backdrops behind the idol of Srinathji (Krishna).",
        "Pichwai = Nathdwara backdrop.", 25)
    S.q("ga-pa-p4", "easy", "Mughal painting is said to have **peaked under Jahangir**; it was **founded** under —",
        ["Akbar", "Humayun", "Shah Jahan", "Babur"], "Akbar",
        "Akbar founded the imperial atelier (the *Hamzanama*); Jahangir's reign brought portraiture and naturalism to their peak. (Humayun did bring the Persian masters, but the workshop flourished under Akbar.)",
        "Akbar founds, Jahangir refines.", 15)
    S.q("ga-pa-p4", "medium", "The painting ***Bharat Mata* (1905)**, icon of the Swadeshi era, was painted by —",
        ["Abanindranath Tagore", "Nandalal Bose", "Raja Ravi Varma", "Amrita Sher-Gil"], "Abanindranath Tagore",
        "**Abanindranath Tagore** — founder of the Bengal School; Nandalal Bose carried the school forward.",
        "Bharat Mata 1905 = Abanindranath.", 25)
    S.q("ga-pa-p4", "medium", "**Raja Ravi Varma**, famed for realistic depictions of Indian subjects, worked mainly in —",
        ["Oil painting and lithography", "Fresco", "Palm-leaf engraving", "Wood carving"], "Oil painting and lithography",
        "The Kerala painter fused European academic realism with Indian themes; his press made his gods and heroines mass-market lithographs.",
        "Ravi Varma = oil + litho.", 25)
    return S


def build_architecture():
    S = Sub("architecture")
    S.notes = """### The three temple styles
| Style | Region | Hallmark | Examples |
|---|---|---|---|
| **Nagara** | North | Curvilinear **shikhara** over the sanctum; **amalaka** on top; no boundary wall | Khajuraho (Chandela), Konark, Lingaraja (Bhubaneswar), Modhera Sun Temple |
| **Dravida** | South | Pyramid **vimana**, towering **gopuram** gateways, enclosed courts | Brihadeeswara (Thanjavur), Meenakshi (Madurai), Srirangam |
| **Vesara** | Deccan | Hybrid of the two | Chalukya (Pattadakal, Badami), **Hoysala** (Belur, Halebidu, Somanathapura) |

Feature sort: **shikhara** = north's curving tower; **vimana** = the south's pyramidal tower **above the sanctum**; **gopuram** = the monumental gateway of south temples; **mandapa** = pillared hall.

### Monument ↔ builder
| Monument | Builder / period |
|---|---|
| Brihadeeswara, Thanjavur (Rajrajeswara) | **Rajaraja I**, Chola (c. 1010 CE) |
| Gangaikonda Cholapuram | **Rajendra I**, Chola |
| **Sun Temple, Konark** | **Narasimhadeva I**, Eastern Ganga (13th c.) |
| Sun Temple, Modhera | **Bhima I**, Solanki (Chaulukya) |
| Kailasa temple, Ellora (rock-cut) | **Krishna I**, Rashtrakuta |
| Chennakesava, Belur | **Vishnuvardhana**, Hoysala (1117) |
| Hoysaleswara, Halebidu | Hoysala kings |
| Kesava, Somanathapura | Hoysala (Narasimha III's reign, 1268) |
| Dilwara Jain temples, Mt Abu | Solanki period (Vimal Shah's Vimal Vasahi) |
| Meenakshi temple, Madurai | Nayak rulers (gopurams restored/expanded) |
| Mahabalipuram rathas & Shore Temple | **Pallavas** — Narasimhavarman I (Mamalla) and Rajasimha |

### Rock-cut caves
**Ajanta** — Buddhist, painted frescoes (Bodhisattva Padmapani), two phases (Satavahana c. 2nd c. BCE; Vakataka 5th c. CE). **Ellora** — Buddhist-Hindu-Jain together; the **Kailasa** temple carved top-down from one rock under **Rashtrakuta Krishna I**. **Elephanta** — mid-first-millennium rock-cut Shiva (Maheshmurti) island caves near Mumbai. **Mahabalipuram** — Pallava monolithic **rathas** and the Shore Temple. **Chaitya** = prayer hall; **vihara** = monastery — the Buddhist cave pair (Karle chaitya, Ajanta viharas).

### Quick revision
- Nagara = shikhara (north); Dravida = vimana + gopuram (south); Vesara = hybrid (Deccan).
- Konark = Narasimhadeva I; Brihadeeswara = Rajaraja I; Modhera = Bhima I.
- Kailasa (Ellora) = Krishna I, Rashtrakuta — carved top-down.
- Belur/Halebidu/Somanathapura = Hoysala; Pattadakal = Chalukya (UNESCO 1987).
- Ajanta = Buddhist frescoes; chaitya = hall, vihara = monastery."""
    S.pattern("ga-ar-p1", "Style ↔ region / feature", "very common",
      "'Gopurams are a feature of which style', or a style-region pairing with four options.",
      "Nagara = curvilinear shikhara, north; Dravida = vimana + gopuram, south; Vesara = hybrid, Deccan (Chalukya-Hoysala). Any 'gopuram' question points south.",
      "The **shikhara** (curvilinear tower) is the hallmark of which temple style?",
      "**Nagara** — north Indian temples, crowned with the amalaka.")
    S.pattern("ga-ar-p2", "Monument ↔ builder / dynasty", "very common",
      "'The Sun Temple at Konark was built by', 'Brihadeeswara was constructed under', and match-the-column of temples and builders.",
      "Six pairs settle most questions: Konark-Narasimhadeva I (Eastern Ganga), Brihadeeswara-Rajaraja I (Chola), Modhera-Bhima I (Solanki), Kailasa-Krishna I (Rashtrakuta), Belur-Vishnuvardhana (Hoysala), Mahabalipuram-Pallavas.",
      "The **Kailasa temple at Ellora** was carved under —",
      "**Rashtrakuta king Krishna I** — cut top-down from a single rock.")
    S.pattern("ga-ar-p3", "Caves ↔ period / religion", "common",
      "Ajanta vs Ellora statements, which dynasty cut Ellora's Kailasa, the religion mix at Ellora, Elephanta's deity.",
      "Ajanta = Buddhist, painted (two phases, Satavahana + Vakataka); Ellora = Buddhist + Hindu + Jain (Rashtrakuta); Elephanta = Shiva Maheshmurti; Mahabalipuram = Pallava monoliths.",
      "Which statement about **Ellora** is correct?",
      "Its caves serve **Buddhist, Hindu and Jain** worship — carved mainly under the Rashtrakutas.")
    S.pattern("ga-ar-p4", "Feature / part ↔ name", "common",
      "Definitions in disguise: what is a vimana, gopuram, mandapa, chaitya, vihara, amalaka.",
      "vimana = tower above the sanctum (south); gopuram = gateway tower; mandapa = pillared hall; chaitya = prayer hall; vihara = monastery; amalaka = ribbed stone cap on northern shikharas.",
      "In south Indian temples, the tower **above the sanctum** is called —",
      "The **vimana** — gateway towers are gopurams, not vimanas.")

    S.q("ga-ar-p1", "easy", "Towering **gopurams** are a characteristic feature of which temple architecture?",
        ["Dravida", "Nagara", "Vesara", "Kalinga"], "Dravida",
        "**Gopurams** — the colossal gateway towers of south Indian (Dravida) temples, e.g. Meenakshi, Srirangam.",
        "Gopuram = Dravida gateway.", 15)
    S.q("ga-ar-p1", "medium", "**Vesara**, the hybrid temple style mixing Nagara and Dravida elements, flourished under —",
        ["Chalukyas and Hoysalas", "Cholas and Pandyas", "Guptas and Mauryas", "Palas and Senas"], "Chalukyas and Hoysalas",
        "**Vesara** — the Deccan style of the Chalukyas (Pattadakal, Badami) perfected by the Hoysalas (Belur, Halebidu).",
        "Vesara = Deccan hybrid.", 25)
    S.q("ga-ar-p1", "medium", "The **Lingaraja temple** at Bhubaneswar follows which style?",
        ["Nagara (Kalinga variant)", "Dravida", "Vesara", "Bengal style"], "Nagara (Kalinga variant)",
        "Odisha's temples (Lingaraja, Konark, Jagannath Puri) follow the **Kalinga** — an eastern branch of the Nagara style with deul towers.",
        "Bhubaneswar = Kalinga-Nagara.", 25)
    S.q("ga-ar-p2", "easy", "The **Brihadeeswara temple** at Thanjavur was built by —",
        ["Rajaraja I", "Rajendra I", "Krishnadeva Raya", "Mahendravarman"], "Rajaraja I",
        "**Rajaraja I** raised the Chola's Rajrajeswara temple around 1010 CE; his son Rajendra I built Gangaikonda Cholapuram.",
        "Thanjavur = Rajaraja I.", 15)
    S.q("ga-ar-p2", "medium", "The **Chennakesava temple at Belur** was commissioned by the Hoysala king —",
        ["Vishnuvardhana", "Ballala III", "Narasimha I", "Rajaraja I"], "Vishnuvardhana",
        "**Vishnuvardhana** built Belur's Chennakesava (c. 1117); Halebidu and Somanathapura complete the Hoysala trio.",
        "Belur = Vishnuvardhana.", 25)
    S.q("ga-ar-p2", "medium", "The **Sun Temple at Modhera** (Gujarat) was built by —",
        ["Bhima I of the Solanki dynasty", "Narasimhadeva I", "Krishna I", "Chandragupta II"], "Bhima I of the Solanki dynasty",
        "**Bhima I** (Chaulukya-Solanki) built Modhera; the Konark Sun Temple belongs to Narasimhadeva I — don't swap the two sun temples.",
        "Modhera = Solanki; Konark = Ganga.", 25)
    S.q("ga-ar-p2", "medium", "The **Dilwara Jain temples** at Mount Abu were built during the reign of the —",
        ["Solanki (Chaulukya) dynasty", "Chauhan dynasty", "Paramara dynasty", "Gahadavala dynasty"], "Solanki (Chaulukya) dynasty",
        "The marble Jain temples — Vimal Vasahi built by minister Vimal Shah under **Bhima I's Solanki rule**.",
        "Dilwara = Solanki era.", 25)
    S.q("ga-ar-p3", "medium", "The **Ajanta caves**, famous for frescoes like the Bodhisattva Padmapani, are devoted to —",
        ["Buddhism", "Jainism", "Shaivism", "Vaishnavism"], "Buddhism",
        "**Ajanta** — purely Buddhist, in two phases (Satavahana, then Vakataka 5th century); painting is its glory.",
        "Ajanta = Buddhist paintings.", 20)
    S.q("ga-ar-p3", "medium", "**Elephanta caves**, with the great Maheshmurti of Shiva, lie near —",
        ["Mumbai", "Goa", "Pune", "Aurangabad"], "Mumbai",
        "**Elephanta** — the island caves in Mumbai harbour; a mid-first-millennium rock-cut Shiva complex (UNESCO 1987).",
        "Elephanta = Mumbai harbour.", 20)
    S.q("ga-ar-p3", "hard", "Consider the statements:\n1. Ellora's Kailasa temple was carved top-down from one rock.\n2. Ajanta's caves were made in two distinct phases.\n3. Ellora has only Buddhist caves.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Ellora includes **Hindu, Buddhist and Jain** caves — statement 3 fails. The top-down Kailasa cut and Ajanta's Satavahana + Vakataka phases are correct.",
        "Ellora is three-religion — 3 is the false one.", 30)
    S.q("ga-ar-p4", "easy", "In Buddhist architecture, the **chaitya** was the —",
        ["Prayer hall", "Monastery", "Stupa umbrella", "Stone fence"], "Prayer hall",
        "**Chaitya** = congregational prayer hall (apse-ended, pillared); **vihara** = the monks' monastery.",
        "Chaitya prays, vihara houses.", 15)
    S.q("ga-ar-p4", "medium", "The ribbed stone **amalaka** crowns the shikhara of which temples?",
        ["North Indian (Nagara)", "South Indian (Dravida)", "Bengal terracotta", "Kerala wooden"], "North Indian (Nagara)",
        "The **amalaka** — a ribbed, myrobalan-shaped cap topped by a kalasha — sits on the northern shikhara.",
        "Amalaka = Nagara crown.", 25)
    S.q("ga-ar-p4", "hard", "Match:\n1. Konark — Narasimhadeva I\n2. Gangaikonda Cholapuram — Rajendra I\n3. Meenakshi gopurams — Nayak rulers\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three correct: Konark (Eastern Ganga), the Chola's second capital temple (Rajendra I), and Madurai's towering gopurams rebuilt by the Nayaks.",
        "Konark-Cholapuram-Madurai: all pair true.", 30)
    return S


def build_festivals():
    S = Sub("festivals-fairs")
    S.notes = """### Festival ↔ state — the core table
| Festival | State | Note |
|---|---|---|
| **Onam** | Kerala | King Mahabali's homecoming; Vallam Kali boat race; pookalam |
| **Pongal** | Tamil Nadu | Mid-January harvest; four days; Jallikattu |
| **Baisakhi** | Punjab | April harvest; Khalsa founding (1699) |
| **Bihu** | Assam | Rongali (spring) the famous one |
| **Durga Puja** | West Bengal | UNESCO ICH 2021 |
| **Ganesh Chaturthi** | Maharashtra | Public sarvajanik utsav (Tilak's mobilisation) |
| **Chhath** | Bihar / Jharkhand | Sun (Surya) worship at rivers, Kartik Shukla Shashthi |
| **Hornbill** | Nagaland | 1–10 December, Kisama; 'festival of festivals' |
| **Losar** | Ladakh / Arunachal | Tibetan new year |
| **Wangala** | Meghalaya | Garo harvest festival |
| **Sarhul** | Jharkhand | Tribal spring festival of the sal tree |
| **Makar Sankranti / Lohri** | Pan-India / Punjab | Lohri falls the night before Sankranti |

### Fairs (melas)
**Kumbh Mela** — rotates among **Prayagraj, Haridwar, Ujjain and Nashik** (UNESCO ICH 2017). **Pushkar** (Rajasthan) — Kartik Purnima camel and livestock fair at the only Brahma temple. **Sonepur** (Bihar) — one of Asia's largest cattle fairs at the Gandak-Ganga confluence. **Nauchandi** (Meerut, UP).

### Season logic
Most Indian festivals are harvest-tied: Pongal (mid-Jan, Tamil Thai month), Baisakhi (mid-April), Bihu (April), Onam (Aug–Sep, Chingam), Wangala (autumn). Winter-solstice cluster: Lohri → Makar Sankranti → Pongal → Bihu within a day or two.

### UNESCO ICH elements of India
**Kutiyattam** (Sanskrit theatre, 2001 — the first), **Ramlila** and the **Vedic chanting** tradition (2008), **Chhau, Kalbelia, Mudiyettu** (2010), **Sankirtana** of Manipur (2013), **Yoga** (2016), **Kumbh Mela** (2017), **Durga Puja in Kolkata** (2021), **Garba of Gujarat** (2023), **Ramman** (Garhwal, 2009 — festival-theatre).

### Two questions that repeat
1. **Which city does not host the Kumbh?** The four are Prayagraj, Haridwar, Ujjain and Nashik — Varanasi, Ayodhya and Mathura are the decoys.
2. **Which dance belongs to which festival?** Garba-Navratri, Bhangra-Baisakhi, Bihu-Rongali Bihu, Jallikattu-Pongal, Vallam Kali-Onam. Pair them and half the festival questions answer themselves.

### Quick revision
- Onam-Kerala (Mahabali, Vallam Kali); Pongal-TN (Jan); Baisakhi-Punjab (Khalsa 1699).
- Chhath = Bihar sun worship; Hornbill = Nagaland, Dec; Losar = Ladakh new year.
- Kumbh: Prayagraj-Haridwar-Ujjain-Nashik; Pushkar = camel fair; Sonepur = Bihar cattle.
- ICH ladder: Kutiyattam 2001 → Ramlila/Veda 2008 → Chhau-Kalbelia-Mudiyettu 2010 → Sankirtana 2013 → Yoga 2016 → Kumbh 2017 → Durga Puja 2021 → Garba 2023."""
    S.pattern("ga-fe-p1", "Festival ↔ state", "very common",
      "A festival with four states as options — Onam, Pongal, Chhath, Hornbill, Bihu and friends.",
      "Pin the one-to-one pairs: Onam-Kerala, Pongal-TN, Chhath-Bihar, Hornbill-Nagaland, Bihu-Assam, Durga Puja-WB, Losar-Ladakh, Wangala-Meghalaya, Sarhul-Jharkhand.",
      "**Chhath**, the sun-worship festival, is most identified with —",
      "**Bihar** (and eastern UP/Jharkhand) — offerings to Surya at river ghats.")
    S.pattern("ga-fe-p2", "Fair ↔ place", "common",
      "Pushkar, Sonepur, Kumbh-location questions, or 'which fair is famous for camels/cattle'.",
      "Kumbh rotates: Prayagraj, Haridwar, Ujjain, Nashik. Pushkar = camels (Rajasthan); Sonepur = cattle (Bihar); Nauchandi = Meerut.",
      "The **Pushkar fair**, famous for its camel trading, is held in —",
      "**Rajasthan** — around Kartik Purnima at the Brahma temple town.")
    S.pattern("ga-fe-p3", "Festival ↔ season / harvest", "common",
      "Which festival falls in January/April, harvest-festival clusters, or ordering Lohri-Sankranti-Pongal.",
      "January cluster: Lohri (13th night before) → Makar Sankranti/Pongal (14–15th) → Bihu (Rongali is April, not January). April harvest: Baisakhi, Bihu.",
      "Which festival falls **immediately after Lohri** in mid-January?",
      "**Makar Sankranti** (celebrated as Pongal in Tamil Nadu).")
    S.pattern("ga-fe-p4", "UNESCO ICH elements", "common",
      "'Which Indian element entered the UNESCO Intangible Cultural Heritage list in…', or matching elements to years.",
      "Keep the ladder: Kutiyattam 2001 (first), Ramlila + Vedic chanting 2008, Chhau-Kalbelia-Mudiyettu 2010, Sankirtana 2013, Yoga 2016, Kumbh 2017, Durga Puja 2021, Garba 2023.",
      "Which was the **first Indian element** on UNESCO's Intangible Cultural Heritage list?",
      "**Kutiyattam** — Sanskrit theatre (2001).")

    S.q("ga-fe-p1", "easy", "**Onam**, celebrating King Mahabali's annual homecoming, is the harvest festival of —",
        ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"], "Kerala",
        "**Onam** — Kerala's Chingam-month festival with pookalam flower carpets and the Vallam Kali snake-boat races.",
        "Onam = Kerala.", 15)
    S.q("ga-fe-p1", "easy", "The **Hornbill Festival**, the 'festival of festivals', is held every December in —",
        ["Nagaland", "Manipur", "Meghalaya", "Mizoram"], "Nagaland",
        "**Hornbill** — 1–10 December at Kisama near Kohima, showcasing all Nagaland tribes.",
        "Hornbill = Nagaland, Dec.", 15)
    S.q("ga-fe-p1", "medium", "**Losar**, the new-year festival, is celebrated mainly in —",
        ["Ladakh and Arunachal Pradesh", "Kerala and Karnataka", "Odisha and Bengal", "Gujarat and Rajasthan"], "Ladakh and Arunachal Pradesh",
        "**Losar** — the Tibetan Buddhist new year of the trans-Himalayan belt.",
        "Losar = Tibetan new year.", 25)
    S.q("ga-fe-p1", "medium", "**Sarhul**, the spring festival worshipping the sal tree, belongs to the tribal culture of —",
        ["Jharkhand", "Punjab", "Assam", "Goa"], "Jharkhand",
        "**Sarhul** — Jharkhand's adivasi spring festival centred on the sal tree and nature worship.",
        "Sarhul = Jharkhand, sal tree.", 25)
    S.q("ga-fe-p1", "medium", "**Wangala**, the hundred-drum harvest festival, is celebrated by the **Garo** community of —",
        ["Meghalaya", "Nagaland", "Tripura", "Manipur"], "Meghalaya",
        "**Wangala** — the Garos of Meghalaya thank the sun god Misi Sal after harvest.",
        "Wangala = Garo = Meghalaya.", 25)
    S.q("ga-fe-p2", "easy", "The **Kumbh Mela** does NOT rotate through which city?",
        ["Varanasi", "Prayagraj", "Haridwar", "Ujjain"], "Varanasi",
        "The four Kumbh venues: **Prayagraj, Haridwar, Ujjain, Nashik** — Varanasi is not one.",
        "Kumbh = 4 cities; Varanasi isn't one.", 15)
    S.q("ga-fe-p2", "medium", "The **Sonepur fair**, one of Asia's largest cattle fairs, is held in —",
        ["Bihar", "Rajasthan", "Madhya Pradesh", "Haryana"], "Bihar",
        "**Sonepur** (near Patna) — at the Gandak-Ganga confluence; Pushkar in Rajasthan is the camel fair, Sonepur the elephant-cattle fair.",
        "Sonepur cattle = Bihar.", 25)
    S.q("ga-fe-p3", "medium", "**Jallikattu**, the bull-embracing sport, is associated with which festival?",
        ["Pongal", "Onam", "Baisakhi", "Bihu"], "Pongal",
        "**Jallikattu** — Tamil Nadu's bull sport during the Pongal season (Mattu Pongal).",
        "Jallikattu = Pongal season.", 20)
    S.q("ga-fe-p3", "hard", "Arrange by calendar:\n1. Baisakhi\n2. Pongal\n3. Onam\n4. Rongali Bihu\nWhich order is correct?",
        ["2, 1, 4, 3", "1, 2, 3, 4", "2, 4, 1, 3", "4, 2, 1, 3"], "2, 1, 4, 3",
        "Pongal (mid-Jan) → Baisakhi (mid-Apr) → Rongali Bihu (mid-Apr, days after Baisakhi) → Onam (Aug–Sep).",
        "Jan → Apr → Apr → Aug-Sep.", 30)
    S.q("ga-fe-p4", "easy", "**Durga Puja** of Kolkata entered the UNESCO Intangible Cultural Heritage list in —",
        ["2021", "2017", "2019", "2023"], "2021",
        "**Durga Puja in Kolkata** — inscribed in **2021**; Garba followed in 2023.",
        "Durga Puja = 2021.", 15)
    S.q("ga-fe-p4", "medium", "**Ramman**, the ritual festival-theatre of Garhwal on the UNESCO ICH list, belongs to —",
        ["Uttarakhand", "Himachal Pradesh", "Jammu region", "Nepal border areas"], "Uttarakhand",
        "**Ramman** — the Salur-dun village ritual of Garhwal, **Uttarakhand**, inscribed in **2009**.",
        "Ramman = Garhwal = Uttarakhand.", 25)
    S.q("ga-fe-p4", "hard", "Match the ICH inscriptions:\n1. Yoga — 2016\n2. Kumbh Mela — 2017\n3. Sankirtana — Manipur, 2013\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are right: Yoga (2016), Kumbh Mela (2017), and Manipur's **Sankirtana** (2013).",
        "2016-2017-2013: all true.", 30)
    return S


def build_unesco():
    S = Sub("unesco-institutions")
    S.notes = """### India's World Heritage Sites — the landscape
India holds **45 World Heritage Sites** (37 cultural, 7 natural, 1 mixed — **Khangchendzonga National Park**, Sikkim, 2016). The 1983 founding batch: **Taj Mahal, Agra Fort, Ajanta, Ellora**. Recent cultural inscriptions: **Ramappa (Rudreswara) Temple** and **Dholavira** (both 2021), **Santiniketan** and the **Sacred Ensembles of the Hoysalas** (2023), the **Moidams** of Assam (2024), **Maratha Military Landscapes** (2025) and the **Ancient Buddhist Site of Sarnath** (2026). India's first city WHS is **Ahmedabad** (2017); Jaipur followed (2019).

### Natural and mixed sites
Natural: **Kaziranga, Manas, Keoladeo, Sundarbans** (East), **Nanda Devi**, **Western Ghats**, **Great Himalayan National Park**. Mixed: only **Khangchendzonga**.

### Cultural institutions
| Institution | Founded | Note |
|---|---|---|
| **Archaeological Survey of India (ASI)** | 1861 | Custodian of monuments; Alexander Cunningham first DG |
| **Sangeet Natak Akademi** | 1953 | Performing arts; New Delhi |
| **Sahitya Akademi** | 1954 | Literature |
| **Lalit Kala Akademi** | 1954 | Fine arts |
| **FTII** | 1960 | Film and Television Institute of India, Pune |
| **INTACH** | 1984 | Indian National Trust for Art and Cultural Heritage |
| **IGNCA** | 1987 | Indira Gandhi National Centre for the Arts, New Delhi |

The three Akademis (Sangeet Natak, Sahitya, Lalit Kala) are the National Akademies set up in the 1950s — Sangeet Natak first (1953).

### Memory hooks
- 1983 = Taj + Agra Fort + Ajanta + Ellora (the first four).
- 2021 = Ramappa + Dholavira; 2023 = Santiniketan + Hoysala Ensembles.
- Mixed = Khangchendzonga only. Natural quartet of the East: Kaziranga, Manas, Keoladeo, Sundarbans.
- Akademis: Sangeet Natak 1953, Sahitya + Lalit Kala 1954; ASI 1861 (Cunningham).

### How the questions are built
Most WHS questions test one of three things: **the state** (Ramappa-Telangana, Dholavira-Gujarat, Santiniketan-Bengal, Hoysalas-Karnataka, Moidams-Assam), **the year** (the 2021 pair, the 2023 pair), or **the type** (mixed = Khangchendzonga, natural = the wildlife quartet). Institution questions test the **year and the art**: performing arts 1953, literature and fine arts 1954, films 1960, archaeology 1861. Learn each site as a triple — site + state + year — and every variant collapses into recall.

### Quick revision
- 45 WHS = 37 cultural + 7 natural + 1 mixed (Khangchendzonga).
- First four (1983): Taj, Agra Fort, Ajanta, Ellora.
- 2021: Ramappa (Telangana), Dholavira (Gujarat); 2023: Santiniketan, Hoysalas.
- ASI 1861 Cunningham; SNA 1953; Sahitya + Lalit Kala 1954; FTII 1960 Pune."""
    S.pattern("ga-un-p1", "WHS ↔ state / year", "very common",
      "'Ramappa temple is in which state', 'Dholavira WHS is in', recent-inscription year questions.",
      "Ramappa-Telangana, Dholavira-Gujarat (both 2021); Santiniketan-WB, Hoysala Ensembles-Karnataka (2023); Moidams-Assam (2024).",
      "The **Ramappa (Rudreswara) temple**, a UNESCO WHS of 2021, is in —",
      "**Telangana** — the Kakatiya-era temple at Palampet.")
    S.pattern("ga-un-p2", "Institution ↔ founding / purpose", "common",
      "ASI's year and first head, which Akademi handles which art, FTII's city.",
      "ASI 1861 (Cunningham first DG); Sangeet Natak Akademi 1953 (performing arts); Sahitya 1954 (literature); Lalit Kala 1954 (fine arts); FTII 1960 Pune.",
      "The **Archaeological Survey of India** was founded in —",
      "**1861**, with Alexander Cunningham as its first Director-General.")
    S.pattern("ga-un-p3", "WHS ↔ natural / mixed / cultural", "common",
      "Statement questions on which sites are natural, or which is India's only mixed site.",
      "Mixed = Khangchendzonga NP only. Natural set: Kaziranga, Manas, Keoladeo, Sundarbans, Nanda Devi, Western Ghats, Great Himalayan NP. Everything else cultural.",
      "Which is India's **only mixed** World Heritage Site?",
      "**Khangchendzonga National Park**, Sikkim (2016).")
    S.pattern("ga-un-p4", "Firsts and inscription order", "common",
      "'India's first WHS were inscribed in…', first heritage city, or ordering recent inscriptions.",
      "First four: 1983 (Taj, Agra Fort, Ajanta, Ellora). First city: Ahmedabad 2017 (Jaipur 2019). Recent run: 2021 Ramappa-Dholavira → 2023 Santiniketan-Hoysala → 2024 Moidams.",
      "India's **first heritage city** on the WHS list is —",
      "**Ahmedabad** (2017); Jaipur joined in 2019.")

    S.q("ga-un-p1", "easy", "**Dholavira**, the Harappan city inscribed as a UNESCO WHS in 2021, is in —",
        ["Gujarat", "Rajasthan", "Punjab", "Haryana"], "Gujarat",
        "**Dholavira** (Rann of Kachchh, Gujarat) — 2021's second Indian inscription with Ramappa.",
        "Dholavira = Gujarat.", 15)
    S.q("ga-un-p1", "medium", "**Santiniketan**, Rabindranath Tagore's university town, was inscribed as a UNESCO WHS in —",
        ["2023", "2021", "2019", "2017"], "2023",
        "**Santiniketan** (West Bengal) — inscribed in **2023**, the same year as the Sacred Ensembles of the Hoysalas.",
        "Santiniketan = 2023.", 25)
    S.q("ga-un-p1", "medium", "The **Sacred Ensembles of the Hoysalas** (Belur, Halebidu, Somanathapura) are located in —",
        ["Karnataka", "Tamil Nadu", "Andhra Pradesh", "Kerala"], "Karnataka",
        "The Hoysala temples — Belur, Halebidu, Somanathapura — all in **Karnataka**, inscribed in 2023.",
        "Hoysalas = Karnataka.", 25)
    S.q("ga-un-p1", "hard", "Arrange the recent Indian WHS inscriptions:\n1. Santiniketan\n2. Ramappa temple\n3. Moidams of Assam\n4. Dholavira",
        ["2 and 4 in 2021, then 1, then 3", "1, 2, 3, 4", "4, 3, 2, 1", "2, 1, 4, 3"], "2 and 4 in 2021, then 1, then 3",
        "Ramappa + Dholavira (2021) → Santiniketan (2023) → Moidams (2024).",
        "2021 pair → 2023 → 2024.", 30)
    S.q("ga-un-p2", "easy", "The **Sangeet Natak Akademi**, India's national academy of performing arts, was set up in —",
        ["1953", "1949", "1961", "1957"], "1953",
        "**SNA 1953** — a year before the Sahitya (1954) and Lalit Kala (1954) Akademis.",
        "Sangeet Natak = 1953, first Akademi.", 15)
    S.q("ga-un-p2", "medium", "The **Film and Television Institute of India (FTII)** is located at —",
        ["Pune", "Mumbai", "Chennai", "Kolkata"], "Pune",
        "**FTII (1960)** — on the former Prabhat Studio campus in Pune.",
        "FTII = Pune.", 20)
    S.q("ga-un-p2", "medium", "Which Akademi is concerned with **fine arts (painting, sculpture, graphics)**?",
        ["Lalit Kala Akademi", "Sahitya Akademi", "Sangeet Natak Akademi", "National School of Drama"], "Lalit Kala Akademi",
        "**Lalit Kala Akademi (1954)** = visual arts; Sahitya = literature; Sangeet Natak = music-dance-drama.",
        "Lalit Kala = fine arts.", 25)
    S.q("ga-un-p3", "easy", "Which of the following is a **natural** World Heritage Site of India?",
        ["Kaziranga National Park", "Taj Mahal", "Konark Sun Temple", "Fatehpur Sikri"], "Kaziranga National Park",
        "**Kaziranga** (Assam, 1985) — with Manas, Keoladeo and Sundarbans in the natural list.",
        "Kaziranga = natural.", 15)
    S.q("ga-un-p3", "medium", "**Keoladeo National Park**, a natural WHS famous for birds, is in —",
        ["Rajasthan", "Assam", "West Bengal", "Uttarakhand"], "Rajasthan",
        "**Keoladeo (Bharatpur), Rajasthan** — inscribed 1985; the Sundarbans bird-adjacent natural site is in Bengal.",
        "Keoladeo = Bharatpur = Rajasthan.", 25)
    S.q("ga-un-p3", "hard", "Consider the statements:\n1. Khangchendzonga National Park is India's only mixed WHS.\n2. The Western Ghats are a natural WHS.\n3. Manas National Park is a cultural WHS.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "**Manas is natural**, not cultural — Assam's pair (Kaziranga, Manas) is both natural.",
        "Manas = natural; that kills statement 3.", 30)
    S.q("ga-un-p4", "medium", "India's **first four** World Heritage Sites, inscribed in 1983, included —",
        ["Taj Mahal, Agra Fort, Ajanta, Ellora", "Konark, Khajuraho, Taj, Sanchi", "Taj, Qutb Minar, Ellora, Hampi", "Ajanta, Elephanta, Taj, Mahabalipuram"], "Taj Mahal, Agra Fort, Ajanta, Ellora",
        "The 1983 batch: **Taj Mahal, Agra Fort, Ajanta, Ellora**; Konark and Mahabalipuram followed in 1984.",
        "1983 = Taj + Fort + Ajanta + Ellora.", 25)
    S.q("ga-un-p4", "medium", "The **Archaeological Survey of India's** first Director-General was —",
        ["Alexander Cunningham", "John Marshall", "Lord Curzon", "Mortimer Wheeler"], "Alexander Cunningham",
        "**Alexander Cunningham** — the 'father of Indian archaeology', first DG from 1861.",
        "Cunningham = first DG.", 20)
    S.q("ga-un-p4", "hard", "Match the inscriptions:\n1. Ramappa temple — Telangana, 2021\n2. Maratha Military Landscapes — 2025\n3. Sarnath Buddhist site — 2026\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three: Ramappa (Telangana, 2021), the Maratha fort landscapes of Maharashtra-Tamil Nadu (2025), and Sarnath (2026) — India's most recent inscriptions.",
        "2021-2025-2026: all true.", 30)
    return S
