import { ${queue}, ${worker} } from "./queue.js";
import { ${logger} } from "../logger.js";

console.log('pause http eval workers');

await ${queue}.pause();

${logger}.warn(`\n----- pausing worker -----\n`);
