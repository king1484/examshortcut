/**
 * Splits a long intro into a short lead (kept under the page heading) and the rest
 * (shown lower on the page), so nothing is dropped and the content below the heading stays on screen.
 */
export function splitLead(text: string | undefined | null, max = 190): { lead: string; rest: string } {
  const t = (text ?? '').trim();
  if (!t) return { lead: '', rest: '' };
  const sentences = t.match(/[^.!?]+[.!?]+(?=\s|$)|[^.!?]+$/g) ?? [t];
  let lead = '';
  let used = 0;
  for (const s of sentences) {
    if (lead && (lead + s).length > max) break;
    lead += s;
    used += s.length;
    if (lead.length >= 80) break;
  }
  return { lead: lead.trim(), rest: t.slice(used).trim() };
}
