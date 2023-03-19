from __future__ import annotations

import pytest
from pydantic import ValidationError

from api.models.hello import Hello


def it_creates_a_hello_response() -> None:
    Hello(message='Hello, World!')


def it_does_not_allow_extra_values() -> None:
    with pytest.raises(ValidationError, match='extra fields not permitted'):
        Hello(message='Hello, World!', invalid='wow')  # type: ignore[call-arg]
