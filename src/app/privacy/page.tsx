import type { Metadata } from 'next';
import Link from 'next/link';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Privacy policy',
  description: 'What ExamShortcut stores (and does not store): studying is open without an account and your data stays on your device; if you choose to log in, only your email and your progress sync — nothing is sold or profiled.',
};

export default function PrivacyPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">Privacy policy</h1>
      <p className="muted mt-2">Last updated: 24 September 2026</p>

      <div className="card p-5 mt-6 text-sm space-y-4">
        <div>
          <h2 className="font-extrabold text-base">The short version</h2>
          <p className="mt-1">
            All notes, practice, calculators and open mocks work <b>without an account</b>. Without logging in, your progress —
            mock attempts, mistake notebook, study plan, eligibility inputs — is saved <b>only in your own browser</b> and we never
            receive a copy. A free login exists for one reason only: to sync that same progress across your devices.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">What stays on your device</h2>
          <p className="mt-1">
            Without an account, the site uses your browser&apos;s local storage to remember your progress between visits: mock attempts and analysis,
            your score entries, your study-plan ticks, your date of birth and category <i>if</i> you choose to enter them in the
            posts checker, and your typing-test history. This data never leaves your device — it is not transmitted to us or to
            anyone else. Clearing your browser data for this site erases it permanently; there is no server copy to restore.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">If you log in</h2>
          <p className="mt-1">
            Accounts are optional and free (Google sign-in or an email link). Logging in stores <b>your email address</b> and a
            copy of your progress (scores, mistakes, saved questions, studied topics) with our authentication provider so your
            devices stay in sync. We do not sell it, share it, or use it to profile you, and you can erase it any time by logging
            out and asking us to delete your account data.
          </p>

          <h2 className="font-extrabold text-base">What we collect otherwise</h2>
          <p className="mt-1">
            Nothing beyond the above. No analytics profile, no advertising identifier, no newsletters.
            Like any website, our hosting provider may see standard technical request logs (IP address, browser type) for security
            and uptime — these are not used to profile you.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">Cookies and advertising</h2>
          <p className="mt-1">
            ExamShortcut sets no tracking cookies today. If advertising is shown on the site in future, third-party vendors,
            including Google, may use cookies to serve ads based on your prior visits to this or other websites. You can opt out
            of personalised advertising at <a className="underline" href="https://adssettings.google.com" target="_blank" rel="noopener noreferrer">Google Ads Settings</a>,
            or control cookies through your browser settings. Any such change will be reflected on this page.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">Offline use (PWA)</h2>
          <p className="mt-1">
            If you install ExamShortcut as an app, a service worker stores the site&apos;s pages on your device so it works offline.
            That cache contains only the site itself — not your data, which stays in local storage as described above.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">Children</h2>
          <p className="mt-1">
            The site is intended for exam aspirants and does not knowingly collect any personal information from anyone, including
            children under 13.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">Questions</h2>
          <p className="mt-1">
            Anything about this policy — <Link className="underline" href="/contact/">write to us</Link>.
          </p>
        </div>
      </div>
    </div>
  );
}
