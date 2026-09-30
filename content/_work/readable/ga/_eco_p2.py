"""Economy part 2: eco-rbi, eco-inflation, eco-budget."""
from _eco_common import pat, mis, trick

assert 5.25 - 0.25 == 5.00 and 5.25 + 0.25 == 5.50
assert 6.00 + 0.25 == 6.25
assert 6 - 2.5 == 3.5
assert 45 - 39 == 6
assert 40 - 33 == 7
assert 6 - 2 == 4

SUBS = {}

# =====================================================================
SUBS["eco-rbi"] = dict(
    concept=(
        "The RBI is India's central bank. It issues currency, keeps the banks' reserves and sets the policy rates. "
        "A six-member Monetary Policy Committee decides the repo rate to keep CPI inflation at 4%, with a band of 2% either side. "
        "Most questions test dates, rate positions and the ratios CRR and SLR."
    ),
    notes=r"""### The RBI in brief
The RBI Act, 1934 created the bank. It began work on **1 April 1935**. It was **nationalised on 1 January 1949**. Its head office is in **Mumbai**.

The RBI issues all currency except the **₹1 note and coins**. The Finance Ministry issues those. The RBI is also banker to the government and banker to banks. It is the **lender of last resort**. It keeps the country's forex reserves.

The Governor is **Sanjay Malhotra**, the 26th Governor, since December 2024.

### The rate corridor
The **repo rate** is the rate at which the RBI lends short-term to banks. It is the main policy rate. Two rates sit around it.

| Rate | Position | Level (after 5 Aug 2026 MPC) |
|---|---|---|
| MSF and Bank Rate | Repo + 0.25 (ceiling) | 5.50% |
| Repo | Middle | 5.25% |
| SDF | Repo - 0.25 (floor) | 5.00% |

The MPC held rates unchanged in August 2026 with a neutral stance. The reverse repo is 3.35%, but it is dormant as an operative rate since the SDF began in 2022.

> **Rule:** SDF is the floor and MSF is the ceiling. Bank Rate equals MSF.

SDF lets banks park spare cash with the RBI without collateral. MSF lets banks borrow overnight, even beyond their SLR holdings.

### CRR, SLR and liquidity
- **CRR:** the share of deposits a bank keeps as **cash with the RBI**. It earns no interest. It is now **3.00%**, cut from 4% in four steps in Sep-Nov 2025.
- **SLR:** the share of deposits a bank keeps in liquid assets such as government securities and gold, held by the bank itself. It is **18%**.
- **OMOs:** the RBI buys or sells government securities. Buying adds liquidity.

> **Tip:** Cutting CRR or repo makes money cheaper and adds liquidity. Raising them controls inflation.

### The Monetary Policy Committee
The RBI (Amendment) Act, 2016 set up the MPC. It has **six members**: three from the RBI, including the Governor, and three named by the government. The Governor has the **casting vote**.

It meets at least four times a year. The target is **CPI inflation of 4% with a 2% band on each side**. Missing the band for three straight quarters means a report to the government. The target uses CPI, not WPI.

### Money supply
| Measure | Contents |
|---|---|
| M1 (narrow money) | Currency with the public + demand deposits + other RBI deposits |
| M2 | M1 + post-office savings |
| M3 (broad money) | M1 + time deposits |
| M4 | M3 + post-office deposits (not NSCs) |

### Banking milestones
| Year | Event |
|---|---|
| 1955 | SBI formed from the Imperial Bank |
| 1969 | 14 banks nationalised (19 July) |
| 1975 | Regional Rural Banks begin |
| 1980 | 6 more banks nationalised (15 April) |
| 1991, 1998 | Narasimham Committees I and II |
| 2008 | NPCI set up (UPI came in 2016) |
| 2014 | Nachiket Mor Committee |

DICGC insures deposits up to **₹5 lakh** per depositor per bank. Payment banks take deposits but cannot lend.
""",
    tricks=[
        trick("Corridor arithmetic",
              "Repo is the middle. The floor (SDF) is repo minus 0.25. The ceiling (MSF and Bank Rate) is repo plus 0.25.",
              "If repo were 6.00%, what would the MSF be?",
              ["MSF is the ceiling.", "Ceiling = repo + 0.25.", "6.00 + 0.25 = 6.25."],
              "6.25%"),
        trick("Nationalisation anchors",
              "1935 RBI born, 1949 RBI nationalised, 1955 SBI, 1969 fourteen banks, 1975 RRBs, 1980 six banks.",
              "How many banks were nationalised in 1980?",
              ["The 1969 round had 14 banks.", "The 1980 round was smaller.", "It covered banks with deposits of ₹200 crore or more."],
              "Six"),
        trick("MPC fixed points",
              "Six members. At least four meetings a year. Target CPI 4% with a 2% band. The Governor has the casting vote.",
              "Who has the casting vote in the MPC?",
              ["The MPC has an even number of members.", "A tie needs a tie-breaker.", "The RBI Governor holds it."],
              "The RBI Governor"),
    ],
    mistakes=[
        mis("Repeating old rates such as repo 6.5% and CRR 4%.", "After the 5 Aug 2026 MPC, repo is 5.25% and CRR is 3%."),
        mis("Mixing up reverse repo (3.35%, dormant) and SDF (5.00%).", "SDF is the operative floor of the corridor."),
        mis("Crediting the Nachiket Mor Committee with the 1990s reforms.", "Those were Narasimham I and II. Nachiket Mor (2014) is about inclusion and payment banks."),
        mis("Calling CRR and SLR 'policy rates'.", "They are ratios. The policy rate is the repo rate."),
        mis("Saying the RBI issues the ₹1 note.", "The Finance Ministry issues the ₹1 note and coins."),
    ],
    revision=[
        "RBI Act 1934. Started 1 April 1935. Nationalised 1 January 1949. HQ Mumbai.",
        "Finance Ministry issues the ₹1 note and coins. RBI issues the rest.",
        "SDF = repo - 0.25 (floor). MSF = Bank Rate = repo + 0.25 (ceiling).",
        "CRR = cash with the RBI. SLR = liquid assets held by the bank.",
        "MPC: 6 members, Governor's casting vote, CPI 4% with a 2% band.",
        "M1 is narrow money. M3 = M1 + time deposits.",
        "1955 SBI, 1969 (14), 1975 RRBs, 1980 (6). DICGC cover ₹5 lakh.",
    ],
    patterns=[
        pat("ga-ecoR-p1", "RBI identity, history and currency", "very common",
            "'The RBI was set up under which Act', 'when was it nationalised', 'which note does the RBI not issue', or 'where is its HQ'.",
            ["Recall the dates: Act 1934, start 1 April 1935, nationalised 1 January 1949.", "HQ is Mumbai.", "The ₹1 note and coins come from the Finance Ministry.", "The RBI is the bankers' bank and lender of last resort."],
            "These few facts repeat in almost every paper.",
            "The one-rupee note in India is issued by whom?",
            ["The RBI issues other notes.", "The ₹1 note is an exception.", "The Finance Ministry issues it."],
            "The Government of India (Finance Ministry)"),
        pat("ga-ecoR-p2", "Policy rates and the corridor", "very common",
            "'SDF is how much below repo', 'the Bank Rate equals', or 'which rate is the policy rate'.",
            ["Place repo in the middle.", "SDF is repo - 0.25 (floor).", "MSF and Bank Rate are repo + 0.25 (ceiling).", "Do not call CRR or SLR a rate of the corridor."],
            "Positions stay fixed even when the numbers change.",
            "The Standing Deposit Facility (SDF) is placed how far from the repo rate?",
            ["SDF is the floor of the corridor.", "Banks park surplus cash there without collateral.", "It sits 25 basis points below repo."],
            "25 basis points below repo"),
        pat("ga-ecoR-p3", "MPC and the inflation target", "very common",
            "'How many members sit on the MPC', 'who holds the casting vote', or 'what is the inflation target'.",
            ["The MPC has 6 members: 3 from the RBI and 3 outsiders.", "The Governor has the casting vote.", "Target is CPI 4% with a 2% band.", "Three straight quarters outside the band trigger a report."],
            "The MPC facts are a short fixed list from the 2016 Act.",
            "Who holds the casting vote in the Monetary Policy Committee?",
            ["There are six members.", "A 3-3 split needs a tie-breaker.", "The Governor breaks the tie."],
            "The RBI Governor"),
        pat("ga-ecoR-p4", "CRR, SLR and liquidity tools", "common",
            "'CRR is kept with', 'SLR consists of', or 'which tool adds liquidity at once'.",
            ["CRR means cash with the RBI. It earns nothing.", "SLR means the bank's own liquid assets.", "A CRR or repo cut adds liquidity. A rise removes it.", "Buying securities in OMO adds liquidity."],
            "Every tool moves liquidity in one direction, so learn the direction.",
            "The Cash Reserve Ratio (CRR) requires banks to keep what?",
            ["CRR is a share of deposits.", "It is held as cash.", "The cash sits with the RBI and earns no interest."],
            "A fixed share of their deposits as cash with the RBI"),
        pat("ga-ecoR-p5", "Money supply and banking milestones", "common",
            "'M1 consists of', 'which is the broad money measure', '14 banks were nationalised in', or DICGC and NPCI facts.",
            ["M1 = currency + demand deposits + other RBI deposits.", "M3 = M1 + time deposits.", "Recall the years: 1955, 1969 (14), 1975, 1980 (6).", "Recall DICGC ₹5 lakh and NPCI 2008."],
            "Each measure adds one item to the last.",
            "Which item is included in M1 but not in M3?",
            ["M3 is M1 plus time deposits.", "So every M1 item is also in M3.", "The correct answer is that there is no such item."],
            "None. M3 contains all of M1."),
    ],
)

