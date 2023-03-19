from __future__ import annotations

from http import HTTPStatus

import pytest
from starlite import (
    AsyncTestClient,
    Starlite,
)

from api.app import app


@pytest.fixture()
def async_client() -> AsyncTestClient[Starlite]:
    return AsyncTestClient(app)


@pytest.mark.asyncio()
async def it_runs_the_app(async_client: AsyncTestClient[Starlite]) -> None:
    response = await async_client.get('/hello')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, world!'}
