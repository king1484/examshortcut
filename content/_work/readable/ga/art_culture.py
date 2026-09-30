"""Readable rewrite of General Awareness > Art & Culture (all 7 subtopics).

Plain English, short sentences, tables for the pairings. Every fact comes from the existing lesson text.
Old pattern ids are kept; new ids continue each prefix (ga-cd-p5 ...).
Run: python art_culture.py  (patches content/core/topics/ga/art-culture.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "art-culture.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


SUBS = {}

# =====================================================================
# 1. Classical dances
# =====================================================================
SUBS["classical-dances"] = dict(
    concept=(
        "The **Sangeet Natak Akademi** recognises **8 classical dances**. The Ministry of Culture also lists **Chhau**, which makes 9. "
        "Each dance belongs to one home state, and exam questions test that pair first. "
        "Then they ask for a famous dancer, a special feature or the founder of an arts school."
    ),
    notes="""### The nine dances at a glance
Learn each dance with its state. Then add one feature and one famous name.

| Dance | State | Signature feature | Famous names |
|---|---|---|---|
| **Bharatanatyam** | Tamil Nadu | Oldest; temple *devadasi* roots; based on the *Natya Shastra* | Rukmini Devi Arundale, Padma Subrahmanyam, Yamini Krishnamurthy, Mrinalini Sarabhai |
| **Kathak** | Uttar Pradesh / north | Only one linked with the **Mughal courts**; *chakkars* (spins), *tatkar* (footwork) | Pt. Birju Maharaj, Sitara Devi, Shovana Narayan |
| **Kathakali** | **Kerala** | Dance-drama; heavy make-up; green *pacha* for noble roles | Vallathol Narayana Menon, Kalamandalam Gopi |
| **Mohiniyattam** | Kerala | Graceful solo, the "dance of the enchantress" (Mohini) | Kalamandalam Kalyanikutty Amma, Bharati Shivaji, Sunanda Nair |
| **Kuchipudi** | **Andhra Pradesh** | Named after Kuchipudi village (Krishna district); *tarangam* on a brass plate | Vempati Chinna Satyam, Raja and Radha Reddy |
| **Odissi** | Odisha | *Tribhanga* posture; temple sculpture roots (Konark) | Kelucharan Mohapatra, Sonal Mansingh, Sanjukta Panigrahi |
| **Manipuri** | Manipur | Ras Lila of Radha and Krishna; soft, no ankle bells | Guru Bipin Singh, Jhaveri sisters |
| **Sattriya** | Assam | Created in the *sattras* (monasteries); recognised in **2000** | Guru Jatin Goswami, Indira P.P. Bora |
| **Chhau** | Odisha / Jharkhand / West Bengal | Semi-classical martial dance | none listed |

### Count and the Kerala confusion
The Akademi counts 8. The Ministry of Culture adds Chhau, so the total is 9.

Kerala has two dances: **Kathakali** and **Mohiniyattam**. Kathak is the north Indian court dance. Setters mix these up on purpose.

> **Rule:** Every other dance has one home state. Tamil Nadu is Bharatanatyam, Andhra Pradesh is Kuchipudi, Odisha is Odissi, Manipur is Manipuri, and Assam is Sattriya.

### Clues from make-up and movement
Make-up and movement name the dance faster than any list.

- **Kathakali:** elaborate green face (*pacha* means noble hero), codified hand language, heavy drums.
- **Mohiniyattam:** white *kasavu* costume and graceful *lasya* movement.
- **Manipuri:** circular, flowing, never sharp. The theme is the Ras Lila of Radha-Krishna.
- **Odissi:** the **tribhanga**, a three-bend stance.
- **Kathak:** spinning *chakkars* and rhythmic footwork. It has both Hindu and Mughal themes.
- **Sattriya:** the only classical dance born inside a monastery tradition. It comes from Srimanta Sankaradeva's 15th-century Bhakti movement.
- **Kuchipudi:** first a male Brahmin theatre, codified by Siddhendra Yogi. Dancers often balance on a brass plate.

> **Tip:** Read the clue first, then pick the dance. Green face means Kathakali. Three-bend means Odissi.

### Exponents and revival
- **Rukmini Devi Arundale** lifted Bharatanatyam out of its devadasi stigma. She founded **Kalakshetra** in **1936** at Chennai.
- **Vallathol Narayana Menon** founded **Kerala Kalamandalam** in **1930** to revive Kathakali.
- **Pt. Birju Maharaj** belonged to the Lucknow gharana of Kathak. Sitara Devi was its celebrated "Kathak queen".
- **Kelucharan Mohapatra** carried Odissi to the world stage.
- **Sonal Mansingh** is an Odissi dancer and a Padma Vibhushan awardee.

Kathak has three gharanas: Lucknow, Jaipur and Banaras.

### The Chhau triangle
Chhau is a semi-classical dance with masks and martial moves. It has three regional styles.

| Style | State | Masks |
|---|---|---|
| Mayurbhanj | Odisha | No masks |
| Seraikella | Jharkhand | Masks |
| Purulia | West Bengal | Masks |

Chhau entered UNESCO's Intangible Cultural Heritage list in **2010**.

> **Watch:** Mayurbhanj is the maskless style. If an option says all three use masks, reject it.
""",
    tricks=[
        trick("Kerala has two, the rest one each",
              "Kerala gives Kathakali and Mohiniyattam. Every other dance has one home state: TN Bharatanatyam, AP Kuchipudi, Odisha Odissi, Manipur Manipuri, Assam Sattriya, UP Kathak.",
              "Which state is home to two of the eight classical dances?",
              ["List the Kerala dances.", "Kathakali is Kerala.", "Mohiniyattam is Kerala."], "Kerala (Kathakali and Mohiniyattam)."),
        trick("Exponent hooks",
              "Birju is Kathak. Kelucharan is Odissi (Konark poses). Rukmini Devi revived Bharatanatyam (Kalakshetra). Vempati is Kuchipudi (village). Vallathol is Kerala Kalamandalam (Kathakali)."),
    ],
    mistakes=[
        mis("Giving Kathak to Kerala because it is a famous dance.", "Kerala has Kathakali and Mohiniyattam. Kathak is north Indian."),
        mis("Saying the Akademi recognises 9 dances.", "The Akademi recognises 8. The Ministry of Culture adds Chhau to make 9."),
        mis("Mixing up the two Kerala dances.", "Kathakali has green make-up and is a dance-drama. Mohiniyattam is a graceful solo."),
        mis("Swapping the two institutions.", "Kalakshetra (1936) is Rukmini Devi's, for Bharatanatyam. Kerala Kalamandalam (1930) is Vallathol's, for Kathakali."),
        mis("Saying all Chhau styles use masks.", "Mayurbhanj (Odisha) uses no masks. Seraikella and Purulia use masks."),
    ],
    revision=[
        "The Akademi recognises 8 classical dances. Adding Chhau makes 9.",
        "Kerala: Kathakali and Mohiniyattam. UP: Kathak.",
        "Bharatanatyam is Tamil Nadu. Kuchipudi is Andhra Pradesh. Odissi is Odisha. Manipuri is Manipur. Sattriya is Assam.",
        "Rukmini Devi started Kalakshetra in 1936. Vallathol started Kerala Kalamandalam in 1930.",
        "Odissi has tribhanga. Kathak has chakkars. Sattriya comes from the sattras of Sankaradeva.",
        "Chhau: Mayurbhanj has no masks. Seraikella and Purulia use masks. UNESCO listing in 2010.",
    ],
    patterns=[
        pat("ga-cd-p1", "Dance to state", "very common",
            "A dance is named and four states are given. Or a matching question mixes classical and folk forms.",
            ["Recall the seven main pairs.", "Cross out states that do not match.", "Watch for the Kerala-has-two trap."],
            "Each classical dance has one home state, so recall settles it.",
            "Kuchipudi is a classical dance of which state?",
            ["Kuchipudi is named after a village.", "The village is in Krishna district.", "That district is in Andhra Pradesh."],
            "Andhra Pradesh"),
        pat("ga-cd-p2", "Exponent to dance", "very common",
            "A dancer's name (Birju Maharaj, Rukmini Devi, Kelucharan Mohapatra) comes with four dance options.",
            ["Recall one famous name per dance.", "Match the name to its dance.", "Ignore options that share a state with the right one."],
            "One name per dance is enough to answer most questions.",
            "Pt. Birju Maharaj was a maestro of which dance?",
            ["He belonged to the Lucknow gharana.", "Lucknow is a Kathak gharana."],
            "Kathak"),
        pat("ga-cd-p3", "Dance to feature or theme", "very common",
            "A clue is described, such as green make-up, tribhanga, Ras Lila, plate balance or chakkars.",
            ["Read the clue.", "Map it: green face is Kathakali, tribhanga is Odissi, Ras Lila is Manipuri.", "Plate balance is Kuchipudi. Chakkars are Kathak. Lasya is Mohiniyattam."],
            "Each dance owns one clear feature that no other dance shares.",
            "The tribhanga (three-bend) posture is typical of which dance?",
            ["Tribhanga is a three-bend stance.", "It comes from temple sculpture at Konark.", "That is the dance of Odisha."],
            "Odissi"),
        pat("ga-cd-p4", "Institutions and recognition", "common",
            "Questions like who founded Kalakshetra, the year of Kerala Kalamandalam, or when a dance became classical.",
            ["Recall the two revival schools with year and founder.", "Recall that Sattriya was recognised in 2000.", "Match founder to art form."],
            "Two schools and one year cover this whole pattern.",
            "Kalakshetra was founded in 1936 by whom?",
            ["Kalakshetra is at Chennai.", "It was set up for Bharatanatyam.", "Its founder lifted the dance out of devadasi stigma."],
            "Rukmini Devi Arundale"),
        pat("ga-cd-p5", "Chhau styles and masks", "common",
            "The question names Chhau and asks about a style, a state, masks or the UNESCO year.",
            ["List the three styles: Mayurbhanj, Seraikella, Purulia.", "Pair each with its state.", "Remember that only Mayurbhanj has no mask."],
            "The mask difference is the easiest way for setters to create a trap.",
            "In which Chhau style are masks not used?",
            ["Seraikella (Jharkhand) uses masks.", "Purulia (West Bengal) uses masks.", "Mayurbhanj (Odisha) has no masks."],
            "Mayurbhanj (Odisha)"),
        pat("ga-cd-p6", "Count and Kerala trap", "occasional",
            "The question asks how many classical dances exist, or which state has more than one.",
            ["Recall that the Akademi lists 8.", "Recall that Chhau makes it 9.", "Recall that Kerala has two: Kathakali and Mohiniyattam."],
            "Count and Kerala are the two facts setters twist most often.",
            "Which body recognises 8 classical dances?",
            ["The body works for music, dance and drama.", "Its name begins with Sangeet Natak."],
            "Sangeet Natak Akademi (the Ministry of Culture adds Chhau to make 9)"),
    ],
)

# =====================================================================
# 2. Folk dances
# =====================================================================
SUBS["folk-dances"] = dict(
    concept=(
        "Folk dances are tied to a state, a community or a season. "
        "Most questions ask you to pair a dance with its state. "
        "Others ask for a feature, such as sticks or bamboo, or the festival where it is performed."
    ),
    notes="""### The core table
