import * as winston from 'winston';
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const { combine, timestamp, printf, align } = winston.format;

const console_logger = winston.createLogger({
  level: 'debug',
  format: combine(
    timestamp({
      format: 'YYYY-MM-DD hh:mm:ss.SSS A'
    }),
    align(),
    printf((info) => `[${info.timestamp}] ${info.level}: ${info.message}`)
  ),
  transports: [new winston.transports.Console()],
});

const file_logger = winston.createLogger({
  level: 'debug',
  format: combine(
    timestamp({
      format: 'YYYY-MM-DD hh:mm:ss.SSS A'
    }),
    align(),
    printf((info) => `[${info.timestamp}] ${info.level}: ${info.message}`)
  ),
  transports: [
    new winston.transports.File({filename: __dirname + `/logs/${name}_all.log`}),
    new winston.transports.File({filename: __dirname + `/logs/${name}_warn.log`, level: 'warn'})
  ],
});

export{
  console_logger,
  file_logger
}
