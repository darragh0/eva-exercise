# EVA Analysis

Analyses spacewalk (EVA) data from `eva-data.json`: total duration per country, a country-vs-country comparison over a
year range, and cumulative and annual duration charts.

## Setup & Run

Requires [uv](https://docs.astral.sh/uv/).

```sh
uv sync
uv run python -m eva   # run from the repo root
uv run pytest          # run tests
```

## Architecture

Each module owns one responsibility; data flows one way.

```
loader  →  preparation  →  analysis  →  cli / charts
(read)     (validate)      (calculate)  (present)
```

| Module           | Responsibility                                                       |
| ---------------- | -------------------------------------------------------------------- |
| `models.py`      | Shared data types (`RawEva`, `EvaRecord`, `YearRange`, result types) |
| `loader.py`      | Read the JSON file                                                   |
| `preparation.py` | Skip incomplete records; parse dates and durations into `EvaRecord`s |
| `analysis.py`    | Pure calculations (no I/O)                                           |
| `cli.py`         | Prompt for input and print results                                   |
| `charts.py`      | Draw and save charts (the only module using matplotlib)              |
| `__main__.py`    | Coordinate: load → prepare → analyse → present                       |

Calculations take and return plain data, so they can be tested without files, prompts or plots (see `tests/`).

## Architectural Decisions

See [`docs/adr.md`](docs/adr.md).
