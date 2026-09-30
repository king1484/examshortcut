"""Readable rewrite of General Awareness > Indian Geography (all 6 subtopics).

Facts are kept exactly as in the existing lessons; wording, order and structure are new.
Old pattern ids are kept; new ids continue each prefix.
Run: python indian_geography.py  (patches content/core/topics/ga/indian-geography.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "indian-geography.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

SUBS["ig-location"] = dict(
    concept=(
        "India lies wholly in the northern and eastern hemispheres. It covers 32.87 lakh sq km, "
        "which is 2.4% of the world's land, and ranks 7th by area. "
        "Most questions ask about the Tropic of Cancer, the Standard Meridian, neighbours, borders and island channels."
    ),
    notes=r"""### Where India sits
India lies wholly in the **Northern and Eastern hemispheres**. The mainland runs from **8°4'N to 37°6'N** (latitude) and **68°7'E to 97°25'E** (longitude).

The **Tropic of Cancer (23.5°N)** cuts the country roughly into two halves. It passes through **8 states**, west to east:

1. Gujarat
2. Rajasthan
3. Madhya Pradesh
4. Chhattisgarh
5. Jharkhand
6. West Bengal
7. Tripura
8. Mizoram

> **Watch:** Odisha, Bihar and Uttar Pradesh are the usual wrong options. The Tropic misses all three.

### Size and the Standard Meridian
India covers about **32.87 lakh sq km**. That is only **2.4%** of the world's land. Yet India holds about **17.5%** of the world's people (Census 2011). By area it is the **7th largest** country.

- Largest state: **Rajasthan**. Second: **Madhya Pradesh**.
- Smallest state: **Goa**.

The Sun rises about two hours earlier in Arunachal Pradesh than in Gujarat. So the whole country follows one reference line, the **Standard Meridian, 82°30'E**. It passes near **Mirzapur** in Uttar Pradesh.

The Meridian crosses 5 states: **Uttar Pradesh, Madhya Pradesh, Chhattisgarh, Odisha and Andhra Pradesh**.

> **Rule:** The Earth turns 1° of longitude in 4 minutes. So 82.5 × 4 = 330 minutes. Indian Standard Time is **GMT + 5:30**.

### Land neighbours and border lengths
India has **7 land neighbours**. It has two sea neighbours: **Sri Lanka** and the **Maldives**. Lengths below are Home Ministry figures.

| Neighbour | Border (km) | Remember |
|---|---|---|
| **Bangladesh** | 4,096.7 | Longest border |
| China | 3,488 | McMahon Line in the east |
| Pakistan | 3,323 | Radcliffe Line (1947) |
| Nepal | 1,751 | Open border |
| Myanmar | 1,643 | |
| Bhutan | 699 | |
| Afghanistan | 106 | Shortest border |

States that touch each neighbour:

- **Bangladesh (5):** West Bengal, Assam, Meghalaya, Tripura, Mizoram.
- **China (5):** Ladakh/J&K, Himachal Pradesh, Uttarakhand, Sikkim, Arunachal Pradesh.
- **Nepal (5):** Uttarakhand, UP, Bihar, West Bengal, Sikkim.
- **Myanmar (4):** Arunachal Pradesh, Nagaland, Manipur, Mizoram.
- **Bhutan (4):** Sikkim, West Bengal, Assam, Arunachal Pradesh.

### Sea around India
The **Arabian Sea** is on the west. The **Bay of Bengal** is on the east. The **Indian Ocean** is to the south. The ocean takes its name from India.

- The coastline was long quoted as **7,516.6 km**.
- A 2024 re-measurement on more detailed maps gives about **11,098 km**.
- On both counts, **Gujarat** has the longest state coastline.

The **Palk Strait** and the **Gulf of Mannar** separate India from Sri Lanka. A chain of shoals called **Adam's Bridge (Ram Setu)** lies between them.

### Island groups and channels
The **Andaman and Nicobar Islands** are about **572 islands**. Only around 38 are inhabited. They are the peaks of a submerged mountain chain.

- **Barren Island** in the Andaman Sea is India's **only active volcano**. Nearby **Narcondam** is dormant.
- **Indira Point** (Great Nicobar) is the southernmost point of India. **Kanyakumari** is the mainland tip.
- **Indira Col** in the Siachen area of Ladakh is the northernmost point.

**Lakshadweep** is a group of **coral islands (atolls)** in the Arabian Sea. Its capital is **Kavaratti**. **Minicoy** is its southernmost island.

| Channel | It separates |
|---|---|
| **Ten Degree** | Andaman from Nicobar |
| **Nine Degree** | Minicoy from the main Lakshadweep group |
| **Eight Degree** | Minicoy from the Maldives |
| **Duncan Passage** | South Andaman from Little Andaman |
| **Coco Channel** | North Andaman from Myanmar's Coco Islands |
| **Great Channel** | Great Nicobar from Sumatra (Indonesia) |

