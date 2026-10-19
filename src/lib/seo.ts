/** Trim metadata to a search-result limit at a word boundary. */
export function cap(text: string, max: number) {
  const clean = text.replace(/\s+/g, ' ').trim();
  if (clean.length <= max) return clean;
  const cut = clean.slice(0, max - 1);
  const at = cut.lastIndexOf(' ');
  const base = at > Math.floor(max * 0.5) ? cut.slice(0, at) : cut;
  return `${base.replace(/[\s,;:·—–-]+$/, '')}…`;
}
