"""A shim module to refine pytest.fixture to a concrete type."""
from __future__ import annotations

from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

import pytest
from pytest_mock import MockerFixture

if TYPE_CHECKING:
    from typing_extensions import Protocol

    class TakesMocker(Protocol):
        """A protocol for a fixture that takes a MockerFixture."""

        def __call__(self, mocker: MockerFixture) -> object:
            """A Higher-Order fixture that takes a MockerFixture."""
            ...

    class TakesNothing(Protocol):
        """A protocol for a fixture that takes nothing."""

        def __call__(self) -> object:
            """A Higher-Order fixture that takes a MockerFixture."""
            ...


fixture: Callable[[Union[TakesMocker, TakesNothing]], object] = pytest.fixture
