import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import fs from "fs";
import { resolve } from 'path';

export const GET = (async (event) => {
    const filePath = resolve("."+event.url.pathname);
    const fileExtension = filePath.split(".").pop();
    var file = fs.readFileSync(filePath);

    const blob = new Blob([file]);

    console.log(blob);

    return new Response(blob);
}) satisfies RequestHandler;