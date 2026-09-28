"""economy deep content — part 1: eco-basics, eco-planning, eco-rbi, eco-inflation."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_basics():
    S = Sub("eco-basics")
    S.notes = """### Counting the economy — the national income family
**GDP (Gross Domestic Product)** is the market value of all **final** goods and services produced **within India** in a year — by Indians or foreigners. **GNP** adds what Indians earn abroad: **GNP = GDP + Net Factor Income from Abroad (NFIA)** — remittances, profits, interest flowing in minus the same flowing out. **NNP = GNP − depreciation** (wear and tear of machines). **National Income** in exam language = **NNP at factor cost**. **Per capita income** = national income ÷ population. Moving between prices: **Market Price = Factor Cost + indirect taxes − subsidies**, because indirect taxes push the price up and subsidies hold it down.

Chains to memorise:
- GDP → (+NFIA) → GNP → (−depreciation) → NNP → (−indirect taxes, +subsidies) → National Income (NNP at FC).
- NNP at factor cost is the textbook definition of 'national income'; GNP is the widest of the family.

### Nominal, real and the deflator
**Nominal (current-price) GDP** uses this year's prices, so it grows even if only prices grow. **Real (constant-price) GDP** uses a fixed **base year's** prices, so it shows real production. The bridge is the **GDP deflator**:

$$\\text{Deflator} = \\frac{\\text{Nominal GDP}}{\\text{Real GDP}} \\times 100$$

If nominal GDP is ₹330 and real GDP is ₹300, the deflator is 110 — prices rose 10% since the base year. Divide nominal by (deflator ÷ 100) to recover real GDP. Base years are **revised periodically**: the older national accounts series used **2011-12**, and MoSPI released a **new series with base year 2022-23** in February 2026 (the IIP followed with the same base from June 2026). Exams frame base-year questions around exactly this revision.

### How it is measured
Three equivalent approaches: the **income method** (wages + rent + interest + profit), the **expenditure method** (private consumption + investment + government spending + net exports: $C + I + G + (X-M)$) and the **product (value-added) method** (output sector by sector, counting only **value added** to avoid double counting). India now anchors sectoral reporting on **Gross Value Added (GVA) at basic prices**, with GDP = GVA + product taxes − product subsidies. The statistical agency is the **National Statistical Office (NSO)** under **MoSPI** (the old CSO and NSSO were merged into it in 2019). Estimates come in stages — advance, provisional, revised, final.

### The three sectors
**Primary** = agriculture, forestry, fishing, mining; **secondary** = manufacturing, construction, electricity; **tertiary (services)** = trade, transport, finance, IT, public administration. Services contribute the biggest share of India's GVA today, which is why exams test sector shares and which activity belongs to which sector. Related small facts: the **eight core industries** (coal, crude oil, natural gas, refinery products, fertilisers, steel, cement, electricity) feed the Index of Eight Core Industries and carry a large weight in the IIP; **per capita income** here means per capita **net national income**, not GDP per head.

