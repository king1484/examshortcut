# -*- coding: utf-8 -*-
"""Builds content/ssc-cgl/topics/ga/indian-geography.json. Run: py -3 build_indian_geography.py"""
from scicommon import Q, save_topic, place

C_LOCATION = """India lies entirely in the **Northern and Eastern hemispheres**. The mainland extends from **8°4'N to 37°6'N** latitude and **68°7'E to 97°25'E** longitude. Area is about **32.87 lakh sq km (3.287 million sq km)** — roughly **2.4%** of the world's land area, making India the **7th largest** country.

### Key location facts
| Fact | Answer |
|---|---|
| Tropic of Cancer (23.5°N) passes through | **8 states**: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram |
| Standard Meridian (IST) | **82°30'E**, passes near **Mirzapur (UP)**; IST = GMT + 5:30 |
| States the Standard Meridian crosses | Uttar Pradesh, Madhya Pradesh, Chhattisgarh, Odisha, Andhra Pradesh |
| Southernmost point | **Indira Point** (Great Nicobar); mainland tip = **Kanyakumari** |
| Largest / smallest state (area) | **Rajasthan** / **Goa** |
| State with longest coastline | **Gujarat** |
| Coastline | 7,516.6 km (long-used figure; a 2024-25 re-measurement by a finer method reported about 11,099 km) |
| Land frontier | about 15,200 km |

### Neighbours and land border length (MHA figures)
| Neighbour | Border (km) | Remember |
|---|---|---|
| **Bangladesh** | 4,096.7 | **Longest** border |
| China | 3,488 | McMahon Line in the east |
| Pakistan | 3,323 | Radcliffe Line (1947) |
| Nepal | 1,751 | Open border |
| Myanmar | 1,643 | |
| Bhutan | 699 | |
| Afghanistan | 106 | **Shortest** border |

### Water bodies around India
- **Palk Strait** and **Gulf of Mannar** separate India from **Sri Lanka**; Adam's Bridge (Ram Setu) lies between them.
- **Ten Degree Channel** separates **Andaman** from **Nicobar**; **Duncan Passage** separates South Andaman from Little Andaman.
- **Eight Degree Channel** separates **Minicoy** (India) from the **Maldives**; **Nine Degree Channel** separates Minicoy from the main Lakshadweep group.
- **Barren Island** (Andaman Sea) is India's **only active volcano**; Narcondam is a dormant volcano.
- Andaman & Nicobar are the peaks of a submerged mountain chain; **Lakshadweep** islands are **coral** (atoll) islands.
"""

C_PHYSIO = """India has six physiographic divisions: **Himalayas, Northern Plains, Peninsular Plateau, Indian Desert, Coastal Plains and Islands**.

### The Himalayas — three parallel ranges (north to south)
| Range | Other name | Key point |
|---|---|---|
| **Himadri** | Greater / Inner Himalaya | Highest peaks, perennial snow |
| **Himachal** | Lesser / Middle Himalaya | Hill stations — Shimla, Mussoorie, Nainital; Pir Panjal, Dhauladhar ranges |
| **Shiwalik** | Outer Himalaya | Youngest, lowest; **Duns** (Dehradun) are longitudinal valleys between Himachal and Shiwalik |

The **Aravallis** are the **oldest fold mountains** of India; the Himalayas are among the youngest.

### Highest peaks to remember
| Peak | Where | Note |
|---|---|---|
| **K2 (Godwin Austen)** | Karakoram, Ladakh (PoK-administered area) | Highest peak claimed by India, 8,611 m |
| **Kangchenjunga** | Sikkim | Highest peak within India's administered territory, 8,586 m |
| Nanda Devi | Uttarakhand | Highest entirely within India |
| **Anamudi** | Anaimalai Hills, Kerala | **Highest peak of South India** (2,695 m) |
| Doddabetta | Nilgiris, Tamil Nadu | Highest peak of Nilgiris |
| **Guru Shikhar** | Mount Abu, Rajasthan | Highest peak of Aravallis |
| Dhupgarh | Satpura (Pachmarhi), MP | Highest peak of Satpura |

### Mountain passes (very common PYQ)
| Pass | State/UT | Connects / note |
|---|---|---|
| **Karakoram Pass** | Ladakh | Ladakh–Xinjiang (China) |
| **Khardung La** | Ladakh | Leh–Nubra valley; one of the highest motorable passes |
| **Zoji La** | Ladakh / J&K | Srinagar–Kargil–Leh |
| **Banihal** | J&K | Jammu–Srinagar (Jawahar Tunnel, Pir Panjal) |
| **Rohtang** | Himachal Pradesh | Kullu–Lahaul-Spiti; Atal Tunnel runs beneath it |
| **Baralacha La** | Himachal Pradesh | Manali–Leh road |
| **Shipki La** | Himachal Pradesh | **Sutlej enters India** here; route to Tibet |
| **Lipulekh** | Uttarakhand | India–Tibet–Nepal trijunction; **Kailash Mansarovar** yatra |
| **Mana Pass** | Uttarakhand | Near Badrinath, to Tibet |
| **Nathu La** | Sikkim | India–China trade route, reopened **2006** |
| **Jelep La** | Sikkim | Sikkim–Lhasa via Chumbi valley |
| **Bomdi La** | Arunachal Pradesh | Towards Tawang |
| **Palghat (Palakkad) Gap** | Kerala–Tamil Nadu | Between **Nilgiri** and **Anaimalai** hills |
| **Thal Ghat** / **Bhor Ghat** | Maharashtra | Mumbai–Nashik / **Mumbai–Pune** |

### Peninsular plateau and coasts
- **Western Ghats (Sahyadri)** are continuous and higher; **Eastern Ghats** are broken by rivers. The Western Ghats are a **UNESCO World Heritage Site (2012)** and a biodiversity hotspot.
- **Deccan Trap** — basaltic lava region of Maharashtra; source of **black soil**.
- West coast from north: **Konkan** (Mumbai–Goa) → **Kannad** → **Malabar** (Kerala, with **kayals/backwaters**, e.g. Vembanad).
- East coast: **Northern Circars** (north) and **Coromandel** (south); wide deltas of Mahanadi, Godavari, Krishna, Kaveri.

### Lakes
| Lake | Fact |
|---|---|
| **Wular** (J&K) | Largest **freshwater** lake of India |
| **Chilika** (Odisha) | Largest **brackish-water lagoon** of India |
| **Sambhar** (Rajasthan) | Largest **inland salt** lake |
| **Loktak** (Manipur) | Floating *phumdis*; **Keibul Lamjao**, the only floating national park |
| **Pulicat** (AP–TN) | Lagoon; Sriharikota island separates it from the sea |
| Dal (Srinagar) | Houseboats, shikaras |
"""

