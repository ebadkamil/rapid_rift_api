import logging
import os
from logging.handlers import RotatingFileHandler

from . import ROOT_PATH


class RapidFormatter(logging.Formatter):
    custom_format = "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s() | %(message)s"

    def format(self, record):
        formatter = logging.Formatter(self.custom_format, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


def get_logger(
    name: str,
    level: int = logging.DEBUG,
) -> logging.Logger:
    logger = logging.getLogger(name)
    console_handler = logging.StreamHandler()
    log_file = os.path.join(ROOT_PATH, name + ".log")

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=50000000,  # 50 MB files at max
        backupCount=5,  # Keep 5 backups
    )
    console_handler.setFormatter(RapidFormatter())
    file_handler.setFormatter(RapidFormatter())

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.setLevel(level)
    return logger


logger = get_logger("rapid-rift-api")
