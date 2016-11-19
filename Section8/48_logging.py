"""
Log severity:
 - Debug
 - Info
 - Warning
 - Error
 - Critical
"""

import logging

logging.basicConfig(level=logging.INFO, filename='example.log')

logging.debug("This will be ignored")
logging.info("This will be logged")
logging.warning("And this too")
