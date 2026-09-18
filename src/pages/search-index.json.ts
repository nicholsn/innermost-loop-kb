import type { APIRoute } from 'astro';
import { loadBundle, hrefOf, titleOf } from '../lib/lokf';
import { buildIndex } from '../lib/search.mjs';

export const GET: APIRoute = async () => {
  const { concepts } = await loadBundle();
  const documents = concepts.map(c => ({
    title: titleOf(c), type: c.data.type, href: hrefOf(c), tags: c.data.tags || [],
    description: String(c.data.description || c.data.claim || c.data.thesis || ''),
    text: [c.data.claim, c.data.thesis, c.body].filter(Boolean).join('\n')
      .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/[#*_`>]/g, ''),
    date: String(c.data.issue_date || c.id.match(/\d{4}-\d{2}-\d{2}/)?.[0] || ''),
  }));
  return new Response(JSON.stringify(buildIndex(documents)), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
