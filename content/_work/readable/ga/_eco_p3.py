"""Economy part 3: eco-taxes, eco-schemes, eco-institutions."""
from fractions import Fraction as F

from _eco_common import pat, mis, trick

# --- arithmetic used in examples -------------------------------------------------
assert 1000 * 18 // 100 == 180 and 180 // 2 == 90          # GST split example
assert F(1, 3) < F(3, 4) and F(2, 3) < F(3, 4)               # neither side passes a decision alone
assert F(1, 3) + F(2, 3) == 1
assert 6000 // 3 == 2000                                     # PM-KISAN instalment
assert 125 - 100 == 25                                       # RAM G extra days

SUBS = {}

# =====================================================================
SUBS["eco-taxes"] = dict(
    concept=(
        "A direct tax falls on the person who pays it, like income tax. An indirect tax is passed on to buyers, like GST. "
        "GST began on 1 July 2017, and GST 2.0 cut it to two main slabs, 5% and 18%, from 22 September 2025. "
        "The new Income-tax Act, 2025 replaced the 1961 Act from 1 April 2026."
    ),
    notes=r"""### Direct and indirect taxes
A direct tax is borne by the person who pays it. An indirect tax is paid to the government but passed on to buyers through prices.

| Type | Examples | Can the burden shift? |
|---|---|---|
| Direct | Income tax, corporate tax, capital gains tax, STT | No |
| Indirect | GST, customs duty, excise on petroleum and alcohol, stamp duty | Yes, to the consumer |

STT is the securities transaction tax. It is a direct tax.

Direct taxes are progressive: a higher income pays a higher rate. Indirect taxes are regressive, because rich and poor pay the same rate on a good. But they are easy to collect.

> **Example:** A shop adds GST to your bill. The shop pays it to the government, but you bear it. So GST is an indirect tax.

Corporation tax and personal income tax are the two biggest direct taxes. GST is the biggest indirect tax. **Agricultural income** is outside income tax, because taxing it is a state power.

### GST basics
GST (Goods and Services Tax) is one tax on goods and services. The **101st Constitutional Amendment Act, 2016** created it. It began on **1 July 2017**.

It is a **destination-based consumption tax**. The tax follows the place where the goods are consumed. GST took over excise, service tax, VAT, CST, entry tax and luxury tax.

| Article | What it covers |
|---|---|
| 246A | Power to make GST laws |
| 269A | GST on inter-state trade (IGST) and its sharing |
| 279A | The GST Council |

### Which GST applies
- A sale **within one state** carries CGST (to the Centre) plus SGST (to the state).
- A sale **between states**, and imports, carry **IGST**.
- The **GSTN** is the IT network that runs GST.

> **Example:** A ₹1,000 item taxed at 18% is sold within one state. CGST is ₹90 and SGST is ₹90. Total tax is ₹180.

### The GST Council
The **Union Finance Minister** chairs the Council. The other members are the Union Minister of State for Finance and the state finance ministers. The quorum is half the members.

Decisions need a **three-fourths weighted majority**. The Centre holds **one-third** of the votes. All states together hold **two-thirds**.

> **Rule:** Neither side can pass a decision alone. One-third and two-thirds are both below three-fourths.

### GST 2.0, the 2025 slab reform
The 56th Council meeting approved it on 3 September 2025. It took effect on **22 September 2025**.

| Slab | Used for |
|---|---|
| 5% | Merit goods |
| 18% | Standard rate |
| 40% | Demerit goods: tobacco, pan masala, some luxury items |

The **12% and 28% slabs were abolished**. Small cars, ACs and TVs moved to 18%. Unprocessed food, education and health stay exempt. Compensation cess ended, except on pan masala and tobacco products. Compensation to states under the GST law ran from July 2017 to June 2022.

### The new Income-tax Act
The **Income-tax Act, 2025** was passed in August 2025. It replaced the 1961 Act from **1 April 2026**. It has 536 sections in 23 chapters, in plainer language.

Its key change is one **tax year**. It replaces the old pair "previous year" and "assessment year". So income of FY 2026-27 is called Tax Year 2026-27.

Filing is still yearly. The default **new regime** has lower rates but few deductions. The older regime stays as an option. Under the new regime (Budget FY 2025-26), income up to ₹12 lakh pays no tax. For salaried people, the limit is ₹12.75 lakh with the standard deduction.

### Other tax facts
- **LTCG** (long-term capital gains) on equities is taxed at 12.5% above ₹1.25 lakh, since Budget 2024.
- STT was raised in Budget 2026.
- Share buybacks are taxed as capital gains for holders. Promoters also face a buyback tax.
- The **Finance Commission** (Article 280) decides how central taxes are shared with states.
- Cesses and surcharges are outside the shared pool, so states get no part of them.
""",
    tricks=[
        trick("GST article trio",
              "246A is the power to tax. 269A is inter-state GST. 279A is the Council. All came from the 101st Amendment, in force from 1 July 2017.",
              "Which article created the GST Council?",
              ["Recall the trio 246A, 269A, 279A.", "The last one is the Council.", "The 101st Amendment (2016) inserted it."],
              "Article 279A"),
        trick("GST 2.0 slab story",
              "Two working slabs: 5 (merit) and 18 (standard). 40 is kept for sin and luxury goods. 12% and 28% ended on 22 September 2025.",
              "What is the GST on a small car now?",
              ["Small cars were at 28% plus cess.", "The 28% slab was abolished.", "Small cars moved to the standard slab."],
              "18%"),
        trick("Tax-year switch",
              "Income-tax Act, 2025 works from 1 April 2026. One 'tax year' replaces the previous year and assessment year pair. 536 sections, 23 chapters.",
              "From which income year does the term 'Tax Year' apply?",
              ["The Act started on 1 April 2026.", "That is the start of FY 2026-27.", "So that year is Tax Year 2026-27."],
              "FY 2026-27 (Tax Year 2026-27)"),
    ],
    mistakes=[
        mis("Calling STT an indirect tax.", "STT is a direct tax on securities transactions."),
        mis("Thinking compensation cess still applies to all goods.", "It ended on 22 September 2025, except on pan masala and tobacco products."),
        mis("Saying the GST Council decides by a simple majority.", "It needs a three-fourths weighted majority. Centre has 1/3 of votes, states 2/3."),
        mis("Still listing a 12% or 28% GST slab.", "GST 2.0 kept 5% and 18%, plus a 40% demerit rate."),
        mis("Using IGST for a sale inside one state.", "Inside one state it is CGST + SGST. IGST is for inter-state sales and imports."),
        mis("Saying the Centre taxes agricultural income.", "Agricultural income is outside income tax. Taxing it is a state power."),
    ],
    revision=[
        "Direct: income, corporate, STT, capital gains. Indirect: GST, customs, excise (petroleum, alcohol), stamp duty.",
        "GST: 101st Amendment (2016), from 1 July 2017. Articles 246A, 269A, 279A.",
        "GST Council: Union FM chairs; 3/4 weighted majority; Centre 1/3, states 2/3.",
        "CGST + SGST inside a state. IGST between states and on imports. GSTN is the IT network.",
        "GST 2.0 from 22 September 2025: 5% and 18%, plus 40% demerit. 12% and 28% abolished.",
        "Income-tax Act, 2025 from 1 April 2026: one 'tax year'; 536 sections, 23 chapters.",
        "New regime: no tax up to ₹12 lakh (₹12.75 lakh for salaried).",
        "Agricultural income is not taxed by the Centre. Tax sharing goes through the Finance Commission (Article 280).",
    ],
    patterns=[
        pat("ga-ecoT-p1", "GST Council and constitutional articles", "very common",
            "'Article 279A deals with', 'who chairs the GST Council', or 'the Centre has what share of votes'.",
            ["Recall the articles: 246A power, 269A inter-state, 279A Council.",
             "The Union Finance Minister chairs the Council.",
             "Members add the Union MoS Finance and state finance ministers.",
             "Decisions need 3/4 of weighted votes: Centre 1/3, states 2/3."],
            "Three articles and one voting rule cover almost every Council question.",
            "Under which article of the Constitution is the GST Council constituted?",
            ["The 101st Amendment added three articles.", "246A and 269A deal with taxing power and inter-state trade.", "279A sets up the Council."],
            "Article 279A"),
        pat("ga-ecoT-p2", "GST launch and the 2025 slab reform", "very common",
            "'GST was introduced from', 'which amendment brought GST', or 'the GST slabs after September 2025 are'.",
            ["GST began on 1 July 2017.", "The 101st Constitutional Amendment Act, 2016 created it.",
             "GST 2.0 took effect on 22 September 2025.", "Slabs are now 5% and 18%, plus 40% for demerit goods."],
            "The launch date and the new slabs are fixed, often-asked facts.",
            "After the GST 2.0 reform of 22 September 2025, what are the two main GST slabs?",
            ["The 12% and 28% slabs were abolished.", "5% is for merit goods. 18% is the standard rate.", "40% is only for demerit goods."],
            "5% and 18% (with a separate 40% demerit rate)"),
        pat("ga-ecoT-p3", "Direct versus indirect tax", "common",
            "'Which is a direct tax', 'which tax cannot be shifted', or options mixing customs, corporate tax, GST and STT.",
            ["Ask: can the payer pass the tax on to a buyer?", "If not, it is direct: income, corporate, STT, capital gains.",
             "If yes, it is indirect: GST, customs, excise, stamp duty.", "STT is the usual trick option. It is direct."],
            "The burden test sorts every option in one pass.",
            "Which of the following is a direct tax? (a) GST (b) Customs duty (c) Corporate tax (d) Stamp duty",
            ["GST, customs and stamp duty are passed on to buyers.", "Corporate tax falls on company profits.", "The company cannot shift it."],
            "(c) Corporate tax"),
        pat("ga-ecoT-p4", "Income-tax Act 2025 and the tax year", "common",
            "'The new Income-tax Act is effective from', 'the tax year replaces', or 'how many sections does the new Act have'.",
            ["The Act was passed in August 2025.", "It works from 1 April 2026 and replaces the 1961 Act.",
             "One 'tax year' replaces previous year and assessment year.", "It has 536 sections in 23 chapters."],
            "A new law is a favourite current-affairs question.",
            "From which date did the Income-tax Act, 2025 come into force?",
            ["It replaced the Income-tax Act, 1961.", "It starts with a financial year.", "That year began on 1 April 2026."],
            "1 April 2026"),
        pat("ga-ecoT-p5", "Tax bases, exemption and devolution", "occasional",
            "'Agricultural income is taxed by', 'which tax gives the most direct-tax revenue', or 'how are taxes shared with states'.",
            ["Agricultural income is outside income tax. It is a state subject.",
             "Corporation tax and personal income tax lead direct taxes. GST leads indirect taxes.",
             "The Finance Commission (Article 280) shares central taxes with states.",
             "Cesses and surcharges are outside the shared pool."],
            "These are fixed statements that show up in true/false options.",
            "Which statement about agricultural income in India is correct?",
            ["Income tax is a central tax.", "Taxing agricultural income is a state power.", "So the Income-tax Act leaves it out."],
            "It is outside central income tax; only states can tax it"),
        pat("ga-ecoT-p6", "Which GST applies to a sale", "common",
            "'A sale from one state to another attracts', 'GST on imports is', or 'CGST and SGST are levied on'.",
            ["Check if buyer and seller are in the same state.", "Same state: CGST (Centre) + SGST (state).",
             "Different states, or an import: IGST.", "The GSTN only runs the IT system. It is not a tax."],
            "The place of sale alone decides the GST type.",
            "A trader in Gujarat sells goods to a buyer in Rajasthan. Which GST applies?",
            ["Seller and buyer are in different states.", "This is an inter-state sale.", "Inter-state sales carry IGST."],
            "IGST (Integrated GST)"),
        pat("ga-ecoT-p7", "Taxes merged into GST", "occasional",
            "'Which tax was not subsumed in GST', 'GST replaced which taxes', or 'which tax is still outside GST'.",
            ["GST took over excise, service tax, VAT, CST, entry tax and luxury tax.",
             "Customs duty is still outside GST.", "Excise on petroleum and alcohol continues.",
             "Pick the option that is still levied separately."],
            "Learn the merged list once and the odd one out is clear.",
            "Which of these taxes was NOT merged into GST? (a) Service tax (b) VAT (c) Customs duty (d) Entry tax",
            ["Service tax, VAT and entry tax were merged.", "Customs is charged on imports at the border.", "It is still a separate tax."],
            "(c) Customs duty"),
    ],
)