Learn the bold names first. They are asked most often.

| State | Folk dances |
|---|---|
| Gujarat | **Garba** (UNESCO ICH 2023), **Dandiya Raas**, Tippani, Padhar |
| Rajasthan | **Ghoomar**, **Kalbelia** (ICH 2010), Chari, Kachchhi Ghodi, Gair |
| Punjab | **Bhangra** (men), **Giddha** (women), Jhumar |
| Haryana | Phag, Saang, Loor |
| Maharashtra | **Lavani**, Tamasha, Koli, Lezim, Dhangari Gaja |
| Karnataka | **Yakshagana**, **Dollu Kunitha**, Bhootha Kola |
| Kerala | **Theyyam**, Padayani, Oppana, Thiruvathirakali, Ottam Thullal |
| Tamil Nadu | **Karakattam**, Kummi, Kolattam, Oyilattam |
| Andhra / Telangana | Dhimsa, Kolattam, Burrakatha, Perini Shivatandavam (Telangana) |
| Odisha | Chhau (Mayurbhanj), Dalkhai, Ghumura, Gotipua |
| West Bengal | Chhau (Purulia), Gambhira, Jatra, Baul (music) |
| Bihar | Jat-Jatin, Bidesia, Jhijhiya, Jhumar |
| Jharkhand | Chhau (Seraikela), Karma, Paika |
| Chhattisgarh | **Raut Nacha**, **Pandavani** (ballad, Teejan Bai), Gaur Maria, Karma, Panthi |
| Madhya Pradesh | Jawara, Matki, Tertali |
| Uttar Pradesh | Charkula, Nautanki, Raslila |
| Uttarakhand | Chholiya, Langvir Nritya, Barada Nati |
| Himachal Pradesh | **Nati** (Kullu Nati in Guinness Records), Jhora |
| Jammu & Kashmir | **Rouf**, Dumhal, Bhand Pather |
| Assam | **Bihu**, **Bagurumba** (Bodo), Jhumur (tea tribes) |
| Mizoram | **Cheraw** (bamboo dance) |
| Manipur | Thang Ta (martial), Lai Haraoba |
| Meghalaya | **Nongkrem** (Khasi), **Wangala** (Garo) |
| Nagaland | Chang Lo (Sua Lua), Zeliang |
| Tripura | **Hojagiri** (balancing on a pitcher) |
| Arunachal Pradesh | Bardo Chham, Ponung |
| Sikkim | Singhi Chham (snow-lion masks) |
| Goa | Fugdi, Dekhni |

### The North-East set
This set is a favourite in match-the-column questions.

- **Cheraw** is the bamboo dance of Mizoram.
- **Hojagiri** is the balancing dance of Tripura.
- **Nongkrem** is the Khasi dance of Meghalaya.
- **Wangala** is the Garo dance of Meghalaya.
- **Bagurumba** is the Bodo dance of Assam.

> **Tip:** Link the feature to the state. Bamboo is Mizoram. Balancing is Tripura. Khasi is Meghalaya.

### Feature and occasion clues
- **Garba** is a circular women's dance of Navratri, with clapping. **Dandiya Raas** uses sticks.
- **Ghoomar** is of Bhil origin. Rajasthan's royal houses adopted it. Women wear swirling ghagras.
- **Kalbelia** belongs to the snake-charmer Kalbelia community. Its moves imitate a serpent.
- **Bhangra** and **Giddha** mark the Baisakhi harvest.
- **Lavani** is fast, with dholki music. It grew inside the *tamasha* theatre of Maharashtra.
- **Yakshagana** is a night-long dance-drama of Karnataka with huge headgear.
- **Theyyam** is a Kerala ritual. Performers embody village goddesses, mostly male performers.
- **Bihu** is the spring (Rongali) dance of Assam.
- **Cheraw** dancers step between crossed bamboo staves clapped in rhythm.
- **Hojagiri** dancers are Reang women who balance on pots and bottles.
- **Nongkrem** is a Khasi thanksgiving dance.
- **Karma** is a dance of Karma-devi tree worship in the Chhattisgarh-Jharkhand belt.

> **Watch:** Yakshagana is Karnataka. Kathakali is Kerala. Setters put them side by side.

### The classical-folk border
Some forms sit near the line between classical and folk.

- **Chhau** is semi-classical and martial. It has three styles: Mayurbhanj, Seraikella and Purulia.
- **Yakshagana** is a folk dance-drama, not a classical dance.
- **Jatra** of Bengal is folk theatre, not a dance.

Setters swap these with classical names. Pin the state dance before you answer.

