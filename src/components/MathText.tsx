import { LazyTex } from '@/components/LazyTex';

/* Plain-text rendering of a markdown-ish snippet that contains $…$ math: the text is
   shown as-is (markdown emphasis stripped) and each math span goes through LazyTex, so a
   page with hundreds of snippets ships TeX source instead of server-rendered KaTeX.
   `max` truncates for previews (at a word boundary, never inside a $…$ span). */
export function MathText({ text, max, className }: { text: string; max?: number; className?: string }) {
  // \$ in data = a literal dollar: park it so the $…$ splitter can't mispair
  const D = '\u0001';
  let s = text.replace(/\\\$/g, D).replace(/\\([#*+_~\-])/g, '$1');
  let cut = false;
  if (max && s.length > max) {
    s = s.slice(0, max);
    const sp = s.lastIndexOf(' ');
    if (sp > max * 0.6) s = s.slice(0, sp);
    cut = true;
  }
  // A cut through a $…$ span would leave an unbalanced delimiter: drop the tail
  if ((s.match(/\$/g)?.length ?? 0) % 2) s = s.slice(0, s.lastIndexOf('$'));
  const parts = s.split(/\$([^$]+)\$/);
  return (
    <span className={className}>
      {parts.map((p, i) => (i % 2 ? <LazyTex key={i} tex={p} /> : p.replace(/\*\*|__|`/g, '').split(D).join('$')))}
      {cut && '…'}
    </span>
  );
}