C_RIVERS = """### Himalayan rivers (perennial — fed by snow and rain)
| River | Source | Key facts |
|---|---|---|
| **Indus** | Near **Mansarovar**, Tibet | Enters India in Ladakh; tributaries **Jhelum, Chenab, Ravi, Beas, Sutlej**; Indus Waters Treaty **1960** |
| Jhelum | **Verinag** spring (Kashmir) | Flows through Wular lake and Srinagar |
| Chenab | Chandra + Bhaga meet at Tandi (HP) | Largest Indus tributary in volume |
| **Sutlej** | **Rakas Tal** (Tibet) | Enters India at **Shipki La**; **Bhakra Nangal** dam (Gobind Sagar) |
| Beas | Beas Kund near Rohtang | Joins Sutlej at Harike (Punjab) |
| **Ganga** | **Bhagirathi** from Gangotri glacier (Gaumukh) | Bhagirathi + Alaknanda meet at **Devprayag**; **longest river of India (about 2,525 km)** |
| **Yamuna** | Yamunotri glacier | Longest tributary of Ganga; joins at **Prayagraj** |
| **Brahmaputra** | Near Mansarovar (Chemayungdung glacier) | **Tsangpo** in Tibet, **Siang/Dihang** in Arunachal; **Majuli** (Assam) is the largest river island |

**Panch Prayag** (Alaknanda's confluences, upstream to downstream): **Vishnuprayag** (Dhauliganga) → **Nandprayag** (Nandakini) → **Karnaprayag** (Pindar) → **Rudraprayag** (Mandakini) → **Devprayag** (Bhagirathi).

### Peninsular rivers (mostly rain-fed)
| River | Source | Flows into | Key facts |
|---|---|---|---|
| **Godavari** | **Trimbakeshwar**, Nashik | Bay of Bengal | **Longest peninsular river**, 'Dakshin Ganga' |
| **Krishna** | Near **Mahabaleshwar** | Bay of Bengal | Nagarjuna Sagar, Srisailam, Almatti dams |
| **Kaveri** | **Talakaveri**, Brahmagiri hills (Kodagu) | Bay of Bengal | Shivanasamudra and Hogenakkal falls; **Mettur** dam; KRS dam |
| **Mahanadi** | Sihawa, Chhattisgarh | Bay of Bengal | **Hirakud** dam — longest earthen dam |
| **Narmada** | **Amarkantak** (MP) | **Arabian Sea** | Flows **west** in a **rift valley**; Dhuandhar falls at Bhedaghat (Jabalpur); **Sardar Sarovar** dam; forms an estuary |
| **Tapi** | Multai, Betul (MP) | Arabian Sea | West-flowing, rift valley; Surat on its bank |
| **Mahi** | Vindhyas (MP) | Gulf of Khambhat | Crosses the **Tropic of Cancer twice** |
| **Luni** | Aravallis near Ajmer | **Rann of Kutch** | Does not reach the sea as a regular river; saline lower course |

West-flowing rivers (Narmada, Tapi) form **estuaries**; east-flowing ones form **deltas**.

### Dams and waterfalls
| Dam | River | | Waterfall | River |
|---|---|---|---|---|
| **Tehri** (highest dam of India) | Bhagirathi | | **Jog / Gersoppa** | **Sharavati** (Karnataka) |
| **Bhakra Nangal** | Sutlej | | **Chitrakote** ('Niagara of India') | **Indravati** (Chhattisgarh) |
| **Hirakud** | Mahanadi | | **Dudhsagar** | **Mandovi** (Goa) |
| **Sardar Sarovar** | Narmada | | **Athirappilly** | Chalakudy (Kerala) |
| **Nagarjuna Sagar** | Krishna | | **Shivanasamudra, Hogenakkal** | Kaveri |
| **Mettur** | Kaveri | | Dhuandhar | Narmada |
| **Idukki** | Periyar | | | |
| **Koyna** | Koyna (Maharashtra) | | | |
| Farakka Barrage | Ganga (West Bengal) | | | |
"""

