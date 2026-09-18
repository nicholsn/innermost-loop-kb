import type { APIRoute } from 'astro';
import { loadGraph } from '../lib/graph';

// Full export remains available for downloads; the explorer uses graph-data/.
export const GET: APIRoute = async () => new Response(JSON.stringify(await loadGraph()), {
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
});
