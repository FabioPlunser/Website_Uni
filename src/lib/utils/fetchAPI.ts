
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

export async function login(username: string, password:string){
    console.log("login");
    
}
export async function logout(sessionid:string){
    let res = await fetch("http://localhost:3002/api/logout", {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({session: sessionid})
    })
    let res2 = await res.json()
    if(res2.ok) return res2; 
    throw error(res2.message);
}