C_CLIMATE_SOIL = """### Monsoon and seasons
- India has a **tropical monsoon** climate. The **south-west monsoon** normally reaches **Kerala around 1 June** and covers the whole country by mid-July.
- The monsoon has two branches: **Arabian Sea** branch (stronger; heavy rain on the Western Ghats) and **Bay of Bengal** branch (NE India, Gangetic plains).
- **Mawsynram** and **Cherrapunji (Sohra)** in Meghalaya record some of the world's highest rainfall (funnel-shaped Khasi hills).
- **Retreating / north-east monsoon (Oct–Dec)** gives most of the rain to the **Tamil Nadu (Coromandel) coast**.
- Leeward side of the Western Ghats (e.g. interior Karnataka, Marathwada) is a **rain-shadow** area.

### Local winds and pre-monsoon showers
| Name | Region | Nature |
|---|---|---|
| **Loo** | North Indian plains | Hot, dry, dusty summer wind |
| **Mango showers** | Kerala, Karnataka coast | Pre-monsoon showers, help mangoes ripen |
| **Cherry / Coffee blossoms** | Karnataka | Pre-monsoon showers for coffee flowering |
| **Kalbaisakhi (Nor'westers)** | West Bengal, Assam | Violent evening thunderstorms; 'Tea showers' in Assam help tea |
| **Western disturbances** | Punjab, Haryana, J&K | Winter rain from the Mediterranean region; good for **rabi wheat** |

### Soils of India (ICAR recognises 8 main groups)
| Soil | Where | Key properties / crops |
|---|---|---|
| **Alluvial** | Northern plains, deltas | **Most widespread**; *khadar* = new, fertile; *bhangar* = old, has kankar; rice, wheat, sugarcane |
| **Black (Regur)** | Deccan trap — Maharashtra, Gujarat, MP | Formed from **basalt**; rich in **lime, iron, magnesium, potash**; poor in **nitrogen, phosphorus**; high moisture retention, 'self-ploughing' cracks; **cotton** ('black cotton soil') |
| **Red and yellow** | Tamil Nadu, Karnataka, Odisha, Chhattisgarh | Red due to **iron oxide**; yellow when hydrated; poor in N, P, humus |
| **Laterite** | Western Ghats, Kerala, Odisha hills, NE | Formed by **leaching** under high rain and heat (Latin *later* = brick); good for **tea, coffee, cashew** after manuring |
| **Arid / desert** | Rajasthan | Sandy, saline, low humus; kankar layer |
| **Mountain / forest** | Himalayan slopes | Rich in humus, acidic |
| **Saline / alkaline** | Dry areas, over-irrigated Punjab–Haryana | *Reh, kallar, usar*; treated with **gypsum** |
| **Peaty / marshy** | Kerala (*kari*), Sundarbans | Heavy rain, high organic matter |

Soil erosion forms: **gully erosion** creates **ravines** (Chambal badlands); **sheet erosion** removes topsoil evenly. Contour ploughing, terrace farming and shelter belts check erosion.
"""

C_AGRI_MIN = """### Cropping seasons
| Season | Sowing – harvest | Crops |
|---|---|---|
| **Kharif** | June–July (monsoon) → Sep–Oct | **Rice, maize, jowar, bajra, cotton, jute, groundnut, soybean** |
| **Rabi** | Oct–Nov (winter) → Mar–Apr | **Wheat, barley, gram, mustard, peas** |
| **Zaid** | Short summer season | **Watermelon, muskmelon, cucumber**, fodder |

Leading states (stable, frequently asked): **tea — Assam**, **coffee — Karnataka**, **rubber — Kerala**, **jute — West Bengal** ('golden fibre'), **sugarcane — Uttar Pradesh**. Coffee arrived via Baba Budan hills (Karnataka).

### Revolutions in agriculture
| Revolution | Product | Name linked |
|---|---|---|
| **Green** | Food grains (wheat, rice) | **M.S. Swaminathan** (India); Norman Borlaug (world) |
| **White** (Operation Flood, 1970) | **Milk** | **Verghese Kurien** (Amul, Anand) |
| **Blue** | **Fish** | |
| **Yellow** | **Oilseeds** | |
| **Silver** | **Eggs** / poultry | |
| **Round** | **Potato** | |
| **Golden** | Horticulture / honey | |

### Minerals and energy (location facts)
| Resource | Place |
|---|---|
| **Coal** | **Jharia** (Jharkhand, largest coking coal field); **Raniganj** (WB, first mine, 1774); Singrauli, Talcher, Korba |
| **Lignite** | **Neyveli** (Tamil Nadu) |
| **Petroleum** | **Digboi** (Assam) — oldest refinery (**1901**); **Mumbai High** — offshore field; Ankleshwar (Gujarat) |
| **Iron ore** | **Bailadila** (Chhattisgarh), Odisha–Jharkhand belt, Bellary (Karnataka), Goa |
| **Bauxite** | Odisha (Panchpatmali, Koraput) — largest reserves |
| **Mica** | **Koderma** (Jharkhand), Nellore (AP) |
| **Copper** | **Khetri** (Rajasthan), Singhbhum (Jharkhand), Malanjkhand (MP) |
| **Gold** | **Hutti** (Karnataka); **Kolar** Gold Fields closed in 2001 |
| **Zinc–lead** | **Zawar** (Rajasthan) |
| **Monazite (thorium)** | Kerala beach sands |

### Ports (east and west)
- West: **Deendayal (Kandla)** — tidal port, Gujarat; **Mumbai**; **JNPT (Nhava Sheva)**; **Mormugao** (Goa, iron-ore export); New Mangalore; **Kochi**.
- East: **V.O. Chidambaranar (Tuticorin)**; **Chennai**; **Kamarajar (Ennore)** — India's first corporatised major port; **Visakhapatnam** — deepest landlocked harbour; **Paradip**; **Syama Prasad Mookerjee (Kolkata)** — riverine port with Haldia dock.
"""

