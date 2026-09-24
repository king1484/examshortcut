"""Build t1-mock-2--ga.json and t1-mock-3--ga.json (25 Qs each).

Distribution per mock: ancient 1, medieval 1, modern 2, art-culture 3, polity 4,
indian-geography 2, world-geography 1, economy 2, physics 2, chemistry 2, biology 2,
static-gk 2, current-affairs 1 (copied from ca_mock_pool.json: q3 -> mock-2, q4 -> mock-3).

Only stable, NCERT-level static facts. Authoring convention: the correct option is
written FIRST; place_answers() rotates options to spread answers over A/B/C/D.
The current-affairs question keeps its pool option order and answer.

Run:  python build_t1_mocks_2_3_ga.py
"""
import json
import os
import random
from collections import Counter

from gacommon import Q, save_mock, all_topic_questions, _norm

HERE = os.path.dirname(os.path.abspath(__file__))

DIST = {"ancient-history": 1, "medieval-history": 1, "modern-history": 2, "art-culture": 3,
        "polity": 4, "indian-geography": 2, "world-geography": 1, "economy": 2, "physics": 2,
        "chemistry": 2, "biology": 2, "static-gk": 2, "current-affairs": 1}


def builder(mock_id):
    qs = []

    def add(q, options, solution, shortcut, difficulty, subtopic, pattern, t=25):
        n = len(qs) + 1
        qs.append(Q(f"q-{mock_id}-ga-{n}", q, options, 0, solution, shortcut,
                    difficulty, subtopic, pattern, t))
    return qs, add


def add_ca(qs, mock_id, pool_id):
    with open(os.path.join(HERE, "ca_mock_pool.json"), encoding="utf-8") as f:
        pool = {x["id"]: x for x in json.load(f)}
    x = dict(pool[pool_id])
    x["id"] = f"q-{mock_id}-ga-{len(qs) + 1}"
    x["fixed"] = True
    qs.append(x)


# =========================================================================
# MOCK 2 — CGL 2025 level (7 easy / 13 medium / 5 hard)
# =========================================================================
m2, a = builder("t1-mock-2")

a("Which Gupta ruler was called the 'Napoleon of India' by the historian V.A. Smith?",
  ["Samudragupta", "Chandragupta I", "Chandragupta II", "Skandagupta"],
  "V.A. Smith called **Samudragupta** the 'Napoleon of India' because of his long run of military campaigns, which are recorded in the Allahabad (Prayag) Pillar inscription.",
  "Conqueror + pillar full of victories = Samudragupta.", "hard", "ancient-history", "title of a ruler")
a("The Vijayanagara Empire was founded in 1336 by —",
  ["Harihara and Bukka", "Krishnadevaraya", "Devaraya II", "Alauddin Hasan Bahman Shah"],
  "Brothers **Harihara and Bukka** of the Sangama dynasty founded Vijayanagara in 1336. Krishnadevaraya (Tuluva dynasty) was its best-known later ruler; Hasan Bahman Shah founded the rival Bahmani kingdom in 1347.",
  "1336 = Sangama brothers; 1347 = Bahmani.", "easy", "medieval-history", "founder")
a("Who founded the Servants of India Society in 1905?",
  ["Gopal Krishna Gokhale", "Bal Gangadhar Tilak", "Dadabhai Naoroji", "Pherozeshah Mehta"],
  "**Gopal Krishna Gokhale** founded the Servants of India Society at Poona in 1905 to train workers for national service. Gokhale was a moderate leader and is regarded as Gandhi's political guru.",
  "Gokhale = 'servants' — a moderate's society of trained volunteers.", "medium", "modern-history", "organisation founder")
a("The Rowlatt Act, against which Gandhi launched a nationwide satyagraha, was passed in —",
  ["1919", "1909", "1916", "1922"],
  "The **Rowlatt Act (March 1919)** allowed detention without trial. Protests against it led up to the Jallianwala Bagh massacre of 13 April 1919 in Amritsar.",
  "Rowlatt and Jallianwala Bagh belong to the same year — 1919.", "medium", "modern-history", "year of event")
a("Mohiniyattam is a classical dance form of which state?",
  ["Kerala", "Tamil Nadu", "Karnataka", "Odisha"],
  "**Mohiniyattam**, a graceful solo dance performed by women, belongs to **Kerala**. Kerala's other classical form is Kathakali.",
  "Kerala has two classical dances: Kathakali and Mohiniyattam.", "easy", "art-culture", "dance-state")
