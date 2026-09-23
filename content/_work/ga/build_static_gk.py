from gacommon import Q, save_topic

S = []

S.append({
"id": "books-authors",
"title": "Books & Authors",
"concept": """**Classics & freedom-era works**

| Book | Author |
|---|---|
| *Arthashastra* | Kautilya (Chanakya) |
| *Gitanjali* (Nobel 1913) | Rabindranath Tagore |
| *Anandamath* (contains *Vande Mataram*) | Bankim Chandra Chattopadhyay |
| *Godan*, *Gaban*, *Nirmala* | Munshi Premchand |
| *Hind Swaraj* (1909), *My Experiments with Truth* | M.K. Gandhi |
| *The Discovery of India*, *Glimpses of World History* | Jawaharlal Nehru |
| *Poverty and Un-British Rule in India* | Dadabhai Naoroji |
| *India Wins Freedom* | Maulana Abul Kalam Azad |
| *Annihilation of Caste* | B.R. Ambedkar |
| *Unto This Last* (Gandhi's *Sarvodaya*) | John Ruskin |

**Modern Indian fiction**

| Book | Author | Note |
|---|---|---|
| *Midnight's Children* | Salman Rushdie | Booker 1981 |
| *The God of Small Things* | Arundhati Roy | Booker 1997 |
| *The Inheritance of Loss* | Kiran Desai | Booker 2006 |
| *The White Tiger* | Aravind Adiga | Booker 2008 |
| *Train to Pakistan* | Khushwant Singh | Partition novel |
| *The Guide*, *Malgudi Days* | R.K. Narayan | Fictional town Malgudi |
| *A Suitable Boy* | Vikram Seth | |
| *Tomb of Sand* (*Ret Samadhi*) | Geetanjali Shree (tr. Daisy Rockwell) | International Booker 2022 |

**Sports & public-life autobiographies**

| Book | Author |
|---|---|
| *Playing It My Way* | Sachin Tendulkar |
| *Sunny Days* | Sunil Gavaskar |
| *Straight from the Heart* | Kapil Dev |
| *The Race of My Life* | Milkha Singh |
| *Unbreakable* | M.C. Mary Kom |
| *Ace Against Odds* | Sania Mirza |
| *The Test of My Life* | Yuvraj Singh |
| *Ignited Minds*, *India 2020* | A.P.J. Abdul Kalam |""",
"formulas": [],
"tricks": [
 {"title": "Booker ladder — \"Rushdie 81, Roy 97, Desai 06, Adiga 08\"",
  "body": "Four India-connected Booker winners in order: **Midnight's Children → God of Small Things → Inheritance of Loss → White Tiger**. **Geetanjali Shree (2022)** won the **International** Booker (for translated fiction).",
  "example": {"q": "Who wrote 'The White Tiger', the 2008 Booker winner?", "solution": "**Aravind Adiga**."}},
 {"title": "Sports book hooks",
  "body": "**Sunny** Days = **Sunil** Gavaskar · **Race** of My Life = Milkha (the 'Flying Sikh' raced) · **Unbreakable** = Mary Kom (boxer) · **Ace** = Sania (tennis ace) · **Test** of My Life = Yuvraj (cancer battle)."}
],
"mistakes": [
 "*Vande Mataram* is from *Anandamath* (Bankim), **not** from Tagore's works — Tagore wrote *Jana Gana Mana*.",
 "*Unto This Last* was written by **John Ruskin**; Gandhi only paraphrased it into Gujarati as *Sarvodaya*.",
 "*The Discovery of India* was written by **Nehru** in Ahmednagar Fort jail (1942–46)."
]
})

