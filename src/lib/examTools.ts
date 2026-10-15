/* Shared config for the generic per-exam tools (score calculator, rank estimator, salary calculator,
   normalisation calculator) under /exams/<exam>/. Client-safe: no fs, no network.

   Marking schemes mirror content/exams/<exam>/exam.json `stages` (each carries a lastVerified date).
   Anything that could not be confirmed from an official notice is flagged `verified: false` and the UI
   tells the reader to check the official notice instead of presenting it as fact. */

export type ToolKind = 'score-calculator' | 'rank-estimator' | 'salary-calculator' | 'normalisation-calculator';

export const TOOL_KINDS: ToolKind[] = ['score-calculator', 'rank-estimator', 'salary-calculator', 'normalisation-calculator'];

export const TOOL_META: Record<ToolKind, { label: string; blurb: string; emoji: string }> = {
  'score-calculator': { label: 'Score calculator', blurb: 'Marks from your attempts, with the real marking scheme', emoji: '🧮' },
  'rank-estimator': { label: 'Rank estimator', blurb: 'A planning estimate of percentile and rank', emoji: '📈' },
  'salary-calculator': { label: 'Salary calculator', blurb: 'Monthly in-hand pay for the post', emoji: '💰' },
  'normalisation-calculator': { label: 'Normalisation calculator', blurb: 'Estimate your normalised marks across shifts', emoji: '⚖️' },
};

/** Exams that get the generic tools. ssc-cgl and cat have their own hand-written ones. */
export const TOOL_EXAMS = ['ssc-chsl', 'ssc-mts', 'ssc-gd', 'ssc-cpo', 'rrb-ntpc', 'rrb-group-d', 'ibps-po', 'ibps-clerk', 'rrb-alp', 'rrb-je', 'sbi-po', 'sbi-clerk', 'up-police'] as const;

/** Multi-shift exams that normalise marks. IBPS, SBI and UP Police are not offered a normalisation tool: the
    IBPS and SBI notices do not describe any cross-shift adjustment, and the UP Police board's method is not
    confirmed from an official source. */
export const NORMALISING: Record<string, 'ssc' | 'rrb'> = {
  'ssc-chsl': 'ssc', 'ssc-mts': 'ssc', 'ssc-gd': 'ssc', 'ssc-cpo': 'ssc',
  'rrb-ntpc': 'rrb', 'rrb-group-d': 'rrb', 'rrb-alp': 'rrb', 'rrb-je': 'rrb',
};

/** A rank estimator needs an applicant or shortlist figure to anchor on, so it is offered only where RANK_CFG has one.
    SBI PO and SBI Clerk publish no cut-offs and no applicant counts on file, so they get none. */
export const hasTool = (id: string, kind: ToolKind) =>
  (TOOL_EXAMS as readonly string[]).includes(id)
  && (kind !== 'normalisation-calculator' || id in NORMALISING)
  && (kind !== 'rank-estimator' || id in RANK_CFG);

export const toolsFor = (id: string): ToolKind[] => TOOL_KINDS.filter((k) => hasTool(id, k));

export const toolPath = (id: string, kind: ToolKind) => `/exams/${id}/${kind}/`;

/** ids that have a given tool, for generateStaticParams */
export const examsWith = (kind: ToolKind) => TOOL_EXAMS.filter((id) => hasTool(id, kind));

/* ───────────────────────── score calculator config ───────────────────────── */

export interface SecDef {
  name: string;
  q: number;
  /** marks per question */
  mpq: number;
  /** marks lost per wrong answer */
  neg: number;
  mins?: number;
  /** false = the section is qualifying only and does not count towards merit marks */
  merit?: boolean;
}

export interface StageDef {
  id: string;
  label: string;
  sections: SecDef[];
  /** shown under the calculator */
  note: string;
  /** minimum qualifying percentage of the stage's marks, by category (official notice, before normalisation) */
  qualPct?: Record<string, number>;
  qualNote?: string;
  /** true when the stage is pass/fail only */
  qualifyingOnly?: boolean;
  /** which key of the server-side cutoff map to compare with (see examToolsServer) */
  cutStage?: string;
}

export interface ScoreCfg {
  schemeLine: string;
  stages: StageDef[];
  /** things we could not confirm; shown on the page */
  checkOfficial: string;
}

const SSC_QUAL = { UR: 30, OBC: 25, EWS: 25, SC: 20, ST: 20 };

