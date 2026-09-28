"""polity deep content — part 2: pol-parliament-judiciary, pol-amendments, pol-local-bodies-emergency, pol-bodies."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_parliament():
    S = Sub("pol-parliament-judiciary")
    S.notes = """### Parliament — Articles 79 to 122
Parliament = **President + Rajya Sabha + Lok Sabha**. The Lok Sabha is capped at **552** (530 states + 20 UTs; the two nominated Anglo-Indian seats ended with the **104th Amendment, 2020**). The Rajya Sabha is capped at **250** — 238 elected plus **12 nominated** (literature, science, art, social service). Rajya Sabha members are elected by MLAs by **single transferable vote** (Seat allocation: Fourth Schedule); term is **6 years**, one-third retiring every two years, and it is a **permanent House** — never dissolved. Lok Sabha's normal term is **5 years**. The minimum age is **25** (Lok Sabha) and **30** (Rajya Sabha). A gap between two sessions cannot exceed **6 months**; quorum = **one-tenth** of the total membership. The **Speaker** is elected by the Lok Sabha, resigns to the Deputy Speaker, has a **casting vote**, certifies **Money Bills**, and presides over joint sittings (in the Speaker's absence, the Deputy Speaker Rajya Sabha's Deputy Chairman steps in). **Article 108** provides for **joint sittings** to break deadlocks on ordinary bills — **never** for Money Bills or Constitution Amendment Bills; only **three** joint sittings have been held (Dowry Prohibition Bill 1960, Banking Service Commission (Repeal) Bill 1977, POTA 2002).

