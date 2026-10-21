import { notFound } from 'next/navigation';
import { getGuide, listGuides } from '@/lib/content';
import { ExamGuideArticle, examGuideMetadata } from '@/components/ExamGuideArticle';
export const dynamic = 'force-static';
export const dynamicParams = false;
export const generateStaticParams = () => listGuides().map(guide => ({ slug: guide.id }));
type Params = Promise<{ slug: string }>;
export async function generateMetadata({ params }: { params: Params }) {
  const guide = getGuide((await params).slug);
  return guide ? examGuideMetadata('ssc-cgl', guide) : {};
}
export default async function GuidePage({ params }: { params: Params }) {
  const guide = getGuide((await params).slug);
  if (!guide) notFound();
  return <ExamGuideArticle examId="ssc-cgl" guide={guide} />;
}
