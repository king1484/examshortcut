# -*- coding: utf-8 -*-
"""Assembles and saves the economy topic file."""
from gacommon import save_topic
from economy_concepts import C_BASICS, C_PLANNING, C_RBI, C_INFL
from economy_concepts2 import C_BUDGET, C_TAXES, C_SCHEMES, C_INST
from economy_questions import SOLVED, PRACTICE

topic = {
    "id": "economy",
    "sectionId": "ga",
    "title": "Indian Economy",
    "order": 8,
    "importance": "high",
    "avgQuestions": {"tier1": 2, "tier2": 2},
    "summary": "Planning legacy, national income, RBI and monetary policy, inflation indices, the Budget, taxes and GST, flagship schemes and economic institutions. CGL asks 2-3 questions, increasingly tilted to current numbers (rates, budget, index revisions).",
    "subtopics": [
        {
            "id": "eco-basics",
            "title": "National income, growth and base years",
            "concept": C_BASICS,
            "formulas": [
                {"name": "NNP", "tex": "NNP = GNP - \\text{Depreciation}", "note": "GNP already includes net factor income from abroad"},
                {"name": "GDP deflator", "tex": "\\text{Deflator} = \\frac{\\text{Nominal GDP}}{\\text{Real GDP}} \\times 100", "note": "divide nominal by (deflator/100) to get real"},
                {"name": "Market price bridge", "tex": "MP = FC + \\text{Indirect taxes} - \\text{Subsidies}", "note": "moving between factor cost and market price"},
            ],
            "tricks": [
                {
                    "title": "G-D-N ladder",
                    "body": "GDP (territory) + NFIA = GNP; GNP − depreciation = NNP. 'Territory → Nation → Net'.",
                    "example": {"q": "Which measure subtracts depreciation?", "solution": "NNP (Net National Product)."},
                },
                {
                    "title": "New base-year pairs",
                    "body": "Production takes financial years: **GDP and IIP = 2022-23**; prices of consumers take a calendar year: **CPI = 2024**; wholesale moved to 2022-23 with PPI twins in June 2026.",
                    "example": {"q": "New CPI base year?", "solution": "2024 (series launched February 2026)."},
                },
            ],
            "mistakes": [
                "Calling GNP 'GDP minus NFIA' — it is GDP **plus** NFIA.",
                "Quoting 2011-12 as the GDP base — since 27 Feb 2026 it is 2022-23.",
                "Assuming the Economic Survey comes from MoSPI — it is a Finance Ministry (DEA) document.",
            ],
        },
        {
            "id": "eco-planning",
            "title": "Five Year Plans and NITI Aayog",
            "concept": C_PLANNING,
            "formulas": [],
            "tricks": [
                {
                    "title": "Plan-era story line",
                    "body": "1-farm (1951) → 2-machines (Mahalanobis) → 3-wars → holiday (66-69) → 4-stability + bank nationalisation → 5-Garibi Hatao → rolling (Janata) → 6-7 growth → 8-reforms (1992) → 9-12 inclusive → NITI (2015).",
                    "example": {"q": "Which plan coincided with the LPG reforms?", "solution": "The 8th Plan (1992-97)."},
                },
                {
                    "title": "Plan-break tags",
                    "body": "Two gaps: **Plan Holiday 1966-69** (wars/drought) and **Annual Plans 1990-92** (transition after the 8th was delayed).",
                    "example": {"q": "Why was there a 'Plan Holiday'?", "solution": "1962 and 1965 wars plus drought deranged the 3rd Plan; 1966-69 ran as annual plans."},
                },
            ],
            "mistakes": [
                "Saying NITI Aayog is statutory — it is a Cabinet-resolution body.",
                "Crediting the 2nd Plan to Harrod-Domar — the 1st Plan's framework was Harrod-Domar; Mahalanobis belongs to the 2nd.",
                "Assuming the 12th Plan ended early — it ran full term to 2017; NITI then took over.",
            ],
        },
        {
            "id": "eco-rbi",
            "title": "Money, banking and the RBI",
            "concept": C_RBI,
            "formulas": [],
            "tricks": [
                {
                    "title": "Corridor arithmetic",
                    "body": "Repo is the middle: SDF = repo − 0.25 (floor), MSF = Bank Rate = repo + 0.25 (ceiling). With repo 5.25 → 5.00 / 5.25 / 5.50.",
                    "example": {"q": "If repo were 6.00%, what would the MSF be?", "solution": "6.25% — always repo + 25 bp."},
                },
                {
                    "title": "Nationalisation anchors",
                    "body": "1935 born, 1949 nationalised (RBI), 1955 SBI, 1969 fourteen, 1975 RRBs, 1980 six.",
                    "example": {"q": "How many banks in the 1980 round?", "solution": "Six (deposits ≥ ₹200 crore)."},
                },
                {
                    "title": "MPC fixed points",
                    "body": "6 members; 4 meetings a year minimum; target CPI 4% ± 2%; Governor's casting vote.",
                    "example": {"q": "Who has the casting vote in the MPC?", "solution": "The RBI Governor."},
                },
            ],
            "mistakes": [
                "Repeating pre-2026 rates — repo is 5.25%, CRR 3%, not 6.5%/4%.",
                "Confusing reverse repo (3.35%, dormant) with SDF (5.00%, the operative floor).",
                "Crediting the Nachiket Mor committee with banking reforms of the 1990s — those were Narasimham I/II.",
            ],
        },
        {
            "id": "eco-inflation",
            "title": "Inflation and price indices",
            "concept": C_INFL,
            "formulas": [],
            "tricks": [
                {
                    "title": "Index-compiler pairs",
                    "body": "CPI-IIP-GDP = MoSPI/NSO; WPI-PPI = DPIIT's Office of Economic Adviser. 'M for MoSPI, W for DPIIT(OEA)'.",
                    "example": {"q": "Who compiles the WPI?", "solution": "Office of Economic Adviser, DPIIT (Commerce & Industry Ministry)."},
                },
                {
                    "title": "Core = strip the volatile",
                    "body": "Core inflation = headline − food − fuel. Stagflation = stagnation + inflation together.",
                    "example": {"q": "If headline CPI is 6%, food & fuel contribute 2.5%, what is core?", "solution": "About 3.5%."},
                },
            ],
            "mistakes": [
                "Using WPI for the inflation target — the MPC targets **CPI**.",
                "Giving WPI the old 2011-12 base — since 15 June 2026 it is 2022-23 (957 items).",
                "Calling disinflation 'deflation' — disinflation is only a slower rise, deflation is a fall.",
            ],
        },
        {
            "id": "eco-budget",
            "title": "Budget and fiscal policy",
            "concept": C_BUDGET,
            "formulas": [
                {"name": "Fiscal deficit", "tex": "FD = \\text{Total Expenditure} - \\text{Total Receipts (excl. borrowings)}", "note": "equals government borrowing requirement"},
                {"name": "Revenue deficit", "tex": "RD = \\text{Revenue Expenditure} - \\text{Revenue Receipts}", "note": "revenue items only"},
                {"name": "Primary deficit", "tex": "PD = FD - \\text{Interest Payments}", "note": "strips out past borrowing costs"},
            ],
            "tricks": [
                {
                    "title": "Budget 2026-27 number sheet",
                    "body": "Spend 53.5 • Receipts 36.5 • Borrow 16.9 (₹ lakh crore); FD 4.3% • RD 1.5% • PD 0.7%; Capex 12.2; Debt 55.6%.",
                    "example": {"q": "Budget 2026-27 fiscal deficit?", "solution": "4.3% of GDP (₹16.96 lakh crore)."},
                },
                {
                    "title": "Article trio for money matters",
                    "body": "112-Budget • 266-Consolidated Fund • 267-Contingency Fund; 265-no tax without law.",
                    "example": {"q": "Which article is the Annual Financial Statement?", "solution": "Article 112."},
                },
            ],
            "mistakes": [
                "Quoting 4.4% for FY27 — 4.4% is the 2025-26 RE; the BE 2026-27 is 4.3%.",
                "Confusing primary deficit (fiscal − interest) with revenue deficit (revenue expenditure − receipts).",
                "Thinking the railway budget still exists separately — merged in 2017.",
            ],
        },
        {
            "id": "eco-taxes",
            "title": "Taxation and GST",
            "concept": C_TAXES,
            "formulas": [],
            "tricks": [
                {
                    "title": "GST article trio",
                    "body": "246A power • 269A inter-state • 279A Council. 101st Amendment, 1 July 2017.",
                    "example": {"q": "Which article created the GST Council?", "solution": "Article 279A (101st Amendment, 2016)."},
                },
                {
                    "title": "GST 2.0 slab story",
                    "body": "Two working slabs — 5 (merit) and 18 (standard) — with 40 kept aside for sin/luxury; 12% and 28% abolished on 22 Sep 2025.",
                    "example": {"q": "GST on a small car now?", "solution": "18% (moved from 28% plus cess)."},
                },
                {
                    "title": "Tax-year switch",
                    "body": "Income-tax Act, 2025 → effective 1 April 2026; one 'tax year' replaces previous/assessment year pair; 536 sections, 23 chapters.",
                    "example": {"q": "From which income year does 'Tax Year' apply?", "solution": "FY 2026-27, called Tax Year 2026-27."},
                },
            ],
            "mistakes": [
                "Calling STT an indirect tax — it is a direct tax on transactions.",
                "Assuming compensation cess continues on all goods — it ended 22 Sep 2025 except pan masala/tobacco lines.",
                "Mixing the GST Council's 3/4 weighted majority with a 'simple majority of members'.",
            ],
        },
        {
            "id": "eco-schemes",
            "title": "Government schemes and missions",
            "concept": C_SCHEMES,
            "formulas": [],
            "tricks": [
                {
                    "title": "Launch-year clusters",
                    "body": "2014: Jan Dhan, Make in India • 2015: BBBP, APY, MUDRA, PMAY • 2016: Ujjwala • 2018: Ayushman • 2019: KISAN • 2020: SVANidhi, PLI • 2023: Vishwakarma, Drone Didi • 2024: Surya Ghar • 2026: VB-G RAM G live (125 days).",
                    "example": {"q": "Which scheme gives ₹6,000 a year to farmers?", "solution": "PM-KISAN (2019, Agriculture Ministry)."},
                },
                {
                    "title": "MGNREGA → RAM G swap",
                    "body": "100 → 125 days; 15-day → weekly wages; Act of 2025, in force 1 July 2026.",
                    "example": {"q": "From when does VB-G RAM G apply?", "solution": "1 July 2026."},
                },
            ],
            "mistakes": [
                "Attaching Ayushman Bharat to the Health Ministry alone — PM-JAY sits with Health, but BBBP is a three-ministry convergence.",
                "Recalling MUDRA's ₹10 lakh limit but missing Tarun Plus (₹20 lakh, Oct 2024).",
                "Believing MGNREGA still runs — it is replaced by VB-G RAM G from 1 July 2026.",
            ],
        },
        {
            "id": "eco-institutions",
            "title": "Regulators, exchanges and international organisations",
            "concept": C_INST,
            "formulas": [],
            "tricks": [
                {
                    "title": "Regulator HQ pairs",
                    "body": "RBI-SEBI-NABARD = Mumbai; IRDAI = Hyderabad; SIDBI = Lucknow; PFRDA = New Delhi.",
                    "example": {"q": "SIDBI headquarters?", "solution": "Lucknow (set up 1990)."},
                },
                {
                    "title": "Bretton-Woods twins",
                    "body": "IMF + World Bank both born at Bretton Woods (1944), both in Washington DC; WTO (1995, Geneva) replaced GATT (1947).",
                    "example": {"q": "Where is the WTO headquartered?", "solution": "Geneva."},
                },
                {
                    "title": "Asian banks map",
                    "body": "ADB 1966 → Manila; AIIB 2016 → Beijing; NDB (BRICS) 2015 → Shanghai. India founding member in all three.",
                    "example": {"q": "NDB headquarters?", "solution": "Shanghai."},
                },
            ],
            "mistakes": [
                "Placing SEBI in New Delhi — it is Mumbai; PFRDA is the Delhi one.",
                "Saying India is an OECD member — India is not (it engages as a Key Partner).",
                "Assuming the IMF chief is always a European — tradition, not rule; Georgieva (Bulgarian) is the current MD.",
            ],
        },
    ],
    "pyqPatterns": [
        {
            "pattern": "Current RBI policy rates",
            "frequency": "very common",
            "howToSpot": "'The present repo rate / CRR / SDF is:'",
            "approach": "Memorise the corridor trio (5.00-5.25-5.50) plus CRR 3% and SLR 18%; refresh after every MPC.",
        },
        {
            "pattern": "Index and base-year questions",
            "frequency": "very common",
            "howToSpot": "'The new CPI/WPI/GDP series uses which base year?'",
            "approach": "2022-23 for GDP/IIP/WPI, 2024 for CPI; note compilers (NSO vs DPIIT).",
        },
        {
            "pattern": "Plan ↔ model / plan ↔ theme matching",
            "frequency": "common",
            "howToSpot": "'The Second Plan was based on...' or 'Garibi Hatao belongs to which plan?'",
            "approach": "Story-line of 12 plans; anchor Mahalanobis-2nd, Harrod-Domar-1st, Garibi Hatao-5th, LPG-8th.",
        },
        {
            "pattern": "Budget headline and deficit arithmetic",
            "frequency": "common",
            "howToSpot": "'Fiscal deficit in Budget 2026-27 is...' or a small primary-deficit calculation.",
            "approach": "Know 4.3% (FY27 BE), ₹53.5 lakh crore spend; primary deficit = fiscal − interest.",
        },
        {
            "pattern": "GST facts (council, slabs, dates)",
            "frequency": "very common",
            "howToSpot": "'GST Council is chaired by...' / 'new slabs effective...' ",
            "approach": "279A, FM-chaired, 3/4 weighted (Centre 1/3); GST 2.0 from 22 Sep 2025 (5/18/40).",
        },
        {
            "pattern": "Scheme ↔ ministry / provision matching",
            "frequency": "very common",
            "howToSpot": "Match pairs like PM-KISAN-Agriculture or the 125-day guarantee.",
            "approach": "Launch-year clusters table; note the 2025-26 swaps (VB-G RAM G, Vay Vandana).",
        },
        {
            "pattern": "Institutions: HQ, year, heads",
            "frequency": "common",
            "howToSpot": "'NABARD was set up in...' / 'SEBI headquarters...'",
            "approach": "Regulator HQ pairs + international bank HQs (Beijing AIIB, Shanghai NDB).",
        },
        {
            "pattern": "Statement-based economy (2 of 3 correct)",
            "frequency": "common",
            "howToSpot": "'Consider the statements...' with one wrong absolute statement.",
            "approach": "Hunt for stale numbers (old rates, old base years) — that is usually the false one.",
        },
    ],
    "solvedExamples": SOLVED,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    save_topic(topic)
