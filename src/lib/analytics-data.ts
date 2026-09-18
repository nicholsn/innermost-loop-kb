import {loadBundle,iriOf,hrefOf,titleOf,relationsOf} from './lokf';
import {reportingDate} from './evidence.mjs';
import {validDate} from './analytics.mjs';
export async function analyticsData() {
 const {concepts,byIri}=await loadBundle();
 const records=concepts.filter(c=>c.data.type==='Development').map(c=>{
  const rels=relationsOf(c);
  const resolve=(slot:string,type?:string)=>[...new Set(rels.filter(r=>r.slot===slot).map(r=>byIri.get(r.target)).filter(e=>e&&(!type||e.data.type===type)).map(e=>e!.id))];
  const issueDates=rels.filter(r=>r.slot==='reported_in').map(r=>byIri.get(r.target)).filter(Boolean).map(e=>reportingDate(e)).filter(validDate).sort();
  const fallback=reportingDate(c);
  return {id:c.id,title:titleOf(c),href:hrefOf(c),date:issueDates[0] || (validDate(fallback)?fallback:''),themes:resolve('evidences','Theme'),actors:resolve('actor')};
 });
 const actorIds=new Set(records.flatMap(r=>r.actors));
 const themes=concepts.filter(c=>c.data.type==='Theme').map(c=>({id:c.id,title:titleOf(c),href:hrefOf(c),count:records.filter(r=>r.themes.includes(c.id)).length})).sort((a,b)=>b.count-a.count||a.id.localeCompare(b.id));
 const actors=concepts.filter(c=>actorIds.has(c.id)).map(c=>({id:c.id,title:titleOf(c),href:hrefOf(c),type:c.data.type}));
 const dates=records.map(r=>r.date).filter(Boolean).sort();
 return {records,themes,actors,min:dates[0]||'',max:dates.at(-1)||'',undated:records.filter(r=>!r.date).length,unlinked:records.filter(r=>!r.themes.length).length};
}
