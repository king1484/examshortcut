"""Build t1-pyq-2025--ga.json — 25 GA questions mirroring the CGL 2025 Tier 1
GA topic distribution and question formats (statements / assertion-reason /
chronological order / fill-in-the-blanks), with freshly written questions.

Distribution derived from published shift analyses and the actual GA sections
of the 12 Sep 2025 Shift 1 and 13 Sep 2025 Shift 2 papers: art-culture ~4,
polity ~5, science (phy+chem+bio) ~6, geography ~3, economy ~2, history ~3,
static GK ~1, current-affairs/sports ~1.

Run:  py -3 build_t1_pyq_ga.py
"""
import sys

from gacommon import Q, save_mock, validate_question, all_topic_questions

QS = []


def add(*a, **kw):
    QS.append(Q(*a, **kw))


# --- HISTORY (3) -----------------------------------------------------------

# P1 ANCIENT — chronological order (format seen in both analysed shifts)
add("pyq-q01",
    "Arrange the following monuments in chronological order of their construction:\n"
    "(a) Great Stupa at Sanchi\n(b) Kailasa temple at Ellora\n(c) Brihadeeswara Temple at Thanjavur",
    ["b - c - a", "a - c - b", "a - b - c", "c - b - a"], 2,
    "The Sanchi Great Stupa began in the 3rd century BCE under Ashoka (enlarged by the Sungas). The Kailasa temple at Ellora was cut in the 8th century CE by Rashtrakuta king Krishna I. Brihadeeswara was completed in 1010 CE by Rajaraja Chola I. Hence a - b - c.",
    "Age order: Stupa (BCE) → Ellora (700s) → Thanjavur (1000s); 3 → 8 → 11 century anchors.",
    "medium", "ancient-history", "chronological order of monuments", 40)

# P2 MEDIEVAL — fill-in-the-blank battle (format seen in shift 2)
add("pyq-q02",
    "Fill in the blanks:\nThe Battle of Khanwa (1527) was fought between Babur and ____.",
    ["Ibrahim Lodi", "Medini Rai", "Rana Sanga", "Hasan Khan Mewati"], 2,
    "At Khanwa (near Agra) in 1527 Babur defeated Rana Sangram Singh (Sanga) of Mewar, ending Rajput resistance. Ibrahim Lodi was defeated a year earlier at Panipat (1526); Hasan Khan Mewati fought at Khanwa but on Rana Sanga's side.",
    "Panipat→Lodi, Khanwa→Sanga, Chausa/Kannauj→Humayun vs Sher Shah.",
    "easy", "medieval-history", "battle-opponent fill in the blank", 25)

# P3 MODERN — Gandhian movements
add("pyq-q03",
    "Mahatma Gandhi withdrew the Non-Cooperation Movement in February 1922 after the violence at:",
    ["Jallianwala Bagh, Amritsar", "Kakori, Uttar Pradesh", "Bardoli, Gujarat", "Chauri Chaura, Uttar Pradesh"], 3,
    "After a mob set fire to the Chauri Chaura police station (Gorakhpur district) killing 22 policemen on 5 February 1922, Gandhi suspended the Non-Cooperation Movement. Bardoli later gave him the title 'Sardar' (1928, via Vallabhbhai Patel's campaign).",
    "NCM ends at Chauri Chaura; CDM begins at Dandi — 'C starts it... C stops it'.",
    "easy", "modern-history", "movement-cause pairing", 25)

# --- ART & CULTURE (4) -----------------------------------------------------

# P4 ART — instruments & regional traditions
add("pyq-q04",
    "The santoor, popularised in Hindustani classical music by Pandit Shivkumar Sharma, was originally used in the 'Sufiana Mausiqi' music tradition of which region?",
    ["Bengal", "Kashmir", "Rajasthan", "Kerala"], 1,
    "The 100-stringed santoor was the accompaniment of Sufiana Mausiqi, the classical music of Kashmir, before Shivkumar Sharma adapted it for Hindustani recitals.",
    "Santoor–Snow–Sufiana–Srinagar: all S, all Kashmir.",
    "medium", "art-culture", "instrument-regional tradition", 30)

# P5 ART — festivals
add("pyq-q05",
    "Bihu, celebrated thrice a year with the Rongali Bihu marking the Assamese New Year, is the principal festival of which state?",
    ["Assam", "West Bengal", "Odisha", "Manipur"], 0,
    "Bihu is Assam's state festival — Bohag (Rongali) Bihu in April for the Assamese New Year, Kati (Kongali) Bihu in October and Magh (Bhogali) Bihu in January.",
    "Three Bihus = Assam's three seasons; Rongali = Rong (colour) = New Year.",
    "easy", "art-culture", "festival-state", 20)