export const SCORE_CFG: Record<string, ScoreCfg> = {
  'ssc-chsl': {
    schemeLine: 'Tier 1: 100 questions, 200 marks, +2 for a right answer, 0.5 off for a wrong one. Tier 2: +3 and 1 off.',
    checkOfficial: 'Tier 2 session details and the typing or skill test are in the official notice. Check it for the current year.',
    stages: [
      {
        id: 'tier1', label: 'Tier 1 (100 Q)', cutStage: 'tier1', qualPct: SSC_QUAL,
        sections: [
          { name: 'English Language', q: 25, mpq: 2, neg: 0.5, mins: 15 },
          { name: 'General Intelligence', q: 25, mpq: 2, neg: 0.5, mins: 15 },
          { name: 'Quantitative Aptitude', q: 25, mpq: 2, neg: 0.5, mins: 15 },
          { name: 'General Awareness', q: 25, mpq: 2, neg: 0.5, mins: 15 },
        ],
        note: 'Each section has its own 15 minute timer. Tier 1 is qualifying plus a shortlist: the real cut-off for Tier 2 runs well above the bare qualifying percentage.',
        qualNote: 'Minimum qualifying marks: 30% for UR, 25% for OBC and EWS, 20% for other categories. These are the bare minimums, not the shortlist cut-off.',
      },
      {
        id: 'tier2', label: 'Tier 2 (Sections I to III)',
        sections: [
          { name: 'Section I: Mathematical Abilities', q: 30, mpq: 3, neg: 1 },
          { name: 'Section I: Reasoning and General Intelligence', q: 30, mpq: 3, neg: 1 },
          { name: 'Section II: English Language and Comprehension', q: 40, mpq: 3, neg: 1 },
          { name: 'Section II: General Awareness', q: 20, mpq: 3, neg: 1 },
          { name: 'Section III: Computer Knowledge Test (qualifying)', q: 15, mpq: 3, neg: 1, merit: false },
        ],
        note: 'Merit uses Sections I and II only (360 marks). The computer test is qualifying. The typing or skill test (Section IV) is qualifying and depends on the post.',
      },
    ],
  },
  'ssc-mts': {
    schemeLine: 'Two sessions of 45 minutes. Session 1 is qualifying only, +3 per right answer and no negative marking. Session 2 decides merit, +3 and 1 off per wrong answer.',
    checkOfficial: 'Check the official notice for the current year, since SSC revises the MTS pattern from time to time.',
    stages: [
      {
        id: 's1', label: 'Session 1 (qualifying)', qualifyingOnly: true, qualPct: SSC_QUAL,
        sections: [
          { name: 'Numerical and Mathematical Ability', q: 20, mpq: 3, neg: 0 },
          { name: 'Reasoning Ability and Problem Solving', q: 20, mpq: 3, neg: 0 },
        ],
        note: 'Session 1 only has to be cleared. Its marks do not add to merit. SSC applies the qualifying percentage to normalised marks, so treat the verdict here as an estimate.',
        qualNote: 'Minimum qualifying marks: 30% for UR, 25% for OBC and EWS, 20% for SC and ST.',
      },
      {
        id: 's2', label: 'Session 2 (merit)',
        sections: [
          { name: 'General Awareness', q: 25, mpq: 3, neg: 1 },
          { name: 'English Language and Comprehension', q: 25, mpq: 3, neg: 1 },
        ],
        note: 'Session 2 marks decide the merit list. MTS has no Tier 2. Havaldar posts add a physical test.',
      },
    ],
  },
  'ssc-gd': {
    schemeLine: '80 questions, 160 marks, 60 minutes. +2 for a right answer, 0.25 off for a wrong one.',
    checkOfficial: 'Check the official notice for the current year, in case the scheme changes.',
    stages: [
      {
        id: 'cbt', label: 'CBE (80 Q)', cutStage: 'paper1',
        sections: [
          { name: 'General Intelligence and Reasoning', q: 20, mpq: 2, neg: 0.25 },
          { name: 'General Knowledge and General Awareness', q: 20, mpq: 2, neg: 0.25 },
          { name: 'Elementary Mathematics', q: 20, mpq: 2, neg: 0.25 },
          { name: 'English or Hindi', q: 20, mpq: 2, neg: 0.25 },
        ],
        note: 'The CBE decides the shortlist for the physical tests. Marks are normalised across shifts and NCC certificate holders get bonus marks, so your final score can differ from the raw one here.',
      },
    ],
  },
  'ssc-cpo': {
    schemeLine: 'Paper 1: 100 questions, 100 marks, +1 and 0.25 off, 15 minutes per section. Paper 2: 160 questions, 320 marks, +2 and 0.5 off.',
    checkOfficial: 'The 2026 pattern is new (Paper 1 was 200 questions till 2025). Check the official notice before relying on any number here.',
    stages: [
      {
        id: 'paper1', label: 'Paper 1 (100 Q)', cutStage: 'paper1', qualPct: SSC_QUAL,
        sections: [
          { name: 'General Intelligence and Reasoning', q: 25, mpq: 1, neg: 0.25, mins: 15 },
          { name: 'General Knowledge and General Awareness', q: 25, mpq: 1, neg: 0.25, mins: 15 },
          { name: 'Quantitative Aptitude', q: 25, mpq: 1, neg: 0.25, mins: 15 },
          { name: 'English Comprehension', q: 25, mpq: 1, neg: 0.25, mins: 15 },
        ],
        note: 'Paper 1 only shortlists you for the physical tests. Its marks do not count in the final merit. Earlier years had 200 marks, so old cut-offs are scaled to this paper by percentage.',
        qualNote: 'Minimum qualifying marks: 30% for UR, 25% for OBC and EWS, 20% for other categories.',
      },
      {
        id: 'paper2', label: 'Paper 2 (160 Q)',
        sections: [
          { name: 'General Intelligence and Reasoning', q: 20, mpq: 2, neg: 0.5 },
          { name: 'General Knowledge and General Awareness', q: 20, mpq: 2, neg: 0.5 },
          { name: 'Quantitative Aptitude', q: 20, mpq: 2, neg: 0.5 },
          { name: 'English Language and Comprehension', q: 100, mpq: 2, neg: 0.5 },
        ],
        note: 'Paper 2 is the merit paper for the final list.',
      },
    ],
  },
  'rrb-ntpc': {
    schemeLine: 'CBT 1: 100 questions. CBT 2: 120 questions. One mark per right answer, one third off per wrong answer, 90 minutes each.',
    checkOfficial: 'Typing test and CBAT rules depend on the post. Check the CEN notice for the current year.',
    stages: [
      {
        id: 'cbt1', label: 'CBT 1 (100 Q)', cutStage: 'cbt1', qualPct: { UR: 40, EWS: 40, OBC: 30, SC: 30, ST: 25 },
        sections: [
          { name: 'Mathematics', q: 30, mpq: 1, neg: 1 / 3 },
          { name: 'General Intelligence and Reasoning', q: 30, mpq: 1, neg: 1 / 3 },
          { name: 'General Awareness', q: 40, mpq: 1, neg: 1 / 3 },
        ],
        note: 'CBT 1 only shortlists you for CBT 2 and its marks do not carry into the final merit. There is no sectional timing.',
        qualNote: 'Qualifying percentages in the last cycle: 40% for UR and EWS, 30% for OBC and SC, 25% for ST. Actual shortlist cut-offs are zone-wise and run higher.',
      },
      {
        id: 'cbt2', label: 'CBT 2 (120 Q)',
        sections: [
          { name: 'Mathematics', q: 35, mpq: 1, neg: 1 / 3 },
          { name: 'General Intelligence and Reasoning', q: 35, mpq: 1, neg: 1 / 3 },
          { name: 'General Awareness', q: 50, mpq: 1, neg: 1 / 3 },
        ],
        note: 'CBT 2 marks decide merit. For posts with CBAT, merit is 70% CBT 2 and 30% CBAT.',
      },
    ],
  },
  'rrb-group-d': {
    schemeLine: '100 questions, 100 marks, 90 minutes. One mark per right answer, one third off per wrong answer.',
    checkOfficial: 'Check the CEN notice for the current cycle, as the paper language options and ratios can change.',
    stages: [
      {
        id: 'cbt', label: 'CBT (100 Q)', cutStage: 'cbt', qualPct: { UR: 40, EWS: 40, OBC: 30, SC: 30, ST: 30 },
        sections: [
          { name: 'General Intelligence and Reasoning', q: 30, mpq: 1, neg: 1 / 3 },
          { name: 'Mathematics', q: 25, mpq: 1, neg: 1 / 3 },
          { name: 'General Science', q: 25, mpq: 1, neg: 1 / 3 },
          { name: 'General Awareness and Current Affairs', q: 20, mpq: 1, neg: 1 / 3 },
        ],
        note: 'CBT marks, after normalisation, decide who is called for the physical test (PET). The PET is pass or fail.',
        qualNote: 'Minimum qualifying marks: 40% for UR and EWS, 30% for OBC, SC and ST. Actual cut-offs run far higher.',
      },
    ],
  },
  'ibps-po': {
    schemeLine: 'Prelims: 100 marks in 3 sections of 20 minutes each. Mains: 200 marks objective plus 25 marks descriptive. A wrong answer costs one quarter of that question\'s marks.',
    checkOfficial: 'IBPS announces the sectional cut-offs only in the result notice. Check it, and the exam notice, for the current year.',
    stages: [
      {
        id: 'prelims', label: 'Prelims (100 Q)', cutStage: 'prelims',
        sections: [
          { name: 'English Language', q: 30, mpq: 1, neg: 0.25, mins: 20 },
          { name: 'Quantitative Aptitude', q: 35, mpq: 30 / 35, neg: 0.25 * (30 / 35), mins: 20 },
          { name: 'Reasoning Ability', q: 35, mpq: 40 / 35, neg: 0.25 * (40 / 35), mins: 20 },
        ],
        note: 'Prelims is qualifying. Quant (35 questions for 30 marks) and Reasoning (35 questions for 40 marks) carry different marks per question, so the totals here come out as 30 and 40. Sectional cut-offs also apply.',
      },
      {
        id: 'mains', label: 'Mains objective (170 Q)', cutStage: 'mains',
        sections: [
          { name: 'Reasoning and Computer Aptitude', q: 40, mpq: 1.5, neg: 0.375, mins: 45 },
          { name: 'General, Economy and Banking Awareness', q: 50, mpq: 1.2, neg: 0.3, mins: 35 },
          { name: 'English Language', q: 40, mpq: 0.5, neg: 0.125, mins: 35 },
          { name: 'Data Analysis and Interpretation', q: 40, mpq: 1.5, neg: 0.375, mins: 45 },
        ],
        note: 'The descriptive paper (letter and essay, 25 marks, 30 minutes) is marked separately and not included here. The final score is 80% mains and 20% interview.',
      },
    ],
  },
  'ibps-clerk': {
    schemeLine: 'Prelims: 100 questions, 100 marks, +1 and 0.25 off, 20 minutes per section. Mains: 160 questions, 200 marks, 125 minutes. A wrong answer costs one quarter of that question\'s marks.',
    checkOfficial: 'IBPS announces the sectional cut-offs only in the result notice. Check it, and the exam notice, for the current year.',
    stages: [
      {
        id: 'prelims', label: 'Prelims (100 Q)', cutStage: 'prelims',
        sections: [
          { name: 'English Language', q: 30, mpq: 1, neg: 0.25, mins: 20 },
          { name: 'Numerical Ability', q: 35, mpq: 1, neg: 0.25, mins: 20 },
          { name: 'Reasoning Ability', q: 35, mpq: 1, neg: 0.25, mins: 20 },
        ],
        note: 'Prelims is qualifying, and the cut-off is state-wise. Sectional cut-offs also apply.',
      },
      {
        id: 'mains', label: 'Mains (160 Q)', cutStage: 'mains',
        sections: [
          { name: 'General and Financial Awareness', q: 40, mpq: 1.25, neg: 0.3125, mins: 20 },
          { name: 'English Language', q: 40, mpq: 1, neg: 0.25, mins: 35 },
          { name: 'Reasoning Ability and Computer Aptitude', q: 40, mpq: 1.5, neg: 0.375, mins: 35 },
          { name: 'Quantitative Aptitude', q: 40, mpq: 1.25, neg: 0.3125, mins: 35 },
        ],
        note: 'There is no interview for Clerk, so mains is the final merit. IBPS scales mains to 100 in the result, so compare with the cut-off by percentage.',
      },
    ],
  },
  /* CEN 01/2026 ALP. Source: content/exams/rrb-alp/exam.json (lastVerified 2026-10-06). */
  'rrb-alp': {
    schemeLine: 'CBT 1: 75 questions, 75 marks, 60 minutes. CBT 2: Part A of 100 questions in 90 minutes decides merit, and Part B (ITI trade) of 75 questions in 60 minutes is qualifying only. One mark per right answer, one third off per wrong answer.',
    checkOfficial: 'The 2026 CEN does not fix a question count for each CBT 1 subject area or for the Part A subjects, so each stage is entered as one block. The Part B marks and the 35% Part B qualifying line are taken from our exam page, not read from the CEN itself. The CBAT weighting has changed between cycles (70:30 earlier, 50:50 from CEN 01/2026). Check the CEN for the current year.',
    stages: [
      {
        id: 'cbt1', label: 'CBT 1 (75 Q)', cutStage: 'cbt1@75', qualPct: { UR: 40, EWS: 40, OBC: 30, SC: 30, ST: 25 },
        sections: [
          { name: 'All questions (Mathematics, Mental Ability, General Science)', q: 75, mpq: 1, neg: 1 / 3 },
        ],
        note: 'The CEN lists three subject areas but does not fix how many questions each carries, so enter your total right and wrong answers. The 60 minutes run as one block. CBT 1 marks are normalised across shifts and only shortlist you for CBT 2. They do not count in the final panel. The past cut-offs on file are RRB Secunderabad figures for one cycle, so zone and year change them.',
        qualNote: 'Minimum qualifying marks: 40% for UR and EWS, 30% for OBC-NCL and SC, 25% for ST. The actual shortlist cut-off is zone-wise and runs higher.',
      },
      {
        id: 'cbt2', label: 'CBT 2 (Part A 100 Q + Part B 75 Q)', cutStage: 'cbt1@100', qualPct: { UR: 40, EWS: 40, OBC: 30, SC: 30, ST: 25 },
        sections: [
          { name: 'Part A: Mathematics, Reasoning, Basic Science and Engineering', q: 100, mpq: 1, neg: 1 / 3, mins: 90 },
          { name: 'Part B: ITI trade (qualifying)', q: 75, mpq: 1, neg: 1 / 3, mins: 60, merit: false },
        ],
        note: 'Only Part A counts towards the CBAT shortlist, and only if you also clear Part B. Part B needs 35% for every category. The percentage check above applies to Part A. Final merit is 50% Part A and 50% CBAT from CEN 01/2026. Technician posts use a different single CBT (100 questions, 90 minutes) that this calculator does not cover.',
        qualNote: 'Part A minimum qualifying marks: 40% for UR and EWS, 30% for OBC-NCL and SC, 25% for ST. Part B: 35% for every category.',
      },
    ],
  },
  /* CEN 04/2026 JE/DMS/CMA. Source: content/exams/rrb-je/exam.json (lastVerified 2026-10-06). */
  'rrb-je': {
    schemeLine: 'CBT 1: 100 questions, 100 marks, 90 minutes. CBT 2: 150 questions, 120 minutes. One mark per right answer, one third off per wrong answer.',
    checkOfficial: 'The CBT 2 technical paper depends on your Exam Group, and the final list uses a Merit Index of 350 to 900, not raw marks. Check the CEN for the current year.',
    stages: [
      {
        id: 'cbt1', label: 'CBT 1 (100 Q)', cutStage: 'cbt1', qualPct: { UR: 40, EWS: 40, OBC: 30, SC: 30, ST: 25 },
        sections: [
          { name: 'Mathematics', q: 30, mpq: 1, neg: 1 / 3 },
          { name: 'General Intelligence and Reasoning', q: 25, mpq: 1, neg: 1 / 3 },
          { name: 'General Science (30) and General Awareness (15)', q: 45, mpq: 1, neg: 1 / 3 },
        ],
        note: 'CBT 1 is one 90 minute block with no sectional timing. Normalised CBT 1 marks only shortlist you for CBT 2, at 15 times the community-wise vacancies of the board, and do not count in the final merit. Cut-offs are zone-wise and post-category-wise, and the reference points on file are RRB Chandigarh figures.',
        qualNote: 'Minimum qualifying marks: 40% for UR and EWS, 30% for OBC-NCL and SC, 25% for ST. The actual shortlist cut-off for your post category is higher.',
      },
      {
        id: 'cbt2', label: 'CBT 2 (150 Q)', qualPct: { UR: 40, EWS: 40, OBC: 30, SC: 30, ST: 25 },
        sections: [
          { name: 'Common part: General Awareness', q: 15, mpq: 1, neg: 1 / 3 },
          { name: 'Common part: Physics and Chemistry', q: 15, mpq: 1, neg: 1 / 3 },
          { name: 'Common part: Basics of Computers and Applications', q: 10, mpq: 1, neg: 1 / 3 },
          { name: 'Common part: Environment and Pollution Control', q: 10, mpq: 1, neg: 1 / 3 },
          { name: 'Technical Abilities (your Exam Group)', q: 100, mpq: 1, neg: 1 / 3 },
        ],
        note: 'CBT 2 decides merit, but the board converts normalised marks to a Merit Index from 350 to 900 so that different branches compete on one list. So the raw total here cannot be compared with the Merit Index cut-offs, and no cut-off comparison is shown for this stage.',
        qualNote: 'Minimum qualifying marks are the same as CBT 1: 40% for UR and EWS, 30% for OBC-NCL and SC, 25% for ST.',
      },
    ],
  },
  /* Advertisement CRPD/PO/2026-27/09. Source: SBI detailed advertisement (sbi.bank.in/csfile/18062026_1_Detailed_Adv.2026.pdf),
     section 8, and content/exams/sbi-po/exam.json (lastVerified 2026-10-06). SBI publishes no cut-off figures. */
  'sbi-po': {
    schemeLine: 'Prelims: 100 questions, 100 marks, 60 minutes, 20 minutes per section. Mains objective: 170 questions, 200 marks, 3 hours, with a timer for every section. A wrong answer costs one quarter of that question\'s marks.',
    checkOfficial: 'SBI decides the sectional cut-offs and the minimum aggregate itself, and no past cut-off figures are on file, so this page does not compare your score with a cut-off. Check the advertisement for the current year.',
    stages: [
      {
        id: 'prelims', label: 'Prelims (100 Q)',
        sections: [
          { name: 'English Language', q: 40, mpq: 1, neg: 0.25, mins: 20 },
          { name: 'Quantitative Aptitude', q: 30, mpq: 1, neg: 0.25, mins: 20 },
          { name: 'Reasoning Ability', q: 30, mpq: 1, neg: 0.25, mins: 20 },
        ],
        note: 'Prelims is a shortlist only: about 10 times the category-wise vacancies go to Mains, from the aggregate. There is no sectional cut-off in Prelims, and Prelims marks are not added to the final merit.',
      },
      {
        id: 'mains', label: 'Mains objective (170 Q)',
        sections: [
          { name: 'Reasoning and Computer Aptitude', q: 40, mpq: 1.5, neg: 0.375, mins: 50 },
          { name: 'Data Analysis and Interpretation', q: 30, mpq: 2, neg: 0.5, mins: 45 },
          { name: 'General, Economy and Banking Awareness', q: 60, mpq: 1, neg: 0.25, mins: 45 },
          { name: 'English Language', q: 40, mpq: 0.5, neg: 0.125, mins: 40 },
        ],
        note: 'The descriptive test (30 marks, 30 minutes: email, situation analysis and a report or precis) is marked separately and not entered here. The objective and descriptive marks together (230) are scaled to 75, the group exercise and interview (50) to 25, and the final merit is out of 100. Each Mains section has its own minimum, set by the Bank, and about 3 times the category-wise vacancies go to the final phase.',
      },
    ],
  },
  /* Advertisement CRPD/CR/2026-27/17. Source: SBI Junior Associate detailed advertisement
     (sbi.bank.in/webfiles/uploads/files_2627/08/JA_2026_Detailed_Advt_Eng.pdf), section 4, and
     content/exams/sbi-clerk/exam.json (lastVerified 2026-10-06). SBI publishes no numeric cut-offs. */
  'sbi-clerk': {
    schemeLine: 'Prelims: 100 questions, 100 marks, 60 minutes, 20 minutes per section. Mains: 190 questions, 200 marks, 2 hours 40 minutes, with a timer for every section. A wrong answer costs one quarter of that question\'s marks.',
    checkOfficial: 'SBI sets the minimum aggregate for Mains in the result notice, and no past cut-off figures are on file, so this page does not compare your score with a cut-off. Check the advertisement for the current year.',
    stages: [
      {
        id: 'prelims', label: 'Prelims (100 Q)',
        sections: [
          { name: 'English Language', q: 30, mpq: 1, neg: 0.25, mins: 20 },
          { name: 'Numerical Ability', q: 35, mpq: 1, neg: 0.25, mins: 20 },
          { name: 'Reasoning Ability', q: 35, mpq: 1, neg: 0.25, mins: 20 },
        ],
        note: 'Prelims is a shortlist only. No minimum qualifying marks are fixed, about 10 times the category-wise vacancies go to Mains, and Prelims marks are not added to the final merit.',
      },
      {
        id: 'mains', label: 'Mains (190 Q)',
        sections: [
          { name: 'General and Financial Awareness', q: 50, mpq: 1, neg: 0.25, mins: 35 },
          { name: 'General English', q: 40, mpq: 1, neg: 0.25, mins: 35 },
          { name: 'Quantitative Aptitude', q: 50, mpq: 1, neg: 0.25, mins: 45 },
          { name: 'Reasoning Ability and Computer Aptitude', q: 50, mpq: 1.2, neg: 0.3, mins: 45 },
        ],
        note: 'Mains is the final merit, state-wise and category-wise, with no interview. Reasoning and Computer Aptitude carries 60 marks for 50 questions, so it is 1.2 marks per question here. SBI trained apprentices who meet the notice conditions get 5 extra marks on the aggregate, which is not added here. The local language test is qualifying.',
      },
    ],
  },
  /* Advertisement 07/2025. Source: content/exams/up-police/exam.json (lastVerified 2026-10-06). */
  'up-police': {
    schemeLine: 'One written paper: 150 questions, 2 marks each, 300 marks, 2 hours, OMR sheet, four subjects. The physical standard and efficiency tests are qualifying only.',
    checkOfficial: 'Not confirmed from the board\'s own notice: the number of questions in each subject (the 38, 37, 38, 37 split is from the previous cycle\'s paper) and the penalty for a wrong answer. Our exam page records 0.5 marks off for the previous cycle, and some secondary exam pages quote 0.25, so this calculator uses 0.5 and you should check the board notice at uppbpb.gov.in.',
    stages: [
      {
        id: 'written', label: 'Written exam (150 Q)', cutStage: 'written', qualPct: { UR: 30, OBC: 25, SC: 20, ST: 20 },
        sections: [
          { name: 'General Knowledge', q: 38, mpq: 2, neg: 0.5 },
          { name: 'General Hindi', q: 37, mpq: 2, neg: 0.5 },
          { name: 'Numerical and Mental Ability', q: 38, mpq: 2, neg: 0.5 },
          { name: 'Mental Aptitude, IQ and Reasoning', q: 37, mpq: 2, neg: 0.5 },
        ],
        note: 'Merit is built from written marks alone, category-wise, and the document, height and race tests only qualify. There is no sectional timing. The cut-offs on file are normalised marks shown for male and female candidates, so a raw score is only a rough guide against them. The 2025 cycle ran far higher than the 2023 cycle, so compare within a cycle.',
        qualNote: 'Minimum qualifying marks: 30% for Unreserved, 25% for OBC, 20% for SC and ST. A separate EWS figure is not stated in our notes, so no line is shown for EWS. Check the notice.',
      },
    ],
  },
};

