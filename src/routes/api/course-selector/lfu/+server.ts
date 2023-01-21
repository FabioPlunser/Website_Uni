import type { RequestHandler } from './$types';
import { json } from '@sveltejs/kit';
import { error } from '@sveltejs/kit';
import { Step } from "$types/enums";

export const GET = (async ({params, url }) => {
    let id = url.searchParams.get("id");
    let step = url.searchParams.get("step");
    id = parseInt(id);
    step = parseInt(step);
    
    console.log(`Fetch: id:${id} step:${step}`);
    let res = null;
    if(step === 0){
        res = await fetch("http://127.0.0.1:3001/lfu");
    }else if(step == 5){
        res = await fetch(`http://127.0.0.1:3001/course/${id}`);
    }else{
        res = await fetch(`http://127.0.0.1:3001/lfu/${id}`);
    }
    res = await res.json();
    if(res.success) {
        return json(res);
    }else {
        throw error(40, "Not found");
    }

    return json({success: false});
}) satisfies RequestHandler;
