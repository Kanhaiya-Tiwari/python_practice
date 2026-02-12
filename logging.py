#Logging
#Concept: Proper script logs
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Deployment started")
logging.error("Deployment failed")
#👉 Used in production scripts