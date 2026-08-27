# Logging se 3 messages (info, warning, error) print karo timestamps ke saath.

'''

'''

import logging

from datetime import datetime

logging.basicConfig(level=logging.INFO  ,  format="%(asctime)s - %(levelname)s - %(message)s")


logging.info("This is logging message .")

logging.warning("This is warning messages")

logging.error("This is error messages ")

