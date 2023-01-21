import { connect_db } from "./mongodb.js";
import { ${worker} } from "./get_all_q.js";


await connect_db();

${worker}.run();
