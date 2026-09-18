export function safeSourceUrl(value) {
  try { const url = new URL(value); return ['http:', 'https:'].includes(url.protocol) ? url.href : null; } catch { return null; }
}
export function reportingDate(entry) {
  const value = entry.data.issue_date;
  const date = value instanceof Date ? value.toISOString().slice(0, 10) : String(value || entry.id.match(/\d{4}-\d{2}-\d{2}/)?.[0] || '');
  return /^\d{4}-\d{2}-\d{2}$/.test(date) ? date : '';
}
export function evidenceSources(data) {
  return (Array.isArray(data.sources) ? data.sources : []).flatMap(source => {
    const url = safeSourceUrl(typeof source === 'string' ? source : source?.resource);
    return url ? [{ url, title: source.title || new URL(url).hostname, host: new URL(url).hostname }] : [];
  });
}
// Only suppress an exact first-paragraph duplicate; never rewrite the body.
export const descriptionInBody = (description, body) => Boolean(description && String(body || '').trim().split(/\n\s*\n/)[0].trim() === description.trim());
