'use client';
import { useCallback, useEffect, useMemo, useRef, useState, type ReactNode } from 'react';
import { VOCAB_LISTS, type VocabItem, type VocabList, type VocabListId } from '@/data/vocab';

const KEY = 'es-vocab-known';
type Tab = 'all' | VocabListId;
type Known = Record<string, 1>;

interface Card { list: VocabListId; item: VocabItem; key: string; flip: boolean }

const keyOf = (list: VocabListId, term: string) => `${list}:${term}`;

/** Sort / group key: ignore a leading article or "to" so "The last straw" files under L. */
const sortKey = (t: string) =>
  t.toLowerCase().replace(/^(a|an|the|to)\s+/, '').replace(/^[^a-z]+/, '');

const letterOf = (t: string) => {
  const c = sortKey(t).charAt(0).toUpperCase();
  return c >= 'A' && c <= 'Z' ? c : '#';
};

function readKnown(): Known {
  try {
    const v = JSON.parse(localStorage.getItem(KEY) ?? '{}');
    return v && typeof v === 'object' && !Array.isArray(v) ? (v as Known) : {};
  } catch { return {}; }
}
function writeKnown(k: Known) {
  try { localStorage.setItem(KEY, JSON.stringify(k)); } catch {}
}

function shuffle<T>(a: T[]): T[] {
  const r = a.slice();
  for (let i = r.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [r[i], r[j]] = [r[j], r[i]];
  }
  return r;
}

const escapeRe = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function Hl({ text, q }: { text: string; q: string }): ReactNode {
  if (!q) return text;
  const parts = text.split(new RegExp(`(${escapeRe(q)})`, 'ig'));
  if (parts.length === 1) return text;
  return parts.map((p, i) =>
    i % 2 === 1
      ? <mark key={i} style={{ background: 'var(--warn-soft)', color: 'inherit', borderRadius: 3, padding: '0 1px' }}>{p}</mark>
      : p);
}

const matches = (it: VocabItem, q: string) =>
  !q ||
  it.term.toLowerCase().includes(q) ||
  it.meaning.toLowerCase().includes(q) ||
  (it.example?.toLowerCase().includes(q) ?? false) ||
  (it.wrong?.toLowerCase().includes(q) ?? false) ||
  (it.words?.some((w) => w.toLowerCase().includes(q)) ?? false);

const SORTED: VocabList[] = VOCAB_LISTS.map((l) => ({
  ...l,
  items: l.items.slice().sort((a, b) => sortKey(a.term).localeCompare(sortKey(b.term))),
}));
const TOTAL = SORTED.reduce((n, l) => n + l.items.length, 0);

const selected = { background: 'var(--ink)', color: 'var(--bg)' };
const inputStyle = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };

function WordChips({ words, tone, q }: { words: string[]; tone: 'ok' | 'bad'; q: string }) {
  return (
    <span className="inline-flex flex-wrap gap-1 mt-1">
      {words.map((w) => (
        <span key={w} className="text-xs font-semibold px-2 py-0.5 rounded-full"
          style={{ background: `var(--${tone}-soft)`, color: `var(--${tone})` }}>
          <Hl text={w} q={q} />
        </span>
      ))}
    </span>
  );
}

function Row({ list, item, q, known }: { list: VocabListId; item: VocabItem; q: string; known: boolean }) {
  const tick = known ? <span title="Marked as known" className="ml-1 text-xs" style={{ color: 'var(--ok)' }}>✓</span> : null;
  if (list === 'spelling') {
    return (
      <div className="py-2.5 px-3.5">
        <div className="flex flex-wrap items-baseline gap-x-3 gap-y-0.5">
          <span className="font-bold" style={{ color: 'var(--ok)' }}>✓ <Hl text={item.term} q={q} /></span>
          <span className="text-sm line-through" style={{ color: 'var(--bad)' }}>✗ <Hl text={item.wrong ?? ''} q={q} /></span>
          {tick}
        </div>
        <div className="text-sm muted"><Hl text={item.meaning} q={q} /></div>
      </div>
    );
  }
  return (
    <div className="py-2.5 px-3.5">
      <div className="font-bold"><Hl text={item.term} q={q} />{tick}</div>
      <div className="text-sm muted"><Hl text={item.meaning} q={q} /></div>
      {item.words && <WordChips words={item.words} tone={list === 'antonyms' ? 'bad' : 'ok'} q={q} />}
      {item.example && <div className="text-xs faint italic mt-0.5"><Hl text={item.example} q={q} /></div>}
    </div>
  );
}

