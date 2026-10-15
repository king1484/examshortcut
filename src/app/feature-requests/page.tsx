import type { Metadata } from 'next';
import Link from 'next/link';
import { FeedbackForm } from '@/components/FeedbackForm';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Request a feature',
  description: 'Suggest a study tool, topic or improvement for ExamShortcut. Explain your preparation needs and submit a private feature request without login.',
};

export default function FeatureRequestsPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">What would make studying easier?</h1>
      <p className="muted mt-3">Request a missing topic, a study tool or a better way to use existing notes and revision features. A useful request explains the study problem and how the change would help you solve it.</p>
      <nav aria-label="Feedback options" className="flex flex-wrap gap-3 mt-5">
        <Link href="/feedback/" className="btn">Feedback & corrections</Link>
        <Link href="/feature-requests/" className="btn btn-brand" aria-current="page">Request a feature</Link>
      </nav>
      <FeedbackForm kind="feature" />
      <section className="card p-5 mt-5 text-sm space-y-3" aria-labelledby="fr-good">
        <h2 id="fr-good" className="font-extrabold text-base">How to write a request that gets built</h2>
        <p>Start with the problem, not the screen. &ldquo;I forget formulas a week after reading them&rdquo; tells more than &ldquo;add a flashcard page&rdquo;, because the same problem can often be fixed in a simpler way than the one you pictured.</p>
        <ul className="list-disc pl-5 space-y-1.5">
          <li><b>Name your exam and stage.</b> A tool that helps SSC CGL Tier 1 may not suit a bank clerk mains paper.</li>
          <li><b>Describe what you do today.</b> A spreadsheet, a notebook or another website tells us what the new feature has to beat.</li>
          <li><b>Say how often you would use it.</b> Daily tools get more weight than ones used once before an exam.</li>
        </ul>
      </section>

      <section className="card p-5 mt-4 text-sm space-y-3" aria-labelledby="fr-have">
        <h2 id="fr-have" className="font-extrabold text-base">Check what already exists</h2>
        <p>
          Many requests are for things that are already on the site. Before sending, look through the <Link className="underline" href="/exams/">exam hubs</Link> for mock tests, cutoffs, score calculators and rank estimators, the <Link className="underline" href="/learn/">topic notes</Link> for lessons and practice, the <Link className="underline" href="/revision-planner/">revision planner</Link> for spaced revision, and the <Link className="underline" href="/daily-quiz/">daily quiz</Link> for short daily practice. The <Link className="underline" href="/updates/">updates log</Link> lists what changed recently.
        </p>
      </section>

      <section className="card p-5 mt-4 text-sm space-y-2" aria-labelledby="fr-scope">
        <h2 id="fr-scope" className="font-extrabold text-base">What we will not build</h2>
        <p>
          ExamShortcut is a free study site. We do not handle applications, admit cards, fee payment or result checking, because only the exam body can do that. Requests for those are best taken to the official exam website.
        </p>
      </section>

      <div className="card p-5 mt-4 text-sm">
        <h2 className="font-extrabold">How we choose improvements</h2>
        <p className="muted mt-2">We look at how many students face the problem, whether the idea makes preparation clearer or more accessible, and what we can maintain well. Requests are reviewed privately; submitting one does not guarantee implementation or a release date.</p>
      </div>
    </div>
  );
}
