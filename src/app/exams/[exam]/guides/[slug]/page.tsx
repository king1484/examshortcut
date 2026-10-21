import { notFound } from 'next/navigation';
import { EXAMS } from '@/lib/exams';
import { getGuide, listGuides } from '@/lib/content';
import { ExamGuideArticle, examGuideMetadata } from '@/components/ExamGuideArticle';

export const dynamic = 'force-static';
export const dynamicParams = false;
export const generateStaticParams = () => EXAMS.filter(exam => exam.id !== 'ssc-cgl').flatMap(exam => listGuides(exam.id).map(guide => ({ exam: exam.id, slug: guide.id })));
type Params = Promise<{ exam: string; slug: string }>;
export async function generateMetadata({ params }: { params: Params }) {
  const { exam, slug } = await params;
  const guide = getGuide(slug, exam);
  return guide ? examGuideMetadata(exam, guide) : {};
}
export default async function GuidePage({ params }: { params: Params }) {
  const { exam, slug } = await params;
  const guide = getGuide(slug, exam);
  if (!guide || exam === 'ssc-cgl') notFound();
  return <ExamGuideArticle examId={exam} guide={guide} />;
}