a("Pandit Ravi Shankar is famous for playing which musical instrument?",
  ["Sitar", "Sarangi", "Tabla", "Veena"],
  "**Pandit Ravi Shankar** (Bharat Ratna, 1999) was the sitar player who made Indian classical music known around the world.",
  "Ravi Shankar = sitar; Zakir Hussain = tabla; Ram Narayan = sarangi.", "easy", "art-culture", "musician-instrument")
a("Yakshagana, a traditional theatre form combining dance, music and dialogue, belongs to which state?",
  ["Karnataka", "Kerala", "Andhra Pradesh", "Maharashtra"],
  "**Yakshagana** is the traditional theatre form of coastal **Karnataka**. Kerala is the usual trap because Yakshagana's costumes look like those of Kathakali.",
  "Yakshagana = coastal Karnataka (Udupi and Dakshina Kannada).", "hard", "art-culture", "folk theatre-state")
a("Which Article of the Indian Constitution provides for the Finance Commission?",
  ["Article 280", "Article 270", "Article 300", "Article 312"],
  "**Article 280** requires the President to set up a Finance Commission every five years to recommend how taxes are shared between the Union and the States.",
  "280 = Finance Commission; 324 = Election Commission; 312 = All India Services.", "hard", "polity", "article number")
a("What is the minimum age to become a member of the Lok Sabha?",
  ["25 years", "21 years", "30 years", "35 years"],
  "Under Article 84, a person must be at least **25 years** old to become a Lok Sabha member. The Rajya Sabha requires 30, and the President and Vice-President require 35.",
  "Lok Sabha 25, Rajya Sabha 30, President 35.", "easy", "polity", "age qualification")
a("The Governor of a state holds office during the pleasure of the —",
  ["President", "Chief Minister", "Prime Minister", "Chief Justice of the High Court"],
  "Under Article 156, the Governor holds office **during the pleasure of the President**, who also appoints the Governor (Article 155).",
  "The President appoints the Governor and can remove them.", "medium", "polity", "constitutional office")
a("The provisions on disqualification on grounds of defection (the anti-defection law) are contained in which Schedule of the Constitution?",
  ["Tenth Schedule", "Eighth Schedule", "Ninth Schedule", "Seventh Schedule"],
  "The **Tenth Schedule** contains the anti-defection provisions. The Eighth Schedule lists languages, the Ninth protects certain laws from judicial review, and the Seventh contains the Union, State and Concurrent Lists.",
  "Defection → Tenth Schedule.", "medium", "polity", "schedule")
a("Which is the longest river of peninsular India?",
  ["Godavari", "Krishna", "Narmada", "Mahanadi"],
  "The **Godavari** (about 1,465 km) is the longest peninsular river, which is why it is called the 'Dakshin Ganga'. The Krishna comes second.",
  "Dakshin Ganga = Godavari = longest in the south.", "medium", "indian-geography", "river superlative")
a("Which Indian state has the longest coastline?",
  ["Gujarat", "Andhra Pradesh", "Tamil Nadu", "Maharashtra"],
  "**Gujarat** has the longest coastline of any Indian state, including the Gulf of Kachchh and the Gulf of Khambhat. Andhra Pradesh and Tamil Nadu follow.",
  "Two gulfs (Kachchh and Khambhat) give Gujarat the longest coast.", "medium", "indian-geography", "state superlative")
a("The Suez Canal connects which two water bodies?",
  ["Mediterranean Sea and Red Sea", "Red Sea and Arabian Sea", "Mediterranean Sea and Black Sea", "Atlantic Ocean and Pacific Ocean"],
  "The **Suez Canal** in Egypt connects the **Mediterranean Sea** with the **Red Sea**, so ships can travel between Europe and Asia without going around Africa. The Panama Canal connects the Atlantic and Pacific.",
  "Suez = Mediterranean to Red Sea; Panama = Atlantic to Pacific.", "medium", "world-geography", "canal")
a("Which body regulates the insurance sector in India?",
  ["IRDAI", "SEBI", "PFRDA", "NABARD"],
  "The **Insurance Regulatory and Development Authority of India (IRDAI)** regulates insurance. SEBI regulates securities markets and PFRDA regulates pensions.",
  "Insurance → IRDAI; shares → SEBI; pensions → PFRDA.", "easy", "economy", "regulator")
