"""economy deep content — part 2: eco-budget, eco-taxes, eco-schemes, eco-institutions."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def lakh(x):
    return "₹{} lakh crore".format(x)


def build_budget():
    S = Sub("eco-budget")
    # Deficit arithmetic is computed, never hand-typed.
    exp, rec, intr = 45, 39, 10
    fd = exp - rec                      # fiscal deficit
    pd = fd - intr                      # primary deficit
    assert (fd, pd) == (6, -4)
    rev_rec, rev_exp = 25, 28
    rd = rev_exp - rev_rec              # revenue deficit
    grants_cap = 1
    erd = rd - grants_cap               # effective revenue deficit
    assert (rd, erd) == (3, 2)

    S.notes = """### The Budget — what the Constitution calls it
The word 'Budget' appears nowhere in the Constitution. Article 112 names it the **Annual Financial Statement** — estimated receipts and expenditure of the government for a year, laid before both Houses. Since **2017** it is presented on **1 February** (earlier: the last day of February), and the separate **Railway Budget was merged** into the general Budget the same year. A day before, the government tables the **Economic Survey** (prepared by the Department of Economic Affairs under the Chief Economic Adviser). The expenditure side appears as **Demands for Grants** per ministry; approval flows through the **Appropriation Bill** (spending) and the **Finance Bill** (tax proposals).

### The three funds
- **Consolidated Fund of India — Article 266(1)**: all revenues, loans and receipts; Parliament must authorise every withdrawal.
- **Public Account — Article 266(2)**: money held in trust — provident funds, small savings; no vote needed.
- **Contingency Fund — Article 267**: at the disposal of the **President** for unforeseen spending; corpus raised to **₹30,000 crore** in 2021.

Receipts split into **revenue** (tax, interest, dividends — non-creating) and **capital** (borrowings, disinvestment, loan recoveries); expenditure likewise splits into **revenue** (salaries, subsidies, interest) and **capital** (assets — roads, buildings, defence equipment).

### The deficits — four formulas that settle most questions
- **Revenue Deficit** = Revenue expenditure − Revenue receipts: the government borrows to run day-to-day affairs.
- **Effective Revenue Deficit** = Revenue deficit − grants for creation of capital assets: introduced in 2011-12.
- **Fiscal Deficit** = Total expenditure − Total receipts **other than borrowings**: the year's total borrowing need.
- **Primary Deficit** = Fiscal deficit − interest payments: this year's borrowing appetite, freed of past debts' interest.

The **FRBM Act, 2003** set legal limits on these deficits (amended in 2018 to add debt-GDP targets); Budgets announce a multi-year fiscal **glide path**. In matching questions, fiscal deficit always 'includes' the others' interest burden — the largest single expenditure head is interest payment, followed by subsidies and defence.

