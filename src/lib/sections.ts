// Client-safe constants — NO node imports here (client components import this).
export type SectionId = 'quant' | 'reasoning' | 'english' | 'ga' | 'computer';

export const SECTION_ORDER: SectionId[] = ['quant', 'reasoning', 'english', 'ga', 'computer'];

export const SECTION_META: Record<SectionId, { name: string; short: string; emoji: string; color: string }> = {
  quant: { name: 'Quantitative Aptitude', short: 'Quant', emoji: '∑', color: 'var(--c-quant)' },
  reasoning: { name: 'General Intelligence & Reasoning', short: 'Reasoning', emoji: '◇', color: 'var(--c-reasoning)' },
  english: { name: 'English Comprehension', short: 'English', emoji: 'Aa', color: 'var(--c-english)' },
  ga: { name: 'General Awareness', short: 'GA', emoji: '◎', color: 'var(--c-ga)' },
  computer: { name: 'Computer Knowledge', short: 'Computer', emoji: '⌘', color: 'var(--c-computer)' },
};