# =====================================================================
SUBS["eco-schemes"] = dict(
    concept=(
        "A scheme question tests four hooks: launch year, ministry, benefit and purpose. "
        "Learn each flagship scheme as one line with its number, such as ₹6,000 for PM-KISAN or ₹5 lakh for PM-JAY. "
        "The big recent change is VB-G RAM G, which replaced MGNREGA from 1 July 2026 with 125 days of work."
    ),
    notes=r"""### How to read a scheme question
Every scheme question asks one of four things: **launch year, ministry, benefit or purpose**. Learn one line per scheme. News brings new schemes each month, but these flagships appear in every paper.

> **Tip:** Match the number first. ₹6,000 a year means PM-KISAN. ₹5 lakh health cover means PM-JAY. 125 days means VB-G RAM G.

### Jobs and livelihoods
- **MGNREGA** (Act 2005, working from 2006): 100 days of wage work a year per rural household.
- **VB-G RAM G** replaced MGNREGA from **1 July 2026**, under a 2025 Act. The full name is Viksit Bharat - Guarantee for Rozgar and Ajeevika Mission (Gramin). The guarantee rose to **125 days**. Wages are paid weekly, not every 15 days.
- **DAY-NRLM** (2011): rural livelihoods through women's self-help groups (SHGs). **DAY-NULM** (2014) is the urban twin. Both sit under the Deendayal Antyodaya Yojana.
- **PM SVANidhi** (2020): working-capital loans for street vendors.
- **PM Vishwakarma** (2023): support for 18 traditional trades.
- **Namo Drone Didi** (2023) gives drones to women SHGs. **Lakhpati Didi** (2023) aims at ₹1 lakh+ yearly income for them.

### Bank accounts, loans and insurance
| Scheme | Launch | Key fact |
|---|---|---|
| PM Jan Dhan Yojana | 28 Aug 2014 | Zero-balance accounts, RuPay card, overdraft |
| MUDRA Yojana | 8 Apr 2015 | Loans without collateral |
| Atal Pension Yojana | 2015 | Pension for unorganised workers aged 18-40 |
| Sukanya Samriddhi | 2015 | Savings for the girl child |
| PMSBY | - | Accident cover of ₹2 lakh for ₹20 a year |
| PMJJBY | - | Life insurance cover |

Jan Dhan is the world's largest financial-inclusion drive. PMSBY and PMJJBY are the two Jan Suraksha insurance schemes.

MUDRA loans come in tiers: **Shishu** up to ₹50,000, **Kishor** ₹50,000-5 lakh and **Tarun** ₹5-10 lakh. **Tarun Plus** goes up to ₹20 lakh since October 2024.

### Farmers and villages
- **PM-KISAN** (February 2019): **₹6,000 a year** to landholding farmer families, in three direct transfers. The Agriculture Ministry runs it.
- **PM Fasal Bima Yojana** (2016): low-cost crop insurance.
- **e-NAM** (2016): one online market linking mandis.
- **Kisan Credit Card** (1998): short-term crop loans.
- **PM-KUSUM**: solar pumps for farmers.

> **Example:** ₹6,000 in three equal parts is ₹2,000 per instalment.

### Health, water, housing and fuel
| Scheme | Launch | Key fact |
|---|---|---|
| Ayushman Bharat PM-JAY | 23 Sep 2018 | ₹5 lakh cover per family a year for hospital care |
| Ayushman Bharat Digital Mission | Sep 2021 | Digital health stack; ABHA health ID |
| Jal Jeevan Mission | Aug 2019 | "Har Ghar Jal": tap water to every home |
| Swachh Bharat Mission | 2 Oct 2014 | Toilets; open-defecation-free goal |
| POSHAN Abhiyaan | 2018 | Nutrition, under the WCD Ministry |
| PM Awas Yojana | 2015 urban, 2016 rural | Pucca houses |
| PM Ujjwala Yojana | 1 May 2016 | Free LPG connections to poor women |
| Beti Bachao Beti Padhao | 2015 | Girl child; launched at Panipat |

Since 2024, **Vay Vandana** extends PM-JAY to everyone aged 70 and above.

### Industry, skills and energy
- **Make in India** (25 September 2014): manufacturing push.
- **Skill India / PMKVY** (2015): job skills.
- **Startup India** (16 January 2016): DPIIT recognition and tax holidays for startups.
- **UDAN** (2016): regional air links.
- **PLI schemes** (2020): production-linked incentives in 14 sectors.
- **PM Gati Shakti** (October 2021): national infrastructure master plan.
- **PM Surya Ghar Muft Bijli** (2024): rooftop solar, up to 300 free units a month.

### Which ministry runs it
| Ministry | Schemes |
|---|---|
| Housing and Urban Affairs | PMAY-Urban, DAY-NULM, PM SVANidhi |
| Rural Development | MGNREGA line, DAY-NRLM |
| Women and Child Development | POSHAN Abhiyaan |
| Civil Aviation | UDAN |
| Jal Shakti | Jal Jeevan Mission |

> **Watch:** Beti Bachao Beti Padhao is a joint scheme of three ministries, not one.

### New in Budget 2026-27
The Budget of 1 February 2026 added these:
- **Biopharma SHAKTI**: ₹10,000 crore.
- **SME Growth Fund**: ₹10,000 crore.
- Semiconductor Mission 2.0 and an Infrastructure Risk Guarantee Fund.
- City Economic Regions.
- A five-part textile programme, including Samarth 2.0.
- Rare Earth corridors in Odisha, Kerala, Andhra Pradesh and Tamil Nadu.
""",
    tricks=[
        trick("Launch-year clusters",
              "2014: Jan Dhan, Make in India, Swachh Bharat. 2015: BBBP, APY, MUDRA, PMAY. 2016: Ujjwala, Startup India. 2018: Ayushman. 2019: PM-KISAN. 2020: SVANidhi, PLI. 2023: Vishwakarma, Drone Didi. 2024: Surya Ghar. 2026: VB-G RAM G.",
              "Which scheme gives ₹6,000 a year to farmers?",
              ["₹6,000 is the PM-KISAN number.", "It started in 2019.", "The Agriculture Ministry runs it."],
              "PM-KISAN"),
        trick("MGNREGA to RAM G swap",
              "100 days became 125. Wages every 15 days became weekly. Act of 2025, in force from 1 July 2026.",
              "From when does VB-G RAM G apply?",
              ["It was passed as an Act in 2025.", "It replaced MGNREGA.", "It came into force in mid-2026."],
              "1 July 2026"),
        trick("MUDRA ladder",
              "Shishu up to ₹50,000. Kishor ₹50,000-5 lakh. Tarun ₹5-10 lakh. Tarun Plus up to ₹20 lakh. The names go from child to young adult.",
              "A MUDRA loan of ₹3 lakh falls in which tier?",
              ["Shishu ends at ₹50,000.", "Kishor covers ₹50,000 to ₹5 lakh.", "₹3 lakh lies in that range."],
              "Kishor"),
    ],
    mistakes=[
        mis("Naming one ministry for Beti Bachao Beti Padhao.", "BBBP is a joint scheme of three ministries."),
        mis("Stopping MUDRA at ₹10 lakh.", "Tarun Plus goes up to ₹20 lakh since October 2024."),
        mis("Saying MGNREGA still gives 100 days.", "VB-G RAM G replaced it from 1 July 2026, with 125 days."),
        mis("Mixing up PMSBY and PMJJBY.", "PMSBY is accident cover (₹20 a year). PMJJBY is life cover."),
        mis("Giving PM-JAY cover per person.", "PM-JAY gives ₹5 lakh per family a year."),
        mis("Putting Jal Jeevan Mission under Swachh Bharat.", "JJM (2019) is tap water. SBM (2014) is sanitation."),
    ],
    revision=[
        "VB-G RAM G (1 July 2026): 125 days, weekly wages; replaced MGNREGA (100 days).",
        "Jan Dhan 28-8-2014. MUDRA 8-4-2015: Shishu, Kishor, Tarun, Tarun Plus (₹20 lakh).",
        "APY: ages 18-40. PMSBY: ₹2 lakh accident cover for ₹20 a year. PMJJBY: life cover.",
        "PM-KISAN (2019): ₹6,000 a year in 3 instalments. Fasal Bima 2016. e-NAM 2016. KCC 1998.",
        "PM-JAY (2018): ₹5 lakh per family; Vay Vandana covers all 70+.",
        "JJM 2019. SBM 2-10-2014. Ujjwala 1-5-2016. PMAY 2015 urban, 2016 rural.",
        "Make in India 25-9-2014. Startup India 16-1-2016. PLI 2020 (14 sectors). Gati Shakti 2021.",
        "Vishwakarma 2023 (18 trades). Surya Ghar 2024 (300 free units a month).",
    ],
    patterns=[
        pat("ga-ecoS-p1", "Scheme, ministry and launch year", "very common",
            "'X was launched in which year', 'which ministry runs X', or a list of schemes with 2014-2021 dates.",
            ["Fix the year first: SBM and Jan Dhan 2014, MUDRA 2015, Startup India 2016.",
             "Then JJM and PM-KISAN 2019, Gati Shakti 2021.",
             "Get the ministry from the subject: urban schemes are MoHUA, rural jobs are Rural Development.",
             "POSHAN is WCD. UDAN is Civil Aviation."],
            "The year narrows the options. The subject gives the ministry.",
            "In which year was Startup India launched?",
            ["Startup India gives DPIIT recognition and tax holidays.", "It came after Make in India (2014).", "It was launched on 16 January 2016."],
            "2016 (16 January)"),
        pat("ga-ecoS-p2", "Scheme and its benefit", "very common",
            "A rupee amount, an age band or a cover figure is given. The scheme is asked.",
            ["Spot the number in the question.", "₹6,000 a year: PM-KISAN. ₹5 lakh per family: PM-JAY.",
             "Ages 18-40: Atal Pension Yojana.", "₹20 a year for accident cover: PMSBY."],
            "Each flagship has one signature number.",
            "Under which scheme do landholding farmer families get ₹6,000 a year?",
            ["₹6,000 is the signature number.", "It is paid in three instalments by direct transfer.", "The scheme started in 2019."],
            "PM-KISAN"),
        pat("ga-ecoS-p3", "Employment and livelihood schemes", "common",
            "'How many days of work does X guarantee', 'which scheme replaced MGNREGA', or SHG and street-vendor schemes.",
            ["MGNREGA gave 100 days (Act 2005).", "VB-G RAM G replaced it from 1 July 2026 with 125 days and weekly wages.",
             "DAY-NRLM (2011) works through women's SHGs. DAY-NULM (2014) is urban.",
             "PM SVANidhi (2020) is for street vendors."],
            "The job-guarantee change is the newest and most asked fact.",
            "Which scheme replaced MGNREGA from 1 July 2026?",
            ["It came from a 2025 Act.", "It raised the guarantee to 125 days a year.", "Wages are now paid weekly."],
            "VB-G RAM G"),
        pat("ga-ecoS-p4", "Financial inclusion schemes", "common",
            "'Zero-balance accounts under', 'Shishu, Kishor and Tarun belong to', or 'accident cover for ₹20 a year'.",
            ["Jan Dhan (28 August 2014): accounts, RuPay card, overdraft.",
             "MUDRA (8 April 2015): Shishu up to ₹50,000, Kishor to ₹5 lakh, Tarun to ₹10 lakh.",
             "Tarun Plus goes up to ₹20 lakh (October 2024).",
             "APY is pension. PMSBY is accident cover. PMJJBY is life cover."],
            "Each scheme covers one money need: account, loan, pension or insurance.",
            "The loan categories Shishu, Kishor and Tarun belong to which scheme?",
            ["These are loan sizes for small businesses.", "The loans need no collateral.", "They come under the 2015 scheme for micro units."],
            "Pradhan Mantri MUDRA Yojana"),
        pat("ga-ecoS-p5", "Health, water, housing and fuel schemes", "very common",
            "'Har Ghar Jal belongs to', 'the free LPG scheme is', or '₹5 lakh hospital cover'.",
            ["Health: PM-JAY (2018), ₹5 lakh per family. ABDM (2021) gives ABHA IDs.",
             "Water: JJM (2019). Sanitation: SBM (2 October 2014).",
             "Housing: PMAY (2015 urban, 2016 rural).", "Fuel: Ujjwala (1 May 2016), LPG for poor women."],
            "Each need maps to one mission.",
            "'Har Ghar Jal', a tap connection for every rural home, is the goal of which mission?",
            ["The need is drinking water at home.", "The mission began in August 2019.", "The Jal Shakti ministry runs it."],
            "Jal Jeevan Mission"),
        pat("ga-ecoS-p6", "Industry, skills and energy schemes", "common",
            "'Make in India was launched on', 'PLI schemes cover how many sectors', 'Gati Shakti is', or 'rooftop solar scheme'.",
            ["Make in India: 25 September 2014.", "Skill India / PMKVY: 2015. UDAN: 2016.",
             "PLI (2020) covers 14 sectors. Gati Shakti (October 2021) is the infrastructure master plan.",
             "PM Surya Ghar (2024): rooftop solar, up to 300 free units a month."],
            "These schemes are asked with one number or one purpose.",
            "The Production-Linked Incentive (PLI) schemes of 2020 cover how many sectors?",
            ["PLI pays incentives for extra production.", "It was launched in 2020.", "It covers 14 sectors."],
            "14"),
        pat("ga-ecoS-p7", "Farm and rural schemes", "common",
            "'Kisan Credit Card was introduced in', 'e-NAM is', or 'PM-KUSUM provides'.",
            ["PM-KISAN (2019): ₹6,000 a year.", "Fasal Bima (2016): crop insurance. e-NAM (2016): online mandi.",
             "KCC (1998): short-term crop loans.", "PM-KUSUM: solar pumps."],
            "Farm schemes differ by one purpose: cash, insurance, market, credit or power.",
            "e-NAM, launched in 2016, is best described as what?",
            ["NAM stands for National Agriculture Market.", "The 'e' means it is online.", "It links mandis on one platform."],
            "A unified online market for farm produce"),
    ],
)