### Quick revision
- Budget = Annual Financial Statement (Art 112); presented 1 February since 2017; Railway Budget merged 2017.
- Funds: Consolidated 266(1), Public Account 266(2), Contingency 267 (President; ₹30,000 crore corpus).
- Economic Survey: day before, Dept of Economic Affairs; Appropriation Bill = spending, Finance Bill = taxes.
- RD = Rev Exp − Rev Rec; ERD = RD − capital-asset grants; FD = Total Exp − (Rec − borrowings); PD = FD − interest.
- FRBM Act 2003; interest payments are the largest expenditure head."""
    S.pattern("ga-ecoBu-p1", "Deficit arithmetic", "very common",
        "Expenditure, receipts and interest figures are given and one deficit is asked; or a relationship ('primary deficit is negative because') is tested.",
        None,
        "1. Fiscal deficit = total expenditure − total receipts **excluding borrowings**.\n2. Primary deficit = fiscal deficit − **interest payments** (it can be negative — a primary surplus).\n3. Revenue deficit = revenue expenditure − revenue receipts; plug the numbers in one step and check units (lakh crore).",
        "Total expenditure is ₹45 lakh crore and receipts excluding borrowings ₹39 lakh crore. The **fiscal deficit** is —",
        "45 − 39 = **₹6 lakh crore** — exactly the amount the government must borrow this year.")
    S.pattern("ga-ecoBu-p2", "Budget structure, articles and funds", "common",
        "'Which article is the Annual Financial Statement', 'the Contingency Fund is at whose disposal', matching each fund with its article and purpose.",
        None,
        "1. Article 112 = Annual Financial Statement (the constitutional 'Budget'); Article 266(1) = Consolidated Fund; 266(2) = Public Account; Article 267 = Contingency Fund.\n2. Contingency Fund = **President's disposal**; Consolidated Fund = no withdrawal without **Parliament's vote**; Public Account = no vote needed.\n3. 'Budget' is not a constitutional word — options saying 'Budget is defined in Article 112' are wrong.",
        "The **Contingency Fund of India** is placed at the disposal of —",
        "The **President** (Article 267) — used for unforeseen expenditure, later regularised by Parliament; corpus ₹30,000 crore.")
    S.pattern("ga-ecoBu-p3", "Revenue vs capital, effective revenue deficit", "common",
        "'Which is a capital receipt', 'effective revenue deficit excludes', statements classifying disinvestment, borrowings, grants.",
        None,
        "1. Capital receipts: **borrowings, disinvestment proceeds, recovery of loans** — they either create liability or cut assets.\n2. Capital expenditure: roads, buildings, defence equipment, loans to states. Revenue expenditure: salaries, subsidies, interest.\n3. **Effective revenue deficit = revenue deficit − grants for creation of capital assets** (introduced 2011-12).",
        "Which of the following is a **capital receipt**?",
        "**Disinvestment proceeds** — selling government equity reduces assets; borrowings and loan recoveries are the other classic capital receipts.")
    S.pattern("ga-ecoBu-p4", "FRBM and the fiscal glide path", "occasional",
        "'The FRBM Act was passed in', statements on deficit targets, debt-GDP anchors, the meaning of a glide path in Budget speeches.",
        None,
        "1. **FRBM Act 2003** — fiscal responsibility and budget management: legal deficit targets, amended in 2018 (debt anchors added).\n2. Budgets declare a **fiscal glide path** — a year-by-year path for fiscal deficit as a share of GDP.\n3. Interest payments, not subsidies, are the single largest revenue-expenditure head — a favourite 'true statement' fact.",
        "The **FRBM Act**, which sets legal targets for deficits and debt, was enacted in —",
        "**2003** — the Fiscal Responsibility and Budget Management Act disciplines deficits; a 2018 amendment added debt-to-GDP anchors.")
    S.pattern("ga-ecoBu-p5", "Budget process, dates and documents", "common",
        "'Since which year is the Budget presented on 1 February', 'the Economic Survey is tabled when', 'the Railway Budget was merged in', questions on Demands for Grants / appropriation.",
        None,
        "1. From **2017**: presentation on **1 February** and the **Railway Budget merged** into the general Budget.\n2. **Economic Survey** comes the day before (Dept of Economic Affairs / Chief Economic Adviser).\n3. Spending needs **Demands for Grants** per ministry, then an **Appropriation Bill**; taxes move via the **Finance Bill**.",
        "The **Economic Survey** is presented —",
        "A day **before the Union Budget**, by the Department of Economic Affairs; it reviews the economy's performance and outlook.")

    S.q("ga-ecoBu-p1", "easy", "The **fiscal deficit** is best defined as —",
        ["Revenue expenditure minus revenue receipts", "Total expenditure minus total receipts excluding borrowings", "Total expenditure minus interest payments", "Total borrowings minus interest payments"], "Total expenditure minus total receipts excluding borrowings",
        "**Fiscal deficit** = the government's total borrowing requirement for the year — total expenditure minus all receipts other than borrowings. The first option defines revenue deficit.",
        "FD = borrowing need.", 20)
    S.q("ga-ecoBu-p1", "medium", "Total expenditure ₹45 lakh crore; receipts excluding borrowings ₹39 lakh crore. The **fiscal deficit** equals —",
        [lakh(6), lakh(84), lakh(39), lakh(45)], lakh(fd),
        "45 − 39 = **₹6 lakh crore** — computed as expenditure minus non-borrowed receipts.",
        "45 − 39.", 25)
    S.q("ga-ecoBu-p1", "medium", "Fiscal deficit is ₹6 lakh crore and interest payments ₹10 lakh crore. The **primary deficit** is —",
        [lakh(16), lakh(-4) + " (primary surplus)", lakh(6), lakh(4)], lakh(pd) + " (primary surplus)",
        "6 − 10 = **−₹4 lakh crore**, i.e. a primary surplus: excluding past interest, this year's operations raise no new borrowing.",
        "PD = FD − interest; here it flips negative.", 25)
    S.q("ga-ecoBu-p1", "hard", "A government has revenue receipts ₹25, revenue expenditure ₹28 (all figures lakh crore). Its **revenue deficit** is —",
        [lakh(3), lakh(25), lakh(28), lakh(53)], lakh(rd),
        "28 − 25 = **₹3 lakh crore** — revenue spending exceeds revenue income, so borrowing finances routine running costs.",
        "28 − 25.", 25)
    S.q("ga-ecoBu-p2", "easy", "The **Annual Financial Statement** of the Union is laid before Parliament under —",
        ["Article 112", "Article 266", "Article 267", "Article 280"], "Article 112",
        "**Article 112** presents estimated receipts and expenditure — the constitutional name for the Union Budget. Articles 266-267 deal with the funds; 280 is the Finance Commission.",
        "112 = the Budget's legal name.", 20)
    S.q("ga-ecoBu-p2", "medium", "Which statement about the **Consolidated Fund of India** is correct?",
        ["Money is held in trust and needs no parliamentary approval", "No money can be withdrawn without appropriation by Parliament", "It is at the President's personal disposal", "It holds only provident-fund balances"], "No money can be withdrawn without appropriation by Parliament",
        "Article 266(1): every withdrawal from the Consolidated Fund needs **Parliament's authorisation**. The trust balances with no vote sit in the Public Account; the President's discretion runs on the Contingency Fund.",
        "CFI = voted money.", 25)
    S.q("ga-ecoBu-p3", "medium", "**Disinvestment proceeds** of the government are classified as —",
        ["Revenue receipts", "Capital receipts", "Capital expenditure", "Public-account receipts"], "Capital receipts",
        "Selling government equity **reduces assets** — the defining mark of a capital receipt, along with borrowings and loan recoveries.",
        "Asset-reducing = capital receipt.", 25)
    S.q("ga-ecoBu-p3", "hard", "Revenue deficit is ₹3 lakh crore, including grants of ₹1 lakh crore for creation of capital assets. The **effective revenue deficit** is —",
        [lakh(4), lakh(3), lakh(2), lakh(1)], lakh(erd),
        "ERD = RD − grants for capital assets = 3 − 1 = **₹2 lakh crore** — introduced in 2011-12 to show borrowing that funds only consumption.",
        "Subtract the capital-asset grants.", 30)
    S.q("ga-ecoBu-p4", "medium", "Which one of the following is **correct**?",
        ["The FRBM Act was enacted in 1991", "Primary deficit excludes interest payments", "Subsidies are the largest revenue-expenditure head", "Fiscal deficit excludes borrowings entirely"], "Primary deficit excludes interest payments",
        "**Primary deficit = fiscal deficit − interest payments**, isolating this year's borrowing appetite. FRBM came in 2003; interest payments top the expenditure list; fiscal deficit is defined including the effect of borrowing needs.",
        "PD strips out interest.", 25)
    S.q("ga-ecoBu-p4", "hard", "Consider the statements:\n1. The FRBM Act gives legal backing to deficit targets.\n2. Interest payments are the largest single item of government expenditure.\n3. Fiscal deficit can never exceed revenue deficit.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is false — the fiscal deficit (total borrowing need) routinely **exceeds** the revenue deficit because capital expenditure is also financed by borrowing.",
        "FD ≥ RD is the normal case.", 30)
    S.q("ga-ecoBu-p5", "easy", "The Union Budget is presented on **1 February** since —",
        ["2014", "2015", "2017", "2019"], "2017",
        "From **2017** the Budget moved to 1 February — giving ministries time to spend from April 1 — and the **Railway Budget was merged** the same year.",
        "2017: new date + rail merger.", 20)
    S.q("ga-ecoBu-p5", "medium", "Approval of government **expenditure** proceeds through —",
        ["The Finance Bill", "The Appropriation Bill on Demands for Grants", "The Economic Survey", "The Fringe Benefits Bill"], "The Appropriation Bill on Demands for Grants",
        "Each ministry's **Demand for Grants** is voted; the **Appropriation Bill** then authorises withdrawal from the Consolidated Fund. The Finance Bill carries tax proposals instead.",
        "Demands → Appropriation = spending.", 25)
    return S


def build_taxes():
    S = Sub("eco-taxes")
    S.notes = """### Direct vs indirect — the master divide
