import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { EXAMS, getExamInfo } from '@/lib/exams';
import { listGuides } from '@/lib/content';
import { ExamUpdatesForExam } from '@/components/ExamUpdatesForExam';

export const dynamic = 'force-static';
export const dynamicParams = false;
export const generateStaticParams = () => EXAMS.filter(exam => exam.id !== 'ssc-cgl' && listGuides(exam.id).length).map(exam => ({ exam: exam.id }));
type Params = Promise<{ exam: string }>;
export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam } = await params;
  const name = getExamInfo(exam)?.name;
  return { title: `${name} preparation and next-stage guides`, description: `Practical ${name} guides with original worked checks, revision decisions, official references and a checklist to save on your browser.`, alternates: { canonical: `/exams/${exam}/guides/` } };
}
export default async function GuidesIndex({ params }: { params: Params }) {
  const { exam } = await params;
  const info = getExamInfo(exam);
  const guides = listGuides(exam);
  if (!info || !guides.length || exam === 'ssc-cgl') notFound();
  return <div className="max-w-4xl mx-auto"><Link href={`/exams/${exam}/`} className="text-sm underline">← {info.name}</Link>
    <p className="kicker mt-5">Free guides · no login needed</p><h1 className="text-3xl sm:text-4xl font-extrabold mt-2">{info.name}: prepare for your next stage</h1>
    <p className="muted mt-4">Turn a notice or a mock result into a useful next step. Work through the examples, check the official references and save your action checklist.</p>
    <div className="grid sm:grid-cols-2 gap-4 mt-6">{guides.map(guide => <Link className="card p-5" key={guide.id} href={`/exams/${exam}/guides/${guide.id}/`}><h2 className="text-xl font-bold">{guide.title}</h2><p className="text-sm muted mt-3">{guide.description}</p><span className="block font-semibold mt-4">Read and try the checks →</span></Link>)}</div>
    <nav className="flex flex-wrap gap-3 mt-6" aria-label="Exam resources"><Link className="btn" href={`/exams/${exam}/exam-pattern/`}>Paper pattern</Link><Link className="btn" href={`/exams/${exam}/calendar/`}>Important dates</Link><Link className="btn" href="/study-guides/">Guides for every exam</Link></nav>
    <ExamUpdatesForExam examId={exam} />
  </div>;
}
