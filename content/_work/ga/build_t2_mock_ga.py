"""Build t2-mock-1--ga.json — 25 GA questions for the Tier 2 Paper 1 mock.
Run:  py -3 build_t2_mock_ga.py          (needs ca_mock_pool.json from CA agent)
      py -3 build_t2_mock_ga.py --dry    (structural check only, 24 Qs)
"""
import json
import os
import sys

from gacommon import Q, save_mock, validate_question, all_topic_questions

DRY = "--dry" in sys.argv
QS = []
sp = []


def add(*a, **kw):
    x = Q(*a, **kw)
    sp.append(x)
    QS.append(x)


# 1 ANCIENT — inscriptions (slightly deeper recall, suits Tier 2)
add("t2m-q01",
    "The Junagadh rock inscription of Rudradaman I, the earliest known long inscription in chaste Sanskrit, records the original construction of the Sudarshana lake during the reign of which Mauryan ruler?",
    ["Ashoka", "Bindusara", "Chandragupta Maurya", "Samudragupta"], 2,
    "Rudradaman's inscription (c. 150 CE) says the Sudarshana lake in Saurashtra was built by the governor Pushyagupta during Chandragupta Maurya's reign, embellished with conduits under Ashoka by the Yavana Tushaspha, and repaired by Rudradaman himself after a storm.",
    "Chain to remember: built under CGM → conduits under Ashoka → repaired by Rudradaman.",
    "hard", "ancient-history", "inscription-ruler matching", 40)

# 2 ANCIENT — Buddhist councils
add("t2m-q02",
    "The Third Buddhist Council, at which the Abhidhamma Pitaka was compiled, was held at Pataliputra under the patronage of:",
    ["Ashoka", "Ajatashatru", "Kalashoka", "Kanishka"], 0,
    "The Third Council (c. 250 BCE, Pataliputra) was held under Ashoka with Moggaliputta Tissa presiding. Ajatashatru patronised the First Council at Rajgriha, Kalashoka the Second at Vaishali and Kanishka the Fourth in Kashmir.",
    "Council patron order: Ajatashatru → Kalashoka → Ashoka → Kanishka (A-K-A-K).",
    "medium", "ancient-history", "Buddhist councils", 30)

# 3 MEDIEVAL — Vijayanagara administration
add("t2m-q03",
    "The 'amara-nayaka' system, in which military chiefs were assigned territories for revenue in return for troops, was a feature of which empire?",
    ["Delhi Sultanate", "Bahmani kingdom", "Vijayanagara empire", "Maratha confederacy"], 2,
    "The amara-nayaka system of the Vijayanagara empire closely resembled the Iqta system of the Delhi Sultanate: nayakas collected taxes, maintained troops and presented gifts to the king annually.",
    "Amara-nayaka = Vijayanagara's version of the Sultanate iqta.",
    "medium", "medieval-history", "administrative system-empire", 30)

# 4 MODERN — INC firsts
add("t2m-q04",
    "Who presided over the first session of the Indian National Congress held at Bombay in December 1885?",
    ["Womesh Chandra Bonnerjee", "A.O. Hume", "Dadabhai Naoroji", "Surendranath Banerjee"], 0,
    "W.C. Bonnerjee presided over the first INC session (72 delegates, Bombay, 1885). A.O. Hume was the founder-convenor but never president of the first session; Naoroji presided thrice (1886, 1893, 1906 — the Calcutta 'Swaraj' session).",
    "Firsts: Hume founded, Bonnerjee presided, Naoroji said 'Swaraj' (1906).",
    "easy", "modern-history", "INC session-firsts", 25)

# 5 MODERN — Muslim League
add("t2m-q05",
    "The 'Pakistan Resolution', demanding independent states for Muslim-majority areas, was passed at the Lahore session of the Muslim League in which year?",
    ["1930", "1933", "1940", "1946"], 2,
    "The resolution was passed on 23 March 1940 at Minto Park, Lahore, at the League's session presided over by Muhammad Ali Jinnah; the name 'Pakistan' had been coined by Choudhary Rahmat Ali in 1933. In 1946 the League amplified it into a demand for a single sovereign Pakistan state.",
    "23 March 1940 — Lahore, Jinnah in the chair.",
    "medium", "modern-history", "organisation-resolution-year", 30)

