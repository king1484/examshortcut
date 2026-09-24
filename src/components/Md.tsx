import ReactMarkdown, { type Components } from 'react-markdown';
import Link from 'next/link';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const remarkPlugins = [remarkGfm, remarkMath];
const rehypePlugins = [rehypeKatex];

/* Content never links out: internal paths stay links, anything external (including
   bare URLs that GFM autolinks) renders as plain text. */
const components: Components = {
  a: ({ href, children }) =>
    href && href.startsWith('/') && !href.startsWith('//') ? <Link href={href}>{children}</Link> : <span>{children}</span>,
};

export function isSvg(s: string | null | undefined): s is string {
  return !!s && s.trimStart().startsWith('<svg');
}

/** Markdown + KaTeX. `inline` drops block margins for option labels etc. */
export function Md({ children, inline = false, className = '' }: { children?: string | null; inline?: boolean; className?: string }) {
  if (!children) return null;
  if (isSvg(children)) return <span className="opt-svg inline-block" dangerouslySetInnerHTML={{ __html: children }} />;
  return (
    <div className={`md prose prose-sm sm:prose-base ${inline ? 'md-inline' : ''} ${className}`}>
      <ReactMarkdown remarkPlugins={remarkPlugins} rehypePlugins={rehypePlugins} components={components}>{children}</ReactMarkdown>
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