# =====================================================================
SUBS["eco-inflation"] = dict(
    concept=(
        "Inflation is a sustained rise in the general price level. It comes from higher demand or higher costs. "
        "CPI measures retail prices and the RBI targets it. WPI measures wholesale goods and is compiled by the Office of Economic Adviser."
    ),
    notes=r"""### Types of inflation
Inflation means prices keep rising. The same ₹100 buys less over time.

| Type | Cause or meaning |
|---|---|
| Demand-pull | Too much demand chasing goods (cheap credit, tax cuts) |
| Cost-push | Costlier inputs such as oil, fertiliser, wages |
| Stagflation | High inflation with stagnant growth |
| Disinflation | Inflation still positive but slowing |
| Deflation | Prices falling |
| Hyperinflation | Runaway triple-digit monthly rise |

> **Tip:** Ask one question. Did demand rise, or did costs rise?

### Headline and core
**Headline inflation** covers all items. **Core inflation** is headline minus food and fuel. Core shows the steadier, underlying trend.

Food has the largest weight in the CPI basket. A monsoon shock moves headline sharply while core stays steadier.

### The main price indices
| Index | Agency | Base |
|---|---|---|
| CPI (Combined) | NSO, MoSPI | 2024 (new series Feb 2026); old 2012 |
| WPI | Office of Economic Adviser, DPIIT | 2022-23 (Jun 2026); old 2011-12 |
| CPI-IW | Labour Bureau | Used for dearness allowance |
| CPI-AL, CPI-RL | Labour Bureau | Farm and rural labourers |
| IIP | NSO | 2022-23 from 1 Jun 2026; old 2011-12 |

IIP measures industrial output, not prices.

### CPI versus WPI
- **CPI** measures retail prices. It includes services.
- **WPI** measures wholesale or producer prices. It covers goods only. It has no services.

The 2026 WPI revision raised the basket from **697 to 957 items**. It also introduced Producer Price Indices (PPI).

> **Watch:** The RBI targets CPI, not WPI. The target is 4% with a 2% band.

### Inflation targeting
The RBI Act was amended in **2016**. The MPC now aims at **CPI inflation of 4% plus or minus 2%**. The RBI has failed if inflation stays outside the band for **three consecutive quarters**.

### Small facts
- CPI-IW drives dearness allowance for central employees.
- The food part of CPI is called CFPI.
- WPI fuel and power and manufactured products are the volatile groups.
- The Eight Core Industries index feeds the IIP. The eight are coal, crude oil, natural gas, refinery products, fertilisers, steel, cement and electricity.
- The GDP deflator is nominal GDP divided by real GDP, times 100.
""",
    tricks=[
        trick("Compiler pairs",
              "CPI, IIP and GDP come from MoSPI (NSO). WPI and PPI come from DPIIT's Office of Economic Adviser.",
              "Who compiles the WPI?",
              ["WPI covers wholesale goods.", "It is a commerce-side index.", "The Office of Economic Adviser in DPIIT compiles it."],
              "Office of Economic Adviser, DPIIT"),
        trick("Core is headline without the volatile part",
              "Core inflation = headline minus food and fuel. Stagflation = stagnation plus inflation.",
              "Headline CPI is 6%. Food and fuel contribute 2.5%. What is core?",
              ["Core = headline - food and fuel part.", "6 - 2.5 = 3.5."],
              "About 3.5%"),
    ],
    mistakes=[
        mis("Using WPI for the inflation target.", "The MPC targets CPI."),
        mis("Giving WPI the old 2011-12 base.", "Since 15 June 2026 WPI uses 2022-23 with 957 items."),
        mis("Calling disinflation 'deflation'.", "Disinflation is a slower rise. Deflation is a fall."),
        mis("Saying WPI includes services.", "WPI covers goods only. CPI includes services."),
        mis("Treating IIP as a price index.", "IIP measures industrial output."),
    ],
    revision=[
        "Demand-pull is excess demand. Cost-push is costlier inputs.",
        "Stagflation is inflation with stagnation. Core = headline - food and fuel.",
        "CPI: retail, includes services, NSO (MoSPI), base 2024.",
        "WPI: wholesale, goods only, DPIIT, base 2022-23, 957 items.",
        "CPI-IW, CPI-AL and CPI-RL come from the Labour Bureau.",
        "The RBI targets CPI at 4% with a 2% band.",
        "IIP is output, re-based to 2022-23.",
    ],
    patterns=[
        pat("ga-ecoI-p1", "Identify the inflation type", "very common",
            "A story about an oil shock, monsoon failure or credit boom. The type is asked.",
            ["Ask: did demand rise or did costs rise?", "Higher demand (cheap loans, tax cuts) is demand-pull.", "Costlier inputs (crude, wages) is cost-push.", "Falling prices is deflation. Slower inflation is disinflation."],
            "The cause in the story gives the label.",
            "A sharp rise in imported crude oil prices pushes up general prices. What is this?",
            ["Crude oil is an input.", "Input cost rose.", "Demand did not need to rise."],
            "Cost-push inflation"),
        pat("ga-ecoI-p2", "Index, agency and coverage", "very common",
            "'The WPI is compiled by', 'which index does the RBI target', or 'which index covers services'.",
            ["CPI (Combined) comes from NSO, MoSPI.", "WPI comes from the Office of Economic Adviser, DPIIT.", "CPI-IW, CPI-AL and CPI-RL come from the Labour Bureau.", "WPI is goods only. CPI includes services."],
            "Each index has one agency and one coverage.",
            "The Wholesale Price Index in India is released by which office?",
            ["WPI is a commerce-ministry series.", "It sits in DPIIT.", "The Office of Economic Adviser releases it."],
            "Office of Economic Adviser, DPIIT (not the NSO)"),
        pat("ga-ecoI-p3", "Base years and new series", "common",
            "'The new CPI series uses which base year', 'the WPI basket was expanded to', or 'the IIP base'.",
            ["New CPI base is 2024 (February 2026).", "New WPI and IIP base is 2022-23.", "WPI items went from 697 to 957.", "Old bases were 2012 (CPI) and 2011-12 (WPI, IIP)."],
            "Match each index to its new year.",
            "The new Consumer Price Index series released in February 2026 has which base year?",
            ["CPI uses a calendar year.", "It replaced the 2012 base.", "The new year is 2024."],
            "2024"),
        pat("ga-ecoI-p4", "Core versus headline", "common",
            "'Core inflation excludes', 'headline inflation means', or a statement on food and fuel.",
            ["Headline is the full published index.", "Core = headline minus food and fuel.", "Food has a big CPI weight, so headline jumps with supply shocks.", "Disinflation is slower inflation. Deflation is negative."],
            "Core removes the volatile items.",
            "Core inflation is best described as what?",
            ["Start with headline inflation.", "Remove food and fuel.", "What remains is the underlying trend."],
            "Headline inflation excluding food and fuel"),
        pat("ga-ecoI-p5", "CPI variants, IIP and core industries", "occasional",
            "'DA is linked to which CPI', 'IIP measures', or 'the eight core industries include'.",
            ["CPI-IW from the Labour Bureau drives dearness allowance.", "CPI-AL and CPI-RL track farm and rural labourers.", "IIP measures output, not prices.", "Learn the eight core industries as one list."],
            "These small facts are fixed and easy to match.",
            "Which index is used to revise the dearness allowance of central employees?",
            ["Dearness allowance follows industrial workers' prices.", "That is CPI-IW.", "The Labour Bureau compiles it."],
            "CPI-IW (Consumer Price Index for Industrial Workers)"),
    ],
)

