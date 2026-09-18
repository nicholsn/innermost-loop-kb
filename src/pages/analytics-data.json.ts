import {analyticsData} from '../lib/analytics-data';
export async function GET(){return new Response(JSON.stringify(await analyticsData()),{headers:{'Content-Type':'application/json; charset=utf-8'}});}
