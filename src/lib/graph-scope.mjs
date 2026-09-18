// Kept independent of Astro so scope limits can be regression-tested.
export const PAGE_SIZE = 60;
export const MAX_NODES = 180;

export function graphScopes(graph) {
  const nodes = new Map(graph.nodes.map(n => [n.data.id, n]));
  const adjacent = new Map([...nodes.keys()].map(id => [id, new Set()]));
  const outgoing = new Map([...nodes.keys()].map(id => [id, []]));
  const edges = [...new Map(graph.edges.map(e => [e.data.id, e])).values()];
  for (const edge of edges) {
    const { source, target } = edge.data;
    if (!nodes.has(source) || !nodes.has(target) || source === target) continue;
    adjacent.get(source).add(target);
    adjacent.get(target).add(source);
    outgoing.get(source).push(edge);
  }
  const newestFirst = (a, b) => {
    const x = nodes.get(a).data, y = nodes.get(b).data;
    return (y.date || '').localeCompare(x.date || '') || x.concept_id.localeCompare(y.concept_id);
  };
  const result = [];
  for (const center of graph.nodes) {
    const { id, type, concept_id, label } = center.data;
    let related = [...adjacent.get(id)];
    // Article and topic pages show their developments, then their context.
    if (type === 'Issue' || type === 'Theme') {
      related = related.filter(target => nodes.get(target).data.type === 'Development' &&
        [...outgoing.get(target), ...outgoing.get(id)].some(e =>
          (e.data.source === id && e.data.target === target && e.data.predicate === 'covers') ||
          (e.data.source === target && e.data.target === id && e.data.predicate === (type === 'Issue' ? 'reported_in' : 'evidences'))));
    }
    related.sort(newestFirst);
    const pages = Math.max(1, Math.ceil(related.length / PAGE_SIZE));
    for (let page = 1; page <= pages; page++) {
      const seeds = related.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);
      const selected = new Set([id, ...seeds]);
      const context = new Set();
      if (type === 'Issue' || type === 'Theme') {
        for (const seed of seeds) for (const edge of outgoing.get(seed)) {
          const target = edge.data.target;
          if (!['Issue', 'Development'].includes(nodes.get(target).data.type)) context.add(target);
        }
      }
      const candidates = [...context].filter(target => !selected.has(target)).sort(newestFirst);
      for (const target of candidates.slice(0, MAX_NODES - selected.size)) selected.add(target);
      result.push({
        scope: `${concept_id}/${page}`,
        graph: {
          nodes: [...selected].map(key => nodes.get(key)),
          edges: [...selected].flatMap(key => outgoing.get(key)).filter(e => selected.has(e.data.target)),
          scope: { id: concept_id, title: label, type, page, pages, total: related.length,
            start: related.length ? (page - 1) * PAGE_SIZE + 1 : 0,
            end: Math.min(page * PAGE_SIZE, related.length),
            omitted: Math.max(0, candidates.length - (MAX_NODES - seeds.length - 1)) },
        },
      });
    }
  }
  return result;
}
