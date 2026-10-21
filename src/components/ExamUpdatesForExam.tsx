import Link from 'next/link';
import { listExamUpdates } from '@/lib/examUpdates';

export function ExamUpdatesForExam({ examId }: { examId: string }) {
  const items = listExamUpdates().filter(item => item.examId === examId);
  if (!items.length) return null;
  return <aside className="card p-5 mt-6" aria-label="Latest verified notices">
    <h2 className="font-extrabold text-lg">Latest results and notices</h2>
    <ul className="mt-3 space-y-3">{items.map(item => <li key={item.slug}>
      <Link className="font-semibold underline underline-offset-4" href={`/exam-updates/${item.slug}/`}>{item.title}</Link>
      <p className="text-sm muted mt-1">{item.cycle} · {item.status}</p>
    </li>)}</ul>
  </aside>;
}
