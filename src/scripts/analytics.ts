import {aggregateAnalytics,analyticsCsv,validDate} from '../lib/analytics.mjs';
const root=document.querySelector<HTMLElement>('.analytics')!;
const el=(id:string)=>root.querySelector<HTMLElement>('#'+id)!;
const form=el('analytics-controls') as HTMLFormElement;
const from=form.querySelector<HTMLInputElement>('[name=from]')!,to=form.querySelector<HTMLInputElement>('[name=to]')!,metric=form.querySelector<HTMLSelectElement>('[name=metric]')!;
const slots=[...form.querySelectorAll<HTMLSelectElement>('[data-theme-slot]')];
const month=el('inspect-month') as HTMLSelectElement,theme=el('inspect-theme') as HTMLSelectElement;
const palette=['#276c91','#a34c27','#7555a0'];
let data:any,result:any,selected:string[]=[],actor='',shown=20;
let themes=new Map<string,any>(),actors=new Map<string,any>();
const node=(tag:string,text='')=>{const n=document.createElement(tag);n.textContent=text;return n;};
function option(select:HTMLSelectElement,value:string,label:string){const o=document.createElement('option');o.value=value;o.textContent=label;select.append(o);}
function writeURL(){const url=new URL(location.href);for(const [key,value] of Object.entries({themes:selected.join(','),from:from.value,to:to.value,metric:metric.value,month:month.value,theme:theme.value,actor})){if(value||key==='themes')url.searchParams.set(key,value);else url.searchParams.delete(key);}if(url.href!==location.href)history.pushState({},'',url);}
function inspect(m:string,t:string){month.value=m;theme.value=t;actor='';shown=20;render(true);el('records-title').focus();}
function svgNode(tag:string,attrs:Record<string,string|number>,text=''){const n=document.createElementNS('http://www.w3.org/2000/svg',tag);for(const [k,v]of Object.entries(attrs))n.setAttribute(k,String(v));n.textContent=text;return n;}
const tooltip=el('growth-tooltip');
let tooltipTimer:ReturnType<typeof setTimeout>;
function hideTooltip(){clearTimeout(tooltipTimer);tooltip.hidden=true;}
function deferHideTooltip(){clearTimeout(tooltipTimer);tooltipTimer=setTimeout(hideTooltip,120);}
function showTooltip(point:Element,text:string){
 clearTimeout(tooltipTimer);tooltip.textContent=text;tooltip.hidden=false;
 const box=point.getBoundingClientRect(),size=tooltip.getBoundingClientRect();
 tooltip.style.left=`${Math.max(12,Math.min(innerWidth-size.width-12,box.left+box.width/2-size.width/2))}px`;
 tooltip.style.top=`${Math.max(12,Math.min(innerHeight-size.height-12,box.top-size.height-10>=12?box.top-size.height-10:box.bottom+10))}px`;
}
tooltip.addEventListener('pointerenter',()=>clearTimeout(tooltipTimer));
tooltip.addEventListener('pointerleave',deferHideTooltip);
window.addEventListener('scroll',hideTooltip,true);window.addEventListener('resize',hideTooltip);
root.addEventListener('keydown',event=>{if(event.key==='Escape')hideTooltip();});
function drawGrowth(){
 hideTooltip();
 const mode=metric.value;
 const max=Math.max(mode==='share'?1:1,...result.series.flatMap((s:any)=>s.points.map((p:any)=>p[mode]??0)));
 const step=Math.max(1,10**Math.floor(Math.log10(max/4)));
 const top=mode==='share'?Math.min(100,Math.ceil(max/20)*20):Math.ceil(max/4/step)*step*4;
 const svg=svgNode('svg',{viewBox:'0 0 840 330',role:'img','aria-labelledby':'growth-title growth-description'});
 const x=(i:number)=>60+(result.months.length===1?350:i*700/(result.months.length-1));const y=(v:number)=>265-v/top*220;
 for(let i=0;i<=4;i++){const value=top*i/4;svg.append(svgNode('line',{x1:60,x2:780,y1:y(value),y2:y(value),stroke:'currentColor',opacity:.15}),svgNode('text',{x:50,y:y(value)+4,'text-anchor':'end',fill:'currentColor','font-size':12},value.toLocaleString(undefined,{maximumFractionDigits:1})+(mode==='share'?'%':'')));}
 result.months.forEach((m:string,i:number)=>{if(i===0||i===result.months.length-1||i%Math.ceil(result.months.length/8)===0)svg.append(svgNode('text',{x:x(i),y:295,'text-anchor':'middle',fill:'currentColor','font-size':12},m));});
 const legend=el('growth-legend');legend.replaceChildren();
 result.series.forEach((s:any,idx:number)=>{
  const dash=['','7 4','2 4'][idx];let segment:string[]=[];
  const flush=()=>{if(segment.length)svg.append(svgNode('polyline',{points:segment.join(' '),fill:'none',stroke:palette[idx],'stroke-width':2.5,'stroke-dasharray':dash}));segment=[];};
  s.points.forEach((p:any,i:number)=>{const value=p[mode];if(value===null){flush();return;}segment.push(`${x(i)},${y(value)}`);});flush();
  s.points.forEach((p:any,i:number)=>{if(p[mode]===null)return;const circle=svgNode('circle',{cx:x(i),cy:y(p[mode]),r:5,fill:palette[idx],tabindex:0,role:'button','aria-label':`${themes.get(s.id).title}, ${p.month}: ${Number(p[mode]).toFixed(mode==='share'?1:0)}${mode==='share'?' percent':''}. Inspect new records this month.`});const summary=`${themes.get(s.id).title} — ${p.month}\nNew records: ${p.count}\nCumulative in range: ${p.cumulative}\nAll records this month: ${p.total}\nShare of coverage: ${p.share===null?'No coverage':p.share.toFixed(1)+'%'}\nSelect to inspect this month’s records.`;
  circle.setAttribute('aria-describedby','growth-tooltip');
  circle.addEventListener('pointerenter',()=>showTooltip(circle,summary));
  circle.addEventListener('pointerleave',()=>{if(document.activeElement!==circle)deferHideTooltip();});
  circle.addEventListener('focus',()=>showTooltip(circle,summary));
  circle.addEventListener('blur',deferHideTooltip);circle.addEventListener('click',()=>inspect(p.month,s.id));circle.addEventListener('keydown',(e:any)=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();inspect(p.month,s.id);}});svg.append(circle);});
  const label=node('span',`${idx+1}. ${themes.get(s.id).title} (${['solid','dashed','dotted'][idx]})`);label.style.color=palette[idx];legend.append(label);
 });
 el('growth-chart').replaceChildren(svg);
 el('growth-description').textContent=mode==='cumulative'?'Unique linked developments accumulated since the selected start date. Select a point to inspect that month’s additions; a rising line is not increasing confidence.':mode==='count'?'New linked developments reported each month. Zero means no theme-linked records in this corpus, not no real-world events.':'Theme-linked developments divided by all recorded developments in the month and selected date range. Gaps mean no denominator. Overlapping themes can sum above 100%.';
 const table=node('table');const head=node('tr');for(const title of ['Theme','Month','New records','Cumulative in range','All records','Share'])head.append(node('th',title));const thead=node('thead');thead.append(head);table.append(thead);const body=node('tbody');
 for(const s of result.series)for(const p of s.points){const tr=node('tr');tr.append(node('th',themes.get(s.id).title),node('td',p.month));const cell=node('td'),button=node('button',String(p.count));button.setAttribute('aria-label',`${themes.get(s.id).title}, ${p.month}: inspect ${p.count} new records`);button.addEventListener('click',()=>inspect(p.month,s.id));cell.append(button);tr.append(cell,node('td',String(p.cumulative)),node('td',String(p.total)),node('td',p.share===null?'No coverage':p.share.toFixed(1)+'%'));body.append(tr);}table.append(body);el('growth-table').replaceChildren(table);
}
function drawPulse(){
 const table=node('table'),head=node('tr');head.append(node('th','Theme / reporting month'));
 for(const m of result.months){const first=m+'-01',last=new Date(Number(m.slice(0,4)),Number(m.slice(5)),0).getDate();const partial=from.value>first||to.value<m+'-'+String(last).padStart(2,'0');head.append(node('th',m+(partial?' (partial)':'')));}
 const thead=node('thead');thead.append(head);table.append(thead);const body=node('tbody');
 const max=Math.max(1,...result.series.flatMap((s:any)=>s.points.map((p:any)=>metric.value==='share'?(p.share||0):p.count)));
 for(const s of result.series){const tr=node('tr'),label=node('th',themes.get(s.id).title);label.setAttribute('scope','row');tr.append(label);for(const p of s.points){const value=metric.value==='share'?p.share:p.count;const td=node('td'),button=node('button',p.total===0?'—':metric.value==='share'?value.toFixed(1)+'%':String(value));button.style.background=`rgba(39,108,145,${p.total===0?0:.05+.24*(value||0)/max})`;button.setAttribute('aria-label',`${themes.get(s.id).title}, ${p.month}: ${p.count} of ${p.total} recorded developments. Inspect records.`);button.addEventListener('click',()=>inspect(p.month,s.id));td.append(button);tr.append(td);}body.append(tr);}table.append(body);el('pulse-table').replaceChildren(table);
}
function drawDrilldown(){
 el('actor-description').textContent=`${result.matched} unique developments · ${month.value||'All months in range'} · ${theme.value?themes.get(theme.value)?.title:'All selected themes'}. Showing ${Math.min(12,result.actors.length)} of ${result.actors.length} actors. Records without an actor still appear below.`;
 const list=el('actor-bars');list.replaceChildren();const max=result.actors[0]?.count||1;
 for(const item of result.actors.slice(0,12)){const a=actors.get(item.id);const li=node('li'),button=node('button',`${a?.title||item.id} · ${item.count} unique records`);button.setAttribute('aria-pressed',String(actor===item.id));button.addEventListener('click',()=>{actor=item.id;shown=20;render(true);el('records-title').focus();});const track=node('div');track.className='actor-track';track.setAttribute('aria-hidden','true');const fill=node('div');fill.className='actor-fill';fill.style.width=`${item.count/max*100}%`;track.append(fill);li.append(button,track);list.append(li);}
 if(!result.actors.length)list.append(node('li','No linked actors in this selection.'));
 const rows=el('analytics-records');rows.replaceChildren();for(const r of result.rows.slice(0,shown)){const li=node('li'),a=node('a',r.title) as HTMLAnchorElement;a.href=r.href;li.append(a,node('small',`${r.date} · ${r.themes.filter((id:string)=>selected.includes(id)).map((id:string)=>themes.get(id)?.title).join(' · ')}`));rows.append(li);}
 el('records-status').textContent=`${result.rows.length} matching records${actor?' for '+actors.get(actor)?.title:''} · showing ${Math.min(shown,result.rows.length)}. Open a record to inspect its claim and sources.`;
 el('records-more').hidden=shown>=result.rows.length;
}
function render(write=false){
 if(!validDate(from.value)||!validDate(to.value)||from.value>to.value||from.value<data.min||to.value>data.max){el('analytics-status').textContent=`Choose a valid range within ${data.min}–${data.max}.`;el('analytics-content').hidden=true;return;}
 selected=[...new Set(slots.map(s=>s.value).filter(Boolean))];
 result=aggregateAnalytics(data,{themes:selected,from:from.value,to:to.value});
 const oldMonth=month.value,oldTheme=theme.value;month.replaceChildren();theme.replaceChildren();option(month,'','All months in range');option(theme,'','All selected themes');for(const m of result.months)option(month,m,m);for(const id of selected)option(theme,id,themes.get(id).title);month.value=result.months.includes(oldMonth)?oldMonth:'';theme.value=selected.includes(oldTheme)?oldTheme:'';
 result=aggregateAnalytics(data,{themes:selected,from:from.value,to:to.value,month:month.value,detailTheme:theme.value,actor});
 el('analytics-status').textContent=`${result.total.toLocaleString()} dated developments in range · ${selected.length} selected themes · ${data.undated} undated records excluded. ${selected.length?'Choose a chart point or pulse cell to inspect evidence.':'Select at least one theme to draw a comparison.'}`;
 drawGrowth();drawPulse();drawDrilldown();el('analytics-content').hidden=!selected.length;if(write)writeURL();
}
function restore(){clearTimeout(updateTimer);const p=new URLSearchParams(location.search);const ids=p.has('themes')?(p.get('themes')||'').split(',').filter(id=>themes.has(id)).slice(0,3):data.themes.slice(0,3).map((t:any)=>t.id);slots.forEach((s,i)=>s.value=ids[i]||'');from.value=validDate(p.get('from'))?p.get('from')!:data.min;to.value=validDate(p.get('to'))?p.get('to')!:data.max;metric.value=['count','share'].includes(p.get('metric')||'')?p.get('metric')!:'cumulative';actor=actors.has(p.get('actor')||'')?p.get('actor')!:'';shown=20;render();month.value=p.get('month')||'';theme.value=p.get('theme')||'';render();}
async function load(){el('analytics-status').textContent='Loading analytics…';el('analytics-retry').hidden=true;try{const response=await fetch(root.dataset.endpoint!);if(!response.ok)throw Error('load');data=await response.json();themes=new Map(data.themes.map((t:any)=>[t.id,t]));actors=new Map(data.actors.map((a:any)=>[a.id,a]));for(const slot of slots){slot.replaceChildren();option(slot,'','No theme');for(const t of [...data.themes].sort((a:any,b:any)=>a.title.localeCompare(b.title)))option(slot,t.id,`${t.title} (${t.count})`);}from.min=to.min=data.min;from.max=to.max=data.max;form.hidden=false;el('analytics-method').textContent=`Corpus reporting range: ${data.min}–${data.max}. ${data.records.length} developments; ${data.undated} without a usable reporting date; ${data.unlinked} without a resolved theme. Dates use the earliest linked issue date, falling back to a dated record ID. Records are grouped by calendar month, with partial boundary months retained.`;restore();}catch{el('analytics-status').textContent='Analytics could not load. Retry to fetch the data.';el('analytics-retry').hidden=false;}}
let updateTimer:ReturnType<typeof setTimeout>;
function updateViews(){clearTimeout(updateTimer);if(!data)return;actor='';shown=20;render(true);}
form.addEventListener('submit',e=>{e.preventDefault();updateViews();});
for(const control of [...slots,metric,from,to])control.addEventListener('change',updateViews);
for(const control of [from,to])control.addEventListener('input',()=>{clearTimeout(updateTimer);updateTimer=setTimeout(updateViews,150);});
for(const control of [month,theme])control.addEventListener('change',()=>{actor='';shown=20;render(true);});
el('clear-actor').addEventListener('click',()=>{actor='';shown=20;render(true);});
el('records-more').addEventListener('click',()=>{shown+=20;drawDrilldown();});
el('analytics-reset').addEventListener('click',()=>{clearTimeout(updateTimer);slots.forEach((s,i)=>s.value=data.themes[i]?.id||'');from.value=data.min;to.value=data.max;metric.value='cumulative';month.value=theme.value=actor='';shown=20;render(true);});
el('analytics-export').addEventListener('click',()=>{const csv=analyticsCsv(result,Object.fromEntries([...themes].map(([id,t])=>[id,t.title])));const url=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='theme-evidence-'+from.value+'-'+to.value+'.csv';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
el('analytics-retry').addEventListener('click',load);window.addEventListener('popstate',()=>{if(data)restore();});load();
