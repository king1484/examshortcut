import { isOfficialUpdateUrl } from '@/lib/examUpdateRules';

export function OfficialSourceLinks({ sources }: { sources: string[] }) {
  const urls = [...new Set(sources.map(source => source.match(/^https:\/\/[^\s)]+/)?.[0]).filter((url): url is string => !!url && isOfficialUpdateUrl(url)))];
  if (!urls.length) return null;
  return <div className="mt-5"><h3 className="text-sm font-bold">Official sources</h3><ul className="mt-2 space-y-2 text-sm">{urls.map(url => <li key={url}><a className="underline underline-offset-4 break-words" href={url} target="_blank" rel="noopener noreferrer">{new URL(url).hostname} — {decodeURIComponent(new URL(url).pathname.split('/').filter(Boolean).at(-1) ?? 'official portal').replaceAll('_', ' ')} ↗<span className="sr-only"> (opens in a new tab)</span></a></li>)}</ul></div>;
}
