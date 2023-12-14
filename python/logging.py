import subprocess

import logging


logging.basicConfig(filename=f'file.log', filemode='a', format='[%(asctime)s] %(message)s', level=logging.DEBUG)

logging.info(f"{log}")


# multiple loggers

def setup_logger(name, format,log_file='get-module-function.log', level=logging.DEBUG):
  """To setup as many loggers as you want"""

  handler = logging.FileHandler(log_file)        
  handler.setFormatter(format)

  logger = logging.getLogger(name)
  logger.setLevel(level)
  logger.addHandler(handler)

  return logger

general_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [general] %(message)s')
query_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [query]   %(message)s')

general_logger = setup_logger('general_logger', general_format)
query_logger = setup_logger('query_logger', query_format)


query_logger.info(f"query for module:{path}, function:{function}, file:{file}")

general_logger.info(f'----- function call:{external_func_call}, file:{caller_file}, line:{line}')