C_PARKS = """India's first national park: **Hailey National Park (1936)**, now **Jim Corbett NP** (Uttarakhand) — also the first **Project Tiger** reserve (**1973**). **Project Elephant** began in **1992**. The first biosphere reserve was **Nilgiri (1986)**.

### National parks — speciality animal / feature
| National park | State / UT | Known for |
|---|---|---|
| **Jim Corbett** | Uttarakhand | First NP; tigers; Ramganga river |
| **Kaziranga** | Assam | **One-horned rhinoceros**; UNESCO WHS (1985) |
| **Manas** | Assam | Tiger, golden langur, pygmy hog; UNESCO WHS |
| **Gir** | Gujarat | Last home of the **Asiatic lion** |
| **Sundarbans** | West Bengal | **Royal Bengal tiger**, mangroves; UNESCO WHS |
| **Keoladeo (Ghana)** | Rajasthan (Bharatpur) | **Birds**, earlier Siberian cranes; UNESCO WHS |
| **Ranthambore**, Sariska | Rajasthan | Tiger reserves |
| **Kanha** | Madhya Pradesh | Hard-ground **barasingha**; setting linked to *The Jungle Book* |
| **Bandhavgarh** | Madhya Pradesh | High tiger density |
| **Kuno** | Madhya Pradesh | **Cheetah** reintroduction (from **Namibia**, Sept **2022**) |
| **Dudhwa** | Uttar Pradesh | Swamp deer, rhino rehabilitation |
| **Hemis** | Ladakh | **Snow leopard**; largest national park of India |
| **Dachigam** | J&K | **Hangul** (Kashmir stag) |
| **Great Himalayan** | Himachal Pradesh | UNESCO WHS (2014) |
| **Nanda Devi & Valley of Flowers** | Uttarakhand | UNESCO WHS; alpine flowers |
| **Keibul Lamjao** | Manipur | Only **floating** NP; **Sangai** (brow-antlered deer) |
| **Namdapha** | Arunachal Pradesh | Four big cats incl. clouded and snow leopard |
| **Silent Valley** | Kerala | **Lion-tailed macaque** |
| **Eravikulam** | Kerala | **Nilgiri tahr** |
| **Periyar** | Kerala | Elephants; tiger reserve around a lake |
| **Bandipur**, **Nagarhole** | Karnataka | Tigers, elephants (Nilgiri Biosphere) |
| **Bhitarkanika** | Odisha | **Saltwater crocodiles**, mangroves |
| **Simlipal** | Odisha | Tigers, elephants, biosphere reserve |

**Gahirmatha** (Odisha) is a marine sanctuary famous for mass nesting (*arribada*) of **Olive Ridley turtles**.
"""

