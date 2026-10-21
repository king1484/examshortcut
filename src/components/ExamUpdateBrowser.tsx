'use client';
import { useMemo, useState } from 'react';
import { filterExamUpdates, UPDATE_LABELS, UPDATE_KINDS, type ExamUpdate, type UpdateKind } from '@/lib/examUpdateRules';
import { ExamUpdateCards } from './ExamUpdateCards';
import { getExamInfo } from '@/lib/exams';

export function ExamUpdateBrowser({ items, resultsOnly = false, kindOnly }: { items: ExamUpdate[]; resultsOnly?: boolean; kindOnly?: UpdateKind }) {
  const [query, setQuery] = useState('');
  const [exam, setExam] = useState('');
  const [kind, setKind] = useState('');
  const exams = [...new Set(items.map(item => item.examId))].sort();
  const shown = useMemo(() => filterExamUpdates(items, query, exam, kindOnly ?? (resultsOnly ? 'result' : kind)), [items, query, exam, kind, resultsOnly, kindOnly]);
  return <>
    <div className="exam-update-filters card p-4 mt-6">
      <label className="text-sm font-semibold">Search updates<input className="exam-update-input mt-1" type="search" placeholder="Exam, result or recruitment cycle" value={query} onChange={e => setQuery(e.target.value)} /></label>
      <label className="text-sm font-semibold">Exam<select className="exam-update-input mt-1" value={exam} onChange={e => setExam(e.target.value)}><option value="">All exams</option>{exams.map(id => <option key={id} value={id}>{getExamInfo(id)?.name ?? id}</option>)}</select></label>
      {!resultsOnly && !kindOnly && <label className="text-sm font-semibold">Update type<select className="exam-update-input mt-1" value={kind} onChange={e => setKind(e.target.value)}><option value="">All updates</option>{UPDATE_KINDS.map(id => <option key={id} value={id}>{UPDATE_LABELS[id]}</option>)}</select></label>}
    </div>
    <p className="muted text-sm my-4" role="status">{shown.length} {shown.length === 1 ? 'update' : 'updates'}{query || exam || kind ? ' matching your filters' : ' published'}</p>
    {shown.length ? <ExamUpdateCards items={shown} /> : <div className="card p-6"><h2 className="font-bold">No published update matches these filters</h2><p className="muted mt-2">Try another exam or a shorter search. We add a release only after checking its official source.</p><button className="btn mt-4" onClick={() => { setQuery(''); setExam(''); setKind(''); }}>Clear filters</button></div>}
  </>;
}
