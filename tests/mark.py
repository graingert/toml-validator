"""a shim module to refine pytest.mark to a concrete type."""
from __future__ import annotations

from typing import cast
from typing import TypeVar

import pytest

T = TypeVar("T")


def e2e(f: T) -> T:
    """Mark as end-to-end test."""
    return cast(T, pytest.mark.e2e(f))
