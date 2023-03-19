"""Hello model.

This is the model in use for the /hello endpoint.
"""

from __future__ import annotations

from pydantic import (
    BaseModel,
    Extra,
)


class Hello(BaseModel):
    """Hello Model."""

    class Config:
        extra = Extra.forbid

    message: str
