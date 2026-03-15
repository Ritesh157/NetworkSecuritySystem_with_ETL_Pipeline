import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # Ex: LOG_FILE = 03_16_2026_15_45_20.log

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # Ex: logs_path = C:/Users/Ritesh/Network_Security/logs/03_16_2026_15_45_20.log

os.makedirs(logs_path, exist_ok=True)                   # This creates folders automatically.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)       # This creates the final log file location. Ex: Network_Security/logs/03_16_2026_15_45_20.log/03_16_2026_15_45_20.log

logging.basicConfig(
    filename = LOG_FILE_PATH,                    # Save logs in this file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",     # how log messages look
    level=logging.INFO,
)