"""Economy part 1: eco-basics, eco-planning."""
from _eco_common import pat, mis, trick

# --- arithmetic used in examples -------------------------------------------------
assert 100 + 5 == 105
assert 330 * 100 // 300 == 110
assert 550 * 100 // 110 == 500
assert 900 + 120 - 20 == 1000

SUBS = {}

# =====================================================================
SUBS["eco-basics"] = dict(
    concept=(
        "National income measures how much a country produces in a year. The main measures are GDP, GNP and NNP, "
        "and each one adds or subtracts one item from the last. Real GDP uses fixed base-year prices, so it shows true growth. "
        "In 2026 MoSPI moved the GDP base year from 2011-12 to 2022-23."
    ),
    notes=r"""### The national income family
GDP counts what is produced **inside India**, by anyone. Other measures start from GDP and change one item at a time.

| Measure | How to get it |
|---|---|
| GDP | Final goods and services made within India in a year |
| GNP | GDP + NFIA |
| NNP | GNP - depreciation |
| National income | NNP at factor cost |
| Per capita income | National income / population |

NFIA means net factor income from abroad. It is what Indians earn abroad minus what foreigners earn here. Depreciation is the wear and tear of machines.

> **Example:** GDP is ₹100 and NFIA is ₹5. So GNP is ₹105.

The chain to remember is GDP, then GNP, then NNP, then national income. NNP at factor cost is the textbook meaning of "national income".

### Factor cost and market price
Market price is what buyers pay. Factor cost is what producers earn.

> **Rule:** Market price = factor cost + indirect taxes - subsidies.

Indirect taxes raise the price. Subsidies hold it down. If factor cost is ₹900, taxes are ₹120 and subsidies are ₹20, market price is ₹1000.

### Nominal and real GDP
Nominal GDP uses this year's prices. It can rise only because prices rose. Real GDP uses the prices of a fixed base year. It shows real production.

The link between them is the GDP deflator.

$$\text{Deflator} = \frac{\text{Nominal GDP}}{\text{Real GDP}} \times 100$$

Nominal GDP ₹330 and real GDP ₹300 give a deflator of 110. Prices are 10% above the base year.

> **Tip:** To get real GDP, divide nominal GDP by (deflator / 100).

### Three ways to measure
All three methods aim at the same total.

- **Income method:** add wages, rent, interest and profit.
- **Expenditure method:** add consumption, investment, government spending and net exports, written $C + I + G + (X-M)$.
- **Product method:** add the value added at each stage, so nothing is counted twice.

India now reports sectors as Gross Value Added (GVA) at basic prices. GDP equals GVA plus product taxes minus product subsidies. Estimates come in stages: advance, provisional, revised and final.

### Three sectors and core industries
| Sector | Examples |
|---|---|
| Primary | Agriculture, forestry, fishing, mining |
| Secondary | Manufacturing, construction, electricity |
| Tertiary (services) | Trade, transport, finance, IT, public administration |

India is a services-led economy. Services give over half of GVA.

The **eight core industries** are coal, crude oil, natural gas, refinery products, fertilisers, steel, cement and electricity. They carry a large weight in the IIP.

### Base years and who publishes
The **NSO** (National Statistical Office) works under **MoSPI**. It was formed in 2019 by merging the CSO and NSSO. The Economic Survey is different. The Department of Economic Affairs in the Finance Ministry issues it, a day before the Budget.

| Indicator | Old base | New base |
|---|---|---|
| GDP | 2011-12 | 2022-23 (27 Feb 2026) |
| CPI | 2012 | 2024 (12 Feb 2026) |
| IIP | 2011-12 | 2022-23 (from 1 Jun 2026) |
| WPI | 2011-12 | 2022-23 (15 Jun 2026) |

> **Watch:** GDP and IIP use a financial-year base. CPI uses a calendar year, 2024.
""",
    tricks=[
        trick("Territory, nation, net",
              "GDP is about territory. Add NFIA to reach the nation (GNP). Subtract depreciation to reach net (NNP).",
              "Which measure subtracts depreciation?",
              ["GDP is a gross measure.", "GNP adds NFIA and is still gross.", "NNP is GNP minus depreciation."],
              "NNP (Net National Product)."),
        trick("New base-year pairs",
              "Production series (GDP, IIP, WPI) use 2022-23. Consumer prices (CPI) use 2024.",
              "What is the new CPI base year?",
              ["CPI tracks consumer prices.", "The new series was launched in February 2026.", "It replaced the 2012 base."],
              "2024"),
    ],
    mistakes=[
        mis("Calling GNP 'GDP minus NFIA'.", "GNP is GDP plus NFIA."),
        mis("Quoting 2011-12 as the GDP base year.", "Since 27 Feb 2026 the base is 2022-23."),
        mis("Thinking the Economic Survey comes from MoSPI.", "It is a Finance Ministry (DEA) document."),
        mis("Using GDP divided by population as per capita income.", "Exam definition: national income (NNP) divided by population."),
        mis("Adding subsidies when going from factor cost to market price.", "Add indirect taxes and subtract subsidies."),
    ],
    revision=[
        "GDP is within India. GNP = GDP + NFIA. NNP = GNP - depreciation.",
        "National income = NNP at factor cost.",
        "Market price = factor cost + indirect taxes - subsidies.",
        "Deflator = (nominal / real) x 100.",
        "New bases: GDP, IIP, WPI 2022-23; CPI 2024.",
        "NSO sits under MoSPI (CSO + NSSO merged in 2019).",
        "Eight core industries: coal, crude oil, gas, refinery, fertilisers, steel, cement, electricity.",
    ],
    patterns=[
        pat("ga-ecoB-p1", "GDP, GNP and NNP chains", "very common",
            "Words like 'GNP equals', 'national income means', or 'which is the widest measure'. Statement sets mix the four aggregates.",
            ["Write the chain: GDP, +NFIA, GNP, -depreciation, NNP.", "National income means NNP at factor cost.",
             "Check each option against the chain.", "Reject any option that says GDP includes NFIA."],
            "Every option is a step in the same chain, so the chain settles it.",
            "If GDP is ₹100 and net factor income from abroad is ₹5, GNP equals what?",
            ["GNP = GDP + NFIA.", "100 + 5 = 105.", "Residents earn more abroad than foreigners earn here."],
            "₹105"),
        pat("ga-ecoB-p2", "Nominal and real GDP, the deflator", "very common",
            "Nominal and real GDP figures are given and the deflator is asked. Or two GDP concepts are compared.",
            ["Divide nominal GDP by real GDP.", "Multiply by 100.", "For real GDP, divide nominal GDP by (deflator / 100).", "Read the result as a price index with the base year at 100."],
            "The deflator tells you how far prices have moved since the base year.",
            "Nominal GDP is ₹330 lakh crore and real GDP is ₹300 lakh crore. What is the GDP deflator?",
            ["330 / 300 = 1.1.", "1.1 x 100 = 110.", "Prices are 10% above the base year."],
            "110"),
        pat("ga-ecoB-p3", "Base years and the new series", "common",
            "'The new GDP series has which base year', 'the old base was', or 'who releases national accounts'.",
            ["Recall old bases: GDP and IIP 2011-12, CPI 2012.", "Recall new bases: GDP 2022-23, CPI 2024.", "The release body is the NSO under MoSPI.", "A base year is the year whose prices equal 100."],
            "Base-year questions follow the 2026 revision, so learn both the old and new years.",
            "India's national accounts statistics are released by which body?",
            ["National accounts are official statistics.", "The CSO and NSSO were merged in 2019.", "The merged body works under MoSPI."],
            "The National Statistical Office (NSO), under MoSPI"),
        pat("ga-ecoB-p4", "Per capita income and the methods", "occasional",
            "'Per capita income is calculated from', 'the expenditure method adds', or 'which method uses wages, rent, interest, profit'.",
            ["Per capita income = national income / population.", "Wages, rent, interest, profit means the income method.", "C + I + G + (X - M) means the expenditure method.", "Value added at each stage means the product method."],
            "Each method has its own list of items, so match the list to the name.",
            "The expenditure method of measuring national income adds up what?",
            ["Start with private consumption.", "Add investment and government spending.", "Add net exports, which is X - M."],
            "C + I + G + (X - M)"),
        pat("ga-ecoB-p5", "Sectors, GVA and core industries", "occasional",
            "'Which activity is tertiary', 'GVA is measured at which prices', or a list of the eight core industries.",
            ["Sort the activity: farming and mining primary, factories secondary, services tertiary.", "GVA is measured at basic prices.", "GDP = GVA + product taxes - product subsidies.", "Learn the eight core industries as one list."],
            "The GVA link is a fixed formula and the sector lists are short.",
            "Under the GVA framework, how is GDP obtained?",
            ["GVA at basic prices is the starting point.", "Add product taxes.", "Subtract product subsidies."],
            "GDP = GVA + product taxes - product subsidies"),
        pat("ga-ecoB-p6", "Factor cost to market price", "occasional",
            "Factor cost, taxes and subsidies are given. Market price is asked.",
            ["Write the bridge: MP = FC + indirect taxes - subsidies.", "Add the taxes.", "Subtract the subsidies."],
            "The bridge always runs the same way, so one line settles it.",
            "Factor cost is ₹900. Indirect taxes are ₹120 and subsidies are ₹20. What is market price?",
            ["900 + 120 = 1020.", "1020 - 20 = 1000."],
            "₹1000"),
        pat("ga-ecoB-p7", "Recover real GDP from the deflator", "occasional",
            "Nominal GDP and a deflator are given. Real GDP is asked.",
            ["Divide the deflator by 100.", "Divide nominal GDP by that number."],
            "Real GDP strips out the price rise, so it must be smaller when the deflator is above 100.",
            "Nominal GDP is ₹550 lakh crore and the deflator is 110. What is real GDP?",
            ["110 / 100 = 1.1.", "550 / 1.1 = 500."],
            "₹500 lakh crore"),
    ],
)

