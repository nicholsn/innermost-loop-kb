export function readView(params) {
 return { view:params.get('view') === 'list' ? 'list' : 'graph', query:params.get('q') || '', selected:params.get('node') || '',
  hiddenTypes:(params.get('hideTypes') || '').split(',').filter(Boolean), hiddenRelations:(params.get('hideRelations') || '').split(',').filter(Boolean),labels:params.get('labels')==='1' };
}
export function writeView(url, state) {
 const values={view:state.view==='list'?'list':'',q:state.query,node:state.selected,hideTypes:[...state.hiddenTypes].sort().join(','),hideRelations:[...state.hiddenRelations].sort().join(','),labels:state.labels?'1':''};
 for(const [key,value] of Object.entries(values)){if(value)url.searchParams.set(key,value);else url.searchParams.delete(key);}
 return url;
}
