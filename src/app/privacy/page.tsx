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
      <p className="muted mt-2">Last updated: 4 October 2026</p>

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

          <h2 className="font-extrabold text-base">Analytics</h2>
          <p className="mt-1">
            We use <b>Google Analytics 4</b> to count visits and see which pages are useful. It sets first-party cookies (such as <code>_ga</code>) and
            receives your IP address (truncated by Google), browser, device type, approximate location (city level) and the pages you view. We use
            this only in aggregate to improve the site; we do not build profiles of individual visitors or combine it with your account.
            You can opt out with the <a className="underline" href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener noreferrer">Google Analytics opt-out add-on</a>.
          </p>

          <h2 className="font-extrabold text-base mt-4">What we collect otherwise</h2>
          <p className="mt-1">
            No newsletters and no sale of data. Like any website, our hosting provider (Cloudflare) may see standard technical request logs
            (IP address, browser type) for security and uptime — these are not used to profile you.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">Cookies and advertising</h2>
          <p className="mt-1">
            ExamShortcut may show advertising served by <b>Google AdSense</b>. Third-party vendors, including Google, use cookies to serve ads based on
            your prior visits to this or other websites. Google&apos;s use of advertising cookies enables it and its partners to serve ads to you based
            on your visit to this site and/or other sites on the internet. You can opt out of personalised advertising at{' '}
            <a className="underline" href="https://adssettings.google.com" target="_blank" rel="noopener noreferrer">Google Ads Settings</a>{' '}
            or at <a className="underline" href="https://www.aboutads.info" target="_blank" rel="noopener noreferrer">aboutads.info</a>, and you can
            control or delete cookies through your browser settings. See{' '}
            <a className="underline" href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener noreferrer">how Google uses data when you use our site</a>.
            Visitors from the EEA, UK and Switzerland are shown Google&apos;s consent choices before personalised ads or cookies are used.
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
