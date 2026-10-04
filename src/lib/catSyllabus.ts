// Client-safe CAT section/topic reference shared by the CAT syllabus page and the CAT study planner.
// CAT has NO official published syllabus. The topic areas below are the ones that recur in past papers and in
// prep-portal syllabus guides (cross-checked 2026-10-04: Cracku, TopRankers, MBAUniverse, iQuanta, Hitbullseye).
// Treat them as "commonly tested areas", not an official list.

export type CatSecId = 'varc' | 'dilr' | 'qa';

export interface CatSecDef {
  id: CatSecId;
  /** matches stages[].sections[].sectionId in content/exams/cat/exam.json */
  sectionId: 'english' | 'reasoning' | 'quant';
  short: string;
  name: string;
  color: string;
  /** Plain-language description of the CAT 2025 composition, taken from exam.json stage notes. */
  composition: string;
  areas: { name: string; topics: string[] }[];
  /** Illustrative approach (NOT from official sources). */
  strategy: string[];
}

export const CAT_SECS: CatSecDef[] = [
  {
    id: 'varc', sectionId: 'english', short: 'VARC', name: 'Verbal Ability & Reading Comprehension', color: 'var(--c-english)',
    composition: 'CAT 2025: 4 reading-comprehension passages of 4 questions each, plus 8 verbal-ability items.',
    areas: [
      { name: 'Reading comprehension', topics: ['Main idea and central theme', 'Inference and implication', 'Author’s tone and attitude', 'Supporting / weakening arguments', 'Vocabulary-in-context'] },
      { name: 'Verbal ability', topics: ['Para jumbles (sentence ordering)', 'Para summary', 'Odd sentence out'] },
    ],
    strategy: [
      'The 40-minute lock is per section, so time not used in VARC cannot be carried into DILR or QA. Plan the section as a whole.',
      'Verbal-ability items are short, so many aspirants clear them first and then go to the passages. Whether that suits you is something to settle in mocks, not a rule.',
      'Wrong MCQs cost 1 mark; skipped questions cost nothing. Eliminate to two options before you commit.',
      'Any TITA question in this section has no negative marking, so always type in an answer.',
    ],
  },
  {
    id: 'dilr', sectionId: 'reasoning', short: 'DILR', name: 'Data Interpretation & Logical Reasoning', color: 'var(--c-reasoning)',
    composition: 'CAT 2025: about five sets, each with 4–5 questions.',
    areas: [
      { name: 'Data interpretation', topics: ['Tables', 'Bar, line and pie charts', 'Caselets', 'Data comparison and calculation-heavy sets'] },
      { name: 'Logical reasoning', topics: ['Arrangements (linear, circular, grid)', 'Games and tournaments', 'Venn diagrams and sets', 'Distribution / allocation puzzles', 'Networks and routes'] },
    ],
    strategy: [
      'Questions come in sets, so the choice of which sets to attempt matters more than speed. Spend the first few minutes scanning every set before committing.',
      'Abandon a set when you are stuck after the first couple of questions. Sunk time is the usual DILR mistake.',
      'TITA items carry no negative marking, so attempt them even when only partly sure.',
      'The on-screen basic calculator is the only calculator allowed. Practise with it.',
    ],
  },
  {
    id: 'qa', sectionId: 'quant', short: 'QA', name: 'Quantitative Ability', color: 'var(--c-quant)',
    composition: 'CAT 2025: arithmetic was the biggest chunk, followed by algebra, geometry, number systems and modern maths.',
    areas: [
      { name: 'Arithmetic', topics: ['Percentages, profit and loss', 'Ratio, proportion, averages', 'Time, speed, distance and work', 'Mixtures and alligation', 'Simple and compound interest'] },
      { name: 'Algebra', topics: ['Linear and quadratic equations', 'Inequalities', 'Progressions', 'Functions, logarithms and surds'] },
      { name: 'Geometry & mensuration', topics: ['Lines, angles, triangles', 'Circles', 'Polygons and quadrilaterals', 'Areas and volumes'] },
      { name: 'Number systems', topics: ['Divisibility, factors and remainders', 'HCF and LCM', 'Base systems'] },
      { name: 'Modern maths', topics: ['Permutations and combinations', 'Probability', 'Set theory'] },
    ],
    strategy: [
      'Since arithmetic was the largest block in CAT 2025, strong arithmetic accuracy is the base. Other areas add to it.',
      'Do a quick first pass for questions you can solve quickly, then return for the longer ones.',
      'Wrong MCQs cost 1 mark. TITA items cost nothing when wrong.',
      'Aim for accuracy first and speed second; sectional percentile minimums at most IIMs mean a lopsided score can disqualify you.',
    ],
  },
];

/** Concept-phase rotation lists used by the planner. */
export const CONCEPT_ROTATION: Record<CatSecId, string[]> = {
  varc: ['Reading comprehension: main idea and inference', 'Reading comprehension: tone, arguments, vocabulary-in-context', 'Para jumbles and odd sentence out', 'Para summary and mixed verbal sets'],
  dilr: ['Tables and charts (data interpretation)', 'Caselets and calculation-heavy sets', 'Arrangements and puzzles', 'Games, tournaments and Venn / sets'],
  qa: ['Arithmetic (percentages, ratios, speed-time-work)', 'Algebra (equations, inequalities, progressions)', 'Geometry and mensuration', 'Number systems', 'Modern maths (P&C, probability, sets)'],
};