### Quick revision
- GDP = within India; GNP = GDP + NFIA; NNP = GNP − depreciation; National Income = NNP at factor cost.
- MP = FC + indirect taxes − subsidies; deflator = (nominal ÷ real) × 100.
- Real GDP uses base-year prices; the current family of series moved to **base year 2022-23** (released Feb 2026), replacing 2011-12.
- Methods: income, expenditure ($C+I+G+X-M$), value-added; GVA at basic prices; NSO under MoSPI (CSO + NSSO merged 2019).
- Sectors: primary / secondary / tertiary; services now the largest GVA share.
- Eight core industries: coal, crude, gas, refinery, fertilisers, steel, cement, electricity."""
    S.pattern("ga-ecoB-p1", "GDP–GNP–NNP chains and definitions", "very common",
        "'GNP equals', 'national income means NNP at factor cost', 'which is the largest measure', statement sets mixing the four aggregates.",
        None,
        "1. Build the ladder in one line: GDP → +NFIA → GNP → −depreciation → NNP → −indirect taxes + subsidies → National Income.\n2. The widest measure is GNP (when NFIA is positive); 'national income' in exams = **NNP at factor cost**.\n3. Watch the trap: GDP excludes NFIA entirely — an option calling GDP 'income of residents at home and abroad' is wrong.",
        "If GDP is ₹100 and net factor income from abroad is ₹5, GNP equals —",
        "**₹105** — GNP = GDP + NFIA; here income earned abroad by residents exceeds what foreigners earn here by 5.")
    S.pattern("ga-ecoB-p2", "Nominal vs real GDP and the deflator", "very common",
        "Numbers for nominal and real GDP are given and the deflator (or real growth) is asked, or statements compare the two concepts.",
        None,
        "1. Deflator = (Nominal ÷ Real) × 100. Compute in one step; the answer is an index number with base year = 100.\n2. Real GDP = Nominal ÷ (deflator ÷ 100).\n3. Real GDP can fall while nominal rises — that is exactly what a high deflator means.",
        "Nominal GDP is ₹330 lakh crore and real GDP ₹300 lakh crore. The GDP deflator is —",
        "(330 ÷ 300) × 100 = **110** — the price level stands 10% above the base year.")
    S.pattern("ga-ecoB-p3", "Base years and the new series", "common",
        "'The new GDP series has which base year', 'which agency releases national accounts', 'the old base was', questions on the 2022-23 / 2011-12 shift.",
        None,
        "1. Old bases: GDP and IIP **2011-12**, CPI **2012**; the new national accounts series uses **2022-23** (released February 2026), with IIP re-based alongside.\n2. Release authority: **NSO under MoSPI** — the CSO and NSSO were merged into the NSO in 2019.\n3. A base year is a reference year whose prices equal 100; both real GDP and indices are measured against it.",
        "India's national accounts statistics are released by —",
        "The **National Statistical Office (NSO)** under the **Ministry of Statistics and Programme Implementation (MoSPI)** — the merged successor of the CSO and NSSO.")
    S.pattern("ga-ecoB-p4", "Per capita income and measurement methods", "occasional",
        "'Per capita income is calculated from', 'the expenditure method adds', which method uses wages-rent-interest-profit.",
        None,
        "1. Per capita income = national income (NNP at FC) ÷ population — not GDP ÷ population.\n2. Methods: income = wages + rent + interest + profit; expenditure = $C + I + G + (X-M)$; value-added = sector-wise GVA.\n3. Double counting is avoided by counting only **value added** at each stage.",
        "The **expenditure method** of measuring national income adds up —",
        "Private final consumption + investment + government expenditure + net exports, i.e. $C + I + G + (X - M)$. The income method instead sums factor incomes.")
    S.pattern("ga-ecoB-p5", "Sectors, GVA and core industries", "occasional",
        "'Which activity belongs to the tertiary sector', 'GVA is measured at which prices', the eight core industries list.",
        None,
        "1. Sectors: primary (agriculture, mining), secondary (manufacturing, construction), tertiary (services).\n2. GVA is measured at **basic prices**; GDP = GVA + product taxes − product subsidies.\n3. Eight core industries: coal, crude oil, natural gas, refinery products, fertilisers, steel, cement, electricity — electricity and refinery carry large weights.",
        "Under the GVA framework, **GDP** is obtained by —",
        "Adding **product taxes** and subtracting **product subsidies** from GVA at basic prices.")

    S.q("ga-ecoB-p1", "easy", "**National income** of India is conventionally defined as —",
        ["GDP at market prices", "NNP at factor cost", "GNP at market prices", "Personal disposable income"], "NNP at factor cost",
        "Textbook national income = **Net National Product at factor cost** — GNP minus depreciation, adjusted for indirect taxes and subsidies.",
        "NI = NNP at FC.", 20)
    S.q("ga-ecoB-p1", "medium", "Which one of the following is **correct**?",
        ["GDP = GNP + NFIA", "GNP = GDP + NFIA", "NNP = GNP + depreciation", "National income = GDP − NFIA"], "GNP = GDP + NFIA",
        "**GNP = GDP + Net Factor Income from Abroad.** The other relations invert or misuse the links: NNP = GNP − depreciation; GDP ignores NFIA.",
        "GNP starts from GDP and adds NFIA.", 25)
    S.q("ga-ecoB-p1", "hard", "Consider the statements:\n1. Depreciation is deducted while moving from GNP to NNP.\n2. Indirect taxes are subtracted while moving from market prices to factor cost.\n3. GDP includes net factor income from abroad.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is wrong — **GNP**, not GDP, brings in net factor income from abroad.",
        "GDP never carries NFIA.", 30)
    S.q("ga-ecoB-p2", "easy", "GDP measured at **constant prices** is called —",
        ["Nominal GDP", "Real GDP", "GVA at basic prices", "Potential GDP"], "Real GDP",
        "**Real GDP** values output at base-year prices, stripping out inflation. Nominal (current-price) GDP mixes price and volume changes.",
        "Constant = real.", 20)
    S.q("ga-ecoB-p2", "medium", "If the GDP deflator is 125 and nominal GDP is ₹500 lakh crore, **real GDP** is —",
        ["₹625 lakh crore", "₹475 lakh crore", "₹400 lakh crore", "₹375 lakh crore"], "₹400 lakh crore",
        "Real GDP = Nominal ÷ (deflator ÷ 100) = 500 ÷ 1.25 = **₹400 lakh crore**. A deflator of 125 means prices are 25% above the base year.",
        "Divide by 1.25, not multiply.", 25)
    S.q("ga-ecoB-p2", "medium", "Nominal GDP rose 12% in a year while the deflator rose 8%. **Real growth** was approximately —",
        ["20%", "4%", "8%", "12%"], "4%",
        "Real growth ≈ nominal growth − inflation measured by the deflator = 12 − 8 = **about 4%**. (Exactly: 1.12/1.08 − 1 = 3.7%.)",
        "Subtract the deflator rise from nominal growth.", 25)
    S.q("ga-ecoB-p3", "medium", "The new series of India's national accounts released in **February 2026** uses which **base year**?",
        ["2011-12", "2015-16", "2022-23", "2024"], "2022-23",
        "MoSPI released the GDP series with **base year 2022-23** in February 2026, replacing the 2011-12 base; the IIP moved to the same base from June 2026.",
        "New accounts = 2022-23.", 20)
    S.q("ga-ecoB-p3", "medium", "The **CSO and NSSO** were merged in 2019 to form —",
        ["NITI Aayog", "The National Statistical Office", "The Finance Commission", "The Indian Statistical Service"], "The National Statistical Office",
        "The merger created the **NSO**, which works under MoSPI and releases GDP, CPI and survey data.",
        "Two old bodies → one NSO (2019).", 25)
    S.q("ga-ecoB-p4", "easy", "**Per capita income** is obtained by dividing —",
        ["GDP by the working population", "National income by total population", "GNP by the number of taxpayers", "Personal income by households"], "National income by total population",
        "Per capita income = **national income ÷ population**. Using GDP or taxpayers would give different, non-standard measures.",
        "NI ÷ population.", 20)
    S.q("ga-ecoB-p4", "medium", "Which of the following is included under the **income method** of measuring national income?",
        ["Wages, rent, interest and profit", "Exports minus imports", "Government final consumption", "Change in inventories only"], "Wages, rent, interest and profit",
        "The income method sums **factor incomes** — wages (labour), rent (land), interest (capital) and profit (enterprise). Expenditure and output methods take the other two routes to the same total.",
        "Income method = factor incomes.", 25)
    S.q("ga-ecoB-p5", "medium", "**Gross Value Added (GVA)** in India's national accounts is measured at —",
        ["Market prices", "Factor cost", "Basic prices", "Constant consumer prices"], "Basic prices",
        "India reports sectoral GVA at **basic prices**; GDP = GVA + product taxes − product subsidies. Market prices sit one step further up.",
        "GVA = basic prices; GDP = GVA + product taxes − subsidies.", 25)
    S.q("ga-ecoB-p5", "hard", "Which of the following belongs to the **secondary sector**?",
        ["Coal mining", "Banking", "Construction of buildings", "Fishing"], "Construction of buildings",
        "**Construction** is secondary (it transforms materials). Mining and fishing are primary; banking is tertiary.",
        "Construction = secondary — a favourite trap.", 25)
    return S


def build_planning():
    S = Sub("eco-planning")
    S.notes = """### From plans to NITI
India adopted planning after independence; the **Planning Commission** was set up on **15 March 1950** by a **Cabinet resolution** (not a statute) with the **Prime Minister as chairman**. It steered **twelve Five Year Plans** from 1951 to 2017. From **1 January 2015** a **Cabinet resolution** replaced it with **NITI Aayog** (National Institution for Transforming India) — a think tank, not a fund-allocating plan body.

