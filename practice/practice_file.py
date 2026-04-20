import logging

logging.basicConfig(level=logging.ERROR)

def login():
    logging.info("Login started")
    logging.error("Login failed")

login()

#import logging

#logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
logging.error("Error message1")
logging.debug("debug messag2")