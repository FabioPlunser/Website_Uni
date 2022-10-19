
import { error } from "@sveltejs/kit";

export async function getLFU(){
    const res = await fetch('http://localhost:3001/lfu');
    const res2 = await res.json() ;

    if(res.ok) return res2;
    throw error(res2.message);

}
   
export async function getLFUID(id: number){
    const res = await fetch(`http://localhost:3001/lfu/${id}`);
    const res2 = await res.json();
    if(res.ok) return res2;
    throw error(res2.message);
}


export async function getCourse(id: number, name: string){
    const res = await fetch(`http://localhost:3001/course/${id}`);
    const res2 = await res.json();
    if(res.ok) return res2;
    throw error(res2.message);
}