SUBTOPICS = [
    {
        "id": "ig-location",
        "title": "Location, extent, neighbours and islands",
        "concept": C_LOCATION,
        "formulas": [],
        "tricks": [
            {
                "title": "Tropic of Cancer states — 'GRM CJ WTM'",
                "body": "West to east: **G**ujarat, **R**ajasthan, **M**adhya Pradesh, **C**hhattisgarh, **J**harkhand, **W**est Bengal, **T**ripura, **M**izoram. Read it as '**Great Royal Mango, Cool Juice, With Tasty Mangoes**'. Odisha and Bihar are the usual traps — the Tropic misses both.",
                "example": {"q": "Does the Tropic of Cancer pass through Odisha?", "solution": "No. It passes through Jharkhand and West Bengal to the north of Odisha."},
            },
            {
                "title": "Border order: 'Big Cats Prowl Near My Big Area'",
                "body": "Longest to shortest border — **B**angladesh > **C**hina > **P**akistan > **N**epal > **M**yanmar > **B**hutan > **A**fghanistan.",
                "example": {"q": "With which neighbour does India share its shortest land border?", "solution": "Afghanistan (about 106 km, in PoK area)."},
            },
            {
                "title": "Channel numbers go down as you go south-west",
                "body": "**Ten** Degree (Andaman | Nicobar) → **Nine** Degree (Minicoy | Lakshadweep) → **Eight** Degree (Minicoy | Maldives). The Andaman group has the bigger number.",
                "example": None,
            },
        ],
        "mistakes": [
            "Taking Kanyakumari as India's southernmost point — it is Indira Point in Great Nicobar; Kanyakumari is the mainland tip.",
            "Answering China for the longest land border — it is Bangladesh.",
            "Placing the Standard Meridian at Prayagraj — the reference town is Mirzapur (82°30'E).",
        ],
    },
    {
        "id": "ig-physiography",
        "title": "Himalayas, peaks, passes, plateau, coasts and lakes",
        "concept": C_PHYSIO,
        "formulas": [],
        "tricks": [
            {
                "title": "Pass → state by first letter group",
                "body": "**Z-K-K** (Zoji, Khardung, Karakoram) = **Ladakh**; **R-S-B** (Rohtang, Shipki, Baralacha) = **Himachal**; **L-M** (Lipulekh, Mana) = **Uttarakhand**; **N-J** (Nathu, Jelep) = **Sikkim**; **Bomdi** = **Arunachal**; **Palghat** = Kerala–TN gap.",
                "example": {"q": "Shipki La lies in which state?", "solution": "Himachal Pradesh — it is where the Sutlej enters India."},
            },
            {
                "title": "Highest-peak ladder",
                "body": "India claimed: **K2** → India administered: **Kangchenjunga** → South India: **Anamudi** → Nilgiris: **Doddabetta** → Aravallis: **Guru Shikhar** → Satpura: **Dhupgarh**.",
                "example": None,
            },
            {
                "title": "Lake superlatives: 'Fresh Wular, Brackish Chilika, Salty Sambhar, Floating Loktak'",
                "body": "Say it as one chain. Examiners swap the adjectives between the four lakes.",
                "example": None,
            },
        ],
        "mistakes": [
            "Calling the Shiwaliks the oldest range — they are the youngest; the Aravallis are the oldest fold mountains.",
            "Placing the Duns between Himadri and Himachal — they lie between Himachal and Shiwalik.",
            "Confusing Nathu La (Sikkim) with Lipulekh (Uttarakhand) as the Kailash Mansarovar route — Lipulekh is the traditional one.",
        ],
    },
    {
        "id": "ig-rivers",
        "title": "Rivers, dams and waterfalls",
        "concept": C_RIVERS,
        "formulas": [],
        "tricks": [
            {
                "title": "Panch Prayag order — 'Very Nice Kids Read Daily'",
                "body": "**V**ishnuprayag → **N**andprayag → **K**arnaprayag → **R**udraprayag → **D**evprayag (upstream to downstream). At Devprayag the river becomes the **Ganga**.",
                "example": {"q": "At which confluence does the Mandakini meet the Alaknanda?", "solution": "Rudraprayag."},
            },
            {
                "title": "West-flowers: 'Nobody Takes Mahi Seriously'",
                "body": "**N**armada, **T**api, **M**ahi, **S**abarmati flow into the **Arabian Sea** and form **estuaries**. Narmada and Tapi flow through **rift valleys**.",
                "example": None,
            },
            {
                "title": "Waterfall ↔ river pairs",
                "body": "Jog–Sharavati, Chitrakote–Indravati, Dudhsagar–Mandovi, Athirappilly–Chalakudy, Shivanasamudra/Hogenakkal–Kaveri, Dhuandhar–Narmada.",
                "example": None,
            },
        ],
        "mistakes": [
            "Calling the Godavari India's longest river — it is the longest peninsular river; the Ganga is the longest overall.",
            "Saying the Narmada rises in the Western Ghats — it rises at Amarkantak (MP) and flows west.",
            "Putting Tehri on the Alaknanda — it is on the Bhagirathi.",
        ],
    },
    {
        "id": "ig-climate-soils",
        "title": "Monsoon, local winds and soils",
        "concept": C_CLIMATE_SOIL,
        "formulas": [],
        "tricks": [
            {
                "title": "Black soil rich/poor list",
                "body": "Rich in **'LIMP'** — **L**ime, **I**ron, **M**agnesium, **P**otash. Poor in **'NPH'** — **N**itrogen, **P**hosphorus, **H**umus.",
                "example": {"q": "Black soil is generally deficient in which nutrient?", "solution": "Nitrogen (also phosphorus and organic matter)."},
            },
            {
                "title": "Shower names by crop",
                "body": "Mango showers → **mango** (Kerala); Blossom showers → **coffee** (Karnataka); Kalbaisakhi → **tea/jute/rice** (Bengal, Assam). Western disturbances → **wheat** (rabi) in the north-west.",
                "example": None,
            },
        ],
        "mistakes": [
            "Saying Tamil Nadu gets most rain from the south-west monsoon — it gets most in Oct–Dec from the retreating/north-east monsoon.",
            "Attributing red colour of red soil to aluminium — it is iron oxide.",
            "Treating laterite as naturally fertile — it is leached and needs manure.",
        ],
    },
    {
        "id": "ig-agri-minerals",
        "title": "Agriculture, revolutions, minerals and ports",
        "concept": C_AGRI_MIN,
        "formulas": [],
        "tricks": [
            {
                "title": "Revolution colours",
                "body": "Colour of the product: **White = milk**, **Blue = water/fish**, **Yellow = oilseeds (mustard flower)**, **Silver = eggs (shell shine)**, **Round = potato**, **Green = grains/fields**.",
                "example": {"q": "The Yellow Revolution relates to which product?", "solution": "Oilseeds."},
            },
            {
                "title": "Kharif = 'Monsoon crops need water'",
                "body": "Water-loving rice, jute, cotton → **kharif**. Cool-weather wheat, gram, mustard → **rabi**. Summer melons → **zaid**.",
                "example": None,
            },
        ],
        "mistakes": [
            "Placing Digboi in Gujarat — it is in Assam (1901).",
            "Calling Kolar the working gold mine — Kolar closed in 2001; Hutti is operational.",
            "Classifying maize as only rabi — in most of India it is a kharif crop.",
        ],
    },
    {
        "id": "ig-parks",
        "title": "National parks, tiger reserves and wildlife",
        "concept": C_PARKS,
        "formulas": [],
        "tricks": [
            {
                "title": "Animal-first recall",
                "body": "Rhino → **Kaziranga**; Lion → **Gir**; Cheetah → **Kuno**; Snow leopard → **Hemis**; Hangul → **Dachigam**; Sangai → **Keibul Lamjao**; Nilgiri tahr → **Eravikulam**; Lion-tailed macaque → **Silent Valley**; Saltwater crocodile → **Bhitarkanika**; Olive Ridley → **Gahirmatha**.",
                "example": {"q": "Where is the Sangai deer found?", "solution": "Keibul Lamjao National Park, Manipur (on Loktak lake)."},
            },
            {
                "title": "Year chain 36-73-86-92",
                "body": "1936 first NP (Hailey/Corbett) → 1973 Project Tiger → 1986 first biosphere reserve (Nilgiri) → 1992 Project Elephant.",
                "example": None,
            },
        ],
        "mistakes": [
            "Putting Kanha in Maharashtra — it is in Madhya Pradesh.",
            "Placing Keoladeo in Gujarat — it is at Bharatpur, Rajasthan.",
            "Saying cheetahs were brought to Gir — they were brought to Kuno (MP).",
        ],
    },
]