# P6 ART — painting styles
add("pyq-q06",
    "The Warli painting style, executed with white rice-paste figures on mud walls, belongs to which state?",
    ["Gujarat", "Bihar", "Maharashtra", "West Bengal"], 2,
    "Warli art is the tribal art of the Warli community of north Maharashtra (Palghar belt). Madhubani belongs to Bihar and Pattachitra to Odisha/West Bengal.",
    "Warli–Worli (Mumbai sea-face) → Maharashtra.",
    "easy", "art-culture", "painting style-state", 20)

# P7 ART — temple architecture (mirrors cave-architecture question format)
add("pyq-q07",
    "The famous rock-cut Kailasa temple (Cave 16) at Ellora was carved during the reign of which dynasty?",
    ["Rashtrakuta", "Chalukya", "Pallava", "Yadava"], 0,
    "Krishna I of the Rashtrakuta dynasty had the Kailasa temple cut out of a single rock in the 8th century CE. The Pallavas built the ratha temples of Mahabalipuram; Badami Chalukyas excelled at Aihole-Pattadakal.",
    "Ellora = E for Eight century = Rashtrakuta Krishna I.",
    "medium", "art-culture", "monument-dynasty", 30)

# --- POLITY (5) ------------------------------------------------------------

# P8 POLITY — Article–subject
add("pyq-q08",
    "Freedom to move freely throughout the territory of India is guaranteed to citizens under which of the following?",
    ["Article 19(1)(d)", "Article 21", "Article 22", "Article 25"], 0,
    "Article 19(1)(d) gives citizens the right to move freely and 19(1)(e) to reside anywhere in India. Article 21 protects life and personal liberty, Article 22 safeguards against arrest and Article 25 gives freedom of religion.",
    "19's six freedoms: speech, assemble, association, move, reside, profession — MAP-RRP order gives d = move.",
    "easy", "polity", "Article-subject", 20)

# P9 POLITY — amendments
add("pyq-q09",
    "The voting age in elections to the Lok Sabha and State Legislative Assemblies was reduced from 21 to 18 years by which Constitutional Amendment?",
    ["61st Amendment Act, 1988", "42nd Amendment Act, 1976", "52nd Amendment Act, 1985", "73rd Amendment Act, 1992"], 0,
    "The 61st Constitutional Amendment Act, 1988 lowered the voting age to 18 by amending Article 326, effective from 1989. The 52nd added the Tenth Schedule (anti-defection) and the 73rd inserted Part IX on Panchayati Raj.",
    "Six-One = 'so young' can vote now.",
    "easy", "polity", "amendment-purpose", 20)

# P10 POLITY — statement-based (dominant format of CGL 2025 GA)
add("pyq-q10",
    "Consider the following statements regarding the Rajya Sabha:\n"
    "1. Like the Lok Sabha, it can be dissolved before the completion of its term.\n"
    "2. A Money Bill can be introduced only in the Lok Sabha.\n"
    "3. Its maximum sanctioned strength is 250 members.\n"
    "Which of the statements given above is/are correct?",
    ["Only 1", "Only 2", "2 and 3 only", "1, 2 and 3"], 2,
    "The Rajya Sabha is a permanent House — one-third of members retire every two years and it is never dissolved, so statement 1 is wrong. Money Bills (Article 110) originate only in the Lok Sabha, and the Rajya Sabha's maximum strength is 250 (238 elected + 12 nominated). Hence 2 and 3 are correct.",
    "RS = 'Rests forever' — never dissolved. Trap options usually carry 'dissolved'.",
    "medium", "polity", "statement-based Parliament", 35)

# P11 POLITY — constitutional bodies
add("pyq-q11",
    "Under which Article of the Constitution is the Comptroller and Auditor-General of India appointed?",
    ["Article 76", "Article 148", "Article 280", "Article 315"], 1,
    "Article 148 provides for the CAG, who is appointed by the President and can be removed like a Supreme Court judge. Article 76 deals with the Attorney-General, 280 with the Finance Commission and 315 with UPSC and State PSCs.",
    "148: 'one-four-eight — the Auditor watches all three: union, states, accounts'.",
    "medium", "polity", "constitutional body-Article", 25)

