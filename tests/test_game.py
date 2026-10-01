"""The example game runs on the engine, and its seed data loads."""

from terraforma.seed import load_seed

from example_game import GAME


def test_the_engine_serves_this_game(app_client):
    assert app_client.get("/api/about").json()["game"] == "TerraForma Example Game"


def test_the_seed_loads():
    seed = load_seed(GAME.seed_dir)
    assert [monster["name"] for monster in seed["monsters"]] == ["Slime", "Cave Bat"]
