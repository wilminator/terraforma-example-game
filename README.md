# TerraForma example game

The smallest game you can build on the [TerraForma RPG Engine](https://github.com/wilminator/terraforma). Copy it to start your own.

A game is a Python package that holds:
- its content (JSON seed data in `seed/`),
- its assets,
- a `Game` it hands to the engine.

The engine does everything else: accounts, server calls, live fights, the database, the world.

```sh
pip install -e ".[dev]"
cp settings.example.toml settings.toml       # set session_secret
python -m terraforma serve example_game:app  # checks settings, migrates, serves on :8000
pytest
```

## Licenses

- **This example:** MIT, so you can copy any of it into your own game.
- **The engine:** AGPL-3.0 with an additional permission. A game that uses the engine through its public interfaces (`Game`, `create_app`, the seed formats, `terraforma.testing`) may use any license, including a closed one. Changes to the engine itself stay AGPL. See the engine's `LICENSE-EXCEPTION.md`.
