export const LAYOUTS = {
  fcose: { label: 'Fast force · fCoSE', description: 'Combines spectral placement with force refinement to reveal connected neighborhoods.' },
  communities: { label: 'Community clusters', description: 'Groups densely connected nodes using Markov clustering, then arranges the groups with fCoSE. Inferred from this view; article-membership links are excluded.' },
  types: { label: 'Group by concept type', description: 'Separates people, organizations, developments, and topics into labeled groups. These groups reflect types, not inferred communities.' },
  cose: { label: 'Classic force · CoSE', description: 'Uses attraction along edges and repulsion between nodes to reveal the shape of the network.' },
  radial: { label: 'Radial · connection hubs', description: 'Places highly connected nodes in the center and less-connected nodes in outer rings.' },
};
export const validLayout = value => Object.hasOwn(LAYOUTS, value) ? value : 'fcose';

// Synthetic parents are presentation only. Never alter the source graph.
export function clearGroups(cy) {
  cy.nodes('.concept').move({ parent: null });
  cy.nodes('.layout-group').remove();
}

export function clusterNodes(elements, mode) {
  const nodes = elements.nodes();
  if (mode === 'types') {
    const types = [...new Set(nodes.map(n => n.data('type')))].sort();
    return types.map(type => ({ label: type, nodes: nodes.filter(n => n.data('type') === type) }));
  }
  // Membership hubs connect unrelated stories and obscure substantive groups.
  const candidates = nodes.filter(n => n.data('type') !== 'Issue');
  const relationships = elements.edges().filter(e => !['covers', 'reported_in', 'isPartOf', 'hasPart'].includes(e.data('predicate')) && candidates.contains(e.source()) && candidates.contains(e.target()));
  if (!candidates.length) return [];
  const raw = candidates.union(relationships).markovClustering({ expandFactor: 2, inflateFactor: 1.3, maxIterations: 30 });
  // Finite-iteration MCL can return overlapping sets: assign each node once.
  const seen = new Set();
  const groups = [];
  raw.sort((a, b) => a.length - b.length || a[0].id().localeCompare(b[0].id()));
  for (const cluster of raw) {
    const members = cluster.filter(n => !seen.has(n.id()));
    if (!members.length) continue;
    members.forEach(n => seen.add(n.id()));
    groups.push(members);
  }
  for (const n of candidates) if (!seen.has(n.id())) groups.push(n.collection());
  const singletons = groups.filter(group => group.length === 1);
  const result = groups.filter(group => group.length > 1).map((group, i) => {
    const representative = group.filter(n => n.data('type') === 'Theme').sort((a, b) => b.degree() - a.degree())[0];
    return { label: `Community ${i + 1}${representative ? ' · ' + representative.data('label').slice(0, 42) : ''}`, nodes: group };
  });
  if (singletons.length) result.push({label: 'Unclustered', nodes: singletons.reduce((all, group) => all.union(group), nodes.cy().collection())});
  return result;
}

export function prepareLayout(cy, choice) {
  clearGroups(cy);
  const mode = validLayout(choice);
  const nodes = cy.nodes('.concept').not('.hidden');
  const edges = cy.edges().not('.hidden').filter(e => nodes.contains(e.source()) && nodes.contains(e.target()));
  let elements = nodes.union(edges);
  let groups = [];
  if (mode === 'communities' || mode === 'types') {
    groups = clusterNodes(elements, mode);
    cy.batch(() => {
      groups.forEach((group, i) => {
        let id = `__layout_group_${i}`;
        while (cy.getElementById(id).length) id += '_';
        const parent = cy.add({ data: {id, label: group.label}, classes: 'layout-group' });
        group.nodes.move({ parent: id });
        elements = elements.union(parent);
      });
    });
  }
  const common = { animate: false, fit: true, padding: 55 };
  let options;
  if (mode === 'radial') {
    const degrees = new Map(nodes.map(n => [n.id(), edges.filter(e => e.source().id() === n.id() || e.target().id() === n.id()).length]));
    options = { ...common, name: 'concentric', concentric: n => degrees.get(n.id()) || 0, levelWidth: () => Math.max(1, Math.ceil(Math.max(0, ...degrees.values()) / 5)), minNodeSpacing: 65, avoidOverlap: true, nodeDimensionsIncludeLabels: true };
  } else if (mode === 'cose') {
    options = { ...common, name: 'cose', numIter: 500, nodeRepulsion: () => 14000, idealEdgeLength: () => 130, componentSpacing: 120 };
  } else {
    options = { ...common, name: 'fcose', quality: 'default', randomize: true, numIter: 800, nodeSeparation: 100, nodeRepulsion: () => 12000, idealEdgeLength: () => 120, packComponents: false, tile: true, tilingPaddingHorizontal: 50, tilingPaddingVertical: 50 };
  }
  // fCoSE spectral initialization expects more than one visible node.
  if (nodes.length < 2) options = { ...common, name: 'grid' };
  return { elements, options, groups: groups.length, nodes: nodes.length };
}
