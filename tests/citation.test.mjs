import test from 'node:test';import assert from 'node:assert/strict';import {citation,correctionUrl} from '../src/lib/citation.mjs';
test('citations retain attribution and qualify missing metadata',()=>{
 const e={id:'developments/2026-09-17-example',data:{title:'A [claim]',claim:'Reportedly $3.9 billion',sources:[{title:'Reporting',resource:'https://example.org/story'}]}};
 const text=citation(e,'https://example.org/kb');assert.match(text,/secondary record/);assert.match(text,/2026-09-17/);assert.match(text,/Reportedly/);assert.match(text,/does not imply independent verification/);
 assert.ok(citation(e,'https://example.org/kb',true).includes('A \\[claim\\]'));
 const legacy=citation({id:'systems/model',data:{}},'https://example.org/kb');assert.match(legacy,/Reporting date: unknown/);assert.match(legacy,/No source links recorded/);
 const url=new URL(correctionUrl(e,'https://example.org/kb'));assert.equal(url.pathname,'/nicholsn/innermost-loop-kb/issues/new');assert.ok(url.searchParams.get('body').includes(e.id));
});
