// Issued ExamShortcut display units. No popunder, Smartlink, Social Bar or auto-refresh.
// Tina in Adsterra support confirmed the requested exclusions on 6 November.
// Honour the vendor's 15-minute propagation period before requesting any creative.
export const ADSTERRA_ENABLED = true;
export const ADSTERRA_CATEGORY_CONFIRMATION: string | null = '2026-11-06T12:42:50Z';
export const ADSTERRA_SERVE_AFTER = '2026-11-06T12:57:50Z';
export const ADSTERRA_FRAME_ORIGIN = 'https://examshortcut.pages.dev';
export const ADSTERRA_UNITS = {
  mobile: { zone: '31792398', width: 320, height: 50 },
  desktop: { zone: '31792399', width: 728, height: 90 },
  article: { zone: '31786624', width: 300, height: 250 },
} as const;
export type AdsterraUnit = keyof typeof ADSTERRA_UNITS;

export function canServeAdsterra(hostname: string, now = Date.now()): boolean {
  return ADSTERRA_ENABLED && Boolean(ADSTERRA_CATEGORY_CONFIRMATION)
    && now >= Date.parse(ADSTERRA_SERVE_AFTER)
    && ['examshortcut.in', 'www.examshortcut.in'].includes(hostname);
}

/** Deliberate reading-page allowlist: never a catch-all for an exam subtree. */
export function isAdsterraReadingPage(path: string): boolean {
  return path === '/'
    || /^\/(study-guides|exam-updates)(\/[^/]+)?\/?$/.test(path)
    || /^\/exams(\/[^/]+)?\/?$/.test(path)
    || /^\/exams\/[^/]+\/guides(\/[^/]+)?\/?$/.test(path)
    || /^\/(quant|reasoning|english|ga|computer)(\/[^/]+)?\/?$/.test(path)
    || /^\/(quant|reasoning|english|ga|computer)\/[^/]+\/(learn|formulas|examples)\/?$/.test(path)
    || /^\/exam-analysis(\/[^/]+){0,2}\/?$/.test(path)
    || path === '/current-affairs/' || /^\/current-affairs\/\d{4}\/?$/.test(path);
}

export function chooseAdsterraUnit(width: number, position: 'reading' | 'article'): AdsterraUnit | null {
  if (position === 'article') return width >= 300 ? 'article' : null;
  return width >= 728 ? 'desktop' : width >= 320 ? 'mobile' : null;
}