S.append({
"id": "sports",
"title": "Sports: Trophies, Terms, Players & Venues",
"concept": """**Trophy → sport**

| Trophy / Cup | Sport |
|---|---|
| Ranji, Duleep, Irani, Deodhar, Vijay Hazare | **Cricket** |
| Santosh Trophy, Subroto Cup (schools), I-League | **Football** |
| Beighton Cup, Aga Khan Cup, Dhyan Chand Trophy | **Hockey** |
| **Thomas Cup** (men), **Uber Cup** (women), Sudirman Cup (mixed) | **Badminton** |
| **Davis Cup** (men), Billie Jean King Cup (women) | **Tennis** |
| Ryder Cup, Walker Cup | Golf |
| Stanley Cup | Ice hockey |
| Wightman Cup | Tennis (women, UK–USA, discontinued) |

**Players per side**

| 5 | 6 | 7 | 9 | 11 | 15 |
|---|---|---|---|---|---|
| Basketball | Volleyball, ice hockey | Kabaddi, netball, water polo, handball | Kho-kho (in field), baseball | Cricket, football, hockey | Rugby union |

Polo = 4 per side.

**Terms → sport**: *Googly, LBW, maiden over* → cricket · *Bully, penalty corner* → hockey · *Love, deuce, ace* → tennis · *Checkmate, castling, en passant* → chess · *Smash, drop shot* → badminton · *Birdie, bogey, caddie* → golf · *Raid, bonus line* → kabaddi · *Punch, knock-out, uppercut* → boxing.

**Grand Slam surfaces:** Australian Open (hard, Jan) · **French Open / Roland Garros (clay)** · **Wimbledon (grass)** · US Open (hard, Flushing Meadows).

**Olympics essentials**
- Paris **2024** (India: 6 medals — Neeraj Chopra silver; **Manu Bhaker** two bronzes, the first Indian after independence to win two medals at one Games).
- Los Angeles **2028**, Brisbane **2032**.
- **Abhinav Bindra** — India's first individual Olympic gold (**Beijing 2008**, 10 m air rifle).
- **Neeraj Chopra** — javelin gold, Tokyo 2020 (India's first in athletics).
- Olympic rings: 5 (blue, yellow, black, green, red) = 5 continents.

**Indian stadiums:** Eden Gardens (Kolkata) · Narendra Modi Stadium (Motera, Ahmedabad — world's largest cricket stadium) · Wankhede (Mumbai) · Chepauk / M.A. Chidambaram (Chennai) · Salt Lake / Vivekananda Yuba Bharati Krirangan (Kolkata, football) · Major Dhyan Chand National Stadium (Delhi, hockey).""",
"formulas": [],
"tricks": [
 {"title": "Badminton cups — \"Thomas the man, Uber the woman\"",
  "body": "**Thomas** Cup = men's team, **Uber** Cup = women's team, **Sudirman** = mixed. Tennis: **D**avis = **D**udes (men), **B**illie Jean King = women.",
  "example": {"q": "India won the Thomas Cup for the first time in 2022. The sport is —", "solution": "**Badminton** (men's team championship)."}},
 {"title": "Team size — \"Basket 5, Volley 6, Kabaddi 7\"",
  "body": "Count up: basketball **5**, volleyball **6**, kabaddi **7**; then cricket/football/hockey **11**."}
],
"mistakes": [
 "Santosh Trophy is **football**; Ranji Trophy is **cricket**.",
 "Roland Garros is **clay**; Wimbledon is the only Grand Slam on **grass**.",
 "Abhinav Bindra won India's first **individual** gold; India had team golds in hockey much earlier (from 1928)."
]
})