const PROMPT: Record<VocabListId, string> = {
  idioms: 'What does this idiom mean?',
  ows: 'One word for …',
  synonyms: 'Give a synonym / the meaning',
  antonyms: 'Give the opposite',
  spelling: 'Which spelling is correct?',
};

function CardFace({ card, revealed }: { card: Card; revealed: boolean }) {
  const { list, item } = card;
  const label = VOCAB_LISTS.find((l) => l.id === list)?.short ?? '';
  let front: ReactNode;
  let back: ReactNode;

  if (list === 'ows') {
    front = <div className="text-lg sm:text-xl font-bold leading-snug">{item.meaning}</div>;
    back = (
      <>
        <div className="text-2xl font-extrabold" style={{ color: 'var(--brand)' }}>{item.term}</div>
        {item.example && <div className="text-sm faint italic mt-1">{item.example}</div>}
      </>
    );
  } else if (list === 'spelling') {
    const opts = card.flip ? [item.wrong ?? '', item.term] : [item.term, item.wrong ?? ''];
    front = (
      <div className="flex flex-wrap justify-center gap-3">
        {opts.map((o) => {
          const right = o === item.term;
          const style = !revealed
            ? { borderColor: 'var(--line)' }
            : right
              ? { borderColor: 'var(--ok)', background: 'var(--ok-soft)', color: 'var(--ok)' }
              : { borderColor: 'var(--bad)', background: 'var(--bad-soft)', color: 'var(--bad)', textDecoration: 'line-through' };
          return <span key={o} className="text-xl font-extrabold px-4 py-2 rounded-xl border-2" style={style}>{o}</span>;
        })}
      </div>
    );
    back = <div className="text-sm muted">{item.term} — {item.meaning}</div>;
  } else {
    front = <div className="text-2xl font-extrabold leading-snug">{item.term}</div>;
    back = (
      <>
        <div className="text-base font-semibold">{item.meaning}</div>
        {item.words && (
          <div className="mt-1">
            <span className="text-xs faint font-semibold uppercase mr-1">{list === 'antonyms' ? 'Opposites' : 'Synonyms'}:</span>
            <WordChips words={item.words} tone={list === 'antonyms' ? 'bad' : 'ok'} q="" />
          </div>
        )}
        {item.example && <div className="text-sm faint italic mt-1">{item.example}</div>}
      </>
    );
  }

  return (
    <div className="text-center">
      <div className="text-xs font-semibold faint uppercase">{label} · {PROMPT[list]}</div>
      <div className="mt-4">{front}</div>
      <div className="mt-4 min-h-[4.5rem]">
        {revealed ? <div className="pt-3 border-t" style={{ borderColor: 'var(--line)' }}>{back}</div>
          : <div className="text-sm faint">Tap the card or press Space to reveal</div>}
      </div>
    </div>
  );
}

const ROUND_SIZES = [10, 20, 50, 0] as const; // 0 = whole list

