// Client-safe exam registry — NO node imports here (client components import this).
// Subjects (sections/topics) are shared by every exam; an exam only decides which
// subjects matter and brings its own pattern, cutoffs and mocks under /exams/<id>/.
// The list = the exams whose syllabus is >80% the shared maths / reasoning / English / GA subjects.
import type { SectionId } from './sections';

export type ExamCategory = 'SSC' | 'Railways' | 'MBA' | 'Banking' | 'Police';

export interface ExamBasics {
  conductingBody: string;
  eligibility: string;
  stages: string;
  /** applications in a recent cycle, with the cycle named */
  applicants: string;
}

export interface ExamInfo {
  id: string;
  name: string;
  short: string;
  category: ExamCategory;
  /** site subjects this exam tests; empty = none of our subjects map to it yet */
  sections: SectionId[];
  /** live = full exam hub (pattern, cutoffs, mocks). soon = listed with basic info, hub coming. */
  status: 'live' | 'soon';
  blurb: string;
  basics: ExamBasics;
  /** exam-specific section names (e.g. CAT: english → VARC); default = the shared subject name */
  sectionLabels?: Partial<Record<SectionId, string>>;
  /** exam-specific preparation advice per section; default = generic advice */
  sectionApproach?: Partial<Record<SectionId, string>>;
  /** topic ids to feature per section on the exam pattern page; default = topics flagged high-importance */
  sectionFocus?: Partial<Record<SectionId, string[]>>;
}

