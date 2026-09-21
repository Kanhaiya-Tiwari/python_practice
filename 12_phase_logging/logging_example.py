import logging
from logging.handlers import RotatingFileHandler


# Basic configuration for file logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('app.log', maxBytes=1024, backupCount=3)
    ]
)

logger = logging.getLogger("demo_logger")


# Example function

def process_data(data):
    logger.info("Processing started")
    if not data:
        logger.warning("No data received")
        return

    logger.info("Data processed successfully")
    return data


if __name__ == "__main__":
    process_data([1, 2, 3])
    process_data([])
    logger.error("This is an error example")