/* ───────────────────────── rank estimator config ───────────────────────── */

export interface RankCfg {
  stageId: string;
  stageLabel: string;
  maxMarks: number;
  /** which cutoff stage supplies reference points */
  cutStage: string;
  applicants: number;
  applicantsVerified: boolean;
  appearedPct: number;
  appearedVerified: boolean;
  /** exact appeared count when one was published */
  appearedFixed?: number;
  /** shown under the appeared field instead of the default text when appearedFixed is set */
  appearedNote?: string;
  vacancies: number;
  /** number shortlisted divided by vacancies, or null when shortlistFixed is used */
  ratio: number;
  ratioVerified: boolean;
  ratioNote: string;
  shortlistFixed?: number;
  /** extra caution specific to this exam */
  caveat: string;
}

export const RANK_CFG: Record<string, RankCfg> = {
  'ssc-chsl': {
    stageId: 'tier1', stageLabel: 'Tier 1', maxMarks: 200, cutStage: 'tier1',
    applicants: 3069000, applicantsVerified: true, appearedPct: 36.1, appearedVerified: true, appearedFixed: 1107975,
    vacancies: 2536, ratio: 15.7, ratioVerified: true, shortlistFixed: 39901,
    ratioNote: 'In the 2025-26 cycle about 30.69 lakh applied, about 11.08 lakh appeared and 39,901 were shortlisted for Tier 2.',
    caveat: 'The cut-offs on file are from 2021 to 2023, while the numbers above are from the 2025-26 cycle. The anchor mixes the two, so edit it if you know a newer cut-off.',
  },
  'ssc-mts': {
    stageId: 's2', stageLabel: 'Session 2', maxMarks: 150, cutStage: 'none',
    applicants: 3620000, applicantsVerified: false, appearedPct: 22.2, appearedVerified: false,
    vacancies: 7948, ratio: 1, ratioVerified: false,
    ratioNote: 'Reported figures for MTS 2025: about 36.2 lakh applications and about 8.05 lakh appeared. Selection is state-wise and category-wise, so one all-India rank is only a rough stand-in. The ratio of 1 means the anchor is the last selected candidate.',
    caveat: 'There is no published all-India Session 2 cut-off on file, so enter the score you expect the last selected candidate to have.',
  },
  'ssc-gd': {
    stageId: 'cbt', stageLabel: 'CBE', maxMarks: 160, cutStage: 'paper1',
    applicants: 4880000, applicantsVerified: false, appearedPct: 60, appearedVerified: false,
    vacancies: 25487, ratio: 8, ratioVerified: false,
    ratioNote: 'About 8 times the vacancies are shortlisted for the physical tests, as per our exam page. The attendance figure is an assumption.',
    caveat: 'Cut-offs here are state-wise, area-wise and category-wise, and the paper is easy, so scores bunch up near the top. Treat a rank as very approximate.',
  },
  'ssc-cpo': {
    stageId: 'paper1', stageLabel: 'Paper 1', maxMarks: 100, cutStage: 'paper1',
    applicants: 250000, applicantsVerified: false, appearedPct: 60, appearedVerified: false,
    vacancies: 1871, ratio: 15, ratioVerified: false,
    ratioNote: 'The shortlist ratio for the physical test and the attendance are assumptions. Edit them if you have the official figures.',
    caveat: 'Old cut-offs were out of 200 and are scaled to this paper by percentage. The 2026 pattern is new, so the real distribution may look different.',
  },
  'rrb-ntpc': {
    stageId: 'cbt1', stageLabel: 'CBT 1', maxMarks: 100, cutStage: 'cbt1',
    applicants: 12100000, applicantsVerified: false, appearedPct: 55, appearedVerified: false,
    vacancies: 5165, ratio: 20, ratioVerified: true,
    ratioNote: 'Candidates are shortlisted for CBT 2 at 20 times the vacancies of each category. The attendance figure is an assumption.',
    caveat: 'Cut-offs are zone-wise (RRB-wise), so an all-India rank is a rough guide only. The reference points on file are example zones.',
  },
  'rrb-group-d': {
    stageId: 'cbt', stageLabel: 'CBT', maxMarks: 100, cutStage: 'cbt',
    applicants: 10800000, applicantsVerified: false, appearedPct: 55, appearedVerified: false,
    vacancies: 22195, ratio: 3, ratioVerified: false,
    ratioNote: 'About 3 times the vacancies are shortlisted for the PET, as per our exam page. The ratio can change with the railways\' requirement. The attendance figure is an assumption.',
    caveat: 'Cut-offs are zone-wise (RRC-wise), so an all-India rank is a rough guide only. The reference points on file are an example zone.',
  },
  'ibps-po': {
    stageId: 'prelims', stageLabel: 'Prelims', maxMarks: 100, cutStage: 'prelims',
    applicants: 900000, applicantsVerified: false, appearedPct: 60, appearedVerified: false,
    vacancies: 7565, ratio: 10, ratioVerified: false,
    ratioNote: 'IBPS does not publish how many were shortlisted for mains in advance. The ratio of 10 and the attendance are assumptions. Edit them.',
    caveat: 'IBPS prelims cut-offs are low (around half of the marks) because the paper is hard, so the curve is tighter than it looks. Sectional cut-offs also apply.',
  },
  'ibps-clerk': {
    stageId: 'prelims', stageLabel: 'Prelims', maxMarks: 100, cutStage: 'prelims',
    applicants: 1150000, applicantsVerified: false, appearedPct: 60, appearedVerified: false,
    vacancies: 11663, ratio: 10, ratioVerified: false,
    ratioNote: 'IBPS does not publish how many were shortlisted for mains in advance. The ratio of 10 and the attendance are assumptions. Edit them.',
    caveat: 'Clerk cut-offs are state-wise and the vacancies are spread across states, so an all-India rank says little about your own state. Pick your state in the reference list.',
  },
  'rrb-alp': {
    stageId: 'cbt1', stageLabel: 'CBT 1', maxMarks: 75, cutStage: 'cbt1@75',
    applicants: 2200000, applicantsVerified: false, appearedPct: 100, appearedVerified: false, appearedFixed: 2200000,
    appearedNote: 'About 22 lakh appeared in CBT 1 of the previous cycle (CEN 01/2024), as per press reports. No 2026 figure is on file, so this is a previous-cycle number. Edit it.',
    vacancies: 11127, ratio: 15, ratioVerified: true,
    ratioNote: 'Candidates are shortlisted for CBT 2 at 15 times the ALP vacancies (11,127 in CEN 01/2026), per our exam page. The attendance figure is from the previous cycle and is not confirmed.',
    caveat: 'Cut-offs are zone-wise (RRB-wise), so an all-India rank is a rough guide only. The reference point on file is one RRB Secunderabad cycle.',
  },
  'rrb-je': {
    stageId: 'cbt1', stageLabel: 'CBT 1', maxMarks: 100, cutStage: 'cbt1',
    applicants: 574402, applicantsVerified: false, appearedPct: 60, appearedVerified: false,
    vacancies: 4029, ratio: 15, ratioVerified: true,
    ratioNote: 'Candidates are shortlisted for CBT 2 at 15 times the community-wise vacancies (4,029 in CEN 04/2026), per our exam page, and the board can change this ratio. The applicant count (5,74,402) is from the previous cycle, CEN 05/2025, and the attendance figure is an assumption. Edit both.',
    caveat: 'Cut-offs are zone-wise and post-category-wise, and a JE shortlist is made per post category, so an all-India rank is a rough guide only. The reference points on file are RRB Chandigarh figures.',
  },
  'up-police': {
    stageId: 'written', stageLabel: 'written exam', maxMarks: 300, cutStage: 'written',
    applicants: 2886000, applicantsVerified: false, appearedPct: 76, appearedVerified: false, appearedFixed: 2190000,
    appearedNote: 'About 21.9 lakh appeared for the June 2026 written exam, as per dated news reports. The board\'s own figure may differ. Edit it.',
    vacancies: 32679, ratio: 2.3, ratioVerified: false, shortlistFixed: 76184,
    ratioNote: 'About 28.86 lakh applied, about 21.9 lakh appeared and about 76,184 were shortlisted for document verification and the physical tests, all from dated news reports and not from a board notice. The shortlist is made category-wise and gender-wise, so one overall rank is a rough stand-in.',
    caveat: 'The cut-offs on file are normalised marks and differ by category and gender. Pick the list that matches you in the reference list. The 2025 cycle ran far higher than the 2023 cycle.',
  },
};

