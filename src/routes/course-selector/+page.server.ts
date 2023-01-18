import type { PageLoad } from './$types';
 
export const load = (async ({ fetch, params }) => {
  let res = await fetch("http://127.0.0.1:3001/lfu");
  res = await res.json();
  // console.log(res);
 
  return res;
}) satisfies PageLoad;
