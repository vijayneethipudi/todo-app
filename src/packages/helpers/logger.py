import logging
import logging.config
import os

ROOT_LEVEL = os.environ.get("PROD", "INFO")
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"standard": {"format": "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"}},
    "handlers": {
        "default": {
            "level": ROOT_LEVEL,
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "": {"level": ROOT_LEVEL, "handlers": ["default"], "propagate": False},  # root logger
        "uvicorn.error": {"level": "DEBUG", "handlers": ["default"]},
        "uvicorn.access": {"level": "DEBUG", "handlers": ["default"]},
    },
}

logger_blocklist = ["paramiko"]

for module in logger_blocklist:
    logging.getLogger(module).setLevel(logging.WARNING)

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)

# test logging
logger.debug("debug message")
logger.info("debug message")
logger.warning("debug message")
logger.error("debug message")
logger.critical("debug message")
