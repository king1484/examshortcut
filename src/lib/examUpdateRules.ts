export const UPDATE_KINDS = ['result', 'admit-card', 'answer-key', 'schedule', 'application'] as const;
export type UpdateKind = typeof UPDATE_KINDS[number];
export const UPDATE_LABELS: Record<UpdateKind, string> = {
  result: 'Result', 'admit-card': 'Admit card', 'answer-key': 'Answer key', schedule: 'Exam dates', application: 'Application',
};
export interface ExamUpdate {
  slug: string;
  examId: string;
  kind: UpdateKind;
  title: string;
  summary: string;
  cycle: string;
  published: boolean;
  publishedAt: string;
  updatedAt: string;
  verifiedAt: string;
  noticeDate?: string;
  status: string;
  facts: { label: string; value: string }[];
  sections: { title: string; body: string }[];
  nextSteps: string[];
  sources: { label: string; url: string }[];
}

/** These links are selected from retrieved official pages; no arbitrary redirects or credentials. */
export function isOfficialUpdateUrl(value: string): boolean {
  try {
    const u = new URL(value);
    const host = u.hostname.toLowerCase();
    return u.protocol === 'https:' && !u.username && !u.password && !u.port &&
      (host.endsWith('.gov.in') || ['ibps.in', 'www.ibps.in', 'sbi.bank.in', 'iimcat.ac.in'].includes(host) ||
        (host === 'ibpsreg.ibps.in' && (u.pathname === '/csaxvijul26/' || u.pathname === '/sbijasrdjl26/oecla_oct26/login.php')) ||
        (host === 'rrb.digialm.com' && u.pathname.replace(/^\/+/, '/').startsWith('/EForms/configuredHtml/')));
  } catch { return false; }
}

export function filterExamUpdates(items: ExamUpdate[], query = '', examId = '', kind = ''): ExamUpdate[] {
  const words = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  return items.filter(item => item.published && (!examId || item.examId === examId) && (!kind || item.kind === kind) &&
    words.every(word => `${item.title} ${item.summary} ${item.cycle} ${item.examId}`.toLowerCase().includes(word)));
}

export function updateDate(value: string): string {
  return new Date(value.length === 10 ? `${value}T00:00:00+05:30` : value).toLocaleDateString('en-IN', {
    day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Asia/Kolkata',
  });
}
