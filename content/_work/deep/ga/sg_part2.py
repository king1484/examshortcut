"""static-gk deep content - part 2: important-days, national-symbols-firsts, organisations-countries."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub
from sg_notes import NOTES


def build_days():
    S = Sub("important-days")
    S.notes = NOTES["important-days"].strip()
    S.pattern("ga-id-p1", "Day ↔ birth/death anniversary of a person", "very common",
        "'National Sports Day honours', 'Teachers' Day is the birth anniversary of', 'Youth Day', 'Mathematics Day', person-linking questions.",
        None,
        "1. Birth-linked chain: 12 Jan Vivekananda (Youth), 28 Feb Raman effect (Science), 1 Jul B.C. Roy (Doctors), 29 Aug Dhyan Chand (Sports), 5 Sep Radhakrishnan (Teachers), 15 Sep Visvesvaraya (Engineers), 14 Nov Nehru (Children), 22 Dec Ramanujan (Mathematics).\n2. 30 Jan - Martyrs' Day, the day Gandhi was assassinated (1948).\n3. If the question names a profession or field, first look for the person-date row.",
        "**National Mathematics Day** (22 December) commemorates the birth anniversary of —",
        "**Srinivasa Ramanujan** (born 22 December 1887); observed since 2012. Teachers' Day (5 Sep) marks Radhakrishnan's birthday.")
    S.pattern("ga-id-p2", "National day ↔ date", "very common",
        "'National Voters' Day', 'National Technology Day', 'Hindi Diwas', 'National Unity Day', date-to-theme matching.",
        None,
        "1. Republic dates: 26 Jan Republic Day; 25 Jan National Voters' Day (EC founded 25 Jan 1950); 24 Jan National Girl Child Day.\n2. **11 May National Technology Day** - Pokhran nuclear tests of 11 May 1998. **14 Sep Hindi Diwas** (official-language resolution 1949). **31 Oct National Unity Day** - Sardar Patel's birthday.\n3. **28 Feb National Science Day** - Raman effect announced 28 February 1928.",
        "**National Unity Day**, marked on 31 October, celebrates the birth anniversary of —",
        "**Sardar Vallabhbhai Patel** - the 'Iron Man' who integrated the princely states.")
    S.pattern("ga-id-p3", "International day ↔ date (UN and others)", "very common",
        "'World Water/Health/Environment/Food day', 'International Yoga Day', 'Human Rights Day', UN-day matching.",
        None,
        "1. Spring cluster: 8 Mar Women, 22 Mar Water, 7 Apr Health (WHO founded 7 Apr 1948), 22 Apr Earth, 1 May Labour.\n2. Mid-year: 5 Jun Environment, 21 Jun Yoga (first observed 2015, India's proposal), 12 Aug Youth, 29 Jul Tiger.\n3. Year-end: 16 Oct Food (FAO 1945), 24 Oct UN (founded 1945), 1 Dec AIDS, 10 Dec Human Rights (UDHR 1948).",
        "**World Health Day** is observed on 7 April because —",
        "The **World Health Organization was founded on 7 April 1948** - the date of its constitution coming into force.")
    S.pattern("ga-id-p4", "Defence forces days", "common",
        "'Army/Navy/Air Force day', dates of the three services, Operation Trident link.",
        None,
        "1. **Army Day - 15 January** (K.M. Cariappa became the first Indian Commander-in-Chief on 15 Jan 1949).\n2. **Air Force Day - 8 October** (the IAF was founded 8 Oct 1932).\n3. **Navy Day - 4 December** (recalls Operation Trident's missile attack on Karachi, 1971).",
        "**Indian Navy Day** is celebrated on —",
        "**4 December** - commemorating Operation Trident of the 1971 war; Army Day is 15 January and Air Force Day 8 October.")
    S.pattern("ga-id-p5", "Republic-era constitutional days", "occasional",
        "'Why is 26 January Republic Day', 'Constitution came into force on', 'Samvidhan Divas', founding dates behind days.",
        None,
        "1. **26 January 1950** - the Constitution came into force (adopted 26 November 1949 - **Samvidhan Divas**, Constitution Day).\n2. **15 August 1947** - Independence Day.\n3. 25 January - Voters' Day (Election Commission set up 25 January 1950).",
        "Why is **Republic Day** celebrated on 26 January?",
        "The **Constitution came into force on 26 January 1950** - the date chosen to honour the 1930 Purna Swaraj declaration of 26 January.")

    S.q("ga-id-p1", "easy", "**Teachers' Day** in India (5 September) is the birth anniversary of:",
        ["S. Radhakrishnan", "Rajendra Prasad", "A.P.J. Abdul Kalam", "Madan Mohan Malaviya"], "S. Radhakrishnan",
        "Dr **S. Radhakrishnan**, philosopher and second President, was born on 5 September 1888; since 1962 the day honours teachers.",
        None, 15)
    S.q("ga-id-p1", "medium", "**National Youth Day** (12 January) marks the birth anniversary of:",
        ["Swami Dayananda Saraswati", "Swami Vivekananda", "Sri Aurobindo", "Raja Ram Mohan Roy"], "Swami Vivekananda",
        "**Swami Vivekananda** (born 12 January 1863); the date also opens the National Youth Festival.",
        None, 15)
    S.q("ga-id-p1", "medium", "**Engineers' Day** (15 September) commemorates the birth of which engineer?",
        ["M. Visvesvaraya", "E. Sreedharan", "C.V. Raman", "Homi Bhabha"], "M. Visvesvaraya",
        "Sir **M. Visvesvaraya** (1861), knighted engineer of the Krishna Raja Sagara dam and automatic sluices.",
        None, 20)
    S.q("ga-id-p1", "medium", "**National Doctors' Day** (1 July) honours which physician-statesman?",
        ["B.C. Roy", "Anandi Gopal Joshi", "P.K. Sen", "K. Srinath Reddy"], "B.C. Roy",
        "Dr **Bidhan Chandra Roy**, physician and West Bengal Chief Minister, born and died on 1 July; a Bharat Ratna recipient (1961).",
        None, 25)
    S.q("ga-id-p2", "medium", "**National Technology Day** (11 May) recalls which event of 1998?",
        ["Launch of INSAT-2D", "The Pokhran nuclear tests", "First indigenous aircraft carrier", "Chandrayaan-1 approval"], "The Pokhran nuclear tests",
        "Operation Shakti's **Pokhran-II tests** of **11 May 1998**; the day celebrates Indian technology.",
        None, 20)
    S.q("ga-id-p2", "medium", "**Hindi Diwas** is observed on 14 September because on that day in 1949 —",
        ["Hindi's grammar was standardised", "Hindi was adopted as the official language of the Union", "The first Hindi newspaper appeared", "The Sahitya Akademi was set up"], "Hindi was adopted as the official language of the Union",
        "The Constituent Assembly adopted **Hindi in Devanagari script** as the official language of the Union on **14 September 1949** (Article 343).",
        None, 25)
    S.q("ga-id-p2", "hard", "**National Voters' Day** (25 January) marks the founding day of the:",
        ["Parliament of India", "Election Commission of India", "Supreme Court of India", "Niti Aayog"], "Election Commission of India",
        "The **Election Commission was constituted on 25 January 1950**; Voters' Day has been observed on the date since 2011.",
        None, 25)
    S.q("ga-id-p3", "easy", "**International Yoga Day** is observed on:",
        ["21 March", "21 June", "21 September", "21 December"], "21 June",
        "**21 June**, the longest day in the north - first observed in **2015** after India's proposal at the UN (2014).",
        None, 15)
    S.q("ga-id-p3", "medium", "**World Food Day** (16 October) is linked to the founding of which organisation?",
        ["World Food Programme", "FAO", "UNICEF", "WHO"], "FAO",
        "The **Food and Agriculture Organization** was founded on **16 October 1945** in Rome, its permanent headquarters city.",
        None, 20)
    S.q("ga-id-p3", "medium", "**Human Rights Day** (10 December) commemorates the adoption in 1948 of the:",
        ["Geneva Conventions", "Universal Declaration of Human Rights", "International Covenant on Civil Rights", "UN Charter"], "Universal Declaration of Human Rights",
        "The **UDHR** was adopted by the UN General Assembly in Paris on **10 December 1948**.",
        None, 20)
    S.q("ga-id-p3", "hard", "**World Water Day** falls on which date?",
        ["22 February", "22 March", "22 April", "22 June"], "22 March",
        "**22 March** (since 1993). 22 April is Earth Day; 5 June is Environment Day.",
        None, 20)
    S.q("ga-id-p4", "medium", "**Indian Air Force Day** is observed on —",
        ["15 January", "8 October", "4 December", "16 December"], "8 October",
        "The **IAF was founded on 8 October 1932**; Army Day - 15 January; Navy Day - 4 December.",
        None, 20)
    S.q("ga-id-p4", "hard", "**Army Day** (15 January) recalls the day in 1949 when:",
        ["The first war ended", "K.M. Cariappa became the first Indian Commander-in-Chief", "The NCC was founded", "The National War Memorial opened"], "K.M. Cariappa became the first Indian Commander-in-Chief",
        "General **K.M. Cariappa** (later Field Marshal) took over from General Sir Francis Butcher on **15 January 1949**.",
        None, 30)
    S.q("ga-id-p5", "medium", "**Constitution Day (Samvidhan Divas)** is observed on 26 November, the day the Constitution was —",
        ["Came into force", "Adopted by the Constituent Assembly", "First amended", "Signed by the President"], "Adopted by the Constituent Assembly",
        "Adopted **26 November 1949**; it **came into force on 26 January 1950**, which is Republic Day.",
        None, 25)
    S.q("ga-id-p5", "hard", "Republic Day is fixed on 26 January to honour the **Purna Swaraj** declaration of independence, first publicly celebrated on 26 January of which year?",
        ["1919", "1927", "1930", "1942"], "1930",
        "The Congress declared Purna Swaraj at its **Lahore session (December 1929)**; the first Independence Day was observed on **26 January 1930**, hence the date for Republic Day.",
        None, 30)
    return S


def build_symbols():
    S = Sub("national-symbols-firsts")
    S.notes = NOTES["national-symbols-firsts"].strip()
    S.pattern("ga-nf-p1", "National symbol ↔ identity", "very common",
        "'National aquatic animal', 'national tree/fruit/river', 'heritage animal', symbol matching.",
        None,
        "1. Tiger - animal; **peacock - bird (1963)**; lotus - flower; **banyan - tree**; mango - fruit.\n2. **Ganga - national river (2008)**; **Gangetic river dolphin - aquatic animal (2009)**; **elephant - heritage animal (2010)**; Saka calendar - national calendar.\n3. The royal Bengal tiger replaced the lion as national animal; the peacock was chosen in 1963.",
        "Which is India's **national heritage animal**?",
        "The **Asian elephant** (declared 2010). The Gangetic dolphin is the national aquatic animal.")
    S.pattern("ga-nf-p2", "Flag facts: design, dates, code", "common",
        "'Who designed the national flag', 'ratio of the flag', 'number of spokes in the chakra', 'flag adopted on'.",
        None,
        "1. Adopted **22 July 1947**; ratio **3 : 2**; **Pingali Venkayya**'s design.\n2. Navy-blue **Ashoka Chakra with 24 spokes** at the centre, from the Sarnath Lion Capital.\n3. Saffron = courage-sacrifice; white = truth-peace; green = faith-prosperity.",
        "How many **spokes** does the Ashoka Chakra on the national flag have?",
        "**24 spokes** - it is taken from the Lion Capital of Ashoka at Sarnath.")
    S.pattern("ga-nf-p3", "Anthem, song, emblem and calendar", "very common",
        "'Anthem was adopted on', 'Vande Mataram is from', 'state emblem is taken from', 'Satyameva Jayate source', adoption dates.",
        None,
        "1. **Anthem** - Jana Gana Mana (Tagore), adopted **24 January 1950**; playing time about 52 seconds.\n2. **National song** - Vande Mataram by Bankim Chandra, from *Anandamath* (first sung at the 1896 Congress session).\n3. **Emblem** - Sarnath Lion Capital of Ashoka, adopted **26 January 1950**; motto **Satyameva Jayate** from the **Mundaka Upanishad**; Saka calendar in use since 1957.",
        "India's **national anthem** was adopted by the Constituent Assembly on —",
        "**24 January 1950** - Jana Gana Mana by Rabindranath Tagore; the emblem had been adopted a day later, on 26 January 1950.")
    S.pattern("ga-nf-p4", "Firsts - women", "very common",
        "'First woman Chief Minister/Governor/President/IPS/pilot in space/Everest', first-women matching.",
        None,
        "1. **Governor - Sarojini Naidu** (UP, 1947); **Chief Minister - Sucheta Kripalani** (UP, 1963); **President - Pratibha Patil** (2007); **Speaker - Meira Kumar** (2009).\n2. **IPS - Kiran Bedi (1972)**; **space - Kalpana Chawla (1997)**; **Everest - Bachendri Pal (1984)**.\n3. INC first woman president - Annie Besant (1917); first Indian woman - Sarojini Naidu (1925).",
        "Who was the **first woman Chief Minister** of an Indian state?",
        "**Sucheta Kripalani** (Uttar Pradesh, 1963). Sarojini Naidu was the first woman *Governor* (UP, 1947).")
    S.pattern("ga-nf-p5", "Firsts - offices, science and infrastructure", "common",
        "'First President/Prime Minister/Field Marshal', 'first Indian in space', 'first satellite/feature film/railway', pioneering-list questions.",
        None,
        "1. Offices: **Rajendra Prasad** first President; **Nehru** first (and longest-serving) PM; **Sam Manekshaw** first Field Marshal (1973).\n2. Space: **Rakesh Sharma** (1984, Soyuz T-11) first Indian in space; **Kalpana Chawla** (1997) first Indian woman; **Aryabhata** first satellite (1975); Chandrayaan-3 landed near the lunar south pole **23 August 2023** - **National Space Day**.\n3. beginnings: first feature film **Raja Harishchandra** (1913); first railway **Bombay-Thane, 16 April 1853**; first census 1872; first bank Bank of Hindustan (1770).",
        "Who was the **first Field Marshal** of the Indian Army?",
        "**Sam Manekshaw** (1973), Chief of Army Staff during the 1971 war; K.M. Cariappa and Arjan Singh followed in 1986 and 2002.")

    S.q("ga-nf-p1", "easy", "The **national aquatic animal** of India is the:",
        ["Blue whale", "Gangetic river dolphin", "Olive Ridley turtle", "King cobra"], "Gangetic river dolphin",
        "The **Gangetic river dolphin** was declared national aquatic animal in 2009; the Ganga is the national river (2008).",
        None, 15)
    S.q("ga-nf-p1", "medium", "Which of the following is India's **national tree**?",
        ["Peepal", "Neem", "Banyan", "Mango"], "Banyan",
        "The **banyan** (Ficus benghalensis) - longevity and rootedness; the mango is the national fruit.",
        None, 15)
    S.q("ga-nf-p1", "medium", "The **Saka calendar**, used in official gazettes alongside the Gregorian calendar, was adopted in —",
        ["1947", "1950", "1957", "1962"], "1957",
        "Adopted from **22 March 1957** (= 1 Chaitra 1879 Saka) on the Calendar Reform Committee's recommendation.",
        None, 25)
    S.q("ga-nf-p2", "easy", "The Indian national flag was adopted by the Constituent Assembly on:",
        ["15 August 1947", "22 July 1947", "26 January 1950", "26 November 1949"], "22 July 1947",
        "**22 July 1947** - about a fortnight before Independence; the ratio is 3:2.",
        None, 15)
    S.q("ga-nf-p2", "medium", "Who designed the present form of the **Indian national flag**?",
        ["Pingali Venkayya", "Bankim Chandra", "Abanindranath Tagore", "Nandalal Bose"], "Pingali Venkayya",
        "**Pingali Venkayya** of Andhra, whose design (with Gandhi's suggested additions) became the tricolour.",
        None, 15)
    S.q("ga-nf-p2", "medium", "In the national flag, the **navy-blue Ashoka Chakra** stands for —",
        ["Sacrifice", "Truth and peace", "Progress and motion (the wheel of law)", "Faith and fertility"], "Progress and motion (the wheel of law)",
        "The chakra represents the **wheel of law (dharma)** and constant movement forward; the 24 spokes evoke the hours of the day.",
        None, 25)
    S.q("ga-nf-p3", "medium", "*Vande Mataram*, India's national song, is taken from Bankim Chandra Chattopadhyay's novel —",
        ["Devi Chaudhurani", "Anandamath", "Kapalkundala", "Durgeshnandini"], "Anandamath",
        "***Anandamath*** (1882); the song was first sung at the 1896 Calcutta session of the Congress.",
        None, 20)
    S.q("ga-nf-p3", "medium", "The State Emblem of India is adapted from the Lion Capital of Ashoka at —",
        ["Delhi-Topra", "Sarnath", "Lauriya Nandangarh", "Rampurva"], "Sarnath",
        "The **Sarnath** capital (four lions on an abacus), adopted on 26 January 1950 with the motto Satyameva Jayate.",
        None, 20)
    S.q("ga-nf-p3", "medium", "The words **'Satyameva Jayate'** on the state emblem are taken from:",
        ["Bhagavad Gita", "Rig Veda", "Mundaka Upanishad", "Arthashastra"], "Mundaka Upanishad",
        "The **Mundaka Upanishad** - 'truth alone triumphs'.",
        None, 20)
    S.q("ga-nf-p4", "medium", "Who was the **first woman Speaker** of the Lok Sabha?",
        ["Sushma Swaraj", "Meira Kumar", "Sumitra Mahajan", "Najma Heptullah"], "Meira Kumar",
        "**Meira Kumar** (2009-14); Sumitra Mahajan followed her in the chair.",
        None, 25)
    S.q("ga-nf-p4", "medium", "The **first Indian woman to reach the summit of Mount Everest** (1984) was:",
        ["Santosh Yadav", "Bachendri Pal", "Premlata Agarwal", "Arunima Sinha"], "Bachendri Pal",
        "**Bachendri Pal** (Tata group mountaineer) climbed Everest in May 1984; Santosh Yadav summited twice later.",
        None, 25)
    S.q("ga-nf-p4", "hard", "Who was the **first woman President of the Indian National Congress**?",
        ["Sarojini Naidu", "Annie Besant", "Nellie Sengupta", "Kadambini Ganguly"], "Annie Besant",
        "**Annie Besant** presided over the Calcutta session in 1917; **Sarojini Naidu** was the first Indian woman, in 1925 (Kanpur session).",
        None, 30)
    S.q("ga-nf-p5", "easy", "India's **first Prime Minister** was:",
        ["Sardar Patel", "Jawaharlal Nehru", "Rajendra Prasad", "Lal Bahadur Shastri"], "Jawaharlal Nehru",
        "**Nehru** (1947-64), also the longest-serving Prime Minister; Rajendra Prasad was the first President.",
        None, 15)
    S.q("ga-nf-p5", "medium", "The **first Indian satellite**, launched in 1975, was named:",
        ["Rohini", "Aryabhata", "Bhaskara", "INSAT-1A"], "Aryabhata",
        "**Aryabhata**, launched (from a Soviet rocket) in 1975 and named after the ancient astronomer.",
        None, 20)
    S.q("ga-nf-p5", "medium", "**23 August**, the day Chandrayaan-3 landed near the Moon's south pole (2023), is observed as —",
        ["National Space Day", "National Science Day", "Mission Day", "Vigyan Diwas"], "National Space Day",
        "**National Space Day** - the Vikram lander touched down on 23 August 2023, making India the fourth country to soft-land on the Moon.",
        None, 20)
    S.q("ga-nf-p5", "medium", "India's **first passenger train** ran in 1853 between:",
        ["Howrah and Hughli", "Bombay and Thane", "Madras and Arcot", "Delhi and Meerut"], "Bombay and Thane",
        "**16 April 1853** - 34 km from Bombay (Bori Bunder) to Thane; the first railway company had been formed in 1849.",
        None, 20)
    S.q("ga-nf-p5", "hard", "Who was the **first Indian to travel into space** (1984)?",
        ["Kalpana Chawla", "Rakesh Sharma", "Ravish Malhotra", "Sunita Williams"], "Rakesh Sharma",
        "Sqn Ldr **Rakesh Sharma** flew on the Soviet Soyuz T-11 in 1984; his reply from orbit - 'saare jahaan se achha'. Ravish Malhotra was his backup.",
        None, 30)
    return S


def build_orgs():
    S = Sub("organisations-countries")
    S.notes = NOTES["organisations-countries"].strip()
    S.pattern("ga-oc-p1", "UN bodies ↔ headquarters", "very common",
        "'Where is UNESCO/WHO/FAO/UNICEF headquartered', match-the-column on UN agencies.",
        None,
        "1. New York: UN, UNICEF, UNDP. Geneva: WHO, ILO, WTO, ICRC. Paris: UNESCO. Rome: FAO, WFP.\n2. Nairobi: UNEP. Vienna: IAEA, OPEC. The Hague: ICJ, OPCW. Washington DC: IMF, World Bank.\n3. Founding years asked together: UN 1945, UNICEF 1946, WHO 1948, WTO 1995, ILO 1919.",
        "The **International Court of Justice** sits at —",
        "**The Hague** (Netherlands), in the Peace Palace; the UN itself is headquartered in New York.")
    S.pattern("ga-oc-p2", "International bodies ↔ headquarters and founding years", "very common",
        "'NATO/ASEAN/SAARC headquarters', 'ADB/AIIB/NDB', 'FIFA/IOC/ICC', HQ-plus-year questions.",
        None,
        "1. Brussels-NATO (1949); Jakarta-ASEAN (1967); Kathmandu-SAARC (1985); Dhaka-BIMSTEC (1997).\n2. Banks: ADB-Manila (1966), AIIB-Beijing (2016), NDB-Shanghai (2015); solar: International Solar Alliance-**Gurugram**.\n3. Sport: FIFA-Zurich (1904), IOC-Lausanne (1894), ICC-Dubai; police/travel: INTERPOL-Lyon (1923), ICAO-Montreal, IMO-London.",
        "The **International Solar Alliance**, founded at India's initiative, is headquartered at —",
        "**Gurugram** (India) - the first treaty-based international organisation headquartered in India.")
    S.pattern("ga-oc-p3", "Currency ↔ country", "very common",
        "'Currency of Bangladesh/Thailand/Indonesia/South Africa', currency matching, unusual currencies.",
        None,
        "1. South Asia: taka-Bangladesh, **ngultrum-Bhutan**, rufiyaa-Maldives, afghani-Afghanistan; rupee elsewhere.\n2. East Asia: yuan-China, yen-Japan, won-South Korea, baht-Thailand, ringgit-Malaysia, rupiah-Indonesia, dong-Vietnam, kyat-Myanmar.\n3. West/Africa/Americas: rouble-Russia, riyal-Saudi, dirham-UAE, shekel-Israel, rand-South Africa, naira-Nigeria, real-Brazil, peso-Argentina/Mexico.",
        "The currency of **Indonesia** is the —",
        "**Rupiah**. Malaysia uses the ringgit; Vietnam the dong; Thailand the baht.")
    S.pattern("ga-oc-p4", "Parliament ↔ country", "very common",
        "'Knesset/Diet/Majlis/Bundestag is the parliament of', 'Duma is the lower house of', legislature matching.",
        None,
        "1. Israel-Knesset, Japan-Diet, Iran-Majlis, Germany-Bundestag, Bangladesh-Jatiya Sangsad, Pakistan-Majlis-e-Shoora.\n2. Russia-Federal Assembly (lower house **Duma**), China-National People's Congress, France-National Assembly, Turkey-Grand National Assembly.\n3. Nordic set: Denmark-Folketing, Norway-Storting, Sweden-Riksdag.",
        "The **Bundestag** is the lower house of the parliament of —",
        "**Germany**. The Diet belongs to Japan; the Knesset to Israel; the Riksdag to Sweden.")
    S.pattern("ga-oc-p5", "Organisation ↔ founding year / founder context", "common",
        "'When was WHO/ASEAN/NATO established', Bretton Woods twins, UN Charter dates.",
        None,
        "1. 1945: UN (24 Oct), FAO (16 Oct), UNESCO adopted. 1944: IMF and World Bank at **Bretton Woods**.\n2. 1948 WHO; 1949 NATO; 1957 IAEA; 1960 OPEC; 1967 ASEAN; 1985 SAARC; 1995 WTO.\n3. Older bodies: ILO 1919, ICRC 1863, FIFA 1904, IOC 1894.",
        "The **IMF and the World Bank** were conceived at which 1944 conference?",
        "**Bretton Woods** (New Hampshire, USA) - hence their nickname, the Bretton Woods twins.")

    S.q("ga-oc-p1", "easy", "The headquarters of **UNESCO** are in:",
        ["New York", "Geneva", "Paris", "Vienna"], "Paris",
        "**UNESCO - Paris**; UNICEF and UNDP sit at New York; WHO and WTO at Geneva.",
        None, 15)
    S.q("ga-oc-p1", "medium", "The **Food and Agriculture Organization (FAO)** is headquartered in:",
        ["Geneva", "Rome", "Paris", "Nairobi"], "Rome",
        "**Rome** (Italy) - shared with the World Food Programme; UNEP alone is in Nairobi.",
        None, 15)
    S.q("ga-oc-p1", "medium", "Which specialised agency of the UN is headquartered in **Nairobi**?",
        ["UNESCO", "UNEP", "UNHCR", "UNIDO"], "UNEP",
        "The **UN Environment Programme** - making Nairobi the only UN headquarters city in the Global South.",
        None, 20)
    S.q("ga-oc-p2", "easy", "The headquarters of **SAARC** are at:",
        ["Dhaka", "New Delhi", "Kathmandu", "Colombo"], "Kathmandu",
        "**SAARC - Kathmandu** (founded 1985); BIMSTEC's secretariat is in Dhaka.",
        None, 15)
    S.q("ga-oc-p2", "medium", "The **Asian Development Bank (ADB)** is headquartered at:",
        ["Singapore", "Manila", "Tokyo", "Beijing"], "Manila",
        "**ADB - Manila** (1966). AIIB sits in Beijing and the NDB (BRICS bank) in Shanghai.",
        None, 20)
    S.q("ga-oc-p2", "medium", "The **International Olympic Committee (IOC)** is headquartered at:",
        ["Geneva", "Lausanne", "Zurich", "Paris"], "Lausanne",
        "**Lausanne**, Switzerland - the 'Olympic Capital'; FIFA's HQ is in Zurich.",
        None, 20)
    S.q("ga-oc-p2", "hard", "**INTERPOL**, the international police organisation (founded 1923), has its headquarters at:",
        ["The Hague", "Lyon", "Vienna", "Brussels"], "Lyon",
        "**INTERPOL - Lyon, France** (it began in Vienna in 1923). The Hague hosts the ICJ and OPCW.",
        None, 25)
    S.q("ga-oc-p3", "easy", "The currency of **Bangladesh** is the:",
        ["Rupee", "Taka", "Rupiah", "Dinar"], "Taka",
        "**Taka**. The rupiah belongs to Indonesia; the rupee to India, Pakistan, Nepal and Sri Lanka.",
        None, 15)
    S.q("ga-oc-p3", "medium", "The currency of **Myanmar** is the:",
        ["Baht", "Kyat", "Kip", "Ringgit"], "Kyat",
        "**Kyat**. Thailand - baht; Laos - kip; Malaysia - ringgit.",
        None, 15)
    S.q("ga-oc-p3", "medium", "The currency of **South Africa** is the:",
        ["Rand", "Naira", "Shilling", "Pula"], "Rand",
        "**Rand**. Nigeria - naira; Kenya - shilling; Botswana - pula.",
        None, 15)
    S.q("ga-oc-p3", "hard", "Which country's currency is the **real**?",
        ["Mexico", "Brazil", "Argentina", "Chile"], "Brazil",
        "**Brazil** uses the real; Mexico and Argentina use pesos; Chile the Chilean peso.",
        None, 25)
    S.q("ga-oc-p4", "easy", "The **Diet** is the national legislature of:",
        ["China", "Japan", "South Korea", "Mongolia"], "Japan",
        "Japan's parliament is the **Diet** (House of Representatives + House of Councillors); China's is the National People's Congress.",
        None, 15)
    S.q("ga-oc-p4", "medium", "The parliament of **Iran** is known as the:",
        ["Shura", "Majlis", "Wolesi Jirga", "Consultative Assembly"], "Majlis",
        "Iran's parliament is the **Majlis**; Pakistan's federal legislature is the Majlis-e-Shoora.",
        None, 20)
    S.q("ga-oc-p4", "medium", "The **Folketing** is the parliament of which country?",
        ["Norway", "Denmark", "Iceland", "Netherlands"], "Denmark",
        "**Denmark - Folketing**; Norway - Storting; Sweden - Riksdag.",
        None, 20)
    S.q("ga-oc-p4", "hard", "The lower house of Russia's Federal Assembly is called the:",
        ["State Duma", "Federation Council", "Gosplan", "Supreme Soviet"], "State Duma",
        "The **State Duma** is the lower house; the Federation Council is the upper house. (Gosplan was the Soviet planning body.)",
        None, 30)
    S.q("ga-oc-p5", "medium", "The **World Health Organization** was established in:",
        ["1945", "1946", "1948", "1950"], "1948",
        "**WHO - 7 April 1948** (hence World Health Day); it sits in Geneva.",
        None, 20)
    S.q("ga-oc-p5", "medium", "**ASEAN**, the association of South-East Asian nations, was founded in 1967 at:",
        ["Jakarta", "Bangkok", "Manila", "Kuala Lumpur"], "Bangkok",
        "Founded at **Bangkok** by the five original members (Indonesia, Malaysia, Philippines, Singapore, Thailand); its headquarters are in **Jakarta**.",
        None, 25)
    S.q("ga-oc-p5", "hard", "Which pair of organisations was created together at the **Bretton Woods Conference** (1944)?",
        ["UN and UNESCO", "IMF and World Bank", "WHO and ILO", "WTO and GATT"], "IMF and World Bank",
        "The **Bretton Woods twins** - the IMF and the International Bank for Reconstruction and Development (now the World Bank), both seated at Washington DC.",
        None, 30)
    return S