### The plan ladder — who believed in what
| Plan | Period | Signature idea |
|---|---|---|
| 1st | 1951-56 | **Harrod-Domar model**; agriculture and irrigation priority |
| 2nd | 1956-61 | **P.C. Mahalanobis model**; heavy industry and capital goods |
| 3rd | 1961-66 | 'Gadgil strategy'; self-reliance; broken by wars and drought |
| Plan Holiday | 1966-69 | Three **annual plans** after the 3rd failed |
| 4th | 1969-74 | 'Growth with stability'; family planning pushed |
| 5th | 1974-78 | Poverty removal ('Garibi Hatao'); terminated early |
| Rolling plan | 1978-80 | The **rolling plan** concept (D.T. Lakdawala) |
| 6th | 1980-85 | Poverty eradication first; IRDP, NREP begin |
| 7th | 1985-90 | Food, work, productivity; Jawahar Rozgar Yojana (1989) |
| Annual plans | 1990-92 | Transition years, economic crisis |
| 8th | 1992-97 | Launched alongside the **1991 reforms** (LPG) |
| 9th | 1997-2002 | 'Growth with social justice and equality' |
| 10th | 2002-07 | 8% growth target; monitoring |
| 11th | 2007-12 | '**Faster and more inclusive growth**' |
| 12th | 2012-17 | 'Faster, more inclusive and **sustainable** growth' — the last plan |

Memory hooks: 2nd plan = Mahalanobis = machines; 8th plan began with liberalisation; 11th = inclusive; 12th = sustainable; the words 'plan holiday' and 'rolling plan' belong to 1966-69 and 1978-80 respectively.

### NITI Aayog — structure and work
The **Prime Minister chairs** NITI Aayog. Its **Governing Council** brings together all Chief Ministers and Lt Governors of UTs; a **Vice-Chairperson** and full-time members are appointed by the PM; a **CEO** runs day-to-day work. Its design philosophy is **cooperative federalism** (states as partners) and **competitive federalism** (states ranked and nudged). Instead of plans it produces planning documents: a **15-year vision**, a **7-year strategy** and a **3-year action agenda**. Its visible products are the indices and programmes exams quote: the **SDG India Index**, the **Multidimensional Poverty Index (MPI)** for states, the **Aspirational Districts Programme (2018, 112 districts)**, the Composite Water Management Index, and school/health innovation reports. Contrast lines asked in exams: Planning Commission allocated plan funds and made five-year plans; NITI Aayog is advisory, does not allocate funds, and works through indices, evidence and monitoring.

### Why this subtopic scores
Questions stay at the level of models, years, themes and NITI structure — all stable facts. Learn one phrase per plan, the two annual-plan interludes, and the three NITI documents, and you can crack any match-the-column on this page.