S.append({
"id": "awards",
"title": "Awards & Honours",
"concept": """| Award | Started | Field | First / key facts |
|---|---|---|---|
| **Bharat Ratna** | **1954** | Highest civilian honour | First: **C. Rajagopalachari, S. Radhakrishnan, C.V. Raman** (1954). First woman: **Indira Gandhi (1971)**. First sportsperson: **Sachin Tendulkar (2014)**. First non-Indian: Khan Abdul Ghaffar Khan (1987); Nelson Mandela (1990). Normally max **3 per year** |
| Padma Vibhushan / Bhushan / Shri | 1954 | 2nd / 3rd / 4th civilian honours | Announced on Republic Day eve |
| **Param Vir Chakra** | 1950 | Highest wartime gallantry | First: **Maj. Somnath Sharma** (1947, posthumous) |
| Ashoka Chakra | 1952 | Highest peacetime gallantry | |
| **Jnanpith** | **1965** | Highest literary award (Indian languages) | First: **G. Sankara Kurup** (Malayalam, *Odakkuzhal*) |
| Sahitya Akademi Award | 1955 | Literature (24 languages) | |
| **Dadasaheb Phalke** | **1969** | Lifetime contribution to cinema | First: **Devika Rani** |
| **Major Dhyan Chand Khel Ratna** | 1991–92 | Highest sports honour | Renamed from Rajiv Gandhi Khel Ratna in **2021**; first winner **Viswanathan Anand** |
| **Arjuna Award** | 1961 | Sportspersons | |
| **Dronacharya Award** | 1985 | Sports **coaches** | |
| Dhyan Chand Award | 2002 | Lifetime achievement in sport | |

**Indian Nobel laureates**

| Year | Laureate | Field |
|---|---|---|
| 1913 | **Rabindranath Tagore** | Literature (first Asian) |
| 1930 | **C.V. Raman** | Physics (Raman effect) |
| 1979 | **Mother Teresa** | Peace |
| 1998 | **Amartya Sen** | Economics (welfare economics) |
| 2014 | **Kailash Satyarthi** (with Malala Yousafzai) | Peace |

**International awards by field:** Pulitzer → journalism & literature (USA) · Booker → English fiction · Oscar (Academy Award) → film · Grammy → music · Pritzker → architecture · Abel Prize & Fields Medal → mathematics · Kalinga Prize → popularising science (UNESCO).""",
"formulas": [],
"tricks": [
 {"title": "First Bharat Ratnas — \"RRR 1954\"",
  "body": "**R**ajagopalachari, **R**adhakrishnan, **R**aman — three Rs in 1954.",
  "example": {"q": "Which of the following was NOT among the first Bharat Ratna recipients in 1954? (a) C.V. Raman (b) S. Radhakrishnan (c) Jawaharlal Nehru (d) C. Rajagopalachari", "solution": "**Nehru** (awarded 1955). 1954 = RRR."}},
 {"title": "Award decade ladder",
  "body": "**50s** Bharat Ratna (54) → **60s** Arjuna (61), Jnanpith (65), Phalke (69) → **80s** Dronacharya (85) → **90s** Khel Ratna (91–92)."}
],
"mistakes": [
 "Dronacharya is for **coaches**; Arjuna is for **players**.",
 "The first Phalke awardee was **Devika Rani**, not Prithviraj Kapoor (he got it posthumously in 1971).",
 "Khel Ratna was **renamed** after Major Dhyan Chand in 2021; the separate *Dhyan Chand Award* (lifetime) is a different award."
]
})

S.append({
"id": "important-days",
"title": "Important Days",
"concept": """**National days (India)**

| Date | Day | Why |
|---|---|---|
| 12 Jan | **National Youth Day** | Birth anniversary of **Swami Vivekananda** |
| 15 Jan | Army Day | K.M. Cariappa took over as C-in-C (1949) |
| 25 Jan | National Voters' Day | ECI founded 25 Jan 1950 |
| **28 Feb** | **National Science Day** | Discovery of the **Raman effect** (1928) |
| 1 Jul | National Doctors' Day | Dr B.C. Roy |
| **29 Aug** | **National Sports Day** | Major **Dhyan Chand**'s birthday |
| 5 Sep | Teachers' Day | Dr S. Radhakrishnan |
| 14 Sep | Hindi Diwas | Hindi adopted as official language (1949) |
| **15 Sep** | **Engineers' Day** | **M. Visvesvaraya** |
| 8 Oct | Air Force Day | IAF formed 1932 |
| 31 Oct | National Unity Day (Rashtriya Ekta Diwas) | Sardar Patel |
| 14 Nov | Children's Day | Nehru |
| 26 Nov | **Constitution Day** (Samvidhan Divas) | Constitution adopted 1949 |
| 4 Dec | Navy Day | Operation Trident (1971) |
| **22 Dec** | **National Mathematics Day** | **Srinivasa Ramanujan** |
| 23 Dec | Kisan Diwas | Chaudhary Charan Singh |
| 25 Dec | Good Governance Day | A.B. Vajpayee |

**International days**

| Date | Day |
|---|---|
| 8 Mar | International Women's Day |
| 22 Mar | World Water Day |
| 7 Apr | World Health Day (WHO founded 1948) |
| 22 Apr | Earth Day |
| **21 Jun** | **International Day of Yoga** (from 2015) |
| 8 Sep | International Literacy Day |
| 16 Sep | World Ozone Day (Montreal Protocol) |
| 1 Dec | World AIDS Day |
| **10 Dec** | **Human Rights Day** (UDHR 1948) |""",
"formulas": [],
"tricks": [
 {"title": "Birthday days — pair the person",
  "body": "12 Jan **Vivekananda** → youth · 29 Aug **Dhyan Chand** → sports · 5 Sep **Radhakrishnan** → teachers · 15 Sep **Visvesvaraya** → engineers · 14 Nov **Nehru** → children · 22 Dec **Ramanujan** → maths.",
  "example": {"q": "National Mathematics Day (22 December) honours —", "solution": "**Srinivasa Ramanujan** (born 22 Dec 1887)."}},
 {"title": "Two 'Feb–Nov' science/constitution anchors",
  "body": "**28 Feb** = Raman effect (Science Day). **26 Nov** = Constitution adopted (26 Jan = enforced → Republic Day)."}
],
"mistakes": [
 "Constitution Day is **26 November** (adoption); Republic Day is 26 January (enforcement).",
 "National Science Day marks the **discovery** of the Raman effect (1928), not Raman's birthday (7 Nov).",
 "Engineers' Day (15 Sep) is Visvesvaraya's birthday; Teachers' Day (5 Sep) is Radhakrishnan's."
]
})

