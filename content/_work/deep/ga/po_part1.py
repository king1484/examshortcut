"""polity deep content — part 1: pol-making, pol-preamble-parts, pol-fundamental-rights, pol-executive."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_making():
    S = Sub("pol-making")
    S.notes = """### The Assembly that wrote the Constitution
India's Constituent Assembly was formed in **1946** under the **Cabinet Mission Plan**. Its members were **indirectly elected** by the provincial assemblies through proportional representation. The sanctioned strength was **389** — 292 from British provinces, 93 from princely states and 4 from chief commissioners' provinces; after Partition it came down to **299**. It first met on **9 December 1946** in the Central Hall of Parliament. **Dr Sachchidananda Sinha** presided as temporary chairman. **Dr Rajendra Prasad** was elected permanent President on **11 December 1946**, with **H.C. Mukherjee** as Vice-President. **Sir B.N. Rau** was the constitutional adviser who prepared the first draft that the Drafting Committee reworked.

### The clock of key dates
| Date | Event |
|---|---|
| 13 Dec 1946 | **Objectives Resolution** moved by **Nehru**; adopted **22 Jan 1947** — the seed of the Preamble |
| 29 Aug 1947 | **Drafting Committee** formed — **7 members**, chaired by **Dr B.R. Ambedkar** |
| 4 Nov 1948 | Draft Constitution introduced in the Assembly |
| 26 Nov 1949 | Constitution **adopted** (now Constitution Day) |
| 24 Jan 1950 | **284 members signed**; 'Jana Gana Mana' adopted as anthem |
| 26 Jan 1950 | Constitution **came into force** (Republic Day) |

The Assembly took **2 years, 11 months and 18 days**, held **11 sessions**, and the whole exercise cost about **₹64 lakh**. It then served as the **provisional Parliament** until the first general election (1951-52). 26 January was chosen to honour **Purna Swaraj Day** (26 Jan 1930), the day the Congress had demanded complete independence (decided at the Lahore session, Dec 1929).

### Committee ↔ chairman (asked again and again)
| Committee | Chairman |
|---|---|
| Union Powers Committee; Union Constitution Committee; States Committee | **Jawaharlal Nehru** |
| Provincial Constitution Committee; Advisory Committee on Fundamental Rights, Minorities | **Sardar Patel** |
| Rules of Procedure; Steering Committee; Flag Committee | **Rajendra Prasad** |
| **Drafting Committee** | **Dr B.R. Ambedkar** |

The rough division: **Nehru** took the 'national' committees, **Patel** the 'practical/state' ones, **Prasad** the procedural ones, **Ambedkar** the drafting pen.

### Borrowed features — the source map
| Feature | Borrowed from |
|---|---|
| Federal scheme, Governors, judiciary, Public Service Commissions, emergency provisions, administrative detail | **Government of India Act, 1935** (the single biggest source) |
| Parliamentary system, rule of law, single citizenship, cabinet, legislative procedure, bicameralism, writs | **Britain** |
| Fundamental Rights, judicial review, independence of judiciary, impeachment of the President, Vice-President as Rajya Sabha chairman, removal of judges | **USA** |
| Directive Principles, method of President's election, nomination of 12 members to Rajya Sabha | **Ireland** |
| Federation with a strong Centre, residuary powers with the Centre, appointment of Governors, advisory jurisdiction of the Supreme Court | **Canada** |
| Concurrent List, freedom of trade and commerce, **joint sitting** of the two Houses | **Australia** |
| Fundamental Duties, the ideal of justice (social, economic, political) in the Preamble | **USSR** |
| Ideals of liberty, equality, fraternity in the Preamble; Republic | **France** |
| Suspension of Fundamental Rights during Emergency | **Germany (Weimar)** |
| Procedure for amendment; election of Rajya Sabha members | **South Africa** |
| 'Procedure established by law' (Art 21 wording) | **Japan** |

