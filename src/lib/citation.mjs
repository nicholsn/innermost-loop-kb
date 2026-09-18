import {evidenceSources, reportingDate} from './evidence.mjs';
const escape = text => String(text).replace(/[\\`*_[\]<>]/g, '\\$&');
export function citation(entry, permalink, markdown = false) {
 const title=entry.data.title || entry.id;
 const date=reportingDate(entry) || 'unknown';
 const lines=[markdown ? `## ${escape(title)}` : title, 'Innermost Loop KB — secondary record', `Reporting date: ${date}`, `KB permalink: ${permalink}`];
 if(entry.data.claim) lines.push(`Claim: ${markdown ? escape(entry.data.claim) : entry.data.claim}`);
 const sources=evidenceSources(entry.data);
 lines.push('Attributed sources:', ...sources.map(s=>markdown?`- [${escape(s.title)}](<${s.url}>)`:`- ${s.title} — ${s.url}`));
 if(!sources.length)lines.push('No source links recorded.');
 lines.push('This citation does not imply independent verification of linked-source claims.');
 return lines.join('\n');
}
export function correctionUrl(entry, permalink) {
 const url=new URL('https://github.com/nicholsn/innermost-loop-kb/issues/new');
 url.searchParams.set('template','correction.md');
 url.searchParams.set('title',`Correction: ${entry.data.title || entry.id}`);
 url.searchParams.set('body',`Record: ${entry.id}\nPage: ${permalink}\n\nWhat should change?\n\nSupporting evidence / source links:\n\nProposed correction:\n`);
 return url.href;
}
