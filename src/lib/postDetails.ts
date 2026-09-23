// Long-form per-post content. Numbers (level, age, in-hand) come from exam.json; only the
// narrative lives here. Everything marked "typical" varies by zone and cadre year to year.

export type PostDetail = {
  tagline: string;
  about: string;
  profile: string[];
  growth: [string, string][]; // [role + level, typical time]
  goodFor: string;
  watchOut: string[];
};

export const POST_DETAILS: Record<string, PostDetail> = {
  aao: {
    tagline: 'The highest-paid post in CGL — audit of government departments under C&AG.',
    about:
      'Assistant Audit Officer is a Group B gazetted post in the Indian Audit & Accounts Department, the office of the Comptroller and Auditor General. You audit the accounts of central and state government departments, PSUs and autonomous bodies. It carries the highest pay level (8) of any CGL post, and the audit cadre is known for predictable, desk-oriented work.',
    profile: [
      'Audit parties visit government offices and PSU premises; you examine vouchers, contracts and compliance records there',
      'Desk work back at the office: drafting audit notes, chasing replies, preparing audit reports and paras',
      'Performance audit of big schemes and certification of accounts; you may specialise (IT audit, health, energy)',
      'Travel is real but bounded — audit parties typically tour some weeks a month, often within your stationed office\'s jurisdiction',
    ],
    growth: [
      ['AAO (Level 8, gazetted)', 'entry post'],
      ['Audit Officer / Senior AAO (Level 9–10)', '≈ 6–10 years, by DPC'],
      ['Deputy Accountant General cadre support (Level 11+)', 'seniority-capped, slow'],
      ['IA&AS officer only via the separate UPSC route, not by promotion from here in practice', '—'],
    ],
    goodFor:
      'You want the top CGL pay level with gazetted status, steady desk work with some touring, and a qualification-heavy professional environment. CA/CS/CMA/MBA-Fin/M.Com holders find the work familiar.',
    watchOut: [
      'The desirable qualification (CA/CS/CMA/MBA-Fin/M.Com) is optional at application, but you compete against candidates who have it',
      'Posting follows C&AG offices across states — an home-state posting is not guaranteed',
      'Slower empanelment-style growth than an organised Group A service; most careers plateau around Audit Officer',
    ],
  },
  aso: {
    tagline: 'Desk officer in a central ministry in Delhi; the classic Delhi career post.',
    about:
      'Assistant Section Officer is a Group B non-gazetted post, mostly in the Central Secretariat Service — the ministries and departments of Government of India in New Delhi. A smaller stream goes to MEA, AFHQ and other offices. ASO is the entry point of the main Delhi bureaucratic ladder.',
    profile: [
      'File work: putting up noting and drafts, tracking approvals, preparing briefs and replies to Parliament questions',
      'Section handling — you become the person who knows the rules and the file history of your subject',
      'Meeting coordination, inter-ministerial references, RTI and court-case replies',
      'MEA stream: posting in Indian missions abroad in rotation, which is the single biggest lifestyle difference in CGL',
    ],
    growth: [
      ['ASO (Level 7)', 'entry post'],
      ['Section Officer (Level 8)', '≈ 8–12 years, by DPC'],
      ['Under Secretary (Level 10, deemed gazetted)', '≈ 15+ years'],
      ['Deputy Secretary and above', 'a small promotee quota reaches this'],
    ],
    goodFor:
      'You want a Delhi desk career in the secretariat, good promotion prospects for a Group B post, and city schooling/family stability. The CSS ladder to Under Secretary is one of the cleanest in the central services.',
    watchOut: [
      'CSS is almost entirely Delhi — great if you want Delhi, restrictive if you don\'t',
      'Work is rule-and-file heavy; the first years are genuinely clerical before you grow into section handling',
      'Government accommodation is scarce relative to demand; plan rent for the first years',
    ],
  },
  iti: {
    tagline: 'Assess incomes, run surveys and raids — the post most people picture when they say "CGL".',
    about:
      'Income Tax Inspector in CBDT works in assessment wings or in the investigation/TDS wings of a Principal Chief Commissionerate. It is a Group B non-gazetted post with genuine authority — notices, surveys and search-assessment participation — and is among the most sought-after preferences every year.',
    profile: [
      'Assessment wing: processing returns, framing assessments under a supervising Income Tax Officer, handling rectifications and appeals notes',
      'Tax Evasion / Investigation wing: surveys of business premises and participation in search & seizure operations',
      'TDS wing: verifying deductors, chasing defaults, certificate handling',
      'Mostly desk work punctuated by field duty; raids are team work and usually not frequent enough to define the job',
    ],
    growth: [
      ['Income Tax Inspector (Level 7)', 'entry post'],
      ['Income Tax Officer (Level 8)', '≈ 6–8 years after the departmental exam'],
      ['Assistant Commissioner (IRS promotee quota)', 'slow; a fraction of ITOs reach it'],
    ],
    goodFor:
      'You want a respected enforcement-adjacent career with a mix of desk and field work, decent growth through the departmental exam, and a posting in your region (zones are large but you generally stay within one commissionerate region).',
    watchOut: [
      'Zone preference matters — big-city regions fill with higher ranks; a lower rank can mean a far corner of the region',
      'Targets and assessment pressure exist; the ITO above you shapes your work life more than anything else',
      'No uniform, no housing priority — plan for rent in most postings',
    ],
  },
  cbic: {
    tagline: 'Customs at ports and airports, GST and excise field formations — the most "field" CGL offers.',
    about:
      'This preference covers three Inspector roles in CBIC: Central Excise Inspector (GST field work), Preventive Officer (customs at airports and seaports) and Examiner (customs clearance of cargo and vessels). Group B non-gazetted, Level 7, and the work is the most operationally field-heavy in CGL.',
    profile: [
      'Central Excise/GST: registration verification, audit of assessees, detection of duty evasion, adjudication support',
      'Preventive Officer: passenger profiling and baggage at airports, anti-smuggling patrols at ports, rummaging of vessels',
      'Examiner: examination of import/export cargo, assessment of duty, clearing ships — logistics-heavy, out-door work',
      'Uniformed drills exist in some formations; shifts at ports/airports are common in PO and Examiner roles',
    ],
    growth: [
      ['Inspector / PO / Examiner (Level 7)', 'entry post'],
      ['Superintendent (Level 8)', '≈ 8–15 years by zone; heavy backlog varies by cadre'],
      ['Assistant Commissioner (promotee quota)', 'slow and zone-dependent'],
    ],
    goodFor:
      'You want operational, outdoors work with real authority day one, are fine with shifts and transfers, and want a post where the department (customs houses, ports, airports) is a visible institution.',
    watchOut: [
      'Transfers across a large zone are frequent in the first years; home posting is luck-of-the-rank',
      'Superintendent promotion is backlog-choked in several zones — ask current officers, not brochures',
      'Integrity pressure is real in customs postings; the department watches its inspectors closely',
    ],
  },
  'si-cbi': {
    tagline: 'Investigate corruption cases in India\'s premier investigative agency.',
    about:
      'Sub-Inspector in the Central Bureau of Investigation is a Group B post, Level 7, working on anti-corruption and special-crime cases under an SP. CBI is small and centrally posted, with training at the CBI Academy, and the SI is the backbone of its casework.',
    profile: [
      'Case investigation support: source information, surveillance, raids along with DSP-led teams',
      'Documentation: charge-sheets, case diaries, court appearances with the prosecuting officer',
      'Verification and disproportionate-assets inquiries; liaison with banks, registries and other departments',
      'Delhi and regional branch offices; travel within your branch\'s jurisdiction is constant',
    ],
    growth: [
      ['Sub-Inspector (Level 7)', 'entry post'],
      ['Inspector (Level 8)', '≈ 6–8 years, by DPC'],
      ['DSP rank work as Inspector (Investigation)', 'seniority-based, limited'],
    ],
    goodFor:
      'You want investigative work in a compact, high-prestige agency with manageable strength, you meet the physical standards comfortably, and you can accept Delhi-centric posting with travel.',
    watchOut: [
      'Physical and medical standards apply at appointment (height/chest/walking-cycling tests) — failing them at DV ends the candidacy',
      'Small cadre means slow, seniority-locked growth compared with tax departments',
      'Court testimony and case deadlines can make hours unpredictable',
    ],
  },
  jso: {
    tagline: 'The only CGL post for Statistics graduates — surveys and official data at MoSPI.',
    about:
      'Junior Statistical Officer is a Group B post in the Ministry of Statistics & Programme Implementation (NSSO/CSO). It is the only CGL post with an academic gate — you must have Statistics as a subject in your degree, and you also sit Paper 2 (Statistics) in Tier 2. The trade: a slightly lower pay level for a technical, research-flavoured career.',
    profile: [
      'Field-operations support for national surveys (household consumption, employment, industry) — scrutiny of schedules and data quality',
      'Data processing, tabulation and analysis in FOD offices or CSO divisions',
      'Report drafting for publications used by every economist in the country',
      'Far less public contact than tax/customs posts; the work is technical and team-based',
    ],
    growth: [
      ['JSO (Level 6)', 'entry post'],
      ['Senior Statistical Officer (Level 7)', 'via the SSO grade exam/DPC, ≈ 5–8 years'],
      ['Deputy Director (Level 8+)', 'seniority-capped'],
    ],
    goodFor:
      'You studied Statistics, prefer data work to enforcement, and want a government career where the degree you earned is actually used. The Paper 2 gate thins the competition sharply.',
    watchOut: [
      'FOD survey duties can include touring your region for field scrutiny — it is not a pure desk job',
      'Pay level 6 is a rung below the Level 7 posts; the exam discount is the competition relief you are buying',
      'Fewer posts than tax/customs, so cut-offs behave differently — a "safe" tier-1 score for other posts may not be safe here',
    ],
  },
  auditor: {
    tagline: 'Entry into the audit cadre at Level 5 — the same offices as AAO, one rung lower.',
    about:
      'Auditor is a Group C post in the C&AG, CGDA and CGA offices. The work mirrors the AAO cadre — audit of government accounts — at a lower pay level and with a steadier clerical-technical mix. It is one of the most-applied CGL posts because it is seen as a stable, transfer-light path into the accounts world.',
    profile: [
      'Vouching and pre-check of bills, bookkeeping scrutiny in departmental audit parties',
      'Local audit tours to offices within your circle — short, frequent, planned trips',
      'Preparing audit notes and compliance follow-ups under an AAO/Audit Officer',
      'In CGDA (defence accounts) formations, audit of defence bills and contracts',
    ],
    growth: [
      ['Auditor (Level 5)', 'entry post'],
      ['Senior Auditor (Level 6)', '≈ 3–5 years, by DPC'],
      ['AAO (Level 8)', 'via the departmental AAO/SAS exam or fresh CGL — this is the standard ladder'],
    ],
    goodFor:
      'You want a government accounts/audit career with a clear promotional exam (SAS) that can take you to the same AAO level as direct CGL recruits, and you prefer Light-transfer Group C stability.',
    watchOut: [
      'Starting pay (Level 5) is the second-lowest in CGL; the SAS exam is the reason to pick it',
      'Audit-party touring is not optional; planners of a strictly desk job should weigh it',
      'Offices are spread across states; asking for a specific city narrows your cadre choice',
    ],
  },
  accountant: {
    tagline: 'Run government accounts at Level 5 — bills, pensions and GPF in every central office.',
    about:
      'Accountant (also styled Junior Accountant) is a Group C post under C&AG, CGA and other accounting offices. Where auditors check accounts, accountants make them: pay bills, maintain GPF and pension records, and keep the books of central offices. It shares the Level 5 pay and the AAO ladder with Auditor.',
    profile: [
      'Preparation and checking of pay bills, TA bills and contingent bills of the office',
      'GPF, pension and gratuity case maintenance; reconciliation with the bank and PAO',
      'Budget and appropriation accounts support, monthly accounts compilation',
      'Almost entirely desk work; touring is rare compared with the audit cadre',
    ],
    growth: [
      ['Accountant (Level 5)', 'entry post'],
      ['Senior Accountant (Level 6)', '≈ 3–5 years, by DPC'],
      ['AAO (Level 8)', 'via departmental exam or fresh CGL'],
    ],
    goodFor:
      'You want the accounts career and the AAO ladder but with a nearly zero-travel desk job. Offices are in state capitals and district HQs, which helps people planning a home region.',
    watchOut: [
      'Month-end and year-end closing weeks are genuinely busy; the rest of the year is even',
      'Same Level 5 start as Auditor — choose by the work you prefer, not the pay',
      'Growth above Senior Accountant depends on clearing the departmental exam at some point',
    ],
  },
  ta: {
    tagline: 'The youngest entry point into the tax departments — Level 4, wide-open ladder ahead.',
    about:
      'Tax Assistant is a Group C post in CBDT (Income Tax) or CBIC (Customs/Excise/GST) offices. It is clerical-cum-data work in assessment or commissionerate offices, and because the entry age is 18, it is the post with the longest runway — many ITI/Inspector promotees began as TAs through the departmental exam.',
    profile: [
      'Data entry and scrutiny support in assessment wings; PAN/return matching in CBDT offices',
      'Dispatch, file movement, notices preparation support in commissionerates',
      'In CBIC, front-office and record work at customs divisions',
      'Pure desk work with fixed hours in most offices',
    ],
    growth: [
      ['Tax Assistant (Level 4)', 'entry post'],
      ['Upper Division Clerk / Head Clerk track (Level 4–5)', '≈ 3–6 years'],
      ['Inspector / ITO via departmental exams', 'the main reason to pick TA young'],
    ],
    goodFor:
      'Candidates entering at 18–21 who want to be inside the tax machinery early, learn it from the desk up, and then leap to Inspector/ITO through departmental exams while their CGL batchmates are still finishing probation elsewhere.',
    watchOut: [
      'Level 4 is the lowest CGL pay; the plan only works if you actually sit the departmental exams',
      'Choosing CBDT vs CBIC at preference time shapes which departmental ladder you get',
      'Work can be repetitive for years if you don\'t chase the exams',
    ],
  },
};