# P12 POLITY — Preamble amendments
add("pyq-q12",
    "The words 'Socialist', 'Secular' and 'Integrity' were inserted into the Preamble by which amendment?",
    ["24th Amendment", "44th Amendment", "42nd Amendment", "52nd Amendment"], 2,
    "The 42nd Amendment Act, 1976 (the 'Mini-Constitution') added the three words to the Preamble, restricted judicial review and moved five subjects (including education) to the Concurrent List. The 44th Amendment later softened some 42nd changes, removing 'internal disturbance' as a ground for emergency.",
    "42 = the all-rounder: Preamble words, Fundamental Duties, education shift.",
    "easy", "polity", "amendment-purpose", 20)

# --- SCIENCE (6) -----------------------------------------------------------

# P13 PHYSICS — optics (mirrors the light question asked in shift 2)
add("pyq-q13",
    "When a ray of light travels from air into a glass slab, which property of the light remains unchanged?",
    ["Speed", "Frequency", "Wavelength", "Direction"], 1,
    "On entering a denser medium the speed falls (v = c/n) and wavelength shortens, but frequency depends only on the source and stays constant. The ray also bends towards the normal, so direction changes.",
    "Source fixes frequency: medium can only change speed and wavelength.",
    "medium", "physics", "refraction invariant", 30)

# P14 PHYSICS — laws of motion
add("pyq-q14",
    "According to Newton's second law of motion, the rate of change of momentum of a body is equal to:",
    ["the work done on it", "the power developed", "the impulse applied", "the external force applied"], 3,
    "Newton's second law gives F = dp/dt = ma — the applied external force equals the rate of change of momentum. Impulse is the change of momentum itself (F x t), not its rate.",
    "Second law = Force. First = inertia, third = action-reaction.",
    "easy", "physics", "laws of motion", 20)

# P15 CHEMISTRY — common names (plaster of Paris asked across shifts)
add("pyq-q15",
    "Plaster of Paris, used for plastering fractured bones, is chemically:",
    ["Calcium sulphate dihydrate", "Calcium sulphate hemihydrate", "Calcium carbonate", "Calcium hydroxide"], 1,
    "Plaster of Paris is calcium sulphate hemihydrate (CaSO4.1/2 H2O), obtained by heating gypsum (calcium sulphate dihydrate) to about 373 K. Lime water is calcium hydroxide and limestone is calcium carbonate.",
    "POP is gypsum 'minus' water: dihydrate - 1.5 H2O = hemihydrate.",
    "medium", "chemistry", "common name-chemical composition", 30)

# P16 CHEMISTRY — acids
add("pyq-q16",
    "Which acid is responsible for the stinging pain of an ant bite?",
    ["Acetic acid", "Lactic acid", "Citric acid", "Formic acid"], 3,
    "Ants inject formic acid (methanoic acid) when they sting, so applying a mild base like baking soda neutralises it. Lactic acid curdles milk and citric acid is found in citrus fruits.",
    "Formica = Latin for ant → formic acid.",
    "easy", "chemistry", "acid-natural source", 20)

# P17 BIOLOGY — cell organelles
add("pyq-q17",
    "Which cell organelle is called the 'suicidal bag' of the cell?",
    ["Ribosome", "Mitochondrion", "Golgi apparatus", "Lysosome"], 3,
    "Lysosomes contain hydrolytic enzymes; if they burst, the cell digests itself — hence 'suicidal bags'. Mitochondria are the powerhouse, ribosomes build proteins and the Golgi body packages them.",
    "Lysosome–Lethal liquids → suicidal bag.",
    "easy", "biology", "organelle-function", 20)

# P18 BIOLOGY — blood groups
add("pyq-q18",
    "Persons with which blood group are regarded as universal recipients?",
    ["AB", "O", "A", "B"], 0,
    "AB blood group persons have both A and B antigens but no antibodies, so they can receive blood of any group — universal recipients. Group O (negative) is the universal donor.",
    "Recipient-AB: 'AB = A-l-l Blood accepted'.",
    "easy", "biology", "blood group facts", 20)

# --- GEOGRAPHY (3) ---------------------------------------------------------

# P19 INDIAN GEOGRAPHY — statement-based (format seen in shifts)
add("pyq-q19",
    "Consider the following statements about the Deccan Plateau:\n"
    "1. It is largely composed of basaltic lava flows.\n"
    "2. It slopes generally from west to east.\n"
    "Which of the statements given above is/are correct?",
    ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"], 2,
    "The Deccan Trap was formed by Cretaceous-era lava flows of basalt, and the plateau tilts eastward — most rivers (Godavari, Krishna, Kaveri) flow east into the Bay of Bengal. Hence both are correct. (The Narmada and Tapi are west-flowing rift-valley exceptions.)",
    "Deccan = Done by lava, Drains eastwards — D-D-E.",
    "medium", "indian-geography", "statement-based physiography", 35)

