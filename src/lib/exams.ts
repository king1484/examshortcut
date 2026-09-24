// Client-safe exam registry — NO node imports here (client components import this).
// Subjects (sections/topics) are shared by every exam; an exam only decides which
// subjects matter and brings its own pattern, cutoffs and mocks under /exams/<id>/.
import type { SectionId } from './sections';

export type ExamCategory = 'SSC' | 'Railways' | 'Banking' | 'Entrance' | 'Defence';

export interface ExamInfo {
  id: string;
  name: string;
  short: string;
  category: ExamCategory;
  sections: SectionId[];
  /** live = full exam hub (pattern, cutoffs, mocks). soon = subjects work now, exam hub coming. */
  status: 'live' | 'soon';
  blurb: string;
}

export const EXAMS: ExamInfo[] = [
  { id: 'ssc-cgl', name: 'SSC CGL', short: 'CGL', category: 'SSC', status: 'live',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: 'Graduate-level posts — Tier 1 + Tier 2, full mocks, cutoffs, post planner.' },
  { id: 'ssc-chsl', name: 'SSC CHSL', short: 'CHSL', category: 'SSC', status: 'soon',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: '12th-level posts — LDC, JSA, DEO.' },
  { id: 'ssc-mts', name: 'SSC MTS', short: 'MTS', category: 'SSC', status: 'soon',
    sections: ['reasoning', 'quant', 'english', 'ga'],
    blurb: 'Multi-Tasking Staff and Havaldar.' },
  { id: 'ssc-gd', name: 'SSC GD Constable', short: 'GD', category: 'SSC', status: 'soon',
    sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: 'Constables in CAPFs, NIA, SSF and Assam Rifles.' },
  { id: 'ssc-cpo', name: 'SSC CPO', short: 'CPO', category: 'SSC', status: 'soon',
    sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: 'Sub-Inspector in Delhi Police and CAPFs.' },
  { id: 'rrb-ntpc', name: 'RRB NTPC', short: 'NTPC', category: 'Railways', status: 'soon',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Railway non-technical graduate and undergraduate posts.' },
  { id: 'rrb-group-d', name: 'RRB Group D', short: 'Group D', category: 'Railways', status: 'soon',
    sections: ['quant', 'reasoning', 'ga'],
    blurb: 'Railway Level-1 posts.' },
  { id: 'ibps-po', name: 'IBPS PO', short: 'IBPS PO', category: 'Banking', status: 'soon',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: 'Probationary Officer in public sector banks.' },
  { id: 'sbi-po', name: 'SBI PO', short: 'SBI PO', category: 'Banking', status: 'soon',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: 'Probationary Officer, State Bank of India.' },
  { id: 'ibps-clerk', name: 'IBPS Clerk', short: 'Clerk', category: 'Banking', status: 'soon',
    sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: 'Clerical cadre in public sector banks.' },
  { id: 'cds', name: 'CDS', short: 'CDS', category: 'Defence', status: 'soon',
    sections: ['quant', 'english', 'ga'],
    blurb: 'Combined Defence Services — IMA, INA, AFA, OTA.' },
  { id: 'cuet-ug', name: 'CUET UG (General Test)', short: 'CUET', category: 'Entrance', status: 'soon',
    sections: ['quant', 'reasoning', 'english', 'ga'],
    blurb: 'General Test for central university admissions.' },
];

export const EXAM_CATEGORIES: ExamCategory[] = ['SSC', 'Railways', 'Banking', 'Defence', 'Entrance'];

export const getExamInfo = (id: string | null | undefined) => EXAMS.find((e) => e.id === id) ?? null;