### Quick revision
- Cabinet Mission Plan 1946; indirect election; 389 seats → 299 after Partition.
- 9 Dec 1946 first meeting; Sinha temporary chair; Rajendra Prasad permanent President; B.N. Rau adviser.
- Drafting Committee 29 Aug 1947, 7 members, Ambedkar chairman.
- Adopted 26 Nov 1949, enforced 26 Jan 1950 (Purna Swaraj Day 1930); 2y-11m-18d; 11 sessions; ₹64 lakh.
- Nehru — Objectives Resolution; union committees. Patel — provinces + rights. Prasad — rules/flag/steering.
- Biggest source = Government of India Act 1935; DPSP-Ireland, FRs-USA, Duties-USSR, joint sitting-Australia."""
    S.pattern("ga-polmk-p1", "Assembly: people, dates and numbers", "very common",
        "'Who was the temporary/permanent President of the Constituent Assembly', 'when did it first meet', 'how long did it take', 'how many members signed'.",
        None,
        "1. Fix the four anchors: 9 Dec 1946 (first meeting), 26 Nov 1949 (adopted), 24 Jan 1950 (284 signed), 26 Jan 1950 (in force).\n2. People: Sinha = temporary chairman, Rajendra Prasad = permanent President, H.C. Mukherjee = Vice-President, B.N. Rau = constitutional adviser, Ambedkar = Drafting Committee chairman only.\n3. Numbers: 389 → 299 members; 2 years 11 months 18 days; 11 sessions; ₹64 lakh; 284 signatures.",
        "The Constituent Assembly met for the first time on —",
        "**9 December 1946**, in the Central Hall of Parliament, with **Dr Sachchidananda Sinha** as temporary chairman.")
    S.pattern("ga-polmk-p2", "Borrowed feature ↔ source country", "very common",
        "A feature (DPSP, joint sitting, fundamental duties, concurrent list, writs) is named and its source country asked, often as a correctly-matched pair.",
        None,
        "1. Memorise the map: FRs/judicial review/impeachment = USA; DPSP/President's election/12 RS nominees = Ireland; Duties/justice ideal = USSR; liberty-equality-fraternity/Republic = France.\n2. Structural ones: strong Centre/residuary with Centre/Canada; concurrent list/joint sitting/Australia; amendment procedure/South Africa; 'procedure established by law'/Japan; emergency FR suspension/Germany.\n3. In match-the-pairs, eliminate the UK — it never had a written constitution, so 'written constitution from Britain' is always wrong.",
        "The concept of a **Concurrent List** and the **joint sitting** of the two Houses of Parliament was borrowed from —",
        "**Australia** — Australia's Constitution carries a concurrent list of powers and the device of a joint sitting to resolve deadlocks between the two Houses.")
    S.pattern("ga-polmk-p3", "Committee ↔ chairman pairing", "common",
        "'The Advisory Committee on Fundamental Rights was chaired by', or a four-row match on committees and chairmen.",
        None,
        "1. Rule of thumb: Nehru = national subjects (Union Powers, Union Constitution, States); Patel = provinces and rights; Prasad = procedure, steering, flag; Ambedkar = Drafting only.\n2. Trap: the Advisory Committee on Fundamental Rights and Minorities is **Patel**, not Ambedkar.\n3. Trap: the Assembly's President is **Rajendra Prasad**, not Ambedkar — Ambedkar chaired only the Drafting Committee.",
        "Who among the following chaired the **Advisory Committee on Fundamental Rights and Minorities** of the Constituent Assembly?",
        "**Sardar Vallabhbhai Patel**. He also chaired the Provincial Constitution Committee; the Drafting Committee was Ambedkar's.")
    S.pattern("ga-polmk-p4", "Government of India Act 1935 and famous labels", "common",
        "'The bulk of the Constitution is drawn from', 'which act provided the federal scheme', plus nickname questions (Mini-Constitution, Magna Carta, heart and soul).",
        None,
        "1. The single largest source is the **Government of India Act, 1935** — federal scheme, Governors, judiciary, public service commissions, emergency powers.\n2. Labels: 42nd Amendment = 'Mini-Constitution'; Part III = 'Magna Carta of India'; Article 32 = 'heart and soul' (Ambedkar); CAG = 'guardian of the public purse'.\n3. The Act of 1935 was itself not fully federal in practice — safeguards and reserved subjects stayed with the Viceroy.",
        "Which one of the following is described as the **'heart and soul'** of the Indian Constitution?",
        "**Article 32** (right to constitutional remedies) — Dr Ambedkar's phrase, because the writ power makes the Fundamental Rights real.")

    S.q("ga-polmk-p1", "easy", "The Constituent Assembly of India held its **first meeting** on —",
        ["26 November 1949", "9 December 1946", "26 January 1950", "15 August 1947"], "9 December 1946",
        "The Assembly first met on **9 December 1946**; it adopted the Constitution on 26 November 1949 and brought it into force on 26 January 1950.",
        "First met 1946 → adopted 1949 → enforced 1950.", 20)
    S.q("ga-polmk-p1", "easy", "The **permanent President** of the Constituent Assembly was —",
        ["Dr B.R. Ambedkar", "Dr Sachchidananda Sinha", "Dr Rajendra Prasad", "Sir B.N. Rau"], "Dr Rajendra Prasad",
        "**Dr Rajendra Prasad** was elected permanent President on 11 December 1946. Sinha was only the temporary chairman; Ambedkar chaired the Drafting Committee.",
        "Prasad presided; Ambedkar drafted; Sinha only opened.", 20)
    S.q("ga-polmk-p1", "medium", "How many members **signed** the Constitution of India on 24 January 1950?",
        ["299", "284", "389", "275"], "284",
        "**284 members signed** on 24 January 1950, the last day of the Assembly. The full post-Partition strength was 299; 389 was the pre-Partition sanctioned strength.",
        "389 → 299 → 284: sanctioned → after Partition → signed.", 20)
    S.q("ga-polmk-p2", "easy", "The **Directive Principles of State Policy** were borrowed from the Constitution of —",
        ["USA", "Ireland", "Australia", "Canada"], "Ireland",
        "**Ireland** supplied the DPSP idea, the method of electing the President, and the nomination of 12 members to the Rajya Sabha.",
        "Irish trio: DPSP, President's election, 12 RS nominees.", 20)
    S.q("ga-polmk-p2", "medium", "Which one of the following pairs is **correctly matched**?",
        ["Fundamental Duties — USA", "Joint sitting of Parliament — Australia", "Residuary powers with states — Canada", "Liberty, Equality, Fraternity — Ireland"], "Joint sitting of Parliament — Australia",
        "Joint sitting (Art 108) is an Australian import. Fundamental Duties are from the USSR; Canada gives residuary powers to the **Centre**, not states; liberty-equality-fraternity came from France.",
        "Run each pair against the source map.", 25)
    S.q("ga-polmk-p2", "medium", "The principle of **suspension of Fundamental Rights during Emergency** was borrowed from the Constitution of —",
        ["Germany", "Japan", "South Africa", "Britain"], "Germany",
        "The **Weimar Constitution of Germany** supplied the idea of suspending rights during an emergency. Japan gave the phrase 'procedure established by law'; South Africa gave the amendment procedure.",
        "Germany = emergency rights suspension.", 25)
    S.q("ga-polmk-p3", "medium", "The **Union Powers Committee** of the Constituent Assembly was chaired by —",
        ["Sardar Patel", "Jawaharlal Nehru", "Dr Rajendra Prasad", "Dr B.R. Ambedkar"], "Jawaharlal Nehru",
        "**Nehru** chaired the Union Powers, Union Constitution and States Committees. Patel handled the Provincial Constitution Committee and the Advisory Committee on rights and minorities.",
        "Nehru = 'national' committees; Patel = provinces and rights.", 20)
    S.q("ga-polmk-p3", "medium", "The **Objectives Resolution**, which became the base of the Preamble, was moved by —",
        ["Dr B.R. Ambedkar", "Sardar Patel", "Jawaharlal Nehru", "Sir B.N. Rau"], "Jawaharlal Nehru",
        "**Nehru** moved the Objectives Resolution on **13 December 1946**; the Assembly adopted it on **22 January 1947**. It sets out sovereignty, justice, liberty, equality and fraternity.",
        "Objectives Resolution = Nehru, Dec 1946.", 20)
    S.q("ga-polmk-p3", "hard", "Consider the statements about the Constituent Assembly:\n1. It was directly elected by adult franchise.\n2. It adopted the Objectives Resolution in January 1947.\n3. It acted as the provisional Parliament after 1950.\nWhich are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], "2 and 3 only",
        "Statement 1 is wrong — members were elected **indirectly** by provincial assemblies under the Cabinet Mission Plan, not by adult franchise. Statements 2 and 3 are correct.",
        "Assembly = indirect election; provisional Parliament till 1952.", 30)
    S.q("ga-polmk-p4", "easy", "The federal scheme, office of Governor, and emergency provisions of our Constitution are drawn mainly from the —",
        ["Government of India Act, 1935", "Indian Councils Act, 1909", "British Constitution", "Constitution of Canada"], "Government of India Act, 1935",
        "The **Government of India Act, 1935** is the single largest source — federal scheme, Governors, federal court structure, public service commissions and emergency machinery.",
        "Most of the 'machinery' comes from the 1935 Act.", 20)
    S.q("ga-polmk-p4", "medium", "How much time did the Constituent Assembly take to frame the Constitution?",
        ["2 years, 11 months, 18 days", "1 year, 10 months, 12 days", "3 years, 4 months, 5 days", "2 years, 5 months, 10 days"], "2 years, 11 months, 18 days",
        "From 9 December 1946 to 26 November 1949 the Assembly worked for **2 years, 11 months and 18 days**, across **11 sessions**, at a cost of about **₹64 lakh**.",
        "2-11-18 is the standard exam number.", 20)
    return S


def build_preamble():
    S = Sub("pol-preamble-parts")
    S.notes = """### The Preamble — the identity card of the Constitution
