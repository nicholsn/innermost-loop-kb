export function terms(text) {
  return String(text).normalize('NFKD').replace(/\p{M}/gu, '').toLowerCase().match(/[\p{L}\p{N}]+/gu) || [];
}

// Weighted inverted index, built once with the site, with no external service.
export function buildIndex(documents) {
  const postings = Object.create(null);
  documents.forEach((doc, id) => {
    for (const [text, weight] of [[doc.title, 8], [doc.tags.join(' '), 5], [doc.description, 3], [doc.text, 1]]) {
      for (const term of new Set(terms(text))) {
        const posting = postings[term] ||= Object.create(null);
        posting[id] = (posting[id] || 0) + weight;
      }
    }
  });
  return { documents, postings };
}

export function searchIndex(index, query, type = '') {
  const queryTerms = [...new Set(terms(query))].slice(0, 12);
  let scores;
  queryTerms.forEach((term, position) => {
    const matches = new Map();
    const add = (posting, multiplier) => {
      for (const [id, score] of Object.entries(posting || {})) matches.set(Number(id), Math.max(matches.get(Number(id)) || 0, Number(score) * multiplier));
    };
    add(index.postings[term], 2);
    // Prefix completion on the final word, including when an exact word exists.
    if (position === queryTerms.length - 1 && term.length >= 2) {
      for (const word of Object.keys(index.postings)) if (word !== term && word.startsWith(term)) add(index.postings[word], 1);
    }
    scores = scores === undefined ? matches : new Map([...scores].filter(([id]) => matches.has(id)).map(([id, score]) => [id, score + matches.get(id)]));
  });
  const ids = scores ? [...scores.keys()] : index.documents.map((_, id) => id);
  return ids.filter(id => !type || index.documents[id].type === type)
    .sort((a, b) => (scores?.get(b) || 0) - (scores?.get(a) || 0) || index.documents[b].date.localeCompare(index.documents[a].date) || index.documents[a].title.localeCompare(index.documents[b].title));
}
