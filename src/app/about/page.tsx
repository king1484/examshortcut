import type { Metadata } from 'next';
import Link from 'next/link';
import { contentStats } from '@/lib/content';

export const dynamic = 'force-static';
export const metadata: Metadata = { title: 'About ExamShortcut', description: 'ExamShortcut is an independent study website maintained by Vinay, with topic explanations, study guides and practice resources for Indian exam aspirants.', alternates: { canonical: '/about/' } };

export default function AboutPage() {
  const stats = contentStats();
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">About ExamShortcut</h1>
      <p className="mt-3">
        ExamShortcut is a preparation site for Indian government and entrance exams, starting with SSC CGL.
        All learning content is open to everyone. Log in to track your mock attempts, mistake notebook and progress,
        synced to your private account across devices.
      </p>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6 text-center">
        {[['Topics', stats.topics], ['Questions', stats.questions], ['Formulas', stats.formulas], ['Shortcut tricks', stats.tricks]].map(([k, v]) => (
          <div key={k as string} className="card p-4"><div className="text-2xl font-extrabold">{v as number}</div><div className="text-xs faint font-semibold uppercase mt-0.5">{k}</div></div>
        ))}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Built by Vinay</h2>
      <div className="card p-5 mt-3 text-sm space-y-3">
        <p>
          Hi, I&apos;m Vinay. I&apos;m a software engineer, and what I enjoy most is creating and shipping products that are genuinely helpful to the people who use them.
        </p>
        <p>
          ExamShortcut started from a problem I ran into myself. While looking into government-exam preparation, I struggled to find good content that was free
          and had everything in one place: the prep guides, the formulas and shortcuts, practice questions and the exam details. What I found was either
          scattered across many sites or kept behind a paywall. So I decided to build the thing I was looking for.
        </p>
        <p>
          I build and maintain the site myself. I write and review the material, fix mistakes when readers report them, and publish every change on the{' '}
          <Link className="underline" href="/updates/">updates log</Link>. The site is free, and it will stay focused on being useful to aspirants first.
        </p>
        <p>
          You can write to me at <a className="underline font-bold" href="mailto:singirikonda3@gmail.com">singirikonda3@gmail.com</a>, send a note through the{' '}
          <Link className="underline" href="/contact/">contact page</Link>, or find me on{' '}
          <a className="underline" href="https://www.instagram.com/vinni1484" target="_blank" rel="noopener">Instagram</a>. If a page here is wrong or unclear, I want to know.
        </p>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Where the content comes from</h2>
      <ul className="list-disc pl-5 mt-3 space-y-1.5 text-sm">
        <li><b>Exam data &amp; cutoffs</b> — compiled from notifications and result notices. Confirm the current rules with the official examining body.</li>
        <li><b>Notes, formulas, shortcuts</b> — original explanations written for this site.</li>
        <li><b>Practice questions &amp; tests</b> — a mixture of original exercises and imported previous-year or memory-based questions, identified in test descriptions. Worked solutions and software checks help catch errors, but do not guarantee that every answer is correct.</li>
        <li><b>Photographs</b> — real photographs on the exam pages come from Wikimedia Commons under open licences (CC0 or Creative Commons). The photographer, licence and source are credited under each image. We do not use AI-generated images.</li>
        <li><b>Current affairs</b> — exam-relevant events written up month by month in simple English.</li>
        <li><b>Shift analyses</b> — automatically compiled summaries of linked candidate reviews. Difficulty and attempt ranges are unofficial, with partial coverage labelled.</li>
      </ul>

      <h2 className="text-2xl font-extrabold mt-10">How we check content before and after it goes live</h2>
      <div className="card p-5 mt-3 text-sm space-y-2">
        <p>Every practice paper goes through an automated structural check before it is published: each question must have its options, a valid answer position, and a solution, and the stated answer must match the text of the keyed option. Papers that fail are fixed or held back.</p>
        <p>Where a paper&apos;s explanations followed the source too closely, we hold it back and rewrite the explanations in our own words before republishing. Garbled characters and stray text from imports are cleaned up when found.</p>
        <p>Shift analyses carry a Pending, Partial or Reported label, and any figure that fails a sanity check (for example, attempts larger than the section size) is withheld rather than guessed.</p>
        <p>Corrections are recorded on our <Link className="underline" href="/updates/">updates log</Link>.</p>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Who it is for and what we promise</h2>
      <ul className="list-disc pl-5 mt-3 space-y-1.5 text-sm">
        <li>Aspirants preparing for SSC, railway, banking, police and CAT exams who want clear topic notes, shortcut methods, and timed practice in one place.</li>
        <li>We explain the method, not just the answer, and say when a shortcut only works under certain conditions.</li>
        <li>We do not sell admit cards, guarantee selection, or ask for identity documents. We do not claim any affiliation with an examining body.</li>
        <li>We separate original material, imported previous-year questions, and automated summaries, so you know what you are reading.</li>
      </ul>

      <h2 className="text-2xl font-extrabold mt-10">Disclaimer</h2>
      <div className="card p-5 mt-3 text-sm space-y-2">
        <p>ExamShortcut is an <b>independent learning platform</b>. We are not affiliated with, endorsed by, or connected to any examining body (such as SSC, RRB, IBPS or UPSC) or any Government of India entity.</p>
        <p>Exam patterns, dates, vacancies and cutoffs change. Always confirm with the official notice of your exam before acting on anything you read here.</p>
        <p>Mock scores, normalisation bands and safe-score estimates are approximations for guidance, not predictions.</p>
      </div>

      <p className="text-sm muted mt-8">Read our <Link className="underline" href="/editorial-policy/">content sources and correction policy</Link>. Found a wrong answer or a bug? Tell us on the <Link className="underline" href="/contact/">contact page</Link>.</p>
    </div>
  );
}
