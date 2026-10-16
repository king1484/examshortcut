import type { Metadata, Viewport } from 'next';
import { Plus_Jakarta_Sans } from 'next/font/google';
import 'katex/dist/katex.min.css';
import './globals.css';
import { SiteHeader } from '@/components/SiteHeader';
import { SwRegister } from '@/components/SwRegister';
import { NavLoader } from '@/components/NavLoader';
import Link from 'next/link';
import Script from 'next/script';
import { AuthProvider } from '@/components/Auth';
import { Infolinks, InfolinksTextBoundary } from '@/components/Infolinks';

const sans = Plus_Jakarta_Sans({ subsets: ['latin'], variable: '--font-sans', display: 'swap' });

export const metadata: Metadata = {
  metadataBase: new URL('https://examshortcut.in'),
  title: { default: 'ExamShortcut — SSC, Railway, Banking & CAT Exam Preparation', template: '%s · ExamShortcut' },
  description:
    'Prepare for SSC, Railway, Banking and CAT exams: topic notes, shortcut tricks, practice sets, a daily quiz, full mocks, cutoffs and current affairs.',
  authors: [{ name: 'Vinay', url: 'https://www.instagram.com/vinni1484' }],
  creator: 'Vinay',
  other: { 'msvalidate.01': '97737EC02E19AF7CCACEDE49DAFF567A' },
  manifest: '/manifest.webmanifest',
  icons: { icon: '/icon.svg', apple: '/icon-192.png' },
  openGraph: {
    siteName: 'ExamShortcut',
    type: 'website',
    locale: 'en_IN',
    images: [{ url: '/og.png', width: 1200, height: 630, alt: 'ExamShortcut — exam preparation' }],
  },
  twitter: { card: 'summary_large_image', images: ['/og.png'] },
};

const GA4_ID = 'G-PGZ7PW2PYF';

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: '#f7f5f0' },
    { media: '(prefers-color-scheme: dark)', color: '#111318' },
  ],
};

const siteJsonLd = JSON.stringify({
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      '@id': 'https://examshortcut.in/#org',
      name: 'ExamShortcut',
      url: 'https://examshortcut.in/',
      logo: 'https://examshortcut.in/icon-512.png',
      founder: { '@id': 'https://examshortcut.in/#vinay' },
    },
    {
      '@type': 'Person',
      '@id': 'https://examshortcut.in/#vinay',
      name: 'Vinay',
      jobTitle: 'Software engineer',
      url: 'https://examshortcut.in/about/',
      sameAs: ['https://www.instagram.com/vinni1484'],
    },
  ],
});

