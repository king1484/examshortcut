CREATE TABLE IF NOT EXISTS submissions (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK(kind IN ('feedback', 'feature')),
  title TEXT NOT NULL,
  message TEXT NOT NULL,
  exam TEXT NOT NULL DEFAULT '',
  page TEXT NOT NULL DEFAULT '',
  email TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL,
  rate_bucket TEXT
);
CREATE INDEX IF NOT EXISTS submissions_bucket ON submissions(rate_bucket);
CREATE INDEX IF NOT EXISTS submissions_created ON submissions(created_at);
