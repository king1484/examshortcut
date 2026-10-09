'use client';
import { useEffect, useState } from 'react';
import { isCalendarDate, reviewDates, revisionCalendar, type RevisionTopic } from '@/lib/revisionSchedule';

const KEY = 'es-revision-planner-v1';
function localToday() {
  const date = new Date();
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
}

export function RevisionPlanner({ suggestions }: { suggestions: string[] }) {
  const [topics, setTopics] = useState<RevisionTopic[]>([]);
  const [title, setTitle] = useState('');
  const [start, setStart] = useState('');
  const [loaded, setLoaded] = useState(false);
  const [status, setStatus] = useState('');
  useEffect(() => {
    setStart(localToday());
    try {
      const saved: unknown = JSON.parse(localStorage.getItem(KEY) ?? '[]');
      if (Array.isArray(saved)) setTopics(saved.filter((x): x is RevisionTopic =>
        !!x && typeof x.id === 'string' && typeof x.title === 'string' && x.title.trim().length > 0 && isCalendarDate(x.start)));
    } catch { setStatus('Saved topics could not be loaded. You can start a new list.'); }
    setLoaded(true);
  }, []);

  function save(next: RevisionTopic[]) {
    setTopics(next);
    try { localStorage.setItem(KEY, JSON.stringify(next)); setStatus('Saved in this browser.'); }
    catch { setStatus('Browser storage is unavailable. Download your calendar before leaving.'); }
  }
  function add(event: React.FormEvent) {
    event.preventDefault();
    if (!title.trim() || !isCalendarDate(start)) { setStatus('Enter a topic and a valid study date.'); return; }
    if (topics.some((t) => t.title.toLowerCase() === title.trim().toLowerCase() && t.start === start)) {
      setStatus('This topic already has a plan for that study date.'); return;
    }
    save([...topics, { id: crypto.randomUUID(), title: title.trim(), start }]);
    setTitle('');
  }
  function download() {
    const blob = new Blob([revisionCalendar(topics)], { type: 'text/calendar;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url; link.download = 'examshortcut-revision.ics'; link.click();
    setTimeout(() => URL.revokeObjectURL(url), 4000);
    setStatus('Calendar downloaded. Import it in your calendar app and choose notification settings there.');
  }
  return (
    <div className="mt-6">
      <form onSubmit={add} className="card p-5 space-y-4">
        <div>
          <label htmlFor="revision-topic" className="font-semibold text-sm">Topic you studied</label>
          <input id="revision-topic" list="revision-suggestions" required maxLength={120} className="input w-full mt-2" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="e.g. Percentage: successive changes" />
          <datalist id="revision-suggestions">{suggestions.map((s) => <option value={s} key={s} />)}</datalist>
        </div>
        <div>
          <label htmlFor="revision-date" className="font-semibold text-sm">Date you learned it</label>
          <input id="revision-date" type="date" required min="2000-01-01" max="2100-12-17" className="input block mt-2" value={start} onChange={(e) => setStart(e.target.value)} />
        </div>
        <button className="btn btn-brand" disabled={!loaded} type="submit">Add review dates</button>
      </form>
      <p className="text-sm muted mt-3 break-words" role="status">{status}</p>
      {loaded && topics.length === 0 && <p className="muted text-sm mt-5">Add your first topic to see four suggested review dates.</p>}
      {topics.length > 0 && (
        <section className="mt-6" aria-label="Your revision schedule">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <h2 className="text-xl font-extrabold">Your review dates</h2>
            <button className="btn btn-brand" onClick={download}>Download calendar (.ics)</button>
          </div>
          <div className="space-y-3 mt-4">{topics.map((topic) => (
            <div className="card p-4" key={topic.id}>
              <div className="flex gap-3 justify-between items-start">
                <h3 className="font-bold break-words min-w-0">{topic.title}</h3>
                <button className="btn shrink-0" onClick={() => save(topics.filter((t) => t.id !== topic.id))} aria-label={`Remove ${topic.title}`}>Remove</button>
              </div>
              <p className="text-xs muted mt-1">Studied {topic.start}</p>
              <ul className="flex flex-wrap gap-2 mt-3">{reviewDates(topic.start).map((date, i) => (
                <li className="chip" key={date}>Review {i + 1}: {date}</li>
              ))}</ul>
            </div>
          ))}</div>
        </section>
      )}
    </div>
  );
}
