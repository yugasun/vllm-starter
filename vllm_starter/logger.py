import logging
import os
import sys
from enum import Enum

from loguru import logger

# Remove existing handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller to get correct stack depth
        frame, depth = logging.currentframe(), 2
        while frame.f_back and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


# Intercept standard logging
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)


loggers = (
    "uvicorn",
    "uvicorn.access",
    "uvicorn.error",
    "fastapi",
    "asyncio",
    "starlette",
)

for logger_name in loggers:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = []
    logging_logger.propagate = True


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
