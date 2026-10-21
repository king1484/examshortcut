import Link from 'next/link';
import { UPDATE_LABELS, updateDate, type ExamUpdate } from '@/lib/examUpdateRules';
import { getExamInfo } from '@/lib/exams';

export function ExamUpdateCards({ items }: { items: ExamUpdate[] }) {
  return <div className="exam-update-cards">{items.map(item => <article className="card exam-update-card" key={item.slug}>
    <div className="flex flex-wrap gap-2 items-center"><span className="chip chip-brand">{UPDATE_LABELS[item.kind]}</span><span className="text-xs muted">{getExamInfo(item.examId)?.name}</span></div>
    <h3 className="mt-3 text-lg font-extrabold leading-snug"><Link href={`/exam-updates/${item.slug}/`}>{item.title}</Link></h3>
    <p className="muted text-sm mt-2">{item.summary}</p>
    <p className="text-xs muted mt-3">{item.status}{item.noticeDate ? ` · Notice: ${updateDate(item.noticeDate)}` : ''}</p>
    <div className="flex flex-wrap justify-between items-center gap-2 mt-4 text-sm"><span className="text-xs muted">Checked {updateDate(item.verifiedAt)}</span><Link className="font-bold underline underline-offset-4" href={`/exam-updates/${item.slug}/`}>Read update <span aria-hidden="true">→</span></Link></div>
  </article>)}</div>;
}
