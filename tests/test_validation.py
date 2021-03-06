"""Test cases for the validation module."""
from typing import Any
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
from tomlkit.exceptions import TOMLKitError

from toml_validator import validation


@pytest.fixture
def mock_tomlkit_parse(mocker: MockFixture) -> Any:
    """Fixture for mocking tomlkit.parse."""
    return mocker.patch("tomlkit.parse")


@pytest.fixture
def mock_tomlkit_parse_exception(mocker: MockFixture) -> Any:
    """Fixture for mocking tomlkit.parse."""
    mock = mocker.patch("tomlkit.parse")
    mock.side_effect = TOMLKitError("|some tomlkit error|")
    return mock


@pytest.fixture
def mock_open_valid_file(mocker: MockFixture) -> Any:
    """Fixture for mocking build-in open for valid TOML file."""
    return mocker.patch("builtins.open", mocker.mock_open(read_data="[x]\na = 3"))


@pytest.fixture
def mock_open_invalid_file(mocker: MockFixture) -> Any:
    """Fixture for mocking build-in open for valid TOML file."""
    return mocker.patch(
        "builtins.open", mocker.mock_open(read_data="[x]\na = 3\n[x]\na = 3")
    )


def test_validate_extension_valid() -> None:
    """It returns nothing when extension is valid."""
    assert validation.validate_extension("file.toml")


def test_validate_extension_invalid() -> None:
    """It raises `SystemExit` when extensio is invalid."""
    with pytest.raises(SystemExit):
        assert validation.validate_extension("file.xml")


def test_validate_toml_no_error(
    mock_open_valid_file: Mock, mock_tomlkit_parse: Mock
) -> None:
    """It returns no errors when valid TOML."""
    assert validation.validate_toml("file.toml") == ""


def test_validate_toml_with_error(
    mock_open_invalid_file: Mock, mock_tomlkit_parse_exception: Mock
) -> None:
    """It returns errors when invalid TOML."""
    assert validation.validate_toml("file.toml") == "|some tomlkit error|"


@pytest.mark.e2e
def test_validate_toml_no_error_production(mock_open_valid_file: Mock) -> None:
    """It returns no errors when valid TOML (e2e)."""
    assert validation.validate_toml("file.toml") == ""


@pytest.mark.e2e
def test_validate_toml_with_error_production(mock_open_invalid_file: Mock) -> None:
    """It returns errors when invalid TOML (e2e)."""
    assert validation.validate_toml("file.toml") == 'Key "x" already exists.'