/* ───────────────────────── normal distribution helpers ───────────────────────── */

function erf(x: number) {
  const s = x < 0 ? -1 : 1;
  const a = Math.abs(x);
  const t = 1 / (1 + 0.3275911 * a);
  const y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-a * a);
  return s * y;
}

/** standard normal CDF */
export const normCdf = (z: number) => 0.5 * (1 + erf(z / Math.SQRT2));

/** inverse of the standard normal CDF (Acklam's approximation) */
export function normInv(p: number) {
  const q0 = Math.min(Math.max(p, 1e-9), 1 - 1e-9);
  const a = [-3.969683028665376e1, 2.209460984245205e2, -2.759285104469687e2, 1.38357751867269e2, -3.066479806614716e1, 2.506628277459239];
  const b = [-5.447609879822406e1, 1.615858368580409e2, -1.556989798598866e2, 6.680131188771972e1, -1.328068155288572e1];
  const c = [-7.784894002430293e-3, -3.223964580411365e-1, -2.400758277161838, -2.549732539343734, 4.374664141464968, 2.938163982698783];
  const d = [7.784695709041462e-3, 3.224671290700398e-1, 2.445134137142996, 3.754408661907416];
  const lo = 0.02425;
  if (q0 < lo) {
    const q = Math.sqrt(-2 * Math.log(q0));
    return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1);
  }
  if (q0 > 1 - lo) {
    const q = Math.sqrt(-2 * Math.log(1 - q0));
    return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1);
  }
  const q = q0 - 0.5;
  const r = q * q;
  return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1);
}

