from __future__ import annotations

from typing import Callable, TypeVar, cast

import pytest

T = TypeVar('T')

def e2e(f: T) -> T:
    return cast(T, pytest.mark.e2e(f))
