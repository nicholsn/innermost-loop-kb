import test from 'node:test';
import assert from 'node:assert/strict';
import { evidenceSources, reportingDate, descriptionInBody } from '../src/lib/evidence.mjs';
test('sources preserve attribution and reject unsafe protocols and incomplete records', () => {
 assert.deepEqual(evidenceSources({sources:[{resource:'javascript:alert(1)'},{title:'Missing'},{resource:'https://example.org/report', title:'Original reporting'}]}), [{url:'https://example.org/report',title:'Original reporting',host:'example.org'}]);
 assert.deepEqual(evidenceSources({}), []);
});
test('reporting dates and exact duplicate handling preserve legacy text', () => {
 assert.equal(reportingDate({id:'developments/2026-09-17-story',data:{}}),'2026-09-17');
 assert.equal(reportingDate({id:'systems/model',data:{}}),'');
 assert.ok(descriptionInBody('Same.', '\nSame.\n\nImportant caveat.'));
 assert.ok(!descriptionInBody('Same.', 'Different.\n\nSame.'));
});
