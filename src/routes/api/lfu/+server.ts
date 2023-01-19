import type { RequestHandler } from './$types';
import { json } from '@sveltejs/kit';
import { error } from '@sveltejs/kit';
import { Step } from "$types/enums";

export const GET = (async ({ params, url }) => {

    let id = url.searchParams.get("id");
    let step = url.searchParams.get("step");
    id = parseInt(id);
    step = parseInt(step);
    let urlString = "";
    if(step == Step.new) {
        urlString = "http://127.0.0.1:3001/lfu";
    }
    else if(step == Step.FieldOfStudy || step == Step.Curriculum || step == Step.Category || step == Step.Course) {
        console.log("Get lfu/" + id);
        urlString = `http://127.0.0.1:3001/lfu/${id}`;
    }
    else if(step == Step.CourseType || step == Step.Group) {
        urlString = `http://127.0.0.1:3001/course/${id}`;
    }

    let res = await fetch(urlString);
    res = await res.json();
    if(res.success) {
        return json(res);
    }else {
        throw error(404, "Not found");
    }
}) satisfies RequestHandler;