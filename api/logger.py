"""Logger configuration."""
from __future__ import annotations

import sys

from loguru import logger as logger_
from starlite import (
    BaseLoggingConfig,
    LoggingConfig,
    StructLoggingConfig,
)
from starlite.middleware import LoggingMiddlewareConfig

from api.settings import settings

logging_config: BaseLoggingConfig

if settings.debug:
    logging_config = LoggingConfig(
        formatters={
            'standard': {
                'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
            },
        },
        root={
            'level': 'DEBUG',
            'handlers': ['queue_listener'],
        },
        loggers={
            'starlite': {
                'level': 'DEBUG',
                'handlers': ['queue_listener'],
            },
            'app': {
                'level': 'DEBUG',
                'handlers': ['queue_listener'],
            },
        },
        propagate=True,
    )
else:
    logging_config = StructLoggingConfig()


_logging_config_middleware = LoggingMiddlewareConfig()
logging_middleware = _logging_config_middleware.middleware


logger = logger_.bind(name='app')
if not settings.debug:
    logger.remove(0)
    logger.add(sys.stdout, serialize=True)