# 6 ART — folk dance-state pairs
add("t2m-q06",
    "Which of the following dance–state pairs is correctly matched?",
    ["Ghoomar — Punjab", "Lavani — Maharashtra", "Bihu — Odisha", "Yakshagana — Kerala"], 1,
    "Lavani, with its fast dholki beat, is a folk form of Maharashtra. Ghoomar belongs to Rajasthan, Bihu to Assam and Yakshagana (a dance-drama) to coastal Karnataka.",
    "Lavani–Marathi Tamasha stage; Ghoomar–Rajasthan; Bihu–Assam; Yakshagana–Karnataka.",
    "easy", "art-culture", "dance-state pair check", 20)

# 7 ART — UNESCO World Heritage Sites
add("t2m-q07",
    "Dholavira, the Harappan city with a unique water-harvesting system, was inscribed as a UNESCO World Heritage Site in 2021. It is located in which state?",
    ["Rajasthan", "Haryana", "Punjab", "Gujarat"], 3,
    "Dholavira lies on Khadir Bet island in the Rann of Kachchh, Gujarat — India's 40th World Heritage Site (2021). Ramgarh (Rakhigarhi), the largest Harappan site by some counts, is in Haryana.",
    "Kachchh-K for K for Kutch–Dholavira.",
    "medium", "art-culture", "UNESCO heritage site-state", 30)

# 8 POLITY — President's removal
add("t2m-q08",
    "Under which Article of the Constitution can the President of India be impeached for violation of the Constitution?",
    ["Article 56", "Article 61", "Article 72", "Article 74"], 1,
    "Article 61 lays down impeachment of the President — a quasi-judicial process in Parliament requiring a two-thirds majority of the total membership of each House. Article 56 fixes the term, Article 72 gives pardon powers and Article 74 creates the Council of Ministers to aid and advise.",
    "Impeachment = 61: 'charge-sheet (61) the first citizen'.",
    "medium", "polity", "Article-procedure", 30)

# 9 POLITY — Speaker
add("t2m-q09",
    "The Speaker of the Lok Sabha, when resigning, addresses the letter of resignation to:",
    ["the President", "the Prime Minister", "the Deputy Speaker", "the Chief Justice of India"], 2,
    "Under Article 94, the Speaker resigns by writing to the Deputy Speaker, and the Deputy Speaker resigns by writing to the Speaker. The President resigns to the Vice-President, and the Vice-President resigns to the President.",
    "Speaker ↔ Deputy Speaker; President ↔ Vice-President: each resigns to the partner.",
    "medium", "polity", "resignation addressed to", 25)

# 10 POLITY — Fundamental Duties (statement format)
add("t2m-q10",
    "Consider the following statements about Fundamental Duties:\n"
    "1. They were added to the Constitution by the 42nd Amendment Act, 1976.\n"
    "2. They are contained in Part IV-A, Article 51A.\n"
    "3. Originally ten, an eleventh duty (education of children) was added by the 86th Amendment.\n"
    "Which of the statements is/are correct?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3,
    "All three are correct: the Swaran Singh Committee's recommendation led to the 42nd Amendment inserting Part IV-A with ten duties; the 86th Amendment (2002) added the 11th duty — providing opportunities for education of one's child aged 6-14.",
    "42 added 10, 86 added the 11th — '42+10, 86+11'.",
    "medium", "polity", "statement-based Fundamental Duties", 35)

# 11 POLITY — Schedules / amendments
add("t2m-q11",
    "The Tenth Schedule, which deals with disqualification of legislators on grounds of defection, was added to the Constitution by the:",
    ["52nd Amendment Act, 1985", "44th Amendment Act, 1978", "73rd Amendment Act, 1992", "61st Amendment Act, 1988"], 0,
    "The 52nd Amendment (1985, Rajiv Gandhi government) inserted the Tenth Schedule, known as the anti-defection law. The 91st Amendment (2003) later removed the 'split' exception. The 44th Amendment restored civil-liberty safeguards after the Emergency, the 61st lowered the voting age and the 73rd created Panchayati Raj.",
    "Tenth Schedule = 52nd: 'defect in '85'.",
    "medium", "polity", "Schedule-amendment", 25)

