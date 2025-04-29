import logging
import os
import sys
from enum import Enum

from loguru import logger


def setup_logger(level: str = "INFO"):
    logger.remove(None)

    logger.add(sys.stdout, level=level, colorize=True)

    logger.add(
        "run.log",
        level=level,
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        # format="{message}",
        colorize=False,
        serialize=True,
        backtrace=True,
        diagnose=True,
    )

    return logger