# =====================================================================
SUBS["eco-institutions"] = dict(
    concept=(
        "Each financial market in India has one regulator: SEBI for shares, IRDAI for insurance, PFRDA for pensions and the RBI for banks. "
        "Development banks such as NABARD and SIDBI refinance rural and small-industry loans. "
        "Global bodies are asked with their year, headquarters and head."
    ),
    notes=r"""### Financial regulators
Each regulator watches one market. Learn the market, the year and the HQ together.

| Regulator | Watches | Set up | HQ |
|---|---|---|---|
| RBI | Banks, NBFCs, payments | 1935; nationalised 1949 | Mumbai |
| SEBI | Securities market | 1988; SEBI Act 1992 | Mumbai |
| IRDAI | Insurance | IRDA Act 1999 | Hyderabad |
| PFRDA | Pensions (NPS, APY) | Interim 2003; PFRDA Act 2013 | New Delhi |

SEBI became a statutory body after the Harshad Mehta episode. **RERA** (2016) regulates real estate.

The RBI Governor is **Sanjay Malhotra**. The SEBI chief is **Tuhin Kanta Pandey**, since March 2025.

> **Tip:** Stockbroker or mutual fund means SEBI. Policyholder means IRDAI. NPS means PFRDA.

### Development finance institutions
These banks lend to other lenders. This is called refinance.

- **NABARD** (**12 July 1982**): apex bank for rural credit. It came on the Shivaraman Committee's advice. It took over the RBI's farm refinance work. It refinances RRBs and co-operative banks. HQ Mumbai. The Government of India owns it.
- **SIDBI** (1990): refinance for small industries (MSMEs). HQ **Lucknow**. It is also the fund manager for MUDRA.
- **EXIM Bank** (1982): trade finance. HQ Mumbai.
- **NHB** (1988): housing finance. HQ New Delhi.

> **Watch:** Lucknow (SIDBI) and Hyderabad (IRDAI) are the two surprise HQs. Most others are in Mumbai.

### Stock exchanges and indices
The **BSE** (1875) is **Asia's oldest stock exchange**. It began as the Native Share and Stock Brokers' Association. Its index is the **Sensex, with 30 stocks**.

The **NSE** was set up in 1992 and began trading in 1994. It brought screen-based trading. Its index is the **Nifty 50**.

Both indices are free-float market-cap weighted. Shares are held in electronic form by two depositories, **NSDL and CDSL**.

### Payments and coordination
- **NPCI** (2008) runs India's retail payment rails: **UPI** (2016), RuPay, IMPS, FASTag and NACH.
- **FSDC** (Financial Stability and Development Council, 2010) coordinates all regulators. The Union Finance Minister chairs it.

### Bretton Woods and trade bodies
The IMF and the World Bank were both born at the **Bretton Woods conference in 1944**. Both sit in **Washington DC**.

| Body | Year | HQ | Role and head |
|---|---|---|---|
| IMF | 1944 | Washington DC | Balance-of-payments help, quotas, SDRs; MD Kristalina Georgieva |
| World Bank | 1944 (IBRD 1945) | Washington DC | IBRD + IDA, long-term loans; President Ajay Banga (since June 2023) |
| WTO | 1995 | Geneva | Trade rules; replaced GATT (1947); DG Ngozi Okonjo-Iweala |
| OECD | 1961 | Paris | India is not a member |
| FATF | 1989 | Paris | Money-laundering watchdog; India a member since 2010 |

IMF reports: World Economic Outlook and Global Financial Stability Report. The World Bank publishes the World Development Report. India is a founding member of the WTO.

### Asian and BRICS banks
| Bank | Year | HQ | Key fact |
|---|---|---|---|
| ADB | 1966 | Manila | President Masato Kanda (2025) |
| AIIB | 2016 | Beijing | India is the second-largest shareholder |
| NDB (BRICS bank) | 2015 | Shanghai | First president K.V. Kamath |

India is a founding member of all three.

> **Example:** "BRICS bank" in a question means NDB. Its HQ is Shanghai, not Beijing.
""",
    tricks=[
        trick("Regulator HQ pairs",
              "RBI, SEBI and NABARD are in Mumbai. IRDAI is in Hyderabad. SIDBI is in Lucknow. PFRDA is in New Delhi.",
              "Where is SIDBI headquartered?",
              ["SIDBI is the small-industry bank.", "It was set up in 1990.", "Its HQ is the surprise one."],
              "Lucknow"),
        trick("Bretton Woods twins",
              "IMF and World Bank: both 1944, both Washington DC. WTO: 1995, Geneva, replaced GATT (1947).",
              "Where is the WTO headquartered?",
              ["The WTO is not a Bretton Woods twin.", "It came in 1995 after GATT.", "Its HQ is in Switzerland."],
              "Geneva"),
        trick("Asian banks map",
              "ADB 1966 in Manila. AIIB 2016 in Beijing. NDB (BRICS) 2015 in Shanghai. India is a founding member of all three.",
              "Where is the New Development Bank headquartered?",
              ["NDB is the BRICS bank.", "It was set up in 2015.", "Its HQ is in China, but not Beijing."],
              "Shanghai"),
    ],
    mistakes=[
        mis("Placing SEBI in New Delhi.", "SEBI is in Mumbai. PFRDA is the one in New Delhi."),
        mis("Saying India is an OECD member.", "India is not a member. It works with the OECD as a Key Partner."),
        mis("Assuming the IMF chief must be a European.", "That is a tradition, not a rule. Kristalina Georgieva (Bulgaria) is the MD."),
        mis("Putting the NDB in Beijing.", "The NDB is in Shanghai. The AIIB is in Beijing."),
        mis("Calling the NSE Asia's oldest exchange.", "The BSE (1875) is the oldest. The NSE came in 1992."),
        mis("Placing SIDBI in Mumbai with the other banks.", "SIDBI is in Lucknow. NABARD and EXIM Bank are in Mumbai."),
    ],
    revision=[
        "SEBI: 1988, Act 1992, Mumbai. IRDAI: 1999 Act, Hyderabad. PFRDA: 2013 Act, New Delhi (NPS).",
        "NABARD 12-7-1982 (Shivaraman). SIDBI 1990, Lucknow. EXIM 1982. NHB 1988.",
        "BSE 1875, Asia's oldest, Sensex 30. NSE 1992 (trading 1994), Nifty 50.",
        "NPCI 2008 runs UPI (2016), RuPay, IMPS, FASTag. FSDC 2010, chaired by the FM.",
        "IMF and World Bank: 1944, Washington DC. WTO: 1995, Geneva.",
        "ADB 1966 Manila. AIIB 2016 Beijing. NDB 2015 Shanghai (BRICS).",
        "FATF 1989 Paris (India since 2010). OECD 1961 Paris (India not a member).",
        "Heads: Malhotra (RBI), Pandey (SEBI), Georgieva (IMF), Banga (World Bank), Okonjo-Iweala (WTO).",
    ],
    patterns=[
        pat("ga-ecoN-p1", "Regulator and its sector", "very common",
            "'SEBI regulates', 'the insurance regulator is', or 'who regulates the NPS'.",
            ["SEBI: securities. IRDAI: insurance.", "PFRDA: pensions (NPS, APY). RBI: banks, NBFCs, payments.",
             "Recall the laws: SEBI Act 1992, IRDA Act 1999, PFRDA Act 2013.",
             "Stockbroker or mutual fund means SEBI. Policyholder means IRDAI."],
            "Each market has exactly one regulator.",
            "Who regulates the securities market in India?",
            ["Securities means shares, bonds and mutual funds.", "SEBI was set up in 1988.", "The SEBI Act, 1992 made it statutory."],
            "SEBI"),
        pat("ga-ecoN-p2", "Institution and headquarters", "common",
            "'SIDBI is headquartered at', 'IRDAI is based in', or a city-matching list.",
            ["Mumbai: RBI, SEBI, NABARD, EXIM Bank.", "Lucknow: SIDBI. Hyderabad: IRDAI. New Delhi: NHB, PFRDA.",
             "Abroad: IMF and World Bank in Washington, WTO in Geneva.",
             "ADB Manila, AIIB Beijing, NDB Shanghai, FATF Paris."],
            "Most Indian bodies sit in Mumbai, so the odd ones get asked.",
            "Where is the Small Industries Development Bank of India (SIDBI) headquartered?",
            ["SIDBI refinances small industries.", "It was set up in 1990.", "It is not in Mumbai."],
            "Lucknow"),
        pat("ga-ecoN-p3", "Year and founding event", "common",
            "'NABARD was set up in', 'Asia's oldest stock exchange', or a year-matching list.",
            ["India: BSE 1875, NABARD 1982, EXIM 1982, NHB 1988, SIDBI 1990.",
             "Then NSE 1992 (trading 1994), NPCI 2008.",
             "Global: IMF and World Bank 1944, ADB 1966, WTO 1995, NDB 2015, AIIB 2016."],
            "Order the years once and each match is quick.",
            "Which is Asia's oldest stock exchange?",
            ["The NSE came only in 1992.", "The BSE dates from 1875.", "It began as the Native Share and Stock Brokers' Association."],
            "The BSE (Bombay Stock Exchange)"),
        pat("ga-ecoN-p4", "Multilateral banks and funds", "common",
            "'The New Development Bank is headquartered at', 'which bank belongs to BRICS', or 'the ADB was set up in'.",
            ["NDB (2015, Shanghai) is the BRICS bank. K.V. Kamath was its first president.",
             "AIIB (2016, Beijing): India is the second-largest shareholder.",
             "ADB (1966, Manila).",
             "IMF gives balance-of-payments help. The World Bank gives long-term development loans."],
            "Each bank has one owner group and one city.",
            "The New Development Bank, set up by BRICS in 2015, is headquartered where?",
            ["NDB is the BRICS bank.", "The AIIB is the one in Beijing.", "The NDB is in Shanghai."],
            "Shanghai"),
        pat("ga-ecoN-p5", "Indices, exchanges and payment systems", "common",
            "'The Sensex has how many stocks', 'Nifty belongs to', or 'UPI is run by'.",
            ["Sensex: 30 stocks, BSE. Nifty 50: NSE.", "NPCI (2008) runs UPI, RuPay, IMPS, FASTag and NACH.",
             "UPI went live in 2016.", "NSDL and CDSL are depositories, not exchanges."],
            "Match each product to the body that runs it.",
            "UPI is built and run by which body?",
            ["UPI is a payment system.", "India's retail payment systems sit under one body.", "That body was set up in 2008."],
            "NPCI (National Payments Corporation of India)"),
        pat("ga-ecoN-p6", "Heads of institutions", "very common",
            "'Who is the current Managing Director of the IMF', 'the President of the World Bank is', or 'the SEBI chairperson is'.",
            ["RBI: Governor Sanjay Malhotra. SEBI: Tuhin Kanta Pandey (since March 2025).",
             "IMF: MD Kristalina Georgieva. World Bank: President Ajay Banga (since June 2023).",
             "WTO: DG Ngozi Okonjo-Iweala. ADB: President Masato Kanda (2025).",
             "Mind the title: Governor, Chairperson, MD, President or DG."],
            "Heads change, so exams ask for the current name.",
            "Who is the President of the World Bank?",
            ["The World Bank's chief is called President.", "He took office in June 2023.", "He is Ajay Banga."],
            "Ajay Banga"),
        pat("ga-ecoN-p7", "Membership, reports and roles", "occasional",
            "'India is not a member of', 'the World Economic Outlook is published by', or 'FATF deals with'.",
            ["India is not an OECD member.", "India joined FATF in 2010. FATF fights money laundering.",
             "IMF: World Economic Outlook, Global Financial Stability Report.",
             "World Bank: World Development Report. FSDC is chaired by the Finance Minister."],
            "These statement-type facts are short and fixed.",
            "The World Economic Outlook report is published by which body?",
            ["It reviews the global economy.", "The IMF also publishes the Global Financial Stability Report.", "Both are IMF reports."],
            "The International Monetary Fund (IMF)"),
    ],
)