# 12 INDIAN GEOGRAPHY — mountain passes
add("t2m-q12",
    "Which pass provides the crucial road link between Srinagar and Leh in Ladakh?",
    ["Rohtang Pass", "Shipki La", "Nathu La", "Zoji La"], 3,
    "Zoji La (about 3,528 m) in the Great Himalaya connects the Kashmir valley (Srinagar) with Kargil-Leh. Rohtang connects Kullu with Lahaul-Spiti, Shipki La is a Himachal-Tibet pass on the Sutlej route and Nathu La links Sikkim with Tibet.",
    "Zoji La = 'Ze link' between Kashmir and Ladakh.",
    "medium", "indian-geography", "pass-connectivity", 30)

# 13 INDIAN GEOGRAPHY — soils
add("t2m-q13",
    "The moisture-retentive black soil, ideal for cotton cultivation, is also known by which local name?",
    ["Regur", "Khadar", "Bangar", "Laterite"], 0,
    "Black (cotton) soil is called Regur, derived from basaltic Deccan Trap lava, rich in iron, lime and magnesia but poor in nitrogen and phosphorus. Khadar and Bangar are new and old alluvium respectively.",
    "Regur = 'rE Gur' = cotton Gur(u) soil.",
    "easy", "indian-geography", "soil type-name", 20)

# 14 WORLD GEOGRAPHY — volcanism
add("t2m-q14",
    "The 'Ring of Fire', a zone of frequent earthquakes and volcanic eruptions, surrounds which ocean?",
    ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 3,
    "The Circum-Pacific Belt (Ring of Fire) along the margins of the Pacific plate accounts for the bulk of the world's active volcanoes (Mount Fuji, Krakatoa, Mount St. Helens) and major earthquakes (Japan, Chile, Indonesia).",
    "Pacific = peace-named, fire-ringed.",
    "easy", "world-geography", "plate tectonics facts", 20)

# 15 ECONOMY — market regulator
add("t2m-q15",
    "SEBI, set up in 1988 as a non-statutory body, received statutory powers through the SEBI Act in which year?",
    ["1992", "1988", "1999", "2003"], 0,
    "SEBI was constituted in April 1988 by a government resolution and became a statutory regulator under the SEBI Act, 1992 (30 January 1992). It is headquartered in Mumbai. 1999 is the year IRDA was set up.",
    "SEBI: born '88, gets teeth in '92.",
    "medium", "economy", "regulator-statutory year", 25)

# 16 ECONOMY — price indices
add("t2m-q16",
    "The Consumer Price Index (CPI), used by the RBI as the headline measure of inflation, is compiled in India by:",
    ["Reserve Bank of India", "National Statistical Office", "NITI Aayog", "Ministry of Labour and Employment"], 1,
    "The NSO under MoSPI compiles the general CPI series; the Ministry of Labour separately releases CPI for industrial workers (IW), agricultural labourers and rural labourers. RBI targets CPI-combined inflation.",
    "NSO = Numbers for the country (CPI, GDP); RBI only uses it.",
    "medium", "economy", "index-compiling body", 30)

# 17 ECONOMY — institutional HQs
add("t2m-q17",
    "The headquarters of NABARD, the apex development bank for agriculture and rural credit, is located in:",
    ["New Delhi", "Hyderabad", "Pune", "Mumbai"], 3,
    "NABARD (established 12 July 1982 on the B. Sivaraman Committee recommendation) is headquartered in Mumbai, like the RBI and SEBI. SIDBI, the apex bank for small industries, is headquartered in Lucknow.",
    "Mumbai trio: RBI, SEBI, NABARD; Lucknow: SIDBI.",
    "easy", "economy", "institution-HQ", 20)

# 18 PHYSICS — gravitation/satellites
add("t2m-q18",
    "An artificial satellite keeps orbiting the Earth without falling towards it because:",
    ["its weight becomes zero once it is in space", "the gravitational pull of the Earth provides the necessary centripetal force", "air resistance balances the Earth's gravitational pull", "there is no gravity in outer space"], 1,
    "A satellite is in continuous free fall towards the Earth; the horizontal velocity is so high that the Earth's curvature falls away as fast as the satellite falls — gravity supplies exactly the centripetal force (mv²/r) needed for the orbit. Gravity does act in space; air resistance is absent, not balancing.",
    "Satellite = perpetually falling while missing the Earth.",
    "medium", "physics", "satellite motion", 30)

