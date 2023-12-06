import { connect_db, find_all_ql_db } from "./mongodb.js";

async function main(){
  await connect_db();

  let resp = await find_all_ql_db();

  console.log(resp[0]);
  console.log(resp.length);

  console.log(resp[0]['_id']);
  console.log(resp[0]['directory']);

  for(let i = 0; i < resp.length; i++){
    get_all_import_queue.add(resp[i]['_id'], {dir: resp[i]['directory']});
    
    if(i == resp.length-1){
      console.log('loaded all');
    }
  }
}

main();
