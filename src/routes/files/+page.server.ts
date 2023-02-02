import type { PageServerLoad } from './$types';
import fs from "fs";
import { resolve } from 'path';


async function getDirectories(path) {
    //remove first param from pathname
    return await fs.promises.readdir(resolve("./fileSharing"), { withFileTypes: true });
}

export const load = (async ({ url }) => {
    let data = await getDirectories(url);
    console.log(data);
    let folders = [];
    for (let folder of data) {
        if (folder.isDirectory()) {
            console.log(folder.name);
            folders.push(folder.name);
        }
    }
    return {folders};


}) satisfies PageServerLoad;

