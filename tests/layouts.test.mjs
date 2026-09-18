import {test} from 'node:test';
import assert from 'node:assert/strict';
import cytoscape from 'cytoscape';
import fcose from 'cytoscape-fcose';
import {LAYOUTS, validLayout, prepareLayout, clusterNodes} from '../src/lib/graph-layouts.mjs';
cytoscape.use(fcose);
function fixture() {
  const elements = [{data:{id:'issue',type:'Issue',label:'Issue'},classes:'concept'}];
  for(const group of ['a','b']) for(let i=0;i<4;i++) {
    const id=group+i;
    elements.push({data:{id,type:i ? 'Development':'Theme',label:id},classes:'concept'});
    elements.push({data:{id:'membership-'+id,source:'issue',target:id,predicate:'covers'}});
    for(let j=0;j<i;j++) elements.push({data:{id:id+'-'+j,source:id,target:group+j,predicate:'evidences'}});
  }
  return cytoscape({elements,headless:true,styleEnabled:true,layout:{name:'preset'}});
}
test('community detection separates dense groups despite a shared article hub',()=>{
  const cy=fixture();
  try {
    const groups=clusterNodes(cy.elements(),'communities');
    assert.equal(groups.length,2);
    assert.deepEqual(groups.map(g=>g.nodes.map(n=>n.id()).sort()).sort(),[['a0','a1','a2','a3'],['b0','b1','b2','b3']]);
  } finally {cy.destroy();}
});
test('switching every layout preserves concepts, relations, and valid coordinates',()=>{
  const cy=fixture();
  const ids=cy.nodes().map(n=>n.id()).sort(), edges=cy.edges().map(e=>e.id()).sort();
  try {
    for(const mode of Object.keys(LAYOUTS)) {
      const plan=prepareLayout(cy,mode);
      plan.elements.layout({...plan.options,boundingBox:{x1:0,y1:0,w:1000,h:700}}).run();
      assert.deepEqual(cy.nodes('.concept').map(n=>n.id()).sort(),ids);
      assert.deepEqual(cy.edges().map(e=>e.id()).sort(),edges);
      assert.ok(cy.nodes('.concept').every(n=>Number.isFinite(n.position('x')) && Number.isFinite(n.position('y'))));
    }
    assert.equal(cy.nodes('.layout-group').length,0);
  } finally {cy.destroy();}
});
test('hidden nodes and edge filters are excluded from clustering; singleton and empty views work',()=>{
  const cy=fixture();
  try {
    cy.nodes('.concept').filter(n=>n.id()!=='a0').addClass('hidden');
    for(const mode of Object.keys(LAYOUTS)) {
      const plan=prepareLayout(cy,mode);
      assert.equal(plan.nodes,1);
      assert.equal(plan.options.name,'grid');
      assert.equal(plan.elements.edges().length,0);
    }
    cy.getElementById('a0').addClass('hidden');
    assert.equal(prepareLayout(cy,'communities').nodes,0);
    assert.equal(cy.nodes('.layout-group').length,0);
    assert.equal(validLayout('invalid'),'fcose');
  } finally {cy.destroy();}
});

import {typeStyle} from '../src/lib/graph-palette.mjs';
test('node colors and shapes depend only on type, never the scope or order',()=>{
 const subset=['Development','Organization','Theme'];
 const superset=['AISystem','Benchmark',...subset].reverse();
 const styles=new Map(superset.map(t=>[t,typeStyle(t)]));
 for(const t of subset)assert.deepEqual(typeStyle(t),styles.get(t));
 assert.notEqual(typeStyle('Development').color,typeStyle('Organization').color);
 assert.deepEqual(typeStyle('FutureType'),typeStyle('FutureType'));
 assert.ok(subset.every(t=>typeStyle(t).shape));
});