/** piecewise-linear interpolation through (x, y) points sorted by x; clamps outside the range */
export function interp(points: [number, number][], x: number) {
  if (!points.length) return NaN;
  if (x <= points[0][0]) return points[0][1];
  for (let i = 1; i < points.length; i++) {
    const [x1, y1] = points[i];
    if (x <= x1) {
      const [x0, y0] = points[i - 1];
      return x1 === x0 ? y1 : y0 + ((x - x0) / (x1 - x0)) * (y1 - y0);
    }
  }
  return points[points.length - 1][1];
}

/* ───────────────────────── salary data ───────────────────────── */

/** Central government (7th CPC) rules used by the salary calculator. Review when DA or allowance orders change. */
export const CENTRAL = {
  /** DA as a percent of basic pay, in force from 1 January 2026 */
  da: 60,
  daAsOf: '1 January 2026',
  /** HRA percent of basic pay by city class, since DA crossed 50% */
  hra: { X: 30, Y: 20, Z: 10 } as Record<string, number>,
  /** transport allowance by pay level band: [higher TPTA cities, other places], before DA on it */
  transport: (level: number): [number, number] => (level <= 2 ? [1350, 900] : level <= 8 ? [3600, 1800] : [7200, 3600]),
  /** CGHS monthly contribution by pay level */
  cghs: (level: number) => (level <= 5 ? 250 : level === 6 ? 450 : level <= 11 ? 650 : 1000),
  /** employee NPS contribution, percent of basic plus DA */
  nps: 10,
};

export interface PayOption { level: number; basic: number }
export interface SalaryPost { key: string; name: string; options: PayOption[] }

/* ───────────────────────── cutoff reference points (built server-side from cutoffs.json) ───────────────────────── */

export interface CutScope { name: string; values: Record<string, number> }
export interface CutRef { id: string; label: string; list: string; maxMarks: number; scopes: CutScope[] }
