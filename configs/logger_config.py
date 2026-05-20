import logging
from pathlib import Path


class LoggerConfig:
    LOGS_DIR_NAME = "logs"
    LOGGER_NAME = "Logger"

    LOGS_DIR = Path(LOGS_DIR_NAME)
    LOGS_FILE_NAME = LOGS_DIR / "test.log"

    LOGS_LEVEL = logging.INFO

    MAX_BYTES = 100_000
    BACKUP_COUNT = 10

    FORMAT = "[%(asctime)s | %(levelname)s] %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"