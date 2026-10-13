const reply = (status, body) => new Response(JSON.stringify(body), {
  status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
});

export function validateSubmission(value) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error('Please send a valid request.');
  if (value.website) throw new Error('Unable to accept this request.');
  if (!['feedback', 'feature'].includes(value.kind)) throw new Error('Choose feedback or a feature request.');
  if (typeof value.id !== 'string' || !/^[a-f\d]{8}-[a-f\d]{4}-4[a-f\d]{3}-[89ab][a-f\d]{3}-[a-f\d]{12}$/i.test(value.id)) throw new Error('Please refresh this page and try again.');
  const field = (name, min, max) => {
    const text = value[name] == null ? '' : value[name];
    if (typeof text !== 'string' || text.trim().length < min || text.trim().length > max) throw new Error(`Please check the ${name} field (${min}–${max} characters).`);
    return text.trim();
  };
  const title = field('title', 5, 100), message = field('message', 20, 3000);
  const email = field('email', 0, 254), exam = field('exam', 0, 60), page = field('page', 0, 500);
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw new Error('Please enter a valid reply email or leave it blank.');
  if (page) {
    let url; try { url = new URL(page); } catch { throw new Error('Please enter the full ExamShortcut page URL.'); }
    if (url.protocol !== 'https:' || !['examshortcut.in', 'www.examshortcut.in'].includes(url.hostname) || url.username || url.password) throw new Error('Please use an ExamShortcut page URL.');
  }
  return { id: value.id, kind: value.kind, title, message, email, exam, page };
}

export async function onRequest({ request, env }) {
  if (request.method !== 'POST') return reply(405, { error: 'Use the feedback form to submit a request.' });
  const origin = request.headers.get('Origin');
  if (origin !== new URL(request.url).origin) return reply(403, { error: 'Please submit from the ExamShortcut website.' });
  if (!request.headers.get('Content-Type')?.startsWith('application/json')) return reply(415, { error: 'Please use the feedback form.' });
  if (Number(request.headers.get('Content-Length')) > 16000) return reply(413, { error: 'Your request is too long.' });
  let data;
  try {
    const raw = await request.text();
    if (raw.length > 16000) return reply(413, { error: 'Your request is too long.' });
    data = validateSubmission(JSON.parse(raw));
  } catch (e) { return reply(400, { error: e instanceof Error ? e.message : 'Please check your request.' }); }
  if (!env.FEEDBACK_DB) return reply(503, { error: 'Submissions are temporarily unavailable. Please email singirikonda3@gmail.com.' });
  try {
    const now = new Date();
    // An hourly rotating hash limits abuse without retaining the raw IP address.
    const input = `${now.toISOString().slice(0, 13)}:${request.headers.get('CF-Connecting-IP') || 'local'}`;
    const hash = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input));
    const bucket = [...new Uint8Array(hash)].map(b => b.toString(16).padStart(2, '0')).join('');
    const existing = await env.FEEDBACK_DB.prepare('SELECT id FROM submissions WHERE id = ?').bind(data.id).first();
    if (existing) return reply(200, { id: data.id });
    const result = await env.FEEDBACK_DB.prepare(`INSERT INTO submissions (id, kind, title, message, exam, page, email, created_at, rate_bucket)
      SELECT ?, ?, ?, ?, ?, ?, ?, ?, ? WHERE (SELECT COUNT(*) FROM submissions WHERE rate_bucket = ?) < 5
      ON CONFLICT(id) DO NOTHING`).bind(data.id, data.kind, data.title, data.message, data.exam, data.page, data.email, now.toISOString(), bucket, bucket).run();
    if (!result.meta.changes) {
      const saved = await env.FEEDBACK_DB.prepare('SELECT id FROM submissions WHERE id = ?').bind(data.id).first();
      return saved ? reply(200, { id: data.id }) : reply(429, { error: 'Too many requests from this network. Please try again in an hour.' });
    }
    // Feedback stays private; old rate-limit identifiers are no longer needed.
    await env.FEEDBACK_DB.prepare("UPDATE submissions SET rate_bucket = NULL WHERE rate_bucket IS NOT NULL AND created_at < ?").bind(new Date(now.getTime() - 86400000).toISOString()).run();
    return reply(201, { id: data.id });
  } catch {
    return reply(503, { error: 'Could not save your request. Please retry or email singirikonda3@gmail.com.' });
  }
}