# 19 PHYSICS — instruments
add("t2m-q19",
    "Which instrument is used to measure atmospheric pressure?",
    ["Barometer", "Hygrometer", "Altimeter", "Odometer"], 0,
    "A barometer (Torricelli's mercury barometer) measures atmospheric pressure. A hygrometer measures humidity, an altimeter altitude (used in aircraft) and an odometer distance travelled by a vehicle.",
    "Baro = weight/pressure; Hygro = moisture.",
    "easy", "physics", "instrument-use", 20)

# 20 CHEMISTRY — metals
add("t2m-q20",
    "Among the following metals, which one has the highest electrical conductivity at room temperature?",
    ["Copper", "Gold", "Silver", "Aluminium"], 2,
    "Silver is the best conductor of electricity, followed by copper, gold and aluminium — which is why silver-plated contacts are used in precision switches despite copper being the commercial standard.",
    "Conductivity order: Ag > Cu > Au > Al ('Silver Simply Above').",
    "medium", "chemistry", "metals properties", 30)

# 21 CHEMISTRY — acids & bases
add("t2m-q21",
    "At 25°C, the pH of a neutral aqueous solution is:",
    ["7", "0", "14", "1"], 0,
    "Pure water at 25°C has [H+] = 10^-7 M, hence pH 7. Below 7 is acidic and above 7 basic; the neutrality point shifts slightly with temperature.",
    "Neutral = 7 at room temperature ('seventh heaven at 25').",
    "easy", "chemistry", "pH scale", 20)

# 22 BIOLOGY — hormones
add("t2m-q22",
    "Insulin, the hormone that lowers blood glucose level, is secreted by which gland?",
    ["Liver", "Pancreas", "Thyroid", "Pituitary"], 1,
    "Beta cells of the islets of Langerhans in the pancreas secrete insulin; its deficiency causes diabetes mellitus. Glucagon from alpha cells raises blood sugar.",
    "Insulin–Islets–Internal secretion–Pancreas (I-I-I-P).",
    "easy", "biology", "endocrine glands-hormones", 20)

# 23 BIOLOGY — nervous system
add("t2m-q23",
    "Which part of the human brain is chiefly responsible for maintaining body balance and muscular coordination?",
    ["Cerebrum", "Medulla oblongata", "Cerebellum", "Hypothalamus"], 2,
    "The cerebellum ('little brain') controls posture, balance and fine coordination of voluntary muscles. The medulla controls involuntary actions like heartbeat and breathing, and the hypothalamus regulates hunger, thirst and body temperature.",
    "Cerebellum = Cyclist's friend (balance).",
    "easy", "biology", "brain-parts function", 20)

# 24 STATIC GK — awards
add("t2m-q24",
    "The Ramon Magsaysay Award, often called Asia's Nobel, is given in the memory of a former President of which country?",
    ["Thailand", "Philippines", "Indonesia", "Malaysia"], 1,
    "The award, instituted in 1957, honours Ramon Magsaysay, President of the Philippines (1953-57). Vinoba Bhave was its first (1958) Indian recipient.",
    "Magsaysay–Manila–Philippines (M-M-P).",
    "easy", "static-gk", "award-country of origin", 20)

if DRY:
    for x in sp:
        validate_question(x, "t2-mock-1")
    ans = [x["answer"] for x in sp]
    print(f"DRY OK: {len(sp)} Qs, spread {[ans.count(i) for i in range(4)]}")
    sys.exit(0)

# Question 25 — one current-affairs item from the verified CA pool (Apr-Sep 2026).
pool_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ca_mock_pool.json")
if not os.path.exists(pool_path):
    raise SystemExit("ca_mock_pool.json not ready yet — run again after the current-affairs agent finishes.")
with open(pool_path, encoding="utf-8") as f:
    pool = json.load(f)
assert isinstance(pool, list) and len(pool) >= 2, "CA pool too small"
for x in pool[:2]:
    validate_question(x, "ca-pool")
ca_q = dict(pool[1])
ca_q["id"] = "t2m-q25"
QS.append(ca_q)

# Final gate: must not duplicate any question already written in the topic files.
seen = all_topic_questions()
for x in QS:
    key = " ".join(x["q"].split()).lower()
    assert key not in seen, f"t2-mock duplicates topic question {seen.get(key)}"

save_mock("t2-mock-1", QS, expected=25)
