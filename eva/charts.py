from typing import TYPE_CHECKING

import matplotlib.pyplot as plt

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from datetime import datetime
    from pathlib import Path


def plot_cumulative(dates: Sequence[datetime], totals: Sequence[float], path: Path) -> None:
    fig, ax = plt.subplots()
    # matplotlib's stubs omit datetime, but it plots dates natively
    ax.plot(dates, totals)  # pyright: ignore[reportArgumentType]
    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative EVA duration (hours)")
    fig.tight_layout()
    fig.savefig(path)


def plot_annual(annual_hours: Mapping[int, float], path: Path) -> None:
    fig, ax = plt.subplots()
    ax.bar(list(annual_hours), list(annual_hours.values()))
    ax.set_xlabel("Year")
    ax.set_ylabel("Annual EVA duration (hours)")
    fig.tight_layout()
    fig.savefig(path)


def show_charts() -> None:
    plt.show()