> **Tip:** The numbers fall as you go south-west: Ten, Nine, Eight.
""",
    tricks=[
        {"title": "Tropic of Cancer states: GRM CJ WTM",
         "body": "West to east: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram. Odisha and Bihar are the usual wrong options. The Tropic misses both.",
         "example": {"q": "Does the Tropic of Cancer pass through Odisha?",
                     "steps": ["The Tropic passes through Jharkhand and West Bengal.", "Both lie to the north of Odisha."],
                     "answer": "No."}},
        {"title": "Border order: Big Cats Prowl Near My Big Area",
         "body": "Longest to shortest: Bangladesh, China, Pakistan, Nepal, Myanmar, Bhutan, Afghanistan.",
         "example": {"q": "With which neighbour does India share its shortest land border?",
                     "steps": ["Take the last name in the order.", "Afghanistan has about 106 km."],
                     "answer": "Afghanistan"}},
        {"title": "Channel numbers fall as you go south-west",
         "body": "Ten Degree splits Andaman and Nicobar. Nine Degree splits Minicoy and Lakshadweep. Eight Degree splits Minicoy and the Maldives. The Andaman group has the biggest number."},
    ],
    mistakes=[
        mis("Taking Kanyakumari as India's southernmost point.", "The southernmost point is Indira Point in Great Nicobar. Kanyakumari is the mainland tip."),
        mis("Answering China for the longest land border.", "Bangladesh has the longest border, 4,096.7 km."),
        mis("Placing the Standard Meridian at Prayagraj.", "The reference town is Mirzapur, at 82°30'E."),
        mis("Adding Odisha, Bihar or Uttar Pradesh to the Tropic of Cancer states.", "The Tropic crosses only 8 states. Learn them west to east."),
        mis("Listing Jharkhand among the Meridian states.", "The Meridian crosses UP, MP, Chhattisgarh, Odisha and Andhra Pradesh."),
    ],
    revision=[
        "Lat 8°4'N to 37°6'N; long 68°7'E to 97°25'E. The Tropic of Cancer crosses 8 states, not Odisha, Bihar or UP.",
        "Area 32.87 lakh sq km = 2.4% of world land = 7th largest. Rajasthan largest, MP second, Goa smallest.",
        "Standard Meridian 82°30'E near Mirzapur. IST = GMT + 5:30. It crosses UP, MP, Chhattisgarh, Odisha, AP.",
        "Longest border Bangladesh (4,096.7 km). Shortest Afghanistan (106 km). 7 land and 2 sea neighbours.",
        "Indira Point is the south. Kanyakumari is the mainland tip. Indira Col is the north.",
        "Ten Degree: Andaman | Nicobar. Nine Degree: Minicoy | Lakshadweep. Eight Degree: Minicoy | Maldives.",
        "Barren Island is the only active volcano. Lakshadweep islands are coral atolls.",
    ],
    patterns=[
        pat("ga-il-p1", "States on the Tropic of Cancer or the Standard Meridian", "very common",
            "'Which state does NOT lie on the Tropic of Cancer?', 'The Standard Meridian passes through', or a list of states to check.",
            ["Write the Tropic list: Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram.",
             "Write the Meridian list: UP, MP, Chhattisgarh, Odisha, Andhra Pradesh.",
             "In a NOT-question, strike each state that is on the list.", "The state left over is the answer."],
            "Both lists are short and fixed, so elimination always works.",
            "The Standard Meridian of India does NOT pass through which state? (a) Uttar Pradesh (b) Chhattisgarh (c) Odisha (d) Jharkhand",
            ["The 82°30'E line crosses UP, MP, Chhattisgarh, Odisha and Andhra Pradesh.", "Options (a), (b) and (c) are on the list.", "Jharkhand lies just east of the line."],
            "(d) Jharkhand"),
        pat("ga-il-p2", "Neighbours: border length and states touching each country", "very common",
            "'Longest or shortest border', 'Which state does NOT border Nepal or Myanmar?', 'Mizoram shares borders with'.",
            ["Recall the border order: Bangladesh, China, Pakistan, Nepal, Myanmar, Bhutan, Afghanistan.",
             "Recall the state list of the country named.", "Tick each option against the list.", "A state missing from the list is the odd one."],
            "Border questions come from two fixed lists: lengths and touching states.",
            "Which neighbouring country shares the shortest land border with India?",
            ["The border order runs from Bangladesh down to Afghanistan.", "Afghanistan is last, at about 106 km.", "It touches Ladakh on India's official map."],
            "Afghanistan (about 106 km). The longest is Bangladesh (4,096.7 km)."),
        pat("ga-il-p3", "Channels, straits and island groups", "very common",
            "A channel, strait or passage is named and the two lands it separates are asked. Or an island fact such as volcano, coral or capital.",
            ["Split by sea: Arabian Sea (Nine and Eight Degree) or Bay of Bengal (Ten Degree, Duncan, Coco, Great).",
             "Match the channel to its two sides using the table.", "Remember Palk Strait and Gulf of Mannar divide India and Sri Lanka."],
            "Each channel has exactly one pair of neighbours to learn.",
            "The Eight Degree Channel separates which two places?",
            ["Eight Degree lies in the Arabian Sea.", "It touches Minicoy.", "The other side is the Maldives."],
            "Minicoy (India) from the Maldives. The Nine Degree Channel lies further north, between Minicoy and the rest of Lakshadweep."),
        pat("ga-il-p4", "Extreme points and size superlatives", "common",
            "'Southernmost point of India', 'largest or smallest state by area', 'India's share of the world's land'.",
            ["Extremes: Indira Col (north), Indira Point (south), Kanyakumari (mainland south tip).",
             "Size: 32.87 lakh sq km, 2.4% of world land, 7th largest.", "States: Rajasthan largest, MP second, Goa smallest."],
            "These are single-fact answers, so clear memory of the list is enough.",
            "Which is the largest state of India by area?",
            ["Recall the order by area.", "Rajasthan is first and Madhya Pradesh is second."],
            "Rajasthan. Goa is the smallest."),
        pat("ga-il-p5", "Latitude-longitude extent and time difference", "occasional",
            "Questions on India's lat/long extent, why IST is GMT + 5:30, or the time gap between the east and west ends.",
            ["Use 1° of longitude = 4 minutes of time.", "Multiply the Meridian: 82.5 × 4 = 330 minutes.", "Convert: 330 minutes = 5 h 30 min ahead of GMT."],
            "The Earth turns 360° in 24 hours, so each degree takes 4 minutes.",
            "Why is Indian Standard Time 5 h 30 min ahead of GMT?",
            ["The Standard Meridian is 82°30'E.", "82.5 × 4 min = 330 min.", "330 min = 5 h 30 min."],
            "Because the Standard Meridian is at 82°30'E: 82.5 × 4 = 330 minutes.",
            formula=r"1^{\circ}\text{ of longitude} = 4\text{ minutes of time}"),
        pat("ga-il-p6", "Island facts: volcano, coral and capital", "common",
            "'India's only active volcano', 'coral islands of India', 'capital of Lakshadweep', 'southernmost island of Lakshadweep'.",
            ["Andaman side: Barren Island (active volcano), Narcondam (dormant).", "Lakshadweep: coral atolls, capital Kavaratti, southernmost island Minicoy.",
             "Note that Andaman and Nicobar are a submerged mountain chain."],
            "Island questions test three or four short facts, and each is easy to pair.",
            "Which is India's only active volcano?",
            ["Volcanoes sit in the Andaman Sea.", "Barren Island is active.", "Narcondam is dormant."],
            "Barren Island"),
        pat("ga-il-p7", "Neighbour by state: which country lies next to it", "common",
            "A list of Indian states and a country such as Bhutan, Myanmar or Nepal, and you must pick the state that does not fit.",
            ["Recall the state list for that country.", "Check whether the state appears on it.", "Watch for states that border only one country."],
            "The same short lists (5, 5, 5, 4, 4) repeat in every paper.",
            "Which state does NOT share a border with Myanmar? (a) Manipur (b) Mizoram (c) Assam (d) Nagaland",
            ["Myanmar touches Arunachal Pradesh, Nagaland, Manipur and Mizoram.", "Manipur, Mizoram and Nagaland are on the list.", "Assam is not."],
            "(c) Assam"),
    ],
)

SUBS["ig-physiography"] = dict(
    concept=(
        "India has six physiographic divisions: the Himalayas, Northern Plains, Peninsular Plateau, Indian Desert, Coastal Plains and Islands. "
        "Exams ask about ranges, the highest peak of each group, passes by state and the biggest lake of each kind."
    ),
    notes=r"""### The six divisions
India is divided into six parts:

1. The Himalayas
2. The Northern Plains
3. The Peninsular Plateau
4. The Indian Desert
5. The Coastal Plains
6. The Islands

Start every "which division" question by placing the place in one of these six boxes.

### The Himalayas
The Himalayas have three parallel ranges. From north to south they fall in height.

| Range | Also called | Key points |
|---|---|---|
| **Himadri** | Greater / Inner | Highest, about 6,000 m average; perennial snow; all 8,000-m peaks |
| **Himachal** | Lesser / Middle | Widest range; Shimla, Mussoorie, Nainital, Darjeeling; Pir Panjal, Dhauladhar, Mahabharat |
| **Shiwalik** | Outer | Youngest and lowest (900-1,100 m) |

**Duns** are valleys between Himachal and Shiwalik. Examples: Dehradun, Kotli Dun, Patli Dun.

In the north-east the ranges bend south as the **Purvanchal** hills: Patkai Bum, Naga Hills, Manipur Hills and Mizo (Lushai) Hills.

> **Note:** The Himalayas are among the youngest fold mountains. The **Aravallis** are the oldest fold mountains of India.

### Peaks to remember

