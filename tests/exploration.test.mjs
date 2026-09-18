import { test } from 'node:test';
import assert from 'node:assert/strict';
import { graphScopes, PAGE_SIZE, MAX_NODES } from '../src/lib/graph-scope.mjs';
import { buildIndex, searchIndex } from '../src/lib/search.mjs';

const node = (id, type, date = '') => ({ data: { id, concept_id: id, type, label: id, date } });
const edge = (source, target, predicate) => ({ data: { id: `${source}:${target}:${predicate}`, source, target, predicate } });

test('large topics stay bounded and every development is reachable once', () => {
  const nodes = [node('topic', 'Theme'), node('article', 'Issue')];
  const edges = [];
  for (let i = 0; i < 150; i++) {
    const id = `dev-${i}`;
    nodes.push(node(id, 'Development', `2026-09-${String(i % 28 + 1).padStart(2, '0')}`));
    edges.push(edge(id, 'topic', 'evidences'), edge(id, 'article', 'reported_in'));
    for (let j = 0; j < 5; j++) {
      nodes.push(node(`${id}-actor-${j}`, 'Organization'));
      edges.push(edge(id, `${id}-actor-${j}`, 'actor'));
    }
  }
  edges.push(edges[0]);
  const scopes = graphScopes({nodes, edges}).filter(s => s.graph.scope.id === 'topic');
  assert.equal(scopes.length, Math.ceil(150 / PAGE_SIZE));
  const seen = [];
  for (const {graph} of scopes) {
    assert.ok(graph.nodes.length <= MAX_NODES);
    assert.ok(graph.scope.omitted > 0);
    const ids = new Set(graph.nodes.map(n => n.data.id));
    assert.equal(new Set(graph.edges.map(e => e.data.id)).size, graph.edges.length);
    assert.ok(graph.edges.every(e => ids.has(e.data.source) && ids.has(e.data.target)));
    seen.push(...graph.nodes.filter(n => n.data.type === 'Development').map(n => n.data.id));
  }
  assert.equal(seen.length, 150);
  assert.equal(new Set(seen).size, 150);
});

test('issue membership is explicit, covers-only links work, and isolated nodes survive', () => {
  const scopes = graphScopes({nodes:[node('issue','Issue'),node('dev','Development'),node('other','Development'),node('alone','Person')],edges:[edge('issue','dev','covers'),edge('other','issue','references')]});
  assert.deepEqual(scopes.find(s => s.scope === 'issue/1').graph.nodes.map(n => n.data.id), ['issue','dev']);
  assert.equal(scopes.find(s => s.scope === 'alone/1').graph.nodes.length, 1);
});

const doc = (title, text, type = 'Development') => ({ title, text, type, description:'', tags:[], date:'2026-09-17' });
const index = buildIndex([doc('Energy report','Ternary compression and inference'),doc('Ternary compression','Power'),doc('René institute','biology','Organization'),doc('Biology','unrelated')]);
test('full-text matching, title ranking, AND terms, prefixes, accents and type filters', () => {
  assert.deepEqual(searchIndex(index,'ternary'),[1,0]);
  assert.deepEqual(searchIndex(index,'compression inf'),[0]);
  assert.deepEqual(searchIndex(index,'rene','Organization'),[2]);
  assert.deepEqual(searchIndex(index,'ternary','Organization'),[]);
  assert.deepEqual(searchIndex(index,'no-such-word'),[]);
  assert.deepEqual(searchIndex(index,'','Organization'),[2]);
});
