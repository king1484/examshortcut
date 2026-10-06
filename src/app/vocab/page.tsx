import Link from 'next/link';
import type { Metadata } from 'next';
import { VocabBank } from '@/components/VocabBank';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL vocabulary — idioms, one word substitution, synonyms, antonyms & spellings',
  description: 'SSC CGL English vocab bank: idioms and phrases, one word substitution, synonyms, antonyms and commonly misspelt words with meanings and examples. Searchable lists plus flashcards that track what you know.',
};

export default function VocabPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL vocabulary bank</h1>
      <p className="muted mt-2">
        The words SSC keeps repeating, each with a one-line meaning. Search, or switch to flashcards.
      </p>
      <VocabBank />
      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Read the full lists</h2>
        <div className="flex flex-wrap gap-2 mt-3">
          {([['idioms-and-phrases', 'Idioms & phrases'], ['one-word-substitution', 'One-word substitution'], ['synonyms', 'Synonyms'], ['antonyms', 'Antonyms'], ['commonly-misspelt-words', 'Misspelt words']] as const).map(([slug, label]) => (
            <Link key={slug} href={`/vocab/${slug}/`} className="chip">{label}</Link>
          ))}
        </div>
      </section>
    </div>
  );
}
