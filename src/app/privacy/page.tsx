import type { Metadata } from 'next';
import Link from 'next/link';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Privacy policy',
  description: 'How ExamShortcut uses browser storage, optional account progress, hosting logs, Google Analytics and advertising technologies.',
};

export default function PrivacyPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">Privacy policy</h1>
      <p className="muted mt-2">Last updated: 14 October 2026</p>

      <div className="card p-5 mt-6 text-sm space-y-4">
        <div>
          <h2 className="font-extrabold text-base">The short version</h2>
          <p className="mt-1">
            Notes, study guides, the revision planner and open practice resources work <b>without an account</b>.
            Personal progress features use an optional account. Some tools save inputs in your browser; account progress can sync
            through Firebase. Google Analytics, advertising services and the hosting provider may receive technical visit data,
            even when you do not sign in.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">What stays on your device</h2>
          <p className="mt-1">
            Browser storage remembers settings, in-progress test drafts, revision-planner topics and some calculator inputs.
            Date of birth and category inputs in the posts checker are processed locally. The standalone revision planner is
            separate from account sync. Clearing site data removes these local records; export your revision calendar first if
            you want to keep its dates. Signed-in progress is also saved locally and may sync as described below.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">If you log in</h2>
          <p className="mt-1">
            Accounts are optional and free (Google sign-in or an email link). Logging in stores <b>your email address</b> and an
            account identifier and progress (scores, mistakes, saved questions, studied topics) using Google Firebase authentication
            and database services so your devices stay in sync. We do not sell your account data. Logging out stops account access
            but does not delete stored data. To request account-data deletion, contact us from the email associated with your account.
          </p>
          <h2 className="font-extrabold text-base mt-4">Optional public leaderboard</h2>
          <p className="mt-1">If you choose to join the leaderboard, your chosen display name and activity totals become public. Leaving removes your leaderboard entry. Keep personal information out of your display name.</p>

          <h2 className="font-extrabold text-base">Analytics</h2>
          <p className="mt-1">
            We use <b>Google Analytics 4</b> to count visits and see which pages are useful. It sets first-party cookies (such as <code>_ga</code>) and
            processes technical visit information including browser, device type, approximate location and pages viewed. Google states that GA4 does not log or store individual IP addresses. We use
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
            The site is intended for government-exam and entrance-exam aspirants. We do not knowingly create accounts for children under 13.
            If you believe a child has provided account information, contact us so we can review and remove it. Optional accounts,
            analytics and technical logs collect information as described above.
          </p>
        </div>

        <div>
          <h2 className="font-extrabold text-base">Feedback and feature requests</h2>
          <p className="mt-1">Our optional forms save your message, its title, any exam or page URL you provide, and an optional reply email in a private Cloudflare database. No account is required. We use this information to review your report or suggestion and contact you if needed; submissions are not posted publicly. A temporary hourly hash of the submitting network address limits spam without storing the raw address in the feedback database. Old rate-limit hashes are cleared when new submissions arrive. We keep reports while needed to resolve or assess them; contact us to request deletion, quoting your submission reference. Please do not send passwords or identity documents.</p>

          <h2 className="font-extrabold text-base mt-4">Questions</h2>
          <p className="mt-1">
            Anything about this policy — <Link className="underline" href="/contact/">write to us</Link>.
          </p>
        </div>
      </div>
    </div>
  );
}
