import type { RequestHandler } from './$types';
import { json } from '@sveltejs/kit';
import { error } from '@sveltejs/kit';
import { Step } from "$types/enums";

export const GET = (async ({ params, url }) => {
    let id = url.searchParams.get("id");
    id = parseInt(id);
    let res = await fetch(`http://127.0.0.1:3001/course/${id}`);
    res = await res.json();
    if(res.success) {
        return json(res);
    }else {
        throw error(404, "Not found");
    }
}) satisfies RequestHandler;