export function VocabBank() {
  const [tab, setTab] = useState<Tab>('all');
  const [mode, setMode] = useState<'list' | 'quiz'>('list');
  const [query, setQuery] = useState('');
  const [known, setKnown] = useState<Known>({});
  const [roundSize, setRoundSize] = useState<number>(20);

  const [deck, setDeck] = useState<Card[] | null>(null);
  const [idx, setIdx] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [knew, setKnew] = useState(0);
  const [missed, setMissed] = useState<Card[]>([]);

  const topRef = useRef<HTMLDivElement>(null);

  useEffect(() => { setKnown(readKnown()); }, []);

  const q = query.trim().toLowerCase();

  const filtered = useMemo(
    () => SORTED.map((l) => ({ ...l, items: l.items.filter((it) => matches(it, q)) })),
    [q],
  );
  const matchTotal = filtered.reduce((n, l) => n + l.items.length, 0);

  const scopeLists = tab === 'all' ? SORTED : SORTED.filter((l) => l.id === tab);
  const scopeTotal = scopeLists.reduce((n, l) => n + l.items.length, 0);
  const scopeKnown = scopeLists.reduce((n, l) => n + l.items.filter((it) => known[keyOf(l.id, it.term)]).length, 0);

  const jumpTop = () => {
    const el = topRef.current;
    if (el && el.getBoundingClientRect().top < 0) el.scrollIntoView({ block: 'start' });
  };

  const chooseTab = (t: Tab) => {
    setTab(t);
    setDeck(null);
    jumpTop();
  };

  const startRound = useCallback((cards?: Card[]) => {
    let d: Card[];
    if (cards) {
      d = shuffle(cards);
    } else {
      const all: Card[] = scopeLists.flatMap((l) =>
        l.items.map((item) => ({ list: l.id, item, key: keyOf(l.id, item.term), flip: Math.random() < 0.5 })));
      const unknown = shuffle(all.filter((c) => !known[c.key]));
      const done = shuffle(all.filter((c) => known[c.key]));
      d = [...unknown, ...done];
      if (roundSize > 0) d = d.slice(0, roundSize);
    }
    setDeck(d);
    setIdx(0);
    setRevealed(false);
    setKnew(0);
    setMissed([]);
    jumpTop();
  }, [scopeLists, known, roundSize]);

  const answer = useCallback((gotIt: boolean) => {
    if (!deck || idx >= deck.length) return;
    const card = deck[idx];
    setKnown((prev) => {
      const next = { ...prev };
      if (gotIt) next[card.key] = 1; else delete next[card.key];
      writeKnown(next);
      return next;
    });
    if (gotIt) setKnew((n) => n + 1); else setMissed((m) => [...m, card]);
    setIdx((i) => i + 1);
    setRevealed(false);
  }, [deck, idx]);

  const inQuiz = mode === 'quiz' && deck !== null && idx < deck.length;

  useEffect(() => {
    if (!inQuiz) return;
    const onKey = (e: KeyboardEvent) => {
      const t = e.target as HTMLElement | null;
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT')) return;
      if (e.key === ' ' || e.key === 'Enter') {
        if (!revealed) { e.preventDefault(); setRevealed(true); }
      } else if (revealed && (e.key === '1' || e.key.toLowerCase() === 'n')) {
        answer(false);
      } else if (revealed && (e.key === '2' || e.key.toLowerCase() === 'y')) {
        answer(true);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [inQuiz, revealed, answer]);

  const resetScope = () => {
    const name = tab === 'all' ? 'all lists' : scopeLists[0]?.label;
    if (!window.confirm(`Clear your "known" marks for ${name}?`)) return;
    setKnown((prev) => {
      const next = { ...prev };
      for (const l of scopeLists) for (const it of l.items) delete next[keyOf(l.id, it.term)];
      writeKnown(next);
      return next;
    });
    setDeck(null);
  };

  const tabs: { id: Tab; label: string; count: number }[] = [
    { id: 'all', label: 'All', count: q ? matchTotal : TOTAL },
    ...filtered.map((l) => ({ id: l.id as Tab, label: l.short, count: q ? l.items.length : SORTED.find((s) => s.id === l.id)!.items.length })),
  ];

  const visible = (tab === 'all' ? filtered : filtered.filter((l) => l.id === tab)).filter((l) => l.items.length > 0 || !q);
  const pctKnown = scopeTotal ? Math.round((100 * scopeKnown) / scopeTotal) : 0;

  return (
    <div className="mt-6">
      {/* Sticky controls */}
      <div className="sticky top-14 z-20 -mx-4 px-4 sm:-mx-6 sm:px-6 py-2.5 border-b backdrop-blur"
        style={{ background: 'color-mix(in srgb, var(--bg) 90%, transparent)', borderColor: 'var(--line)' }}>
        <div className="flex gap-2 overflow-x-auto pb-1" role="tablist" aria-label="Vocabulary lists">
          {tabs.map((t) => (
            <button key={t.id} role="tab" aria-selected={tab === t.id} className="chip shrink-0 whitespace-nowrap px-3 py-1.5 text-sm"
              style={tab === t.id ? selected : {}} onClick={() => chooseTab(t.id)}>
              {t.label} <span className="opacity-70">{t.count}</span>
            </button>
          ))}
        </div>
        <div className="flex gap-2 mt-2 items-center">
          {mode === 'list' ? (
            <input type="search" value={query} onChange={(e) => setQuery(e.target.value)}
              placeholder="Search words, meanings, examples…" aria-label="Search vocabulary"
              className="flex-1 min-w-0 p-2 rounded-lg border text-base" style={inputStyle} />
          ) : (
            <div className="flex-1 min-w-0 text-sm">
              <span className="font-bold">{scopeKnown}</span><span className="faint">/{scopeTotal} known</span>
              <div className="h-1.5 rounded-full overflow-hidden mt-1" style={{ background: 'var(--surface-2)' }}>
                <div className="h-full" style={{ width: `${pctKnown}%`, background: 'var(--ok)' }} />
              </div>
            </div>
          )}
          <div className="flex shrink-0 rounded-lg border overflow-hidden" style={{ borderColor: 'var(--line)' }}>
            {(['list', 'quiz'] as const).map((m) => (
              <button key={m} className="px-3 py-2 text-sm font-bold" aria-pressed={mode === m}
                style={mode === m ? selected : { background: 'var(--surface)', color: 'var(--ink-2)' }}
                onClick={() => { setMode(m); setDeck(null); jumpTop(); }}>
                {m === 'list' ? 'List' : 'Flashcards'}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div ref={topRef} className="scroll-mt-44" />

      {mode === 'list' && (
        <div>
          {q && matchTotal === 0 && (
            <p className="card p-6 mt-6 text-center muted">No word or meaning matches “{query.trim()}”. Try a shorter search.</p>
          )}
          {visible.map((l) => {
            const groups: { letter: string; items: VocabItem[] }[] = [];
            for (const it of l.items) {
              const letter = letterOf(it.term);
              const last = groups[groups.length - 1];
              if (last && last.letter === letter) last.items.push(it); else groups.push({ letter, items: [it] });
            }
            return (
              <section key={l.id} id={`vocab-${l.id}`} className="mt-8 scroll-mt-44">
                <h2 className="text-2xl font-extrabold pb-1 border-b-2" style={{ color: 'var(--c-english)', borderColor: 'var(--c-english)' }}>
                  {l.label} <span className="text-base font-bold faint">({l.items.length})</span>
                </h2>
                <p className="text-sm muted mt-2">{l.blurb}</p>
                {groups.map((g) => (
                  <div key={g.letter} className="mt-4">
                    <div className="text-xs font-extrabold faint uppercase tracking-wider mb-1.5">{g.letter}</div>
                    <div className="card divide-y" style={{ borderColor: 'var(--line)' }}>
                      {g.items.map((it) => (
                        <div key={it.term} style={{ borderColor: 'var(--line)' }}>
                          <Row list={l.id} item={it} q={q} known={!!known[keyOf(l.id, it.term)]} />
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </section>
            );
          })}
        </div>
      )}

      {mode === 'quiz' && (
        <div className="mt-6">
          {deck === null && (
            <div className="card p-5">
              <h2 className="text-xl font-extrabold">Flashcards: {tab === 'all' ? 'all lists' : scopeLists[0]?.label}</h2>
              <p className="text-sm muted mt-1">
                See the prompt, recall the answer, reveal, then mark it honestly. Words you knew are saved on this device and move to the back of later rounds; missed words come first.
              </p>
              <div className="grid grid-cols-3 gap-3 text-center mt-4">
                <div><div className="text-3xl font-extrabold">{scopeKnown}</div><div className="text-xs faint font-semibold uppercase">Known</div></div>
                <div><div className="text-3xl font-extrabold">{scopeTotal - scopeKnown}</div><div className="text-xs faint font-semibold uppercase">To learn</div></div>
                <div><div className="text-3xl font-extrabold">{pctKnown}%</div><div className="text-xs faint font-semibold uppercase">Done</div></div>
              </div>
              <div className="flex items-center gap-2 flex-wrap mt-4">
                <span className="text-sm font-bold">Cards per round:</span>
                {ROUND_SIZES.map((n) => (
                  <button key={n} className="chip" style={roundSize === n ? selected : {}} onClick={() => setRoundSize(n)}>
                    {n === 0 ? `All ${scopeTotal}` : n}
                  </button>
                ))}
              </div>
              <div className="flex gap-2 flex-wrap mt-5">
                <button className="btn btn-brand" onClick={() => startRound()}>Start round</button>
                {scopeKnown > 0 && <button className="btn" onClick={resetScope}>Reset progress</button>}
              </div>
            </div>
          )}

          {deck !== null && idx < deck.length && (
            <div>
              <div className="flex items-center justify-between text-sm mb-2">
                <span className="font-bold">Card {idx + 1} / {deck.length}</span>
                <span>
                  <span style={{ color: 'var(--ok)' }} className="font-bold">{knew} knew</span>
                  <span className="faint"> · </span>
                  <span style={{ color: 'var(--bad)' }} className="font-bold">{missed.length} didn’t</span>
                </span>
              </div>
              <div className="h-1.5 rounded-full overflow-hidden mb-3" style={{ background: 'var(--surface-2)' }}>
                <div className="h-full" style={{ width: `${(100 * idx) / deck.length}%`, background: 'var(--brand)' }} />
              </div>
              <button type="button" className="card p-6 sm:p-8 w-full min-h-[16rem] flex items-center justify-center cursor-pointer"
                onClick={() => setRevealed(true)} aria-label={revealed ? 'Answer shown' : 'Reveal answer'}>
                <CardFace card={deck[idx]} revealed={revealed} />
              </button>
              <div className="grid grid-cols-2 gap-3 mt-3">
                <button className="btn justify-center font-bold py-3" disabled={!revealed} onClick={() => answer(false)}
                  style={{ background: 'var(--bad-soft)', color: 'var(--bad)', borderColor: 'var(--bad)', opacity: revealed ? 1 : 0.45 }}>
                  ✗ Didn’t know <span className="hidden sm:inline text-xs opacity-70">(1)</span>
                </button>
                <button className="btn justify-center font-bold py-3" disabled={!revealed} onClick={() => answer(true)}
                  style={{ background: 'var(--ok-soft)', color: 'var(--ok)', borderColor: 'var(--ok)', opacity: revealed ? 1 : 0.45 }}>
                  ✓ Knew it <span className="hidden sm:inline text-xs opacity-70">(2)</span>
                </button>
              </div>
              <div className="flex justify-between items-center mt-3">
                <span className="text-[11px] faint hidden sm:inline">Keys: Space = reveal · 1 = didn’t know · 2 = knew it</span>
                <button className="text-sm font-semibold underline faint ml-auto" onClick={() => setDeck(null)}>End round</button>
              </div>
            </div>
          )}

          {deck !== null && idx >= deck.length && (
            <div className="card p-5 text-center">
              <div className="text-xs faint font-semibold uppercase">Round complete</div>
              <div className="text-4xl font-extrabold mt-1">{knew}<span className="text-xl faint">/{deck.length}</span></div>
              <p className="text-sm muted mt-1">
                {missed.length === 0 ? 'Clean round — every card known.' : `${missed.length} to revise. Go through the missed cards once more while they are fresh.`}
              </p>
              <p className="text-sm mt-2"><b>{scopeKnown}</b><span className="faint">/{scopeTotal} known overall ({pctKnown}%)</span></p>
              {missed.length > 0 && (
                <div className="mt-4 text-left tbl-wrap">
                  <table className="tbl">
                    <thead><tr><th>Missed</th><th>Answer</th></tr></thead>
                    <tbody>
                      {missed.map((c) => (
                        <tr key={c.key}>
                          <td className="font-bold">{c.list === 'ows' ? c.item.meaning : c.item.term}</td>
                          <td>{c.list === 'ows' ? c.item.term : c.list === 'spelling' ? `${c.item.term} (not ${c.item.wrong})` : c.item.meaning}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
              <div className="flex gap-2 flex-wrap justify-center mt-5">
                {missed.length > 0 && <button className="btn btn-brand" onClick={() => startRound(missed)}>Review missed ({missed.length})</button>}
                <button className={missed.length > 0 ? 'btn' : 'btn btn-brand'} onClick={() => startRound()}>New round</button>
                <button className="btn" onClick={() => setDeck(null)}>Done</button>
              </div>
            </div>
          )}
        </div>
      )}

      <p className="text-[11px] faint mt-8">
        {TOTAL} entries across {VOCAB_LISTS.length} lists. Meanings are short study notes, not dictionary entries — when an option in the exam is a closer fit, trust the context of the sentence. Flashcard progress is saved in this browser only.
      </p>
    </div>
  );
}