**Direct taxes** fall on the person who pays them: **income tax, corporate tax, securities transaction tax (STT), capital-gains tax** — progressivity built in, burden not shiftable. **Indirect taxes** are paid to the government but shifted to consumers through prices: **GST, customs duty, excise duty on petroleum and alcohol, stamp duties** — they are regressive (the rich and poor pay the same rate on a good) but easy to collect. Corporation tax and income tax are the top two direct-tax heads; GST the biggest indirect one. **Agricultural income** stays outside income tax (taxing it is a state power).

### GST — one nation, one tax
The **101st Constitutional Amendment Act, 2016** created GST, effective from **1 July 2017**; it is a **destination-based consumption tax** subsuming excise, service tax, VAT, CST, entry tax and luxury tax. Constitutional pegs: **Article 246A** (power to legislate), **269A** (inter-state/IGST apportionment), **279A** (**GST Council**). The Council — Union **Finance Minister as chair**, with the Union Minister of State for Finance and state finance ministers — decides rates and rules by a **three-fourths weighted majority**: Centre holds **one-third** of votes, states together **two-thirds**. Structure: **CGST** (Centre) + **SGST** (state) on intra-state sales; **IGST** on inter-state and imports; the **GSTN** runs the IT backbone.

**Slabs after the GST 2.0 reform (Council decision of 3 September 2025, effective 22 September 2025)**: two principal slabs — **5% (merit)** and **18% (standard)** — plus a **40% rate for demerit goods** (tobacco, pan masala, some luxury items); the old 12% slab was abolished and the 28% rate phased out into the 40% demerit track. Exemptions survive (unprocessed food, education, health). Compensation cess continues on specified demerit goods, now aligned to the 40% rate.

### Income tax — the new code
The **Income-tax Act, 2025** — passed in August 2025, **effective 1 April 2026** — replaces the Income-tax Act of 1961. Its signature reform is the single '**tax year**' replacing the twin concepts of previous year and assessment year; the Act has 536 sections in 23 chapters, in plainer language. Filing stays annual; a default **new regime** with lower slab rates but few deductions coexists with the older optional regime. **Tax devolution** to states flows through the **Finance Commission** (Article 280), the constitutional arbiter of the vertical split.

