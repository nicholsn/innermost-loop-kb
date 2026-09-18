import type { APIRoute } from 'astro';
import { loadGraph } from '../../lib/graph';
import { graphScopes } from '../../lib/graph-scope.mjs';

export async function getStaticPaths() {
  return graphScopes(await loadGraph()).map(({ scope, graph }) => ({
    params: { scope }, props: { graph },
  }));
}
export const GET: APIRoute = ({ props }) => new Response(JSON.stringify(props.graph), {
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
});
