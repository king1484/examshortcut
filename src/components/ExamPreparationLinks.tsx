import Link from 'next/link';
import { listGuides } from '@/lib/content';
import { EXAMS, getExamInfo } from '@/lib/exams';

export function ExamPreparationLinks({ examId }: { examId: string }) {
  const guides = listGuides(examId);
  if (!guides.length) return null;
  return <aside className="card p-5 mt-6" aria-label="Preparation and next steps">
    <h2 className="text-lg font-extrabold">Prepare for your next stage</h2>
    <ul className="mt-3 space-y-3">{guides.slice(0, 3).map(guide => <li key={guide.id}>
      <Link className="underline font-semibold underline-offset-4" href={`/exams/${examId}/guides/${guide.id}/`}>{guide.title}</Link>
      <p className="text-sm muted mt-1">{guide.description}</p>
    </li>)}</ul>
    <Link className="btn mt-4" href={`/exams/${examId}/guides/`}>All {getExamInfo(examId)?.name} guides →</Link>
  </aside>;
}

export function AllExamPreparationLinks() {
  return <section id="exam-guides" className="mt-9" aria-label="Guides for every exam">
    <h2 className="text-2xl font-extrabold">Choose your exam and next stage</h2>
    <p className="muted mt-2">Practical guides for all {EXAMS.length} exams: worked checks, revision decisions and a checklist you can save.</p>
    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-4">{EXAMS.map(exam => {
      const guides = listGuides(exam.id);
      return guides.length ? <Link className="card p-5" key={exam.id} href={`/exams/${exam.id}/guides/`}>
        <p className="text-sm font-semibold" style={{ color: 'var(--brand-text)' }}>{exam.category}</p>
        <h3 className="font-extrabold text-lg mt-1">{exam.name}</h3>
        <p className="text-sm muted mt-2">{guides.find(g => g.checklist?.length)?.description ?? guides[0].description}</p>
        <span className="block font-semibold text-sm mt-3">Open guides →</span>
      </Link> : null;
    })}</div>
  </section>;
}