a("The repo rate is the rate at which —",
  ["the RBI lends short-term funds to commercial banks", "commercial banks lend to their best customers",
   "the RBI borrows money from commercial banks", "the government borrows from the public"],
  "The **repo rate** is the rate at which the **RBI lends** short-term money to commercial banks against government securities. When the RBI instead absorbs money from banks, that is the reverse-repo idea.",
  "Repo = RBI lends to banks. Reverse repo = banks park money with the RBI.", "medium", "economy", "monetary policy term")
a("What is the SI unit of electrical resistance?",
  ["Ohm", "Volt", "Ampere", "Watt"],
  "Resistance is measured in **ohms** (Ω). By Ohm's law, R = V/I. The volt measures potential difference, the ampere measures current, and the watt measures power.",
  "R = V / I → volt per ampere = ohm.", "easy", "physics", "SI unit")
a("Which type of mirror is used as a rear-view mirror in vehicles?",
  ["Convex mirror", "Concave mirror", "Plane mirror", "Parabolic concave mirror"],
  "A **convex mirror** always forms an erect, smaller image and shows a **wider field of view**, which is why it is used as a rear-view mirror. Concave mirrors are used in headlights and for shaving.",
  "Rear-view → wide view → convex.", "medium", "physics", "mirror application")
a("What is the chemical formula of washing soda?",
  ["Na2CO3·10H2O", "NaHCO3", "CaOCl2", "CaSO4·½H2O"],
  "Washing soda is **sodium carbonate decahydrate, Na2CO3·10H2O**. NaHCO3 is baking soda, CaOCl2 is bleaching powder, and CaSO4·½H2O is plaster of Paris.",
  "Washing soda has 10 waters of crystallisation.", "hard", "chemistry", "chemical formula")
a("Vegetable oils are converted into vanaspati ghee by passing which gas through them in the presence of a nickel catalyst?",
  ["Hydrogen", "Oxygen", "Nitrogen", "Carbon dioxide"],
  "**Hydrogenation** adds **hydrogen** to unsaturated vegetable oils in the presence of a nickel catalyst, which turns them into solid fat (vanaspati).",
  "Vanaspati = hydrogenated oil.", "medium", "chemistry", "industrial process")
a("Night blindness is caused by a deficiency of which vitamin?",
  ["Vitamin A", "Vitamin B12", "Vitamin D", "Vitamin E"],
  "The eye needs **vitamin A** (retinol) to make the pigment rhodopsin, which is required for seeing in dim light. A shortage causes **night blindness**.",
  "A for eyes: vitamin A → night blindness.", "easy", "biology", "deficiency disease")
a("Which blood components help in the clotting of blood?",
  ["Platelets", "Red blood cells", "White blood cells", "Plasma proteins only"],
  "**Platelets** (thrombocytes) gather at a wound and start the clotting process. Red blood cells carry oxygen, and white blood cells fight infection.",
  "Platelets plug the leak.", "medium", "biology", "blood components")
a("Which country hosted the first FIFA World Cup in 1930?",
  ["Uruguay", "Brazil", "Italy", "England"],
  "The first FIFA World Cup was held in **Uruguay** in 1930, and Uruguay also won it.",
  "1930: Uruguay hosted and won.", "hard", "static-gk", "sports first")
a("Where is the headquarters of the World Health Organization (WHO)?",
  ["Geneva", "New York", "Paris", "Vienna"],
  "The **WHO** is headquartered in **Geneva**, Switzerland. New York hosts the UN headquarters, Paris hosts UNESCO, and Vienna hosts the IAEA.",
  "Geneva = WHO, ILO and WTO.", "medium", "static-gk", "organisation headquarters")
add_ca(m2, "t1-mock-2", "capool-q3")


# =========================================================================
# MOCK 3 — tougher final-week set (4 easy / 13 medium / 8 hard)
# =========================================================================
m3, a = builder("t1-mock-3")

