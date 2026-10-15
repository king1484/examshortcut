import { getExamPhoto } from '@/lib/examImages';

/** A real photograph with its caption and credit, shown on an exam hub page. Renders nothing if the exam has no photo. */
export function ExamPhoto({ id }: { id: string }) {
  const p = getExamPhoto(id);
  if (!p) return null;
  return (
    <figure className="card overflow-hidden mt-5 mb-0">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={p.src}
        width={p.width}
        height={p.height}
        alt={p.alt}
        decoding="async"
        style={{ display: 'block', width: '100%', height: 'auto', maxHeight: 380, objectFit: 'cover' }}
      />
      <figcaption className="px-4 py-3 text-xs muted">
        <span>{p.caption}</span>{' '}
        <span className="faint">
          Photo: {p.author},{' '}
          {p.licenseUrl ? <a className="underline" href={p.licenseUrl} target="_blank" rel="noopener noreferrer">{p.license}</a> : p.license},{' '}
          <a className="underline" href={p.source} target="_blank" rel="noopener noreferrer">via Wikimedia Commons</a>.
        </span>
      </figcaption>
    </figure>
  );
}
