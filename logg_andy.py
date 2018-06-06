import logging

logging.basicConfig(level=logging.DEBUG,filename="log.txt")
logging.debug("Default info")
logging.info("This is an info")
logging.warning('Warning Msg')
logging.error("Error msg")