### Quick revision
- Planning Commission: 15 March 1950, Cabinet resolution, PM as chairman; 12 plans, 1951-2017.
- 1st = Harrod-Domar/agriculture; 2nd = Mahalanobis/heavy industry; Plan Holiday 1966-69; Rolling plan 1978-80.
- 8th = LPG reforms era; 11th = inclusive growth; 12th (2012-17) = last plan, 'sustainable'.
- NITI Aayog: 1 Jan 2015, Cabinet resolution; PM chairs; Governing Council = CMs + LGs; CEO + Vice-Chairperson.
- Documents: 15-year vision, 7-year strategy, 3-year action agenda; no fund allocation.
- Flagship indices: SDG India Index, state MPI, Aspirational Districts (2018)."""
    S.pattern("ga-ecoP-p1", "Plan ↔ model matching", "very common",
        "'The Second Five Year Plan was based on', 'the Harrod-Domar model belongs to which plan', matching thinkers and plans.",
        None,
        "1. Two pairs carry all the marks: **1st plan — Harrod-Domar** (agriculture focus) and **2nd plan — P.C. Mahalanobis** (heavy industry).\n2. The 3rd plan's strategy is attributed to **D.R. Gadgil**.\n3. If the question names 'heavy industry' or 'capital goods', the answer is the Mahalanobis model of the 2nd plan (1956-61).",
        "The **Mahalanobis model**, emphasising heavy industry, was the basis of which plan?",
        "The **Second Five Year Plan (1956-61)** — it pushed capital-goods and machine-building industries behind public-sector investment.")
    S.pattern("ga-ecoP-p2", "Plan ↔ years ↔ theme", "very common",
        "'Growth with stability was the theme of', 'which plan coincided with the 1991 reforms', ordering of plans or spotting the last plan.",
        None,
        "1. Theme hooks: 4th = growth with stability; 9th = growth with social justice; 11th = inclusive growth; 12th = faster, inclusive and sustainable — the **last plan (2012-17)**.\n2. The **8th plan (1992-97)** opened in the liberalisation era; its start was delayed by two annual plans (1990-92).\n3. Interludes: Plan Holiday 1966-69 (after the 3rd); Rolling Plan 1978-80.",
        "'Growth with stability' was the stated objective of which Five Year Plan?",
        "The **Fourth Plan (1969-74)** — it sought growth while controlling the inflation that followed the wars and droughts of the 1960s.")
    S.pattern("ga-ecoP-p3", "NITI Aayog structure and documents", "common",
        "'Who chairs NITI Aayog', 'the Governing Council consists of', 'the 15-year vision / 7-year strategy / 3-year action agenda', statements on NITI's powers.",
        None,
        "1. Chairs: the **Prime Minister**; day-to-day work by a **CEO**; think-tank headship by a **Vice-Chairperson**.\n2. **Governing Council = all Chief Ministers + Lt Governors of UTs** — the federalism showcase.\n3. Documents: **15-year vision, 7-year strategy, 3-year action agenda**; NITI does **not** allocate plan funds.",
        "The **Governing Council** of NITI Aayog includes —",
        "The Prime Minister (chair), the **Chief Ministers of all states** and the **Lt Governors of Union Territories** — making it the main centre-state planning forum.")
    S.pattern("ga-ecoP-p4", "Planning Commission vs NITI Aayog", "common",
        "Statement pairs: fund allocation, statutory vs executive origin, plan body vs think tank, year of replacement.",
        None,
        "1. Both were created by **Cabinet resolution** — neither is statutory or constitutional.\n2. Planning Commission (15 March 1950) allocated funds and made plans; NITI Aayog (1 January 2015) advises, monitors and builds indices.\n3. The Finance Commission — a constitutional body — is the body people confuse with both; it handles tax devolution, not planning.",
        "Which statement about NITI Aayog is **correct**?",
        "It was set up on 1 January 2015 by a **Cabinet resolution**, replacing the Planning Commission as an advisory **think tank** — it neither allocates plan funds nor enjoys statutory status.")
    S.pattern("ga-ecoP-p5", "Plan Holiday, rolling plan and annual plans", "occasional",
        "'The Plan Holiday occurred during', 'the rolling plan concept is associated with', which plans were cut short.",
        None,
        "1. **Plan Holiday: 1966-69** — three annual plans after the 3rd plan collapsed under war and drought.\n2. **Rolling plan: 1978-80** (concept credited to D.T. Lakdawala) — plans revised every year with a moving horizon.\n3. Annual plans also ran in **1990-92** before the delayed 8th plan; the 5th plan (1974-78) was terminated a year early by the Janata government.",
        "The '**Plan Holiday**' in Indian planning refers to —",
        "The years **1966-69**, when three **annual plans** replaced the usual five-year plan after the third plan was derailed by wars and drought.")

    S.q("ga-ecoP-p1", "easy", "The **First Five Year Plan** (1951-56) was based on the —",
        ["Mahalanobis model", "Harrod-Domar model", "Gandhian plan", "Bombay plan"], "Harrod-Domar model",
        "The 1st plan used the **Harrod-Domar** growth model and gave top priority to agriculture and irrigation — a success thanks to good monsoons.",
        "1st = Harrod-Domar = farms.", 20)
    S.q("ga-ecoP-p1", "medium", "The strategy of heavy industry and capital goods was the hallmark of the —",
        ["First Plan", "Second Plan", "Fourth Plan", "Seventh Plan"], "Second Plan",
        "The **2nd plan (1956-61)** followed **P.C. Mahalanobis's** model — public investment in machine-building and basic industries.",
        "2nd plan = Mahalanobis = machines.", 20)
    S.q("ga-ecoP-p1", "medium", "The 'Gadgil strategy' is associated with which Five Year Plan?",
        ["Second", "Third", "Fifth", "Ninth"], "Third",
        "The **3rd plan (1961-66)** is linked to **D.R. Gadgil's** strategy of self-reliant growth; it was upset by the 1962 and 1965 wars and droughts, leading to the Plan Holiday.",
        "3rd = Gadgil → Plan Holiday.", 25)
    S.q("ga-ecoP-p2", "easy", "Which was the **last Five Year Plan** of India?",
        ["Tenth (2002-07)", "Eleventh (2007-12)", "Twelfth (2012-17)", "Thirteenth (2017-22)"], "Twelfth (2012-17)",
        "The **12th plan (2012-17)** — 'faster, more inclusive and sustainable growth' — was the final plan; from 2017 NITI Aayog's multi-year documents replaced plans.",
        "12 = the end of the plan era.", 20)
    S.q("ga-ecoP-p2", "medium", "The Eighth Five Year Plan (1992-97) is remembered for —",
        ["The rolling plan concept", "Launching alongside the liberalisation reforms", "The Garibi Hatao slogan", "The Plan Holiday"], "Launching alongside the liberalisation reforms",
        "The **8th plan** ran with the **1991 New Economic Policy** — liberalisation, privatisation, globalisation (LPG). It began two years late after annual plans in 1990-92.",
        "8th = LPG era.", 25)
    S.q("ga-ecoP-p2", "hard", "Arrange chronologically:\n1. Plan Holiday 2. Rolling plan 3. Twelfth plan 4. Eleventh plan",
        ["1, 2, 4, 3", "2, 1, 3, 4", "1, 2, 3, 4", "4, 3, 2, 1"], "1, 2, 4, 3",
        "Plan Holiday (1966-69) → Rolling plan (1978-80) → 11th plan (2007-12) → 12th plan (2012-17).",
        "Holiday, rolling, inclusive, sustainable.", 30)
    S.q("ga-ecoP-p3", "easy", "**NITI Aayog** was established on —",
        ["15 March 1950", "1 January 2015", "26 January 2014", "1 April 2016"], "1 January 2015",
        "NITI Aayog began on **1 January 2015** by a Cabinet resolution, replacing the Planning Commission created on 15 March 1950.",
        "1-1-2015 = NITI day.", 20)
    S.q("ga-ecoP-p3", "medium", "Who is the **chairman** of NITI Aayog?",
        ["The Finance Minister", "The Prime Minister", "The Vice-Chairperson", "The CEO"], "The Prime Minister",
        "The **Prime Minister chairs** NITI Aayog. A Vice-Chairperson leads the think-tank work and a CEO (Secretaries-level officer) administers it.",
        "PM chairs; CEO runs.", 20)
    S.q("ga-ecoP-p3", "hard", "Consider the statements about NITI Aayog:\n1. It allocates plan funds to states.\n2. Its Governing Council includes all Chief Ministers.\n3. It has produced a 3-year action agenda.\nWhich are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], "2 and 3 only",
        "Statement 1 is wrong — NITI Aayog is **advisory** and does not allocate plan funds. Its Governing Council unites CMs and UT Lt Governors, and its planning documents include the 3-year action agenda.",
        "NITI advises; it does not fund.", 30)
    S.q("ga-ecoP-p4", "medium", "Which one of the following pairs is **correctly matched**?",
        ["Planning Commission — statutory body", "NITI Aayog — constitutional body", "Both — created by Cabinet resolution", "NITI Aayog — created 1950"], "Both — created by Cabinet resolution",
        "Both institutions were born of **Cabinet resolutions** (1950 and 2015) — neither statute nor Constitution created them. The Finance Commission, by contrast, is constitutional.",
        "Resolution-born, both of them.", 25)
    S.q("ga-ecoP-p4", "medium", "The **Aspirational Districts Programme** is run by —",
        ["The Finance Commission", "NITI Aayog", "The Reserve Bank of India", "The Ministry of Finance"], "NITI Aayog",
        "NITI Aayog launched the programme in **2018** covering **112** backward districts, nudging them on health, nutrition, education and infrastructure through real-time monitoring.",
        "112 districts, NITI, 2018.", 25)
    S.q("ga-ecoP-p5", "medium", "The **rolling plan** concept was in operation during —",
        ["1966-69", "1978-80", "1990-92", "2017-20"], "1978-80",
        "The **rolling plan (1978-80)** revised targets annually with a moving horizon — the concept is associated with **D.T. Lakdawala**. 1966-69 is the Plan Holiday.",
        "Rolling = 1978-80; holiday = 1966-69.", 25)
    S.q("ga-ecoP-p5", "hard", "Consider the statements:\n1. The Fifth Plan was terminated before its full term.\n2. Annual plans were also used in 1990-92.\n3. The Plan Holiday followed the Second Plan.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct — the 5th plan was cut short in 1978 and annual plans ran in 1990-92. Statement 3 is wrong: the Plan Holiday followed the **Third** plan (1966-69).",
        "Holiday after the 3rd, not the 2nd.", 30)
    return S


def build_rbi():
    S = Sub("eco-rbi")
    S.notes = """### The Reserve Bank of India — the monetary authority