a("Nalanda Mahavihara, the famous centre of Buddhist learning, was founded by which Gupta ruler?",
  ["Kumaragupta I", "Samudragupta", "Chandragupta II", "Skandagupta"],
  "**Kumaragupta I** (5th century CE) founded Nalanda in present-day Bihar. Harsha and the Pala kings later supported it.",
  "Nalanda → Kumaragupta (K for knowledge).", "hard", "ancient-history", "founder")
a("The Buland Darwaza at Fatehpur Sikri was built by Akbar to commemorate his victory over —",
  ["Gujarat", "Bengal", "Chittor", "Kabul"],
  "Akbar built the **Buland Darwaza** to commemorate his **conquest of Gujarat** (1573). It is one of the tallest gateways in the world.",
  "Buland Darwaza = Gujarat victory gate.", "hard", "medieval-history", "monument purpose")
a("Along with Annie Besant, which leader started a Home Rule League in 1916?",
  ["Bal Gangadhar Tilak", "Gopal Krishna Gokhale", "Lala Lajpat Rai", "Motilal Nehru"],
  "In 1916 **Bal Gangadhar Tilak** (in April) and **Annie Besant** (in September) set up separate Home Rule Leagues and divided the country between them. Gokhale had died in 1915.",
  "Tilak: 'Swaraj is my birthright' → Home Rule.", "medium", "modern-history", "movement leader")
a("Which of the following was NOT a member of the Cabinet Mission that came to India in 1946?",
  ["John Simon", "Pethick-Lawrence", "Stafford Cripps", "A.V. Alexander"],
  "The **Cabinet Mission (1946)** had three members: **Pethick-Lawrence, Stafford Cripps and A.V. Alexander**. **John Simon** led the Simon Commission of 1927-28.",
  "Cabinet Mission = P-C-A (Pethick-Lawrence, Cripps, Alexander).", "hard", "modern-history", "odd one out")
a("Rukmini Devi Arundale, who founded Kalakshetra in Chennai, is associated with which dance form?",
  ["Bharatanatyam", "Kathak", "Manipuri", "Odissi"],
  "**Rukmini Devi Arundale** revived **Bharatanatyam** and founded the Kalakshetra academy (1936) in Chennai.",
  "Kalakshetra, Chennai → Tamil Nadu → Bharatanatyam.", "medium", "art-culture", "artist-dance")
a("Ustad Zakir Hussain was a world-renowned exponent of which instrument?",
  ["Tabla", "Sitar", "Santoor", "Sarangi"],
  "**Ustad Zakir Hussain**, son of tabla maestro Ustad Alla Rakha, was the world's best-known **tabla** player.",
  "Alla Rakha and Zakir Hussain = tabla father and son.", "easy", "art-culture", "musician-instrument")
a("The temples of Khajuraho were built mainly by which dynasty?",
  ["Chandela", "Chola", "Pala", "Paramara"],
  "The **Chandela** rulers built most of the Khajuraho temples (roughly 950-1050 CE) in present-day Madhya Pradesh. They are known for the Nagara style of architecture.",
  "Khajuraho (Bundelkhand, MP) → Chandelas; Cholas are the far south.", "hard", "art-culture", "monument-dynasty")
a("Which Article of the Constitution vests the superintendence, direction and control of elections in the Election Commission?",
  ["Article 324", "Article 280", "Article 315", "Article 368"],
  "**Article 324** gives the Election Commission control of elections to Parliament, the state legislatures, and the offices of President and Vice-President. Article 280 covers the Finance Commission, 315 the Public Service Commissions, and 368 amendments.",
  "324 = elections; 368 = amendment.", "medium", "polity", "article number")
a("A joint sitting of the two Houses of Parliament is presided over by the —",
  ["Speaker of the Lok Sabha", "Vice-President", "President", "Prime Minister"],
  "Under Article 108 the President *summons* a joint sitting, but the **Speaker of the Lok Sabha presides** over it (Article 118(4)). If the Speaker is absent, the Deputy Speaker presides.",
  "President summons; Speaker presides.", "medium", "polity", "parliamentary procedure")
a("The Right to Education (Article 21A) was inserted into the Constitution by which Amendment Act?",
  ["86th Amendment, 2002", "73rd Amendment, 1992", "44th Amendment, 1978", "93rd Amendment, 2005"],
  "The **86th Amendment Act, 2002** inserted **Article 21A** (free and compulsory education for children aged 6-14). It also added a related Fundamental Duty (Article 51A(k)) and changed Article 45.",
  "86th = education (for ages 6 to 14).", "hard", "polity", "amendment")
