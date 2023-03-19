"""Hello controller.

This is the controller in use for the /hello endpoint.
"""
from __future__ import annotations

from pydantic import (
    BaseModel,
    Extra,
)
from starlite import (
    Controller,
    get,
    post,
)

from api.logger import logger
from api.models.hello import Hello


class HelloInput(BaseModel):
    """Hello Input Model."""

    class Config:
        extra = Extra.forbid

    wow: int


class HelloController(Controller):
    """Hello Controller."""

    path = '/hello'

    @get()
    async def get_hello_world(self) -> Hello:
        """Get A Hello String."""
        logger.info('get_hello_world was called')
        return Hello(message='Hello, world!')

    @get('/{name:str}')
    async def get_hello(self, name: str) -> Hello:
        """Get A Hello String."""
        logger.info('get_hello was called with {}', repr(name))
        return Hello(message=f'Hello, {name}!')

    @post('/{name:str}')
    async def post_hello(self, data: HelloInput, name: str) -> Hello:
        """Get A Hello String."""
        logger.info('post_hello was called with {}', data.json(), extra={'data': data})
        return Hello(message=f'Hello, {name}!')
