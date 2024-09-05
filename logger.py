import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create a StreamHandler and set its log level to DEBUG
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and attach it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Create a logger and add the console handler
logger = logging.getLogger(__name__)
logger.addHandler(console_handler)

# Log messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

# https://www.samyakinfo.tech/blog/logging-in-python
