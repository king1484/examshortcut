"""Build t1-mock-1--ga.json — 25 GA questions for Tier 1 full mock.
Run:  py -3 build_t1_mock_ga.py          (needs ca_mock_pool.json from CA agent)
      py -3 build_t1_mock_ga.py --dry    (structural check only, 24 Qs)
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


# 1 ANCIENT — Harappan site-river
add("t1m-q01",
    "Mohenjodaro, one of the most important sites of the Indus Valley Civilisation, is situated on the bank of which river?",
    ["Ravi", "Indus", "Ghaggar", "Bhogava"], 1,
    "Mohenjodaro (Sindh, Pakistan) lies on the right bank of the Indus. Harappa is on the Ravi, Kalibangan on the dried Ghaggar and Lothal on the Bhogava (a tributary of the Sabarmati).",
    "R for Ravi–Harappa, I for Indus–Mohenjodaro: pair the initial letters.",
    "easy", "ancient-history", "Harappan site-river matching", 20)

# 2 MEDIEVAL — Delhi Sultanate dynasties
add("t1m-q02",
    "Who among the following founded the Sayyid dynasty of the Delhi Sultanate?",
    ["Khizr Khan", "Bahlol Lodi", "Nizam Shah", "Ibrahim Shah"], 0,
    "Khizr Khan (1414–1421) founded the Sayyid dynasty after the fall of the Tughlaqs. Bahlol Lodi founded the Lodi dynasty (1451); Nizam Shah founded the Nizam Shahi dynasty of Ahmadnagar; Ibrahim Shah ruled the Sharqi kingdom of Jaunpur.",
    "Sayyid–Khizr: both end in a soft sound — 'Sayyid K(h)an'.",
    "medium", "medieval-history", "dynasty-founder matching", 25)

# 3 MODERN — pre-INC organisations
add("t1m-q03",
    "The Indian Association, a precursor of the Indian National Congress, was founded in 1876 by:",
    ["Womesh Chandra Bonnerjee", "A.O. Hume", "Surendranath Banerjee and Anand Mohan Bose", "Dadabhai Naoroji"], 2,
    "The Indian Association (1876, Calcutta) was founded by Surendranath Banerjee and Anand Mohan Bose. A.O. Hume founded the INC in 1885; W.C. Bonnerjee was its first president; Dadabhai Naoroji founded the East India Association (1866, London).",
    "1876–'SB-AMB' (Surendranath–Anand Mohan Bose); 1885–Hume.",
    "medium", "modern-history", "organisation-founder-year matching", 30)

# 4 MODERN — Governors-General
add("t1m-q04",
    "The 'Doctrine of Lapse', under which adopted heirs of princely states were denied the throne, was applied by which Governor-General?",
    ["Lord William Bentinck", "Lord Canning", "Lord Ripon", "Lord Dalhousie"], 3,
    "Lord Dalhousie (1848–1856) used the Doctrine of Lapse to annex Satara, Jaitpur, Sambalpur, Udaipur, Jhansi and Nagpur. Bentinck is known for social reforms (abolition of sati), Canning for the 1857 aftermath (Queen's Proclamation) and Ripon as the 'father of local self-government'.",
    "Dalhousie = 'Douglas Lapse' — remember D-D.",
    "easy", "modern-history", "Governor-General–key event", 20)

# 5 ART — classical dances
add("t1m-q05",
    "Sattriya, one of the eight classical dance forms of India recognised by the Sangeet Natak Akademi, belongs to which state?",
    ["Assam", "Odisha", "Manipur", "Kerala"], 0,
    "Sattriya was created in the 15th century by the Vaishnavite saint Sankaradeva and is preserved in the monasteries (satras) of Assam. Odissi belongs to Odisha, Manipuri to Manipur and Kathakali/Mohiniyattam to Kerala.",
    "Sattriya–Satra–Assam: satras are Assam's Vaishnavite monasteries.",
    "easy", "art-culture", "classical dance-state matching", 20)

# 6 ART — instruments & maestros
add("t1m-q06",
    "Ustad Amjad Ali Khan, a Padma Vibhushan awardee, is internationally renowned as an exponent of which musical instrument?",
    ["Sitar", "Sarod", "Santoor", "Sarangi"], 1,
    "Amjad Ali Khan is the best-known exponent of the sarod. Ravi Shankar and Vilayat Khan are linked with the sitar, Shivkumar Sharma with the santoor and Ram Narayan with the sarangi.",
    "A-A pair: Amjad Ali–Archtop sarod (the only one of the four without strings plucked by a mizrab on a guitar-like body).",
    "easy", "art-culture", "instrument-maestro matching", 20)

# 7 ART — UNESCO intangible heritage
add("t1m-q07",
    "Kalbelia, the snake-charmer community dance inscribed on UNESCO's Intangible Cultural Heritage list in 2010, is performed in which state?",
    ["Gujarat", "Haryana", "Madhya Pradesh", "Rajasthan"], 3,
    "Kalbelia of Rajasthan entered the UNESCO ICH list in 2010, the same year as Chhau and Mudiyettu. Ghoomar and Terah Taali are other Rajasthani folk forms.",
    "Kalbelia–Kesariya (saffron skirts of the desert)–Rajasthan.",
    "medium", "art-culture", "folk dance-state / UNESCO ICH", 25)

# 8 POLITY — Fundamental Rights articles
add("t1m-q08",
    "Which Article of the Indian Constitution abolishes untouchability and forbids its practice in any form?",
    ["Article 14", "Article 15", "Article 17", "Article 19"], 2,
    "Article 17 abolishes untouchability; Article 18 abolishes titles. Article 14 gives equality before law, Article 15 prohibits discrimination and Article 19 grants the six freedoms.",
    "17 and 18 — both 'abolition' articles sit side by side (17-untouchability, 18-titles).",
    "easy", "polity", "Article–subject", 20)

# 9 POLITY — emergency provisions
add("t1m-q09",
    "Under which Article of the Constitution can the President proclaim a National Emergency on grounds of war, external aggression or armed rebellion?",
    ["Article 352", "Article 356", "Article 360", "Article 365"], 0,
    "Article 352 covers National Emergency ('armed rebellion' replaced 'internal disturbance' through the 44th Amendment, 1978). Article 356 covers President's Rule in a state, Article 360 covers Financial Emergency and Article 365 lets the Centre treat a state's failure to follow its directions as a breakdown of constitutional machinery.",
    "Emergency trio in ascending order: 352 National → 356 State → 360 Financial ('2-6-0').",
    "easy", "polity", "Article-emergency type", 20)

# 10 POLITY — executive procedure
add("t1m-q10",
    "Who administers the oath of office and secrecy to the President of India?",
    ["Prime Minister", "Vice-President", "Chief Justice of India", "Speaker of the Lok Sabha"], 2,
    "Under Article 60 the Chief Justice of India (or the senior-most available Supreme Court judge) administers the President's oath. The President in turn administers oaths to the Governor and ministers.",
    "The chain: CJI → President → Governors/Ministers. Remember 'Crown is crowned'.",
    "easy", "polity", "constitutional procedure", 20)

# 11 POLITY — Schedules
add("t1m-q11",
    "Which Schedule of the Constitution provides for the administration of tribal areas in Assam, Meghalaya, Tripura and Mizoram?",
    ["Fifth Schedule", "Sixth Schedule", "Ninth Schedule", "Tenth Schedule"], 1,
    "The Sixth Schedule (Articles 244(2), 275(1)) covers the north-eastern tribal areas of Assam, Meghalaya, Tripura and Mizoram through Autonomous District Councils. The Fifth Schedule covers scheduled areas in other states; Ninth Schedule protects land-reform laws; Tenth Schedule deals with anti-defection.",
    "Sixth = 'six north-east sisters' — AMTM (Assam, Meghalaya, Tripura, Mizoram).",
    "medium", "polity", "Schedule–content", 25)

# 12 INDIAN GEOGRAPHY — river nicknames
add("t1m-q12",
    "Which river is notorious as the 'Sorrow of Bihar' because of its frequent devastating floods?",
    ["Kosi", "Gandak", "Son", "Damodar"], 0,
    "The Kosi, a tributary of the Ganga shifting its course frequently, is the Sorrow of Bihar. The Damodar was once called the Sorrow of Bengal (now tamed by dams), and the Son is a major right-bank Ganga tributary.",
    "K for Kosi–K for Karo (weep) in Bihar; Damodar–Dukh of Bengal.",
    "easy", "indian-geography", "river-nickname", 20)

# 13 INDIAN GEOGRAPHY — waterfalls
add("t1m-q13",
    "The Jog Falls (Gerusoppe Falls), one of the highest plunge waterfalls of India, is formed on which river?",
    ["Kaveri", "Krishna", "Sharavathi", "Netravati"], 2,
    "Jog Falls in Karnataka's Shivamogga district is created by the west-flowing Sharavathi river (fall of about 253 m). Shivasamudram falls are on the Kaveri.",
    "Jog–Jharana in the jungle of Sharavathi (both start with S/J sounds alternately).",
    "medium", "indian-geography", "waterfall-river", 25)

# 14 WORLD GEOGRAPHY — deserts
add("t1m-q14",
    "The Atacama Desert, regarded as the driest hot desert of the world, lies mainly in which country?",
    ["Peru", "Chile", "Argentina", "Bolivia"], 1,
    "The Atacama stretches along northern Chile between the Pacific and the Andes; parts of it have had no measurable rainfall for decades. Sechura lies in Peru and Patagonia in Argentina.",
    "Atacama–Andes–Chile coast: A-A-C.",
    "easy", "world-geography", "desert-country superlatives", 20)

# 15 ECONOMY — acts
add("t1m-q15",
    "The Fiscal Responsibility and Budget Management (FRBM) Act, which set targets for fiscal deficit and debt reduction, was enacted in:",
    ["1991", "2000", "2003", "2005"], 2,
    "The FRBM Act was passed in 2003 and came into force from 2004-05, requiring the Centre to place fiscal policy statements before Parliament. The 1991 year is remembered for liberalisation, not FRBM.",
    "FRBM–2003: F=4th letter... simpler: FRBM came 'three years after 2000'.",
    "medium", "economy", "act-enactment year", 25)

# 16 ECONOMY — institutions
add("t1m-q16",
    "The Reserve Bank of India was established in which year, on the recommendation of the Hilton Young Commission?",
    ["1947", "1949", "1969", "1935"], 3,
    "The RBI began operations on 1 April 1935 under the RBI Act, 1934, following the Hilton Young (Royal) Commission. It was nationalised on 1 January 1949; 1969 is the year 14 commercial banks were nationalised.",
    "RBI: Act 1934 → started 1935 → nationalised 1949 ('34-35-49').",
    "easy", "economy", "institution-establishment year", 20)

# 17 PHYSICS — SI units
add("t1m-q17",
    "The SI unit of electric charge is named after which scientist?",
    ["Andre-Marie Ampere", "Alessandro Volta", "Charles-Augustin de Coulomb", "Georg Simon Ohm"], 2,
    "Charge is measured in coulomb (C); 1 C = 1 A x 1 s. Ampere (current), volt (potential difference) and ohm (resistance) are other electrical units named after scientists.",
    "Charge-Coulomb: both start with 'C'.",
    "easy", "physics", "SI unit-scientist", 20)

# 18 PHYSICS — optics in nature
add("t1m-q18",
    "The blue colour of the sky during daytime is due to which optical phenomenon?",
    ["Reflection of light", "Refraction of light", "Dispersion of light", "Scattering of light"], 3,
    "Air molecules scatter shorter (blue) wavelengths far more than longer ones (Rayleigh scattering), so the sky looks blue. At sunrise/sunset light travels a longer path, blue is scattered away and red dominates. Dispersion explains the rainbow, not the sky's colour.",
    "Sky–Scatter (S-S); Rainbow–Dispersion (R-D).",
    "easy", "physics", "everyday physics phenomenon", 20)

# 19 CHEMISTRY — common names
add("t1m-q19",
    "The chemical name of baking soda, used as an antacid and in baking, is:",
    ["Sodium bicarbonate", "Sodium carbonate", "Calcium carbonate", "Sodium hydroxide"], 0,
    "Baking soda is sodium bicarbonate (sodium hydrogencarbonate, NaHCO3). Sodium carbonate is washing soda, calcium carbonate is limestone/marble and sodium hydroxide is caustic soda.",
    "Baking–Bicarbonate: the double-B pair; Washing–(sodium) carbonate.",
    "easy", "chemistry", "common name-chemical formula", 20)

# 20 CHEMISTRY — gases
add("t1m-q20",
    "Which oxide of nitrogen, used as the first anaesthetic, is popularly known as 'laughing gas'?",
    ["Nitric oxide (NO)", "Nitrogen dioxide (NO2)", "Nitrous oxide (N2O)", "Nitrogen pentoxide (N2O5)"], 2,
    "Nitrous oxide (N2O), called laughing gas for the euphoria it produces, was the first gas used as a dental anaesthetic. Nitric oxide and nitrogen dioxide are air pollutants, not anaesthetics.",
    "Laugh = laughter's 'laughing + oxide': N2O has 2 N's like 'ha-ha' (two laughs).",
    "easy", "chemistry", "gas-common name", 20)

# 21 BIOLOGY — vitamins
add("t1m-q21",
    "Deficiency of which vitamin causes scurvy, marked by bleeding gums and slow wound healing?",
    ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], 2,
    "Scurvy is caused by deficiency of vitamin C (ascorbic acid — literally 'anti-scurvy acid'), found in citrus fruits and amla. Vitamin D deficiency causes rickets and vitamin B12 deficiency causes pernicious anaemia.",
    "Ascorbic = anti-scorvy = anti-scurvy → Vitamin C.",
    "easy", "biology", "vitamin-deficiency disease", 20)

# 22 BIOLOGY — human body superlatives
add("t1m-q22",
    "Which is the largest gland as well as the largest internal organ of the human body?",
    ["Pancreas", "Liver", "Thyroid", "Pituitary"], 1,
    "The liver is the largest gland and the largest internal organ (about 1.5 kg). The pancreas is both endocrine and exocrine but second in size; the thyroid is the largest endocrine gland; the pituitary is the smallest endocrine gland, called the master gland.",
    "Liver = Large (both L).",
    "easy", "biology", "largest-smallest organ facts", 20)

# 23 STATIC GK — books & authors
add("t1m-q23",
    "Who is the author of the autobiography 'Wings of Fire'?",
    ["A.P.J. Abdul Kalam", "Khushwant Singh", "R.K. Narayan", "Vikram Seth"], 0,
    "'Wings of Fire' (1999) is the autobiography of Dr A.P.J. Abdul Kalam, co-written with Arun Tiwari. Khushwant Singh wrote 'Train to Pakistan' and R.K. Narayan created the fictional town of Malgudi.",
    "Kalam the 'Missile Man' — wings of fire = missiles need fire.",
    "easy", "static-gk", "book-author", 20)

# 24 STATIC GK — trophies
add("t1m-q24",
    "The Durand Cup, Asia's oldest football tournament, is associated with which sport?",
    ["Hockey", "Football", "Cricket", "Badminton"], 1,
    "The Durand Cup (started 1888 at Shimla by Sir Mortimer Durand) is Asia's oldest football tournament. Hockey trophies include the Aga Khan Cup and Beighton Cup; badminton has Thomas and Uber Cups.",
    "Durand–Dribbling (football); Aga Khan–Aisa stick (hockey).",
    "easy", "static-gk", "trophy-sport", 20)

if DRY:
    for x in sp:
        validate_question(x, "t1-mock-1")
    stems = {x["q"].strip().lower() for x in sp}
    assert len(stems) == len(sp)
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
ca_q = dict(pool[0])
ca_q["id"] = "t1m-q25"
QS.append(ca_q)

# Final gate: must not duplicate any question already written in the topic files.
seen = all_topic_questions()
for x in QS:
    key = " ".join(x["q"].split()).lower()
    assert key not in seen, f"t1-mock duplicates topic question {seen.get(key)}"

save_mock("t1-mock-1", QS, expected=25)
