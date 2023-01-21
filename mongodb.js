import { MongoClient } from 'mongodb';
const url = 'mongodb://localhost:27017';
const db_client = new MongoClient(url);
const db_name = 'vs-extensions';

var ql_databases_collection;


async function connect_db() {
  await db_client.connect();

  const vs_extension_db = db_client.db(db_name);
  ql_databases_collection = vs_extension_db.collection('ql-databases');
}

async function find_all_ql_db() {
  const result = await ql_databases_collection.find().toArray();
  return result;
}


export{
  connect_db,
  find_all_ql_db, 
}
