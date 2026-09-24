export type SectionId = 'quant' | 'reasoning' | 'english' | 'ga' | 'computer';

export interface Question {
  id: string;
  q: string;
  figure?: string | null;
  options: string[];
  answer: number;
  solution: string;
  shortcut?: string | null;
  difficulty?: 'easy' | 'medium' | 'hard';
  subtopic?: string;
  pattern?: string;
  timeSec?: number;
  passage?: string;
  group?: string;
}

export interface Formula { name: string; tex: string; note?: string }
export interface Trick { title: string; body: string; example?: { q: string; solution: string } | null }

export interface Subtopic {
  id: string;
  title: string;
  concept: string;
  formulas?: Formula[];
  tricks?: Trick[];
  mistakes?: string[];
  /** Long-form lesson in markdown (### headings, KaTeX). */
  notes?: string;
  /** Every question type asked from this subtopic; practice questions point here via `pattern`. */
  patterns?: QuestionPattern[];
}

export interface QuestionPattern {
  id: string;
  name: string;
  frequency?: string;
  howToSpot?: string;
  formula?: string | null;
  logic?: string;
  example?: { q: string; solution: string } | null;
}

export interface PyqPattern {
  pattern: string; frequency?: string; howToSpot?: string; approach?: string;
  subtopic?: string; example?: { q: string; solution: string } | null;
}

export interface Topic {
  id: string;
  sectionId: SectionId;
  title: string;
  order: number;
  importance?: 'high' | 'medium' | 'low';
  avgQuestions?: { tier1?: number | null; tier2?: number | null };
  summary: string;
  subtopics: Subtopic[];
  pyqPatterns?: PyqPattern[];
  solvedExamples?: Question[];
  practice?: Question[];
}

export interface Section {
  id: SectionId;
  name: string;
  short: string;
  tier1: { questions: number; marks: number };
  tier2: { questions: number; marks: number };
  overview: string;
  strategy: string;
  topics: string[];
}

export interface MockSection { sectionId: SectionId; name: string; questions: Question[] }

export interface Mock {
  id: string;
  title: string;
  kind: 'full' | 'pyq-pattern';
  tier: 1 | 2;
  durationMin: number;
  plus: number;
  minus: number;
  blurb: string;
  open?: boolean;
  sections: MockSection[];
}

export interface Source { title: string; url: string }