The Preamble opens: '**WE, THE PEOPLE OF INDIA** …', which proclaims that the Constitution draws its authority from the people, not from any king or Parliament. It was framed from **Nehru's Objectives Resolution** (1946). It declares India a **SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC** and promises **justice** (social, economic, political), **liberty** (of thought, expression, belief, faith, worship), **equality** (of status and opportunity) and **fraternity** (assuring dignity, unity and integrity).

Key facts exams test:
- '**Sovereign**' = no outside power controls India. '**Republic**' = the head of state is elected, not hereditary.
- '**Socialist**', '**secular**' and '**integrity**' were added by the **42nd Amendment, 1976** — the only amendment to the Preamble so far.
- The Preamble is **non-justiciable** — its ideals cannot be enforced in court — and it is **neither a source of legislative power nor a limit on it**.
- Court journey: **Berubari case (1960)** held it is **not** a part of the Constitution; **Kesavananda Bharati (1973)** overruled this — it **is** a part, can be amended, but its basic elements cannot be destroyed (basic structure). **LIC of India (1995)** reaffirmed that it is a part.
- The Preamble records the adoption date, **26 November 1949**.

### Parts of the Constitution — the article map
| Part | Subject | Articles |
|---|---|---|
| I | The Union and its territory | 1–4 |
| II | Citizenship | 5–11 |
| III | Fundamental Rights | 12–35 |
| IV | Directive Principles | 36–51 |
| IV-A | Fundamental Duties | 51A |
| V | The Union (President, Parliament, courts) | 52–151 |
| VI | The States | 152–237 |
| VIII | Union Territories | 239–242 |
| IX | Panchayats | 243–243O |
| IX-A | Municipalities | 243P–243ZG |
| X | Scheduled and Tribal Areas | 244–244A |
| XI | Centre–State relations | 245–263 |
| XII | Finance, property, contracts | 264–300A |
| XIII | Trade and commerce | 301–307 |
| XIV | Services | 308–323 |
| XIV-A | Tribunals | 323A–323B |
| XV | Elections | 324–329A |
| XVII | Official language | 343–351 |
| XVIII | Emergency | 352–360 |
| XX | Amendment | 368 |

Part VII (old Part B states) was **repealed** by the 7th Amendment, 1956. **Article 1** names the country: 'India, that is **Bharat**, shall be a **Union of States**'.

### The 12 Schedules
| Schedule | Content |
|---|---|
| 1 | States and Union Territories |
| 2 | Salaries and emoluments of constitutional post-holders |
| 3 | Forms of oaths and affirmations |
| 4 | Allocation of Rajya Sabha seats |
| 5 | Administration of Scheduled Areas and Scheduled Tribes |
| 6 | Tribal areas of Assam, Meghalaya, Tripura, Mizoram |
| 7 | Union (100), State (61) and Concurrent (52) Lists |
| 8 | **22 recognised languages** |
| 9 | Land-reform and other laws protected from challenge (added by 1st Amendment, 1951) |
| 10 | **Anti-defection law** (52nd Amendment, 1985) |
| 11 | Panchayat subjects — 29 items (73rd Amendment) |
| 12 | Municipal subjects — 18 items (74th Amendment) |

In the **I.R. Coelho case (2007)** the Supreme Court held that laws placed in the Ninth Schedule **after 24 April 1973** (the Kesavananda date) can still be reviewed if they destroy the basic structure. The Eighth Schedule's 22 languages include four added by the **92nd Amendment (2003)** — Bodo, Dogri, Maithili and Santhali.