The RBI was set up under the **RBI Act, 1934** and began work on **1 April 1935** (headquarters then Calcutta, moved to **Mumbai** in 1937). It was **nationalised on 1 January 1949** — the same year the Banking Regulation Act arrived. It is the **central bank**: sole issuer of currency (except the **₹1 note and coins**, issued by the Government of India's Finance Ministry), banker to the government, banker to banks and **lender of last resort**, custodian of forex reserves, and regulator of banks and payment systems.

### The policy toolkit
- **Repo rate**: the rate at which the RBI lends short-term to banks against securities — the main **policy rate**.
- **Standing Deposit Facility (SDF)**: since April 2020 the **floor** of the corridor — banks park surplus funds with the RBI **without collateral**, at repo **− 25 basis points**.
- **Marginal Standing Facility (MSF)**: the **ceiling** at repo **+ 25 basis points**; banks may dip into it at night borrowing above their SLR holdings. The **Bank Rate** equals the MSF.
- **CRR (Cash Reserve Ratio)**: the share of deposits banks must keep **as cash with the RBI** — earns no interest. **SLR (Statutory Liquidity Ratio)**: the share kept in **liquid assets** (governments securities, gold) with the bank itself. The RBI moves CRR/SLR to absorb or release liquidity.
- **Open Market Operations (OMOs)**, LAF auctions, and forex swaps fine-tune liquidity daily.

### The Monetary Policy Committee
Since the **RBI (Amendment) Act, 2016**, policy decisions rest with a **six-member MPC** — three from the RBI (the Governor with a **casting vote**) and three outside members appointed by the government. It meets **bi-monthly** and targets **CPI inflation of 4% with a ±2% band**; missing the band for **three consecutive quarters** triggers a report to the government. The framework's nominal anchor is **headline CPI**, not WPI.

### Money supply and bank history
Money stock tiers: **M1 = currency with the public + demand deposits with banks + other deposits with the RBI** (narrow money); M2 = M1 + post-office savings; **M3 = M1 + time deposits** (broad money — the headline aggregate); M4 = M3 + post-office deposits (excluding NSCs). History pins: **SBI** = Imperial Bank of India nationalised in **1955**; its subsidiaries came in 1959. **14 major private banks nationalised on 19 July 1969** and **six more in April 1980**. **Regional Rural Banks** began in **1975** (first: Prathama Grameen Bank). Deposit insurance runs through the **DICGC** (limit **₹5 lakh** per depositor per bank since 2020). **NPCI (2008)** built UPI, RuPay, IMPS and FASTag rails; **payment banks** and **small finance banks** followed the **Nachiket Mor committee (2014)** — payment banks take deposits but cannot lend.

### Quick revision
- RBI Act 1934; working 1 April 1935; nationalised 1 Jan 1949; HQ Mumbai; issues all currency except ₹1 note and coins.
- Corridor: SDF = repo − 25 bp (floor); MSF = Bank Rate = repo + 25 bp (ceiling).
- CRR = cash with RBI; SLR = liquid assets with the bank; OMO = buying/selling G-secs.
- MPC: 6 members (3 RBI, Governor casting vote), bi-monthly, CPI 4% ± 2%, breach = 3 quarters.
- M1 = currency + demand deposits + other RBI deposits; M3 = M1 + time deposits.
- 1955 SBI; 1969 (14 banks); 1980 (6 banks); 1975 RRBs; DICGC ₹5 lakh; NPCI 2008 (UPI 2016)."""
    S.pattern("ga-ecoR-p1", "RBI identity, history and currency facts", "very common",
        "'The RBI was established under which Act', 'when was it nationalised', 'which note does the RBI not issue', 'where is its headquarters'.",
        None,
        "1. Anchors: RBI Act **1934**, operations from **1 April 1935**, nationalised **1 January 1949**, HQ **Mumbai**.\n2. Currency split: RBI issues ₹2 and above; the **₹1 note and all coins** come from the **Finance Ministry**.\n3. The RBI is the bankers' bank and **lender of last resort** — commercial banks are its clients, not the public.",
        "The **one-rupee note** in India is issued by —",
        "The **Government of India (Finance Ministry)** — the RBI issues all other denominations; coins are also minted by the government.")
    S.pattern("ga-ecoR-p2", "Policy rates and the corridor", "very common",
        "'SDF is how much below the repo rate', 'the bank rate equals', 'which rate is the policy rate', matching rate ↔ instrument.",
        None,
        "1. Learn the corridor as positions, not numbers: **SDF = repo − 25 bp (floor)**; **MSF = Bank Rate = repo + 25 bp (ceiling)**.\n2. Repo = RBI lends to banks (policy rate); SDF = banks park surplus without collateral; MSF = emergency overnight borrowing.\n3. CRR and SLR are ratios, not rates — do not call them 'policy rates'.",
        "The **Standing Deposit Facility (SDF)** is placed —",
        "**25 basis points below the repo rate** — the corridor floor where banks deposit surplus liquidity with the RBI without providing collateral.")
    S.pattern("ga-ecoR-p3", "Monetary Policy Committee and the inflation target", "very common",
        "'How many members sit on the MPC', 'who holds the casting vote', 'the inflation target is', 'how often does the MPC meet'.",
        None,
        "1. **6 members**: three from the RBI (the Governor, a Deputy Governor and one RBI officer) and three outside experts appointed by the government. The **Governor has the casting vote**.\n2. Target: **CPI 4% ± 2%**; meetings **bi-monthly**; failure = 3 consecutive quarters outside the band.\n3. Legal base: RBI (Amendment) Act, **2016**; the WPI is not the target.",
        "The **casting vote** in the Monetary Policy Committee belongs to —",
        "The **RBI Governor** — with six members, a 3-3 split is broken by the Governor's casting vote.")
    S.pattern("ga-ecoR-p4", "CRR, SLR and liquidity tools", "common",
        "'CRR is kept with', 'SLR consists of', 'which tool releases liquidity immediately', statement sets contrasting CRR and SLR.",
        None,
        "1. **CRR** = cash **with the RBI**, no interest; **SLR** = the bank's own holdings of G-secs/gold/other approved liquid assets.\n2. Cutting CRR or SLR, buying G-secs (OMO), or lowering repo — each injects ease; the reverse tightens.\n3. The MSF ceiling exists so banks in stress can borrow overnight even beyond SLR holdings.",
        "The **Cash Reserve Ratio (CRR)** requires banks to keep —",
        "A fixed share of their net demand and time liabilities **as cash balances with the RBI**, on which no interest is paid.")
    S.pattern("ga-ecoR-p5", "Money supply tiers and banking milestones", "common",
        "'M1 consists of', 'which is the broad money measure', '14 banks were nationalised in', 'the first RRB was', DICGC and NPCI facts.",
        None,
        "1. M1 = currency with public + **demand deposits** + other deposits with RBI; **M3 = M1 + time deposits** = broad money.\n2. Bank history: SBI 1955 (Imperial Bank); **1969 = 14 banks**; **1980 = 6 banks**; RRBs 1975 (Prathama).\n3. Systems: DICGC insurance **₹5 lakh**; NPCI (2008) runs UPI/RuPay/IMPS; payment banks (Nachiket Mor) take deposits, cannot lend.",
        "Which of the following is included in **M1** but not in M3?",
        "Nothing — **M3 is M1 plus time deposits**, so every M1 component sits inside M3. Watch such trap options carefully in 'narrow vs broad money' questions.")

    S.q("ga-ecoR-p1", "easy", "The Reserve Bank of India was **nationalised** on —",
        ["1 April 1935", "1 January 1949", "19 July 1969", "15 August 1947"], "1 January 1949",
        "The RBI, created under the RBI Act 1934 and operational from 1 April 1935, was **nationalised on 1 January 1949** — ownership moved from private shareholders to the government.",
        "1935 = born; 1949 = nationalised.", 20)
    S.q("ga-ecoR-p1", "medium", "The headquarters of the RBI moved to **Mumbai** in —",
        ["1935", "1937", "1949", "1955"], "1937",
        "The RBI opened in **Calcutta** in 1935 and shifted permanently to **Mumbai in 1937**.",
        "Two years in Kolkata, then Mumbai.", 25)
    S.q("ga-ecoR-p1", "medium", "Which of the following is **not** issued by the Reserve Bank of India?",
        ["₹500 note", "₹100 note", "₹1 note", "₹2,000 note"], "₹1 note",
        "The **₹1 note** (and all coins) are issued by the **Government of India**; the RBI issues the rest of the currency.",
        "One-rupee = government's note.", 20)
    S.q("ga-ecoR-p2", "easy", "The **repo rate** is the rate at which —",
        ["Banks lend to the RBI", "The RBI lends short-term funds to banks", "Banks lend to customers", "The government borrows from banks"], "The RBI lends short-term funds to banks",
        "**Repo** = the RBI repurchases-securities rate — it lends to banks against government securities; that is why it is the main **policy rate**. The reverse direction (banks park funds) is the SDF.",
        "Repo = RBI → banks.", 20)
    S.q("ga-ecoR-p2", "medium", "The **Bank Rate** in India's current framework is kept equal to —",
        ["The SDF rate", "The repo rate", "The MSF rate", "The reverse repo rate"], "The MSF rate",
        "The **Bank Rate** sits at the **MSF** level — repo **+ 25 basis points** — at the corridor ceiling; the SDF (repo − 25 bp) marks the floor.",
        "Bank Rate = MSF = repo + 25 bp.", 25)
    S.q("ga-ecoR-p2", "hard", "Arrange the rates for a given repo rate r (highest first):",
        ["MSF, Repo, SDF", "SDF, Repo, MSF", "Repo, MSF, SDF", "MSF, SDF, Repo"], "MSF, Repo, SDF",
        "The corridor is **SDF (r − 25 bp) < repo (r) < MSF (r + 25 bp)**. The ceiling is the MSF/bank rate; the floor is the collateral-free SDF.",
        "Ceiling MSF, floor SDF.", 30)
    S.q("ga-ecoR-p3", "easy", "The **Monetary Policy Committee** has how many members?",
        ["Four", "Five", "Six", "Nine"], "Six",
        "The **six-member MPC** (RBI Act amendment, 2016) has three RBI members — including the Governor, who holds the casting vote — and three government-appointed external members.",
        "Six: three inside, three outside.", 20)
    S.q("ga-ecoR-p3", "medium", "India's **inflation target** for monetary policy is —",
        ["4% WPI inflation with a ±2% band", "4% CPI inflation with a ±2% band", "5% CPI inflation with a ±1% band", "2% CPI inflation with no band"], "4% CPI inflation with a ±2% band",
        "The flexible inflation target is **4% CPI, ±2%** — set under the 2016 framework; breaching the band for three straight quarters forces a written report to the government.",
        "4 ± 2, CPI, never WPI.", 20)
    S.q("ga-ecoR-p3", "medium", "If inflation breaches the target band for **three consecutive quarters**, the RBI must —",
        ["Resign en masse", "Submit a written report to the government", "Raise the repo rate immediately", "Suspend the MPC"], "Submit a written report to the government",
        "The framework's failure clause: three consecutive quarters outside the 4 ± 2% band obliges the MPC majority and the Governor to **report to the government** the reasons, remedies and the time frame for return.",
        "3 quarters out = write a report.", 25)
    S.q("ga-ecoR-p4", "medium", "Which statement about **SLR** is correct?",
        ["It is kept as cash with the RBI", "It must be maintained in liquid assets such as government securities", "It earns no return for banks", "It is set by the Government of India"], "It must be maintained in liquid assets such as government securities",
        "**SLR** is the bank's own stock of **liquid assets** — G-secs, gold and approved securities. CRR, not SLR, is cash with the RBI; SLR holdings do earn returns; the RBI sets the ratio under the Banking Regulation Act.",
        "SLR = securities with the bank; CRR = cash with RBI.", 25)
    S.q("ga-ecoR-p4", "medium", "To **inject liquidity** into the system, the RBI can —",
        ["Sell government securities in OMOs", "Buy government securities in OMOs", "Raise the CRR", "Raise the SDF rate"], "Buy government securities in OMOs",
        "Open-market **purchases** pay banks money and add liquidity. Sales, higher CRR, or higher rates all drain liquidity.",
        "Buy = inject; sell = drain.", 25)
    S.q("ga-ecoR-p5", "easy", "**14 major commercial banks** were nationalised in —",
        ["1955", "1969", "1980", "1991"], "1969",
        "On **19 July 1969** fourteen big private banks were nationalised; **six** more followed in **1980**, deepening credit reach.",
        "14 in '69, 6 in '80.", 20)
    S.q("ga-ecoR-p5", "medium", "The **State Bank of India** was created in 1955 by nationalising the —",
        ["Bank of Hindustan", "Imperial Bank of India", "Allahabad Bank", "Central Bank of India"], "Imperial Bank of India",
        "The **Imperial Bank of India** became SBI under the SBI Act, 1955; its state-bank subsidiaries followed in 1959 (merged back into SBI in 2017).",
        "Imperial → SBI, 1955.", 25)
    S.q("ga-ecoR-p5", "hard", "Consider the statements:\n1. Payment banks can undertake lending activities.\n2. The DICGC insures bank deposits up to ₹5 lakh.\n3. NPCI operates the UPI system.\nWhich are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], "2 and 3 only",
        "Statement 1 is wrong — **payment banks accept deposits and remit funds but cannot lend**. Statements 2 and 3 are correct: DICGC cover is ₹5 lakh per depositor per bank, and NPCI runs UPI, RuPay and IMPS.",
        "Payment banks: deposits yes, loans never.", 30)
    return S


def build_inflation():
    S = Sub("eco-inflation")
    S.notes = """### What inflation is
Inflation is a **sustained rise in the general price level** — the same ₹100 buys less over time. Its two engines: **demand-pull** (too much money chasing too few goods — often after tax cuts, cheap credit or high government spending) and **cost-push** (costlier inputs — oil, fertiliser, wages — push prices up even when demand is soft). Related labels: **deflation** (falling prices), **disinflation** (inflation falling but still positive), **stagflation** (high inflation + stagnating growth), **headline inflation** (all items) vs **core inflation** (headline minus food and fuel — the 'underlying' trend).

### The price indices — who measures what
| Index | Agency | Base year status |
|---|---|---|
| **CPI (Combined)** — headline, rural, urban | **NSO, MoSPI** | old base **2012**; new series with base **2024** released February 2026 |
| **WPI** | Office of Economic Adviser, **DPIIT** (Commerce Ministry) | old base **2011-12**; new series **2022-23** launched June 2026 with a wider basket (697 → 957 items) and new **Producer Price Indices** |
| **CPI-IW** (industrial workers) | **Labour Bureau** | used for dearness allowance |
| CPI-AL / CPI-RL (agri/rural labourers) | Labour Bureau | — |
| **IIP** (industrial output, not prices) | NSO | old base 2011-12; re-based to **2022-23** from June 2026 |

Key contrasts exams test: the **WPI covers only goods — no services** — and measures prices at the **wholesale/producer** stage; the **CPI measures retail prices** paid by consumers and includes services. Since 2016 the RBI's inflation target is framed on **CPI**, not WPI. The **Eight Core Industries index** (coal, crude oil, natural gas, refinery, fertilisers, steel, cement, electricity) is a high-frequency output series feeding the IIP.

### Reading the numbers
CPI/WPI changes are reported as **year-on-year** per cent. Food and beverages carry the largest weight in the CPI basket, which is why a monsoon shock moves headline inflation sharply while core stays steadier — a favourite statement question. The **GDP deflator** (nominal ÷ real × 100) is the economy-wide price gauge used in national accounts. For fiscal policy, the government watches inflation because it drives **dearness allowance**, indexation and subsidy bills.

### Quick revision
- Demand-pull = excess demand; cost-push = input costs; stagflation = inflation + stagnation; core = headline − food & fuel.
- CPI = retail, includes services, NSO/MoSPI; new base year 2024 (Feb 2026). WPI = wholesale, goods only, DPIIT; new base 2022-23 (Jun 2026) + PPIs.
- CPI-IW/AL/RL = Labour Bureau (DA linkage uses CPI-IW).
- RBI targets CPI (4% ± 2%), never WPI.
- IIP = industrial production (re-based 2022-23); eight core industries feed it.
- Deflation = falling prices; disinflation = slower positive inflation."""
    S.pattern("ga-ecoI-p1", "Identify the inflation type", "very common",
        "A story (oil price shock, monsoon failure, credit boom) is given and the type — demand-pull or cost-push — is asked; sometimes deflation/stagflation options appear.",
        None,
        "1. Ask: did demand rise (tax cuts, cheap loans, spending) → **demand-pull**; or did costs rise (crude, wages, inputs) → **cost-push**.\n2. Stagflation = inflation **plus** stagnant growth — cost-push shocks often produce it.\n3. Deflation = general prices **falling**; disinflation = inflation slowing but positive.",
        "A sharp rise in **imported crude oil prices** pushing up general prices is an example of —",
        "**Cost-push inflation** — the input-cost shock passes into transport, manufacturing and retail prices even without excess demand.")
    S.pattern("ga-ecoI-p2", "Index ↔ agency ↔ coverage", "very common",
        "'The WPI is compiled by', 'which index does the RBI target', 'which index covers services', agency and coverage matching.",
        None,
        "1. Agencies: CPI (Combined) — **NSO/MoSPI**; WPI — **Office of Economic Adviser (DPIIT)**; CPI-IW/AL/RL — **Labour Bureau**.\n2. Coverage: WPI = **goods only, wholesale stage, no services**; CPI = **retail, includes services**.\n3. The RBI's 4 ± 2% target uses **CPI**, never WPI.",
        "The **Wholesale Price Index** in India is released by —",
        "The **Office of Economic Adviser** in the Department for Promotion of Industry and Internal Trade (Commerce & Industry Ministry) — not the NSO.")
    S.pattern("ga-ecoI-p3", "Base years and new series", "common",
        "'The new CPI series uses which base year', 'the WPI basket was expanded to', 'the IIP base', matching index ↔ base year.",
        None,
        "1. New anchors: CPI base **2024** (from February 2026); WPI and IIP base **2022-23** (WPI series June 2026, IIP from June 2026); old bases were 2012 (CPI) and 2011-12 (WPI/IIP).\n2. The 2026 WPI revision enlarged the basket from **697 to 957 items** and launched **Producer Price Indices** alongside.\n3. A base year's index = 100; a series revision resets weights to a recent consumption/production structure.",
        "The new **Consumer Price Index** series released in February 2026 has base year —",
        "**2024** — replacing the 2012 base; GDP and WPI/IIP use the fiscal-year base 2022-23 instead.")
    S.pattern("ga-ecoI-p4", "Core vs headline and related terms", "common",
        "'Core inflation excludes', 'headline inflation means', statement sets pairing food/fuel exclusions with monetary relevance.",
        None,
        "1. **Core = headline − food and fuel** — it shows the underlying trend the MPC watches alongside headline CPI.\n2. Headline = the full published index; food's big CPI weight makes headline jump with supply shocks.\n3. Terms: disinflation = slower inflation; deflation = negative; reflation = policy-driven recovery of prices.",
        "**Core inflation** is best described as —",
        "Headline inflation **excluding food and fuel** — the steadier 'underlying' gauge that central banks read to judge persistent pressure.")
    S.pattern("ga-ecoI-p5", "CPI variants, IIP and core industries", "occasional",
        "'DA is linked to which CPI', 'IIP measures', 'the eight core industries include', matching small facts around price and output indices.",
        None,
        "1. CPI-IW (industrial workers, **Labour Bureau**) drives dearness allowance; CPI-AL/RL track farm and rural labourers.\n2. **IIP measures output**, not prices — short-term industrial production trends.\n3. Eight core industries: coal, crude oil, natural gas, refinery products, fertilisers, steel, cement, electricity — they carry a large IIP weight.",
        "The index used for revising **dearness allowance** of central employees is —",
        "**CPI-IW** (Consumer Price Index for Industrial Workers), compiled by the **Labour Bureau**.")

    S.q("ga-ecoI-p1", "easy", "A **continuous fall in the general price level** is called —",
        ["Disinflation", "Deflation", "Stagflation", "Reflation"], "Deflation",
        "**Deflation** = prices falling on average. Disinflation is only a slowdown in positive inflation; stagflation pairs inflation with stagnant growth.",
        "Deflation = negative inflation.", 20)
    S.q("ga-ecoI-p1", "medium", "Inflation caused by **excess aggregate demand** over available output is —",
        ["Cost-push inflation", "Demand-pull inflation", "Stagflation", "Imported inflation"], "Demand-pull inflation",
        "**Demand-pull** = 'too much money chasing too few goods' — from credit booms, tax cuts or spending surges. Input-cost shocks (crude, wages) create cost-push inflation.",
        "Pull = demand; push = costs.", 20)
    S.q("ga-ecoI-p1", "hard", "An economy shows **rising prices along with falling output and rising unemployment**. This is —",
        ["Demand-pull inflation", "Cost-push inflation", "Stagflation", "Deflation"], "Stagflation",
        "**Stagflation** = stagnation (weak growth, job losses) plus inflation — the classic outcome of a severe cost-push shock, as in the 1970s oil crises.",
        "Stag(nation) + (in)flation.", 30)
    S.q("ga-ecoI-p2", "easy", "The **CPI (Combined)** for India is released by —",
        ["DPIIT", "The Labour Bureau", "NSO under MoSPI", "The RBI"], "NSO under MoSPI",
        "The **National Statistical Office** (Ministry of Statistics and Programme Implementation) compiles CPI Combined, rural and urban series. DPIIT does the WPI; the Labour Bureau does CPI-IW/AL/RL.",
        "CPI = NSO; WPI = OEA/DPIIT.", 20)
    S.q("ga-ecoI-p2", "medium", "Which statement about the **WPI** is correct?",
        ["It includes services", "It is compiled by the NSO", "It measures prices at the wholesale/producer stage and covers only goods", "It is the RBI's inflation target"], "It measures prices at the wholesale/producer stage and covers only goods",
        "The WPI tracks **wholesale-stage prices of goods** — services stay out. The NSO's CPI is the retail gauge, and the RBI targets **CPI**, not WPI.",
        "WPI: goods, wholesale, no services.", 25)
    S.q("ga-ecoI-p2", "medium", "The **Reserve Bank's inflation target** is framed on —",
        ["WPI inflation", "CPI (Combined) inflation", "GDP deflator", "Core inflation alone"], "CPI (Combined) inflation",
        "Since 2016 the nominal anchor is **headline CPI (Combined)** at 4% ± 2% — the WPI is watched but not targeted.",
        "Target = headline CPI.", 20)
    S.q("ga-ecoI-p3", "medium", "The **new WPI series (2022-23 base)** launched in June 2026 —",
        ["Included services for the first time", "Expanded the basket from 697 to 957 items and added Producer Price Indices", "Shifted compilation to the NSO", "Replaced the CPI as the target index"], "Expanded the basket from 697 to 957 items and added Producer Price Indices",
        "The revised series widened the basket to **957 items** and introduced **PPIs** alongside the WPI; services remain outside the headline WPI and compilation stays with DPIIT's Office of Economic Adviser.",
        "WPI revision = wider basket + PPI.", 25)
    S.q("ga-ecoI-p3", "medium", "Before the current revisions, the base years of **CPI and WPI** respectively were —",
        ["2011-12 and 2011-12", "2012 and 2011-12", "2011-12 and 2012", "2010 and 2004-05"], "2012 and 2011-12",
        "The old CPI series used calendar-year base **2012**; the old WPI used **2011-12**. The new bases are 2024 (CPI) and 2022-23 (WPI).",
        "CPI 2012, WPI 2011-12.", 25)
    S.q("ga-ecoI-p4", "easy", "**Core inflation** excludes —",
        ["Food and fuel", "Services", "Manufactured products", "Housing"], "Food and fuel",
        "**Core = headline − food and fuel**, filtering out volatile supply-driven swings to reveal underlying price pressure.",
        "Core = cut food + fuel.", 20)
    S.q("ga-ecoI-p4", "medium", "Which one of the following is **correctly matched**?",
        ["Disinflation — prices falling", "Stagflation — inflation with stagnant growth", "Deflation — inflation slowing", "Reflation — prices constant"], "Stagflation — inflation with stagnant growth",
        "Stagflation pairs **inflation with stagnation**. Disinflation = slower (still positive) inflation; deflation = falling prices; reflation = measures to lift prices/demand back up.",
        "Stag + flation = stuck but rising.", 25)
    S.q("ga-ecoI-p5", "medium", "The dearness allowance of central government employees is revised using —",
        ["WPI", "CPI-IW", "CPI-AL", "The GDP deflator"], "CPI-IW",
        "**CPI-IW** (Industrial Workers), compiled by the **Labour Bureau**, is the DA anchor. CPI-AL/RL serve agricultural and rural labourers.",
        "DA follows CPI-IW.", 25)
    S.q("ga-ecoI-p5", "hard", "Consider the statements:\n1. The IIP measures changes in industrial production.\n2. The eight core industries include fertilisers and cement.\n3. The IIP is a price index.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is wrong — the **IIP is an output index**, not a price index; the WPI/CPI track prices.",
        "IIP = production, never prices.", 30)
    return S