### Bills and motions
A **Money Bill (Article 110)** contains only the six listed matters (taxes, borrowing, custody of the Consolidated Fund, etc.). It can be introduced **only in the Lok Sabha**, only on the **President's recommendation**, and the Rajya Sabha must return it within **14 days** (it can only recommend). The **Speaker's certificate** is final. Financial Bill-I (Art 117(1)) mixes money and other matters — treat it like an ordinary bill; Financial Bill-II (Art 117(3)) involves expenditure from the CFI but is otherwise ordinary. Motions: **no-confidence** (Lok Sabha only, 50 members' support), censure, adjournment, calling attention, privilege. **Cut motions** — policy cut (₹1), economy cut (specified amount), token cut (₹100). Financial committees: **Public Accounts Committee — 22 members (15 LS + 7 RS), chairman from the opposition by convention**; **Estimates Committee — 30 members, all from the Lok Sabha**; Public Undertakings — 22.

### The Supreme Court — Articles 124 to 147
Sanctioned strength: **34 judges including the CJI**. Judges are appointed by the President; since the **Second and Third Judges cases** the **collegium** (CJI + senior judges) recommends names; the 99th Amendment's NJAC (2014) was struck down in 2015. Qualifications: citizen + (HC judge for 5 years) or (HC advocate for 10 years) or a distinguished jurist; retirement at **65**. Removal: 'proved misbehaviour or incapacity', special majority of both Houses, process governed by the **Judges (Inquiry) Act, 1968** (100 Lok Sabha / 50 Rajya Sabha signatures to start). Jurisdiction: **original** (Article 131 — Centre-state disputes), **writ** (32), **appellate** (132–136; Article 136 — special leave to appeal), **review** (137), **advisory** (143 — President may refer questions of law/fact), and **record** (Article 141 — its law binds all courts). **Judicial review** flows from Article 13; the **basic structure** doctrine comes from **Kesavananda Bharati (1973)**.

### The High Courts and below
Articles 214–231: one HC per state (Parliament may create a common HC). Judges retire at **62**; appointed by the President after consultation with the CJI and the Governor. Courts of subordinate jurisdiction are regulated by the states; **Lok Adalats** (Legal Services Authorities Act, 1987) settle disputes by compromise and their awards are deemed decrees.

### Quick revision
- LS max 552, age 25; RS max 250 (12 nominated), age 30, permanent, 6-year terms, STV by MLAs.
- Sessions gap ≤ 6 months; quorum 1/10; Speaker certifies Money Bills; joint sittings: 3, never for Money Bills.
- Money Bill: LS only, President's recommendation, RS 14 days, Speaker's certificate final.
- PAC 22 (15+7, opposition chair); Estimates 30 (all LS, ruling chair by convention).
- SC: 34 judges, retire 65, collegium (99th Amendment struck down 2015); removal = special majority both Houses.
- Jurisdiction map: 131 original, 136 SLP, 137 review, 141 binding, 143 advisory; writs 32/226; HC judge retires 62."""
    S.pattern("ga-polvj-p1", "Money Bill and bill procedures", "very common",
        "'A Money Bill can be introduced only in', 'Rajya Sabha must return a Money Bill within', 'whose certificate decides if a bill is a Money Bill', statement sets on bill types.",
        None,
        "1. Money Bill (Art 110): Lok Sabha only, on the President's recommendation; Rajya Sabha gets **14 days** with recommend-only power; the **Speaker's certificate is final**.\n2. Joint sitting (Art 108) applies to ordinary (and Financial Bill-I) deadlocks — **never** to Money Bills or Constitution Amendment Bills.\n3. The six Money-Bill subjects all concern taxes, borrowing or the Consolidated Fund — check the stem for those words.",
        "The Rajya Sabha must return a **Money Bill** to the Lok Sabha within —",
        "**14 days** — it may only make recommendations, which the Lok Sabha is free to accept or reject; the bill then goes to the President.")
    S.pattern("ga-polvj-p2", "Motions and financial committees", "common",
        "'A no-confidence motion needs the signature of how many members', 'which committee has members only from the Lok Sabha', cut-motion amounts, PAC chairman convention.",
        None,
        "1. No-confidence: **Lok Sabha only**, **50 members** to admit; if passed, the ministry resigns.\n2. Committees: Estimates = **30, all Lok Sabha**; PAC and Public Undertakings = **22 each (15 + 7)**; PAC chairman from the **opposition** by convention.\n3. Cut motions: policy cut ₹1, economy cut a stated sum, token cut ₹100.",
        "The **Estimates Committee** of Parliament consists of —",
        "**30 members, all drawn from the Lok Sabha** (elected by proportional representation); its chairman is appointed by the Speaker from the ruling side.")
    S.pattern("ga-polvj-p3", "Parliament's structure: numbers, ages, sessions", "very common",
        "'Maximum strength of the Rajya Sabha', 'minimum age for the Lok Sabha', 'nominated members of the Rajya Sabha', 'maximum gap between sessions'.",
        None,
        "1. Numbers: LS 552 (Anglo-Indian nomination ended by the 104th Amendment, 2020); RS 250 = 238 + 12 nominated.\n2. Ages: 25 (LS) / 30 (RS); RS term 6 years (one-third retire every 2 years); LS 5 years.\n3. Sessions: budget, monsoon, winter; the gap between sessions cannot exceed **6 months**; quorum = 1/10.",
        "The **Rajya Sabha** can have at most how many members?",
        "**250** — 238 representing states and Union Territories plus **12 nominated** by the President for distinction in literature, science, art and social service.")
    S.pattern("ga-polvj-p4", "Supreme Court: appointment, removal, jurisdiction", "very common",
        "'How are SC judges appointed', 'on what ground can a judge be removed', 'which article gives advisory jurisdiction', retirement ages and collegium statements.",
        None,
        "1. Strength 34 (incl. CJI); appointed by the President on the **collegium's** recommendation (Second/Third Judges cases); NJAC (99th Amendment) struck down in 2015.\n2. Removal: 'proved misbehaviour or incapacity', **special majority of both Houses**, procedure under the Judges (Inquiry) Act 1968 (100 LS / 50 RS members to move).\n3. Jurisdiction anchors: 131 original, 136 SLP, 137 review, 141 law of the land binding, 143 advisory; retire at **65**.",
        "Under which jurisdiction does the Supreme Court answer **questions of law referred by the President**?",
        "**Advisory jurisdiction — Article 143**: the President may refer a question of law or fact of public importance; the Court may report its opinion, which is not binding as a judgment.")
    S.pattern("ga-polvj-p5", "High Courts and Lok Adalats", "occasional",
        "'Retirement age of an HC judge', 'who appoints HC judges', 'Lok Adalat award is equivalent to', common High Court questions.",
        None,
        "1. HC judges appointed by the President after consultation (CJI + Governor); retire at **62** (SC: 65).\n2. Article 226 writ power is **wider** than Article 32 — it covers legal rights too.\n3. Lok Adalats (Legal Services Authorities Act, 1987): awards are **deemed decrees of a civil court**, no appeal on merits.",
        "Every **Lok Adalat** award is deemed to be —",
        "A **decree of a civil court** and is final; it is binding on the parties, and no appeal lies against it on the merits.")

    S.q("ga-polvj-p1", "easy", "A **Money Bill** can be introduced only in the —",
        ["Rajya Sabha", "Lok Sabha", "Either House", "Joint sitting of both Houses"], "Lok Sabha",
        "Article 110 confines Money Bills to the **Lok Sabha**, and only on the **President's recommendation**. The Rajya Sabha must return it within 14 days with recommendations only.",
        "Money = Lok Sabha only + President's nod.", 20)
    S.q("ga-polvj-p1", "medium", "Consider the statements:\n1. The Speaker's decision on whether a bill is a Money Bill is final.\n2. A joint sitting can be summoned for a Money Bill.\n3. A joint sitting has been held three times so far.\nWhich are correct?",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "1 and 3 only",
        "Statements 1 and 3 are correct. Statement 2 is wrong — Article 108 excludes **Money Bills** and Constitution Amendment Bills from joint sittings. The three joint sittings: Dowry Prohibition (1961), Banking Service Commission Repeal (1978), POTA (2002).",
        "No joint sitting for Money Bills — ever.", 30)
    S.q("ga-polvj-p2", "medium", "A **no-confidence motion** in the Lok Sabha requires the support of at least —",
        ["100 members", "50 members", "55 members", "One-tenth of the total membership"], "50 members",
        "**50 members** must stand up to admit the motion (Rule 198); it can be moved only in the **Lok Sabha** against the Council of Ministers as a whole.",
        "No-confidence = 50, LS only.", 20)
    S.q("ga-polvj-p2", "medium", "Which parliamentary committee has **members only from the Lok Sabha**?",
        ["Public Accounts Committee", "Committee on Public Undertakings", "Estimates Committee", "Committee on Privileges"], "Estimates Committee",
        "The **Estimates Committee** has **30 members, all from the Lok Sabha**. PAC and Public Undertakings each have 22 members (15 Lok Sabha + 7 Rajya Sabha).",
        "Estimates = all-LS club of 30.", 25)
    S.q("ga-polvj-p3", "easy", "The **maximum strength** of the Rajya Sabha provided by the Constitution is —",
        ["238", "245", "250", "552"], "250",
        "Article 80 caps the Rajya Sabha at **250** — 238 representatives of states and UTs plus **12 nominated** members. The present House sits at 245.",
        "Cap 250; current 245.", 20)
    S.q("ga-polvj-p3", "medium", "The maximum **gap between two consecutive sessions** of Parliament cannot exceed —",
        ["3 months", "4 months", "6 months", "1 year"], "6 months",
        "Article 85: sessions must be held so that **no more than six months** pass between one session's end and the next's start — hence at least two sessions a year.",
        "Six-month ceiling = at least two sessions yearly.", 20)
    S.q("ga-polvj-p4", "easy", "A judge of the **Supreme Court** retires at the age of —",
        ["60", "62", "65", "68"], "65",
        "Supreme Court judges retire at **65**; High Court judges at **62**. Removal before that needs proved misbehaviour or incapacity and a special majority of both Houses.",
        "SC 65, HC 62.", 20)
    S.q("ga-polvj-p4", "medium", "The **advisory jurisdiction** of the Supreme Court flows from —",
        ["Article 131", "Article 136", "Article 141", "Article 143"], "Article 143",
        "**Article 143** — the President may refer questions of law or fact of public importance to the Court. 131 is original jurisdiction; 136 is special leave to appeal; 141 makes SC law binding on all courts.",
        "143 = advice to the President.", 25)
    S.q("ga-polvj-p4", "hard", "The **National Judicial Appointments Commission (NJAC)** set up by the 99th Amendment was struck down by the Supreme Court in —",
        ["2014", "2015", "2016", "2018"], "2015",
        "In the **Fourth Judges case (October 2015)** the Court struck down the 99th Amendment and the NJAC Act as violative of judicial independence (basic structure), restoring the **collegium** system.",
        "99th in, struck down 2015 — collegium restored.", 30)
    S.q("ga-polvj-p5", "medium", "A judge of a **High Court** is appointed by —",
        ["The Governor of the state", "The Chief Minister", "The President", "The Chief Justice of India"], "The President",
        "**The President** appoints HC judges after consultation with the CJI and the state Governor (collegium recommendations since the Judges cases). Tenure runs to age **62**.",
        "President appoints, Governor consulted.", 25)
    S.q("ga-polvj-p5", "medium", "An award of a **Lok Adalat** is —",
        ["Only advisory to the parties", "Deemed a decree of a civil court and binding", "Subject to a regular appeal on merits", "Valid only if confirmed by the High Court"], "Deemed a decree of a civil court and binding",
        "Under the Legal Services Authorities Act, 1987, a Lok Adalat award is **deemed a civil-court decree**, final and binding on the parties; no appeal lies on the merits.",
        "Lok Adalat award = decree, final.", 25)
    return S


def build_amendments():
    S = Sub("pol-amendments")
    S.notes = """### How the Constitution is amended — Article 368
Amendment power sits in **Part XX, Article 368** (borrowed from South Africa). Three routes:
- **Simple majority** of Parliament (outside Article 368): creating new states, altering state boundaries, citizenship rules, salaries of constitutional functionaries, the Second, Fifth and Sixth Schedules.
- **Special majority** (Article 368 route): majority of total membership of each House **plus** two-thirds of members present and voting — used for most amendments, including Fundamental Rights.
- **Special majority + ratification by half the state legislatures** — for federal provisions: election of the President (54–55), extent of Union/state executive power, Articles 73/162, Supreme Court and High Courts (124–147, 214–231, 241), distribution of legislative power and the Seventh Schedule, representation of states in Parliament, and Article 368 itself.

There is **no** special convention for joint sittings — a Constitution Amendment Bill never goes to a joint sitting — and the President **must give assent** (24th Amendment). There is no time limit for state ratification.

### The landmarks
| Amendment | What it did |
|---|---|
| **1st, 1951** | Ninth Schedule; Articles 31A/31B; 'reasonable restrictions' on free speech |
| **7th, 1956** | States reorganisation; abolished A/B/C/D state classes; repealed Part VII |
| **24th, 1971** | Parliament can amend **any** part, including Fundamental Rights |
| **42nd, 1976** | '**Mini-Constitution**': socialist, secular, integrity; Fundamental Duties; tribunals; DPSP primacy attempt; LS term extended to 6 years |
| **44th, 1978** | Property deleted from FRs (Article 300A); 'armed rebellion' replaced 'internal disturbance'; emergency approvals tightened; LS term back to 5 years |
| **52nd, 1985** | Anti-defection law (Tenth Schedule) |
| **61st, 1989** | Voting age **21 → 18** (Article 326) |
| **69th, 1991** | Delhi as **National Capital Territory** |
| **73rd / 74th, 1992** | Panchayats (Part IX, 11th Schedule) and Municipalities (Part IX-A, 12th Schedule) |
| **86th, 2002** | Article 21A (education 6–14); Article 45 rewritten; 11th Fundamental Duty |
| **91st, 2003** | Council of Ministers capped at 15% (min 12); defection bar tightened |
| **92nd, 2003** | Bodo, Dogri, Maithili, Santhali added to the Eighth Schedule (22 languages) |
| **97th, 2011** | Cooperative societies — new Part IX-B; 'cooperative societies' added to Article 19(1)(c) |
| **99th, 2014** | NJAC — struck down by the Supreme Court (2015) |
| **100th, 2015** | India–Bangladesh Land Boundary Agreement |
| **101st, 2016** | **GST** (Articles 246A, 269A, 279A — GST Council) |
| **102nd, 2018** | National Commission for Backward Classes given constitutional status (Article 338B) |
| **103rd, 2019** | **10% reservation for EWS** (Articles 15(6), 16(6)) |
| **104th, 2020** | Ended Anglo-Indian nomination; extended SC/ST reservation in legislatures |
| **105th, 2021** | Restored states' power to identify SEBCs (OBCs) |
| **106th, 2023** | **One-third seats for women** in Lok Sabha, state assemblies and Delhi assembly (after delimitation, for 15 years) |

The most recent number to remember: **106 amendments so far** (the 106th was enacted in September 2023).

### Quick revision
- Three routes: simple majority (outside 368), special majority, special majority + half-state ratification.
- Ratification list = federal items: President's election, SC/HCs, Seventh Schedule, state representation, Article 368.
- 42nd = Mini-Constitution; 44th = property out, 'armed rebellion' in; 52nd = defection; 61st = vote at 18.
- 73/74 = PRI + Municipalities; 86 = 21A + 11th duty; 101 = GST; 103 = EWS 10%; 106 = women's one-third.
- Constitutional Amendment Bills: no joint sitting; President's assent obligatory (24th Amendment)."""
    S.pattern("ga-polam-p1", "Amendment procedure and state ratification", "very common",
        "'Which provisions need ratification by half the states', 'what majority amends Fundamental Rights', statement sets on Article 368.",
        None,
        "1. Special majority = majority of **total membership** of each House + **two-thirds present and voting**; Fundamental Rights are amended by this route.\n2. Ratification (half the state legislatures) is needed only for **federal** items: President's election, SC/HCs, Seventh Schedule, state representation in Parliament, Union-state executive power, Article 368.\n3. Simple-majority items (new states, boundaries) sit **outside** Article 368; a Constitutional Amendment Bill never goes to a joint sitting.",
        "Amendment of which of the following requires **ratification by at least half of the state legislatures**?",
        "Any change touching **federal provisions** — e.g. the election of the President, the Seventh Schedule, or the representation of states in Parliament (besides a special majority in Parliament).")
    S.pattern("ga-polam-p2", "42nd and 44th — the twin landmarks", "very common",
        "'Which amendment is called the Mini-Constitution', 'which amendment removed the right to property', 'armed rebellion replaced internal disturbance by which amendment'.",
        None,
        "1. **42nd (1976)**: socialist/secular/integrity, Fundamental Duties, tribunals, DPSP-primacy line, LS term to 6 years — the 'Mini-Constitution'.\n2. **44th (1978)**: property out of Part III (300A), 'armed rebellion' replaces 'internal disturbance', emergency approval window cut to one month, LS term back to 5 years.\n3. The two travel as a pair — 42nd added, 44th corrected.",
        "The words '**armed rebellion**' in Article 352 replaced which earlier expression?",
        "'**Internal disturbance**' — substituted by the **44th Amendment Act, 1978**, to make the emergency ground more specific and serious.")
    S.pattern("ga-polam-p3", "Recent amendments (2016–2023)", "common",
        "'The 101st Amendment deals with', 'the 103rd Amendment provides for', 'the 106th Amendment is about', matching amendments 101–106 to provisions.",
        None,
        "1. **101st = GST**, 102nd = NCBC constitutional status (Art 338B), 103rd = **EWS 10%** (15(6), 16(6)), 104th = Anglo-Indian nomination ended, 105th = states identify OBCs, 106th = **women's one-third reservation**.\n2. 99th (NJAC) was struck down — remember it as the amendment that never survived.\n3. 100th = India–Bangladesh Land Boundary; 97th = cooperative societies.",
        "The **106th Constitutional Amendment Act (2023)** provides for —",
        "**One-third reservation of seats for women** in the Lok Sabha, state legislative assemblies and the Delhi assembly — to operate after the next delimitation, for 15 years.")
    S.pattern("ga-polam-p4", "Older amendments: one-line recall", "common",
        "'Voting age was lowered by which amendment', 'anti-defection law was added by', 'which amendment made Delhi the NCT', 'which amendment added the Ninth Schedule'.",
        None,
        "1. Numbers ladder: 1st — Ninth Schedule; 7th — states reorganisation; 52nd — defection; 61st — vote at 18; 69th — Delhi NCT.\n2. 73rd/74th — PRI/Municipalities; 86th — 21A; 91st — 15% ministry cap; 92nd — four languages.\n3. Pair each number with a one-word hook: 61-eighteen, 69-Delhi, 101-GST.",
        "The voting age in elections to the Lok Sabha and state assemblies was reduced from 21 to 18 years by the —",
        "**61st Constitutional Amendment Act, 1989**, which amended Article 326.")

    S.q("ga-polam-p1", "easy", "The procedure for amendment of the Constitution is laid down in —",
        ["Part XVIII", "Article 368", "Article 356", "Article 245"], "Article 368",
        "Article 368 (Part XX) contains the amendment procedure — special majority, plus ratification by half the states for federal provisions.",
        "368 = amendment article.", 20)
    S.q("ga-polam-p1", "medium", "Which one of the following can be amended by Parliament **alone, by a simple majority**?",
        ["Fundamental Rights", "Creation of a new state", "Election of the President", "The Seventh Schedule"], "Creation of a new state",
        "Creating new states or altering boundaries (Articles 2–4) needs only a **simple majority** and lies outside Article 368. The other three need the special-majority route; President's election and the Seventh Schedule additionally need state ratification.",
        "New states = simple majority, outside 368.", 25)
    S.q("ga-polam-p1", "hard", "Consider the statements about Constitutional Amendment Bills:\n1. They can be introduced in either House.\n2. They can be referred to a joint sitting on a deadlock.\n3. The President's assent is obligatory after passage.\nWhich are correct?",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "1 and 3 only",
        "Statement 2 is wrong — Constitution Amendment Bills **never** go to a joint sitting. They may start in either House (statement 1), and after the 24th Amendment the President **must** assent (statement 3).",
        "No joint sittings for amendment bills.", 30)
    S.q("ga-polam-p2", "easy", "Which amendment is popularly called the '**Mini-Constitution**'?",
        ["44th Amendment", "42nd Amendment", "24th Amendment", "52nd Amendment"], "42nd Amendment",
        "The **42nd Amendment (1976)** touched the Preamble, Fundamental Duties, tribunals, DPSPs and emergency provisions — hence 'Mini-Constitution'. The 44th (1978) partially rolled it back.",
        "42 = Mini-Constitution; 44 = the correction.", 20)
    S.q("ga-polam-p2", "medium", "The **Right to Property** was removed from the list of Fundamental Rights by the —",
        ["42nd Amendment", "43rd Amendment", "44th Amendment", "45th Amendment"], "44th Amendment",
        "The **44th Amendment (1978)** deleted Article 19(1)(f) and Article 31, and created **Article 300A** — property remains a legal (constitutional) right, not a Fundamental Right.",
        "44 → 300A.", 20)
    S.q("ga-polam-p3", "easy", "The **101st Constitutional Amendment Act** is associated with —",
        ["The Goods and Services Tax", "Women's reservation", "EWS reservation", "Anti-defection"], "The Goods and Services Tax",
        "The **101st Amendment (2016)** created the GST framework — Article 246A (power to tax), 269A (inter-state levy) and 279A (the GST Council).",
        "101 = GST.", 20)
    S.q("ga-polam-p3", "medium", "The **103rd Constitutional Amendment Act (2019)** provided —",
        ["One-third seats for women in legislatures", "10% reservation for economically weaker sections", "Constitutional status to the NCBC", "27% OBC reservation"], "10% reservation for economically weaker sections",
        "The **103rd Amendment** inserted Articles 15(6) and 16(6) to allow **10% reservation for EWS** in education and public employment. Women's reservation is the 106th; NCBC status is the 102nd.",
        "103 = EWS 10%.", 25)
    S.q("ga-polam-p3", "medium", "The **National Commission for Backward Classes** received constitutional status under —",
        ["Article 338 (89th Amendment)", "Article 338A", "Article 338B (102nd Amendment)", "Article 340"], "Article 338B (102nd Amendment)",
        "The **102nd Amendment (2018)** inserted **Article 338B**, giving the NCBC constitutional rank. Article 338 = NCSC; 338A = NCSC for STs.",
        "338B = NCBC = 102nd.", 25)
    S.q("ga-polam-p4", "easy", "The **anti-defection law** was added to the Constitution by the —",
        ["42nd Amendment", "44th Amendment", "52nd Amendment", "61st Amendment"], "52nd Amendment",
        "The **52nd Amendment (1985)** inserted the **Tenth Schedule**, listing disqualifications for defection. The 61st lowered the voting age; the 42nd is the Mini-Constitution.",
        "52 = Tenth Schedule = defection.", 20)
    S.q("ga-polam-p4", "medium", "The **voting age** in Lok Sabha and assembly elections was reduced from 21 to 18 years by the —",
        ["52nd Amendment", "61st Amendment", "69th Amendment", "73rd Amendment"], "61st Amendment",
        "The **61st Amendment (1989)** amended Article 326. The 69th (1991) made Delhi the National Capital Territory; the 73rd created the panchayat tier.",
        "61 = vote at eighteen.", 20)
    S.q("ga-polam-p4", "hard", "Match the amendment with its provision:\n1. 97th — Cooperative societies\n2. 100th — India–Bangladesh Land Boundary\n3. 104th — Ended Anglo-Indian nominated seats\nWhich are correctly matched?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are right: the **97th (2011)** added Part IX-B on cooperatives; the **100th (2015)** enacted the Land Boundary Agreement with Bangladesh; the **104th (2020)** ended the Anglo-Indian nomination to the Lok Sabha.",
        "97 coop, 100 boundary, 104 Anglo-Indian.", 30)
    return S


def build_local():
    S = Sub("pol-local-bodies-emergency")
    S.notes = """### Panchayati Raj — Part IX (73rd Amendment, 1992)
Rural local government became a constitutional tier on **24 April 1993** (now **National Panchayati Raj Day**). The framework: **Gram Sabha** (every village, all registered voters) at the base; a **three-tier** system — village panchayat, intermediate (block) panchayat, **Zila Parishad** — though states with under **20 lakh** population may skip the middle tier. Panchayats serve **5-year** terms (dissolved mid-way elections must follow within 6 months). Seats are reserved for **SCs/STs in proportion** to population and **not less than one-third for women** (many states now give 50%). A **State Election Commission** (Article 243K) conducts panchayat elections; a **State Finance Commission (Article 243-I)** reviews panchayat finances **every 5 years**. The **Eleventh Schedule** lists **29 subjects**. Roughly one-third of panchayat seats/chairs are reserved for women by the constitutional minimum.

### The committee ladder
| Committee | Recommendation |
|---|---|
| **Balwant Rai Mehta, 1957** | **Three-tier** democratic decentralisation ('democratic decentralisation' phrase) |
| **Ashok Mehta, 1977** | **Two-tier**: Zila Parishad + Mandal Panchayat |
| **G.V.K. Rao, 1981** | District as the planning unit; 'grass without roots' remark on PRI paralysis |
| **L.M. Singhvi, 1986** | **Constitutional status** for PRIs; Gram Sabha as the base |
| **P.K. Thungon, 1988** | Constitutional recognition; Zila Parishad for planning |

The first panchayat under the 1959 scheme was inaugurated by Nehru at **Nagaur, Rajasthan, on 2 October 1959**. Remember the mapping: Balwant Rai = three-tier, Ashok Mehta = two-tier, Singhvi = constitutional status.

### Municipalities — Part IX-A (74th Amendment, 1992)
In force from **1 June 1993**; Article 243P–243ZG; the **Twelfth Schedule** lists **18 subjects**. Three urban bodies: **Nagar Panchayat** (transitional area), **Municipal Council** (smaller urban area), **Municipal Corporation** (larger urban area). The same 5-year term, reservations, State Election Commission and Finance Commission rules apply; **wards committees** for municipalities with 3 lakh+ population. The **97th Amendment (2011)** added **Part IX-B** on cooperative societies.

### Emergency — Part XVIII (Articles 352–360)
- **National Emergency (352)**: grounds are **war, external aggression, armed rebellion** (the 44th Amendment replaced 'internal disturbance'). Proclamation must be approved by **both Houses within one month** (44th changed it from 2 months); each approval lasts **6 months**, renewable indefinitely by special majority. The Lok Sabha's own term can be extended **one year at a time**. Article **358** automatically suspends Article 19 (only in war/external-aggression cases); Article **359** lets the President suspend enforcement of other rights by order (Articles 20 and 21 can never be suspended — 44th Amendment).
- **President's Rule (356)**: failure of constitutional machinery in a state; approval within **2 months**; lasts **6 months** at a time, extendable to **3 years** with conditions (annual parliamentary approval after the first year). **S.R. Bommai (1994)** made proclamations subject to **judicial review** and barred using Article 356 for partisan ends.
- **Financial Emergency (360)**: threatens financial stability; approval in 2 months; salaries of officials including judges can be reduced; **never imposed** so far.

### Quick revision
- 73rd (24 Apr 1993): Part IX, three tiers, Gram Sabha, 29 subjects (11th Schedule), SEC + SFC every 5 years.
- Committees: Balwant Rai = 3-tier (1957), Ashok Mehta = 2-tier (1977), Singhvi = constitutional status (1986).
- 74th: Part IX-A, 18 subjects (12th Schedule), Nagar Panchayat/Council/Corporation, wards committees (3 lakh+).
- National emergency: 'armed rebellion' (44th), 1-month approval, 6-month renewals; Art 19 auto-suspends (358); 20–21 never suspended.
- President's Rule: 2-month approval, 6-month spells, 3-year ceiling; Bommai (1994) = judicial review.
- Financial Emergency (360) has never been proclaimed."""
    S.pattern("ga-polloc-p1", "73rd Amendment structure", "very common",
        "'The Gram Sabha consists of', 'which article provides a State Finance Commission', 'how many subjects in the Eleventh Schedule', statement sets on PRI structure.",
        None,
        "1. Base = **Gram Sabha** (all registered voters of the village); tiers = village + intermediate + Zila Parishad (states under 20 lakh may skip the middle tier).\n2. Terms 5 years; women's reservation one-third minimum; SEC conducts elections (243K); **SFC every 5 years — Article 243-I**.\n3. Eleventh Schedule = **29 subjects**; effective 24 April 1993 = Panchayati Raj Day.",
        "A **State Finance Commission** is constituted once in —",
        "**Five years** under **Article 243-I**, to review the financial position of panchayats and municipalities and recommend tax-sharing and grants.")
    S.pattern("ga-polloc-p2", "Committee ↔ recommendation", "very common",
        "'Which committee recommended a two-tier system', 'constitutional status for panchayats was recommended by', matching four committees to their ideas.",
        None,
        "1. **Balwant Rai Mehta (1957) = three-tier**; **Ashok Mehta (1977) = two-tier** (Zila Parishad + Mandal Panchayat).\n2. **G.V.K. Rao (1981)** = district planning focus; **L.M. Singhvi (1986) = constitutional status + Gram Sabha**; Thungon (1988) = constitutional recognition, district planning.\n3. Do not swap the two Mehtas — Balwant = three, Ashok = two.",
        "Which committee recommended a **two-tier** Panchayati Raj system with Zila Parishad and Mandal Panchayat?",
        "The **Ashok Mehta Committee (1977)** — it wanted the block tier abolished, leaving Zila Parishad at the top and Mandal Panchayat below.")
    S.pattern("ga-polloc-p3", "74th Amendment and urban bodies", "common",
        "'How many subjects in the Twelfth Schedule', 'which body for a transitional area', 'wards committees are required for municipalities above what population'.",
        None,
        "1. Twelfth Schedule = **18 subjects**; Part IX-A; effective 1 June 1993.\n2. Body map: transitional area → **Nagar Panchayat**; smaller urban → **Municipal Council**; larger urban → **Municipal Corporation**.\n3. Wards committees mandatory for municipalities with **3 lakh+** population (Article 243S); cooperative societies = Part IX-B (97th Amendment).",
        "For a **transitional area**, the 74th Amendment provides for a —",
        "**Nagar Panchayat**; smaller urban areas get Municipal Councils and larger urban areas Municipal Corporations.")
    S.pattern("ga-polloc-p4", "National Emergency (Article 352)", "very common",
        "'Armed rebellion replaced internal disturbance — which amendment', 'within how many days/months must Parliament approve', 'which rights cannot be suspended', 358 vs 359 questions.",
        None,
        "1. Grounds: war, external aggression, **armed rebellion** (44th Amendment). Proclamation laid before Parliament; approval within **one month**; 6-month renewals, no ceiling.\n2. **358**: Article 19 stands suspended automatically in war/external aggression — not in armed-rebellion emergencies.\n3. **359**: enforcement of other rights can be suspended by order — but **Articles 20 and 21 never** (44th Amendment).",
        "Under the 44th Amendment, which Fundamental Rights can **never** be suspended during an emergency?",
        "**Articles 20 and 21** — protection in convictions, and life/personal liberty, stay enforceable no matter what the proclamation covers.")
    S.pattern("ga-polloc-p5", "President's Rule and Financial Emergency", "common",
        "'Approval period for Article 356', 'maximum duration of President's Rule', 'which case made 356 justiciable', 'has a Financial Emergency ever been imposed'.",
        None,
        "1. Article 356: approval within **2 months**; 6-month spells; ceiling **3 years** (with conditions and annual approvals after the first year).\n2. **S.R. Bommai (1994)**: proclamations are open to **judicial review**; majority must be tested on the floor of the House.\n3. Article 360 (Financial Emergency) has **never** been used; it can cut salaries, including of judges.",
        "The famous case holding that a proclamation under **Article 356 is subject to judicial review** is —",
        "**S.R. Bommai v. Union of India (1994)** — the Court also laid down that a ministry's majority should be tested on the floor of the assembly, not in Raj Bhavan.")

    S.q("ga-polloc-p1", "easy", "The **Gram Sabha** consists of —",
        ["Elected panchayat members only", "All registered voters of the village", "The Sarpanch and ward members", "Nominees of the state government"], "All registered voters of the village",
        "Under **Article 243(b)** the Gram Sabha is the body of **all persons registered in the electoral rolls** of a village — the foundation of the panchayat system.",
        "Gram Sabha = every voter of the village.", 20)
    S.q("ga-polloc-p1", "medium", "The **Eleventh Schedule** of the Constitution contains how many subjects for panchayats?",
        ["18", "29", "47", "66"], "29",
        "**29 subjects** (11th Schedule, 73rd Amendment). The 12th Schedule gives municipalities **18 subjects**.",
        "11th = 29 villages; 12th = 18 cities.", 20)
    S.q("ga-polloc-p1", "hard", "A state with a population **below 20 lakh** may —",
        ["Skip the Gram Sabha", "Not constitute an intermediate panchayat", "Appoint the Zila Parishad chairman", "Postpone panchayat elections"], "Not constitute an intermediate panchayat",
        "Article 243B lets states with up to **20 lakh** population skip the **intermediate (block) tier**, keeping a village panchayat + Zila Parishad two-level structure.",
        "Small state = no block tier.", 30)
    S.q("ga-polloc-p2", "medium", "The committee that recommended **constitutional status** for Panchayati Raj institutions was chaired by —",
        ["Balwant Rai Mehta", "Ashok Mehta", "G.V.K. Rao", "L.M. Singhvi"], "L.M. Singhvi",
        "The **L.M. Singhvi Committee (1986)** asked for constitutional status and a Gram Sabha at the base — ideas realised by the 73rd Amendment. Balwant Rai Mehta wanted three tiers; Ashok Mehta, two.",
        "Singhvi = constitution; Balwant = three tiers.", 25)
    S.q("ga-polloc-p2", "medium", "The first Panchayati Raj scheme was inaugurated at **Nagaur, Rajasthan** in 1959 by —",
        ["Sardar Patel", "Jawaharlal Nehru", "Rajendra Prasad", "Chaudhary Charan Singh"], "Jawaharlal Nehru",
        "**Nehru** inaugurated the first panchayat at **Nagaur on 2 October 1959**, launching the Balwant Rai Mehta three-tier design in Rajasthan.",
        "Nagaur, 2 Oct 1959, Nehru.", 25)
    S.q("ga-polloc-p3", "easy", "The **Twelfth Schedule** deals with —",
        ["Panchayat subjects", "Municipal subjects", "Languages", "Anti-defection"], "Municipal subjects",
        "The **Twelfth Schedule** lists **18 municipal subjects** (74th Amendment). Panchayat subjects (29) sit in the Eleventh.",
        "12 = municipalities = 18 subjects.", 20)
    S.q("ga-polloc-p3", "medium", "A **wards committee** is mandatory within a municipal area having a population of —",
        ["1 lakh or more", "3 lakh or more", "5 lakh or more", "10 lakh or more"], "3 lakh or more",
        "**Article 243S**: municipalities with **three lakh or more** inhabitants must constitute wards committees (one or more per ward) for local participation.",
        "3 lakh → wards committees.", 25)
    S.q("ga-polloc-p4", "easy", "The phrase '**armed rebellion**' as a ground of National Emergency was substituted for 'internal disturbance' by the —",
        ["42nd Amendment", "43rd Amendment", "44th Amendment", "45th Amendment"], "44th Amendment",
        "The **44th Amendment (1978)** replaced 'internal disturbance' with the narrower '**armed rebellion**' and made parliamentary approval due within **one month**.",
        "44 = armed rebellion.", 20)
    S.q("ga-polloc-p4", "medium", "During a National Emergency proclaimed on the ground of **armed rebellion alone**, which Article stands suspended?",
        ["Article 14", "Article 19", "Article 21", "None — Article 19 suspends only for war or external aggression"], "None — Article 19 suspends only for war or external aggression",
        "**Article 358** suspends Article 19 automatically **only** for war or external aggression. An armed-rebellion emergency leaves Article 19 intact; other rights need an Article 359 order (and 20–21 can never go).",
        "19 auto-suspends only for war/external aggression.", 30)
    S.q("ga-polloc-p4", "medium", "Parliament must approve a proclamation of National Emergency within —",
        ["Two months", "One month", "Six weeks", "One year"], "One month",
        "The **44th Amendment** cut the approval window from two months to **one month**, by special majority of both Houses; each approval then runs six months, renewable indefinitely.",
        "Emergency approval: one month (was two).", 25)
    S.q("ga-polloc-p5", "medium", "President's Rule under **Article 356** can be continued, with parliamentary approvals, for a maximum of —",
        ["One year", "Two years", "Three years", "Five years"], "Three years",
        "Six months at a time, extendable up to **three years** — beyond the first year it needs six-monthly approval plus the special conditions laid down by the 44th Amendment.",
        "356 ceiling = three years.", 25)
    S.q("ga-polloc-p5", "medium", "A **Financial Emergency** under Article 360 has been proclaimed in India —",
        ["Once, in 1962", "Twice", "Once, in 1991", "Never"], "Never",
        "**Never** — Article 360 remains unused. If invoked, it would authorise the reduction of salaries and allowances of all government servants, including Supreme Court and High Court judges.",
        "360 has never been used — the safe answer.", 20)
    return S


def build_bodies():
    S = Sub("pol-bodies")
    S.notes = """### Constitutional bodies — the permanent machinery
- **Election Commission (Article 324)**: conducts elections to Parliament, state assemblies, and the offices of President and Vice-President. Since **1993** it is a **multi-member** body — the CEC and **two Election Commissioners** with equal powers. The **CEC can be removed only like a Judge of the Supreme Court**; the other Commissioners, on the **CEC's recommendation**. Tools: the Model Code of Conduct, electoral rolls, recognition of parties, symbols.
- **Union Public Service Commission (Articles 315–323)**: recruits for Union services. Members serve **6 years or till 65**; removal grounds for the chairman mirror a Supreme Court judge's; expenses are **charged on the Consolidated Fund**. State PSCs mirror it (members retire at 62), with a **UPSC-facilitated** removal.
- **Comptroller and Auditor-General (Articles 148–151)**: the '**guardian of the public purse**'. Term **6 years or age 65**; after leaving office, the CAG cannot take any further government post. Audits the accounts of the Union and the states, and bodies substantially financed by them; reports go to the **President/Governor** and are laid before the legislature. The **PAC examines** the CAG's reports (DPC Act, 1971 governs audit duties).
- **Finance Commission (Article 280)**: a **quasi-judicial** body, constituted **every five years** (or earlier); **Chairman + four members** (qualifications set by Parliament's Finance Act, 1951). Recommends the **vertical and horizontal devolution** of central taxes, grants-in-aid (Article 275), and measures to augment state funds for panchayats/municipalities. Its advice is **advisory**, not binding.
- **Attorney-General (Article 76)** and **Advocate-General (Article 165)**: chief law officers of the Union and the state; hold office during pleasure; the AG may speak in Parliament but not vote.
- **Special Officer for Linguistic Minorities (Article 350B)**; **NCSC (Article 338)** and **NCBC (Article 338B)**; **Official Language rules** sit in Part XVII.

### Statutory and related bodies — know the parent law
| Body | Parent law / note |
|---|---|
| CVC | Statutory from **2003** (earlier executive, 1964; Santhanam Committee advice) |
| CIC | **RTI Act, 2005**; Chief Information Commissioner + Information Commissioners |
| NHRC | **Protection of Human Rights Act, 1993**; chaired by a former Chief Justice of India |
| Lokpal | **Lokpal and Lokayuktas Act, 2013** |
| NGT | **National Green Tribunal Act, 2010**; fast-track environmental adjudication |
| NITI Aayog | Created by a **Cabinet resolution, 1 January 2015** (non-statutory), replacing the Planning Commission |
| NCW | **National Commission for Women Act, 1990** (set up 1992) |

**Remember the split**: constitutional bodies (EC, UPSC, CAG, Finance Commission, NCSC/NCBC) exist because the Constitution says so; statutory bodies exist because a **law of Parliament** created them; NITI Aayog is neither — it is an executive creation. Exams love asking which is which, and whether a body's expenses are charged on the Consolidated Fund (UPSC, CAG — yes).

Exams also ask about **tenure** numbers (6 years or 65 for CEC, CAG, UPSC chairman) and the **removal** ladder (CEC/UPSC-CAG chairman like an SC judge). Names of current office-holders change — revise them separately just before your exam; this lesson sticks to structure.

### Quick revision
- EC: multi-member since 1993 (CEC + 2 ECs); CEC removable like an SC judge; Art 324.
- UPSC: Art 315; 6 years/65; expenses charged; state PSC members retire at 62.
- CAG: Art 148; 'guardian of the public purse'; 6 years/65; no re-employment; reports → President/Governor → PAC scrutiny.
- Finance Commission: Art 280; quasi-judicial; every 5 years; Chairman + 4; advice not binding.
- Statutory vs constitutional: CVC/CIC/NHRC/Lokpal/NGT = statutory; NITI Aayog = executive resolution (2015).
- NCSC Art 338; NCBC Art 338B (102nd Amendment); Special Officer linguistic minorities Art 350B."""
    S.pattern("ga-polbo-p1", "Election Commission structure and removal", "very common",
        "'How many members does the EC have', 'how can the CEC be removed', 'who conducts President/Vice-President elections', statement sets on the EC.",
        None,
        "1. Multi-member since **1993**: CEC + **two Election Commissioners**, all with equal powers.\n2. Removal ladder: CEC — like a **Supreme Court judge**; other ECs — on the **CEC's recommendation**.\n3. Jurisdiction: Parliament, state legislatures, and the **President and Vice-President elections**. Local-body elections belong to the State Election Commissions, not the EC.",
        "The **Chief Election Commissioner** can be removed —",
        "In the **same manner as a Judge of the Supreme Court** — by Parliament on grounds of proved misbehaviour or incapacity, through a special-majority process.")
    S.pattern("ga-polbo-p2", "UPSC and CAG: tenure and features", "common",
        "'The CAG is called the guardian of', 'UPSC members' tenure', 'who audits the accounts of the states', which expenses are charged on the CFI.",
        None,
        "1. UPSC: Article 315; members serve **6 years or till 65**; expenses **charged** on the CFI.\n2. CAG: Article 148; **6 years or 65**; audits Union and state accounts; barred from further government office; reports to the President/Governor.\n3. PAC (22 members, opposition chairman) examines the CAG's reports — 'friend, philosopher and guide of the PAC'.",
        "The **Comptroller and Auditor-General** of India is appointed by the President under Article —",
        "**Article 148**; his removal mirrors that of a Supreme Court judge, and the Constitution bars him from any further office under the Government of India or a state after retirement.")
    S.pattern("ga-polbo-p3", "Finance Commission", "common",
        "'The Finance Commission is constituted every', 'who decides tax devolution', 'how many members', 'is its advice binding'.",
        None,
        "1. Article 280: quasi-judicial, **every five years**; **Chairman + four members**.\n2. Job: split central taxes between Centre and states (vertical) and among states (horizontal), grants-in-aid, and measures to augment state funds for local bodies.\n3. Its recommendations are **advisory** — the government is not bound, though it normally follows them.",
        "The **Finance Commission** is normally constituted once in —",
        "**Every five years** under **Article 280**; it is a quasi-judicial body with a Chairman and four members appointed by the President.")
    S.pattern("ga-polbo-p4", "Constitutional vs statutory vs executive bodies", "very common",
        "'Which of the following is a constitutional body', 'NITI Aayog was created by', 'which act created the CIC/NHRC/Lokpal', odd-one-out sets.",
        None,
        "1. Constitutional: EC, UPSC/SPSCs, CAG, Finance Commission, NCSC (338), NCBC (338B), Official Language Commission.\n2. Statutory: CVC (2003), CIC (RTI 2005), NHRC (1993), Lokpal (2013), NGT (2010), NCW (1990 act).\n3. Executive: **NITI Aayog** (Cabinet resolution, 1 Jan 2015) — the trap answer in odd-one-out questions.",
        "Which one of the following is **not** a statutory body?",
        "**NITI Aayog** — it was set up by a Cabinet resolution on 1 January 2015; the CVC, CIC, NHRC and NGT all rest on statutes.")
    S.pattern("ga-polbo-p5", "Rights commissions and special officers", "occasional",
        "'NCSC is established under which Article', 'which body looks into linguistic minorities', 'the NCBC got constitutional status by which amendment'.",
        None,
        "1. NCSC — **Article 338** (SCs and STs); the separate ST commission sits at **Article 338A**.\n2. NCBC — **Article 338B**, constitutional status by the **102nd Amendment (2018)**; the 105th (2021) returned SEBC identification to states.\n3. Special Officer for **linguistic minorities — Article 350B**; assesses safeguards for language minorities.",
        "The **National Commission for Backward Classes (NCBC)** was given constitutional status by —",
        "The **102nd Amendment Act, 2018**, inserting **Article 338B**; the 105th Amendment (2021) restored the states' power to identify OBCs.")

    S.q("ga-polbo-p1", "easy", "The Election Commission of India became a **multi-member** body in —",
        ["1950", "1989", "1993", "2000"], "1993",
        "Since **October 1993** the Commission has had the **CEC plus two Election Commissioners** with equal powers. (A second commissioner had also been appointed briefly in 1989.)",
        "1993 = three-member EC.", 20)
    S.q("ga-polbo-p1", "medium", "Which statement about the Election Commission is **correct**?",
        ["It conducts elections to panchayats and municipalities", "The CEC can be removed like a Supreme Court judge", "It is a statutory body created in 1950 by law", "Election Commissioners hold office for 5 years"], "The CEC can be removed like a Supreme Court judge",
        "Article 324 makes the EC **constitutional** (not statutory); local-body elections belong to **State Election Commissions**; the tenure of Commissioners is **6 years or age 65**, whichever earlier.",
        "CEC = SC-judge removal; local polls = SEC.", 25)
    S.q("ga-polbo-p1", "medium", "Elections to the offices of **President and Vice-President** are conducted by —",
        ["Parliament", "The Supreme Court", "The Election Commission of India", "The Ministry of Law"], "The Election Commission of India",
        "Under **Article 324** the EC superintends, directs and controls elections to Parliament, state assemblies — and the offices of President and Vice-President.",
        "President/VP polls = EC's job.", 20)
    S.q("ga-polbo-p2", "easy", "The CAG of India is described as the '**guardian of the public purse**' because he —",
        ["Prepares the Union Budget", "Controls the Contingency Fund", "Audits the accounts of the Union and the states", "Sanctions government expenditure"], "Audits the accounts of the Union and the states",
        "The CAG audits all receipts and expenditure of the Union and state governments and bodies substantially financed by them; his reports are laid before the legislatures and examined by the **PAC**.",
        "CAG audits — it does not budget or sanction.", 20)
    S.q("ga-polbo-p2", "medium", "The tenure of a member of the **UPSC** is —",
        ["5 years or 62 years of age", "6 years or 65 years of age", "6 years or 62 years of age", "5 years or 60 years of age"], "6 years or 65 years of age",
        "UPSC members hold office for **six years or until 65**; state PSC members get six years or 62. Expenses of both are charged on the Consolidated Fund.",
        "UPSC 6/65; SPSC 6/62.", 25)
    S.q("ga-polbo-p2", "hard", "Consider the statements:\n1. The CAG can take up another government office after retirement.\n2. The CAG audits the accounts of both the Union and the states.\n3. The CAG's reports are submitted to the President or the Governor.\nWhich are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], "2 and 3 only",
        "Statement 1 is wrong — the Constitution (Article 148) **bars the CAG** from further office under the Government of India or any state. Statements 2 and 3 are correct.",
        "No re-employment for the CAG.", 30)
    S.q("ga-polbo-p3", "easy", "The **Finance Commission** is a —",
        ["Statutory body", "Constitutional body", "Executive body", "Advisory committee of Parliament"], "Constitutional body",
        "It flows from **Article 280** of the Constitution — hence constitutional — and is constituted every five years with a Chairman and four members.",
        "280 = constitutional = Finance Commission.", 20)
    S.q("ga-polbo-p3", "medium", "The recommendations of the **Finance Commission** are —",
        ["Binding on the President", "Binding on Parliament", "Advisory in nature", "Binding on state legislatures"], "Advisory in nature",
        "They are **advisory** — the Union government is not bound to accept them, though in practice it does. The commission also suggests grants-in-aid under Article 275.",
        "FC advises; it does not command.", 25)
    S.q("ga-polbo-p4", "easy", "**NITI Aayog** was established on 1 January 2015 by —",
        ["A constitutional amendment", "An Act of Parliament", "A Union Cabinet resolution", "A presidential ordinance"], "A Union Cabinet resolution",
        "It replaced the Planning Commission through a **Cabinet resolution** — so it is an **executive**, not statutory or constitutional, body.",
        "NITI = resolution, not law.", 20)
    S.q("ga-polbo-p4", "medium", "Which one of the following pairs is **correctly matched**?",
        ["CIC — RTI Act, 2005", "NHRC — Lokpal Act, 2013", "NGT — Companies Act, 2013", "Lokpal — Human Rights Act, 1993"], "CIC — RTI Act, 2005",
        "The **CIC** was created by the RTI Act, 2005. NHRC rests on the Protection of Human Rights Act, 1993; the NGT on the NGT Act, 2010; the Lokpal on the Lokpal and Lokayuktas Act, 2013.",
        "CIC-RTI, NHRC-1993, Lokpal-2013, NGT-2010.", 25)
    S.q("ga-polbo-p5", "easy", "The **National Commission for Scheduled Castes** is established under —",
        ["Article 335", "Article 338", "Article 340", "Article 341"], "Article 338",
        "**Article 338** creates the NCSC (338A covers the ST wing; **338B** the NCBC). Article 340 empowers commissions for backward classes generally.",
        "338 = SC commission; 338B = OBC commission.", 20)
    S.q("ga-polbo-p5", "medium", "The **Special Officer for Linguistic Minorities** is provided for in —",
        ["Article 350", "Article 350A", "Article 350B", "Article 351"], "Article 350B",
        "**Article 350B** — the Special Officer investigates matters concerning safeguards for linguistic minorities and reports to the President. Article 350A covers mother-tongue primary education; 351 directs Hindi's development.",
        "350B = linguistic minorities officer.", 25)
    return S