a("Which writ is issued to produce a detained person before a court to examine whether the detention is lawful?",
  ["Habeas corpus", "Mandamus", "Certiorari", "Prohibition"],
  "**Habeas corpus** ('you may have the body') orders the authority holding a person to bring that person before the court. Mandamus commands a public official to do a duty; certiorari and prohibition are issued to lower courts.",
  "Habeas corpus = produce the body.", "easy", "polity", "writ")
a("The Satpura Range lies between which two rivers?",
  ["Narmada and Tapi", "Godavari and Krishna", "Chambal and Betwa", "Mahanadi and Godavari"],
  "The **Satpura Range** runs between the **Narmada** (to the north) and the **Tapi** (to the south). Both rivers flow west through rift valleys into the Arabian Sea.",
  "Vindhya – Narmada – Satpura – Tapi, from north to south.", "hard", "indian-geography", "relief-rivers")
a("Which state is the largest producer of tea in India?",
  ["Assam", "Kerala", "Tamil Nadu", "Karnataka"],
  "**Assam** produces more tea than any other Indian state; the Brahmaputra valley is the heart of Indian tea. West Bengal (Darjeeling and the Dooars) comes second.",
  "Tea → Assam; coffee → Karnataka.", "easy", "indian-geography", "crop-state")
a("The Kalahari Desert is located mainly in which country?",
  ["Botswana", "Egypt", "Chile", "Mongolia"],
  "The **Kalahari**, a semi-arid sandy desert in southern Africa, covers most of **Botswana**. The Atacama is in Chile and the Gobi is in Mongolia.",
  "Kalahari → southern Africa → Botswana.", "medium", "world-geography", "desert-country")
a("India's First Five-Year Plan (1951-56) was based on which economic model?",
  ["Harrod-Domar model", "Mahalanobis model", "Gandhian model", "Rao-Manmohan model"],
  "The **First Plan** followed the **Harrod-Domar model**, focusing on agriculture and irrigation. The Second Plan used the Mahalanobis model for heavy industry.",
  "Plan 1 = Harrod-Domar (agriculture); Plan 2 = Mahalanobis (industry).", "hard", "economy", "planning")
a("Which of the following is a direct tax?",
  ["Income tax", "Goods and Services Tax", "Customs duty", "Excise duty"],
  "A **direct tax** is paid by the same person on whom it is levied — **income tax** is the standard example. GST, customs and excise are indirect taxes whose burden passes on to the consumer.",
  "Burden can't be shifted = direct (income, corporate tax).", "easy", "economy", "tax classification")
a("Hypermetropia (long-sightedness) is corrected using which type of lens?",
  ["Convex lens", "Concave lens", "Cylindrical lens", "Bifocal concave lens"],
  "In **hypermetropia**, the image of a nearby object forms behind the retina. A **convex (converging) lens** brings it forward onto the retina.",
  "Hyper-metropia → converging (convex) lens.", "medium", "physics", "defects of vision")
a("To hear a distinct echo, the reflected sound must reach the ear at least how long after the original sound?",
  ["0.1 second", "0.01 second", "1 second", "0.5 second"],
  "The ear keeps a sound for about **0.1 s** (persistence of hearing). So an echo is distinct only if it returns after at least 0.1 s. With sound at about 344 m/s, the reflecting surface must be at least **about 17 m** away.",
  "0.1 s → about 17 m (344 × 0.1 ÷ 2).", "hard", "physics", "sound")
a("Rusting of iron requires the presence of —",
  ["both oxygen and water (moisture)", "oxygen only", "water only", "carbon dioxide only"],
  "Iron rusts (forms hydrated iron(III) oxide) only when **both oxygen and water** are present. This is why painting, oiling and galvanising, which keep out air and moisture, prevent rusting.",
  "Rust = iron + air + water.", "medium", "chemistry", "corrosion")
a("Vinegar is a dilute solution of which acid?",
  ["Acetic acid", "Citric acid", "Lactic acid", "Oxalic acid"],
  "Vinegar is about 5-8% **acetic (ethanoic) acid**. Citric acid is found in citrus fruits, lactic acid in curd, and oxalic acid in spinach and tomatoes.",
  "Vinegar = acetic; curd = lactic; lemon = citric.", "medium", "chemistry", "natural acids")
