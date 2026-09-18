import { loadBundle, iriOf, hrefOf, titleOf, relationsOf } from './lokf';

export async function loadGraph() {
  const { concepts } = await loadBundle();
  const nodes = concepts.map(c => ({ data: {
    id: iriOf(c), label: titleOf(c), type: c.data.type, concept_id: c.id, href: hrefOf(c),
    date: String(c.data.issue_date || c.id.match(/\d{4}-\d{2}-\d{2}/)?.[0] || ''),
  } }));
  const known = new Set(nodes.map(n => n.data.id));
  const edges = new Map();
  for (const c of concepts) for (const { slot, target } of relationsOf(c)) {
    const source = iriOf(c);
    if (!known.has(target) || target === source) continue;
    const id = `${slot}:${source}->${target}`;
    edges.set(id, { data: { id, source, target, predicate: slot } });
  }
  return { nodes, edges: [...edges.values()] };
}