S.append({
"id": "national-symbols-firsts",
"title": "National Symbols & Firsts",
"concept": """**National symbols**

| Symbol | Details |
|---|---|
| National flag | Designed by **Pingali Venkayya**; ratio **3 : 2**; Ashoka Chakra in navy blue with **24 spokes**; adopted 22 July 1947 |
| National emblem | From the **Lion Capital of Ashoka at Sarnath**; adopted 26 Jan 1950; motto ***Satyameva Jayate*** from the **Mundaka Upanishad** |
| National anthem | *Jana Gana Mana* (Tagore); adopted **24 Jan 1950**; full version **52 seconds** |
| National song | *Vande Mataram* (Bankim, *Anandamath*) |
| Animal / bird / flower | **Tiger** (1973) / **Peacock** / **Lotus** |
| Tree / fruit | **Banyan** / Mango |
| Aquatic animal | **Gangetic river dolphin** (2009) |
| Heritage animal | Elephant (2010) |
| National river | Ganga (2008) |

**Firsts in India**

| First | Person |
|---|---|
| President / Vice-President | Rajendra Prasad / S. Radhakrishnan |
| Indian Governor-General | **C. Rajagopalachari** (only Indian GG) |
| Chief Justice of India | H.J. Kania |
| Chief Election Commissioner | Sukumar Sen |
| Woman Prime Minister | Indira Gandhi (1966) |
| Woman President | Pratibha Patil (2007) |
| Woman Governor | **Sarojini Naidu** (United Provinces, 1947) |
| Woman Chief Minister | **Sucheta Kriplani** (UP, 1963) |
| Woman IPS officer | Kiran Bedi (1972) |
| Woman Supreme Court judge | **M. Fathima Beevi** (1989) |
| Woman Lok Sabha Speaker | Meira Kumar (2009) |
| Indian in space | **Rakesh Sharma** (1984, Soyuz T-11) |
| Indian-born woman in space | Kalpana Chawla (1997) |
| Indian woman to climb Everest | **Bachendri Pal** (1984) |
| Woman to swim the English Channel (Indian) | Arati Saha (1959) |""",
"formulas": [],
"tricks": [
 {"title": "Women firsts — \"Sarojini Governs, Sucheta Chiefs\"",
  "body": "**Governor** → **S**arojini Naidu (1947) · **C**hief **M**inister → **S**ucheta Kriplani (1963). Both from UP.",
  "example": {"q": "Who was India's first woman Chief Minister?", "solution": "**Sucheta Kriplani** (Uttar Pradesh, 1963)."}},
 {"title": "Flag numbers — \"3:2 and 24\"",
  "body": "Length : width = **3 : 2**; chakra spokes = **24**; designer = **Pingali** Venkayya."}
],
"mistakes": [
 "*Satyameva Jayate* is from the **Mundaka Upanishad**, not the Rigveda.",
 "The national aquatic animal is the **Gangetic dolphin**, not the whale shark.",
 "The first Governor-General of independent India was **Mountbatten**; the first (and last) **Indian** GG was Rajagopalachari."
]
})