### Quick revision
- Preamble words order: Sovereign Socialist Secular Democratic Republic — all capitalised terms define India's character.
- 42nd Amendment (1976) added socialist, secular, integrity — the only Preamble change.
- Berubari (1960): not a part; Kesavananda (1973): a part, amendable within basic structure.
- Part II citizenship (5–11); Part IV DPSP (36–51); IV-A duties (51A); IX panchayats; IX-A municipalities.
- Schedules 1/12: states-UTs / municipal subjects; 4 = Rajya Sabha seats; 8 = 22 languages; 9 = protected laws (1st Amendment); 10 = defection; 11 = 29 panchayat subjects.
- Article 1: 'India, that is Bharat, shall be a Union of States'."""
    S.pattern("ga-polpre-p1", "Preamble keywords and the 42nd Amendment", "very common",
        "'Which words were added to the Preamble by the 42nd Amendment', the order of adjectives, the four ideals and what each promises.",
        None,
        "1. Added trio = **socialist, secular, integrity** (42nd Amendment, 1976). Nothing else in the Preamble has ever changed.\n2. Ideals with brackets: Justice = social, economic, political; Liberty = thought, expression, belief, faith, worship; Equality = status and opportunity; Fraternity = dignity, unity, integrity.\n3. Word order: SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC.",
        "The ideals of **Liberty, Equality and Fraternity** in the Indian Preamble are inspired by the —",
        "**French Revolution** (France's constitution supplies these ideals, along with the word 'Republic'); the 'justice' ideal traces to the USSR.")
    S.pattern("ga-polpre-p2", "Preamble in the courts", "common",
        "'Is the Preamble a part of the Constitution?', 'can it be amended?', which case decided what.",
        None,
        "1. Chain of cases: **Berubari (1960) = NOT a part** → **Kesavananda Bharati (1973) = IS a part, amendable but not destructible** → **LIC of India (1995) = reaffirmed part**.\n2. The Preamble has been amended **once** (42nd Amendment, 1976) and it survived — proof that it is amendable.\n3. It is non-justiciable and neither a source of power nor a prohibition on power.",
        "In which case did the Supreme Court hold that the Preamble **is a part** of the Constitution?",
        "**Kesavananda Bharati (1973)** — overruling Berubari (1960), it made the Preamble a part of the Constitution, amendable without damaging the basic structure.")
    S.pattern("ga-polpre-p3", "Part ↔ Articles range matching", "very common",
        "'Fundamental Rights are contained in which Articles', 'which Part deals with Municipalities', match-the-column across Parts.",
        None,
        "1. Learn the five everyday ranges: FRs 12–35, DPSP 36–51, Duties 51A, Panchayats 243–243O, Municipalities 243P–243ZG.\n2. Emergency = 352–360; Amendment = 368; Elections = 324–329; Services = 308–323.\n3. Odd facts: Part VII stands repealed (7th Amendment, 1956); tribunals = XIV-A (323A-B); citizenship = Part II (5–11).",
        "Which Part of the Constitution deals with **Municipalities**?",
        "**Part IX-A** (Articles 243P to 243ZG), inserted by the 74th Amendment, 1992; Panchayats sit next door in Part IX.")
    S.pattern("ga-polpre-p4", "Schedule ↔ content matching", "very common",
        "'The anti-defection law is in which Schedule', 'which Schedule lists panchayat subjects', correctly-matched schedule pairs.",
        None,
        "1. Anchors: 8 = 22 languages; 9 = protected laws (1st Amendment 1951); 10 = defection (52nd Amendment 1985); 11 = 29 panchayat subjects; 12 = 18 municipal subjects.\n2. Number-memory: 8 → languages, 10 → politicians (defection), 11 → villages, 12 → cities.\n3. Ninth Schedule shield is limited: post-Kesavananda laws in it can be reviewed (I.R. Coelho, 2007).",
        "The **Tenth Schedule** of the Constitution deals with —",
        "**Disqualification on the ground of defection** — inserted by the 52nd Amendment Act, 1985; it decides when an MLA/MP loses the seat for defying the party.")
    S.pattern("ga-polpre-p5", "Eighth Schedule languages", "common",
        "'How many languages are in the Eighth Schedule', 'which amendment added Bodo/Dogri/Maithili/Santhali', 'which language was added by the 21st/71st Amendment'.",
        None,
        "1. Current count: **22 languages** (not 18, not 24).\n2. Addition chain: Sindhi — 21st Amendment (1967); Konkani, Manipuri, Nepali — 71st (1992); Bodo, Dogri, Maithili, Santhali — 92nd (2003).\n3. Classical-language tags are a separate list — do not mix them with the Eighth Schedule count.",
        "The **92nd Constitutional Amendment Act, 2003** added which four languages to the Eighth Schedule?",
        "**Bodo, Dogri, Maithili and Santhali**, taking the total count of scheduled languages to 22.")

    S.q("ga-polpre-p1", "easy", "The words '**socialist**, **secular**' and '**integrity**' were added to the Preamble by the —",
        ["44th Amendment", "24th Amendment", "42nd Amendment", "52nd Amendment"], "42nd Amendment",
        "The **42nd Amendment Act, 1976** (the 'Mini-Constitution') inserted socialist, secular and integrity into the Preamble. It is the only amendment the Preamble has ever received.",
        "42 = the trio + Mini-Constitution.", 20)
    S.q("ga-polpre-p1", "medium", "In the Preamble, the word '**Justice**' is qualified by the ideals —",
        ["Social, economic and political", "Thought, expression and belief", "Status and opportunity", "Dignity and unity"], "Social, economic and political",
        "Justice is **social, economic and political**; Liberty is of thought, expression, belief, faith and worship; Equality is of status and opportunity; Fraternity assures dignity, unity and integrity.",
        "Justice = SEP; Liberty = 5 freedoms; Equality = status+opportunity.", 20)
    S.q("ga-polpre-p2", "medium", "In the **Berubari Union case (1960)**, the Supreme Court held that the Preamble —",
        ["Is a part of the Constitution and can be amended", "Is not a part of the Constitution", "Can override Fundamental Rights", "Is enforceable in a court of law"], "Is not a part of the Constitution",
        "In **Berubari (1960)** the Court said the Preamble is not a part of the Constitution. **Kesavananda Bharati (1973)** reversed this and made it a part, amendable within the basic structure.",
        "Berubari = 'not a part'; Kesavananda = 'a part'.", 25)
    S.q("ga-polpre-p2", "easy", "The Preamble of the Indian Constitution —",
        ["Can be enforced in a court of law", "Is non-justiciable", "Is a source of legislative power", "Was never amended"], "Is non-justiciable",
        "The Preamble is **non-justiciable** — courts cannot enforce its ideals directly — and it is neither a source of power nor a limit on power. It was amended once, by the 42nd Amendment.",
        "Non-justiciable + amended once = the two safe lines.", 20)
    S.q("ga-polpre-p3", "easy", "The **Fundamental Duties** were added to the Constitution by inserting Part —",
        ["IV-A (Article 51A)", "IX (Article 243)", "XIV-A (Article 323A)", "III (Article 32A)"], "IV-A (Article 51A)",
        "Fundamental Duties sit in **Part IV-A, Article 51A**, inserted by the 42nd Amendment (1976) on the Swaran Singh Committee's advice.",
        "IV-A = 51A = duties (42nd).", 20)
    S.q("ga-polpre-p3", "medium", "Which of the following pairs is **correctly matched**?",
        ["Part IX — Municipalities", "Part XIV-A — Elections", "Part XVIII — Emergency", "Part X — Citizenship"], "Part XVIII — Emergency",
        "Emergency provisions (Articles 352–360) lie in **Part XVIII**. Part IX is Panchayats, XIV-A is Tribunals, and Citizenship is Part II.",
        "Check each Part against the article map.", 25)
    S.q("ga-polpre-p4", "easy", "The **anti-defection law** is contained in which Schedule of the Constitution?",
        ["Ninth Schedule", "Tenth Schedule", "Eleventh Schedule", "Eighth Schedule"], "Tenth Schedule",
        "The **Tenth Schedule** (52nd Amendment, 1985) lists the grounds of disqualification for defection. The Eleventh lists panchayat subjects and the Ninth holds protected laws.",
        "Ten = defection; Nine = shield; Eleven = villages.", 20)
    S.q("ga-polpre-p4", "medium", "The **Ninth Schedule** was added to the Constitution by —",
        ["42nd Amendment, 1976", "1st Amendment, 1951", "24th Amendment, 1971", "7th Amendment, 1956"], "1st Amendment, 1951",
        "The **1st Amendment (1951)** created the Ninth Schedule to shield land-reform laws from judicial review. I.R. Coelho (2007) held that laws placed there after 24 April 1973 remain open to basic-structure review.",
        "9th Schedule = 1st Amendment = 1951.", 25)
    S.q("ga-polpre-p5", "easy", "How many languages are recognised in the **Eighth Schedule** at present?",
        ["18", "22", "20", "24"], "22",
        "The Eighth Schedule recognises **22 languages**. The last four — Bodo, Dogri, Maithili, Santhali — came in with the 92nd Amendment (2003).",
        "22 scheduled languages.", 20)
    S.q("ga-polpre-p5", "hard", "**Sindhi** was added to the Eighth Schedule by which amendment?",
        ["21st Amendment", "71st Amendment", "92nd Amendment", "42nd Amendment"], "21st Amendment",
        "The **21st Amendment (1967)** added Sindhi. The 71st (1992) added Konkani, Manipuri and Nepali; the 92nd (2003) added Bodo, Dogri, Maithili and Santhali.",
        "Language additions: 21 (Sindhi) → 71 (3) → 92 (4).", 30)
    return S


def build_frs():
    S = Sub("pol-fundamental-rights")
    S.notes = """### Fundamental Rights — the Magna Carta of India
Part III (Articles 12–35) is called the **Magna Carta of India** — borrowed chiefly from the USA. 'State' here (Article 12) means government and its agencies, against which these rights mainly protect you. Six rights exist today:

| Right | Articles |
|---|---|
| Right to Equality | **14–18** |
| Right to Freedom (six freedoms) | **19–22** |
| Right against Exploitation | **23–24** |
| Right to Freedom of Religion | **25–28** |
| Cultural and Educational Rights | **29–30** |
| Right to Constitutional Remedies | **32** |

The old **Right to Property** (Article 31) was deleted by the **44th Amendment (1978)** and demoted to a legal right under **Article 300A**. Article 14 promises equality before law; 15 bans discrimination (with special-care clauses 15(3)–15(6)); 16 guarantees equal opportunity in government jobs; 17 abolishes **untouchability**; 18 abolishes titles. Article 19 carries **six freedoms** — speech and expression, assembly, association, movement, residence, profession (the property freedom went out with the 44th). Article 21 — **life and personal liberty** — after **Maneka Gandhi (1978)** means any law limiting it must be fair, just and reasonable; **Puttaswamy (2017)** read the **right to privacy** into it. Article 21A (86th Amendment, 2002) makes free, compulsory education for ages **6–14** a right. Article 32 gives the **five writs** and is itself a fundamental right — Ambedkar called it the '**heart and soul**' of the Constitution.

### The five writs
| Writ | Meaning |
|---|---|
| **Habeas corpus** | 'Produce the body' — against illegal detention |
| **Mandamus** | 'We command' — orders a public authority to do its duty |
| **Prohibition** | Stops a lower court from exceeding jurisdiction (issued during the case) |
| **Certiorari** | Quashes an order passed without/ beyond jurisdiction (issued after) |
| **Quo warranto** | 'By what authority' — challenges illegal occupation of a public office |

High Courts can issue the same writs under **Article 226**, with a **wider** scope (for legal as well as fundamental rights).

### DPSP — Part IV (Articles 36–51), from Ireland
Non-justiciable but '**fundamental in the governance of the country**'. The standard three-way split:

| Group | Key articles |
|---|---|
| **Gandhian** | 40 (village panchayats), 43 (cottage industries), 43B (cooperatives), 46 (SC/ST/weaker sections), 47 (nutrition), 48 (agriculture, cow protection) |
| **Socialist** | 38 (social order), 39 (economic principles), 39A (free legal aid), 41 (work, education, public assistance), 42 (maternity relief), 43A (workers' participation) |
| **Liberal-intellectual** | 44 (**uniform civil code**), 45 (early childhood care), 48A (environment), 49 (monuments), 50 (separate judiciary from executive), 51 (international peace) |

**Minerva Mills (1980)**: the balance between Fundamental Rights and DPSP is itself part of the basic structure. Later additions: 39A, 43A, 48A came with the 42nd Amendment; the 86th Amendment (2002) rewrote Article 45 to cover early childhood care below six years.

### Fundamental Duties — Part IV-A, Article 51A
Recommended by the **Swaran Singh Committee**; the **42nd Amendment (1976)** listed **ten** duties, and the **86th Amendment (2002)** added the **eleventh** — parents and guardians providing education opportunities to children aged 6–14. Modeled on the **USSR** constitution. They are non-enforceable by themselves, but courts use them to test reasonableness of laws, and laws can punish their breach (e.g., insult to the flag and anthem under the Prevention of Insults to National Honour Act).

### Quick revision
- Six FRs, Articles 14–32; property now Article 300A (legal right, 44th Amendment 1978).
- 17 = untouchability; 21 = life and liberty (Maneka 1978; privacy — Puttaswamy 2017); 21A = education 6–14 (86th, 2002).
- Writs: habeas corpus, mandamus, prohibition, certiorari, quo warranto; Art 32 (SC), Art 226 (HC, wider).
- DPSP from Ireland; Gandhian 40/43/46/47/48; socialist 38/39/39A/41/42; liberal 44 (UCC)/45/48A/49/50/51.
- Minerva Mills: FR–DPSP balance = basic structure.
- Duties: Swaran Singh Committee, 42nd Amendment, 10 + 1 (86th) = 11, model USSR."""
    S.pattern("ga-polfr-p1", "Article ↔ Fundamental Right mapping", "very common",
        "'Which Article abolishes untouchability', 'which Article gives the right to constitutional remedies', or a four-row article-right match.",
        None,
        "1. Learn 14–32 in blocks: 14–18 equality, 19–22 freedom, 23–24 exploitation, 25–28 religion, 29–30 cultural-educational, 32 remedies.\n2. Trap: right to property is **not** a Fundamental Right — it sits at Article 300A (44th Amendment, 1978).\n3. Single-article favourites: 17 untouchability, 21 life and liberty, 21A education (6–14), 32 writs.",
        "The abolition of **untouchability** is guaranteed under —",
        "**Article 17** — it abolishes untouchability and forbids its practice in any form; Parliament enforces it through the Protection of Civil Rights Act.")
    S.pattern("ga-polfr-p2", "Writs: which writ for which situation", "very common",
        "A situation (illegal detention, officer not doing duty, illegal occupant of office) is described and the writ asked.",
        None,
        "1. Detention → **habeas corpus**; duty not done → **mandamus**; office occupied illegally → **quo warranto**.\n2. Court orders: stopping a case midway → **prohibition**; quashing a finished order → **certiorari**.\n3. Article 32 = Supreme Court, fundamental rights; Article 226 = High Courts, **wider** (fundamental + other legal rights).",
        "A person illegally detained by the police should move the court for the writ of —",
        "**Habeas corpus** ('produce the body') — the court orders the detaining authority to produce the detainee and justify the detention.")
    S.pattern("ga-polfr-p3", "DPSP: classification and article recall", "common",
        "'Which of these is a Gandhian principle', 'uniform civil code is under which Article', statements clubbing DPSP with FRs.",
        None,
        "1. Gandhian = 40 (panchayats), 43 (cottage industry), 43B, 46, 47, 48; Socialist = 38, 39, 39A, 41, 42, 43A; Liberal = 44 (UCC), 45, 48A, 49, 50, 51.\n2. 44 = uniform civil code — the evergreen answer.\n3. DPSPs are non-justiciable ('not enforceable by any court') but 'fundamental in the governance of the country'.",
        "**Article 44** of the Constitution, a Directive Principle, provides for —",
        "A **uniform civil code** for all citizens — a liberal-intellectual directive; it remains unenforced and is often in the news in debate questions.")
    S.pattern("ga-polfr-p4", "Fundamental Duties: count, source, amendments", "common",
        "'How many fundamental duties', 'which committee recommended them', 'which amendment added the eleventh duty'.",
        None,
        "1. Count: **11 duties** today — 10 by the 42nd Amendment (1976), the 11th by the 86th (2002).\n2. Source: Swaran Singh Committee recommendation; modeled on the **USSR**.\n3. The 11th duty: parents/guardians provide education opportunities to children aged **6–14**.",
        "The **11th Fundamental Duty**, added by the 86th Amendment, asks every parent/guardian to —",
        "Provide opportunities for education to his/her child or ward between the age of **six and fourteen** years.")
    S.pattern("ga-polfr-p5", "FR–DPSP conflict and land mark cases", "occasional",
        "'Which case held FRs supreme?', 'balance of FR and DPSP is basic structure', property-right deletion cases.",
        None,
        "1. **Champakam Dorairajan (1951)**: FRs prevail over DPSPs → led to the 1st Amendment.\n2. **Kesavananda Bharati (1973)**: basic structure doctrine; **Minerva Mills (1980)**: FR–DPSP balance is basic structure.\n3. **Maneka Gandhi (1978)**: procedure limiting Article 21 must be fair, just and reasonable — not merely enacted.",
        "Which case held that the **balance between Fundamental Rights and Directive Principles** is part of the basic structure?",
        "**Minerva Mills (1980)** — the Court struck down the 42nd Amendment's attempt to give DPSPs primacy over Fundamental Rights.")

    S.q("ga-polfr-p1", "easy", "Which Article of the Constitution is called its '**heart and soul**' by Dr B.R. Ambedkar?",
        ["Article 14", "Article 19", "Article 21", "Article 32"], "Article 32",
        "**Article 32** (right to constitutional remedies) — Ambedkar's phrase, because without the writ power the other rights would be declarations only.",
        "Heart and soul = 32 = writs.", 20)
    S.q("ga-polfr-p1", "medium", "Free and compulsory education for children aged **6 to 14 years** is a Fundamental Right under —",
        ["Article 45", "Article 21A", "Article 51A(k)", "Article 30"], "Article 21A",
        "**Article 21A**, inserted by the **86th Amendment (2002)**. Article 45 was rewritten as a DPSP for early-childhood care below six; 51A(k) is the matching parental duty.",
        "21A = 86th = 6–14 years.", 20)
    S.q("ga-polfr-p1", "hard", "Which one of the following is **NOT** a Fundamental Right today?",
        ["Right against exploitation", "Right to property", "Right to freedom of religion", "Right to constitutional remedies"], "Right to property",
        "The **44th Amendment (1978)** removed property from Part III and made it a legal right under **Article 300A**. The other three are all Fundamental Rights.",
        "Property = Article 300A, a legal right — never Part III.", 25)
    S.q("ga-polfr-p2", "easy", "The writ of '**mandamus**' is issued to —",
        ["Produce a detained person before the court", "Command a public official to perform a public duty", "Quash an order of a lower court", "Question the authority of a person holding office"], "Command a public official to perform a public duty",
        "**Mandamus** ('we command') orders a public authority or official to do a duty it is legally bound to perform. Producing a detainee = habeas corpus; quashing = certiorari; office challenge = quo warranto.",
        "Mandamus = 'do your duty'.", 20)
    S.q("ga-polfr-p2", "medium", "Which writ can be issued to a person who occupies a **public office without legal authority**?",
        ["Certiorari", "Habeas corpus", "Quo warranto", "Prohibition"], "Quo warranto",
        "**Quo warranto** ('by what authority') asks the occupant to show the legal title to the office. Prohibition stops a lower court mid-case; certiorari quashes its order later.",
        "Quo warranto = 'what is your authority?'.", 25)
    S.q("ga-polfr-p3", "medium", "The Directive Principle calling for a **uniform civil code** for all citizens is contained in —",
        ["Article 40", "Article 44", "Article 48", "Article 51"], "Article 44",
        "**Article 44** — the flagship liberal-intellectual directive. Article 40 = village panchayats, 48 = agriculture and animal husbandry, 51 = international peace and security.",
        "44 = UCC; 40 = panchayats; 51 = world peace.", 20)
    S.q("ga-polfr-p3", "medium", "Which of the following is a **Gandhian** Directive Principle?",
        ["Free legal aid (Art 39A)", "Promotion of cottage industries (Art 43)", "Separation of judiciary from executive (Art 50)", "Uniform civil code (Art 44)"], "Promotion of cottage industries (Art 43)",
        "**Art 43** (village and cottage industries) is Gandhian. 39A is socialist, while 50 and 44 are liberal-intellectual directives.",
        "Gandhian set: 40, 43, 43B, 46, 47, 48.", 25)
    S.q("ga-polfr-p4", "easy", "How many **Fundamental Duties** does Article 51A contain at present?",
        ["Ten", "Eleven", "Twelve", "Nine"], "Eleven",
        "**Eleven** — ten were listed by the **42nd Amendment (1976)** on the Swaran Singh Committee's advice, and the **86th Amendment (2002)** added the duty of parents to educate children aged 6–14.",
        "10 + 1 = 11 (42nd, then 86th).", 20)
    S.q("ga-polfr-p4", "medium", "Fundamental Duties were added to the Constitution on the recommendation of —",
        ["Sarkaria Commission", "Swaran Singh Committee", "Balwant Rai Mehta Committee", "Administered Reforms Commission"], "Swaran Singh Committee",
        "The **Swaran Singh Committee** (1976) recommended the duties; the 42nd Amendment inserted them. The Sarkaria Commission dealt with Centre-state relations.",
        "Duties = Swaran Singh; PRI tiers = Balwant Rai Mehta.", 20)
    S.q("ga-polfr-p5", "hard", "Which one of the following statements is **correct**?",
        ["Directive Principles are enforceable by courts like Fundamental Rights", "In Champakam Dorairajan, the Supreme Court held Fundamental Rights prevail over DPSPs", "The 42nd Amendment made Fundamental Rights superior to DPSPs", "Right to property is still a Fundamental Right"], "In Champakam Dorairajan, the Supreme Court held Fundamental Rights prevail over DPSPs",
        "**Champakam Dorairajan (1951)** held FRs prevail over DPSPs — it triggered the 1st Amendment. DPSPs are non-justiciable; the 42nd tried DPSP primacy (struck down in Minerva Mills); property left Part III in 1978.",
        "1951: FR > DPSP; 1980: balance = basic structure.", 30)
    S.q("ga-polfr-p5", "medium", "In **Maneka Gandhi v. Union of India (1978)**, the Supreme Court laid down that any law restricting personal liberty must be —",
        ["Passed by Parliament by a two-thirds majority", "Fair, just and reasonable, not merely enacted procedure", "Approved by the President", "Certified by the Attorney General"], "Fair, just and reasonable, not merely enacted procedure",
        "Maneka Gandhi read fairness into **Article 21**: 'procedure established by law' must be right, just and fair — a step toward the American 'due process' idea.",
        "Maneka = fairness inside Art 21.", 25)
    return S


def build_executive():
    S = Sub("pol-executive")
    S.notes = """### The President — Articles 52 to 62
The President is the **head of the State** (first citizen), while the Prime Minister heads the government. Election (Articles 54–55) is **indirect**, by an electoral college of **elected MPs** and **elected MLAs of the states**, plus elected MLAs of **Delhi and Puducherry** (added by the 70th Amendment). Nominated members and MLCs do **not** vote. The system is **proportional representation by single transferable vote**; vote values are worked out from the **1971 census** (frozen for this purpose). Disputes are decided by the **Supreme Court** (Article 71). Term: **5 years**; oath administered by the **Chief Justice of India**; resignation addressed to the **Vice-President**. Removal is by **impeachment (Article 61)** for 'violation of the Constitution' — no ground is defined, and the charge can be raised in **either House** (special majority of both, investigated under procedure fixed by each House).

The veto family: **absolute** veto (withholding assent), **suspensive** veto (returning a bill once — if passed again, assent is obligatory), **pocket** veto (sitting on a bill — no time limit; used by President Zail Singh on the Indian Post Office (Amendment) Bill, 1986). For **state** bills the President has an **absolute** veto (Article 201). Ordinance power — **Article 123**: when Parliament is not in session; must be laid before Parliament; ceases six weeks after Parliament reassembles. Pardoning power — **Article 72**: **pardon** (full absolution), **commutation** (substitute a lighter punishment), **remission** (reduce the amount), **respite** (lesser sentence for special reasons, e.g. pregnancy), **reprieve** (temporary stay). It extends to **death sentences, courts-martial and Union-law offences**.

### The Vice-President — Articles 63 to 71
Elected by **all members (elected + nominated) of both Houses** — no state legislatures. Ex-officio **Chairman of the Rajya Sabha**; acts as President when the office falls vacant, for a maximum of **6 months**. Removal: a resolution of the **Rajya Sabha by an effective majority (majority of all then members), with 14 days' notice**, agreed to by the Lok Sabha by simple majority.

### Prime Minister and Council of Ministers — Articles 74 to 75
The **real executive**. Article 74 requires the President to act on the aid and advice of the Council of Ministers; the 42nd and 44th Amendments made this advice binding (President may return it once). The CoM is **collectively responsible to the Lok Sabha (Article 75(3))**; ministers hold office during the President's pleasure. **91st Amendment (2003)**: CoM strength capped at **15% of the Lok Sabha** (minimum **12**); the same cap applies in states. A minister not in Parliament must become one within **6 months**. The **Attorney-General (Article 76)** is the Union's chief law officer — he may speak and take part in **both Houses** but has **no vote**.

### The Governor — Articles 153 to 161
Appointed by the President (not elected); holds office during the President's **pleasure**, though the constitutional term is **5 years**; must be an outsider to the state (convention). Legislative powers include summoning the assembly and **ordinances (Article 213)**; can reserve state bills for the President. Pardoning power (**Article 161**) is **narrower** than the President's: the Governor **cannot pardon a death sentence** (may suspend, remit or commute it) and cannot act in courts-martial cases. The State Council of Ministers follows the same 15% cap (minimum 12) with collective responsibility to the assembly.

### Quick revision
- President: elected MPs + elected MLAs (states + Delhi + Puducherry); PR-STV; 1971 census values; SC decides disputes (Art 71).
- Impeachment Art 61 — 'violation of the Constitution'; either House can start it.
- Vetoes: absolute, suspensive, pocket; pocket used in 1986 (Post Office Bill); state bills = absolute veto of President.
- Art 123 ordinance: 6 weeks from reassembly. Art 72 pardon: death, court-martial, Union law.
- VP: both Houses elect (incl. nominated); RS Chairman; removal only from RS (effective majority, 14 days' notice).
- CoM cap 15% (min 12) — 91st Amendment; AG Art 76 speaks but never votes.
- Governor: pleasure of President; no pardon for death sentence (Art 161)."""
    S.pattern("ga-polexe-p1", "President's election and impeachment", "very common",
        "'Who elects the President', 'which members do not vote', 'value of vote based on which census', impeachment grounds/procedure.",
        None,
        "1. Electors: elected MPs + elected MLAs of states + elected MLAs of Delhi and Puducherry (70th Amendment). Nominated MPs and MLCs stay out.\n2. Method: proportional representation, single transferable vote, secret ballot; values from the **1971 census**.\n3. Impeachment (Art 61): charge = 'violation of the Constitution' (undefined); can start in **either House**; needs special majority of both.",
        "The value of the vote of an MLA in the **Presidential election** is calculated with reference to the population figures of the —",
        "**1971 census** — the 42nd and 84th Amendments froze the 1971 base for presidential elections and delimitation alike.")
    S.pattern("ga-polexe-p2", "President's powers: veto, ordinance, pardon", "very common",
        "'The pocket veto was used for which bill', 'which article empowers ordinances', 'the President can pardon which punishments', statement questions mixing the three.",
        None,
        "1. Vetoes: absolute (withhold), suspensive (return once), pocket (no time limit — Zail Singh, Indian Post Office (Amendment) Bill, 1986).\n2. Ordinance = **Article 123**: only when Parliament is not in session; dies **6 weeks after reassembly** unless approved.\n3. Pardon (Art 72): death sentence, courts-martial, Union-law offences. Five shades: pardon, commutation, remission, respite, reprieve.",
        "The so-called '**pocket veto**' of the President refers to —",
        "Keeping a bill **without acting on it** — the Constitution sets no time limit for assent; President Zail Singh did this to the Indian Post Office (Amendment) Bill, 1986.")
    S.pattern("ga-polexe-p3", "Vice-President: election and removal", "common",
        "'Who elects the Vice-President', 'how can the VP be removed', 'who acts as President and for how long'.",
        None,
        "1. Electors = **all members of both Houses** — elected **and** nominated; no state legislatures. This is the key difference from the President's election.\n2. Ex-officio Chairman of the Rajya Sabha; acts as President up to **6 months** in a vacancy.\n3. Removal only through the **Rajya Sabha**: effective majority + **14 days' notice**, then Lok Sabha concurs by simple majority.",
        "The Vice-President of India is elected by —",
        "An electoral college consisting of **all members of both Houses of Parliament** (elected and nominated) — state legislatures take no part, unlike in the President's election.")
    S.pattern("ga-polexe-p4", "PM and Council of Ministers", "common",
        "Statement questions on collective responsibility, the 15% cap, a non-member minister's 6-month window, the Attorney-General's rights in Parliament.",
        None,
        "1. Collective responsibility to the **Lok Sabha** — Art 75(3); ministers hold office during the President's pleasure.\n2. **91st Amendment (2003)**: CoM ≤ 15% of the House, minimum 12 — applies to the Union and to states.\n3. A minister who is not an MP must get elected to either House within **6 months**. The AG (Art 76) can speak in Parliament but cannot vote.",
        "The strength of the Union Council of Ministers is capped by the **91st Amendment** at —",
        "**15% of the strength of the Lok Sabha**, with a constitutional floor of **12 ministers** (which includes the Prime Minister).")
    S.pattern("ga-polexe-p5", "Governor: appointment, powers, pardon", "common",
        "'The Governor is appointed by', 'can the Governor pardon a death sentence', 'who administers the oath to the Governor', reserve-bill questions.",
        None,
        "1. Appointed by the President; holds office during the President's pleasure; term nominally 5 years.\n2. Pardon (Art 161): **no death-sentence pardon** — only suspension, remission or commutation; no courts-martial power.\n3. Can reserve state bills for the President (Art 200–201); the President then has an **absolute** veto; ordinances = Art 213.",
        "Which statement about the Governor's pardoning power is **correct**?",
        "Under **Article 161** the Governor can suspend, remit or commute a death sentence but **cannot pardon** it — full pardon of a death sentence belongs to the President alone.")

    S.q("ga-polexe-p1", "easy", "The President of India is elected by —",
        ["The people directly", "An electoral college of elected MPs and elected MLAs", "Parliament by simple majority", "The Supreme Court judges"], "An electoral college of elected MPs and elected MLAs",
        "The electoral college has **elected MPs**, **elected MLAs of the states**, and (since the 70th Amendment) elected MLAs of **Delhi and Puducherry**. Voting is by proportional representation, single transferable vote.",
        "Elected MPs + elected MLAs (states, Delhi, Puducherry).", 20)
    S.q("ga-polexe-p1", "hard", "Consider the statements about the President's election:\n1. Nominated members of the Rajya Sabha can vote.\n2. Members of State Legislative Councils cannot vote.\n3. Election disputes are decided by the Election Commission.\nWhich are correct?",
        ["2 only", "1 and 2", "1 and 3", "1, 2 and 3"], "2 only",
        "Statement 2 alone is right. Nominated MPs **cannot** vote (statement 1 wrong); disputes go to the **Supreme Court** under Article 71, not the Election Commission (statement 3 wrong).",
        "Only elected members vote; SC decides disputes.", 30)
    S.q("ga-polexe-p1", "medium", "An impeachment charge against the President for 'violation of the Constitution' may be preferred —",
        ["Only in the Lok Sabha", "Only in the Rajya Sabha", "In either House of Parliament", "Only by the Supreme Court"], "In either House of Parliament",
        "Under **Article 61** the charge can originate in **either House**, which then investigates; removal needs a **special majority of both Houses**. No ground is defined in the Constitution.",
        "Either House may start; both must finish.", 25)
    S.q("ga-polexe-p2", "easy", "The **ordinance-making power** of the President is contained in —",
        ["Article 72", "Article 123", "Article 213", "Article 356"], "Article 123",
        "**Article 123** lets the President promulgate ordinances when **both Houses of Parliament are not in session**; an ordinance lapses **six weeks** after Parliament reassembles unless approved. Article 213 is the Governor's counterpart.",
        "123 = Union; 213 = state.", 20)
    S.q("ga-polexe-p2", "medium", "The pardoning power of the President under Article 72 extends to —",
        ["Only Union-law offences", "Death sentences and Union-law offences only", "Death sentences, courts-martial sentences and Union-law offences", "All sentences passed by any court in India"], "Death sentences, courts-martial sentences and Union-law offences",
        "Article 72 covers **death sentences**, sentences of **courts-martial** and offences against **Union laws**. The Governor's power (Article 161) is narrower — no death pardon, no courts-martial.",
        "President = death + martial + Union law.", 25)
    S.q("ga-polexe-p2", "medium", "Which punishment-modifying power **substitutes a lighter form** of punishment for a heavier one?",
        ["Remission", "Respite", "Commutation", "Reprieve"], "Commutation",
        "**Commutation** substitutes one punishment for a lighter one of a different character (e.g. death → life imprisonment). Remission **reduces the amount**; respite awards a lesser sentence for special reasons; reprieve is a temporary stay.",
        "Commutation = change character; remission = cut amount.", 25)
    S.q("ga-polexe-p3", "medium", "The Vice-President of India can be removed by a resolution —",
        ["Of the Lok Sabha by special majority", "Of the Rajya Sabha by effective majority with 14 days' notice, agreed to by the Lok Sabha", "Passed by both Houses by two-thirds of the total membership", "Of the Cabinet approved by the President"], "Of the Rajya Sabha by effective majority with 14 days' notice, agreed to by the Lok Sabha",
        "Removal starts (and effectively decides) in the **Rajya Sabha**: majority of all then members, **14 days' notice**; the Lok Sabha then needs only a simple majority. No ground is specified in the Constitution.",
        "VP removal = RS first, 14 days' notice.", 25)
    S.q("ga-polexe-p3", "easy", "In the absence of the President, who officiates, and for how long at most?",
        ["The Prime Minister, 1 year", "The Chief Justice of India, 6 months", "The Vice-President, 6 months", "The Speaker, 3 months"], "The Vice-President, 6 months",
        "The **Vice-President acts as President** for up to **6 months** (Article 65). If a fresh election cannot happen in that period, Article 71 (as interpreted) allows the term to extend until a new President assumes office.",
        "Vacancy → VP, 6 months.", 20)
    S.q("ga-polexe-p4", "medium", "The **91st Constitutional Amendment Act, 2003** capped the size of the Council of Ministers at —",
        ["10% of the strength of the Lok Sabha", "15% of the strength of the Lok Sabha", "20% of the strength of the Lok Sabha", "25% of the strength of the Lok Sabha"], "15% of the strength of the Lok Sabha",
        "The cap is **15%** of the House's strength, with a minimum of **12 ministers**, and it applies equally to state Councils of Ministers. It also barred defectors from ministerial office.",
        "15% — ninety-one = fifteen-one.", 20)
    S.q("ga-polexe-p4", "medium", "Which statement about the **Attorney-General of India** is correct?",
        ["He must be a member of the Lok Sabha", "He has the right to speak in Parliament but cannot vote", "He is appointed by the Chief Justice of India", "His advice is binding on the government"], "He has the right to speak in Parliament but cannot vote",
        "Under **Article 76** the AG is the government's chief legal adviser, appointed by the President; he may **speak and take part** in either House or their committees but has **no right to vote**.",
        "AG: speaks, never votes.", 25)
    S.q("ga-polexe-p5", "easy", "The **Governor** of a state is —",
        ["Elected by the state legislature", "Appointed by the President", "Elected by the people of the state", "Appointed by the Chief Minister"], "Appointed by the President",
        "The Governor is **appointed by the President** (Article 155) and holds office during the President's pleasure; the constitutional term is five years — a Canadian borrowing.",
        "Governor = President's appointee.", 20)
    S.q("ga-polexe-p5", "hard", "Consider the statements:\n1. The Governor can pardon a sentence of death.\n2. The Governor can commute a death sentence.\n3. The Governor's pardoning power covers courts-martial cases.\nWhich are correct?",
        ["2 only", "1 and 2", "2 and 3", "1, 2 and 3"], "2 only",
        "Only statement 2 is correct — under **Article 161** the Governor may **suspend, remit or commute** a death sentence but cannot **pardon** it, and courts-martial cases lie wholly outside the Governor's power.",
        "Governor: commute yes, pardon no, martial never.", 30)
    return S
