import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="max-w-lg mx-auto text-center py-20">
      <div className="text-6xl font-extrabold" style={{ color: 'var(--brand)' }}>404</div>
      <h1 className="text-2xl font-extrabold mt-3">Page not found</h1>
      <p className="muted mt-2">The page you're looking for doesn't exist — but your preparation does.</p>
      <div className="flex gap-3 justify-center mt-6 flex-wrap">
        <Link href="/" className="btn btn-brand">Home</Link>
        <Link href="/ssc-cgl/syllabus/" className="btn">Syllabus</Link>
        <Link href="/ssc-cgl/mocks/" className="btn">Mock tests</Link>
      </div>
    </div>
  );
}