# =====================================================================
SUBS["eco-budget"] = dict(
    concept=(
        "The Budget is the government's yearly plan of income and spending. The Constitution calls it the Annual Financial Statement (Article 112). "
        "The main test topics are the four deficits, the three funds and the Budget dates. "
        "Budget 2026-27 put the fiscal deficit at 4.3% of GDP."
    ),
    notes=r"""### The Budget and the Constitution
The word "Budget" is not in the Constitution. **Article 112** calls it the **Annual Financial Statement**. Article 265 says no tax can be levied without the authority of law.

Since **2017** the Budget is presented on **1 February**. The Railway Budget was merged into it in the same year. The **Economic Survey** comes a day before, from the Department of Economic Affairs.

Spending goes through **Demands for Grants** and the **Appropriation Bill**. Taxes go through the **Finance Bill**.

### The three funds
| Fund | Article | Key point |
|---|---|---|
| Consolidated Fund | 266(1) | All revenues and loans; Parliament must approve each withdrawal |
| Public Account | 266(2) | Money held in trust (provident funds, small savings); no vote needed |
| Contingency Fund | 267 | At the President's disposal for unforeseen spending; corpus ₹30,000 crore (2021) |

### Revenue and capital
- **Revenue receipts:** taxes, interest, dividends.
- **Capital receipts:** borrowings, disinvestment, loan recoveries.
- **Revenue expenditure:** salaries, subsidies, interest.
- **Capital expenditure:** roads, buildings, defence equipment.

### The deficits
> **Rule:** Fiscal deficit = total expenditure - total receipts excluding borrowings.

| Deficit | Formula |
|---|---|
| Revenue | Revenue expenditure - revenue receipts |
| Effective revenue | Revenue deficit - grants for capital assets |
| Fiscal | Total expenditure - receipts excluding borrowings |
| Primary | Fiscal deficit - interest payments |

The fiscal deficit is the year's total borrowing need. The primary deficit removes interest on past debt. Interest payments are the largest expenditure head. Subsidies and defence follow.

> **Example:** Expenditure ₹45 lakh crore, receipts without borrowing ₹39 lakh crore. The fiscal deficit is ₹6 lakh crore.

### FRBM Act
The **FRBM Act, 2003** sets legal limits on deficits. It was amended in 2018 to add debt targets. Budgets announce a fiscal **glide path**, a year-by-year route for the deficit as a share of GDP.

### Budget 2026-27 at a glance
Nirmala Sitharaman presented it on 1 February 2026. These are budget estimates.

| Item | Figure |
|---|---|
| Total expenditure | ₹53.47 lakh crore |
| Receipts (excluding borrowings) | ₹36.52 lakh crore |
| Borrowings | ₹16.96 lakh crore |
| Fiscal deficit | 4.3% of GDP (RE 2025-26: 4.4%) |
| Revenue deficit | 1.5% of GDP |
| Primary deficit | 0.7% of GDP |
| Capital expenditure | ₹12.2 lakh crore |
| Central debt | 55.6% of GDP |
| Disinvestment target | ₹80,000 crore |

New in the Budget: Biopharma SHAKTI (₹10,000 crore), SME Growth Fund (₹10,000 crore), Semiconductor Mission 2.0 and MAT cut from 15% to 14%.
""",
    tricks=[
        trick("Number sheet 2026-27",
              "Spend 53.5, receipts 36.5, borrowing 16.9 (₹ lakh crore). Fiscal deficit 4.3%, revenue deficit 1.5%, primary deficit 0.7%. Capex 12.2. Debt 55.6%.",
              "What is the fiscal deficit in Budget 2026-27?",
              ["Recall the deficit trio: 4.3, 1.5, 0.7.", "Fiscal deficit is the largest of the three.", "It equals ₹16.96 lakh crore of borrowing."],
              "4.3% of GDP"),
        trick("Article trio for money",
              "112 is the Budget. 266 is the Consolidated Fund and Public Account. 267 is the Contingency Fund.",
              "Which article covers the Annual Financial Statement?",
              ["The Budget is the Annual Financial Statement.", "Recall the trio 112, 266, 267.", "The first one is the Budget."],
              "Article 112"),
    ],
    mistakes=[
        mis("Quoting 4.4% as the 2026-27 fiscal deficit.", "4.4% is the 2025-26 revised estimate. The 2026-27 budget estimate is 4.3%."),
        mis("Confusing primary deficit with revenue deficit.", "Primary = fiscal deficit - interest. Revenue = revenue expenditure - revenue receipts."),
        mis("Thinking the Railway Budget is still separate.", "It merged with the Union Budget in 2017."),
        mis("Saying Article 112 defines the word 'Budget'.", "Article 112 uses the term Annual Financial Statement."),
        mis("Saying the Contingency Fund is at Parliament's disposal.", "It is at the President's disposal (Article 267)."),
    ],
    revision=[
        "Budget = Annual Financial Statement (Article 112). Presented 1 February since 2017.",
        "Railway Budget merged in 2017. Economic Survey comes a day before.",
        "Funds: Consolidated 266(1), Public Account 266(2), Contingency 267.",
        "Contingency Fund is with the President; corpus ₹30,000 crore.",
        "RD = revenue exp - revenue receipts. FD = total exp - receipts excluding borrowings. PD = FD - interest.",
        "ERD = revenue deficit - grants for capital assets.",
        "FRBM Act 2003, amended 2018. Interest is the largest expenditure head.",
    ],
    patterns=[
        pat("ga-ecoBu-p1", "Deficit arithmetic", "very common",
            "Expenditure, receipts and interest figures are given. One deficit is asked.",
            ["Write the formula for the deficit asked.", "Fiscal = total expenditure - receipts excluding borrowings.", "Primary = fiscal deficit - interest payments.", "Check the units (lakh crore)."],
            "One subtraction gives the answer once the formula is right.",
            "Total expenditure is ₹45 lakh crore. Receipts excluding borrowings are ₹39 lakh crore. What is the fiscal deficit?",
            ["Fiscal deficit = expenditure - receipts excluding borrowings.", "45 - 39 = 6."],
            "₹6 lakh crore"),
        pat("ga-ecoBu-p2", "Budget structure, articles and funds", "common",
            "'Which article is the Annual Financial Statement', 'the Contingency Fund is at whose disposal', or a fund-and-article match.",
            ["112 is the Annual Financial Statement.", "266(1) is the Consolidated Fund. 266(2) is the Public Account.", "267 is the Contingency Fund, at the President's disposal.", "Only the Consolidated Fund needs Parliament's vote for withdrawals."],
            "Each fund has one article and one rule.",
            "The Contingency Fund of India is placed at whose disposal?",
            ["It is for unforeseen spending.", "Article 267 sets it up.", "The President controls it."],
            "The President"),
        pat("ga-ecoBu-p3", "Revenue versus capital, effective revenue deficit", "common",
            "'Which is a capital receipt', 'effective revenue deficit excludes', or a list with disinvestment, borrowings and grants.",
            ["Capital receipts: borrowings, disinvestment, loan recoveries.", "Capital expenditure builds assets: roads, buildings, defence equipment.", "Revenue expenditure: salaries, subsidies, interest.", "ERD = revenue deficit - grants for capital assets."],
            "Sort each item as revenue or capital by asking if it creates a liability or an asset.",
            "Which of these is a capital receipt?",
            ["Borrowings and loan recoveries are capital receipts.", "Selling government shares also counts.", "That sale is called disinvestment."],
            "Disinvestment proceeds"),
        pat("ga-ecoBu-p4", "FRBM and the glide path", "occasional",
            "'The FRBM Act was passed in', 'a glide path means', or a statement on deficit targets.",
            ["FRBM Act is 2003.", "A 2018 amendment added debt targets.", "A glide path is a year-by-year deficit route.", "Interest is the largest expenditure head."],
            "The Act and the glide path are fixed facts.",
            "In which year was the FRBM Act enacted?",
            ["FRBM stands for Fiscal Responsibility and Budget Management.", "It set legal deficit limits.", "It dates from 2003."],
            "2003"),
        pat("ga-ecoBu-p5", "Budget process, dates and documents", "common",
            "'Since which year is the Budget on 1 February', 'the Economic Survey is tabled when', or Demands for Grants questions.",
            ["From 2017 the Budget is on 1 February.", "The Railway Budget merged the same year.", "The Economic Survey comes a day before, from the DEA.", "Spending goes through the Appropriation Bill. Taxes go through the Finance Bill."],
            "The dates and the two bills are fixed.",
            "When is the Economic Survey presented?",
            ["It reviews the economy.", "The Department of Economic Affairs prepares it.", "It comes a day before the Budget."],
            "A day before the Union Budget"),
    ],
)
