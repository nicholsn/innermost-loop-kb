import test from 'node:test';import assert from 'node:assert/strict';import {timelinePage} from '../src/lib/timeline.mjs';
const rows=[{id:'b',date:'2026-09-17'},{id:'a',date:'2026-09-17'},{id:'c',date:'2026-08-01'},{id:'d',date:''}];
test('timeline filters inclusively before paging, ties are stable, unknown dates remain last',()=>{
 assert.deepEqual(timelinePage(rows,{size:2}).entries.map(e=>e.id),['a','b']);
 assert.deepEqual(timelinePage(rows,{from:'2026-09-17',to:'2026-09-17',size:1,page:2}).entries.map(e=>e.id),['b']);
 assert.equal(timelinePage(rows,{from:'2027-01-01'}).total,0);
 assert.equal(timelinePage(rows,{page:999,size:2}).entries.at(-1).id,'d');
 assert.equal(timelinePage(rows,{page:NaN}).page,1);
});
