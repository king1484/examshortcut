import type { Metadata } from 'next';
import Link from 'next/link';
import { DailyQuiz } from '@/components/DailyQuiz';
import { DailyQuizGuide } from '@/components/topic-pages/DailyQuizGuide';
import { SECTION_META, SECTION_ORDER, type SectionId } from '@/lib/content';

export const dynamic = 'force-static';

export const metadata: Metadata = {
  title: 'Daily quiz — a fresh mix for SSC, Railway & entrance exams, every day',
  description: '20 exam questions every day across Quant, Reasoning, English, GK and Computer — tuned to the exam you\'re preparing for, with instant explanations and a daily streak.',
};

export default function DailyQuizPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <p className="text-xs font-bold uppercase tracking-wide mt-4" style={{ color: 'var(--brand)' }}>New every day</p>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-1">Daily quiz</h1>
      <p className="muted mt-2 text-[15px]">A fresh mixed set every day. Read the one-line shortcut after each question and keep your streak alive.</p>

      <div className="mt-6"><DailyQuiz /></div>

      <DailyQuizGuide />

      <section className="card p-5 mt-10">
        <h2 className="font-extrabold">Want more practice on one topic?</h2>
        <p className="text-sm muted mt-1">Every subject has full notes, question types and topic-wise practice sets.</p>
        <div className="flex flex-wrap gap-2 mt-3">
          {SECTION_ORDER.map((s) => {
            const m = SECTION_META[s as SectionId];
            return <Link key={s} href={`/${s}/`} className="btn text-sm" style={{ padding: '.35rem .75rem' }}><span style={{ color: m.color }} className="mr-1">{m.emoji}</span>{m.name}</Link>;
          })}
        </div>
      </section>
    </div>
  );
}
