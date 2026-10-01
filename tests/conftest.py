"""The example game's tests use the engine's fixtures (terraforma.testing), serving this game."""

import pytest

pytest_plugins = ["terraforma.testing"]


@pytest.fixture
def game():
    from example_game import GAME

    return GAME
