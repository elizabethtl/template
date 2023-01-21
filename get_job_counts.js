import { ${queue} } from "./get_all_q.js";

console.log('get all import queue');
const queue1 = await ${queue}.getJobCounts('wait', 'completed', 'failed', 'paused');
console.log(queue1);