export const EXAMS: ExamInfo[] = [
  { id: 'ssc-cgl', name: 'SSC CGL', short: 'CGL', category: 'SSC', status: 'live',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: 'Graduate-level posts — Tier 1 + Tier 2, full mocks, cutoffs, post planner.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: 'Graduation',
      stages: 'Tier 1 CBT → Tier 2 CBT → document verification', applicants: '≈30 lakh a year' } },
  { id: 'ssc-chsl', name: 'SSC CHSL', short: 'CHSL', category: 'SSC', status: 'live',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: '12th-level posts — LDC, JSA, DEO.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: '12th pass',
      stages: 'Tier 1 CBT → Tier 2 CBT (with skill / typing test) → document verification',
      applicants: '30 lakh+ for 3,131 posts (2025)' } },
  { id: 'ssc-mts', name: 'SSC MTS', short: 'MTS', category: 'SSC', status: 'live',
    sections: ['reasoning', 'quant', 'english', 'ga'],
    blurb: 'Multi-Tasking Staff and Havaldar.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: '10th pass',
      stages: 'CBT → PET/PST (Havaldar only) → document verification',
      applicants: '36 lakh+ (recent cycle)' } },
  { id: 'ssc-gd', name: 'SSC GD Constable', short: 'GD', category: 'SSC', status: 'live',
    sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: 'Constables in CAPFs, NIA, SSF and Assam Rifles.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: '10th pass',
      stages: 'CBT → PET/PST → medical exam + document verification',
      applicants: '48.8 lakh (2026 exam)' } },
  { id: 'rrb-ntpc', name: 'RRB NTPC', short: 'NTPC', category: 'Railways', status: 'live',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Railway non-technical graduate and undergraduate posts.',
    basics: { conductingBody: 'Railway Recruitment Boards (RRBs)', eligibility: '12th pass (UG posts) or graduation (graduate posts)',
      stages: 'CBT 1 → CBT 2 → typing / aptitude test (post-wise) → document verification + medical',
      applicants: '1.21 crore, graduate + undergraduate combined (2025)' } },
  { id: 'rrb-group-d', name: 'RRB Group D', short: 'Group D', category: 'Railways', status: 'live',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Railway Level-1 posts.',
    basics: { conductingBody: 'Railway Recruitment Boards (RRBs)', eligibility: '10th pass or ITI',
      stages: 'CBT → physical efficiency test → document verification + medical',
      applicants: '1.08 crore (2025)' } },
  { id: 'rrb-alp', name: 'RRB ALP / Technician', short: 'ALP', category: 'Railways', status: 'soon',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Assistant Loco Pilot and Technician posts in Indian Railways.',
    basics: { conductingBody: 'Railway Recruitment Boards (RRBs)', eligibility: '10th pass + ITI in a notified trade / Act Apprenticeship, or 10th + 3-year engineering diploma (post-wise for Technician)',
      stages: 'CBT 1 → CBT 2 (Part A + B) → CBAT (ALP) → DV + medical',
      applicants: '22 lakh+ appeared in CBT 1 (2024 cycle)' } },
  { id: 'rrb-je', name: 'RRB JE', short: 'JE', category: 'Railways', status: 'soon',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Junior Engineers and technical posts in Indian Railways.',
    basics: { conductingBody: 'Railway Recruitment Boards (RRBs)', eligibility: 'Diploma or degree in the relevant engineering branch (B.Sc Physics + Chemistry for CMA)',
      stages: 'CBT 1 → CBT 2 (with Technical Abilities paper) → document verification + medical',
      applicants: '5.74 lakh applications (CEN 05/2025)' } },
  { id: 'cat', name: 'CAT', short: 'CAT', category: 'MBA', status: 'live',
    sections: ['english', 'reasoning', 'quant'],
    blurb: 'IIM MBA entrance — VARC, DILR and Quantitative Ability at full difficulty.',
    basics: { conductingBody: 'Indian Institutes of Management (IIMs)', eligibility: 'Bachelor\u2019s degree, 50% (45% for reserved categories); final-year students eligible',
      stages: 'CAT CBT → IIM shortlist → written ability / group discussion / interview',
      applicants: '≈3.3 lakh (2024)' },
    sectionLabels: {
      english: 'VARC — Verbal Ability & Reading Comprehension',
      reasoning: 'DILR — Data Interpretation & Logical Reasoning',
      quant: 'QA — Quantitative Ability',
    },
    sectionApproach: {
      english: 'VARC is roughly two-thirds reading comprehension (four passages of four questions each in CAT 2025), plus a handful of verbal-ability items (para-jumbles, summary, odd sentence out). Build reading speed and stamina first with daily long-form reading, then practise RC sets under a timer. Pick passages whose topic you can follow and leave the densest one for last; keep each passage near 8–10 minutes and treat verbal-ability questions as quick marks.',
      reasoning: 'DILR is a set-selection game, not a speed test: the section has about five sets and you will not finish all of them. Spend the first 3–4 minutes scanning every set, start with the one that looks easiest, and drop a set early if it is not opening up. Practise arrangements, scheduling, tables, bar and line charts, caselets and Venn problems, and always check the data carefully before answering the first question of a set.',
      quant: 'QA rewards a strong arithmetic base: percentages, ratio, time-speed-distance, time and work, profit and loss and mixtures are the biggest chunk, followed by algebra, geometry, number systems and modern maths. Learn the shortcut for each topic, then drill timed sets. Solve the quick questions first, skip anything that needs a long multi-step grind, and attempt every TITA, since TITA has no negative marking.',
    },
    sectionFocus: {
      english: ['reading-comprehension', 'paragraph-summary', 'sentence-rearrangement', 'cloze-test'],
      reasoning: ['seating-arrangement', 'order-ranking', 'syllogism', 'venn-diagrams', 'blood-relations', 'direction-distance'],
      quant: ['number-system', 'percentage', 'profit-loss-discount', 'time-speed-distance', 'time-work', 'algebra', 'geometry', 'permutation-combination'],
    } },
  { id: 'ssc-cpo', name: 'SSC CPO', short: 'CPO', category: 'SSC', status: 'live',
    sections: ['quant', 'reasoning', 'english', 'ga'],
    blurb: 'Sub-Inspectors in Delhi Police and CAPFs.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: 'Graduation + physical standards (PET/PST)',
      stages: 'Paper 1 CBT → PET/PST → Paper 2 CBT → detailed medical',
      applicants: '≈2.5 lakh (recent cycles)' } },
  { id: 'ibps-po', name: 'IBPS PO', short: 'IBPS PO', category: 'Banking', status: 'live',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: 'Probationary Management Trainees in public sector banks.',
    basics: { conductingBody: 'Institute of Banking Personnel Selection (IBPS)', eligibility: 'Graduation in any discipline',
      stages: 'Prelims CBT → Mains CBT → interview → provisional allotment',
      applicants: '≈8–10 lakh a year' } },
  { id: 'ibps-clerk', name: 'IBPS Clerk', short: 'Clerk', category: 'Banking', status: 'live',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: 'Customer Service Associates in public sector banks.',
    basics: { conductingBody: 'Institute of Banking Personnel Selection (IBPS)', eligibility: 'Graduation in any discipline; computer literacy preferred',
      stages: 'Prelims CBT → Mains CBT → provisional allotment (no interview)',
      applicants: '≈10–13 lakh a year' } },
  { id: 'sbi-clerk', name: 'SBI Clerk (Junior Associate)', short: 'SBI Clerk', category: 'Banking', status: 'soon',
    sections: ['english', 'quant', 'reasoning', 'computer'],
    blurb: 'Junior Associates in State Bank of India — prelims, mains, state-wise cutoffs.',
    basics: { conductingBody: 'State Bank of India (SBI)', eligibility: 'Graduation + local language proficiency', stages: 'Prelims CBT → Mains CBT → local language test → provisional selection', applicants: 'No official figure published by SBI (2026-27 cycle: 9,124 vacancies)' } },
  { id: 'sbi-po', name: 'SBI PO', short: 'SBI PO', category: 'Banking', status: 'soon',
    sections: ['english', 'quant', 'reasoning', 'computer'],
    blurb: 'Probationary Officers in State Bank of India — prelims, mains, interview.',
    basics: { conductingBody: 'State Bank of India (SBI)', eligibility: 'Graduation in any discipline', stages: 'Prelims CBT → Mains CBT (+ descriptive) → psychometric / GD / interview → provisional selection', applicants: 'No official figure published by SBI (2026-27 cycle: 1,500 vacancies)' } },
  { id: 'up-police', name: 'UP Police Constable', short: 'UP Police', category: 'Police', status: 'soon',
    sections: ['ga', 'english', 'quant', 'reasoning'],
    blurb: 'Constables in Uttar Pradesh Police — written exam, PET/PST, UP-specific GK.',
    basics: { conductingBody: 'Uttar Pradesh Police Recruitment and Promotion Board (UPPRPB)', eligibility: 'Intermediate (12th pass) + PET/PST standards', stages: 'Written exam (offline OMR) → PET/PST → document verification + medical', applicants: '≈28.86 lakh applied (June 2026 exam, 32,679 vacancies)' } },
];

export const EXAM_CATEGORIES: ExamCategory[] = ['SSC', 'Railways', 'MBA', 'Banking', 'Police'];

export const getExamInfo = (id: string | null | undefined) => EXAMS.find((e) => e.id === id) ?? null;

/** True when a subject belongs to the exam. */
export const examHasSection = (exam: ExamInfo | null, s: string) =>
  !exam || !exam.sections.length || exam.sections.includes(s as SectionId);
