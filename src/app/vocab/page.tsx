import type { Metadata } from 'next';
import { VocabBank } from '@/components/VocabBank';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL vocabulary — idioms, one word substitution, synonyms, antonyms & spellings',
  description: 'Free SSC CGL English vocab bank: idioms and phrases, one word substitution, synonyms, antonyms and commonly misspelt words with meanings and examples. Searchable lists plus flashcards that track what you know.',
};

export default function VocabPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">SSC CGL vocabulary bank</h1>
      <p className="muted mt-2">
        The idioms, one-word substitutions, synonyms, antonyms and spellings that SSC keeps repeating, each with a one-line meaning. Search the lists, or switch to flashcards and mark what you know. Progress stays on this device.
      </p>
      <VocabBank />
    </div>
  );
}