S.append({
"id": "organisations-countries",
"title": "Organisations, Capitals, Currencies & Parliaments",
"concept": """**International organisation → headquarters**

| Organisation | HQ |
|---|---|
| UN, UNICEF, UNDP | New York |
| **UNESCO** | **Paris** |
| **WHO, WTO, ILO**, UNHCR, Red Cross (ICRC), WMO | **Geneva** |
| IMF, World Bank | Washington, D.C. |
| **FAO**, WFP, IFAD | **Rome** |
| UNEP, UN-Habitat | **Nairobi** |
| IAEA, OPEC, UNIDO | **Vienna** |
| International Court of Justice | **The Hague** |
| Interpol | Lyon |
| ASEAN | Jakarta |
| **SAARC** | **Kathmandu** |
| Asian Development Bank | Manila |
| New Development Bank (BRICS) | Shanghai |
| AIIB | Beijing |
| International Olympic Committee | Lausanne |
| FIFA | Zurich |
| ICC (cricket) | Dubai |
| WWF | Gland, Switzerland |
| Amnesty International | London |

**Currencies**

| Country | Currency | Country | Currency |
|---|---|---|---|
| Bangladesh | **Taka** | Japan | Yen |
| Bhutan | **Ngultrum** | China | Renminbi (yuan) |
| Myanmar | **Kyat** | South Korea | Won |
| Afghanistan | Afghani | Thailand | **Baht** |
| Malaysia | **Ringgit** | Indonesia | Rupiah |
| Vietnam | Dong | UAE | Dirham |
| Saudi Arabia | Riyal | Iran | Rial |
| South Africa | **Rand** | Brazil | Real |
| Russia | Rouble | Mexico | Peso |

**Capitals often asked:** Australia – **Canberra** · Canada – **Ottawa** · Brazil – Brasília · New Zealand – Wellington · Nigeria – Abuja · Turkey – Ankara · Myanmar – **Nay Pyi Taw** · Kazakhstan – Astana · Sri Lanka – Sri Jayawardenepura Kotte (administrative).

**Parliaments**

| Country | Parliament | Country | Parliament |
|---|---|---|---|
| Israel | **Knesset** | Japan | **Diet** |
| Russia | **(State) Duma** / Federal Assembly | Iran | Majlis |
| Norway | Storting | Sweden | Riksdag |
| Denmark | Folketing | Germany | Bundestag |
| Bangladesh | Jatiya Sangsad | Iceland | Althing (among the oldest) |
| USA | Congress | Poland | Sejm |""",
"formulas": [],
"tricks": [
 {"title": "Geneva vs Rome vs Nairobi",
  "body": "**Geneva** = health, trade, labour (WHO, WTO, ILO). **Rome** = food (FAO, WFP, IFAD). **Nairobi** = environment (UNEP) — the only major UN HQ in Africa/Global South.",
  "example": {"q": "The headquarters of the Food and Agriculture Organization (FAO) is in —", "solution": "**Rome**."}},
 {"title": "Neighbour currencies — \"Taka, Ngul, Kyat\"",
  "body": "East side of India: Bangladesh **Taka**, Bhutan **Ngultrum**, Myanmar **Kyat**. Nepal, Sri Lanka and Pakistan use the **rupee**."}
],
"mistakes": [
 "UNESCO is in **Paris**, not Geneva.",
 "Japan's parliament is the **Diet**; Israel's is the **Knesset**.",
 "Australia's capital is **Canberra**, not Sydney; Canada's is **Ottawa**, not Toronto."
]
})

