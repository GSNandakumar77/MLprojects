import logging 
import os 
from datetime import datetime

# Generate log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logspath = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logspath, exist_ok=True)
LOG_FILE_PATH = os.path.join(logspath, LOG_FILE)

# Setup logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
