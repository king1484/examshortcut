import type { Question } from './types';

export function wrongAnswerPenalty(question: Pick<Question, 'type' | 'negativeMarks'>, defaultPenalty: number): number {
  return question.type === 'numeric' ? 0 : (question.negativeMarks ?? defaultPenalty);
}

export function questionScore(question: Pick<Question, 'answer' | 'type' | 'negativeMarks'>, chosen: number | null, plus: number, minus: number): number {
  if (chosen === null) return 0;
  if (chosen === question.answer) return plus;
  const penalty = wrongAnswerPenalty(question, minus);
  return penalty === 0 ? 0 : -penalty;
}
