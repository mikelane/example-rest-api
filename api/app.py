"""Starlite App.

This is the main entrypoint for the Starlite API. It is responsible for
creating the application and configuring it.
"""
from __future__ import annotations

import uvicorn
from starlite import Starlite

from api.controllers.hello import HelloController
from api.logger import (
    logging_config,
    logging_middleware,
)
from api.settings import settings

app = Starlite(
    route_handlers=[HelloController],
    debug=settings.debug,
    logging_config=logging_config,
    middleware=[logging_middleware] if not settings.debug else [],
)

if __name__ == '__main__':
    uvicorn.run(app, port=57575)
