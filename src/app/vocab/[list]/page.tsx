import Link from 'next/link';
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { VOCAB_LISTS, type VocabList, type VocabListId } from '@/data/vocab';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** URL slug per list, named after what people search for. */
const SLUG: Record<VocabListId, string> = {
  idioms: 'idioms-and-phrases',
  ows: 'one-word-substitution',
  synonyms: 'synonyms',
  antonyms: 'antonyms',
  spelling: 'commonly-misspelt-words',
};

const META: Record<VocabListId, { title: (n: number) => string; desc: (n: number) => string; h1: string; lead: string }> = {
  idioms: {
    h1: 'SSC CGL idioms and phrases',
    title: (n) => `SSC CGL idioms and phrases: ${n} with meanings and examples`,
    desc: (n) => `${n} idioms and phrases for SSC CGL, CHSL, CPO and MTS English, each with a short meaning and an example sentence. Alphabetical, searchable with flashcards.`,
    lead: 'Each idiom with a one-line meaning and an example sentence. In the exam, the options are usually plausible, so learn the meaning rather than the literal words.',
  },
  ows: {
    h1: 'SSC CGL one word substitution',
    title: (n) => `SSC CGL one word substitution: ${n} words with meanings`,
    desc: (n) => `${n} one-word substitutions for SSC exams: the description and the single word that replaces it, with examples. Alphabetical list with flashcards.`,
    lead: 'The exam gives a description and asks for the single word. Learn them in families (-cide, -cracy, -logy, -phobia, -gamy) and test yourself with the flashcards.',
  },
  synonyms: {
    h1: 'SSC CGL synonyms',
    title: (n) => `SSC CGL synonyms: ${n} words with 2-3 close synonyms each`,
    desc: (n) => `${n} headwords with close synonyms for SSC CGL English, with a plain meaning for each. Alphabetical list with flashcards.`,
    lead: 'Each headword with the synonyms that tend to appear as options, plus a short meaning to help you decide when two options look close.',
  },
  antonyms: {
    h1: 'SSC CGL antonyms',
    title: (n) => `SSC CGL antonyms: ${n} words with their opposites`,
    desc: (n) => `${n} words and their opposites for SSC CGL English, with the meaning of each so you can reason out the answer. Alphabetical list with flashcards.`,
    lead: 'Each word with its opposites and a short meaning, so you can work out the antonym even when the options are unfamiliar.',
  },
  spelling: {
    h1: 'SSC CGL commonly misspelt words',
    title: (n) => `SSC CGL spelling: ${n} commonly misspelt words (correct vs wrong)`,
    desc: (n) => `${n} commonly misspelt English words for SSC spelling questions, with the usual wrong spelling beside the correct one and a short meaning.`,
    lead: 'The correct spelling next to the version people usually write. Spot the wrong form quickly by remembering the part that trips most people.',
  },
};

const byId = (slug: string): VocabList | undefined => VOCAB_LISTS.find((l) => SLUG[l.id] === slug);
const sorted = (l: VocabList) => [...l.items].sort((a, b) => a.term.replace(/^(a|an|the)\s+/i, '').localeCompare(b.term.replace(/^(a|an|the)\s+/i, ''), 'en', { sensitivity: 'base' }));

export function generateStaticParams() {
  return VOCAB_LISTS.map((l) => ({ list: SLUG[l.id] }));
}

export async function generateMetadata({ params }: { params: Promise<{ list: string }> }): Promise<Metadata> {
  const { list } = await params;
  const l = byId(list);
  if (!l) return {};
  const m = META[l.id];
  const title = m.title(l.items.length);
  const description = m.desc(l.items.length);
  return {
    title,
    description,
    openGraph: { title, description, images: ['/og.png'] },
    twitter: { card: 'summary_large_image', title, description, images: ['/og.png'] },
  };
}

export default async function VocabListPage({ params }: { params: Promise<{ list: string }> }) {
  const { list } = await params;
  const l = byId(list);
  if (!l) notFound();
  const m = META[l.id];
  const items = sorted(l);

  return (
    <div className="max-w-3xl mx-auto">
      <div className="text-xs faint mt-2"><Link href="/vocab/" className="underline decoration-dotted">Vocabulary bank</Link></div>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-1">{m.h1}</h1>
      <p className="muted mt-2 text-[15px]">{items.length} entries. {m.lead}</p>
      <div className="flex flex-wrap gap-2 mt-4">
        <Link href="/vocab/" className="btn btn-brand">Practise with flashcards</Link>
        {VOCAB_LISTS.filter((x) => x.id !== l.id).map((x) => (
          <Link key={x.id} href={`/vocab/${SLUG[x.id]}/`} className="chip">{x.label}</Link>
        ))}
      </div>

      <div className="card mt-6 overflow-hidden">
        <div className="tbl-wrap">
          <table className="tbl">
            <thead>
              <tr>
                <th>{l.id === 'spelling' ? 'Correct' : l.id === 'idioms' ? 'Idiom' : l.id === 'ows' ? 'Word' : 'Word'}</th>
                <th>{l.id === 'spelling' ? 'Often written' : l.id === 'synonyms' ? 'Synonyms' : l.id === 'antonyms' ? 'Antonyms' : 'Meaning'}</th>
                {(l.id === 'synonyms' || l.id === 'antonyms' || l.id === 'spelling') && <th>Meaning</th>}
                {(l.id === 'idioms' || l.id === 'ows') && <th>Example</th>}
              </tr>
            </thead>
            <tbody>
              {items.map((it) => (
                <tr key={it.term}>
                  <td className="font-bold whitespace-nowrap align-top">{it.term}</td>
                  {l.id === 'spelling' ? <td className="align-top" style={{ color: 'var(--bad)' }}>{it.wrong}</td>
                    : l.id === 'synonyms' || l.id === 'antonyms' ? <td className="align-top">{(it.words ?? []).join(', ')}</td>
                    : <td className="align-top">{it.meaning}</td>}
                  {(l.id === 'synonyms' || l.id === 'antonyms' || l.id === 'spelling') && <td className="align-top muted">{it.meaning}</td>}
                  {(l.id === 'idioms' || l.id === 'ows') && <td className="align-top muted text-sm">{it.example ?? ''}</td>}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
      <p className="text-xs faint mt-4">Meanings are short study notes written for revision, not dictionary entries. When an option in the exam fits the sentence better, trust the sentence.</p>
    </div>
  );
}
