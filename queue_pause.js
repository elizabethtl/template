import { http_eval_queue, http_eval_worker } from "./queue.js";

import { http_eval_logger } from "../logger.js";

console.log('pause http eval workers');

await http_eval_queue.pause();

http_eval_logger.warn(`\n----- pausing worker -----\n`);
