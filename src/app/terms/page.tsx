import type { Metadata } from 'next';
import Link from 'next/link';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Terms of use',
  description: 'The terms for using ExamShortcut: free educational use, no guarantee of exam results, content ownership, acceptable use and how to contact us.',
};

export default function TermsPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">Terms of use</h1>
      <p className="muted mt-2">Last updated: 15 October 2026</p>

      <div className="card p-5 mt-6 text-sm space-y-4">
        <div>
          <h2 className="font-extrabold text-base">Using ExamShortcut</h2>
          <p className="mt-1">
            ExamShortcut (examshortcut.in) is a free educational website for people preparing for Indian government and entrance exams.
            By using it you agree to these terms. If you do not agree, please do not use the site.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">No guarantee</h2>
          <p className="mt-1">
            Notes, formulas, practice questions, mock tests, shift analyses, cutoffs and calculators are study aids. We work to keep them accurate,
            but we give no guarantee that they are complete, current or error-free, and no guarantee about your performance or result in any exam.
            Read the <Link className="underline" href="/disclaimer/">disclaimer</Link> and always confirm dates, eligibility and rules on the exam
            conductor&apos;s official website.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Our content</h2>
          <p className="mt-1">
            The notes, explanations, original practice questions, layouts and code on this site belong to ExamShortcut. You may read, share links to
            and print pages for your own personal, non-commercial study. Please do not copy the site in bulk, republish its content elsewhere,
            or resell it, and do not scrape it in a way that burdens the servers.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Shift analyses and memory-based questions</h2>
          <p className="mt-1">
            Shift-wise exam analyses are compiled from candidate feedback and publicly available reports and are shown as indicative only.
            Memory-based questions are recalled by candidates and are not the official paper. We do not claim to provide
            an official complete paper for every practice test. Imported questions are identified in their test descriptions; third-party material belongs to its respective rights holders.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Copyright concerns and takedown</h2>
          <p className="mt-1">
            If you believe something on the site infringes your copyright, email{' '}
            <a className="underline" href="mailto:singirikonda3@gmail.com">singirikonda3@gmail.com</a> with the page URL, what you believe is yours and how to reach you.
            We will review the request promptly and remove or rewrite the material where it is justified.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Your account and data</h2>
          <p className="mt-1">
            Accounts are optional. You are responsible for activity under your login. How we handle data is described in the{' '}
            <Link className="underline" href="/privacy/">privacy policy</Link>.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Acceptable use</h2>
          <p className="mt-1">
            Do not attempt to break, overload or misuse the site, submit unlawful or abusive content through the contact form, or use the site in a
            way that violates any applicable law.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Advertising and external links</h2>
          <p className="mt-1">
            The site may display ads served by third parties such as Google AdSense. We do not control those advertisers and are not responsible
            for their products or sites. The same applies to any external site we link to.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Limitation of liability</h2>
          <p className="mt-1">
            To the extent permitted by law, ExamShortcut and its maintainer are not liable for any loss arising from use of, or reliance on, the
            site, including a missed deadline, a wrong date or an exam outcome.
          </p>
        </div>
        <div>
          <h2 className="font-extrabold text-base">Changes</h2>
          <p className="mt-1">
            We may update these terms or the site at any time; the date above shows the latest revision. Questions?{' '}
            <Link className="underline" href="/contact/">Contact us</Link>.
          </p>
        </div>
      </div>
    </div>
  );
}
