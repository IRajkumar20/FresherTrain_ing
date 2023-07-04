import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
filehand=logging.StreamHandler()
logger.addHandler(filehand)
logger.info("this is logger method")