### Recognition to remember
- **Garba** entered UNESCO's ICH list in **2023**. It was India's newest dance element at that time.
- **Kalbelia, Chhau and Mudiyettu** all entered in **2010**.
- **Durga Puja of Kolkata** is a festival, not a dance. It entered the ICH list in **2021**.
""",
    tricks=[
        trick("North-East quick five",
              "Cheraw is Mizo. Hojagiri is Tripura. Nongkrem is Khasi (Meghalaya). Wangala is Garo (Meghalaya). Bagurumba is Bodo (Assam).",
              "Hojagiri, where women balance on an earthen pitcher, is a folk dance of which state?",
              ["The dancers are Reang women.", "They balance on pots and bottles."], "Tripura"),
        trick("Men and women in Punjab",
              "Bhangra goes with Bhaiya (men). Giddha goes with Girls (women)."),
    ],
    mistakes=[
        mis("Giving Yakshagana to Kerala.", "Yakshagana is the dance-drama of Karnataka. Kathakali is Kerala."),
        mis("Calling Chhau a purely classical dance.", "Chhau is semi-classical and martial, with three styles."),
        mis("Treating Jatra as a dance.", "Jatra is folk theatre of Bengal."),
        mis("Mixing up Cheraw and Hojagiri.", "Cheraw uses bamboo staves (Mizoram). Hojagiri uses balancing on pots (Tripura)."),
        mis("Saying Durga Puja is an ICH dance.", "Durga Puja of Kolkata is a festival, listed in 2021."),
    ],
    revision=[
        "Gujarat: Garba (ICH 2023) and Dandiya. Rajasthan: Ghoomar and Kalbelia (ICH 2010).",
        "Punjab: Bhangra (men) and Giddha (women). Maharashtra: Lavani, from tamasha. Karnataka: Yakshagana.",
        "Cheraw is Mizoram bamboo. Hojagiri is Tripura balancing. Nongkrem is Meghalaya Khasi.",
        "Theyyam is a Kerala ritual. Bihu is the Assam spring dance. Karma is the Chhattisgarh-Jharkhand dance.",
        "The 2010 ICH trio: Kalbelia, Chhau, Mudiyettu.",
    ],
    patterns=[
        pat("ga-fd-p1", "State to folk dance", "very common",
            "A folk dance with four state options, or a match-the-column of states and dances (often North-East).",
            ["Run the state table in your head.", "For the North-East, use the feature: bamboo, balancing, Khasi.", "Cross out the states that clearly do not fit."],
            "Each folk dance has one state, so recall settles it.",
            "The Cheraw dance, with bamboo staves, belongs to which state?",
            ["Cheraw is the bamboo dance.", "Dancers step in and out of clapped staves."],
            "Mizoram"),
        pat("ga-fd-p2", "Dance to feature or community", "common",
            "A feature is described, such as sticks, snake-like moves, dholki or goddess possession.",
            ["Read the feature.", "Map it: clapping circle is Garba, sticks are Dandiya, snake-charmers are Kalbelia.", "Dholki with tamasha is Lavani. Ritual possession is Theyyam."],
            "Each dance has one feature that acts as its label.",
            "The serpent-like Kalbelia dance is performed by a community traditionally of what?",
            ["Kalbelia is a Rajasthan dance.", "Its moves imitate a snake.", "The community is named after its old trade."],
            "Snake charmers"),
        pat("ga-fd-p3", "Dance to occasion or season", "common",
            "The question asks which dance goes with Baisakhi, Navratri or Bihu.",
            ["Recall the festival's dance.", "Baisakhi is Bhangra and Giddha.", "Navratri is Garba and Dandiya. Rongali Bihu is Bihu."],
            "Folk dances grew around harvests and festivals.",
            "Bhangra is traditionally performed during which festival?",
            ["Bhangra is a Punjab men's dance.", "It marks a harvest."],
            "Baisakhi, the Punjab harvest festival"),
        pat("ga-fd-p4", "Classical-folk border", "common",
            "Which of these is NOT a classical dance, or a semi-classical form slipped into a list.",
            ["Spot Chhau, Yakshagana or Jatra in the options.", "Chhau is semi-classical and martial.", "Yakshagana is folk dance-drama. Jatra is folk theatre."],
            "Setters pick forms that sound classical but are not.",
            "Which form is semi-classical and martial, with Mayurbhanj, Seraikella and Purulia styles?",
            ["Three styles in three states.", "It is not fully classical."],
            "Chhau"),
        pat("ga-fd-p5", "UNESCO recognition of dance forms", "occasional",
            "Which dance or form entered the ICH list, and in which year.",
            ["Recall Garba, 2023.", "Recall the 2010 trio: Kalbelia, Chhau, Mudiyettu.", "Recall that Durga Puja (2021) is a festival, not a dance."],
            "Year and name pairs are easy to test.",
            "Which Gujarat dance entered UNESCO's ICH list in 2023?",
            ["It is a circular dance of Navratri.", "Women clap as they move."],
            "Garba"),
    ],
)

# =====================================================================
# 3. Music and instruments
# =====================================================================
SUBS["music-instruments"] = dict(
    concept=(
        "India has two classical music systems. Hindustani music belongs to the north. Carnatic music belongs to the south. "
        "Exams ask which maestro plays which instrument, which class an instrument falls in, and who is the founder or master of each system."
    ),
    notes="""### Two systems of classical music
| System | Region | Key points |
|---|---|---|
| **Hindustani** | North | Persian influence; ragas tied to the time of day; forms are *dhrupad* (oldest), *khayal*, *thumri*, *tappa*; musicians belong to gharanas |
| **Carnatic** | South | *Kriti* compositions; fixed compositions |

- The **Trinity of Carnatic music** is **Tyagaraja, Muthuswami Dikshitar and Syama Sastri**. They lived in the 18th and 19th centuries in the Thiruvarur region of Tamil Nadu.
- **Purandara Dasa** is the "father" (Pitamaha) of Carnatic music. He is not part of the Trinity.
- The **Tyagaraja Aradhana** is held at **Thiruvaiyaru**.
- **Tansen**, at Akbar's court (one of the Navaratnas), is the fountainhead of Hindustani music.

> **Tip:** Pitamaha means Purandara Dasa. Trinity means Tyagaraja, Dikshitar, Syama Sastri.

### The four classes of instruments
The *Natya Shastra* sorts instruments by how they make sound.

| Class | Meaning | Examples |
|---|---|---|
| **Tata** (string) | Strings are vibrated | sitar, veena, sarod, santoor, violin |
| **Sushira** (wind) | Air column | bansuri (flute), shehnai, nadaswaram |
| **Avanaddha** (membrane) | Stretched skin is struck | tabla, mridangam, pakhawaj, dholak |
| **Ghana** (solid) | Solid body is struck | ghatam, kanjira, manjira, jal tarang, cymbals |

The santoor is a string instrument with 100 strings struck by mallets. The ghatam is a clay pot.

> **Rule:** Shehnai is wind. Santoor is string. Tabla is a drum. Ghatam is solid.

