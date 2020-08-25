from __future__ import annotations

from typing import Callable

import pytest

fixture: Callable[[object], Callable[..., object]] = pytest.fixture