### Quick revision
- Direct: income, corporate, STT, capital gains. Indirect: GST, customs, excise (petroleum/alcohol), stamp.
- GST: 101st Amendment, 1 July 2017; Articles 246A / 269A / 279A; Council chaired by Union FM, 3/4 majority, Centre 1/3 : states 2/3.
- CGST + SGST intra-state; IGST inter-state; GSTN = IT network.
- GST 2.0: 22 September 2025 — slabs 5% and 18%, 40% demerit, 12% abolished.
- Income-tax Act 2025: effective 1 April 2026, 'tax year' replaces previous/assessment year.
- Agricultural income — no income tax; devolution via Finance Commission."""
    S.pattern("ga-ecoT-p1", "GST Council and constitutional articles", "very common",
        "'Article 279A deals with', 'who chairs the GST Council', 'the Centre has what share of votes', matching GST articles and Council facts.",
        None,
        "1. Articles in a line: **246A** = power to tax, **269A** = IGST on inter-state trade, **279A** = GST Council.\n2. Council: Union **Finance Minister chairs**; members include the Union MoS (Finance) and state finance ministers.\n3. Decisions: **3/4 weighted majority — Centre 1/3, all states together 2/3**.",
        "Under the GST framework, the **GST Council** is constituted under —",
        "**Article 279A**, inserted by the 101st Amendment — chaired by the Union Finance Minister, with decisions by a three-fourths weighted majority (Centre one-third, states two-thirds).")
    S.pattern("ga-ecoT-p2", "GST launch, structure and the 2025 slab reform", "very common",
        "'GST was introduced from', 'which article inserted GST', 'the new GST slabs are', questions naming CGST/SGST/IGST and the 22 September 2025 change.",
        None,
        "1. Launch: **1 July 2017**, via the **101st Constitutional Amendment Act, 2016**; destination-based.\n2. Structure: CGST + SGST intra-state; **IGST** inter-state and on imports; GSTN = IT backbone.\n3. From **22 September 2025** (Council decision 3 September 2025): slabs **5% and 18%**, a **40% demerit rate**, **12% abolished** — the GST 2.0 reform.",
        "After the GST 2.0 reform effective 22 September 2025, the principal GST slabs are —",
        "**5% (merit) and 18% (standard)**, with a **40% rate for demerit goods**; the 12% slab was abolished and the 28% rate retired into the demerit track.")
    S.pattern("ga-ecoT-p3", "Direct vs indirect classification", "common",
        "'Which is a direct tax', 'which tax cannot be shifted', options mixing customs, corporate tax, GST, STT.",
        None,
        "1. Direct = burden on the payer: **income tax, corporate tax, STT, capital gains**.\n2. Indirect = shifted to consumers: **GST, customs, excise (petroleum, alcohol), stamp duties**.\n3. Remember the constitutional split: GST article 246A; agricultural income outside income tax.",
        "Which of the following is a **direct tax**?",
        "**Corporate tax** — levied directly on company profits with no shifting; GST, customs and stamp duty are indirect.")
    S.pattern("ga-ecoT-p4", "Income-tax Act 2025 and the tax year", "common",
        "'The new Income-tax Act is effective from', 'the concept of tax year replaces', questions on the 2025 code replacing the 1961 Act.",
        None,
        "1. **Income-tax Act, 2025** — passed August 2025, **effective 1 April 2026**, replacing the 1961 Act.\n2. Single '**tax year**' replaces previous year + assessment year; 536 sections, 23 chapters, simpler drafting.\n3. Devolution of taxes to states = **Finance Commission (Article 280)**.",
        "The **Income-tax Act, 2025** became operative from —",
        "**1 April 2026** — replacing the 1961 Act and introducing the single '**tax year**' in place of the previous-year/assessment-year pair.")
    S.pattern("ga-ecoT-p5", "Tax bases, exemption and devolution facts", "occasional",
        "'Agricultural income is taxed by', 'corporation tax contributes most to', which head dominates direct-tax collections, devolution mechanics.",
        None,
        "1. **Agricultural income** — outside income tax; taxing it belongs to states.\n2. Direct-tax collections are led by **corporation tax and personal income tax**; GST leads the indirect side.\n3. Centre-state sharing runs through the **Finance Commission's** award; cesses and surcharges sit outside the divisible pool — a standard statement question.",
        "Regarding **agricultural income**, the income-tax law —",
        "Leaves it untaxed: taxing agricultural income is a **state** power, so it stays outside the Income-tax Act's net.")

    S.q("ga-ecoT-p1", "easy", "The **GST Council** was established under —",
        ["Article 246A", "Article 269A", "Article 279A", "Article 280"], "Article 279A",
        "**Article 279A** (101st Amendment, 2016) creates the GST Council; 246A grants the taxing power and 269A handles IGST apportionment. 280 is the Finance Commission.",
        "279 = Council.", 20)
    S.q("ga-ecoT-p1", "medium", "In GST Council decisions, the **Union government's weighted vote share** is —",
        ["One-half", "Two-thirds", "One-third", "Three-fourths"], "One-third",
        "Decisions need a **three-fourths weighted majority**: the Centre holds **one-third** of the votes and all states together **two-thirds** — so states can block, but the Centre can also veto.",
        "Centre 1/3, states 2/3.", 25)
    S.q("ga-ecoT-p1", "hard", "Consider the statements:\n1. The Union Finance Minister chairs the GST Council.\n2. GST on inter-state supply is called IGST.\n3. GST Council decisions are binding recommendations implemented by law.\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are correct — the Union FM chairs, inter-state supply attracts IGST (Article 269A), and Council recommendations are implemented through changes in GST laws.",
        "Chair, IGST, binding recommendations — all true.", 30)
    S.q("ga-ecoT-p2", "easy", "Goods and Services Tax was introduced in India from —",
        ["1 April 2016", "1 July 2017", "1 April 2018", "1 January 2017"], "1 July 2017",
        "GST rolled out on **1 July 2017** under the **101st Constitutional Amendment Act, 2016** — a destination-based tax subsuming excise, service tax, VAT and a host of cesses.",
        "1-7-2017 = GST day.", 20)
    S.q("ga-ecoT-p2", "medium", "Under the **GST 2.0** structure effective 22 September 2025, which slab was **abolished**?",
        ["5%", "12%", "18%", "40%"], "12%",
        "The reform kept **5% (merit)** and **18% (standard)**, added a **40% demerit rate** (tobacco, pan masala, certain luxury goods) and **abolished the 12% slab**, with the 28% rate retired into the demerit track.",
        "5 + 18 + 40; the 12% slab died.", 25)
    S.q("ga-ecoT-p2", "medium", "An intra-state sale under GST attracts —",
        ["IGST only", "CGST and IGST", "CGST and SGST", "SGST only"], "CGST and SGST",
        "Intra-state supply splits between **CGST** (Centre) and **SGST** (state); **IGST** applies only to inter-state supplies and imports.",
        "Inside the state: CGST + SGST.", 20)
    S.q("ga-ecoT-p3", "easy", "Which of the following is an **indirect tax**?",
        ["Corporate tax", "Securities transaction tax", "Customs duty", "Capital-gains tax"], "Customs duty",
        "**Customs duty** is loaded onto import prices and borne by consumers — indirect. Corporate tax, STT and capital-gains tax fall on the taxpayer directly.",
        "Customs = indirect.", 20)
    S.q("ga-ecoT-p3", "medium", "The burden of a **direct tax** —",
        ["Falls on the person who pays it to the government", "Is shifted to consumers", "Is shared equally by buyers and sellers", "Is borne by the next purchaser"], "Falls on the person who pays it to the government",
        "A direct tax **cannot legally be shifted** — the payer suffers it. Indirect taxes are passed down the price chain to the final consumer.",
        "Direct = no shifting.", 20)
    S.q("ga-ecoT-p4", "easy", "The **Income-tax Act, 2025** came into force on —",
        ["1 April 2025", "1 April 2026", "1 January 2026", "1 July 2026"], "1 April 2026",
        "The new code took effect from **1 April 2026**, replacing the Income-tax Act, 1961 and introducing the single '**tax year**'.",
        "2026 = new tax code.", 20)
    S.q("ga-ecoT-p4", "medium", "The '**tax year**' introduced by the Income-tax Act, 2025 —",
        ["Replaces both previous year and assessment year", "Applies only to companies", "Replaces GST return periods", "Is a two-year accounting cycle"], "Replaces both previous year and assessment year",
        "The 2025 Act collapses the twin concepts of 'previous year' and 'assessment year' into one '**tax year**' — a plain-language simplification across its 536 sections.",
        "Two concepts → one tax year.", 25)
    S.q("ga-ecoT-p5", "medium", "Which of the following is **exempt from income tax** under Indian law?",
        ["Salary income", "Agricultural income", "House-rent allowance beyond limits", "Capital gains on shares"], "Agricultural income",
        "**Agricultural income** stays outside income tax — taxing it is a state power. Salaries, HRA above limits and share capital gains are all taxable.",
        "Farms = states' call.", 25)
    S.q("ga-ecoT-p5", "hard", "Consider the statements:\n1. GST is a destination-based consumption tax.\n2. The GSTN provides the IT backbone for GST compliance.\n3. Cesses and surcharges form part of the divisible pool with states.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is the classic trap — **cesses and surcharges sit outside the divisible pool**, so states do not share them under the Finance Commission's award.",
        "Cess never reaches the shared pool.", 30)
    return S


def build_schemes():
    S = Sub("eco-schemes")
    S.notes = """### Reading a scheme question
Every scheme question tests four hooks: **launch year, ministry, benefit/eligibility, and purpose**. Learn them as one line each; the exam never asks beyond these. Monthly 'new scheme' news changes, but the flagships below are permanent fixtures of SSC/Railway/Banking papers.

### Livelihood and employment
- **MGNREGA** (Act 2005, operational 2006): 100 days of guaranteed wage employment per rural household — replaced by **VB-G RAM G** from **1 July 2026**, raising the guarantee to **125 days a year** with weekly wage payments.
- **DAY-NRLM** (2011): rural livelihoods through women's self-help groups; urban twin DAY-NULM (2014).
- **PM SVANidhi** (2020): working-capital loans for street vendors.
- **Deendayal Antyodaya Yojana** umbrella covers both livelihood missions (Ministry of Rural Development / MoHUA).