# =====================================================================
SUBS["eco-planning"] = dict(
    concept=(
        "India ran twelve Five Year Plans from 1951 to 2017. The Planning Commission made them. "
        "On 1 January 2015 NITI Aayog replaced the Commission. NITI is a think tank and does not allocate plan funds."
    ),
    notes=r"""### From plans to NITI
The **Planning Commission** was set up on 15 March 1950 by a **Cabinet resolution**. The Prime Minister was its chairman. It steered twelve Five Year Plans from 1951 to 2017.

From 1 January 2015 a Cabinet resolution created **NITI Aayog** (National Institution for Transforming India). Neither body is constitutional or statutory.

### The plans and their ideas
| Plan | Period | Idea |
|---|---|---|
| 1st | 1951-56 | Harrod-Domar model; agriculture and irrigation |
| 2nd | 1956-61 | Mahalanobis model; heavy industry |
| 3rd | 1961-66 | Self-reliance; Gadgil strategy; broken by wars and drought |
| Plan Holiday | 1966-69 | Three annual plans |
| 4th | 1969-74 | Growth with stability |
| 5th | from 1974 | Garibi Hatao; ended early |
| Rolling plan | 1978-80 | Lakdawala concept |
| 6th | 1980-85 | Poverty removal; IRDP and NREP begin |
| 7th | 1985-90 | Food, work, productivity |
| Annual plans | 1990-92 | Transition years |
| 8th | 1992-97 | Started with the 1991 LPG reforms |
| 9th | 1997-2002 | Growth with social justice |
| 10th | 2002-07 | 8% growth target |
| 11th | 2007-12 | Faster and more inclusive growth |
| 12th | 2012-17 | Faster, more inclusive, sustainable growth |

> **Tip:** The 2nd plan is Mahalanobis, and Mahalanobis means machines.

### Breaks in the plan sequence
Two gaps and one special idea are asked often.

- **Plan Holiday (1966-69):** the 1962 and 1965 wars and drought derailed the 3rd plan. Three annual plans followed.
- **Rolling plan (1978-80):** the plan is revised every year. D.T. Lakdawala is linked to the concept.
- **Annual plans (1990-92):** they ran before the delayed 8th plan.

The 12th plan was the last. It ran to 2017, and then NITI took over.

### NITI Aayog: who is in it
The **Prime Minister chairs** NITI Aayog. The **Governing Council** has all Chief Ministers and the Lt Governors of Union Territories. The PM appoints a Vice-Chairperson and full-time members. A **CEO** runs the daily work.

Its ideas are **cooperative federalism**, where states are partners, and **competitive federalism**, where states are ranked.

### What NITI produces
NITI does not make Five Year Plans. It writes three documents:

1. a **15-year vision**
2. a **7-year strategy**
3. a **3-year action agenda**

Its well-known products are the SDG India Index, the state Multidimensional Poverty Index, the Composite Water Management Index and the Aspirational Districts Programme (2018, 112 districts).

### Planning Commission versus NITI
| Point | Planning Commission | NITI Aayog |
|---|---|---|
| Started | 15 March 1950 | 1 January 2015 |
| Origin | Cabinet resolution | Cabinet resolution |
| Role | Made plans, allocated funds | Advises, monitors, builds indices |

> **Watch:** NITI is not statutory and does not allocate plan funds.
""",
    tricks=[
        trick("Plan story line",
              "Farm (1st), machines (2nd), wars (3rd), holiday, stability (4th), Garibi Hatao (5th), rolling plan, reforms (8th), inclusive (11th), sustainable (12th), then NITI.",
              "Which plan coincided with the LPG reforms?",
              ["The reforms began in 1991.", "The plans after the annual plans of 1990-92 began in 1992.", "That is the 1992-97 plan."],
              "The 8th Plan (1992-97)"),
        trick("Two gaps",
              "Plan Holiday was 1966-69. Annual Plans were 1990-92.",
              "Why was there a 'Plan Holiday'?",
              ["The 1962 and 1965 wars hit the economy.", "Drought made it worse.", "The 3rd plan was derailed and annual plans ran in 1966-69."],
              "War and drought derailed the 3rd Plan."),
    ],
    mistakes=[
        mis("Saying NITI Aayog is statutory.", "It was set up by a Cabinet resolution."),
        mis("Crediting the 2nd Plan to Harrod-Domar.", "Harrod-Domar is the 1st Plan. Mahalanobis is the 2nd."),
        mis("Thinking the 12th Plan ended early.", "It ran its full term to 2017. NITI then took over."),
        mis("Saying NITI Aayog allocates plan funds.", "It advises and monitors. It does not allocate funds."),
        mis("Mixing up the Plan Holiday (1966-69) and the rolling plan (1978-80).", "Holiday means annual plans after the 3rd plan. Rolling means revised every year."),
    ],
    revision=[
        "Planning Commission: 15 March 1950, Cabinet resolution, PM as chairman.",
        "12 Five Year Plans, 1951 to 2017. The 12th was the last.",
        "1st = Harrod-Domar. 2nd = Mahalanobis, heavy industry.",
        "Plan Holiday 1966-69. Rolling plan 1978-80. Annual plans 1990-92.",
        "8th plan began with the 1991 reforms. 11th = inclusive. 12th = sustainable.",
        "NITI Aayog: 1 January 2015, Cabinet resolution, PM chairs.",
        "NITI documents: 15-year vision, 7-year strategy, 3-year action agenda.",
    ],
    patterns=[
        pat("ga-ecoP-p1", "Plan and model matching", "very common",
            "'The Second Plan was based on', 'the Harrod-Domar model belongs to which plan', or a thinker-plan match.",
            ["Link the 1st plan to Harrod-Domar and agriculture.", "Link the 2nd plan to Mahalanobis and heavy industry.", "Link the 3rd plan's strategy to D.R. Gadgil.", "Heavy industry or capital goods in the question means the 2nd plan."],
            "Two pairs carry most of the marks.",
            "The Mahalanobis model, which stressed heavy industry, was the basis of which plan?",
            ["Mahalanobis is linked to machines.", "Heavy industry was the focus.", "That was the 2nd plan, 1956-61."],
            "The Second Five Year Plan (1956-61)"),
        pat("ga-ecoP-p2", "Plan, years and theme", "very common",
            "'Growth with stability was the theme of', 'which plan coincided with the 1991 reforms', or 'which was the last plan'.",
            ["Recall the theme hooks: 4th stability, 9th social justice, 11th inclusive, 12th sustainable.", "The 8th plan opened in the liberalisation era.", "The 12th plan (2012-17) was the last.", "Check the gaps: Plan Holiday and Rolling Plan."],
            "Each plan has one short theme, so match the theme to the number.",
            "'Growth with stability' was the objective of which Five Year Plan?",
            ["Recall the theme list.", "Stability belongs to the plan after the Plan Holiday.", "That is 1969-74."],
            "The Fourth Plan (1969-74)"),
        pat("ga-ecoP-p3", "NITI Aayog structure and documents", "common",
            "'Who chairs NITI Aayog', 'the Governing Council consists of', or the 15-year, 7-year and 3-year documents.",
            ["The Prime Minister chairs it.", "The Governing Council has all Chief Ministers and UT Lt Governors.", "A CEO runs daily work.", "Its documents: 15-year vision, 7-year strategy, 3-year action agenda."],
            "The Governing Council is the centre-state forum, and the document trio is a fixed list.",
            "The Governing Council of NITI Aayog includes which members?",
            ["The Prime Minister is the chair.", "All state Chief Ministers are members.", "Lt Governors of Union Territories are members."],
            "The PM, all Chief Ministers and the Lt Governors of UTs"),
        pat("ga-ecoP-p4", "Planning Commission versus NITI Aayog", "common",
            "Statement pairs on fund allocation, legal origin, or year of replacement.",
            ["Both came from Cabinet resolutions.", "The Commission made plans and allocated funds.", "NITI advises, monitors and builds indices.", "Reject any option calling NITI statutory."],
            "Most wrong statements swap the two roles or claim a legal status.",
            "Which statement about NITI Aayog is correct?",
            ["It was set up on 1 January 2015.", "A Cabinet resolution created it.", "It is an advisory think tank and does not allocate plan funds."],
            "It is a Cabinet-resolution think tank that replaced the Planning Commission."),
        pat("ga-ecoP-p5", "Plan Holiday, rolling plan, annual plans", "occasional",
            "'The Plan Holiday occurred during', 'the rolling plan is linked to', or 'which plans were cut short'.",
            ["Plan Holiday is 1966-69, with three annual plans.", "Rolling plan is 1978-80, linked to D.T. Lakdawala.", "Annual plans also ran in 1990-92.", "The 5th plan ended early."],
            "Each break has its own years and its own cause.",
            "The 'Plan Holiday' in Indian planning refers to which years?",
            ["The 3rd plan was derailed by wars and drought.", "Annual plans replaced the five-year plan.", "They ran for three years."],
            "1966-69"),
    ],
)
