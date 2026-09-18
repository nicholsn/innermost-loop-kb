export function timelinePage(entries, {from = '', to = '', page = 1, size = 20} = {}) {
 const filtered = entries.filter(e => (!from || e.date && e.date >= from) && (!to || e.date && e.date <= to))
  .sort((a,b) => b.date.localeCompare(a.date) || a.id.localeCompare(b.id));
 const pages = Math.max(1, Math.ceil(filtered.length / size));
 const current = Math.min(pages, Math.max(1, Number.isSafeInteger(page) ? page : 1));
 return {entries:filtered.slice((current-1)*size,current*size),total:filtered.length,pages,page:current};
}