### Financial inclusion and credit
- **PM Jan Dhan Yojana** — launched **28 August 2014**: zero-balance bank accounts, RuPay card, overdraft facility; the world's largest financial-inclusion drive.
- **MUDRA Yojana** (**8 April 2015**): collateral-free micro-loans in three tiers — **Shishu (up to ₹50,000), Kishor (₹50,000-5 lakh), Tarun (₹5-10 lakh)**.
- **Atal Pension Yojana** (2015): guaranteed pension for unorganised workers aged 18-40.
- **PMSBY** (accident insurance, ₹20/year, cover ₹2 lakh) and **PMJJBY** (life insurance) — the two Jan Suraksha schemes.

### Agriculture and rural
- **PM-KISAN** (Feb 2019): **₹6,000 a year** to landholding farmer families, paid in three DBT instalments.
- **PM Fasal Bima Yojana** (2016): subsidised crop insurance; **e-NAM** (2016): unified electronic mandi.
- **Kisan Credit Card** (1998): short-term crop credit; **PM-KUSUM**: solar pumps for farmers.

### Health, water, housing, fuel
- **Ayushman Bharat PM-JAY** (**23 September 2018**): health cover of **₹5 lakh per family a year** for secondary and tertiary hospitalisation; **ABHA** is its digital health-ID arm, with the **Ayushman Bharat Digital Mission** (September 2021) building the health stack.
- **Jal Jeevan Mission** (**August 2019**, 'Har Ghar Jal'): functional household tap connections.
- **Swachh Bharat Mission** (**2 October 2014**): sanitation and ODF drive; **POSHAN Abhiyaan** (2018): nutrition mission under the WCD ministry.
- **PM Awas Yojana** (urban 2015; Gramin 2016): pucca houses; **PM Ujjwala Yojana** (1 May 2016): free LPG connections to women of poor households.

### Industry and skills
- **Make in India** (25 September 2014); **Startup India** (16 January 2016, DPIIT recognition and tax holidays); **Skill India / PMKVY** (2015); **Production-Linked Incentive (PLI)** schemes (2020); **PM Gati Shakti** (October 2021) national infrastructure master plan; **UDAN** (2016) regional air connectivity.

