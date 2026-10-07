export type SectionId = 'quant' | 'reasoning' | 'english' | 'ga' | 'computer';

export interface Question {
  /** CAT TITA questions use the numeric answer directly, with no options. */
  type?: 'numeric';
  /** Session-specific penalty, e.g. SSC MTS qualifying versus merit sections. */
  negativeMarks?: number;
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
export interface Trick { title: string; body: string; example?: WorkedExample | null }

export interface Subtopic {
  id: string;
  title: string;
  concept: string;
  formulas?: Formula[];
  tricks?: Trick[];
  /** Plain string, or a wrong-way / right-way pair. */
  mistakes?: (string | Mistake)[];
  /** Long-form lesson in markdown (### headings, KaTeX). Each ### becomes a numbered section;
      `> **Rule:** …` / `> **Tip:** …` / `> **Note:** …` / `> **Example:** …` blockquotes render as callouts. */
  notes?: string;
  /** 3–6 one-line takeaways shown as the end-of-page revision checklist. */
  revision?: string[];
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
  /** Solution method as short ordered steps (preferred over numbered lines inside `logic`). */
  steps?: string[];
  /** One or two sentences on why the method works. */
  why?: string;
  example?: WorkedExample | null;
}

export interface Mistake { wrong: string; right: string }

export interface WorkedExample {
  q: string;
  /** Legacy single-paragraph solution; `steps` + `answer` are preferred. */
  solution?: string;
  steps?: string[];
  answer?: string;
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
  kind: 'full' | 'pyq-pattern' | 'real-pyq';
  tier: 1 | 2;
  durationMin: number;
  plus: number;
  minus: number;
  blurb: string;
  open?: boolean;
  /** owning exam id; omitted = ssc-cgl */
  exam?: string;
  sections: MockSection[];
}

export interface Source { title: string; url: string }