P = [
 {"pattern": "Book ↔ author", "frequency": "very common",
  "howToSpot": "\"Who wrote…\" or \"…is the author of\" with four names.",
  "approach": "Classics and freedom-era books are asked most, then sports autobiographies. Use the Booker ladder for novels."},
 {"pattern": "Trophy / term ↔ sport, team size", "frequency": "very common",
  "howToSpot": "A cup or trophy name, a sports term, or \"how many players\".",
  "approach": "Thomas–Uber–Davis mnemonic; team-size ladder 5-6-7-9-11-15."},
 {"pattern": "Award firsts & field", "frequency": "common",
  "howToSpot": "\"first recipient of\", \"awarded for\", \"instituted in\".",
  "approach": "RRR for Bharat Ratna 1954; Devika Rani for Phalke; G. Sankara Kurup for Jnanpith; Dronacharya = coaches."},
 {"pattern": "Important day ↔ date / person", "frequency": "common",
  "howToSpot": "A national or international day with dates (or the person it honours).",
  "approach": "Tie each date to a birthday or founding event (Vivekananda, Dhyan Chand, Ramanujan, Raman effect)."},
 {"pattern": "HQ / currency / parliament / national symbol", "frequency": "occasional",
  "howToSpot": "\"headquartered at\", \"currency of\", \"parliament of\", \"national … of India\".",
  "approach": "Group HQs by city (Geneva–Rome–Nairobi–Vienna); neighbour currencies by direction."},
]

SE = [
 Q("sgk-ex01", "Which of the following pairs of book and author is **NOT** correctly matched?",
   ["Anandamath — Bankim Chandra Chattopadhyay", "India Wins Freedom — Maulana Abul Kalam Azad", "The Discovery of India — Jawaharlal Nehru", "Hind Swaraj — Bal Gangadhar Tilak"], 3,
   "*Hind Swaraj* (1909) was written by **M.K. Gandhi** on board a ship from London to South Africa. Tilak's famous works are *Gita Rahasya* and *The Arctic Home in the Vedas*. The other pairs are correct.",
   "Hind Swaraj = Gandhi's first manifesto; Tilak = Gita Rahasya.",
   "medium", "books-authors", "Book ↔ author (odd pair)", 25),
 Q("sgk-ex02", "How many players does each side have on court in a game of **volleyball**?",
   ["5", "6", "7", "9"], 1,
   "Volleyball is played **6-a-side**. Basketball has 5, kabaddi 7 and baseball/kho-kho 9.",
   "Basket 5, **Volley 6**, Kabaddi 7.",
   "easy", "sports", "Team size", 15),
 Q("sgk-ex03", "Who was the first recipient of the **Dadasaheb Phalke Award**, instituted in 1969?",
   ["Prithviraj Kapoor", "Devika Rani", "Raj Kapoor", "Satyajit Ray"], 1,
   "Actress **Devika Rani** ('First Lady of Indian Cinema') received the first Phalke Award for 1969. Prithviraj Kapoor received it posthumously (1971), Raj Kapoor in 1987 and Satyajit Ray in 1984.",
   "First Phalke = the First Lady of Indian cinema.",
   "medium", "awards", "Award first recipient", 20),
 Q("sgk-ex04", "Match the organisations with their headquarters and choose the correct option.\n\nA. UNESCO  B. UNEP  C. IAEA\n\n1. Vienna  2. Paris  3. Nairobi",
   ["A-2, B-3, C-1", "A-1, B-3, C-2", "A-2, B-1, C-3", "A-3, B-2, C-1"], 0,
   "**UNESCO – Paris**, **UNEP – Nairobi**, **IAEA – Vienna** (also home to OPEC).",
   "Fix UNESCO = Paris first — only option (a) and (c) have A-2; then UNEP = Nairobi settles it.",
   "medium", "organisations-countries", "HQ matching", 30),
]