### Quick revision
- VB-G RAM G (1 July 2026): 125 days, weekly wages — replaced MGNREGA.
- Jan Dhan 28-8-2014; MUDRA 8-4-2015 (Shishu/Kishor/Tarun); APY 2015; PMSBY/PMJJBY insurance.
- PM-KISAN ₹6,000/yr in 3 instalments (2019); Fasal Bima 2016; KCC 1998.
- Ayushman PM-JAY ₹5 lakh/family (2018); JJM 2019; SBM 2-10-2014; Ujjwala 1-5-2016; PMAY 2015/16.
- Make in India 25-9-2014; Startup India 16-1-2016; Gati Shakti 2021; PLI 2020."""
    S.pattern("ga-ecoS-p1", "Scheme ↔ ministry ↔ launch year", "very common",
        "'X scheme was launched in which year', 'which ministry runs X', matching schemes with 2014-2021 launch dates.",
        None,
        "1. Pin the dates: SBM 2-10-2014; Jan Dhan 28-8-2014; MUDRA 8-4-2015; Startup 16-1-2016; JJM 2019; PM-KISAN 2019; Gati Shakti 2021.\n2. Ministry pairs: PMAY-U/Day-NULM/SVANidhi — MoHUA; NRLM/NREGA-line — Rural Development; POSHAN — WCD; UDAN — Civil Aviation.\n3. Anchor on the year first; the ministry usually follows from the scheme's subject.",
        "**Startup India** was launched in —",
        "**January 2016** (16 January) — DPIIT recognition, tax holidays and a fund-of-funds for startups.")
    S.pattern("ga-ecoS-p2", "Scheme ↔ benefit ↔ eligibility", "very common",
        "'₹6,000 a year is paid under', '₹5 lakh health cover belongs to', matching the benefit figure with the right scheme.",
        None,
        "1. Money anchors: PM-KISAN **₹6,000/yr (3 instalments)**; PM-JAY **₹5 lakh/family/yr**; MUDRA tiers ₹50k / ₹5 lakh / ₹10 lakh; APY 18-40 age window.\n2. PMSBY = accident cover ₹20/yr; PMJJBY = life cover; both ₹2 lakh protection.\n3. Match the rupee figure or the age/eligibility first — it eliminates three options at once.",
        "A guaranteed **₹6,000 per year to landholding farmer families** is paid under —",
        "**PM-KISAN** (2019) — direct benefit transfer in three instalments.")
    S.pattern("ga-ecoS-p3", "Employment and livelihood schemes", "common",
        "'How many days of employment does X guarantee', 'which scheme replaced MGNREGA', statements on NRLM self-help groups or SVANidhi vendors.",
        None,
        "1. The wage-employment line: MGNREGA (2005 Act, 100 days) → **VB-G RAM G from 1 July 2026, 125 days, weekly wages**.\n2. Livelihood line: DAY-NRLM (2011) builds **women SHGs** in villages; DAY-NULM (2014) covers urban livelihoods.\n3. PM SVANidhi (2020) = **street vendors'** collateral-free working capital.",
        "The rural employment guarantee that replaced **MGNREGA** from 1 July 2026 is —",
        "**VB-G RAM G** — it lifted the guaranteed days per rural household per year to **125** and moved wages to weekly payment.")
    S.pattern("ga-ecoS-p4", "Financial inclusion schemes", "common",
        "'Zero-balance accounts under', 'Shishu-Kishor-Tarun belong to', which scheme insures against accidents for ₹20 a year.",
        None,
        "1. **Jan Dhan (28-8-2014)** = accounts + RuPay + overdraft; the flagship of financial inclusion.\n2. **MUDRA (8-4-2015)** tiers: Shishu ≤ ₹50,000; Kishor ₹50,000-5 lakh; Tarun ₹5-10 lakh — collateral-free micro-credit.\n3. **APY** = pension for 18-40 unorganised workers; **PMSBY** = ₹2 lakh accident cover at ₹20/year.",
        "The MUDRA loan categories **Shishu, Kishor and Tarun** refer to —",
        "Collateral-free micro-loan sizes: **up to ₹50,000, ₹50,000-5 lakh and ₹5-10 lakh** respectively.")
    S.pattern("ga-ecoS-p5", "Health, water, housing and fuel schemes", "very common",
        "'Har Ghar Jal belongs to', 'the LPG connection scheme is', '₹5 lakh hospitalisation cover', matching social-sector schemes with purposes.",
        None,
        "1. Health: **PM-JAY ₹5 lakh/family** (2018); digital arm **ABDM (2021)** with ABHA IDs.\n2. Water and sanitation: **JJM 2019** (tap connections); **SBM 2-10-2014** (toilets/ODF).\n3. Housing and fuel: **PMAY** (2015 urban / 2016 rural); **Ujjwala 1-5-2016** (free LPG to women).",
        "'**Har Ghar Jal**' — functional tap water connections to every rural household — is the goal of —",
        "**Jal Jeevan Mission**, launched in **August 2019** under the Jal Shakti ministry.")

    S.q("ga-ecoS-p1", "easy", "**Swachh Bharat Mission** was launched on —",
        ["15 August 2014", "2 October 2014", "26 January 2015", "1 May 2016"], "2 October 2014",
        "Launched on **Gandhi Jayanti, 2 October 2014**, with rural (Grameen) and urban arms for sanitation and open-defecation-free status.",
        "Gandhi's birthday = SBM.", 20)
    S.q("ga-ecoS-p1", "medium", "**PM SVANidhi** scheme provides collateral-free working-capital loans to —",
        ["Fishermen", "Street vendors", "Handloom weavers", "Dairy farmers"], "Street vendors",
        "**PM SVANidhi (2020)**, run by MoHUA, gives street vendors working-capital loans with digital-repayment incentives.",
        "SVANidhi = vendors.", 25)
    S.q("ga-ecoS-p1", "medium", "**PM Gati Shakti** — the national master plan for multi-modal infrastructure — was launched in —",
        ["2014", "2016", "2019", "2021"], "2021",
        "Launched **October 2021**, it stitches ministries onto one GIS platform for integrated infrastructure planning.",
        "Gati Shakti = 2021.", 25)
    S.q("ga-ecoS-p2", "easy", "Under **PM-KISAN**, each eligible landholding farmer family receives —",
        ["₹3,000 a year", "₹6,000 a year", "₹10,000 a year", "₹12,000 a year"], "₹6,000 a year",
        "**₹6,000 a year in three DBT instalments** (₹2,000 each), launched February 2019.",
        "6,000 = 3 x 2,000.", 20)
    S.q("ga-ecoS-p2", "medium", "The **₹5 lakh per family per year** hospitalisation cover is provided under —",
        ["PMJJBY", "Ayushman Bharat PM-JAY", "PM Awas Yojana", "PM-KISAN"], "Ayushman Bharat PM-JAY",
        "**PM-JAY (23 September 2018)** covers secondary and tertiary hospitalisation up to ₹5 lakh a family a year; PMJJBY is a life-insurance scheme.",
        "Ayushman = ₹5 lakh cover.", 20)
    S.q("ga-ecoS-p2", "hard", "Match: 1. PM-KISAN 2. PM-JAY 3. MUDRA — with (i) 2019 (ii) 2018 (iii) 2015:",
        ["1-i, 2-ii, 3-iii", "1-ii, 2-i, 3-iii", "1-i, 2-iii, 3-ii", "1-iii, 2-ii, 3-i"], "1-i, 2-ii, 3-iii",
        "PM-KISAN **2019**; PM-JAY **2018**; MUDRA **2015** — the standard launch-year trio.",
        "KISAN '19, JAY '18, MUDRA '15.", 30)
    S.q("ga-ecoS-p3", "easy", "The **VB-G RAM G** scheme, effective 1 July 2026, guarantees —",
        ["75 days of wage employment", "100 days of wage employment", "125 days of wage employment", "150 days of wage employment"], "125 days of wage employment",
        "It replaced MGNREGA's 100-day guarantee with **125 days per rural household per year**, paying wages **weekly**.",
        "125 days, weekly pay.", 20)
    S.q("ga-ecoS-p3", "medium", "**DAY-NRLM** promotes rural livelihoods mainly through —",
        ["Farmer producer companies", "Women's self-help groups", "Contract farming", "Urban micro-enterprises"], "Women's self-help groups",
        "The National Rural Livelihoods Mission (2011) organises rural poor women into **SHGs** for credit access and enterprise; its urban twin is DAY-NULM.",
        "NRLM = women's SHGs.", 25)
    S.q("ga-ecoS-p4", "easy", "Zero-balance bank accounts with a RuPay card and overdraft facility are provided under —",
        ["PMJDY", "PMKVY", "PMAY", "PMGSY"], "PMJDY",
        "**PM Jan Dhan Yojana** (28 August 2014) is the financial-inclusion flagship — accounts, RuPay debit card, accident cover and an overdraft window.",
        "Jan Dhan = accounts for all.", 20)
    S.q("ga-ecoS-p4", "medium", "In **MUDRA** loans, the 'Kishor' category covers loans of —",
        ["Up to ₹50,000", "₹50,000 to ₹5 lakh", "₹5 lakh to ₹10 lakh", "Above ₹10 lakh"], "₹50,000 to ₹5 lakh",
        "MUDRA tiers: **Shishu** ≤ ₹50,000; **Kishor** ₹50,000-5 lakh; **Tarun** ₹5-10 lakh — all collateral-free micro-credit.",
        "Baby → teenager → adult amounts.", 25)
    S.q("ga-ecoS-p4", "hard", "Consider the statements:\n1. Payment banks can issue credit cards.\n2. PMSBY offers ₹2 lakh accidental-death cover for a ₹20 annual premium.\n3. Atal Pension Yojana targets workers aged 18-40.\nWhich are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], "2 and 3 only",
        "Statement 1 is wrong — **payment banks cannot lend or issue credit cards**; statements 2 and 3 describe PMSBY and APY correctly.",
        "Payment banks save; they don't lend.", 30)
    S.q("ga-ecoS-p5", "easy", "'**Har Ghar Jal**' (functional tap connection to every rural home) is the goal of —",
        ["Swachh Bharat Mission", "Jal Jeevan Mission", "Atal Bhujal Yojana", "Namami Gange"], "Jal Jeevan Mission",
        "**Jal Jeevan Mission (August 2019)**, under Jal Shakti, targets piped tap water for all rural households.",
        "Har Ghar Jal = JJM 2019.", 20)
    S.q("ga-ecoS-p5", "medium", "Free **LPG connections** to women of poor households are given under —",
        ["PM Ujjwala Yojana", "Saubhagya", "UDAN", "PMAY-G"], "PM Ujjwala Yojana",
        "**Ujjwala (1 May 2016)** hands LPG connections to women from poor families, cutting indoor smoke; Saubhagya instead electrifies households.",
        "Ujjwala = LPG for women.", 25)
    S.q("ga-ecoS-p5", "hard", "Consider the statements:\n1. The Ayushman Bharat Digital Mission provides digital health IDs (ABHA).\n2. PM Awas Yojana has separate urban and rural arms.\n3. POSHAN Abhiyaan is implemented by the Ministry of Health.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is wrong — **POSHAN Abhiyaan (2018)** runs under the **Ministry of Women and Child Development**, anchored in the ICDS network.",
        "POSHAN lives in the WCD ministry.", 30)
    return S


def build_institutions():
    S = Sub("eco-institutions")
    S.notes = """### Regulators — who watches which market
