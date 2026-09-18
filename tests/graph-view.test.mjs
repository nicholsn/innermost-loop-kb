import test from 'node:test';import assert from 'node:assert/strict';import {readView,writeView} from '../src/lib/graph-view.mjs';
test('view links preserve scope and reproduce filters, selection, query, and labels',()=>{
 const state={view:'list',query:'Crusoe & compute',selected:'developments/example',hiddenTypes:['Person','Role'],hiddenRelations:['actor'],labels:true};
 const url=writeView(new URL('https://example.org/graph?focus=themes/a&page=2&layout=communities'),state);
 assert.deepEqual(readView(url.searchParams),state);assert.equal(url.searchParams.get('page'),'2');assert.equal(url.searchParams.get('layout'),'communities');
 assert.equal(readView(new URLSearchParams('view=bad&labels=oops')).view,'graph');
 const reset=writeView(url,{view:'graph',query:'',selected:'',hiddenTypes:[],hiddenRelations:[],labels:false});assert.equal(reset.searchParams.has('hideTypes'),false);
});
