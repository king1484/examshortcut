"""indian-geography deep content - part 1: ig-location, ig-physiography, ig-rivers."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub
from ig_notes import NOTES


def build_location():
    S = Sub("ig-location")
    S.notes = NOTES["ig-location"].strip()
    S.pattern("ga-il-p1", "States on the Tropic of Cancer / Standard Meridian", "very common",
        "'Which state does NOT lie on the Tropic of Cancer?', 'The Standard Meridian passes through…', or a list of states to check.",
        None,
        "1. Tropic of Cancer (23.5°N), west to east: **Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram** (8 states).\n2. Standard Meridian (82°30'E) crosses **UP, MP, Chhattisgarh, Odisha, Andhra Pradesh** (5 states); reference town Mirzapur.\n3. In a NOT-question, strike every state from the list; the one left is the answer. Traps: Odisha, Bihar and UP are not on the Tropic; Jharkhand is not on the Meridian.",
        "The Standard Meridian of India does NOT pass through which state?\n(a) Uttar Pradesh (b) Chhattisgarh (c) Odisha (d) Jharkhand",
        "(d) **Jharkhand**. The 82°30'E line crosses UP, MP, Chhattisgarh, Odisha and Andhra Pradesh; Jharkhand lies just east of it.")
    S.pattern("ga-il-p2", "Neighbours: border length and states touching each country", "very common",
        "'Longest/shortest border…', 'Which state does NOT border Nepal/Myanmar?', 'Mizoram shares borders with…'.",
        None,
        "1. Border order (MHA): Bangladesh > China > Pakistan > Nepal > Myanmar > Bhutan > Afghanistan.\n2. Keep the state lists: Nepal (Uttarakhand, UP, Bihar, WB, Sikkim), Bhutan (Sikkim, WB, Assam, Arunachal), Myanmar (Arunachal, Nagaland, Manipur, Mizoram), Bangladesh (WB, Assam, Meghalaya, Tripura, Mizoram).\n3. Tick each option against the list; a state missing from the list is the odd one.",
        "Which neighbouring country shares the shortest land border with India?",
        "**Afghanistan** - about 106 km, touching Ladakh (as per India's official map). The longest is with Bangladesh (4,096.7 km).")
    S.pattern("ga-il-p3", "Channels, straits and island groups", "very common",
        "A channel, strait or passage is named and the two land areas it separates are asked, or an island fact (volcano, coral, capital).",
        None,
        "1. Arabian Sea side: **Nine Degree** = Minicoy | main Lakshadweep; **Eight Degree** = Minicoy | Maldives.\n2. Bay of Bengal side: **Ten Degree** = Andaman | Nicobar; **Duncan Passage** = South Andaman | Little Andaman; **Coco Channel** = North Andaman | Coco Islands (Myanmar); **Great Channel** = Great Nicobar | Sumatra.\n3. Palk Strait and Gulf of Mannar separate India from Sri Lanka.",
        "The Eight Degree Channel separates:",
        "**Minicoy (India) from the Maldives.** The Nine Degree Channel lies further north, between Minicoy and the rest of Lakshadweep.")
    S.pattern("ga-il-p4", "Extreme points and size superlatives", "common",
        "'Southernmost point of India', 'largest/smallest state by area', 'India's share of the world's land'.",
        None,
        "1. Extremes: Indira Col (north), Indira Point in Great Nicobar (south), Kanyakumari (mainland south tip).\n2. Size: 32.87 lakh sq km, 2.4% of world land, 7th largest country.\n3. States: Rajasthan largest, MP second, Goa smallest.",
        "Which is the largest state of India by area?",
        "**Rajasthan** (about 3.42 lakh sq km). Madhya Pradesh is second; Goa is the smallest.")
    S.pattern("ga-il-p5", "Latitude-longitude extent and time difference", "occasional",
        "Questions on India's lat/long extent, why IST is GMT + 5:30, or the time gap between the east and west ends.",
        "1^{\\circ}\\text{ of longitude} = 4\\text{ minutes of time}",
        "1. The Earth turns 360° in 24 hours, so **1° = 4 minutes**.\n2. IST: 82.5° x 4 = 330 minutes = **5 h 30 min ahead of GMT**.\n3. East-west spread of India is about 29°, so the Sun rises about 2 hours earlier in Arunachal than in Gujarat.",
        "Why is Indian Standard Time 5 h 30 min ahead of GMT?",
        "Because the Standard Meridian is 82°30'E. 82.5 x 4 min = 330 min = **5 h 30 min**.")

    S.q("ga-il-p1", "easy", "Which of the following states does NOT lie on the Tropic of Cancer?",
        ["Jharkhand", "Tripura", "Mizoram", "Bihar"], "Bihar",
        "The Tropic of Cancer passes through Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura and Mizoram. **Bihar** lies wholly north of it.",
        "Odisha, Bihar and UP are the usual 'NOT on the Tropic' answers.", 20)
    S.q("ga-il-p1", "medium", "India's Standard Meridian (82°30'E) passes close to which town?",
        ["Prayagraj", "Mirzapur", "Jabalpur", "Nagpur"], "Mirzapur",
        "The Standard Meridian passes near **Mirzapur** in Uttar Pradesh. Prayagraj lies slightly west of it (about 81.8°E).",
        "Meridian = Mirzapur (both start with M).", 20)
    S.q("ga-il-p1", "hard", "Which state lies on BOTH the Tropic of Cancer and the Standard Meridian of India?",
        ["Chhattisgarh", "Odisha", "Jharkhand", "Uttar Pradesh"], "Chhattisgarh",
        "Tropic list: Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, WB, Tripura, Mizoram. Meridian list: UP, MP, Chhattisgarh, Odisha, AP. Common states: **MP and Chhattisgarh** - only Chhattisgarh is in the options.",
        "Intersect the two lists: MP and Chhattisgarh.", 35)
    S.q("ga-il-p2", "easy", "India shares its shortest international land border with:",
        ["Bhutan", "Afghanistan", "Myanmar", "Nepal"], "Afghanistan",
        "The border with **Afghanistan** is about 106 km. Bhutan (699 km) is the second shortest.",
        None, 15)
    S.q("ga-il-p2", "medium", "Which of the following states does NOT share a border with Nepal?",
        ["Uttarakhand", "Bihar", "Sikkim", "Himachal Pradesh"], "Himachal Pradesh",
        "Nepal touches five Indian states: Uttarakhand, Uttar Pradesh, Bihar, West Bengal and Sikkim. **Himachal Pradesh** borders China (Tibet), not Nepal.",
        "Nepal's five: U-U-B-W-S.", 25)
    S.q("ga-il-p2", "medium", "Which of these states does NOT share a border with Myanmar?",
        ["Nagaland", "Manipur", "Tripura", "Mizoram"], "Tripura",
        "Myanmar touches **Arunachal Pradesh, Nagaland, Manipur and Mizoram**. **Tripura** is bordered on three sides by Bangladesh.",
        None, 25)
    S.q("ga-il-p2", "medium", "Mizoram shares international borders with which two countries?",
        ["Myanmar and Bangladesh", "Myanmar and China", "Bangladesh and Bhutan", "Bhutan and China"], "Myanmar and Bangladesh",
        "Mizoram lies between **Myanmar** (east and south) and **Bangladesh** (west). It is on both the Bangladesh list and the Myanmar list of states.",
        None, 25)
    S.q("ga-il-p3", "medium", "The Nine Degree Channel separates:",
        ["Andaman from Nicobar", "Minicoy from the Maldives", "Minicoy from the main Lakshadweep islands", "Great Nicobar from Sumatra"],
        "Minicoy from the main Lakshadweep islands",
        "The **Nine Degree Channel** lies between Minicoy and the rest of Lakshadweep. Ten Degree = Andaman | Nicobar; Eight Degree = Minicoy | Maldives; Great Channel = Great Nicobar | Sumatra.",
        "Numbers fall as you go south: 10 (Bay side), then 9 and 8 on the Arabian Sea side.", 25)
    S.q("ga-il-p3", "easy", "The Palk Strait separates India from:",
        ["Sri Lanka", "Maldives", "Myanmar", "Indonesia"], "Sri Lanka",
        "The **Palk Strait** lies between Tamil Nadu and northern **Sri Lanka**; the Gulf of Mannar lies to its south, with Adam's Bridge (Ram Setu) between them.",
        None, 15)
    S.q("ga-il-p3", "hard", "The Duncan Passage lies between:",
        ["North Andaman and Coco Islands", "South Andaman and Little Andaman", "Little Andaman and Car Nicobar", "Great Nicobar and Sumatra"],
        "South Andaman and Little Andaman",
        "**Duncan Passage** separates **South Andaman** from **Little Andaman**. Coco Channel = North Andaman | Coco Islands; Ten Degree Channel = Little Andaman | Car Nicobar; Great Channel = Great Nicobar | Sumatra.",
        None, 30)
    S.q("ga-il-p3", "easy", "The Lakshadweep islands are mainly of which origin?",
        ["Volcanic", "Coral", "Glacial", "Fold mountain peaks"], "Coral",
        "Lakshadweep is made of **coral** atolls in the Arabian Sea. The Andaman and Nicobar Islands, by contrast, are the tops of a submerged mountain chain, with volcanic Barren Island.",
        "Arabian Sea islands = coral; Bay of Bengal islands = mountain tops.", 15)
    S.q("ga-il-p4", "easy", "The southernmost point of the Indian Union is:",
        ["Kanyakumari", "Indira Point", "Rameswaram", "Minicoy"], "Indira Point",
        "**Indira Point** on Great Nicobar Island is the southernmost point of India. **Kanyakumari** is only the southern tip of the mainland.",
        "Union = Indira Point; mainland = Kanyakumari.", 15)
    S.q("ga-il-p4", "easy", "Which is the smallest state of India by area?",
        ["Sikkim", "Tripura", "Goa", "Nagaland"], "Goa",
        "**Goa** (about 3,700 sq km) is the smallest state. Sikkim is the second smallest.",
        None, 15)
    S.q("ga-il-p4", "medium", "India covers roughly what share of the world's total land area?",
        ["2.4%", "4.2%", "7.4%", "17.5%"], "2.4%",
        "India's 32.87 lakh sq km is about **2.4%** of the world's land. The 17.5% figure is India's share of the world's **population** (Census 2011) - a common trap.",
        "Land 2.4%, people about 17.5%.", 20)
    S.q("ga-il-p5", "easy", "Indian Standard Time is ahead of Greenwich Mean Time by:",
        ["4 h 30 min", "5 h 00 min", "5 h 30 min", "6 h 30 min"], "5 h 30 min",
        "IST is based on 82°30'E. At 4 minutes per degree: 82.5 x 4 = 330 min = **5 h 30 min**.",
        "82.5 x 4 = 330.", 15)
    S.q("ga-il-p5", "hard", "India stretches from about 68°7'E to 97°25'E. Roughly how much earlier does the Sun rise in the far east than in the far west?",
        ["About 30 minutes", "About 1 hour", "About 2 hours", "About 3 hours"], "About 2 hours",
        "Longitude gap = 97°25' - 68°7' = 29°18', about 29.3°. Time gap = 29.3 x 4 min, about 117 min - **nearly 2 hours**. This is why one Standard Meridian is needed.",
        "About 30° x 4 min = 120 min.", 35)
    S.q("ga-il-p5", "medium", "The mainland of India extends between which latitudes?",
        ["8°4'N and 37°6'N", "6°4'N and 35°6'N", "8°4'N and 23°30'N", "68°7'N and 97°25'N"], "8°4'N and 37°6'N",
        "Mainland India runs from **8°4'N to 37°6'N**. 68°7' and 97°25' are the **longitude** limits (E), and 6°45'N is Indira Point, which is on an island, not the mainland.",
        None, 25)
    return S


def build_physio():
    S = Sub("ig-physiography")
    S.notes = NOTES["ig-physiography"].strip()
    S.pattern("ga-ip-p1", "Mountain pass ↔ state or route", "very common",
        "A pass name (Nathu La, Zoji La, Shipki La, Rohtang, Bhor Ghat) with states or linked places as options.",
        None,
        "1. Group passes by state: Ladakh/J&K (Karakoram, Khardung La, Zoji La, Banihal); Himachal (Rohtang, Baralacha La, Shipki La); Uttarakhand (Lipulekh, Mana, Niti); Sikkim (Nathu La, Jelep La); Arunachal (Bomdi La, Diphu).\n2. Ghats of the Sahyadri: Thal (Mumbai-Nashik), Bhor (Mumbai-Pune), Palghat (Kerala-TN).\n3. Remember the extra fact attached to each (Shipki La - Sutlej enters India; Rohtang - Atal Tunnel; Banihal - Jawahar Tunnel).",
        "Lipulekh Pass, used by pilgrims to Kailash-Mansarovar, is in which state?",
        "**Uttarakhand** (Pithoragarh district), on the India-Tibet border near the Nepal tri-junction.")
    S.pattern("ga-ip-p2", "Peak superlatives ↔ range or state", "very common",
        "'Highest peak of South India / of the Aravallis / entirely within India', or a peak with states as options.",
        None,
        "1. Learn the ladder: K2 (Karakoram) > Kangchenjunga (Sikkim) > Nanda Devi (fully in India, Uttarakhand).\n2. Range tops: Anamudi (Anaimalai, Kerala - South India), Doddabetta (Nilgiris), Guru Shikhar (Aravalli, Mount Abu), Dhupgarh (Satpura), Parasnath (Jharkhand).\n3. Match the word in the stem (range, state, 'entirely within') to the right row.",
        "Anamudi, the highest peak of South India, is in which state?",
        "**Kerala** - in the Anaimalai Hills (2,695 m).")
    S.pattern("ga-ip-p3", "Himalayan ranges, hills and their features", "common",
        "Order of the three ranges, 'Duns lie between…', 'youngest/oldest mountains', or which hills belong to the Purvanchal.",
        None,
        "1. North to south: Himadri (highest) → Himachal (hill stations, Pir Panjal, Dhauladhar) → Shiwalik (lowest, youngest).\n2. Duns = valleys between Himachal and Shiwalik.\n3. Purvanchal = Patkai Bum, Naga, Manipur, Mizo hills. Aravallis = oldest fold mountains of India.",
        "Hill stations like Shimla, Mussoorie and Nainital lie in which Himalayan range?",
        "The **Himachal (Lesser/Middle) Himalaya** - the widest range and home of most hill stations.")
    S.pattern("ga-ip-p4", "Lake superlatives and lake types", "common",
        "'Largest freshwater / brackish / salt lake', 'floating national park lake', 'crater lake', lake ↔ state.",
        None,
        "1. Fresh = Wular (J&K), brackish lagoon = Chilika (Odisha), inland salt = Sambhar (Rajasthan).\n2. Special: Loktak (Manipur, phumdis), Lonar (Maharashtra, meteorite crater), Pulicat (AP-TN lagoon), Kolleru (AP).\n3. Read the adjective in the stem - fresh, brackish or salt - before choosing.",
        "Loktak Lake, famous for its floating vegetation called phumdis, is in:",
        "**Manipur**. The Keibul Lamjao National Park floats on it.")
    S.pattern("ga-ip-p5", "Plateaus, ghats and coastal plains", "common",
        "Questions on the Deccan Trap, Chota Nagpur, Malda gap, Western vs Eastern Ghats, or which coast (Konkan, Malabar, Coromandel) lies where.",
        None,
        "1. West coast north to south: Konkan (Maharashtra-Goa), Kanara (Karnataka), Malabar (Kerala). East coast: Northern Circars (Odisha-AP), Coromandel (Tamil Nadu).\n2. Western Ghats = continuous, high, UNESCO site; Eastern Ghats = low, broken by rivers.\n3. Deccan Trap = basalt lava (black soil); Chota Nagpur = minerals; Malda gap splits Meghalaya plateau from Chota Nagpur.",
        "Which statement is correct?\n1. The Western Ghats are continuous.\n2. The Eastern Ghats are higher than the Western Ghats.",
        "**Only 1.** The Western Ghats are continuous and higher; the Eastern Ghats are lower and cut through by the Mahanadi, Godavari, Krishna and Kaveri.")

    S.q("ga-ip-p1", "easy", "Nathu La Pass, a trade route between India and China, is located in:",
        ["Arunachal Pradesh", "Sikkim", "Himachal Pradesh", "Uttarakhand"], "Sikkim",
        "**Nathu La** is in **Sikkim** on the old silk route to Tibet; border trade through it reopened in 2006. Jelep La is the other famous Sikkim pass.",
        "Sikkim pair: Nathu La + Jelep La.", 15)
    S.q("ga-ip-p1", "medium", "Zoji La Pass connects:",
        ["Manali and Leh", "Srinagar and Leh", "Jammu and Srinagar", "Leh and Nubra Valley"], "Srinagar and Leh",
        "**Zoji La** links the Kashmir valley (Srinagar) with Kargil and **Leh** in Ladakh. Manali-Leh uses Rohtang and Baralacha La; Jammu-Srinagar uses Banihal; Leh-Nubra uses Khardung La.",
        None, 25)
    S.q("ga-ip-p1", "medium", "Through which pass does the Sutlej river enter India?",
        ["Rohtang", "Baralacha La", "Shipki La", "Lipulekh"], "Shipki La",
        "The Sutlej rises near Rakas Tal in Tibet and enters India at **Shipki La** in Kinnaur district, Himachal Pradesh.",
        "Sutlej - Shipki La (both S).", 20)
    S.q("ga-ip-p2", "medium", "Which is the highest peak lying entirely within India?",
        ["Kangchenjunga", "Nanda Devi", "Anamudi", "Kamet"], "Nanda Devi",
        "**Nanda Devi** (7,816 m, Uttarakhand) is the highest peak wholly inside India. Kangchenjunga is on the India-Nepal border; Kamet (Uttarakhand) is lower; Anamudi is the highest of South India.",
        None, 25)
    S.q("ga-ip-p2", "easy", "Guru Shikhar is the highest peak of which range?",
        ["Satpura", "Aravalli", "Vindhya", "Nilgiri"], "Aravalli",
        "**Guru Shikhar** (1,722 m) near Mount Abu, Rajasthan, is the highest point of the **Aravalli** range.",
        None, 15)
    S.q("ga-ip-p2", "hard", "Dhupgarh, near Pachmarhi, is the highest peak of the:",
        ["Satpura Range", "Vindhya Range", "Aravalli Range", "Eastern Ghats"], "Satpura Range",
        "**Dhupgarh** (about 1,350 m) in Madhya Pradesh is the highest point of the **Satpura** range; Pachmarhi is the Satpura hill station.",
        None, 25)
    S.q("ga-ip-p3", "easy", "Which is the southernmost and youngest range of the Himalayas?",
        ["Himadri", "Himachal", "Shiwalik", "Karakoram"], "Shiwalik",
        "The **Shiwalik** (Outer Himalaya) is the lowest, youngest and southernmost range, made of loose river sediments.",
        None, 15)
    S.q("ga-ip-p3", "medium", "Longitudinal valleys lying between the Lesser Himalaya and the Shiwaliks, such as Dehradun, are called:",
        ["Duns", "Duars", "Kayals", "Terai"], "Duns",
        "Such flat valleys are called **Duns** (Dehradun, Kotli Dun, Patli Dun). Duars are the foothill plains of the eastern Himalaya; kayals are Kerala backwaters; the Terai is the marshy belt below the Bhabar.",
        None, 20)
    S.q("ga-ip-p3", "medium", "Which of the following is NOT a part of the Purvanchal hills?",
        ["Patkai Bum", "Naga Hills", "Mizo Hills", "Pir Panjal"], "Pir Panjal",
        "The **Pir Panjal** is a range of the Lesser Himalaya in J&K and Himachal. The Purvanchal (eastern hills) are Patkai Bum, Naga, Manipur and Mizo (Lushai) hills.",
        None, 20)
    S.q("ga-ip-p4", "medium", "Which is the largest freshwater lake of India?",
        ["Chilika", "Wular", "Sambhar", "Pulicat"], "Wular",
        "**Wular** lake in J&K, fed by the Jhelum, is the largest freshwater lake. Chilika is a brackish lagoon, Sambhar is salt, Pulicat is a lagoon.",
        "Fresh-Wular, brackish-Chilika, salt-Sambhar.", 20)
    S.q("ga-ip-p4", "medium", "Lonar Lake in Maharashtra was formed by:",
        ["A meteorite impact", "A volcanic eruption", "A retreating glacier", "A tectonic rift"], "A meteorite impact",
        "**Lonar** (Buldhana district) sits in a crater made by a **meteorite impact** on the basalt of the Deccan Trap.",
        None, 20)
    S.q("ga-ip-p4", "medium", "Sambhar Lake, India's largest inland salt lake, is in:",
        ["Gujarat", "Rajasthan", "Haryana", "Ladakh"], "Rajasthan",
        "**Sambhar** lies near Jaipur in **Rajasthan** and is a major source of salt.",
        None, 15)
    S.q("ga-ip-p5", "easy", "The Malabar coast lies mainly in which state?",
        ["Kerala", "Tamil Nadu", "Maharashtra", "Odisha"], "Kerala",
        "West coast order north to south: Konkan (Maharashtra-Goa), Kanara (Karnataka), **Malabar (Kerala)**. Tamil Nadu has the Coromandel coast.",
        None, 15)
    S.q("ga-ip-p5", "medium", "The Deccan Trap region is made mainly of:",
        ["Granite", "Basalt lava", "Sandstone", "Limestone"], "Basalt lava",
        "The **Deccan Trap** was formed by huge flows of **basalt lava**; its weathering gave the black (regur) soil of Maharashtra and Gujarat.",
        None, 20)
    S.q("ga-ip-p5", "hard", "The Malda gap separates the Meghalaya plateau from the:",
        ["Chota Nagpur plateau", "Malwa plateau", "Deccan plateau", "Shillong plateau"], "Chota Nagpur plateau",
        "The Meghalaya (Shillong) plateau was once joined to the **Chota Nagpur** plateau; the **Malda gap**, later filled by Ganga-Brahmaputra sediments, now separates them.",
        None, 30)
    return S


def build_rivers():
    S = Sub("ig-rivers")
    S.notes = NOTES["ig-rivers"].strip()
    S.pattern("ga-ir-p1", "River ↔ source (origin point)", "very common",
        "'Which river rises at Amarkantak / Trimbakeshwar / Talakaveri?', or a river with places as options.",
        None,
        "1. Peninsular sources: Godavari - Trimbakeshwar; Krishna - near Mahabaleshwar; Kaveri - Talakaveri; Mahanadi - Sihawa; Narmada and Son - Amarkantak; Tapi - Multai.\n2. Himalayan: Ganga (Bhagirathi) - Gangotri/Gaumukh; Yamuna - Yamunotri; Indus and Brahmaputra - near Mansarovar; Sutlej - Rakas Tal; Beas - Beas Kund.\n3. Amarkantak is the favourite: it feeds both a west-flowing (Narmada) and a north-flowing (Son) river.",
        "The Mahanadi rises in which state?",
        "**Chhattisgarh** - near Sihawa (Dhamtari district). It flows east through Odisha into the Bay of Bengal.")
    S.pattern("ga-ir-p2", "Confluences and tributaries", "very common",
        "'X and Y meet at…', 'Which is a tributary of…', 'Which is a right-bank tributary', Panch Prayag questions.",
        None,
        "1. Panch Prayag on the Alaknanda (upstream to downstream): Vishnu (Dhauliganga), Nand (Nandakini), Karna (Pindar), Rudra (Mandakini), Dev (Bhagirathi) - 'Very Nice Kids Read Daily'.\n2. Other meeting points: Beas-Sutlej at Harike; Ganga-Yamuna at Prayagraj; Chandra-Bhaga at Tandi.\n3. Ganga right-bank: Yamuna, Son; left-bank: Ramganga, Gomti, Ghaghara, Gandak, Kosi, Mahananda.",
        "Karnaprayag is the confluence of the Alaknanda with which river?",
        "The **Pindar**. (Vishnuprayag - Dhauliganga, Nandprayag - Nandakini, Rudraprayag - Mandakini, Devprayag - Bhagirathi.)")
    S.pattern("ga-ir-p3", "Dam / project ↔ river", "very common",
        "'Hirakud / Tehri / Sardar Sarovar is built on…', or a match-the-column of dams and rivers.",
        None,
        "1. North: Tehri - Bhagirathi; Bhakra Nangal - Sutlej; Farakka barrage - Ganga.\n2. Peninsula: Hirakud - Mahanadi; Sardar Sarovar - Narmada; Nagarjuna Sagar and Srisailam - Krishna; Mettur and KRS - Kaveri; Idukki - Periyar.\n3. Superlatives: Tehri tallest; Hirakud longest earthen dam.",
        "The Krishnarajasagar (KRS) dam near Mysuru is on which river?",
        "The **Kaveri**. Mettur dam in Tamil Nadu is on the same river.")
    S.pattern("ga-ir-p4", "Waterfall ↔ river", "common",
        "A named waterfall (Jog, Chitrakote, Dhuandhar, Dudhsagar, Athirappilly, Shivanasamudra) with rivers as options.",
        None,
        "1. Karnataka: Jog - Sharavati; Shivanasamudra - Kaveri.\n2. Central India: Chitrakote - Indravati (Chhattisgarh); Dhuandhar - Narmada (Bhedaghat, Jabalpur).\n3. Coast: Dudhsagar - Mandovi (Goa); Athirappilly - Chalakudy (Kerala); Hogenakkal - Kaveri (TN).",
        "Hogenakkal Falls in Tamil Nadu are on which river?",
        "The **Kaveri** - near the Karnataka-Tamil Nadu border.")
    S.pattern("ga-ir-p5", "River nicknames and unique facts", "common",
        "'Sorrow of Bihar/Bengal', 'Dakshin Ganga', 'largest river island', 'forms an estuary', 'crosses the Tropic twice'.",
        None,
        "1. Nicknames: Kosi - Sorrow of Bihar; Damodar - Sorrow of Bengal; Godavari - Dakshin Ganga.\n2. Firsts: Ganga longest river of India; Yamuna longest tributary; Majuli (Brahmaputra) largest river island; Sundarbans largest delta.\n3. Narmada and Tapi flow west in rift valleys and form estuaries, not deltas; the Mahi crosses the Tropic of Cancer twice.",
        "Which river is called the 'Sorrow of Bengal'?",
        "The **Damodar** - it used to flood the plains of West Bengal; the Damodar Valley Corporation (1948) was set up to control it.")

    S.q("ga-ir-p1", "easy", "The Godavari river rises at:",
        ["Mahabaleshwar", "Trimbakeshwar", "Amarkantak", "Talakaveri"], "Trimbakeshwar",
        "The **Godavari** rises at **Trimbakeshwar** near Nashik, Maharashtra. Krishna - Mahabaleshwar; Narmada - Amarkantak; Kaveri - Talakaveri.",
        None, 15)
    S.q("ga-ir-p1", "medium", "The Kaveri river originates at Talakaveri in which hills?",
        ["Brahmagiri Hills (Kodagu)", "Nilgiri Hills", "Anaimalai Hills", "Cardamom Hills"], "Brahmagiri Hills (Kodagu)",
        "The **Kaveri** rises at **Talakaveri** in the **Brahmagiri hills** of Kodagu (Coorg) district, Karnataka.",
        None, 20)
    S.q("ga-ir-p1", "medium", "Both the Narmada and the Son rise at:",
        ["Multai", "Mahabaleshwar", "Amarkantak", "Sihawa"], "Amarkantak",
        "**Amarkantak** (Madhya Pradesh, at the Maikal hills) is the source of the west-flowing **Narmada** and the north-flowing **Son**. Multai = Tapi; Sihawa = Mahanadi.",
        None, 20)
    S.q("ga-ir-p2", "medium", "The Beas joins the Sutlej at:",
        ["Harike", "Ropar", "Tandi", "Nangal"], "Harike",
        "The **Beas** meets the **Sutlej** at **Harike** in Punjab, where a barrage and a wetland stand. Tandi is where the Chandra and Bhaga meet.",
        None, 20)
    S.q("ga-ir-p2", "hard", "At Rudraprayag the Alaknanda is joined by the:",
        ["Mandakini", "Pindar", "Nandakini", "Dhauliganga"], "Mandakini",
        "**Rudraprayag** = Alaknanda + **Mandakini** (which flows down from Kedarnath). Pindar joins at Karnaprayag, Nandakini at Nandprayag, Dhauliganga at Vishnuprayag.",
        "Very Nice Kids Read Daily: Vishnu, Nand, Karna, Rudra, Dev.", 25)
    S.q("ga-ir-p2", "hard", "Which of the following is a RIGHT-bank tributary of the Ganga?",
        ["Gomti", "Ghaghara", "Kosi", "Son"], "Son",
        "The **Son** comes from the south (Amarkantak) and joins the Ganga on its right bank near Patna. Gomti, Ghaghara and Kosi come from the north - left bank.",
        "Rivers from the peninsula (Yamuna system, Son) join on the right.", 25)
    S.q("ga-ir-p3", "easy", "The Tehri Dam, the tallest dam in India, is built on the:",
        ["Alaknanda", "Bhagirathi", "Yamuna", "Sutlej"], "Bhagirathi",
        "**Tehri Dam** (Uttarakhand) stands on the **Bhagirathi**. Bhakra Nangal is on the Sutlej.",
        None, 15)
    S.q("ga-ir-p3", "medium", "The Nagarjuna Sagar dam is built on which river?",
        ["Godavari", "Krishna", "Kaveri", "Tungabhadra"], "Krishna",
        "**Nagarjuna Sagar** (on the Telangana-Andhra Pradesh border) is on the **Krishna**, as is the Srisailam dam upstream.",
        None, 20)
    S.q("ga-ir-p3", "hard", "The Idukki arch dam in Kerala is built on the:",
        ["Periyar", "Bharathapuzha", "Pamba", "Chalakudy"], "Periyar",
        "The **Idukki** dam, one of Asia's large arch dams, is on the **Periyar**, Kerala's longest river.",
        None, 25)
    S.q("ga-ir-p4", "medium", "Chitrakote Falls, called the 'Niagara of India', is on which river?",
        ["Mahanadi", "Indravati", "Narmada", "Sharavati"], "Indravati",
        "**Chitrakote** (Bastar, Chhattisgarh) is a wide horseshoe fall on the **Indravati**, a tributary of the Godavari.",
        None, 20)
    S.q("ga-ir-p4", "medium", "The Dhuandhar Falls at Bhedaghat near Jabalpur are on the:",
        ["Tapi", "Son", "Narmada", "Chambal"], "Narmada",
        "**Dhuandhar** ('smoke-stream') falls lie on the **Narmada** at Bhedaghat, known for its marble rocks.",
        None, 20)
    S.q("ga-ir-p4", "hard", "Dudhsagar Falls on the Goa-Karnataka border are on which river?",
        ["Mandovi", "Zuari", "Sharavati", "Kali"], "Mandovi",
        "**Dudhsagar** ('sea of milk') is a four-tier waterfall on the **Mandovi** river.",
        None, 25)
    S.q("ga-ir-p5", "easy", "Which river is known as the 'Sorrow of Bihar'?",
        ["Gandak", "Kosi", "Son", "Damodar"], "Kosi",
        "The **Kosi** often changes its course and floods north Bihar, so it is called the 'Sorrow of Bihar'. The Damodar is the 'Sorrow of Bengal'.",
        None, 15)
    S.q("ga-ir-p5", "easy", "Majuli, the largest river island in the world, lies in which river?",
        ["Ganga", "Brahmaputra", "Godavari", "Mahanadi"], "Brahmaputra",
        "**Majuli** in Assam is formed by the **Brahmaputra** and its channels.",
        None, 15)
    S.q("ga-ir-p5", "medium", "Which of the following rivers forms an estuary instead of a delta?",
        ["Godavari", "Krishna", "Tapi", "Mahanadi"], "Tapi",
        "The **Tapi** (like the Narmada) flows west through a rift valley and enters the Arabian Sea through an **estuary**. The Godavari, Krishna and Mahanadi flow east and build deltas.",
        "West-flowing rift rivers = estuary.", 20)
    return S
