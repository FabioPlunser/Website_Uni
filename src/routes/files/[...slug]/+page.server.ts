import type { PageServerLoad, PageServerGet} from './$types';
import fs from "fs";
import { resolve } from 'path';


async function getDirectories(path) {
    //remove first param from pathname
    let test = path.pathname;
    test = test.split("/").slice(2).join("/");

    return await fs.promises.readdir(resolve("./fileSharing/"+test), { withFileTypes: true });
}

export const load = (async ({ url }) => {
    let folders = [];
    let files = [];
    if(url.pathname.includes(".")){
        return {folders, files};
    }else{
        let data = await getDirectories(url);
        // console.log(data);
        
        for (let folder of data) {
            if (folder.isDirectory()) {
                // console.log("fodlername", folder.name);
                folders.push(folder.name);
            }
            if (folder.isFile()) {
                // console.log("filename", folder.name);
                files.push(folder.name);

            }
        }
        return {folders, files};
    }
}) satisfies PageServerLoad;