PYQ = [
    {"pattern": "Pass / national park / dam → state or river", "frequency": "very common", "howToSpot": "'Nathu La is located in...', 'Hirakud dam is built on...', 'Kaziranga is famous for...'", "approach": "Use the grouped tables (pass clusters by state, dam–river pairs, animal-first park list). Eliminate options from the wrong region first."},
    {"pattern": "River origin / confluence / tributary", "frequency": "very common", "howToSpot": "'Which river originates at Amarkantak?', 'Devprayag is the confluence of...'", "approach": "Memorise sources (Amarkantak, Trimbakeshwar, Mahabaleshwar, Talakaveri) and the Panch Prayag chain."},
    {"pattern": "Soil type properties and crops", "frequency": "common", "howToSpot": "'Regur soil is best suited for...', 'Which soil is formed by leaching?'", "approach": "Link each soil to its parent rock/process and one signature crop (black–cotton, laterite–cashew/tea)."},
    {"pattern": "Tropic of Cancer / Standard Meridian / neighbour borders", "frequency": "common", "howToSpot": "'Which state does NOT lie on the Tropic of Cancer?', 'Longest border with...'", "approach": "Use the 8-state mnemonic; remember Bangladesh longest, Afghanistan shortest."},
    {"pattern": "Crop season and agricultural revolutions", "frequency": "common", "howToSpot": "'Which is a rabi crop?', 'Operation Flood is associated with...'", "approach": "Monsoon-sown = kharif; winter-sown = rabi. Match revolution colour to product."},
    {"pattern": "Mineral / oil field / port location", "frequency": "occasional", "howToSpot": "'Jharia is famous for...', 'Oldest oil refinery...'", "approach": "Learn the mineral–place table as flashcards; watch for Digboi vs Mumbai High."},
    {"pattern": "Local winds and monsoon features", "frequency": "occasional", "howToSpot": "'Mango showers occur in...', 'Loo blows in...'", "approach": "Pair each shower/wind with its crop and region."},
]

