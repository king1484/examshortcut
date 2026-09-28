// Client-safe exam registry — NO node imports here (client components import this).
// Subjects (sections/topics) are shared by every exam; an exam only decides which
// subjects matter and brings its own pattern, cutoffs and mocks under /exams/<id>/.
// The list = India's 10 written exams with the most applicants (latest cycles, Sept 2026 check).
import type { SectionId } from './sections';

export type ExamCategory = 'SSC' | 'Railways' | 'Teaching' | 'Entrance';

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
  { id: 'ssc-chsl', name: 'SSC CHSL', short: 'CHSL', category: 'SSC', status: 'soon',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: '12th-level posts — LDC, JSA, DEO.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: '12th pass',
      stages: 'Tier 1 CBT → Tier 2 CBT (with skill / typing test) → document verification',
      applicants: '30 lakh+ for 3,131 posts (2025)' } },
  { id: 'ssc-mts', name: 'SSC MTS', short: 'MTS', category: 'SSC', status: 'soon',
    sections: ['reasoning', 'quant', 'english', 'ga'],
    blurb: 'Multi-Tasking Staff and Havaldar.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: '10th pass',
      stages: 'CBT → PET/PST (Havaldar only) → document verification',
      applicants: '36 lakh+ (recent cycle)' } },
  { id: 'ssc-gd', name: 'SSC GD Constable', short: 'GD', category: 'SSC', status: 'soon',
    sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: 'Constables in CAPFs, NIA, SSF and Assam Rifles.',
    basics: { conductingBody: 'Staff Selection Commission (SSC)', eligibility: '10th pass',
      stages: 'CBT → PET/PST → medical exam + document verification',
      applicants: '48.8 lakh (2026 exam)' } },
  { id: 'rrb-ntpc', name: 'RRB NTPC', short: 'NTPC', category: 'Railways', status: 'soon',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Railway non-technical graduate and undergraduate posts.',
    basics: { conductingBody: 'Railway Recruitment Boards (RRBs)', eligibility: '12th pass (UG posts) or graduation (graduate posts)',
      stages: 'CBT 1 → CBT 2 → typing / aptitude test (post-wise) → document verification + medical',
      applicants: '1.21 crore, graduate + undergraduate combined (2025)' } },
  { id: 'rrb-group-d', name: 'RRB Group D', short: 'Group D', category: 'Railways', status: 'soon',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Railway Level-1 posts.',
    basics: { conductingBody: 'Railway Recruitment Boards (RRBs)', eligibility: '10th pass or ITI',
      stages: 'CBT → physical efficiency test → document verification + medical',
      applicants: '1.08 crore (2025)' } },
  { id: 'ctet', name: 'CTET', short: 'CTET', category: 'Teaching', status: 'soon',
    sections: ['quant', 'english'],
    blurb: 'Central Teacher Eligibility Test — Paper 1 (classes 1–5), Paper 2 (classes 6–8).',
    basics: { conductingBody: 'CBSE', eligibility: '12th / graduation plus D.El.Ed or B.Ed (final-year students may apply)',
      stages: 'One written test per paper; qualifying certificate valid for life',
      applicants: '25.3 lakh (February 2026)' } },
  { id: 'neet-ug', name: 'NEET UG', short: 'NEET', category: 'Entrance', status: 'soon',
    sections: [],
    blurb: 'Single entrance test for MBBS, BDS, AYUSH and nursing seats.',
    basics: { conductingBody: 'National Testing Agency (NTA)', eligibility: '12th with Physics, Chemistry, Biology',
      stages: 'One pen-and-paper test → counselling (MCC / state)', applicants: '22.8 lakh (2025)' } },
  { id: 'jee-main', name: 'JEE Main', short: 'JEE Main', category: 'Entrance', status: 'soon',
    sections: [],
    blurb: 'Engineering entrance for NITs, IIITs and gateway to JEE Advanced.',
    basics: { conductingBody: 'National Testing Agency (NTA)', eligibility: '12th with Physics, Chemistry, Maths',
      stages: 'Two CBT sessions (best score counts) → JoSAA counselling', applicants: '15.4 lakh unique candidates (2025)' } },
  { id: 'cuet-ug', name: 'CUET UG', short: 'CUET', category: 'Entrance', status: 'soon',
    sections: ['quant', 'reasoning', 'english', 'ga'],
    blurb: 'Admission test for central and many state/private universities.',
    basics: { conductingBody: 'National Testing Agency (NTA)', eligibility: '12th pass (or appearing)',
      stages: 'One CBT: languages + domain subjects + optional General Test', applicants: '13.5 lakh (2024)' } },
];

export const EXAM_CATEGORIES: ExamCategory[] = ['SSC', 'Railways', 'Teaching', 'Entrance'];

export const getExamInfo = (id: string | null | undefined) => EXAMS.find((e) => e.id === id) ?? null;

/** True when a subject belongs to the exam. Exams none of our subjects map to (NEET, JEE) never filter. */
export const examHasSection = (exam: ExamInfo | null, s: string) =>
  !exam || !exam.sections.length || exam.sections.includes(s as SectionId);