| Peak | Where | Claim |
|---|---|---|
| **K2 (Godwin Austen)**, 8,611 m | Karakoram, Ladakh (India's official map) | Highest peak claimed by India; 2nd in the world |
| **Kangchenjunga**, 8,586 m | Sikkim | Highest in Sikkim; 3rd in the world |
| **Nanda Devi**, 7,816 m | Uttarakhand | Highest entirely within India |
| **Anamudi**, 2,695 m | Anaimalai Hills, Kerala | Highest of South India |
| Doddabetta, 2,637 m | Nilgiris, Tamil Nadu | Highest of the Nilgiris |
| **Guru Shikhar**, 1,722 m | Mount Abu, Rajasthan | Highest of the Aravallis |
| Parasnath, 1,365 m | Chota Nagpur, Jharkhand | Highest of Jharkhand |
| Dhupgarh, 1,350 m | Satpura (Pachmarhi), MP | Highest of the Satpura |

### Mountain passes by state
Learn passes in groups, one state at a time.

- **Ladakh / J&K:** Karakoram Pass (Ladakh to Xinjiang), Khardung La (Leh to Nubra valley), Zoji La (Srinagar-Kargil-Leh), Banihal (Jammu to Srinagar; Jawahar Tunnel under the Pir Panjal).
- **Himachal Pradesh:** Rohtang (Kullu to Lahaul and Spiti; Atal Tunnel below it), Baralacha La (Manali-Leh road), Shipki La (the **Sutlej enters India** here).
- **Uttarakhand:** Lipulekh (Kailash-Mansarovar route), Mana Pass (near Badrinath), Niti Pass.
- **Sikkim:** Nathu La (India-China trade, reopened 2006), Jelep La (via the Chumbi valley).
- **Arunachal Pradesh:** Bomdi La, Diphu Pass.
- **Western Ghats:** Thal Ghat (Mumbai-Nashik), Bhor Ghat (Mumbai-Pune), **Palghat (Palakkad) Gap** between the Nilgiri and Anaimalai hills (Kerala-TN).

### Plateau, ghats and coasts
The **Peninsular Plateau** is India's oldest landmass. It is made of hard crystalline rock.

- **Deccan Trap:** basalt lava on the north-west edge; the source of black soil.
- **Chota Nagpur Plateau:** the mineral storehouse.
- **Meghalaya Plateau** (Garo-Khasi-Jaintia hills): split from Chota Nagpur by the **Malda gap**.
- **Western Ghats (Sahyadri):** continuous and higher; a UNESCO World Heritage Site (2012).
- **Eastern Ghats:** low and broken by rivers.

> **Tip:** The Nilgiris, Anaimalai and Cardamom hills join the two Ghats.

West coast, north to south: **Konkan, Kannad (Kanara), Malabar**. Kerala's backwaters (*kayals*, e.g. Vembanad) lie here. East coast: **Utkal / Northern Circars** in the north and **Coromandel** in the south, with wide deltas.

### Lakes
| Lake | Fact |
|---|---|
| **Wular** (J&K, on the Jhelum) | Largest freshwater lake |
| **Chilika** (Odisha) | Largest brackish-water lagoon |
| **Sambhar** (Rajasthan) | Largest inland salt lake |
| **Loktak** (Manipur) | Floating *phumdis* |
| Pulicat (AP-TN) | Lagoon behind Sriharikota island |
| Kolleru (AP) | Freshwater lake between the Krishna and Godavari deltas |
| **Lonar** (Maharashtra) | Meteorite-impact crater lake |
| Pangong Tso (Ladakh) | Brackish high-altitude lake |
""",
    tricks=[
        {"title": "Pass to state by first letters",
         "body": "Zoji, Khardung, Karakoram: Ladakh. Rohtang, Shipki, Baralacha: Himachal. Lipulekh, Mana: Uttarakhand. Nathu, Jelep: Sikkim. Bomdi: Arunachal. Palghat: the Kerala-TN gap.",
         "example": {"q": "Shipki La lies in which state?",
                     "steps": ["Shipki belongs to the R-S-B group.", "That group is Himachal Pradesh."],
                     "answer": "Himachal Pradesh, where the Sutlej enters India."}},
        {"title": "Highest-peak ladder",
         "body": "Claimed by India: K2. Administered by India: Kangchenjunga. South India: Anamudi. Nilgiris: Doddabetta. Aravallis: Guru Shikhar. Satpura: Dhupgarh."},
        {"title": "Lake adjectives: Fresh Wular, Brackish Chilika, Salty Sambhar, Floating Loktak",
         "body": "Say it as one chain. Examiners swap the adjectives between the four lakes."},
    ],
    mistakes=[
        mis("Calling the Shiwaliks the oldest range.", "The Shiwaliks are the youngest. The Aravallis are the oldest fold mountains."),
        mis("Placing the Duns between Himadri and Himachal.", "Duns lie between Himachal and Shiwalik."),
        mis("Treating Nathu La as the traditional Kailash Mansarovar route.", "The traditional route is Lipulekh (Uttarakhand). Nathu La is in Sikkim."),
        mis("Swapping lake adjectives, such as Chilika as freshwater.", "Wular is fresh, Chilika is brackish, Sambhar is salt."),
        mis("Calling the Eastern Ghats continuous.", "The Western Ghats are continuous. The Eastern Ghats are broken by rivers."),
    ],
    revision=[
        "Six divisions: Himalayas, Northern Plains, Peninsular Plateau, Desert, Coastal Plains, Islands.",
        "Himadri > Himachal > Shiwalik, north to south. Duns lie between Himachal and Shiwalik.",
        "Purvanchal = Patkai, Naga, Manipur, Mizo hills. Aravallis = oldest fold mountains.",
        "K2 (Karakoram), Kangchenjunga (Sikkim), Nanda Devi (fully inside India), Anamudi (South India).",
        "Guru Shikhar = Aravallis. Dhupgarh = Satpura. Doddabetta = Nilgiris.",
        "Ladakh: Zoji, Khardung, Karakoram. Himachal: Rohtang, Shipki, Baralacha. Uttarakhand: Lipulekh, Mana. Sikkim: Nathu, Jelep.",
        "Fresh Wular, brackish Chilika, salty Sambhar, floating Loktak, meteor crater Lonar.",
    ],
    patterns=[
        pat("ga-ip-p1", "Mountain pass and its state or route", "very common",
            "A pass name (Nathu La, Zoji La, Shipki La, Rohtang, Bhor Ghat) with states or linked places as options.",
            ["Group the pass by state: Ladakh, Himachal, Uttarakhand, Sikkim, Arunachal.", "For Ghat gaps: Thal (Mumbai-Nashik), Bhor (Mumbai-Pune), Palghat (Kerala-TN).",
             "Recall the extra fact: Shipki La (Sutlej), Rohtang (Atal Tunnel), Banihal (Jawahar Tunnel)."],
            "Passes are best learned as state groups, not as a long list.",
            "Lipulekh Pass, used by pilgrims to Kailash-Mansarovar, is in which state?",
            ["Lipulekh belongs to the L-M group.", "That group is Uttarakhand.", "It lies on the India-Tibet border near the Nepal tri-junction."],
            "Uttarakhand (Pithoragarh district)"),
        pat("ga-ip-p2", "Peak superlatives and their range or state", "very common",
            "'Highest peak of South India / of the Aravallis / entirely within India', or a peak with states as options.",
            ["Recall the ladder: K2, Kangchenjunga, Nanda Devi.", "Recall range tops: Anamudi, Doddabetta, Guru Shikhar, Dhupgarh, Parasnath.",
             "Match the key word in the stem (range, state, 'entirely within') to the right row."],
            "Every peak has one range or state, so a single row answers the question.",
            "Anamudi, the highest peak of South India, is in which state?",
            ["Anamudi lies in the Anaimalai Hills.", "Those hills are in Kerala.", "Its height is 2,695 m."],
            "Kerala"),
        pat("ga-ip-p3", "Himalayan ranges, hills and their features", "common",
            "Order of the three ranges, 'Duns lie between', 'youngest or oldest mountains', or which hills belong to the Purvanchal.",
            ["Order north to south: Himadri, Himachal, Shiwalik.", "Duns lie between Himachal and Shiwalik.", "Purvanchal = Patkai Bum, Naga, Manipur and Mizo hills.",
             "Aravallis are the oldest fold mountains."],
            "The three ranges form a fixed ladder of height, age and features.",
            "Hill stations like Shimla, Mussoorie and Nainital lie in which Himalayan range?",
            ["Hill stations are in the widest range.", "That is the middle range."],
            "The Himachal (Lesser or Middle) Himalaya"),
        pat("ga-ip-p4", "Lake superlatives and lake types", "common",
            "'Largest freshwater, brackish or salt lake', 'floating national park lake', 'crater lake', or lake and state.",
            ["Read the adjective in the stem: fresh, brackish or salt.", "Match: Wular, Chilika, Sambhar.",
             "Special lakes: Loktak (phumdis), Lonar (crater), Pulicat (lagoon), Kolleru (freshwater)."],
            "The adjective is the whole clue, so read it before the options.",
            "Loktak Lake, famous for floating vegetation called phumdis, is in which state?",
            ["Loktak has floating phumdis.", "The Keibul Lamjao National Park floats on it."],
            "Manipur"),
        pat("ga-ip-p5", "Plateaus, ghats and coastal plains", "common",
            "The Deccan Trap, Chota Nagpur, Malda gap, Western versus Eastern Ghats, or which coast (Konkan, Malabar, Coromandel) lies where.",
            ["West coast north to south: Konkan, Kanara, Malabar.", "East coast: Northern Circars in the north, Coromandel in the south.",
             "Western Ghats are continuous; Eastern Ghats are low and broken."],
            "Coasts and Ghats follow a fixed north-south order.",
            "Which statement is correct? 1. The Western Ghats are continuous. 2. The Eastern Ghats are higher than the Western Ghats.",
            ["Statement 1: the Western Ghats are continuous.", "Statement 2: the Western Ghats are higher, so it is false.", "The Eastern Ghats are cut by the Mahanadi, Godavari, Krishna and Kaveri."],
            "Only 1"),
        pat("ga-ip-p6", "Hill ranges of the Purvanchal and the plateau edges", "occasional",
            "'Which hills form the Purvanchal', 'Malda gap separates', 'Meghalaya Plateau consists of'.",
            ["Purvanchal = Patkai Bum, Naga, Manipur, Mizo.", "Meghalaya Plateau = Garo, Khasi, Jaintia hills.", "The Malda gap separates it from Chota Nagpur."],
            "These are single-fact links that appear as odd-one-out items.",
            "The Malda gap separates the Meghalaya Plateau from which plateau?",
            ["The gap lies between two plateaus.", "One is Meghalaya.", "The other is the mineral storehouse."],
            "Chota Nagpur Plateau"),
        pat("ga-ip-p7", "Peak or pass by state: odd one out", "common",
            "Four items (peaks or passes) and one belongs to a different state or range.",
            ["Place each item in its state or range.", "Find the one that stands alone.", "Check the extra fact (Sutlej at Shipki La, Atal Tunnel at Rohtang)."],
            "Odd-one-out questions test the state groups you have memorised.",
            "Which of these passes is NOT in Ladakh? (a) Khardung La (b) Zoji La (c) Baralacha La (d) Karakoram Pass",
            ["Khardung La, Zoji La and Karakoram are Ladakh passes in the Z-K-K group.", "Baralacha La is on the Manali-Leh road.", "It is in Himachal Pradesh."],
            "(c) Baralacha La"),
    ],
)

SUBS["ig-rivers"] = dict(
    concept=(
        "Himalayan rivers are snow-fed and flow all year. Peninsular rivers depend mostly on rain. "
        "Exams ask for a river's source, its confluences and tributaries, and which dam or waterfall sits on which river."
    ),
    notes=r"""### Two river systems
**Himalayan rivers** are perennial, which means they flow all year. Snow and rain feed them. They are long and cut deep gorges.

**Peninsular rivers** are mostly rain-fed and seasonal.

- East-flowing peninsular rivers build **deltas**.
- West-flowing rivers (Narmada, Tapi) enter the sea through **estuaries**.

### The Indus system
The Indus rises near Lake Mansarovar in Tibet. It flows through Ladakh into Pakistan. Its tributaries in India:

| River | Source or key fact |
|---|---|
| **Jhelum** | Verinag spring; flows through Srinagar and Wular lake |
| **Chenab** | Chandra and Bhaga meet at Tandi (Himachal Pradesh) |
| **Ravi** | An Indus tributary; an eastern river under the 1960 treaty |
| **Beas** | Beas Kund near Rohtang; joins the Sutlej at **Harike** |
| **Sutlej** | Rakas Tal; enters India at **Shipki La**; Bhakra Nangal dam |

The **Indus Waters Treaty (1960)** gave India the three eastern rivers (Ravi, Beas, Sutlej). It gave Pakistan the three western ones.

### The Ganga system
The **Bhagirathi** comes from the Gangotri glacier and emerges at Gaumukh. It meets the **Alaknanda** at **Devprayag**. From there the river is the **Ganga**. It is the **longest river of India (about 2,525 km)**. It leaves the Himalayas at Haridwar.

**Panch Prayag** are five confluences on the Alaknanda, upstream to downstream:

1. Vishnuprayag (Dhauliganga)
2. Nandprayag (Nandakini)
3. Karnaprayag (Pindar)
4. Rudraprayag (Mandakini)
5. Devprayag (Bhagirathi)

> **Tip:** Say "Very Nice Kids Read Daily" to recall the order.

Main tributaries:

- **Yamuna:** from Yamunotri; the longest tributary; joins at Prayagraj. Its own tributaries are Chambal, Sind, Betwa and Ken.
- **Left bank:** Ramganga, Gomti (Lucknow is on it), Ghaghara, Gandak, Kosi and Mahananda. The **Kosi** is the "Sorrow of Bihar".
- **Right bank:** the Son, which rises at Amarkantak.
- The **Damodar** ("Sorrow of Bengal") feeds the Hugli.

The Ganga-Brahmaputra **Sundarbans delta is the world's largest delta**.

### The Brahmaputra
It rises near Mansarovar (Chemayungdung glacier). In Tibet it is the **Tsangpo**. In Arunachal Pradesh it is the **Siang / Dihang**. In Assam it carries the largest volume of any Indian river. **Majuli** in Assam is the **largest river island in the world**.

### Peninsular rivers
| River | Source | Key facts |
|---|---|---|
| **Godavari** | Trimbakeshwar, Nashik | Longest peninsular river; "Dakshin Ganga"; Manjra, Indravati, Pranhita |
| **Krishna** | Near Mahabaleshwar | Tungabhadra, Bhima, Koyna, Ghataprabha, Malaprabha |
| **Kaveri** | Talakaveri, Brahmagiri hills (Kodagu) | Hemavati, Kabini, Bhavani, Amaravati |
| **Mahanadi** | Sihawa, Chhattisgarh | Hirakud dam; Seonath, Hasdeo |
| **Narmada** | Amarkantak | Flows west in a rift valley to the Gulf of Khambhat; tributary Tawa |
| **Tapi** | Multai (Betul) | West-flowing rift-valley river; Surat is on its bank |
| **Mahi** | Vindhyas | Crosses the Tropic of Cancer twice |
| **Luni** | Aravallis near Ajmer | Ends in the Rann of Kutch (saline) |

### Dams and waterfalls
| Dam | River | Waterfall | River |
|---|---|---|---|
| **Tehri** (tallest in India) | Bhagirathi | **Jog / Gersoppa** | Sharavati (Karnataka) |
| **Bhakra Nangal** (Gobind Sagar) | Sutlej | **Chitrakote** ("Niagara of India") | Indravati (Chhattisgarh) |
| **Hirakud** (longest earthen dam) | Mahanadi | **Dudhsagar** | Mandovi (Goa) |
| **Sardar Sarovar** | Narmada | **Athirappilly** | Chalakudy (Kerala) |
| Nagarjuna Sagar, Srisailam | Krishna | Shivanasamudra, Hogenakkal | Kaveri |
| Mettur, KRS | Kaveri | **Dhuandhar** (Bhedaghat, Jabalpur) | Narmada |
| **Idukki** (arch dam) | Periyar | | |
| Farakka Barrage | Ganga | | |

Shivanasamudra on the Kaveri hosted one of Asia's earliest hydro-electric stations (1902). The **Indira Gandhi Canal** carries Sutlej-Beas water deep into Rajasthan.
""",
    tricks=[
        {"title": "Panch Prayag: Very Nice Kids Read Daily",
         "body": "Vishnuprayag, Nandprayag, Karnaprayag, Rudraprayag, Devprayag, from upstream to downstream. At Devprayag the river becomes the Ganga.",
         "example": {"q": "At which confluence does the Mandakini meet the Alaknanda?",
                     "steps": ["Recall the order: V, N, K, R, D.", "The Mandakini is the fourth river."],
                     "answer": "Rudraprayag"}},
        {"title": "West-flowers: Nobody Takes Mahi Seriously",
         "body": "Narmada, Tapi, Mahi and Sabarmati flow into the Arabian Sea and form estuaries. Narmada and Tapi flow through rift valleys."},
        {"title": "Waterfall and river pairs",
         "body": "Jog with Sharavati. Chitrakote with Indravati. Dudhsagar with Mandovi. Athirappilly with Chalakudy. Shivanasamudra and Hogenakkal with Kaveri. Dhuandhar with Narmada."},
    ],
    mistakes=[
        mis("Calling the Godavari India's longest river.", "It is the longest peninsular river. The Ganga is the longest overall."),
        mis("Saying the Narmada rises in the Western Ghats.", "It rises at Amarkantak (MP) and flows west."),
        mis("Putting the Tehri dam on the Alaknanda.", "Tehri is on the Bhagirathi."),
        mis("Saying the Narmada and Tapi form deltas.", "West-flowing rivers form estuaries. Deltas belong to east-flowing rivers."),
        mis("Mixing up the Kosi and the Damodar nicknames.", "Kosi is the Sorrow of Bihar. Damodar is the Sorrow of Bengal."),
    ],
    revision=[
        "Indus tributaries: Jhelum, Chenab, Ravi, Beas, Sutlej. The Sutlej enters at Shipki La. Beas meets Sutlej at Harike.",
        "Ganga forms at Devprayag. It is the longest river of India. Yamuna is its longest tributary.",
        "Kosi = Sorrow of Bihar. Damodar = Sorrow of Bengal. Sundarbans = largest delta. Majuli = largest river island.",
        "Narmada and Tapi flow west through rift valleys and form estuaries. Mahi crosses the Tropic of Cancer twice.",
        "Godavari = Dakshin Ganga, the longest peninsular river.",
        "Tehri = tallest dam. Hirakud = longest earthen dam.",
        "Jog-Sharavati, Chitrakote-Indravati, Dhuandhar-Narmada.",
    ],
    patterns=[
        pat("ga-ir-p1", "River and its source", "very common",
            "'Which river rises at Amarkantak, Trimbakeshwar or Talakaveri?', or a river with places as options.",
            ["Peninsula: Godavari (Trimbakeshwar), Krishna (near Mahabaleshwar), Kaveri (Talakaveri), Mahanadi (Sihawa), Tapi (Multai).",
             "Amarkantak feeds two rivers: the Narmada (west) and the Son.",
             "Himalaya: Ganga (Gangotri), Yamuna (Yamunotri), Indus and Brahmaputra (near Mansarovar), Sutlej (Rakas Tal), Beas (Beas Kund)."],
            "Sources are single facts, and Amarkantak is the favourite.",
            "The Mahanadi rises in which state?",
            ["The Mahanadi rises at Sihawa.", "Sihawa is in Dhamtari district of Chhattisgarh."],
            "Chhattisgarh. It flows east through Odisha into the Bay of Bengal."),
        pat("ga-ir-p2", "Confluences and tributaries", "very common",
            "'X and Y meet at', 'Which is a tributary of', 'Which is a right-bank tributary', Panch Prayag questions.",
            ["Recall the Panch Prayag order on the Alaknanda.", "Other meeting points: Beas and Sutlej at Harike; Ganga and Yamuna at Prayagraj; Chandra and Bhaga at Tandi.",
             "Ganga right bank: Yamuna and Son. Left bank: Ramganga, Gomti, Ghaghara, Gandak, Kosi, Mahananda."],
            "Confluences follow fixed lists, so order and bank are the only tests.",
            "Karnaprayag is the confluence of the Alaknanda with which river?",
            ["The order is Vishnu, Nand, Karna, Rudra, Dev.", "Karnaprayag is third.", "Its partner river is the Pindar."],
            "The Pindar"),
        pat("ga-ir-p3", "Dam or project and its river", "very common",
            "'Hirakud, Tehri or Sardar Sarovar is built on', or a match-the-column of dams and rivers.",
            ["North: Tehri (Bhagirathi), Bhakra Nangal (Sutlej), Farakka Barrage (Ganga).",
             "Peninsula: Hirakud (Mahanadi), Sardar Sarovar (Narmada), Nagarjuna Sagar and Srisailam (Krishna), Mettur and KRS (Kaveri), Idukki (Periyar).",
             "Superlatives: Tehri tallest; Hirakud longest earthen dam."],
            "A dam has one river, so the pair is a single fact.",
            "The Krishnarajasagar (KRS) dam near Mysuru is on which river?",
            ["KRS is in the Kaveri group.", "Mettur dam in Tamil Nadu is on the same river."],
            "The Kaveri"),
        pat("ga-ir-p4", "Waterfall and its river", "common",
            "A named waterfall (Jog, Chitrakote, Dhuandhar, Dudhsagar, Athirappilly, Shivanasamudra) with rivers as options.",
            ["Karnataka: Jog (Sharavati), Shivanasamudra (Kaveri).", "Central India: Chitrakote (Indravati), Dhuandhar (Narmada, Bhedaghat, Jabalpur).",
             "Coast: Dudhsagar (Mandovi, Goa), Athirappilly (Chalakudy, Kerala), Hogenakkal (Kaveri, Tamil Nadu)."],
            "There are only about seven pairs to learn.",
            "Hogenakkal Falls in Tamil Nadu are on which river?",
            ["Hogenakkal is in the Kaveri group.", "It lies near the Karnataka-Tamil Nadu border."],
            "The Kaveri"),
        pat("ga-ir-p5", "River nicknames and unique facts", "common",
            "'Sorrow of Bihar or Bengal', 'Dakshin Ganga', 'largest river island', 'forms an estuary', 'crosses the Tropic twice'.",
            ["Nicknames: Kosi (Bihar), Damodar (Bengal), Godavari (Dakshin Ganga).",
             "Firsts: Ganga is longest; Yamuna is the longest tributary; Majuli is the largest river island; Sundarbans is the largest delta.",
             "Narmada and Tapi form estuaries; the Mahi crosses the Tropic twice."],
            "Each nickname points to exactly one river.",
            "Which river is called the Sorrow of Bengal?",
            ["Rivers with floods have sorrow nicknames.", "The Damodar floods West Bengal.", "The Damodar Valley Corporation (1948) was set up to control it."],
            "The Damodar"),
        pat("ga-ir-p6", "Indus tributaries and the Indus Waters Treaty", "common",
            "'Which is NOT a tributary of the Indus', 'Chenab is formed by', 'eastern rivers under the 1960 treaty'.",
            ["Name the five: Jhelum, Chenab, Ravi, Beas, Sutlej.", "Chenab = Chandra + Bhaga at Tandi.",
             "The 1960 treaty: India got Ravi, Beas, Sutlej; Pakistan got the three western rivers."],
            "The five names and their sources come as one small block.",
            "The Chenab is formed by the meeting of which two streams?",
            ["The meeting point is Tandi in Himachal Pradesh.", "The two streams are the Chandra and the Bhaga."],
            "The Chandra and the Bhaga"),
        pat("ga-ir-p7", "West-flowing and east-flowing rivers", "occasional",
            "'Which river forms an estuary', 'which river flows through a rift valley', 'which river ends in the Rann of Kutch'.",
            ["West-flowing: Narmada, Tapi, Mahi, Sabarmati.", "Narmada and Tapi flow in rift valleys.", "The Luni ends in the Rann of Kutch."],
            "The direction of flow decides delta or estuary.",
            "Which of these rivers forms an estuary? (a) Godavari (b) Mahanadi (c) Narmada (d) Krishna",
            ["Godavari, Mahanadi and Krishna flow east.", "East-flowing rivers form deltas.", "The Narmada flows west."],
            "(c) Narmada"),
    ],
)

SUBS["ig-climate-soils"] = dict(
    concept=(
        "India has a tropical monsoon climate. The south-west monsoon reaches Kerala around 1 June. "
        "Winds, pre-monsoon showers and soil types each have a place, a crop and a cause that exams ask about."
    ),
    notes=r"""### Why India has a monsoon
The whole year turns on a seasonal reversal of winds. In summer the land heats up and draws in moist ocean winds. This is the **south-west (SW) monsoon**.

- It normally strikes the **Kerala coast around 1 June**. This is called the "burst" of the monsoon.
- It normally covers the whole country by about **mid-July**.
- By **mid-September** it starts to withdraw from the north-west.

It has two branches:

- **Arabian Sea branch:** gives very heavy rain on the windward side of the Western Ghats.
- **Bay of Bengal branch:** goes up the Ganga plain into the north-east.

### Where rain falls and where it does not
The windward side of the Western Ghats (Mumbai, Konkan, Kerala) gets drenched. The leeward side (Pune, interior Karnataka, Marathwada) lies in the **rain shadow**.

- **Mawsynram** and **Cherrapunji (Sohra)** in Meghalaya's Khasi hills record some of the highest rainfall on Earth.
- West Rajasthan (Jaisalmer) is the driest.
- A long dry spell inside the season is a **break** in the monsoon.
- **El Nino** is a warming of the eastern Pacific. It is linked with weaker Indian monsoons.

### Retreating monsoon and local winds
In October the monsoon winds leave. Hot, humid days of this month are called **October heat**. The retreating winds pick up moisture from the Bay of Bengal. They give **October-December rain to the Tamil Nadu (Coromandel) coast**. This is the north-east (NE) monsoon, Tamil Nadu's main rain.

| Name | Region | Nature or use |
|---|---|---|
| **Loo** | North Indian plains | Hot, dry summer wind |
| **Mango showers** | Kerala, Karnataka coast | Help mangoes ripen |
| **Blossom showers** | Karnataka | Help coffee flower |
| **Kalbaisakhi / Nor'westers** | West Bengal, Assam | Evening thunderstorms; help tea and jute; **Bordoichila** in Assam |
| **Western disturbances** | Punjab, Haryana, west UP, J&K | Winter rain from the Mediterranean area; vital for rabi wheat |

> **Tip:** Match the shower to the crop. Mango showers help mango. Blossom showers help coffee. Kalbaisakhi helps tea.

### Soils of India
ICAR recognises 8 soil groups.

| Soil | Where | Key facts |
|---|---|---|
| **Alluvial** | Northern plains, deltas | Most widespread (about 40% of area); *khadar* new and fertile; *bhangar* old with kankar; rice, wheat, sugarcane |
| **Black (Regur)** | Deccan trap: Maharashtra, Gujarat, MP | From basalt; holds moisture; "self-ploughing" cracks; **cotton** |
| **Red and yellow** | TN, Karnataka, Odisha, Chhattisgarh | Red from **iron oxide**; sandy; poor in humus |
| **Laterite** | Western Ghats, Kerala, Odisha hills, NE | Formed by **leaching** in heat and heavy rain; hardens like brick (Latin *later*); tea, coffee, cashew after manuring |
| **Arid** | West Rajasthan | Sandy, saline, calcium (kankar) layers |
| **Saline / alkaline** | Dry areas; over-irrigated Punjab-Haryana | *Reh, kallar, usar*; reclaimed with **gypsum** |
| **Peaty / marshy** | Kerala (*kari*), Sundarbans | High humus, black, heavy |
| **Forest / mountain** | Himalayan slopes | Rich humus, acidic |

Black soil is **rich** in lime, iron, magnesium and potash. It is **poor** in nitrogen, phosphorus and humus.

> **Watch:** Laterite is not naturally fertile. Leaching washes its nutrients away.

### Soil erosion and its cure
- **Gully erosion:** running water cuts the land into bare **ravines**. The Chambal badlands are the example.
- **Sheet erosion:** the topsoil layer is removed evenly.
- **Wind erosion:** open land in dry areas loses soil.

Remedies: **contour ploughing, terrace farming, strip cropping, shelter belts of trees, afforestation**.
""",
    tricks=[
        {"title": "Black soil: LIMP is rich, NPH is poor",
         "body": "Rich in Lime, Iron, Magnesium, Potash. Poor in Nitrogen, Phosphorus, Humus.",
         "example": {"q": "Black soil is generally deficient in which nutrient?",
                     "steps": ["Recall the poor list: N, P, H.", "Nitrogen is first on it."],
                     "answer": "Nitrogen (also phosphorus and organic matter)"}},
        {"title": "Shower names follow the crop",
         "body": "Mango showers: mango, Kerala. Blossom showers: coffee, Karnataka. Kalbaisakhi: tea, jute, rice in Bengal and Assam. Western disturbances: rabi wheat in the north-west."},
    ],
    mistakes=[
        mis("Saying Tamil Nadu gets most rain from the south-west monsoon.", "Its main rain is in October to December from the retreating (north-east) monsoon."),
        mis("Blaming aluminium for the red colour of red soil.", "The colour comes from iron oxide."),
        mis("Treating laterite as naturally fertile.", "It is leached and needs manure."),
        mis("Treating the Chambal ravines as sheet erosion.", "They are gully erosion by running water."),
        mis("Reclaiming saline soil with lime or manure.", "Saline and alkaline soil is treated with gypsum."),
    ],
    revision=[
        "SW monsoon hits Kerala about 1 June. Two branches: Arabian Sea and Bay of Bengal. It withdraws from the NW by mid-September.",
        "Rain shadow lies on the leeward Ghats. Mawsynram is the wettest. Tamil Nadu's main rain is Oct-Dec.",
        "Loo = summer, north India. Mango showers = Kerala. Blossom = coffee. Kalbaisakhi = Bengal and Assam.",
        "Black soil: basalt, cotton, rich in LIMP, poor in N, P and humus.",
        "Laterite forms by leaching and hardens like brick. Saline soil is treated with gypsum.",
        "Alluvial is the most widespread soil. Gully erosion makes the Chambal ravines.",
    ],
    patterns=[
        pat("ga-ics-p1", "SW monsoon: onset, branches and withdrawal", "very common",
            "When and where the monsoon strikes Kerala, its two branches, when it covers the country, or when it starts withdrawing.",
            ["Onset: about 1 June on the Kerala coast.", "Coverage: most of India by mid-July.",
             "Branches: Arabian Sea (Western Ghats) and Bay of Bengal (north-east, Ganga plain).", "Withdrawal starts from the north-west around mid-September."],
            "The monsoon follows a fixed calendar of four dates.",
            "The south-west monsoon normally sets in over the Kerala coast around which date?",
            ["The burst happens on the Kerala coast.", "The usual date is 1 June.", "It then covers the country by mid-July."],
            "1 June"),
        pat("ga-ics-p2", "Rainfall distribution, rain shadow and extremes", "very common",
            "'Which region gets the highest or lowest rainfall?', 'Why is Pune dry?', 'rain shadow of the Western Ghats', 'Mawsynram is in which state?'",
            ["Windward Ghats (Konkan, Kerala, Mumbai): very heavy rain.", "Leeward side (Pune, interior Karnataka, Marathwada): rain shadow.",
             "Wettest: Mawsynram and Cherrapunji (Sohra), Meghalaya. Driest: west Rajasthan.",
             "Tamil Nadu's coast is dry in June-September; its main rain comes later."],
            "Slope direction decides who gets rain.",
            "Mawsynram, one of the rainiest places on Earth, lies in which state?",
            ["It is in the Khasi hills.", "The Khasi hills are in Meghalaya."],
            "Meghalaya. Cherrapunji (Sohra) is the other wet station nearby."),
        pat("ga-ics-p3", "Retreating monsoon, October heat and local winds", "very common",
            "'Kalbaisakhi is associated with', 'mango showers help which crop', 'October heat', 'which wind brings winter rain to Punjab'.",
            ["October: winds retreat; hot and humid days are October heat.", "Oct-Dec rain on the Tamil Nadu coast is the NE monsoon.",
             "Showers by crop: mango, blossom (coffee), Kalbaisakhi (tea, jute; Bordoichila in Assam).", "Winter rain in the north-west: western disturbances."],
            "Each wind or shower has one region and one crop.",
            "Kalbaisakhi thunderstorms, which help tea and jute, occur mainly in which region?",
            ["Kalbaisakhi is a Nor'wester.", "It is in West Bengal and Assam.", "It comes in spring (March to May)."],
            "West Bengal and Assam. In Assam the same season brings the Bordoichila winds."),
        pat("ga-ics-p4", "Soil type, properties, formation and crops", "very common",
            "'Regur soil is best for', 'which soil is formed by leaching', 'black soil is deficient in', 'khadar and bhangar are types of'.",
            ["Match soil to origin: alluvial (river deposits), black (basalt), red (iron oxide), laterite (leaching).",
             "Black soil is rich in lime, iron, magnesium, potash and poor in N, P, humus.", "Saline and alkaline soil (reh, usar) is reclaimed with gypsum."],
            "Every soil has one cause and one crop, so match those two.",
            "Black (regur) soil is well known for being deficient in which nutrients?",
            ["Recall the poor list: N, P, H.", "It holds moisture well and suits cotton."],
            "Nitrogen, phosphorus and humus"),
        pat("ga-ics-p5", "Soil erosion and conservation", "occasional",
            "'Ravines of the Chambal are an example of', 'contour ploughing is used for', 'sheet erosion means'.",
            ["Gully erosion (running water) makes ravines.", "Sheet erosion removes topsoil evenly.", "Wind erosion strips dry open land.",
             "Remedies: contour ploughing, terrace farming, strip cropping, shelter belts, afforestation."],
            "The type of erosion is named by how the soil is lost.",
            "The gullied badlands along the Chambal river are a classic example of what?",
            ["Running water cuts deep channels.", "This makes ravines."],
            "Gully erosion"),
        pat("ga-ics-p6", "Soil and region matching", "common",
            "'Laterite soil is found in', 'peaty soil is found in', 'arid soil is found in', or a match-the-column of soils and regions.",
            ["Alluvial: northern plains and deltas.", "Black: Maharashtra, Gujarat, MP.", "Red and yellow: TN, Karnataka, Odisha, Chhattisgarh.",
             "Laterite: Western Ghats, Kerala, Odisha hills, NE.", "Arid: west Rajasthan. Peaty: Kerala (kari), Sundarbans."],
            "Each soil has a home region, and a few regions repeat.",
            "Which soil is found in the Deccan trap region of Maharashtra, Gujarat and MP?",
            ["The Deccan trap is made of basalt.", "Soil from basalt is black soil."],
            "Black (regur) soil"),
    ],
)

SUBS["ig-agri-minerals"] = dict(
    concept=(
        "Crops are sorted into kharif, rabi and zaid by their season. "
        "Each major crop, mineral and port has one place or speciality that exams ask about. The coloured revolutions pair a colour with a product."
    ),
    notes=r"""### Cropping seasons
Season is the first filter for every crop question.

| Season | Sowing to harvest | Main crops |
|---|---|---|
| **Kharif** | June-July (with the monsoon) to Sep-Oct | Rice, jowar, bajra, maize, cotton, jute, groundnut, soybean, tur |
| **Rabi** | Oct-Nov (winter) to Mar-Apr | Wheat, barley, gram, mustard, peas |
| **Zaid** | Short summer season (Mar-Jun) | Watermelon, muskmelon, cucumber, fodder |

> **Rule:** Monsoon-sown means kharif. Winter-sown means rabi. A summer catch-crop means zaid. In most of India maize is kharif.

### Crops and their leading states
These pairs are stable and often asked.

- **Tea:** Assam (the world's second largest producer).
- **Coffee:** Karnataka (about 70% of Indian coffee). It arrived at the **Baba Budan hills**.
- **Rubber:** Kerala. Kerala is also the "spice garden of India" (pepper, cardamom).
- **Jute:** West Bengal, the "golden fibre".
- **Sugarcane** and **wheat:** Uttar Pradesh.
- **Groundnut:** Gujarat.

> **Note:** The leading state for rice and cotton changes from year to year. Treat those as current-affairs facts.

### The coloured revolutions

| Revolution | Product | Person or programme |
|---|---|---|
| **Green** | Food grains (wheat, rice) | M.S. Swaminathan (India); Norman Borlaug (world); HYV seeds, mid-1960s |
| **White** | Milk | Verghese Kurien; Operation Flood, 1970; Amul, Anand |
| **Blue** | Fish | |
| **Yellow** | Oilseeds | |
| **Silver** | Eggs and poultry | |
| **Round** | Potato | |
| **Golden** | Horticulture and honey | |

India is the world's largest producer of **milk, pulses and jute**.

### Minerals and energy

| Resource | Place to remember |
|---|---|
| **Coal** | **Jharia** (Jharkhand), largest coking-coal field; **Raniganj** (West Bengal), oldest, 1774; Bokaro, Korba (Chhattisgarh), Talcher (Odisha), Singrauli |
| **Lignite** | **Neyveli** (Tamil Nadu) |
| **Petroleum** | **Digboi** (Assam), oldest refinery, 1901; **Mumbai High**, offshore field; Ankleshwar and Koyali (Gujarat) |
| **Iron ore** | **Bailadila** (Chhattisgarh); Bellary-Sandur (Karnataka); Singhbhum (Jharkhand); Mayurbhanj (Odisha) |
| **Bauxite** | Odisha (Panchpatmali, Koraput), largest reserves |
| **Mica** | **Koderma** (Jharkhand); Nellore (AP) |
| **Copper** | **Khetri** (Rajasthan); Singhbhum (Jharkhand); Malanjkhand (MP) |
| **Gold** | **Hutti** (Karnataka), a working mine; **Kolar** Gold Fields closed in 2001 |
| **Zinc-lead** | **Zawar** (Rajasthan) |
| **Thorium** | Monazite sands of Kerala (and Tamil Nadu) |

The Kudremukh iron-ore mine in Karnataka closed in 2005.

### Ports
**West coast**

- **Deendayal (Kandla)**, Gujarat: a tidal port.
- **Mumbai:** the largest natural harbour.
- **JNPT (Nhava Sheva):** the largest container port among the major (central government) ports.
- **Mormugao** (Goa): iron-ore exports.
- New Mangalore and **Kochi**.

**East coast**

- **Chennai:** an artificial harbour.
- **Kamarajar (Ennore):** the first corporatised major port.
- **Visakhapatnam:** the deepest landlocked and protected port.
- **Syama Prasad Mookerjee (Kolkata):** a riverine port with the Haldia dock.
- V.O. Chidambaranar (Tuticorin) and **Paradip** (Odisha).

> **Tip:** Pair the adjective with the port: tidal-Kandla, artificial-Chennai, riverine-Kolkata, deepest-Vizag.
""",
    tricks=[
        {"title": "Revolution colours follow the product",
         "body": "White is milk. Blue is water and fish. Yellow is oilseeds (mustard flower). Silver is eggs. Round is potato. Green is grains.",
         "example": {"q": "The Yellow Revolution relates to which product?",
                     "steps": ["Yellow matches the mustard flower.", "Mustard is an oilseed."],
                     "answer": "Oilseeds"}},
        {"title": "Kharif crops need water",
         "body": "Water-loving rice, jute and cotton are kharif. Cool-weather wheat, gram and mustard are rabi. Summer melons are zaid."},
    ],
    mistakes=[
        mis("Placing Digboi in Gujarat.", "Digboi is in Assam. Its refinery dates from 1901."),
        mis("Calling Kolar the working gold mine.", "Kolar closed in 2001. Hutti is working."),
        mis("Classing maize as only a rabi crop.", "In most of India maize is kharif."),
        mis("Treating rice and cotton leaders as fixed facts.", "Those leaders change from year to year."),
        mis("Calling Mumbai the largest container port among major ports.", "That is JNPT (Nhava Sheva). Mumbai is the largest natural harbour."),
    ],
    revision=[
        "Kharif: monsoon-sown, such as rice, cotton and jute. Rabi: winter-sown, such as wheat, mustard and gram. Zaid: summer melons.",
        "Tea: Assam. Coffee: Karnataka. Rubber: Kerala. Jute: West Bengal. Sugarcane: UP.",
        "Green: Swaminathan. White: Kurien (Operation Flood, 1970). Blue: fish. Yellow: oilseeds. Silver: eggs. Round: potato.",
        "Jharia: coking coal. Neyveli: lignite. Digboi: first refinery. Bailadila: iron. Koderma: mica. Khetri: copper. Zawar: zinc. Hutti: gold.",
        "Kandla: tidal. Vizag: deepest landlocked. JNPT: containers. Kolkata: riverine. Ennore: first corporatised.",
    ],
    patterns=[
        pat("ga-iam-p1", "Crop and season (kharif, rabi, zaid)", "very common",
            "'Which of the following is a rabi or kharif crop?', 'zaid crops are grown when', matching crops to a season.",
            ["Kharif: sown June-July, harvested Sep-Oct (rice, jowar, bajra, maize, cotton, jute, groundnut, soybean, tur).",
             "Rabi: sown Oct-Nov, harvested Mar-Apr (wheat, barley, gram, mustard, peas).", "Zaid: short summer season (watermelon, muskmelon, cucumber, fodder).",
             "For 'NOT a kharif crop', look for wheat or mustard."],
            "The sowing time alone decides the season.",
            "Which of the following is a rabi crop? (a) Cotton (b) Mustard (c) Maize (d) Groundnut",
            ["Cotton, maize and groundnut are sown with the monsoon.", "Mustard is sown in October-November.", "It is harvested in March-April."],
            "(b) Mustard"),
        pat("ga-iam-p2", "Crop and leading state or growing conditions", "very common",
            "'Golden fibre is', 'which state is the largest producer of coffee', 'Baba Budan hills are associated with'.",
            ["Recall the stable pairs: tea-Assam, coffee-Karnataka, rubber-Kerala, jute-West Bengal, sugarcane-UP, wheat-UP, groundnut-Gujarat.",
             "Recall the hook: tea (well-drained slopes), jute (alluvial deltaic soil, standing water), coffee (Baba Budan hills, shade).",
             "Treat rice and cotton leadership as current affairs."],
            "The pairs never change, so one memory line covers them.",
            "The golden fibre of India, grown mainly in West Bengal, is which crop?",
            ["Golden fibre means jute.", "Jute needs deltaic alluvial soil and plenty of water for retting.", "India is the largest producer of jute."],
            "Jute"),
        pat("ga-iam-p3", "Revolution colour, product and pioneer", "very common",
            "'Operation Flood is associated with', 'which revolution relates to fish', 'White Revolution pioneer'.",
            ["Green: food grains, M.S. Swaminathan, mid-1960s HYV seeds.", "White: milk, Verghese Kurien, Operation Flood 1970, Anand and Amul.",
             "Others: Blue (fish), Yellow (oilseeds), Silver (eggs, poultry), Round (potato), Golden (horticulture, honey).",
             "India is the largest producer of milk, pulses and jute."],
            "Each colour maps to one product.",
            "Operation Flood (1970), which made India the world's largest milk producer, is linked to which revolution?",
            ["Operation Flood is about milk.", "Milk is the White Revolution.", "It was led by Dr Verghese Kurien from Anand (Gujarat)."],
            "The White Revolution. Anand is the home of Amul."),
        pat("ga-iam-p4", "Mineral or energy resource and its location", "very common",
            "'Jharia is famous for', 'largest lignite deposit', 'oldest oil refinery', match-the-column on minerals.",
            ["Coal: Jharia (largest coking coal, Jharkhand), Raniganj (oldest, 1774), Korba, Talcher.", "Oil: Digboi (oldest refinery, 1901), Mumbai High (offshore), Ankleshwar and Koyali. Lignite: Neyveli.",
             "Metals: iron Bailadila, Bellary-Sandur; bauxite Odisha; mica Koderma; copper Khetri; zinc-lead Zawar; gold Hutti."],
            "Every mineral has one headline place.",
            "India's largest reserves of bauxite lie in which state?",
            ["Bauxite feeds the aluminium industry.", "The Panchpatmali deposits are in Koraput district."],
            "Odisha"),
        pat("ga-iam-p5", "Major port and its speciality", "common",
            "'Which port is called tidal', 'deepest landlocked port', 'which port handles containers or iron ore', artificial versus natural harbours.",
            ["West: Kandla (tidal), Mumbai (largest natural harbour), JNPT (containers), Mormugao (iron ore).", "East: Chennai (artificial), Ennore (first corporatised), Vizag (deepest landlocked), Kolkata (riverine).",
             "Pair the adjective with the port."],
            "Each port has one adjective to attach.",
            "Which major port of India is known as a tidal port?",
            ["Tides govern how ships enter its basins.", "It lies on the Gulf of Kutch in Gujarat."],
            "Deendayal Port, Kandla"),
        pat("ga-iam-p6", "Old versus new: firsts and closures", "occasional",
            "'Oldest coal mine', 'oldest refinery', 'which gold mine is still working', 'first corporatised port'.",
            ["Coal: Raniganj, 1774.", "Refinery: Digboi, 1901.", "Gold: Kolar closed in 2001, Hutti works.", "Port: Ennore was the first corporatised."],
            "Firsts and closures are single-date facts.",
            "Which is the oldest refinery in India?",
            ["Refineries are linked to Assam.", "The oldest is at Digboi, from 1901."],
            "Digboi (Assam)"),
    ],
)

SUBS["ig-parks"] = dict(
    concept=(
        "India protects wildlife through national parks, sanctuaries, tiger reserves, biosphere reserves and Ramsar wetlands. "
        "Exam questions link a park to its state and to its famous animal, and ask a few key dates."
    ),
    notes=r"""### Why India protects its wildlife
India is one of the world's **megadiverse** countries. The main tools of protection are:

- **National parks** (the strictest).
- Wildlife sanctuaries.
- Tiger reserves.
- Biosphere reserves.
- Ramsar wetlands.

Four dates to memorise:

| Year | Event |
|---|---|
| **1936** | First national park: Hailey NP, now **Jim Corbett NP** (Uttarakhand) |
| **1973** | **Project Tiger** launched from Corbett |
| **1986** | First biosphere reserve: **Nilgiri** |
| **1992** | **Project Elephant** |

### Park, state and animal
Learn any two corners and you can answer the third.

| National park | State / UT | Famous for |
|---|---|---|
| Jim Corbett | Uttarakhand | First NP; tigers; Ramganga river |
| **Kaziranga** | Assam | One-horned rhino; UNESCO site (1985); Brahmaputra bank |
| Manas | Assam | Golden langur, pygmy hog; UNESCO site |
| **Gir** | Gujarat | Last home of the Asiatic lion |
| Sundarbans | West Bengal | Royal Bengal tiger, mangroves; UNESCO site |
| Keoladeo (Bharatpur) | Rajasthan | Birds; UNESCO site |
| Ranthambore, Sariska, Desert NP | Rajasthan | Tigers; Great Indian Bustard in Desert NP |
| Kanha, Bandhavgarh, Pench, Panna, Satpura | Madhya Pradesh | Barasingha in Kanha; tigers in Bandhavgarh |
| **Kuno** | Madhya Pradesh | Cheetahs reintroduced from Namibia (Sept 2022) |
| Dudhwa | Uttar Pradesh | Swamp deer; rhino rehabilitation |
| **Hemis** | Ladakh | Snow leopard; largest national park of India |
| Dachigam | J&K | **Hangul** (Kashmir stag) |
| Great Himalayan; Nanda Devi and Valley of Flowers | HP; Uttarakhand | UNESCO natural sites; alpine flowers |
| **Keibul Lamjao** | Manipur | Only floating NP (on Loktak lake); **Sangai** deer |
| Namdapha | Arunachal Pradesh | Four big cats: tiger, leopard, snow leopard, clouded leopard |
| Silent Valley; Eravikulam; Periyar | Kerala | **Lion-tailed macaque**; **Nilgiri tahr**; elephants |
| Bandipur, Nagarhole | Karnataka | Tigers, elephants (Nilgiri Biosphere) |
| Bhitarkanika; Simlipal | Odisha | **Saltwater crocodiles**; tigers and elephants |
| Khangchendzonga | Sikkim | UNESCO mixed site |

### Other places in the same questions
- **Gahirmatha** (Odisha): a marine sanctuary. Lakhs of **Olive Ridley turtles** nest together here (*arribada*).
- **Chilika** (Odisha): Irrawaddy dolphins and winter birds.
- **Keibul Lamjao:** floating meadows (*phumdis*) carry the Sangai deer of Loktak lake.

### State-level superlatives
**Madhya Pradesh** has the largest number of national parks. It is called the **"Tiger State"** because it led the last tiger counts.

Assam's Kaziranga and Manas, and the Siberian-crane story of Keoladeo, are the evergreen one-liners of this section.

> **Tip:** Start from the animal. Rhino means Kaziranga. Lion means Gir. Cheetah means Kuno. Snow leopard means Hemis.
""",
    tricks=[
        {"title": "Animal-first recall",
         "body": "Rhino: Kaziranga. Lion: Gir. Cheetah: Kuno. Snow leopard: Hemis. Hangul: Dachigam. Sangai: Keibul Lamjao. Nilgiri tahr: Eravikulam. Lion-tailed macaque: Silent Valley. Saltwater crocodile: Bhitarkanika. Olive Ridley: Gahirmatha.",
         "example": {"q": "Where is the Sangai deer found?",
                     "steps": ["Sangai is linked to Loktak lake.", "The park floats on the lake."],
                     "answer": "Keibul Lamjao National Park, Manipur"}},
        {"title": "Year chain 36-73-86-92",
         "body": "1936 first NP (Hailey/Corbett). 1973 Project Tiger. 1986 first biosphere reserve (Nilgiri). 1992 Project Elephant."},
    ],
    mistakes=[
        mis("Putting Kanha in Maharashtra.", "Kanha is in Madhya Pradesh."),
        mis("Placing Keoladeo in Gujarat.", "It is at Bharatpur, Rajasthan."),
        mis("Saying cheetahs were brought to Gir.", "They were brought to Kuno (MP)."),
        mis("Mixing the first national park with the first biosphere reserve.", "The first NP is Corbett (1936). The first biosphere reserve is Nilgiri (1986)."),
        mis("Calling Khangchendzonga a purely natural site.", "It is a UNESCO mixed site."),
    ],
    revision=[
        "Year chain: 1936 Corbett, 1973 Project Tiger, 1986 Nilgiri Biosphere, 1992 Project Elephant.",
        "Rhino: Kaziranga. Lion: Gir. Cheetah: Kuno. Snow leopard: Hemis. Hangul: Dachigam.",
        "Sangai: Keibul Lamjao. Tahr: Eravikulam. Macaque: Silent Valley. Crocodile: Bhitarkanika. Olive Ridley: Gahirmatha.",
        "Kaziranga, Manas and Keoladeo: UNESCO 1985. Sundarbans: 1987. Khangchendzonga: mixed site.",
        "MP has the most national parks and is the Tiger State. Hemis is the largest NP.",
        "Kuno's cheetahs came from Namibia in September 2022.",
    ],
    patterns=[
        pat("ga-pk-p1", "Protection years: first NP, Project Tiger, biosphere, Project Elephant", "common",
            "'Which was the first national park', 'Project Tiger was launched in', 'first biosphere reserve'.",
            ["Write the chain: 1936, 1973, 1986, 1992.", "Match: Hailey NP (Corbett), Project Tiger, Nilgiri, Project Elephant.",
             "Do not mix a biosphere reserve with a national park."],
            "Four dates cover every 'first' question.",
            "Project Tiger, launched in 1973, began with which reserve?",
            ["Project Tiger began from Corbett.", "Corbett was set up in 1936 as Hailey National Park."],
            "Jim Corbett National Park (Uttarakhand)"),
        pat("ga-pk-p2", "National park and its state or UT", "very common",
            "A park name with four states as options, or 'how many parks does X state have'.",
            ["Assam: Kaziranga, Manas, Dibru-Saikhowa, Nameri.", "MP: Kanha, Bandhavgarh, Pench, Panna, Satpura, Kuno.",
             "Rajasthan: Ranthambore, Sariska, Keoladeo, Desert NP. Kerala: Silent Valley, Eravikulam, Periyar.",
             "Single-park states: Hemis (Ladakh), Dachigam (J&K), Keibul Lamjao (Manipur), Namdapha (Arunachal), Bhitarkanika (Odisha), Khangchendzonga (Sikkim)."],
            "Learning parks by state gives quick answers.",
            "Kaziranga National Park, a UNESCO World Heritage Site, is in which state?",
            ["Kaziranga is in the Assam group.", "It stands on the southern bank of the Brahmaputra."],
            "Assam. Manas is the state's other famous UNESCO-listed park."),
        pat("ga-pk-p3", "Park and its famous animal", "very common",
            "'Which park is famous for one-horned rhinoceros', 'Asiatic lion is found in', 'only floating national park'.",
            ["Start from the animal, not the park.", "Rhino: Kaziranga. Lion: Gir. Tahr: Eravikulam. Macaque: Silent Valley. Hangul: Dachigam. Snow leopard: Hemis.",
             "Sangai: Keibul Lamjao. Crocodile: Bhitarkanika. Four big cats: Namdapha.", "Tigers live in many parks, so the question usually names a rarer animal."],
            "The rare animal is the clue.",
            "The Asiatic lion's last natural home is which park?",
            ["The Asiatic lion lives in one forest.", "That forest is in Gujarat."],
            "Gir National Park"),
        pat("ga-pk-p4", "UNESCO natural heritage sites and protected-area categories", "occasional",
            "'Which national park is a World Heritage Site', 'Khangchendzonga is what type of site', 'biosphere reserve versus national park'.",
            ["Natural sites: Kaziranga, Manas, Keoladeo (1985), Sundarbans (1987), Nanda Devi and Valley of Flowers, Great Himalayan NP, Western Ghats, Khangchendzonga.",
             "Khangchendzonga (Sikkim, 2016) is India's first mixed site: nature plus culture.", "Categories: national park (strictest), sanctuary, biosphere reserve (largest, includes people)."],
            "A small list of sites and one 'mixed' fact cover this.",
            "Khangchendzonga National Park was inscribed in 2016. Why is it special?",
            ["It is valued for nature.", "It is also valued for Sikkimese culture."],
            "It is a mixed heritage site (Sikkim)."),
        pat("ga-pk-p5", "Wetlands, sanctuaries and mass-nesting sites", "occasional",
            "'Olive Ridley turtles nest at', 'which lake has Irrawaddy dolphins', 'phumdis are found in', Ramsar wetlands.",
            ["Gahirmatha (Odisha): mass nesting (arribada) of Olive Ridley turtles; Rushikulya is another Odisha nesting beach.", "Chilika (Odisha): Irrawaddy dolphins, winter birds. Loktak (Manipur): phumdis.",
             "Keoladeo (Bharatpur): the classic bird sanctuary; Siberian cranes once wintered there."],
            "Each site has one signature species.",
            "Olive Ridley turtles are famous for mass nesting (arribada) at which place?",
            ["The site is on the Odisha coast.", "It is a marine sanctuary.", "Lakhs of turtles nest together."],
            "Gahirmatha. Rushikulya is the other Odisha nesting beach."),
        pat("ga-pk-p6", "Reintroductions and rehabilitation", "common",
            "'Cheetahs were brought to', 'from which country', 'rhino rehabilitation park', 'Great Indian Bustard park'.",
            ["Cheetahs: Kuno (MP), from Namibia, September 2022.", "Rhino rehabilitation: Dudhwa (UP).", "Great Indian Bustard: Desert NP (Rajasthan)."],
            "Each programme has one place.",
            "Cheetahs were reintroduced in India in September 2022 at which national park?",
            ["The park is in Madhya Pradesh.", "The cheetahs came from Namibia."],
            "Kuno National Park"),
    ],
)


# ---------------------------------------------------------------------
def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


data = json.loads(TOPIC.read_text(encoding="utf-8"))
assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
for sub in data["subtopics"]:
    new = SUBS[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in new["patterns"]]
    assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
    assert len(new_ids) == len(set(new_ids))
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sub["id"], len(n))
    assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
    for p in new["patterns"]:
        assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:80])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
