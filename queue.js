import { Queue, Worker } from 'bullmq';
import IORedis from 'ioredis';
const redis_conn = new IORedis();

import { exec } from 'child_process';
import * as util from 'util';
const exec_prom = util.promisify(exec);

import { dirname } from 'path';
import { fileURLToPath } from 'url';
const __dirname = dirname(fileURLToPath(import.meta.url));

const ${queue} = new Queue('${queue}', {
  connection:{
    redis_conn
  }
});

const ${worker} = new Worker('${queue}', async(job) => {

  // code

}, {
  autorun: false,
  connection: {
    redis_conn
  }
});

${worker}.on('completed', (job) => {
  ${logger}.info(`completed job ${job.id} successfully`);
});

${worker}.on('faled', async(job, err) => {
  ${logger}.error(`failed job ${job.id}, error: ${err}`);
});

export {
  ${queue},
  ${worker}
}
