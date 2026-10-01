"""An example game on the TerraForma RPG Engine: the smallest module that runs.

A game is its content (seed data), assets and settings, handed to the
engine as a Game. Copy this package, rename it, and make it yours. Run it:

    python -m terraforma serve example_game:app
"""

from pathlib import Path

from terraforma.app import create_app
from terraforma.game import Game
from terraforma.settings import load_settings

HERE = Path(__file__).parent

GAME = Game(name="TerraForma Example Game", seed_dir=HERE / "seed", assets_dir=HERE / "assets")


def app():
    return create_app(load_settings(), GAME)
