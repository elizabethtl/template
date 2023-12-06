import subprocess

import logging


logging.basicConfig(filename=f'file.log', filemode='a', format='[%(asctime)s] %(message)s', level=logging.DEBUG)

logging.info(f"{log}")
