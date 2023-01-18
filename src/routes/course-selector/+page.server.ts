import type { PageServerLoad } from './$types';

export const load = (async ({ fetch, request }) => {


    // let urlObj = new URL(request.url);
    // let step = parseInt(urlObj.searchParams.get("step"))
    // let id =  parseInt(urlObj.searchParams.get("id"));
    // let url = "";
    
    // if(step === 0) {
    //     console.log("get new");
    //     url = "http://127.0.0.1:3001/lfu";
    // }
    // else if(step === 1 || 2 || 3 || 4) {
    //     url = `http://127.0.0.1:3001/lfu/${step.id}`
    // }
    // else if(step === 5 || 6) {
    //     url = `http://127.0.0.1: 3001/course/${step.id}`
    // }


    let res = await fetch("http://127.0.0.1:3001/lfu");
    res = await res.json();

    return res;
}) satisfies PageServerLoad;