SOLVED = [
    Q("ig-ex01",
      "Which one of the following states does NOT lie on the Tropic of Cancer?",
      ["Chhattisgarh", "Odisha", "Tripura", "Mizoram"],
      1,
      "The Tropic of Cancer passes through **8 states**: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura and Mizoram. **Odisha** lies entirely south of it.",
      "Mnemonic **GRM CJ WTM** — no 'O' in the chain, so Odisha is out.",
      "easy", "ig-location", "Tropic of Cancer states", 25),
    Q("ig-ex02",
      "Match the mountain passes with the states/UTs in which they are located:\n\n| Pass | State/UT |\n|---|---|\n| a. Shipki La | 1. Sikkim |\n| b. Nathu La | 2. Uttarakhand |\n| c. Lipulekh | 3. Himachal Pradesh |\n| d. Zoji La | 4. Ladakh |",
      ["a-3, b-1, c-2, d-4", "a-1, b-3, c-2, d-4", "a-3, b-1, c-4, d-2", "a-2, b-1, c-3, d-4"],
      0,
      "**Shipki La** — Himachal Pradesh (Sutlej enters India). **Nathu La** — Sikkim (India–China trade). **Lipulekh** — Uttarakhand (Kailash Mansarovar route). **Zoji La** — Ladakh (Srinagar–Leh road). So a-3, b-1, c-2, d-4.",
      "Fix one sure pair first: Nathu La = Sikkim (b-1). That leaves options 1, 3 and 4; then Zoji La = Ladakh (d-4) removes option 3, and Shipki = HP (a-3) picks option 1.",
      "medium", "ig-physiography", "pass–state match", 40),
    Q("ig-ex03",
      "Which soil is known as 'regur' and is ideal for cotton cultivation?",
      ["Laterite soil", "Alluvial soil", "Black soil", "Red soil"],
      2,
      "**Black soil (regur)** forms from the weathering of **basalt** of the Deccan Trap. It holds moisture well, is rich in lime, iron, magnesium and potash, and develops deep cracks in summer ('self-ploughing'). It is called **black cotton soil**.",
      "Regur = Deccan basalt = black = cotton.",
      "easy", "ig-climate-soils", "soil type properties", 20),
    Q("ig-ex04",
      "Hirakud Dam, one of the longest earthen dams in the world, is built on which river?",
      ["Godavari", "Mahanadi", "Krishna", "Narmada"],
      1,
      "**Hirakud Dam** is on the **Mahanadi** near Sambalpur, Odisha. Godavari has no major dam of this name; Krishna has Nagarjuna Sagar; Narmada has Sardar Sarovar.",
      "Hirakud–Mahanadi are both in Odisha — same-state pairing.",
      "easy", "ig-rivers", "dam–river match", 20),
]

