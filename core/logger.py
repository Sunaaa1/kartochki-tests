import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from configs.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)

    _logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    _logger.setLevel(LoggerConfig.LOGS_LEVEL)

    _handler1 = RotatingFileHandler(
        LoggerConfig.LOGS_FILE_NAME,
        maxBytes=LoggerConfig.MAX_BYTES,
        backupCount=LoggerConfig.BACKUP_COUNT,
        encoding="utf-8"
    )

    _handler2 = logging.StreamHandler(sys.stdout)
    _formatter = logging.Formatter(LoggerConfig.FORMAT)
    _handler1.setFormatter(_formatter)
    _handler2.setFormatter(_formatter)
    _logger.addHandler(_handler1)
    _logger.addHandler(_handler2)

    @staticmethod
    def set_level(level: str | int) -> None:
        Logger._logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        Logger._logger.info(message)

    @staticmethod
    def debug(message: str) -> None:
        Logger._logger.debug(message)

    @staticmethod
    def warning(message: str) -> None:
        Logger._logger.warning(message)

    @staticmethod
    def error(message: str) -> None:
        Logger._logger.error(message)

    @staticmethod
    def fatal(message: str) -> None:
        Logger._logger.fatal(message)

    @staticmethod
    def step(message: str) -> None:
        Logger._logger.info(message)