# P20 INDIAN GEOGRAPHY — national parks
add("pyq-q20",
    "Kaziranga National Park, a UNESCO World Heritage Site on the Brahmaputra floodplains, is famous primarily for:",
    ["the one-horned rhinoceros", "the Asiatic lion", "the wild ass", "the Great Indian bustard"], 0,
    "Kaziranga (Assam) hosts about two-thirds of the world's one-horned rhinos. Asiatic lions live in Gir (Gujarat), the wild ass in the Rann of Kachchh and the Great Indian bustard in Rajasthan grasslands.",
    "K for Kaziranga–K for Kala (black) horn of the rhino; Gir–G for Ghads of lions.",
    "easy", "indian-geography", "national park-species", 20)

# P21 WORLD GEOGRAPHY — local winds
add("pyq-q21",
    "The warm, dry local wind 'Chinook', which melts snow on the eastern slopes and is called the 'snow-eater', blows in which region?",
    ["The Alps", "The Andes", "The Rocky Mountains of North America", "The Sahara Desert"], 2,
    "Chinook descends the eastern slopes of the Rocky Mountains, raising temperatures of the prairies ('snow-eater'). Its Alpine counterpart is the Foehn and its Argentine counterpart is the Zonda.",
    "Chinook–Canada/Colorado–Rockies; Alps get the Foehn.",
    "medium", "world-geography", "local wind-region", 30)

# --- ECONOMY (2) -----------------------------------------------------------

# P22 ECONOMY — GST (mirrors the GST Council question format of shift 2)
add("pyq-q22",
    "The Goods and Services Tax (GST) came into force across India with effect from:",
    ["1 April 2017", "1 July 2017", "1 April 2018", "8 November 2016"], 1,
    "GST, introduced by the 101st Constitutional Amendment Act, 2016, was rolled out on 1 July 2017 through the CGST, SGST, IGST and UTGST Acts. The GST Council is constituted under Article 279A.",
    "101st Amendment → 1 July 2017 ('one-oh-one → first of July').",
    "easy", "economy", "reform-launch date", 20)

# P23 ECONOMY — Five Year Plans
add("pyq-q23",
    "The slogan 'Garibi Hatao' is associated with which Five Year Plan?",
    ["Third Five Year Plan", "Fourth Five Year Plan", "Fifth Five Year Plan", "Second Five Year Plan"], 1,
    "'Garibi Hatao' was Congress's 1971 election slogan and guided the Fourth Plan (1969-74), which aimed at growth with stability and reducing poverty. The Fifth Plan (1974-78) then targeted 'Garibi Hatao' formally through poverty-removal programmes.",
    "Fourth Plan = 'Four the Poor' — growth with social justice.",
    "medium", "economy", "plan-slogan-target", 30)

# --- STATIC GK + CURRENT AFFAIRS (2) --------------------------------------

# P24 STATIC GK — important days
add("pyq-q24",
    "World Environment Day, established after the 1972 Stockholm Conference, is observed every year on:",
    ["22 April", "21 March", "16 September", "5 June"], 3,
    "World Environment Day is observed on 5 June. 22 April is Earth Day, 21 March is World Forestry Day and 16 September is the International Day for the Preservation of the Ozone Layer.",
    "5 June 1972 = UNEP's birthday; the first WED was held in 1974.",
    "easy", "static-gk", "important days", 20)

# P25 CURRENT AFFAIRS — sports (settled 2025 fact of the type asked in Sep 2025 shifts)
add("pyq-q25",
    "Which team did India defeat in the final to win the ICC Champions Trophy 2025?",
    ["Australia", "New Zealand", "South Africa", "England"], 1,
    "India beat New Zealand by 4 wickets in the final at the Dubai International Cricket Stadium on 9 March 2025 (Rohit Sharma 76, Player of the Match), lifting a record third Champions Trophy after 2002 and 2013.",
    "CT 2025: unbeaten India, Dubai final, NZ opposition — remember '3rd title'.",
    "easy", "current-affairs", "sports tournament winner", 25)

# --- validate & save --------------------------------------------------------
for x in QS:
    validate_question(x, "t1-pyq-2025")
seen = all_topic_questions()
for x in QS:
    key = " ".join(x["q"].split()).lower()
    assert key not in seen, f"t1-pyq-2025 duplicates topic question {seen.get(key)}"
ans = [x["answer"] for x in QS]
print(f"answer spread {[ans.count(i) for i in range(4)]}")
save_mock("t1-pyq-2025", QS, expected=25)