PR = [
 Q("sgk-q01", "The novel ***Godan*** was written by —",
   ["Munshi Premchand", "Jaishankar Prasad", "Sumitranandan Pant", "Mahadevi Verma"], 0,
   "***Godan*** (1936), Premchand's last completed novel, tells the story of the poor farmer Hori. Premchand also wrote *Gaban* and *Nirmala*.",
   "Godan–Gaban–Nirmala = Premchand trio.", "easy", "books-authors", "Book ↔ author", 15),
 Q("sgk-q02", "***The God of Small Things***, winner of the 1997 Booker Prize, was written by —",
   ["Kiran Desai", "Arundhati Roy", "Anita Desai", "Jhumpa Lahiri"], 1,
   "**Arundhati Roy** won the Booker in **1997** for this Kerala-set debut novel. Kiran Desai won in 2006 for *The Inheritance of Loss*.",
   "Booker ladder: Rushdie 81, **Roy 97**, Desai 06, Adiga 08.", "easy", "books-authors", "Book ↔ author", 15),
 Q("sgk-q03", "***Playing It My Way*** is the autobiography of —",
   ["Rahul Dravid", "Sourav Ganguly", "Sachin Tendulkar", "M.S. Dhoni"], 2,
   "***Playing It My Way*** (2014) is **Sachin Tendulkar**'s autobiography, written with Boria Majumdar.",
   "Sachin — 'my way' of playing for 24 years.", "easy", "books-authors", "Book ↔ author", 15),
 Q("sgk-q04", "***Poverty and Un-British Rule in India***, which set out the 'drain of wealth' theory, was written by —",
   ["R.C. Dutt", "G.K. Gokhale", "Bal Gangadhar Tilak", "Dadabhai Naoroji"], 3,
   "**Dadabhai Naoroji**, the 'Grand Old Man of India', published this book in 1901. R.C. Dutt wrote *The Economic History of India*.",
   "Drain theory = Naoroji.", "medium", "books-authors", "Book ↔ author", 20),
 Q("sgk-q05", "The **Santosh Trophy** is associated with —",
   ["Football", "Hockey", "Cricket", "Badminton"], 0,
   "The **Santosh Trophy** is India's national football championship for state teams, first held in 1941. The Ranji Trophy is its cricket counterpart.",
   "Santosh = football; Ranji = cricket.", "easy", "sports", "Trophy ↔ sport", 15),
 Q("sgk-q06", "The **Uber Cup** is a world team championship for —",
   ["Men's tennis", "Women's badminton", "Women's table tennis", "Men's squash"], 1,
   "The **Uber Cup** is the women's world team badminton championship. The **Thomas Cup** is its men's version.",
   "Thomas the man, **Uber the woman**.", "easy", "sports", "Trophy ↔ sport", 15),
 Q("sgk-q07", "The terms '**bully**' and '**penalty corner**' are associated with —",
   ["Football", "Polo", "Hockey", "Rugby"], 2,
   "Both terms belong to **field hockey** — a bully restarts play between two players, and a penalty corner is awarded for defensive fouls inside the circle.",
   "Penalty **corner** + bully = hockey (football has corner kicks, not penalty corners).", "easy", "sports", "Term ↔ sport", 15),
 Q("sgk-q08", "Which Grand Slam tennis tournament is played on **clay courts**?",
   ["Wimbledon", "Australian Open", "US Open", "French Open"], 3,
   "The **French Open** at Roland Garros, Paris is the only Grand Slam on **clay**. Wimbledon is on grass; the Australian and US Opens are on hard courts.",
   "Red clay = Roland Garros.", "easy", "sports", "Venue / surface", 15),
 Q("sgk-q09", "Which shooter won India's **first individual Olympic gold medal**?",
   ["Abhinav Bindra", "Rajyavardhan Singh Rathore", "Gagan Narang", "Vijay Kumar"], 0,
   "**Abhinav Bindra** won the **10 m air rifle** gold at **Beijing 2008**. Rathore won silver in 2004 (double trap); Narang and Vijay Kumar won medals in 2012.",
   "Beijing 2008 = Bindra = first individual gold.", "easy", "sports", "Olympic firsts", 15),
 Q("sgk-q10", "Which of the following received the **Bharat Ratna in 1954**, the first year of the award?",
   ["Jawaharlal Nehru", "C.V. Raman", "B.R. Ambedkar", "Sardar Vallabhbhai Patel"], 1,
   "The 1954 recipients were **C. Rajagopalachari, S. Radhakrishnan and C.V. Raman**. Nehru got it in 1955; Ambedkar and Patel received it posthumously in 1990 and 1991.",
   "1954 = RRR — only **R**aman is here.", "medium", "awards", "Award first recipients", 20),
 Q("sgk-q11", "The **Dronacharya Award** is given for excellence in —",
   ["Sports coaching", "Teaching in schools", "Military training", "Classical music"], 0,
   "Instituted in **1985**, the Dronacharya Award honours **sports coaches**. The Arjuna Award is for sportspersons.",
   "Drona was the guru (coach) of Arjuna — coach vs player.", "easy", "awards", "Award ↔ field", 15),
 Q("sgk-q12", "The first **Jnanpith Award** (1965) went to G. Sankara Kurup, who wrote in —",
   ["Tamil", "Kannada", "Malayalam", "Bengali"], 2,
   "**G. Sankara Kurup** received the first Jnanpith for his **Malayalam** poetry collection *Odakkuzhal* ('The Bamboo Flute').",
   "First Jnanpith = Kerala poet Kurup.", "medium", "awards", "Award first recipient", 20),
 Q("sgk-q13", "**National Science Day** is celebrated in India on —",
   ["7 November", "15 September", "28 February", "11 May"], 2,
   "**28 February** marks C.V. Raman's discovery of the **Raman effect** in 1928. 7 November is Raman's birthday; 11 May is National Technology Day (Pokhran-II, 1998); 15 September is Engineers' Day.",
   "Science Day = discovery date, not birthday.", "easy", "important-days", "Day ↔ date", 15),
 Q("sgk-q14", "**National Sports Day** (29 August) is observed on the birth anniversary of —",
   ["Milkha Singh", "Major Dhyan Chand", "P.T. Usha", "K.D. Jadhav"], 1,
   "Hockey wizard **Major Dhyan Chand** was born on 29 August 1905. The Khel Ratna is also named after him (since 2021).",
   "29 Aug + hockey wizard = Dhyan Chand.", "easy", "important-days", "Day ↔ person", 15),
 Q("sgk-q15", "Who was the **first woman Governor** of an Indian state?",
   ["Sucheta Kriplani", "Vijaya Lakshmi Pandit", "Padmaja Naidu", "Sarojini Naidu"], 3,
   "**Sarojini Naidu** became Governor of the United Provinces (now UP) in 1947. Sucheta Kriplani was the first woman Chief Minister (UP, 1963). Her daughter Padmaja Naidu later governed West Bengal.",
   "Sarojini **G**overns, Sucheta **C**hiefs.", "medium", "national-symbols-firsts", "Firsts in India", 20),
 Q("sgk-q16", "The motto '**Satyameva Jayate**' on India's national emblem is taken from the —",
   ["Rigveda", "Mundaka Upanishad", "Bhagavad Gita", "Katha Upanishad"], 1,
   "The words come from the **Mundaka Upanishad** ('Truth alone triumphs'). The emblem itself is adapted from Ashoka's Lion Capital at Sarnath.",
   "**M**otto from **M**undaka.", "medium", "national-symbols-firsts", "National symbols", 20),
 Q("sgk-q17", "The currency of **Bhutan** is the —",
   ["Taka", "Kyat", "Ngultrum", "Rupiah"], 2,
   "Bhutan's currency is the **Ngultrum**, pegged at par with the Indian rupee. Taka = Bangladesh, Kyat = Myanmar, Rupiah = Indonesia.",
   "East neighbours: Taka, **Ngultrum**, Kyat.", "easy", "organisations-countries", "Country ↔ currency", 15),
 Q("sgk-q18", "The headquarters of the **International Labour Organization (ILO)** is in —",
   ["Geneva", "New York", "Paris", "Vienna"], 0,
   "The ILO, founded in **1919**, is based in **Geneva**, along with WHO and WTO.",
   "Geneva = health, trade, labour.", "easy", "organisations-countries", "Organisation ↔ HQ", 15),
 Q("sgk-q19", "The **Knesset** is the parliament of —",
   ["Iran", "Japan", "Norway", "Israel"], 3,
   "The **Knesset** is Israel's unicameral legislature in Jerusalem. Iran – Majlis, Japan – Diet, Norway – Storting.",
   "**K**nesset – Hebrew for 'assembly' – Israel.", "easy", "organisations-countries", "Country ↔ parliament", 15),
]

topic = {
 "id": "static-gk",
 "sectionId": "ga",
 "title": "Static GK",
 "order": 12,
 "importance": "high",
 "avgQuestions": {"tier1": 3, "tier2": 3},
 "summary": "Books and authors, sports, awards, important days, national symbols and firsts, and organisations with their headquarters, currencies and parliaments. These are facts that do not change year to year and add up to 2–4 GA questions in almost every shift. Learn them as tables and review often.",
 "subtopics": S,
 "pyqPatterns": P,
 "solvedExamples": SE,
 "practice": PR,
}

if __name__ == "__main__":
    save_topic(topic)
