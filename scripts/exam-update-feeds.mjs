const escape = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&apos;');
export function buildExamUpdateRss(items) {
  const published = items.filter(item => item.published).sort((a, b) => b.publishedAt.localeCompare(a.publishedAt));
  const entries = published.map(item => {
    const url = `https://examshortcut.in/exam-updates/${item.slug}/`;
    return `<item><title>${escape(item.title)}</title><link>${url}</link><guid isPermaLink="true">${url}</guid><pubDate>${new Date(item.publishedAt).toUTCString()}</pubDate><category>${escape(item.kind)}</category><description>${escape(item.summary)}</description></item>`;
  });
  const newest = published.map(item => item.updatedAt).sort().at(-1);
  return `<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>ExamShortcut exam updates</title><link>https://examshortcut.in/exam-updates/</link><description>Verified exam results, official notices and candidate next steps.</description><language>en-IN</language><atom:link href="https://examshortcut.in/exam-updates.xml" rel="self" type="application/rss+xml"/>${newest ? `<lastBuildDate>${new Date(newest).toUTCString()}</lastBuildDate>` : ''}${entries.join('\n')}</channel></rss>\n`;
}
