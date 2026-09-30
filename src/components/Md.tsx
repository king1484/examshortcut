import ReactMarkdown, { type Components } from 'react-markdown';
import Link from 'next/link';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const remarkPlugins = [remarkGfm, remarkMath];
const rehypePlugins = [rehypeKatex];

/* Content never links out: internal paths stay links, anything external (including
   bare URLs that GFM autolinks) renders as plain text. */
/* `> **Rule:** …` style blockquotes become coloured callouts; the bold label picks the colour. */
const CALLOUT: Record<string, string> = { rule: 'rule', remember: 'rule', key: 'rule', tip: 'tip', shortcut: 'tip', note: 'note', example: 'example', watch: 'warn', careful: 'warn', warning: 'warn', trap: 'warn' };

function calloutKind(node: unknown): string | null {
  const p = (node as { children?: { tagName?: string; children?: unknown[] }[] })?.children?.find((c) => c.tagName === 'p');
  const strong = p?.children?.[0] as { tagName?: string; children?: { value?: string }[] } | undefined;
  if (strong?.tagName !== 'strong') return null;
  const word = (strong.children?.[0]?.value ?? '').toLowerCase().replace(/[^a-z ]/g, '').trim().split(' ')[0];
  return CALLOUT[word] ?? null;
}

const components: Components = {
  blockquote: ({ node, children }) => {
    const kind = calloutKind(node);
    return kind ? <div className={`callout callout-${kind}`}>{children}</div> : <blockquote>{children}</blockquote>;
  },
  a: ({ href, children }) =>
    href && href.startsWith('/') && !href.startsWith('//') ? <Link href={href}>{children}</Link> : <span>{children}</span>,
};

export function isSvg(s: string | null | undefined): s is string {
  return !!s && s.trimStart().startsWith('<svg');
}

/** Markdown + KaTeX. `inline` drops block margins for option labels etc. */
export function Md({ children, inline = false, className = '' }: { children?: string | null; inline?: boolean; className?: string }) {
  if (!children) return null;
  let text: string = children;
  if (text.trimStart().startsWith("<svg")) return <span className="opt-svg inline-block" dangerouslySetInnerHTML={{ __html: text }} />;
  // A `$$…$$` line glued to the paragraph around it parses as inline math; give it its own block.
  if (!inline && text.includes('$$')) text = text.replace(/^[ \t]*\$\$([^\n$]+)\$\$[ \t]*$/gm, '\n$$$$\n$1\n$$$$\n');
  return (
    <div className={`md prose prose-sm sm:prose-base ${inline ? 'md-inline' : ''} ${className}`}>
      <ReactMarkdown remarkPlugins={remarkPlugins} rehypePlugins={rehypePlugins} components={components}>{text}</ReactMarkdown>
    </div>
  );
}

export function Tex({ tex, display = false }: { tex: string; display?: boolean }) {
  const src = display ? `$$\n${tex}\n$$` : `$${tex}$`;
  return <Md inline={!display}>{src}</Md>;
}

export function Figure({ svg }: { svg?: string | null }) {
  if (!isSvg(svg)) return null;
  return <div className="figure my-3 flex justify-center" dangerouslySetInnerHTML={{ __html: svg }} />;
}