a("Which metal is present at the centre of the chlorophyll molecule?",
  ["Magnesium", "Iron", "Copper", "Zinc"],
  "The chlorophyll molecule has a **magnesium** ion at its centre. Iron plays the matching role in haemoglobin.",
  "Chlorophyll = Mg; haemoglobin = Fe.", "medium", "biology", "biomolecules")
a("Which part of the human brain controls involuntary actions such as breathing and heartbeat?",
  ["Medulla oblongata", "Cerebrum", "Hypothalamus", "Pons only"],
  "The **medulla oblongata** in the hindbrain controls involuntary vital functions such as breathing, heartbeat and blood pressure. The cerebrum handles thinking and voluntary action.",
  "Medulla = vital functions.", "medium", "biology", "human brain")
a("Who wrote the novel 'Anandamath', which contains the song 'Vande Mataram'?",
  ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarat Chandra Chattopadhyay", "Subramania Bharati"],
  "**Bankim Chandra Chatterjee** wrote **Anandamath** (1882), which includes 'Vande Mataram', India's National Song. Tagore wrote the National Anthem, 'Jana Gana Mana'.",
  "National Song = Bankim; National Anthem = Tagore.", "medium", "static-gk", "books-authors")
a("The Davis Cup is associated with which sport?",
  ["Tennis", "Badminton", "Golf", "Table tennis"],
  "The **Davis Cup** is the international men's team competition in **tennis**. Badminton's men's team event is the Thomas Cup, and golf has the Ryder Cup.",
  "Davis = tennis; Thomas = badminton; Ryder = golf.", "medium", "static-gk", "trophy-sport")
add_ca(m3, "t1-mock-3", "capool-q4")


# =========================================================================
def place_answers(qs, seed_base):
    fixed = [x for x in qs if x.get("fixed")]
    free = [x for x in qs if not x.get("fixed")]
    have = Counter(x["answer"] for x in fixed)
    n = len(qs)
    for seed in range(seed_base, seed_base + 5000):
        rng = random.Random(seed)
        order = [0, 1, 2, 3]
        rng.shuffle(order)
        quota = {pos: n // 4 + (1 if rank < n % 4 else 0) for rank, pos in enumerate(order)}
        need = []
        for pos in range(4):
            need += [pos] * max(0, quota[pos] - have[pos])
        need = need[:len(free)]
        rng.shuffle(need)
        tgt = dict(zip([x["id"] for x in free], need))
        seq = [tgt.get(x["id"], x["answer"]) for x in qs]
        longest = max(len(r) for r in _runs(seq))
        if longest <= 2:
            break
    for x in free:
        t = tgt[x["id"]]
        k = (0 - t) % 4
        opts = x["options"]
        x["options"] = opts[k:] + opts[:k]
        x["answer"] = t
        assert x["options"][t] == opts[0]
    for x in fixed:
        del x["fixed"]
    return qs


def _runs(seq):
    out, cur = [], [seq[0]]
    for v in seq[1:]:
        if v == cur[-1]:
            cur.append(v)
        else:
            out.append(cur)
            cur = [v]
    out.append(cur)
    return out


def finish(mock_id, qs, want_diff, seed):
    assert dict(Counter(x["subtopic"] for x in qs)) == DIST, Counter(x["subtopic"] for x in qs)
    bank = all_topic_questions()
    for x in qs:
        assert _norm(x["q"]) not in bank, f"{x['id']} duplicates topic bank {bank[_norm(x['q'])]}"
        assert 20 <= x["timeSec"] <= 35, x["id"]
    diff = Counter(x["difficulty"] for x in qs)
    assert (diff["easy"], diff["medium"], diff["hard"]) == want_diff, dict(diff)
    place_answers(qs, seed)
    save_mock(mock_id, qs, 25)
    ans = [x["answer"] for x in qs]
    print(f"   answers A/B/C/D = {[ans.count(i) for i in range(4)]}  seq={''.join('ABCD'[v] for v in ans)}")
    print(f"   difficulty easy/medium/hard = {diff['easy']}/{diff['medium']}/{diff['hard']}")


if __name__ == "__main__":
    finish("t1-mock-2", m2, (7, 13, 5), 500)
    finish("t1-mock-3", m3, (4, 13, 8), 600)