const themeScript =`try{var t=localStorage.getItem('es-theme');if(t==='light'||t==='dark')document.documentElement.dataset.theme=t}catch(e){}`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-IN" className={sans.variable} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: siteJsonLd }} />
        <meta name="google-adsense-account" content="ca-pub-1700177065699672" />
      </head>
      <body className="min-h-screen flex flex-col">
        <AuthProvider>
        <InfolinksTextBoundary mode="off" />
        <SiteHeader />
        <InfolinksTextBoundary mode="on" />
        <main className="flex-1 w-full max-w-6xl mx-auto px-4 sm:px-6 py-6 sm:py-8">{children}</main>
        <InfolinksTextBoundary mode="off" />
        <footer className="border-t mt-10" style={{ borderColor: 'var(--line)' }}>
          <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8 text-sm faint space-y-3">
            <a
              href="https://t.me/examshortcutin"
              target="_blank"
              rel="noopener"
              aria-label="Join our Telegram channel for daily shortcut tricks"
              className="inline-flex items-center gap-2 rounded-full px-3.5 py-2 text-sm font-semibold text-white"
              style={{ backgroundColor: '#229ED9' }}
            >
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">
                <path d="M21.9 4.6c.3-1.2-.9-2.2-2-1.7L2.7 9.6c-1.2.5-1.2 2.2.1 2.6l4.4 1.4 1.7 5.4c.4 1.1 1.8 1.4 2.6.5l2.4-2.5 4.5 3.3c1 .8 2.5.2 2.7-1.1l2.8-14.6zM8.5 13.1l9.7-6.1c.2-.1.4.2.2.3l-8 7.4-.3 3.2-1.6-4.8z" />
              </svg>
              Join Telegram
            </a>
            <nav aria-label="Footer" className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-x-6 gap-y-5">
              <div><p className="font-bold muted mb-1.5">Exams</p><ul className="space-y-1.5">
                <li><Link href="/exams/">All exams</Link></li>
                <li><Link href="/exams/ssc-cgl/">SSC CGL</Link></li>
                <li><Link href="/exams/ssc-cgl/mocks/">Mock tests</Link></li>
                <li><Link href="/exams/ssc-cgl/cutoffs/">Cutoffs</Link></li>
                <li><Link href="/exams/ssc-cgl/score-calculator/">Score calculator</Link></li>
                <li><Link href="/exam-analysis/">Exam analysis</Link></li>
              </ul></div>
              <div><p className="font-bold muted mb-1.5">Subjects</p><ul className="space-y-1.5">
                <li><Link href="/learn/">Subjects &amp; notes</Link></li>
                <li><Link href="/quant/">Quantitative Aptitude</Link></li>
                <li><Link href="/reasoning/">Reasoning</Link></li>
                <li><Link href="/english/">English</Link></li>
                <li><Link href="/ga/">General Awareness</Link></li>
                <li><Link href="/computer/">Computer</Link></li>
              </ul></div>
              <div><p className="font-bold muted mb-1.5">Practice</p><ul className="space-y-1.5">
                <li><Link href="/daily-quiz/">Daily quiz</Link></li>
                <li><Link href="/current-affairs/">Current affairs</Link></li>
                <li><Link href="/formula-sheet/">Formula sheet</Link></li>
                <li><Link href="/shortcut-tricks/">Shortcut tricks</Link></li>
                <li><Link href="/data-interpretation/">Data interpretation</Link></li>
                <li><Link href="/vocab/">Vocab bank</Link></li>
                <li><Link href="/static-gk/">Static GK</Link></li>
              </ul></div>
              <div><p className="font-bold muted mb-1.5">Your study</p><ul className="space-y-1.5">
                <li><Link href="/study-guides/">Study guides</Link></li>
                <li><Link href="/revision-planner/">Revision planner</Link></li>
                <li><Link href="/dashboard/">My progress</Link></li>
                <li><Link href="/revision/">My revision</Link></li>
              </ul></div>
              <div><p className="font-bold muted mb-1.5">About</p><ul className="space-y-1.5">
                <li><Link href="/about/">About</Link></li>
                <li><Link href="/editorial-policy/">Content &amp; corrections</Link></li>
                <li><Link href="/updates/">Site updates</Link></li>
                <li><Link href="/contact/">Contact</Link></li>
                <li><Link href="/feedback/">Feedback &amp; corrections</Link></li>
                <li><Link href="/feature-requests/">Request a feature</Link></li>
                <li><Link href="/privacy/">Privacy</Link></li>
                <li><Link href="/terms/">Terms</Link></li>
                <li><Link href="/disclaimer/">Disclaimer</Link></li>
              </ul></div>
            </nav>
            <p>
              © {new Date().getFullYear()} ExamShortcut · Made with <span aria-label="love">❤️</span> by{' '}
              <a href="https://www.instagram.com/vinni1484" target="_blank" rel="noopener" className="underline">Vinay</a>
            </p>
          </div>
        </footer>
        <NavLoader />
        <SwRegister />
        <Infolinks />
        {/* lazyOnload: gtag.js is ~170 KB and ~0.8 s of main-thread work on mobile; load it after the page is idle */}
        <Script src={`https://www.googletagmanager.com/gtag/js?id=${GA4_ID}`} strategy="lazyOnload" />
        <Script id="ga4" strategy="lazyOnload">
          {`window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','${GA4_ID}');`}
        </Script>
        </AuthProvider>
      </body>
    </html>
  );
}
