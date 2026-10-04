// Client-safe exam registry — NO node imports here (client components import this).
// Subjects (sections/topics) are shared by every exam; an exam only decides which
// subjects matter and brings its own pattern, cutoffs and mocks under /exams/<id>/.
// The list = the exams whose syllabus is >80% the shared maths / reasoning / English / GA subjects.
import type { SectionId } from './sections';

export type ExamCategory = 'SSC' | 'Railways' | 'MBA' | 'Banking';

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
  { id: 'cat', name: 'CAT', short: 'CAT', category: 'MBA', status: 'live',
    sections: ['english', 'reasoning', 'quant'],
    blurb: 'IIM MBA entrance — VARC, DILR and Quantitative Ability at full difficulty.',
    basics: { conductingBody: 'Indian Institutes of Management (IIMs)', eligibility: 'Bachelor\u2019s degree, 50% (45% for reserved categories); final-year students eligible',
      stages: 'CAT CBT → IIM shortlist → written ability / group discussion / interview',
      applicants: '≈3.3 lakh (2024)' } },
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
];

export const EXAM_CATEGORIES: ExamCategory[] = ['SSC', 'Railways', 'MBA', 'Banking'];

export const getExamInfo = (id: string | null | undefined) => EXAMS.find((e) => e.id === id) ?? null;

/** True when a subject belongs to the exam. */
export const examHasSection = (exam: ExamInfo | null, s: string) =>
  !exam || !exam.sections.length || exam.sections.includes(s as SectionId);
