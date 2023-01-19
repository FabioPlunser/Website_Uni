import type { PageServerLoad } from './$types';

export const load = (async ({ fetch }) => {
    let res = await fetch("http://127.0.0.1:3001/lfu");
    res = await res.json();

    return res;
}) satisfies PageServerLoad;

import type { Actions } from './$types';
 
export const actions: Actions = {
  default: async (event) => {
    const formData = new FormData(event.target);
    console.log(event);
  }
};