### Maestros and their instruments
| Instrument | Maestros |
|---|---|
| **Sitar** | Pt. Ravi Shankar, Vilayat Khan, Anoushka Shankar |
| Sarod | Ali Akbar Khan, Amjad Ali Khan |
| **Shehnai** | Ustad Bismillah Khan |
| **Tabla** | Zakir Hussain, Alla Rakha (Zakir's father), Kishan Maharaj |
| **Bansuri** | Pt. Hariprasad Chaurasia, Pannalal Ghosh |
| Santoor | Shivkumar Sharma, Rahul Sharma |
| Sarangi (bowed) | Pt. Ram Narayan, Sabri Khan |
| Violin | Lalgudi Jayaraman, L. Subramaniam (Carnatic); N. Rajam (Hindustani) |
| Mandolin | U. Srinivas |
| Mridangam | Palghat Mani Iyer, Umayalpuram Sivaraman |
| Veena (Saraswati) | E. Gayathri, S. Balachander |
| Mohan veena (slide guitar) | Pt. Vishwa Mohan Bhatt |

**Ustad Allauddin Khan** belonged to the Maihar gharana. He taught Ravi Shankar and Ali Akbar Khan.

### Musicians with the Bharat Ratna
- **M.S. Subbulakshmi** (1998) was the **first musician** to receive it. She was a Carnatic vocalist.
- **Pt. Ravi Shankar** (1999) played the sitar.
- **Lata Mangeshkar** (2001) and **Ustad Bismillah Khan** (2001, shehnai) followed.
- **Pt. Bhimsen Joshi** was a Hindustani vocalist of the Kirana gharana.
- **Bhupen Hazarika** received it in 2019, after his death.

> **Watch:** Bharat Ratna years vary across sources for Bhimsen Joshi. Trust the order and the first-musician fact.

### Gharanas
- **Gwalior** is the oldest khayal gharana.
- **Kirana** is Bhimsen Joshi's line, through Abdul Karim Khan.
- Others: Jaipur-Atrauli, Agra, Patiala (Bade Ghulam Ali Khan) and Banaras (tabla and thumri).
- Tabla gharanas: Lucknow, Farrukhabad, Banaras, Punjab and Delhi.
- Kathak gharanas: Lucknow, Jaipur and Banaras.

### The violin and the nadaswaram
The European violin joined Carnatic music around the 18th and 19th centuries. Baluswami Dikshitar, brother of Muthuswami, gets the credit. It is now a key accompaniment.

The **nadaswaram** is a wind instrument. It leads temple processions in the south, paired with the **thavil** drum.
""",
    tricks=[
        trick("Carnatic Trinity",
              "T for Tyagaraja, M for Muthuswami Dikshitar, S for Syama Sastri. Purandara Dasa is the father, not part of the Trinity.",
              "Who is called the Pitamaha of Carnatic music?",
              ["Pitamaha means father.", "The Trinity has three other names."], "Purandara Dasa"),
        trick("Instrument classes",
              "Tata is strings. Sushira is air, so wind. Avanaddha is skin drums. Ghana is solid, such as bells, cymbals and ghatam."),
    ],
    mistakes=[
        mis("Naming Purandara Dasa as one of the Trinity.", "The Trinity is Tyagaraja, Muthuswami Dikshitar and Syama Sastri. Purandara Dasa is the father."),
        mis("Calling the shehnai a string instrument.", "The shehnai is a wind (sushira) instrument."),
        mis("Calling the santoor a wind instrument.", "The santoor is a string instrument struck with mallets."),
        mis("Giving Zakir Hussain the sarod.", "Zakir Hussain plays the tabla. Sarod belongs to Ali Akbar Khan and Amjad Ali Khan."),
        mis("Naming Ravi Shankar as the first musician with the Bharat Ratna.", "M.S. Subbulakshmi (1998) came first. Ravi Shankar followed in 1999."),
    ],
    revision=[
        "Purandara Dasa is the Carnatic Pitamaha. The Trinity is Tyagaraja, Dikshitar and Syama Sastri.",
        "Classes: tata (string), sushira (wind), avanaddha (drum), ghana (solid).",
        "Bismillah Khan: shehnai. Ravi Shankar: sitar. Zakir Hussain: tabla.",
        "Shivkumar Sharma: santoor. Chaurasia: bansuri. Vishwa Mohan Bhatt: Mohan veena.",
        "M.S. Subbulakshmi was the first musician with the Bharat Ratna (1998).",
        "Gwalior is the oldest gharana. Allauddin Khan belonged to Maihar.",
    ],
    patterns=[
        pat("ga-mu-p1", "Instrument to class", "common",
            "How is the shehnai classified, or find the odd one out among wind, string and drum instruments.",
            ["Recall the four classes.", "Flute, shehnai, nadaswaram are wind.", "Tabla, mridangam are drums. Ghatam, kanjira are solid. Sitar, sarod, santoor are strings."],
            "The class depends on how the sound is made.",
            "The shehnai is classified as which type of instrument?",
            ["Sound comes from a vibrating air column.", "That is the sushira class."],
            "Wind instrument (sushira)"),
        pat("ga-mu-p2", "Maestro to instrument", "very common",
            "A musician's name comes with four instrument options.",
            ["Recall the one-to-one pairs.", "Bismillah Khan is shehnai. Ravi Shankar is sitar. Zakir Hussain is tabla.", "Shivkumar Sharma is santoor. Chaurasia is flute."],
            "One instrument per maestro settles the question.",
            "Ustad Zakir Hussain is a virtuoso of which instrument?",
            ["He is the son of Ustad Allah Rakha.", "Allah Rakha was a tabla legend."],
            "Tabla"),
        pat("ga-mu-p3", "Hindustani versus Carnatic", "very common",
            "Father of Carnatic music, the Carnatic Trinity, Tansen's court, or a statement pair about the two systems.",
            ["North is Hindustani: dhrupad, khayal, gharanas, Tansen.", "South is Carnatic: kriti, Trinity, Purandara Dasa.", "Pitamaha means Purandara Dasa."],
            "Each system has its own names and forms.",
            "Who make up the Carnatic Trinity?",
            ["All three lived in the Thiruvarur region.", "Names: Tyagaraja, Dikshitar, Syama Sastri."],
            "Tyagaraja, Muthuswami Dikshitar and Syama Sastri"),
        pat("ga-mu-p4", "Bharat Ratna musicians and gharanas", "common",
            "First musician with the Bharat Ratna, a singer's gharana, or the oldest gharana.",
            ["Recall the order: M.S. Subbulakshmi 1998, Ravi Shankar 1999, then Lata Mangeshkar and Bismillah Khan 2001.", "Gwalior is the oldest khayal gharana.", "Maihar is Allauddin Khan's school."],
            "The first-musician fact is the favourite question.",
            "Who was the first musician to receive the Bharat Ratna?",
            ["She was a Carnatic vocalist.", "The year was 1998."],
            "M.S. Subbulakshmi"),
        pat("ga-mu-p5", "Teacher and gharana", "occasional",
            "Who taught Ravi Shankar, which gharana a singer belongs to, or the gharana of Bhimsen Joshi.",
            ["Recall Allauddin Khan of Maihar as the teacher of Ravi Shankar and Ali Akbar Khan.", "Bhimsen Joshi is Kirana.", "Bade Ghulam Ali Khan is Patiala."],
            "Teacher-student lines link gharanas and maestros.",
            "Bhimsen Joshi belongs to which gharana?",
            ["He was a Hindustani vocalist.", "His line goes back to Abdul Karim Khan."],
            "Kirana gharana"),
    ],
)

# =====================================================================
# 4. Paintings, textiles, crafts
# =====================================================================
SUBS["paintings-crafts"] = dict(
    concept=(
        "This subtopic pairs an art with a place. A folk painting belongs to a state. A craft or textile belongs to a town. "
        "The exam also asks about the miniature schools and a few famous painters. "
        "Learn each pair with one feature word."
    ),
    notes="""### Folk and tribal paintings
| Painting | State | Hallmark |
|---|---|---|
| **Madhubani (Mithila)** | Bihar | Women's wall art; double-line borders; GI tag |
| **Warli** | Maharashtra | White rice-paste stick figures on mud walls |
| **Pattachitra** | Odisha (also West Bengal) | Cloth or palm-leaf scrolls; Jagannath themes |
| **Phad** | Rajasthan | Long cloth scrolls of Pabuji and Devnarayan |
| **Kalamkari** | Andhra Pradesh / Telangana | "Pen-work" on cloth: Srikalahasti (hand-drawn), Machilipatnam (block) |
| **Gond** | Madhya Pradesh | Tribal dots and dashes; Jangarh Singh Shyam |
| Pithora | Gujarat / MP | Rathwa and Bhil ritual walls |
| Kalighat | West Bengal | 19th-century Kolkata bazaar painting |
| **Tanjore** | Tamil Nadu | Gold foil and gems |
| Mysore | Karnataka | Gesso work and gold |
| **Cheriyal** | Telangana | Bright story scrolls |
| Saura | Odisha | Tribal wall art (*idital*) |
| **Thangka** | Sikkim, Ladakh, Arunachal | Buddhist cloth scrolls used in worship |
| **Pichwai** | Rajasthan (Nathdwara) | Backdrops of Srinathji (Krishna) |

> **Tip:** Kalamkari means pen-work, because *kalam* is a pen. Andhra Pradesh holds the pen.

### Miniature schools and painters
- **Mughal** painting began under **Akbar** with the *Hamzanama* workshops. It peaked under **Jahangir**, in portraits and naturalism. Akbar's atelier had Mir Sayyid Ali and Abdus Samad.
- **Rajasthani** schools include Kishangarh (the Bani Thani style), Mewar and Bundi.
- **Pahari** schools grew in the Himalayan foothills. **Kangra** is the best known, with Radha-Krishna themes. Basohli is also Pahari.
- **Company paintings** (late 18th to 19th century) were made for British patrons.
- The **Bengal School** was led by **Abanindranath Tagore**, whose *Bharat Mata* dates from 1905. E.B. Havell backed it and **Nandalal Bose** carried it on. It answered Western academic style with an Asian idiom.
- **Raja Ravi Varma** of Kerala painted in oils. He blended European realism with Indian subjects and spread them through mass lithographs.

### Crafts and textiles by place
| Craft | Place |
|---|---|
| **Bidriware** (silver inlay on blackened metal) | Bidar, Karnataka |
| Chikankari (shadow embroidery) | Lucknow, UP |
| Phulkari (flower work) | Punjab |
| Kantha (running stitch) | West Bengal |
| Bandhani / Bandhej (tie-dye) | Gujarat and Rajasthan |
| **Patola** (double ikat silk) | Patan, Gujarat |
| Pochampally ikat | Telangana |
| Kanjeevaram silk | Kanchipuram, Tamil Nadu |
| Banarasi brocade | Varanasi, UP |
| Chanderi and Maheshwari | Madhya Pradesh |
| Paithani | Maharashtra |
| **Muga silk** (golden) | Assam |
| Pashmina | Jammu & Kashmir |
| Blue pottery | Jaipur, Rajasthan |
| Channapatna lacquer toys | Karnataka |
| Brass ware | Moradabad, UP |

> **Rule:** Many crafts are named after their town. Bidriware comes from Bidar. Patola comes from Patan.

### Memory hooks
- Women's wall art from Mithila is Madhubani (Bihar).
- White figures on mud is Warli.
- A Jagannath scroll is Pattachitra.
- Silver on black is Bidri.
- Tie-dye is Bandhani.
- A Nathdwara backdrop is Pichwai.
""",
    tricks=[
        trick("Kalam, Patta, Phad",
              "Kalamkari is Andhra (the pen, kalam). Pattachitra is Odisha (cloth, patta). Phad is Rajasthan (Pabuji scroll). Madhubani is Bihar (Mithila).",
              "Kalamkari art is chiefly linked with which state?",
              ["Kalam means pen.", "Its centres are Srikalahasti and Machilipatnam."], "Andhra Pradesh"),
        trick("Bidri is Bidar",
              "The craft carries its town's name. Bidriware comes from Bidar (Karnataka). Patola comes from Patan. Chanderi comes from Chanderi."),
    ],
    mistakes=[
        mis("Giving Warli to Bihar because it also uses wall art.", "Warli is Maharashtra. Bihar's wall art is Madhubani."),
        mis("Putting Pattachitra in Rajasthan.", "Pattachitra is Odisha (also West Bengal). Rajasthan has Phad."),
        mis("Placing Bidriware in Bihar.", "Bidriware comes from Bidar, Karnataka."),
        mis("Saying Jahangir founded Mughal painting.", "Akbar founded it (Hamzanama). Jahangir's reign was its peak."),
        mis("Placing Pochampally ikat in Tamil Nadu.", "Pochampally is Telangana. Kanjeevaram silk is Tamil Nadu."),
    ],
    revision=[
        "Madhubani is Bihar. Warli is Maharashtra. Pattachitra is Odisha. Phad is Rajasthan. Gond is MP. Thangka is Ladakh.",
        "Mughal: Akbar founded it (Hamzanama). Jahangir was the peak. Kangra is the Pahari gem.",
        "Bengal School: Abanindranath Tagore (Bharat Mata, 1905) and Nandalal Bose.",
        "Raja Ravi Varma: oil paintings and lithographs.",
        "Bidri is Bidar. Chikankari is Lucknow. Phulkari is Punjab. Pochampally is Telangana.",
    ],
    patterns=[
        pat("ga-pa-p1", "Painting to state", "very common",
            "A folk painting such as Madhubani, Warli, Pattachitra or Phad with four states, or a match-the-column.",
            ["Fix the big five: Madhubani Bihar, Warli Maharashtra, Pattachitra Odisha, Phad Rajasthan, Gond MP.", "Thangka points to the Buddhist Himalaya (Ladakh or Sikkim).", "Cross out the rest."],
            "Each painting has one home state.",
            "Madhubani (Mithila) painting is native to which state?",
            ["Mithila is a region.", "It is traditionally women's wall art."],
            "Bihar"),
        pat("ga-pa-p2", "Craft to place or GI tag", "very common",
            "A craft such as Bidriware, Chikankari, Pochampally or Channapatna with a place question.",
            ["Recall the craft table.", "Many crafts take their town's name.", "Cross out places that do not fit."],
            "Craft and town pairs are direct recall.",
            "Bidriware, with silver inlay on blackened metal, comes from which place?",
            ["The craft is named after a town.", "The town is in Karnataka."],
            "Bidar, Karnataka"),
        pat("ga-pa-p3", "Painting to feature or theme", "common",
            "A hallmark is described: white stick figures, Jagannath scrolls, Pabuji epic cloth, or pen-work cotton.",
            ["Read the hallmark.", "White rice-paste figures are Warli.", "Jagannath scrolls are Pattachitra. Pabuji cloth is Phad. Pen-work is Kalamkari. A Srinathji backdrop is Pichwai."],
            "Each painting has one signature feature.",
            "White rice-paste stick figures on mud walls identify which painting?",
            ["They are on mud walls.", "The state is Maharashtra."],
            "Warli"),
        pat("ga-pa-p4", "Miniature schools and painters", "common",
            "Mughal painting under which emperor, the Kangra school, Bengal School painters, or Ravi Varma's medium.",
            ["Mughal: Akbar founds it, Jahangir peaks.", "Pahari: Kangra.", "Bengal School: Abanindranath Tagore and Nandalal Bose. Ravi Varma: oil and lithography."],
            "Each school has one or two names to recall.",
            "The Hamzanama series of paintings was produced under which ruler?",
            ["It was a workshop project.", "It began Mughal painting."],
            "Akbar"),
        pat("ga-pa-p5", "Textile to place", "common",
            "A cloth or embroidery with a place question, such as Phulkari, Patola, Kantha or Muga.",
            ["Recall the textile pairs.", "Phulkari is Punjab. Patola is Patan. Muga is Assam.", "Kantha is West Bengal. Paithani is Maharashtra."],
            "Textile names point to their home towns or states.",
            "Muga silk, known for its golden colour, comes from which state?",
            ["It is a golden silk.", "The state is in the North-East."],
            "Assam"),
    ],
)

# =====================================================================
# 5. Architecture
# =====================================================================
SUBS["architecture"] = dict(
    concept=(
        "Indian temples follow three styles: Nagara in the north, Dravida in the south and Vesara in the Deccan. "
        "Each style has its own tower and layout. "
        "The exam also asks who built a famous monument, which caves belong to which faith, and what a temple part is called."
    ),
    notes="""### The three temple styles
| Style | Region | Hallmarks | Examples |
|---|---|---|---|
| **Nagara** | North | Curvilinear *shikhara* over the sanctum; *amalaka* on top; no boundary wall | Khajuraho (Chandela), Lingaraja (Bhubaneswar), Konark, Modhera Sun Temple |
| **Dravida** | South | Pyramidal *vimana*; huge *gopuram* gateways; enclosure wall; temple tank | Brihadeeswara (Thanjavur), Meenakshi (Madurai), Srirangam, Mahabalipuram |
| **Vesara** | Deccan (Karnataka) | Mix of Nagara and Dravida; star-shaped plans | Chalukya (Pattadakal, Badami); Hoysala (Belur, Halebidu, Somanathapura) |

> **Tip:** Curved shikhara means north. Gopuram means south. Star plan in Karnataka means Vesara.

### Parts of a temple
- **Shikhara:** the curving tower of the north.
- **Vimana:** the pyramidal tower above the sanctum in the south.
- **Gopuram:** the tall gateway of a southern temple.
- **Mandapa:** a pillared hall.
- **Amalaka:** the ribbed stone cap on a northern shikhara.
- **Chaitya:** a Buddhist prayer hall.
- **Vihara:** a Buddhist monastery. Karle has a chaitya. Ajanta has viharas.

> **Watch:** The gopuram is a gateway. The tower above the sanctum is the vimana.

### Monument and builder
| Monument | Builder and period |
|---|---|
| Brihadeeswara, Thanjavur | Rajaraja I, Chola (c. 1010 CE) |
| Gangaikonda Cholapuram | Rajendra I, Chola |
| **Sun Temple, Konark** | Narasimhadeva I, Eastern Ganga (13th century) |
| Sun Temple, Modhera | Bhima I, Solanki (Chaulukya) |
| Kailasa temple, Ellora | Krishna I, Rashtrakuta |
| Chennakesava, Belur | Vishnuvardhana, Hoysala (1117) |
| Hoysaleswara, Halebidu | Hoysala kings |
| Kesava, Somanathapura | Hoysala, Narasimha III's reign (1268) |
| Dilwara Jain temples, Mt Abu | Solanki period (Vimal Shah's Vimal Vasahi) |
| Meenakshi, Madurai | Nayak rulers (gopurams restored and expanded) |
| Mahabalipuram rathas, Shore Temple | Pallavas: Narasimhavarman I (Mamalla), Rajasimha |

### Odisha temples
- **Konark Sun Temple** is a chariot with 24 wheels. It is called the "Black Pagoda". UNESCO listed it in 1984.
- **Jagannath Temple, Puri** was built by Anantavarman Chodaganga. It is the "White Pagoda".
- **Lingaraja** stands at Bhubaneswar.

### Rock-cut caves
| Site | State | Faith and feature |
|---|---|---|
| **Bhimbetka** | Madhya Pradesh | Prehistoric rock shelters and paintings (UNESCO 2003) |
| **Ajanta** | Maharashtra | Buddhist; 29-30 caves; murals such as Padmapani |
| **Ellora** | Maharashtra | 34 caves: Buddhist, Hindu and Jain |
| Elephanta | Maharashtra | Shaiva; Trimurti (Maheshmurti) sculpture |
| Udayagiri-Khandagiri | Odisha | Jain caves (Kharavela) |
| Barabar | Bihar | Oldest rock-cut caves (Mauryan, Ajivikas) |

Ajanta was painted in two phases, Satavahana (c. 2nd century BCE) and Vakataka (5th century CE). The Kailasa temple at Ellora was carved top-down from one rock. Mahabalipuram has Pallava monolithic rathas.

### Colonial and Indo-Saracenic
- Victoria Memorial, Kolkata.
- Gateway of India, Mumbai (1924).
- Chhatrapati Shivaji Maharaj Terminus, Mumbai (UNESCO 2004, Gothic Revival).
""",
    tricks=[
        trick("Shikhara North, Gopuram South",
              "A gopuram means Dravida. A curved shikhara means Nagara. A star-shaped Hoysala plan means Vesara (Deccan).",
              "The towering gateway called a gopuram is a feature of which style?",
              ["Gopuram is a southern gateway.", "The southern style is Dravida."], "Dravida"),
        trick("Odisha pagodas",
              "Black Pagoda is Konark (dark stone, Sun temple). White Pagoda is Puri (whitewashed Jagannath)."),
    ],
    mistakes=[
        mis("Saying vimana is the gateway tower.", "The vimana is the tower above the sanctum. The gateway is the gopuram."),
        mis("Placing Hoysala temples in Dravida.", "Hoysala temples are Vesara, in Karnataka."),
        mis("Crediting Konark to Rajaraja I.", "Konark is Narasimhadeva I (Eastern Ganga). Rajaraja I built Brihadeeswara."),
        mis("Calling Ellora only Buddhist.", "Ellora has Buddhist, Hindu and Jain caves."),
        mis("Swapping Black and White Pagoda.", "Konark is the Black Pagoda. Puri is the White Pagoda."),
    ],
    revision=[
        "Nagara has a shikhara (north). Dravida has a vimana and gopuram (south). Vesara is a mix (Deccan).",
        "Konark is Narasimhadeva I. Brihadeeswara is Rajaraja I. Modhera is Bhima I.",
        "Kailasa at Ellora is Krishna I, Rashtrakuta, carved top-down.",
        "Belur, Halebidu, Somanathapura are Hoysala. Pattadakal is Chalukya (UNESCO 1987).",
        "Ajanta has Buddhist murals. Chaitya is a hall. Vihara is a monastery.",
    ],
    patterns=[
        pat("ga-ar-p1", "Style to region or feature", "very common",
            "Which style has gopurams, or a pairing of style and region.",
            ["Recall: Nagara is north with a shikhara.", "Dravida is south with a vimana and gopuram.", "Vesara is Deccan and mixed."],
            "Each style has one tower or gate that names it.",
            "The shikhara is the hallmark of which temple style?",
            ["Shikhara is a curvilinear tower.", "It is topped with an amalaka."],
            "Nagara, the north Indian style"),
        pat("ga-ar-p2", "Monument to builder or dynasty", "very common",
            "Who built the Sun Temple at Konark or Brihadeeswara, or a match-the-column of temples and builders.",
            ["Recall six pairs: Konark, Brihadeeswara, Modhera, Kailasa, Belur, Mahabalipuram.", "Match each to its king.", "Cross out the wrong dynasty."],
            "Six pairs settle most of these questions.",
            "The Kailasa temple at Ellora was carved under which king?",
            ["It is a rock-cut temple.", "It was cut top-down from a single rock.", "The dynasty was Rashtrakuta."],
            "Krishna I"),
        pat("ga-ar-p3", "Caves to period or religion", "common",
            "Ajanta versus Ellora statements, the faith mix at Ellora, or Elephanta's deity.",
            ["Ajanta is Buddhist and painted.", "Ellora is Buddhist, Hindu and Jain.", "Elephanta is Shiva (Maheshmurti). Mahabalipuram is Pallava."],
            "Each cave site has one defining fact.",
            "Which statement about Ellora is correct?",
            ["Ellora has 34 caves.", "Three faiths used them."],
            "Its caves serve Buddhist, Hindu and Jain worship"),
        pat("ga-ar-p4", "Part or feature to name", "common",
            "Definitions in disguise: what is a vimana, gopuram, mandapa, chaitya, vihara or amalaka.",
            ["Read the definition.", "Match: tower above the sanctum is vimana; gateway tower is gopuram; pillared hall is mandapa.", "Prayer hall is chaitya; monastery is vihara."],
            "The words are fixed, so recall settles it.",
            "In south Indian temples, what is the tower above the sanctum called?",
            ["The gateway tower is the gopuram.", "The sanctum tower is another word."],
            "Vimana"),
        pat("ga-ar-p5", "Odisha temples", "occasional",
            "Black Pagoda or White Pagoda, or who built the Jagannath temple at Puri.",
            ["Konark is the Black Pagoda.", "Puri is the White Pagoda.", "Puri was built by Anantavarman Chodaganga."],
            "The two pagoda names are the usual trap.",
            "The Jagannath Temple at Puri is known as which pagoda?",
            ["Its stone is whitewashed.", "Konark is the other pagoda."],
            "White Pagoda"),
    ],
)

# =====================================================================
# 6. Festivals and fairs
# =====================================================================
SUBS["festivals-fairs"] = dict(
    concept=(
        "Most festival questions pair a festival with its state. Others ask about fairs, harvest seasons or India's UNESCO cultural elements. "
        "Learn each festival with one feature word. "
        "Then learn the Kumbh cities and the year ladder of UNESCO entries."
    ),
    notes="""### Festival and state
| Festival | State | Note |
|---|---|---|
| **Onam** | Kerala | Harvest; King Mahabali; Vallam Kali (snake-boat race); pookalam |
| **Pongal** | Tamil Nadu | Mid-January harvest; four days; Jallikattu |
| Makar Sankranti / Lohri | Many / Punjab | Lohri is the night before Sankranti |
| **Baisakhi** | Punjab | April harvest; Khalsa founded (1699) |
| **Bihu** | Assam | Rongali (spring) is the famous one |
| **Durga Puja** | West Bengal | UNESCO ICH 2021 |
| **Ganesh Chaturthi** | Maharashtra | Public utsav (Tilak's mobilisation) |
| **Chhath** | Bihar / Jharkhand | Sun worship at rivers, Kartik Shukla Shashthi |
| **Hornbill** | Nagaland | 1-10 December, Kisama; "festival of festivals" |
| Sangai | Manipur | Named after the brow-antlered deer |
| Chapchar Kut | Mizoram | Spring, after jhum clearing |
| **Wangala** | Meghalaya | Garo harvest ("100 drums") |
| **Losar** | Ladakh, Sikkim, Arunachal | Tibetan New Year |
| **Hemis** | Ladakh | Birth of Guru Padmasambhava; masked Cham dance |
| Ugadi | Andhra, Telangana, Karnataka | New Year |
| Gudi Padwa | Maharashtra | New Year |
| **Bonalu, Bathukamma** | Telangana | Mahakali / floral festival |
| Nuakhai | Odisha | New rice |
| Thrissur Pooram | Kerala | Elephant pageant |
| Hareli | Chhattisgarh | First festival of the farming year |
| Kharchi Puja | Tripura | Fourteen deities |
| Moatsu / Sekrenyi | Nagaland | Ao / Angami festivals |
| **Sarhul** | Jharkhand | Tribal spring festival of the sal tree |

> **Tip:** Hornbill runs 1-10 December in Nagaland. December is when Nagaland's year closes.

### Fairs (melas)
- **Kumbh Mela** rotates among **Prayagraj, Haridwar, Ujjain and Nashik**. UNESCO listed it in 2017.
- **Pushkar** (Rajasthan) is a camel and livestock fair on Kartik Purnima. It is held at the only Brahma temple.
- **Sonepur Mela** (Bihar) is among Asia's largest cattle fairs. It is at the Gandak-Ganga confluence.
- **Ambubachi Mela** is at Kamakhya, Assam.
- **Rath Yatra** is at Puri.
- Suraj Kund Crafts Mela is in Haryana.
- Nauchandi is at Meerut, UP.

> **Watch:** Varanasi, Ayodhya and Mathura are decoys. They do not host the Kumbh.

### Season logic
Most festivals follow the harvest.

- Pongal falls in mid-January (Tamil Thai month).
- Baisakhi falls in mid-April, and so does Bihu.
- Onam falls in August-September (Chingam).
- Wangala falls in autumn.

The mid-January run goes Lohri, then Makar Sankranti, then Pongal, then Bihu within a day or two.

### UNESCO cultural elements of India
| Year | Element |
|---|---|
| 2001 | Kutiyattam, Sanskrit theatre (the first) |
| 2008 | Ramlila; Vedic chanting |
| 2009 | Ramman (Garhwal, festival-theatre) |
| 2010 | Chhau, Kalbelia, Mudiyettu |
| 2013 | Sankirtana of Manipur |
| 2016 | Yoga |
| 2017 | Kumbh Mela |
| 2021 | Durga Puja in Kolkata |
| 2023 | Garba of Gujarat |

> **Note:** Kutiyattam was proclaimed in 2001. It moved to the ICH list in 2008.

### Two questions that repeat
1. Which city does not host the Kumbh? The four are Prayagraj, Haridwar, Ujjain and Nashik.
2. Which dance belongs to which festival? Garba with Navratri, Bhangra with Baisakhi, Bihu with Rongali Bihu, Jallikattu with Pongal, Vallam Kali with Onam.
""",
    tricks=[
        trick("Hornbill closes the year",
              "The Hornbill Festival runs 1-10 December. Nagaland Statehood Day is 1 December.",
              "The Hornbill Festival is held every year in which state?",
              ["The site is Kisama Heritage Village.", "The dates are 1-10 December."], "Nagaland"),
        trick("Two cattle fairs",
              "Pushkar is in Rajasthan, the Pink City state, for camels. Sonepur is in Bihar, for cattle and elephants."),
    ],
    mistakes=[
        mis("Placing Chhath in Punjab.", "Chhath is Bihar (and Jharkhand): sun worship at rivers."),
        mis("Adding Varanasi to the Kumbh cities.", "The four are Prayagraj, Haridwar, Ujjain and Nashik."),
        mis("Giving Onam to Tamil Nadu.", "Onam is Kerala. Pongal is Tamil Nadu."),
        mis("Placing Pushkar fair in Bihar.", "Pushkar is Rajasthan (camels). Sonepur is Bihar (cattle)."),
        mis("Saying Bihu is celebrated in Bihar.", "Bihu is Assam. Bihar has Chhath."),
    ],
    revision=[
        "Onam is Kerala (Mahabali, Vallam Kali). Pongal is Tamil Nadu (January). Baisakhi is Punjab (Khalsa 1699).",
        "Chhath is Bihar sun worship. Hornbill is Nagaland, December. Losar is the Ladakh new year.",
        "Kumbh cities: Prayagraj, Haridwar, Ujjain, Nashik. Pushkar is a camel fair. Sonepur is a Bihar cattle fair.",
        "UNESCO ladder: Kutiyattam 2001, Ramlila and Vedic chanting 2008, Chhau-Kalbelia-Mudiyettu 2010, Sankirtana 2013.",
        "Then Yoga 2016, Kumbh 2017, Durga Puja 2021, Garba 2023.",
    ],
    patterns=[
        pat("ga-fe-p1", "Festival to state", "very common",
            "A festival with four state options: Onam, Pongal, Chhath, Hornbill, Bihu and others.",
            ["Recall the one-to-one pairs.", "Onam Kerala, Pongal TN, Chhath Bihar, Hornbill Nagaland, Bihu Assam.", "Durga Puja WB, Losar Ladakh, Wangala Meghalaya, Sarhul Jharkhand."],
            "Each festival has one home state.",
            "The sun-worship festival Chhath is most identified with which state?",
            ["Offerings go to Surya.", "They are made at river ghats."],
            "Bihar"),
        pat("ga-fe-p2", "Fair to place", "common",
            "Pushkar, Sonepur, Kumbh locations, or which fair is famous for camels or cattle.",
            ["Kumbh rotates: Prayagraj, Haridwar, Ujjain, Nashik.", "Pushkar is camels in Rajasthan.", "Sonepur is cattle in Bihar."],
            "Each fair has one place and one animal or purpose.",
            "The Pushkar fair, famous for camel trading, is held in which state?",
            ["It happens around Kartik Purnima.", "It is at the town of the Brahma temple."],
            "Rajasthan"),
        pat("ga-fe-p3", "Festival to season or harvest", "common",
            "Which festival falls in January or April, harvest clusters, or the order of Lohri, Sankranti and Pongal.",
            ["Place Lohri first, the night before Sankranti.", "Then Makar Sankranti, which is Pongal in Tamil Nadu.", "April harvest: Baisakhi and Bihu."],
            "Harvest time sets the date of most festivals.",
            "Which festival falls immediately after Lohri in mid-January?",
            ["Lohri is the night before.", "Tamil Nadu celebrates it as Pongal."],
            "Makar Sankranti"),
        pat("ga-fe-p4", "UNESCO ICH elements", "common",
            "Which Indian element entered the ICH list in a given year, or matching elements to years.",
            ["Keep the ladder in order.", "Kutiyattam 2001, then 2008, 2010, 2013, 2016, 2017, 2021, 2023.", "Match the element to its year."],
            "The ladder gives every year in one string.",
            "Which was the first Indian element on UNESCO's ICH list?",
            ["It is Sanskrit theatre.", "It comes from Kerala."],
            "Kutiyattam (2001)"),
        pat("ga-fe-p5", "Kumbh city trap", "common",
            "Which city does NOT host the Kumbh Mela, or which city hosts it.",
            ["List the four: Prayagraj, Haridwar, Ujjain, Nashik.", "Spot the decoy: Varanasi, Ayodhya or Mathura.", "Choose the decoy."],
            "The decoy cities sound sacred, so students choose them.",
            "Which of these does not host the Kumbh Mela: Ujjain, Nashik, Varanasi, Haridwar?",
            ["Ujjain is a host.", "Nashik and Haridwar are hosts.", "Varanasi is not."],
            "Varanasi"),
        pat("ga-fe-p6", "Festival to dance or activity", "occasional",
            "Which dance or event belongs to which festival.",
            ["Recall the pairs.", "Garba goes with Navratri, Bhangra with Baisakhi.", "Jallikattu goes with Pongal. Vallam Kali goes with Onam."],
            "Pair the two and half the festival questions answer themselves.",
            "Vallam Kali, the snake-boat race, goes with which festival?",
            ["It is a boat race.", "It happens in Kerala at harvest."],
            "Onam"),
    ],
)

# =====================================================================
# 7. UNESCO heritage and institutions
# =====================================================================
SUBS["unesco-institutions"] = dict(
    concept=(
        "India has 45 World Heritage Sites as of September 2026. Most are cultural. Only a few are natural, and one is mixed. "
        "Questions ask for the state and year of recent sites and for the founding year of cultural bodies. "
        "Learn each site as three facts: site, state and year."
    ),
    notes="""### India's World Heritage Sites
India holds **45 sites**: 37 cultural, 7 natural and 1 mixed. The mixed site is **Khangchendzonga National Park**, Sikkim (2016).

The first batch came in **1983**: Taj Mahal, Agra Fort, Ajanta and Ellora.

Ahmedabad became India's first heritage city in 2017. Jaipur followed in 2019.

### Recent inscriptions
| No. | Site | State | Year |
|---|---|---|---|
| 39 | Ramappa (Rudreswara) Temple | Telangana | 2021 |
| 40 | Dholavira | Gujarat | 2021 |
| 41 | **Santiniketan** | West Bengal | 2023 |
| 42 | **Sacred Ensembles of the Hoysalas** (Belur, Halebidu, Somnathapura) | Karnataka | 2023 |
| 43 | **Moidams of Charaideo** (Ahom mound burials) | Assam | 2024 |
| 44 | Maratha Military Landscapes (12 forts) | Maharashtra | 2025 |
| 45 | Ancient Buddhist Site of **Sarnath** | Uttar Pradesh | 2026 |

> **Tip:** Count by year. 2021 gives 40. 2023 gives 42. 2024 gives 43. 2025 gives 44. 2026 gives 45.

### Natural and mixed sites
- **Natural:** Kaziranga, Manas, Keoladeo, Sundarbans, Nanda Devi, Western Ghats and Great Himalayan National Park.
- **Mixed:** only Khangchendzonga.
- Everything else is cultural.

> **Rule:** Only one mixed site exists. It is Khangchendzonga.

### Intangible Cultural Heritage elements
India has 16 elements on UNESCO's ICH list.

| Year | Elements |
|---|---|
| 2008 | Koodiyattam (Sanskrit theatre, Kerala), Ramlila, Vedic chanting |
| 2009 | Ramman (religious festival, Garhwal, Uttarakhand) |
| 2010 | Mudiyettu (Kerala), Kalbelia (Rajasthan), Chhau |
| 2012 | Buddhist chanting of Ladakh |
| 2013 | Sankirtana of Manipur |
| 2014 | Brass and copper craft of the Thatheras of Jandiala Guru (Punjab) |
| 2016 | Yoga; Nowruz (multinational) |
| 2017 | Kumbh Mela |
| 2021 | Durga Puja in Kolkata |
| 2023 | Garba of Gujarat |
| 2025 | Deepavali (the 16th) |

Koodiyattam was proclaimed in 2001 and moved to the ICH list in 2008. Some lists therefore give 2001 as the first.

### Cultural institutions
| Body | Set up | Note |
|---|---|---|
| **Archaeological Survey of India** | 1861 | Custodian of monuments; Alexander Cunningham was the first Director-General |
| **Sangeet Natak Akademi** | 1953 | Music, dance, drama; New Delhi |
| **Sahitya Akademi** | 1954 | Literature; awards in 24 languages |
| **Lalit Kala Akademi** | 1954 | Visual arts |
| National School of Drama | 1959 | New Delhi |
| **FTII** | 1960 | Film and Television Institute of India, Pune |
| **INTACH** | 1984 | Indian National Trust for Art and Cultural Heritage |
| **IGNCA** | 1987 | Indira Gandhi National Centre for the Arts, New Delhi |
| Kalakshetra | 1936 | Rukmini Devi Arundale, Chennai |
| Kerala Kalamandalam | 1930 | Vallathol Narayana Menon |

The three Akademis are the national academies of the 1950s. Sangeet Natak came first, then Sahitya and Lalit Kala together.

### How the questions are built
Most World Heritage questions test one of three things.

- **The state:** Ramappa is Telangana. Dholavira is Gujarat. Santiniketan is Bengal. The Hoysalas are Karnataka. The Moidams are Assam.
- **The year:** the 2021 pair and the 2023 pair.
- **The type:** mixed is Khangchendzonga. Natural is the wildlife set.

Institution questions test the year and the art. Performing arts is 1953. Literature and fine arts are 1954. Films are 1960. Archaeology is 1861.
""",
    tricks=[
        trick("WHS count ladder",
              "2021 gives 40 (Dholavira). 2023 gives 42 (Hoysala). 2024 gives 43 (Moidams). 2025 gives 44 (Maratha forts). 2026 gives 45 (Sarnath).",
              "The Moidams of Charaideo belong to which state?",
              ["They are Ahom mound burials.", "The Ahom kingdom was in the North-East."], "Assam (inscribed 2024)"),
        trick("Three Akademis",
              "Sangeet Natak comes first (1953). Sahitya and Lalit Kala come together in 1954."),
    ],
    mistakes=[
        mis("Saying India has more than one mixed site.", "Only Khangchendzonga is mixed."),
        mis("Placing Dholavira in Rajasthan.", "Dholavira is in Gujarat."),
        mis("Placing Ramappa in Karnataka.", "Ramappa (Rudreswara) Temple is in Telangana."),
        mis("Mixing the 2021 and 2023 pairs.", "2021 is Ramappa and Dholavira. 2023 is Santiniketan and the Hoysala Ensembles."),
        mis("Saying Sahitya Akademi came before Sangeet Natak.", "Sangeet Natak is 1953. Sahitya and Lalit Kala are 1954."),
    ],
    revision=[
        "45 sites = 37 cultural + 7 natural + 1 mixed (Khangchendzonga).",
        "The first four (1983): Taj Mahal, Agra Fort, Ajanta, Ellora.",
        "2021: Ramappa (Telangana), Dholavira (Gujarat). 2023: Santiniketan, Hoysalas.",
        "ASI 1861 with Cunningham. Sangeet Natak 1953. Sahitya and Lalit Kala 1954. FTII 1960, Pune.",
        "Ahmedabad is the first heritage city (2017). Jaipur followed in 2019.",
    ],
    patterns=[
        pat("ga-un-p1", "Site to state or year", "very common",
            "Ramappa temple is in which state, Dholavira is in which state, or the year of a recent site.",
            ["Recall the triple: site, state, year.", "Ramappa and Dholavira are 2021.", "Santiniketan and Hoysalas are 2023. Moidams are 2024."],
            "Each site has one state and one year.",
            "The Ramappa (Rudreswara) temple, a UNESCO site of 2021, is in which state?",
            ["It is a Kakatiya-era temple.", "It stands at Palampet."],
            "Telangana"),
        pat("ga-un-p2", "Institution to founding or purpose", "common",
            "The year of ASI and its first head, which Akademi handles which art, or the city of FTII.",
            ["Recall the years: ASI 1861, SNA 1953, Sahitya and Lalit Kala 1954.", "Match Akademi to art.", "FTII is 1960 in Pune."],
            "Each body has one year and one field.",
            "In which year was the Archaeological Survey of India founded?",
            ["Alexander Cunningham was its first head.", "It is the oldest body in the list."],
            "1861"),
        pat("ga-un-p3", "Natural, mixed or cultural", "common",
            "Which sites are natural, or which is India's only mixed site.",
            ["Recall that Khangchendzonga is the only mixed site.", "Recall the natural set: Kaziranga, Manas, Keoladeo, Sundarbans, Nanda Devi, Western Ghats, Great Himalayan NP.", "Everything else is cultural."],
            "The natural set is short, so recall settles it.",
            "Which is India's only mixed World Heritage Site?",
            ["It is a national park in Sikkim.", "It was listed in 2016."],
            "Khangchendzonga National Park"),
        pat("ga-un-p4", "Firsts and inscription order", "common",
            "India's first sites, first heritage city, or ordering recent inscriptions.",
            ["The first four came in 1983.", "First city: Ahmedabad, 2017. Jaipur, 2019.", "Recent order: 2021, then 2023, then 2024."],
            "The order ties years to sites.",
            "Which is India's first heritage city on the World Heritage list?",
            ["It was listed in 2017.", "Jaipur joined two years later."],
            "Ahmedabad"),
        pat("ga-un-p5", "ICH element to year", "common",
            "Which Indian element entered the ICH list in a given year, or which element is on the list.",
            ["Recall the year table.", "2010 has Mudiyettu, Kalbelia and Chhau.", "2016 has Yoga. 2017 has Kumbh Mela. 2021 has Durga Puja. 2023 has Garba."],
            "Element-year pairs are direct recall.",
            "Which Kolkata festival entered the ICH list in 2021?",
            ["It is a festival, not a dance.", "It is celebrated in West Bengal."],
            "Durga Puja"),
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
    assert "$" not in n
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
