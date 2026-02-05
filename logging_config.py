import sys
import logging
from colorlog import ColoredFormatter

def get_logger(name: str = "app"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if logger.handlers:
        return logger

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s | %(levelname)s | %(name)s:%(lineno)d | %(message)s",
        log_colors={
            "DEBUG":    "cyan",
            "INFO":     "green",
            "WARNING":  "yellow",
            "ERROR":    "red",
            "CRITICAL": "bold_red",
        },
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger