export function validDate(value) {
 return typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value) && !Number.isNaN(Date.parse(value)) && new Date(value).toISOString().slice(0,10) === value;
}
export function monthsBetween(from,to) {
 if(!validDate(from)||!validDate(to)||from>to)return [];
 const dates=[];let date=new Date(from.slice(0,7)+'-01T00:00:00Z');
 while(date.toISOString().slice(0,7)<=to.slice(0,7)){dates.push(date.toISOString().slice(0,7));date.setUTCMonth(date.getUTCMonth()+1);}
 return dates;
}
export function aggregateAnalytics(data, {themes,from,to,month='',actor='',detailTheme=''} ) {
 const months=monthsBetween(from,to);
 const selected=new Set(themes);
 const records=[...new Map(data.records.map(r=>[r.id,r])).values()].filter(r=>validDate(r.date)&&r.date>=from&&r.date<=to);
 const denominator=new Map(months.map(m=>[m,records.filter(r=>r.date.startsWith(m)).length]));
 const series=themes.map(id=>{let cumulative=0;return {id,points:months.map(m=>{const rows=records.filter(r=>r.date.startsWith(m)&&r.themes.includes(id));cumulative+=rows.length;const total=denominator.get(m);return {month:m,count:rows.length,cumulative,total,share:total ? rows.length/total*100 : null};})};});
 const matching=records.filter(r=>r.themes.some(t=>selected.has(t))&&(!detailTheme||r.themes.includes(detailTheme))&&(!month||r.date.startsWith(month)));
 const actors=new Map();
 for(const r of matching)for(const id of new Set(r.actors)){actors.set(id,(actors.get(id)||0)+1);}
 return {months,series,denominator:Object.fromEntries(denominator),total:records.length,matched:matching.length,
  actors:[...actors].map(([id,count])=>({id,count})).sort((a,b)=>b.count-a.count||a.id.localeCompare(b.id)),
  rows:matching.filter(r=>!actor||r.actors.includes(actor)).sort((a,b)=>b.date.localeCompare(a.date)||a.id.localeCompare(b.id))};
}
export function analyticsCsv(result, titles) {
 const quote=v=>'"'+String(v ?? '').replaceAll('"','""')+'"';
 return [['Theme','Month','New records','Cumulative in range','All records in month','Share percent'],...result.series.flatMap(s=>s.points.map(p=>[titles[s.id]||s.id,p.month,p.count,p.cumulative,p.total,p.share===null?'':p.share.toFixed(2)]))].map(row=>row.map(quote).join(',')).join('\r\n');
}
