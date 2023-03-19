from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add a command line option to disable logger."""
    parser.addoption(
        '--log-disable',
        action='append',
        default=[],
        help='disable specific loggers',
    )


def pytest_configure(config: pytest.Config) -> None:
    """Disable the loggers."""
    for name in config.getoption('--log-disable', default=[]):
        logger = logging.getLogger(name)
        logger.propagate = False