- **SEBI** — securities market regulator; set up 1988 (executive), statutory by the **SEBI Act, 1992** (after the Harshad Mehta episode); HQ **Mumbai**.
- **IRDAI** — insurance regulator under the **IRDA Act, 1999**; HQ **Hyderabad**.
- **PFRDA** — pension regulator (interim 2003; statutory by the **PFRDA Act, 2013**); runs **NPS** and **APY**; HQ New Delhi.
- **RBI** — banks, NBFCs, payment systems. Others worth a line: **NABARD** (rural credit apex), **SIDBI** (small-industry finance), real-estate **RERA** (2016).

### Development finance institutions
- **NABARD** — **12 July 1982**, on the **Shivaraman committee's** advice, taking over RBI's agricultural-refinance functions; apex for rural credit, refinances RRBs and co-operative banks; HQ Mumbai; owned by the Government of India.
- **SIDBI** — **1990**, HQ **Lucknow**; refinance window for small industries and the fund manager for MUDRA.
- **EXIM Bank** — **1982**, trade finance; **NHB** — **1988**, housing finance regulator-turned-developer of the housing market.

### Markets and exchanges
The **BSE (1875)** — Asia's oldest exchange, began as the Native Share & Stock Brokers' Association — publishes the **Sensex (30 stocks)**. The **NSE** (incorporated 1992, trading from 1994) brought screen-based trading and publishes the **Nifty 50**. **NPCI (2008)**, the payments umbrella body, built **UPI (2016), RuPay, IMPS, FASTag**. Shares are held electronically with two depositories — **NSDL and CDSL** — while the **FSDC** (Financial Stability and Development Council, 2010) coordinates regulators at the apex level, chaired by the Union Finance Minister.

### Multilateral institutions — HQs to memorise
| Institution | Year | HQ | Note |
|---|---|---|---|
| IMF | 1944 (Bretton Woods) | Washington DC | quotas, SDRs, BoP support |
| World Bank | 1944 | Washington DC | IBRD + IDA |
| WTO | **1995** (GATT 1947/48 before) | **Geneva** | 164 members, trade rules |
| **ADB** | **1966** | **Manila** | regional development bank |
| **AIIB** | **2016** | **Beijing** | India an early, large shareholder |
| **New Development Bank** | **2015** | **Shanghai** | BRICS bank; first president K.V. Kamath |
| FATF | 1989 | Paris | money-laundering watchdog (India member since 2010) |

