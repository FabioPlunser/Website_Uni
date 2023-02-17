
import Database from "better-sqlite3";

let db = null;
export function initDB(){
    db = new Database("db/lfu.db", {verbose: console.log});
}

export function getStudies(){
    const sql = `select * from studies`;
    const stmnt = db.prepare(sql);
	const rows = stmnt.all();
    console.log(rows);
    return rows;
    
}
