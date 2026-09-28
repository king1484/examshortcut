"""Phase-2 deep content for ga/economy. Run: py -3 economy.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from ec_part1 import build_basics, build_planning, build_rbi, build_inflation
from ec_part2 import build_budget, build_taxes, build_schemes, build_institutions


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Policy rates and the monetary corridor", "very common",
      "'The repo rate is the rate at which', 'the SDF sits how far below the repo', 'who holds the casting vote in the MPC', or a table of rate ↔ definition is offered.",
      "Fix the corridor's geometry, not its numbers: SDF = repo − 25 bp (floor, collateral-free), MSF = Bank Rate = repo + 25 bp (ceiling). MPC = 6 members (3 RBI, Governor casting vote), bi-monthly, CPI 4% ± 2%, breach reported after 3 quarters. CRR is cash with the RBI; SLR is the bank's own liquid assets — never call them policy rates.",
      "eco-rbi",
      "In India's current framework, the **Bank Rate** equals —",
      "The **MSF rate** — repo + 25 basis points at the corridor ceiling; the SDF (repo − 25 bp) is the floor."),
    P("Index, agency and base-year matching", "very common",
      "'The WPI is compiled by', 'which index does the RBI target', 'the new GDP series uses which base year' — options pair CPI, WPI, IIP, deflator with agencies and bases.",
      "Grid it: CPI — NSO/MoSPI, retail, services included, new base 2024 (Feb 2026); WPI — Office of Economic Adviser (DPIIT), wholesale, goods only, new base 2022-23 (Jun 2026) with PPIs; IIP — NSO output index, re-based 2022-23; CPI-IW — Labour Bureau (DA linkage). RBI targets headline CPI, never WPI.",
      "eco-inflation",
      "Which pair is correctly matched?\n(a) WPI — NSO (b) CPI — Office of Economic Adviser (c) IIP — a price index (d) CPI-IW — Labour Bureau",
      "(d) — CPI-IW is compiled by the Labour Bureau and drives dearness allowance. WPI belongs to DPIIT's Office of Economic Adviser, CPI to the NSO, and the IIP measures output, not prices."),
    P("Plan ↔ model ↔ theme matching", "common",
      "'The Mahalanobis model belongs to which plan', 'growth with stability was the objective of', ordering of plans or spotting the last plan and the plan interludes.",
      "Two model pairs carry the marks: 1st — Harrod-Domar (agriculture), 2nd — Mahalanobis (heavy industry). Theme hooks: 4th growth with stability, 8th launched with the 1991 LPG reforms, 11th inclusive, 12th (2012-17) the last plan. Interludes: Plan Holiday 1966-69, Rolling Plan 1978-80, annual plans 1990-92.",
      "eco-planning",
      "The **Harrod-Domar model** formed the basis of which Five Year Plan?",
      "The **First Plan (1951-56)** — agriculture and irrigation priority; the 2nd plan switched to Mahalanobis and heavy industry."),
    P("Budget structure, funds and deficit arithmetic", "very common",
      "Either figures for expenditure, receipts and interest are given and a deficit is asked, or articles/funds are matched: Annual Financial Statement 112, Consolidated Fund 266(1), Contingency Fund 267.",
      "Four formulas settle it: RD = revenue expenditure − revenue receipts; ERD = RD − capital-asset grants; FD = total expenditure − receipts excluding borrowings; PD = FD − interest (can be negative). Articles: 112 AFS, 266 two funds, 267 Contingency (President, ₹30,000 crore). Budget on 1 February since 2017; Railway Budget merged 2017; Economic Survey the day before.",
      "eco-budget",
      "Total expenditure ₹45 lakh crore, receipts excluding borrowings ₹39 lakh crore, interest payments ₹10 lakh crore. The primary deficit is —",
      "6 − 10 = **−₹4 lakh crore** — a primary surplus: FD = 45 − 39 = 6, then subtract interest."),
    P("GST: articles, council and the slab reform", "very common",
      "'Article 279A provides for', 'GST was introduced from', 'the new slabs after the 2025 reform are' — plus CGST/SGST/IGST structure and council voting shares.",
      "Chain: 101st Amendment (2016) → GST from 1 July 2017 → Articles 246A (power), 269A (IGST), 279A (Council). Council: Union FM chairs, 3/4 weighted majority, Centre 1/3 vs states 2/3. Slabs since 22 September 2025 (Council decision 3 September 2025): 5% merit and 18% standard, 40% demerit rate, 12% abolished.",
      "eco-taxes",
      "In the GST Council, the combined weighted vote share of the **states** is —",
      "**Two-thirds** — the Centre holds one-third and decisions need a three-fourths majority, so states together can block but not pass."),
    P("Scheme ↔ ministry ↔ benefit matching", "very common",
      "'₹6,000 a year is given under', 'Har Ghar Jal is the goal of', 'which ministry runs POSHAN', or match-the-column pairing schemes with years and benefits.",
      "Anchor on the rupee figures and dates: PM-KISAN ₹6,000/yr (2019); PM-JAY ₹5 lakh/family (2018); MUDRA tiers 50k/5L/10L (2015); Jan Dhan 28-8-2014; SBM 2-10-2014; Ujjwala 1-5-2016; JJM 2019; Gati Shakti 2021. Employment: MGNREGA (100 days) replaced by VB-G RAM G from 1 July 2026 — 125 days, weekly wages.",
      "eco-schemes",
      "The health cover of **₹5 lakh per family per year** for hospitalisation is provided under —",
      "**Ayushman Bharat PM-JAY** (23 September 2018); its digital arm, the ABDM (2021), issues ABHA health IDs."),
    P("Regulators, institutions and multilaterals: sector, HQ, year", "very common",
      "'SEBI became statutory in', 'SIDBI is headquartered at', 'the NDB of BRICS is based in', pairs mixing regulators, development banks and multilateral institutions.",
      "Sector lines: SEBI — securities (1992 Act, Mumbai); IRDAI — insurance (1999, Hyderabad); PFRDA — pensions (2013 Act, New Delhi); RBI — banks and payments. Dev banks: NABARD 1982 (Mumbai), SIDBI 1990 (**Lucknow**), EXIM 1982, NHB 1988. Multilaterals: IMF/WB 1944 Washington, WTO 1995 Geneva, ADB 1966 Manila, AIIB 2016 Beijing, NDB 2015 Shanghai.",
      "eco-institutions",
      "Which pair is correctly matched?\n(a) IRDAI — Mumbai (b) SIDBI — Lucknow (c) ADB — Beijing (d) NDB — Manila",
      "(b) — SIDBI (1990) is headquartered at Lucknow. IRDAI sits at Hyderabad, the ADB at Manila, and the BRICS NDB at Shanghai."),
    P("Statement-based economy (2-3 statements, pick correct set)", "very common",
      "Numbered statements about monetary policy, the budget, GST or a flagship scheme are offered and the candidate picks which are correct — the dominant PYQ format for this topic.",
      "Hunt the planted error first: 'payment banks can lend' (false), 'the RBI targets WPI' (false — CPI), 'fiscal deficit never exceeds revenue deficit' (false), 'cesses are shared with states' (false — outside the divisible pool), 'Plan Holiday followed the 2nd plan' (false — the 3rd). If one statement is clearly wrong, three options fall at once.",
      "eco-rbi",
      "Consider: 1. The MPC has six members. 2. The RBI's inflation target is framed on the WPI. 3. Payment banks cannot undertake lending. Which are correct?",
      "Statements 1 and 3 only — the MPC has six members with the Governor's casting vote, the target is **CPI** 4% ± 2%, and payment banks take deposits without lending."),
]

if __name__ == "__main__":
    subs = [build_basics(), build_planning(), build_rbi(), build_inflation(),
            build_budget(), build_taxes(), build_schemes(), build_institutions()]
    apply_topic("economy", subs, PYQ)
