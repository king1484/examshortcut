import type { Metadata } from 'next';
import Link from 'next/link';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Disclaimer',
  description: 'ExamShortcut is an independent study site, not affiliated with SSC, RRB, or any government body. Always verify exam dates, eligibility and cutoffs on the official website.',
};

export default function DisclaimerPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">Disclaimer</h1>
      <p className="muted mt-2">Last updated: 15 October 2026</p>

      <div className="card p-5 mt-6 text-sm space-y-4">
        <div>
          <h2 className="font-extrabold text-base">We are not an official site</h2>
          <p className="mt-1">
            ExamShortcut is an independent educational website. It is <b>not affiliated with, endorsed by or connected to</b> the Staff Selection
            Commission (SSC), the Railway Recruitment Boards (RRB), the Government of India or any other exam-conducting body. Names of exams are
            used only to describe what the study material is for.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Verify before you act</h2>
          <p className="mt-1">
            Exam patterns, dates, vacancies, fees, eligibility rules and cutoffs change, and notices can be corrected after publication. Every page
            shows the information as we last checked it. <b>Always confirm against the official notification</b> (for SSC: ssc.gov.in; for RRB: the
            regional RRB sites and indianrailways.gov.in) before applying, paying a fee or making a decision.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Study material, not a promise</h2>
          <p className="mt-1">
            Notes, shortcuts, practice questions, mocks and calculators are made to help you practise. Mock scores, rank estimates and cutoff
            predictions are indicative and do not predict your actual result. Practice questions are original and modelled on recurring patterns; they
            are not the official papers.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Shift analysis and memory-based content</h2>
          <p className="mt-1">
            Shift-wise difficulty ratings, &ldquo;good attempts&rdquo; figures and questions recalled by candidates are compiled from candidate feedback
            and publicly shared reports. They are subjective, may differ from your own experience, and are not official figures. Where data is thin
            or unconfirmed, the page says so.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Not professional advice</h2>
          <p className="mt-1">
            Study plans, score targets and strategy tips are general guidance from one maintainer, not career, legal or financial advice. How you prepare, and which
            exams you apply for, is your own decision.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Advertising and external links</h2>
          <p className="mt-1">
            The site may show ads served by Adcash or Google AdSense, and ads are never presented as study content or as a recommendation. Links to other websites, including
            official exam sites, are provided for convenience; we do not control their content or availability. See the{' '}
            <Link className="underline" href="/privacy/">privacy policy</Link> for how ads and cookies work.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Errors and corrections</h2>
          <p className="mt-1">
            Found a mistake? Please <Link className="underline" href="/contact/">tell us</Link> and we will correct it. See also the{' '}
            <Link className="underline" href="/terms/">terms of use</Link> and <Link className="underline" href="/privacy/">privacy policy</Link>.
          </p>
        </div>
      </div>
    </div>
  );
}
