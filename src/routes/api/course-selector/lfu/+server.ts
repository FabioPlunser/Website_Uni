import type { RequestHandler } from './$types';
import { json } from '@sveltejs/kit';
import { error } from '@sveltejs/kit';
import { Step } from "$types/enums";
import { convertToDate } from "$helper/convertTime";

export const GET = (async ({params, url }) => {
    let id = url.searchParams.get("id");
    let step = url.searchParams.get("step");
    id = parseInt(id);
    step = parseInt(step);
    
    console.log(`Fetch: id:${id} step:${step}`);
    let data;
    if(step === 0){
        let res = await fetch("http://127.0.0.1:3001/lfu");
        data = await res.json();
    }else if(step >= 5){
        let res = await fetch(`http://127.0.0.1:3001/course/${id}`);
        res = await res.json();
        if(res.success && res.groups.length > 0){
            for(let group of res.groups){
                for (let time of group.times){
                    let {from, to} = convertToDate(time);
                    time.from = from;
                    time.to = to;
                }
            }
        }
        data = res;
       
    }else{
        let res = await fetch(`http://127.0.0.1:3001/lfu/${id}`);
        data = await res.json();
    }
    if(data?.success){
        return json(data);
    }else{
        throw error(404, "Not Found")
        return {success: false};  
    }
}) satisfies RequestHandler;