/** One shared "how the salary is built" table, by pay level. DA/HRA move with government revisions; treat as indicative for 2026. */
export function salaryRows(level: number): [string, string][] {
  const basic = { 8: 47600, 7: 44900, 6: 35400, 5: 29200, 4: 25500 }[level] ?? 0;
  const da = Math.round(basic * 0.58); // Dearness Allowance, indicative rate for 2026
  const hra = Math.round(basic * 0.3); // X-city rate; 20% Y-city, 10% Z-city; nil in quarters
  const ta = level >= 7 ? Math.round(3600 * 1.58) : Math.round(1350 * 1.58);
  const nps = Math.round((basic + da) * 0.1);
  return [
    ['Basic pay', `₹${basic.toLocaleString('en-IN')}`],
    ['Dearness Allowance (≈58%)', `₹${da.toLocaleString('en-IN')}`],
    ['HRA — X-city rate, 30% (nil in govt quarters)', `₹${hra.toLocaleString('en-IN')}`],
    ['Travelling allowance (city-dependent)', `≈ ₹${ta.toLocaleString('en-IN')}`],
    ['Gross (X-city, no quarters)', `≈ ₹${(basic + da + hra + ta).toLocaleString('en-IN')}`],
    ['Deductions — NPS 10% + CGHS etc.', `≈ −₹${(nps + 700).toLocaleString('en-IN')}`],
  ];
}