PRACTICE = [
    Q("ig-q01",
      "With which neighbouring country does India share its longest international land border?",
      ["China", "Pakistan", "Bangladesh", "Nepal"],
      2,
      "India's border with **Bangladesh** is about **4,096.7 km** — the longest. China (3,488 km) and Pakistan (3,323 km) follow. The shortest is with Afghanistan (106 km).",
      "'Big Cats Prowl Near My Big Area' — B first.", "easy", "ig-location", "neighbour border length", 20),
    Q("ig-q02",
      "The Ten Degree Channel separates which of the following?",
      ["Lakshadweep and Minicoy", "Andaman Islands and Nicobar Islands", "Minicoy and the Maldives", "India and Sri Lanka"],
      1,
      "The **Ten Degree Channel** lies between the **Andaman** and **Nicobar** groups. Nine Degree Channel separates Minicoy from the main Lakshadweep group; Eight Degree Channel separates Minicoy from the Maldives; Palk Strait separates India and Sri Lanka.",
      "Largest number (10) goes with the biggest island group (Andaman–Nicobar).", "medium", "ig-location", "channels and straits", 25),
    Q("ig-q03",
      "India's only active volcano, Barren Island, is located in the:",
      ["Arabian Sea", "Bay of Bengal off the Odisha coast", "Andaman Sea", "Gulf of Mannar"],
      2,
      "**Barren Island** lies in the **Andaman Sea**, east of the main Andaman islands. It is India's only confirmed active volcano; Narcondam nearby is dormant.",
      None, "easy", "ig-location", "island facts", 20),
    Q("ig-q04",
      "Which is the highest peak of South India?",
      ["Doddabetta", "Anamudi", "Mahendragiri", "Guru Shikhar"],
      1,
      "**Anamudi** (2,695 m) in the Anaimalai Hills of Kerala is the highest peak of South India. Doddabetta is the highest in the Nilgiris; Guru Shikhar is the highest in the Aravallis (Rajasthan).",
      "'Ana-mudi' — the 'elephant's forehead' stands tallest in the south.", "easy", "ig-physiography", "highest peak", 20),
    Q("ig-q05",
      "The Palghat Gap connects which two states?",
      ["Karnataka and Kerala", "Kerala and Tamil Nadu", "Tamil Nadu and Andhra Pradesh", "Maharashtra and Goa"],
      1,
      "The **Palghat (Palakkad) Gap** is a low pass in the Western Ghats between the **Nilgiri** and **Anaimalai** hills, linking **Kerala** and **Tamil Nadu**. It lets moist winds reach Coimbatore.",
      None, "medium", "ig-physiography", "pass location", 25),
    Q("ig-q06",
      "Which of the following is the largest brackish-water lagoon in India?",
      ["Wular Lake", "Sambhar Lake", "Chilika Lake", "Loktak Lake"],
      2,
      "**Chilika** (Odisha) is India's largest brackish-water lagoon and a Ramsar site known for Irrawaddy dolphins and migratory birds. Wular is the largest freshwater lake, Sambhar the largest inland salt lake and Loktak has floating phumdis.",
      "Fresh Wular, Brackish Chilika, Salty Sambhar, Floating Loktak.", "easy", "ig-physiography", "lake superlatives", 20),
    Q("ig-q07",
      "The Bhagirathi and the Alaknanda meet at which place to form the Ganga?",
      ["Rudraprayag", "Karnaprayag", "Devprayag", "Haridwar"],
      2,
      "The Ganga is formed at **Devprayag** (Uttarakhand), the last of the Panch Prayag, where the **Bhagirathi** joins the **Alaknanda**. Rudraprayag is the Alaknanda–Mandakini confluence; Karnaprayag is the Alaknanda–Pindar confluence.",
      "'Very Nice Kids Read Daily' — D = Devprayag, the final meeting.", "easy", "ig-rivers", "river confluence", 20),
    Q("ig-q08",
      "Which of the following rivers flows westward through a rift valley and drains into the Arabian Sea?",
      ["Mahanadi", "Narmada", "Godavari", "Krishna"],
      1,
      "The **Narmada** rises at **Amarkantak** and flows **west** between the Vindhya and Satpura ranges in a **rift valley**, entering the **Gulf of Khambhat** (Arabian Sea) through an estuary. The other three flow east into the Bay of Bengal and form deltas.",
      "Estuary = west-flowing (Narmada, Tapi); delta = east-flowing.", "easy", "ig-rivers", "west vs east flowing rivers", 20),
    Q("ig-q09",
      "Jog Falls, one of the highest plunge waterfalls in India, is on which river?",
      ["Kaveri", "Sharavati", "Tungabhadra", "Indravati"],
      1,
      "**Jog (Gersoppa) Falls** in Shivamogga district, Karnataka, is on the **Sharavati**. Chitrakote Falls is on the Indravati; Shivanasamudra and Hogenakkal are on the Kaveri.",
      None, "medium", "ig-rivers", "waterfall–river match", 20),
    Q("ig-q10",
      "Which river is known to cross the Tropic of Cancer twice?",
      ["Sabarmati", "Tapi", "Mahi", "Luni"],
      2,
      "The **Mahi** rises in the Vindhyas of Madhya Pradesh, flows north into Rajasthan, turns back south-west through Gujarat and enters the **Gulf of Khambhat** — crossing the **Tropic of Cancer twice**.",
      None, "hard", "ig-rivers", "river unique fact", 25),
    Q("ig-q11",
      "The retreating (north-east) monsoon brings most of the annual rainfall to which region?",
      ["Konkan coast", "Tamil Nadu coast", "Punjab plains", "Meghalaya plateau"],
      1,
      "The **Coromandel (Tamil Nadu) coast** lies in the rain-shadow of the south-west monsoon. It receives most of its rain from **October to December** when the retreating monsoon winds pick up moisture over the Bay of Bengal.",
      "SW monsoon misses TN; NE monsoon feeds TN.", "medium", "ig-climate-soils", "monsoon distribution", 25),
    Q("ig-q12",
      "Laterite soil is mainly formed by which process?",
      ["Deposition by rivers", "Weathering of basalt lava", "Leaching under high temperature and heavy rainfall", "Wind deposition in arid regions"],
      2,
      "**Laterite** forms where heavy rain and high heat **leach** away silica and lime, leaving iron and aluminium oxides. The name comes from Latin *later* (brick). River deposition gives alluvial soil, basalt weathering gives black soil and wind gives arid soils.",
      None, "medium", "ig-climate-soils", "soil formation process", 25),
    Q("ig-q13",
      "Which of the following is a rabi crop?",
      ["Paddy", "Jute", "Mustard", "Cotton"],
      2,
      "**Mustard** is sown in October–November and harvested in March–April, so it is a **rabi** crop, like wheat, barley and gram. Paddy, jute and cotton are monsoon-sown **kharif** crops.",
      "Winter-sown = rabi; the other three need monsoon water.", "easy", "ig-agri-minerals", "crop season classification", 20),
    Q("ig-q14",
      "Digboi, the site of India's oldest oil refinery, is located in which state?",
      ["Gujarat", "Maharashtra", "Assam", "Arunachal Pradesh"],
      2,
      "The **Digboi** refinery in **Assam** began operating in **1901** and is the oldest operating refinery in India. Gujarat has Ankleshwar and Koyali; Mumbai High is an offshore field off Maharashtra.",
      None, "easy", "ig-agri-minerals", "mineral / oil location", 20),
    Q("ig-q15",
      "Keibul Lamjao, the only floating national park in the world, is home to which animal?",
      ["Hangul", "Sangai deer", "Nilgiri tahr", "One-horned rhinoceros"],
      1,
      "**Keibul Lamjao** on **Loktak Lake, Manipur** floats on *phumdis* and protects the endangered **Sangai** (brow-antlered deer). The hangul lives in Dachigam, the Nilgiri tahr in Eravikulam and the one-horned rhino in Kaziranga.",
      "Animal-first list: Sangai → Keibul Lamjao.", "medium", "ig-parks", "national park speciality", 20),
]

topic = {
    "id": "indian-geography",
    "sectionId": "ga",
    "title": "Indian Geography",
    "importance": "high",
    "avgQuestions": {"tier1": 2, "tier2": 2},
    "summary": "India's location, physiography, passes, rivers and dams, monsoon, soils, crops, minerals and national parks. CGL asks 2-3 direct factual questions here in almost every shift — mostly 'X is located in / built on / famous for' one-liners.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PYQ,
    "solvedExamples": SOLVED,
    "practice": PRACTICE,
}

place(PRACTICE, [0, 1, 3, 1, 0, 2, 3, 0, 1, 3, 2, 2, 0, 3, 1])

if __name__ == "__main__":
    save_topic(topic)