### Quick revision
- SEBI 1992 Act, Mumbai; IRDAI 1999, Hyderabad; PFRDA 2013 Act, New Delhi (NPS).
- NABARD 12-7-1982 (Shivaraman; from RBI agri refinance); SIDBI 1990 Lucknow; EXIM 1982; NHB 1988.
- BSE 1875 (Asia's oldest) → Sensex 30; NSE 1992/94 → Nifty 50; NPCI 2008 → UPI 2016.
- IMF/WB 1944 Washington; WTO 1995 Geneva; ADB 1966 Manila; AIIB 2016 Beijing; NDB 2015 Shanghai (BRICS); FATF Paris."""
    S.pattern("ga-ecoN-p1", "Regulator ↔ sector matching", "very common",
        "'SEBI regulates', 'the insurance regulator is', 'who runs the NPS', matching each regulator with its market.",
        None,
        "1. One line each: **SEBI** — securities; **IRDAI** — insurance; **PFRDA** — pensions (NPS/APY); **RBI** — banks, NBFCs, payments.\n2. Year hooks: SEBI statutory **1992**; IRDAI **1999**; PFRDA statutory **2013** (interim 2003).\n3. If the question names 'stock broker' or 'mutual fund', the answer is SEBI; 'policy-holder' points to IRDAI.",
        "The regulation of the **securities market** in India vests in —",
        "**SEBI**, constituted in 1988 and made statutory by the SEBI Act, **1992**; headquartered in Mumbai.")
    S.pattern("ga-ecoN-p2", "Institution ↔ headquarters", "common",
        "'SIDBI is headquartered at', 'the IRDAI sits in', matching development banks and regulators with cities.",
        None,
        "1. Financial-sector HQs: **SIDBI — Lucknow** (the classic answer); **IRDAI — Hyderabad**; SEBI, NABARD, EXIM — Mumbai; NHB and PFRDA — New Delhi.\n2. Multilaterals: IMF/World Bank — Washington; **ADB — Manila**; **AIIB — Beijing**; **NDB — Shanghai**; WTO — Geneva; FATF — Paris.\n3. Lucknow and Hyderabad are the two 'surprise' HQs exams love.",
        "The **Small Industries Development Bank of India (SIDBI)** is headquartered in —",
        "**Lucknow** — set up in **1990** as the apex refinancer for small industries (and MUDRA's fund manager).")
    S.pattern("ga-ecoN-p3", "Year ↔ founding event", "common",
        "'NABARD was established in', 'Asia's oldest stock exchange is', matching years with institutions.",
        None,
        "1. India: BSE **1875** (Asia's oldest); NSE 1992/1994; NPCI 2008; NABARD **1982**; SIDBI 1990; EXIM 1982; NHB 1988.\n2. Multilaterals: IMF/WB **1944** (Bretton Woods); WTO **1995** (GATT 1947 before); ADB 1966; NDB 2015; AIIB 2016.\n3. 'Oldest exchange in Asia' = **BSE**, born as the Native Share & Stock Brokers' Association.",
        "Which is **Asia's oldest stock exchange**?",
        "The **BSE, Bombay (1875)** — founded as the Native Share & Stock Brokers' Association; the NSE followed only in 1992.")
    S.pattern("ga-ecoN-p4", "Multilateral banks and funds", "common",
        "'The New Development Bank is headquartered at', 'which bank do BRICS countries own', 'the ADB was set up in', matching multilaterals with HQ and membership.",
        None,
        "1. **NDB (2015, Shanghai)** = the **BRICS** bank; first president **K.V. Kamath**.\n2. **AIIB (2016, Beijing)** — India an early member and second-largest shareholder.\n3. IMF = balance-of-payments support, quotas and **SDRs**; World Bank = long-term development lending; both born at **Bretton Woods, 1944**.",
        "The **New Development Bank**, set up by BRICS nations in 2015, is headquartered in —",
        "**Shanghai** — with **K.V. Kamath** as its first president; it funds infrastructure and sustainable development.")
    S.pattern("ga-ecoN-p5", "Indices, exchanges and payment rails", "common",
        "'The Sensex comprises', 'Nifty belongs to which exchange', 'UPI is operated by', matching index ↔ exchange and product ↔ operator.",
        None,
        "1. **Sensex — 30 stocks, BSE**; **Nifty 50 — NSE**; both free-float market-cap weighted.\n2. **NPCI (2008)** operates **UPI, RuPay, IMPS, FASTag, NACH**; UPI went live in **2016**.\n3. Depositories: **NSDL and CDSL** hold shares electronically — a frequent fourth option in such questions.",
        "**UPI** is built and operated by —",
        "**NPCI** (National Payments Corporation of India, est. **2008**) — the umbrella body behind UPI (live 2016), RuPay, IMPS and FASTag.")

    S.q("ga-ecoN-p1", "easy", "**SEBI** was given statutory status by an Act of Parliament in —",
        ["1988", "1992", "2000", "2014"], "1992",
        "Set up in **1988** as an executive body, SEBI became statutory under the **SEBI Act, 1992** — the Harshad Mehta scam year accelerated the change.",
        "1988 born, 1992 empowered.", 20)
    S.q("ga-ecoN-p1", "medium", "The regulation of the **insurance sector** in India rests with —",
        ["SEBI", "IRDAI", "PFRDA", "NABARD"], "IRDAI",
        "The **Insurance Regulatory and Development Authority of India** (IRDA Act, 1999) polices insurers and policy-holders; headquartered at **Hyderabad**.",
        "Insurance = IRDAI.", 20)
    S.q("ga-ecoN-p1", "hard", "Match the regulator to its market: 1. SEBI 2. IRDAI 3. PFRDA — with (i) pensions (ii) securities (iii) insurance:",
        ["1-ii, 2-iii, 3-i", "1-i, 2-ii, 3-iii", "1-iii, 2-i, 3-ii", "1-ii, 2-i, 3-iii"], "1-ii, 2-iii, 3-i",
        "SEBI → **securities**; IRDAI → **insurance**; PFRDA → **pensions** (it administers the NPS and Atal Pension Yojana).",
        "Securities-insurance-pensions.", 30)
    S.q("ga-ecoN-p2", "easy", "**SIDBI** is headquartered in —",
        ["Mumbai", "New Delhi", "Lucknow", "Hyderabad"], "Lucknow",
        "**SIDBI (1990)** sits at **Lucknow** — the odd-one-out HQ among Indian financial institutions, and a repeated exam answer.",
        "SIDBI = Lucknow.", 20)
    S.q("ga-ecoN-p2", "medium", "The **IRDAI** is headquartered at —",
        ["Mumbai", "Hyderabad", "New Delhi", "Chennai"], "Hyderabad",
        "The insurance regulator's headquarters is **Hyderabad**; SEBI and NABARD sit in Mumbai.",
        "IRDAI = Hyderabad.", 25)
    S.q("ga-ecoN-p2", "medium", "**NABARD's** headquarters is located in —",
        ["New Delhi", "Lucknow", "Mumbai", "Nagpur"], "Mumbai",
        "**NABARD (1982)** is headquartered in **Mumbai**, like the RBI and SEBI; it was spun out of the RBI's agricultural refinance function.",
        "NABARD with the RBI in Mumbai.", 25)
    S.q("ga-ecoN-p3", "easy", "**NABARD** was established in —",
        ["1975", "1982", "1990", "1992"], "1982",
        "NABARD came up on **12 July 1982**, on the Shivaraman committee's recommendation, taking over the RBI's agricultural-refinance wing.",
        "NABARD = 1982.", 20)
    S.q("ga-ecoN-p3", "medium", "Which pair is **correctly matched**?",
        ["EXIM Bank — 1990", "NHB — 1982", "SIDBI — 1990", "NABARD — 1975"], "SIDBI — 1990",
        "**SIDBI — 1990** is correct. EXIM Bank is 1982; NHB 1988; NABARD 1982.",
        "EXIM '82, NHB '88, NABARD '82, SIDBI '90.", 25)
    S.q("ga-ecoN-p4", "easy", "The **Asian Development Bank (ADB)** is headquartered in —",
        ["Singapore", "Manila", "Tokyo", "Beijing"], "Manila",
        "The **ADB (1966)** sits at **Manila**, Philippines — the standard HQ question on regional banks.",
        "ADB = Manila.", 20)
    S.q("ga-ecoN-p4", "medium", "The **New Development Bank**, set up by the BRICS countries, is headquartered in —",
        ["Beijing", "Moscow", "Shanghai", "Johannesburg"], "Shanghai",
        "The **NDB (2015)** works from **Shanghai** with **K.V. Kamath** as first president; the AIIB (2016) sits separately in Beijing.",
        "BRICS bank = Shanghai.", 25)
    S.q("ga-ecoN-p5", "easy", "The **Sensex** is an index of —",
        ["50 NSE stocks", "30 BSE stocks", "100 largest companies", "Banking stocks only"], "30 BSE stocks",
        "**Sensex = 30 BSE stocks** (free-float weighted); the NSE's counterpart is the **Nifty 50**.",
        "Sensex 30, Nifty 50.", 20)
    S.q("ga-ecoN-p5", "medium", "Which of the following is **correctly matched**?",
        ["UPI — operated by SEBI", "Nifty — index of the BSE", "RuPay — card network of NPCI", "FASTag — a health-insurance product"], "RuPay — card network of NPCI",
        "**RuPay** is NPCI's domestic card network. UPI belongs to NPCI, not SEBI; Nifty is the **NSE's** index; FASTag is a road-toll payment tag.",
        "NPCI owns RuPay and UPI.", 25)
    return S
