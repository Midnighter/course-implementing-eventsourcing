# Shopping Cart

| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Meta | [![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/) [![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) |
| Automation |                                                                                                                                                                                                                                                                                                                                                                                                                                       |

_A sample project that implements a few vertical slices of a shopping cart event model using event sourcing._

## Usage

This project uses [hatch](https://hatch.pypa.io),
please [install it](https://hatch.pypa.io/latest/install/) before going further.
You can quickly do so with `pipx`.

```shell
pipx install hatch
```

To just try things out, you then enter the configured `dev` environment.

```shell
hatch -e dev shell
```

Now, you can start the FastAPI application

```shell
fastapi dev src/shopping_cart/http_interface.py
```

and look at the [documentation](http://127.0.0.1:8000/docs).

## Copyright

- Copyright © 2025 Moritz E. Beber.
- Free software distributed under the [Apache Software License 2.0](./LICENSE).

