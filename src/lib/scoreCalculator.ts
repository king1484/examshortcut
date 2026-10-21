export interface CutoffEntry {
  year: number;
  list: string;
  cutoffs: Record<string, number>;
}

export function cutoffKey(entry: CutoffEntry): string {
  return `${entry.year}:${entry.list}`;
}

export function tier1CutoffEntries(data: { tier1?: CutoffEntry[] } | null): CutoffEntry[] {
  return [...(data?.tier1 ?? [])]
    .filter((entry) => entry.cutoffs && Object.keys(entry.cutoffs).length > 0)
    .sort((a, b) => b.year - a.year || Number(/all posts/i.test(b.list)) - Number(/all posts/i.test(a.list)) || a.list.localeCompare(b.list));
}

/** Answer counts are whole numbers, even when a number input accepts decimals. */
export function updateAnswerCounts(
  counts: { correct: number; wrong: number; total: number },
  field: 'correct' | 'wrong',
  value: number,
) {
  const next = { ...counts, [field]: Number.isFinite(value) ? Math.max(0, Math.min(Math.trunc(value), counts.total)) : 0 };
  if (next.correct + next.wrong > next.total) {
    if (field === 'correct') next.wrong = next.total - next.correct;
    else next.correct = next.total - next.wrong;
  }
  return next;
}
