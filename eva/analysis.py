from collections import defaultdict
from itertools import accumulate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable
    from datetime import datetime

    from eva.models import EvaRecord


def _chronological(records: Iterable[EvaRecord]) -> list[EvaRecord]:
    return sorted(records, key=lambda record: record.date)


def country_total(records: Iterable[EvaRecord], country: str) -> float:
    """Total EVA hours for `country`."""
    return sum(record.duration_hours for record in records if record.country == country)


def cumulative_hours(records: Iterable[EvaRecord]) -> tuple[list[datetime], list[float]]:
    """Dates in chronological order, paired with running total of EVA hours."""
    ordered = _chronological(records)
    dates = [record.date for record in ordered]
    totals = list(accumulate(record.duration_hours for record in ordered))
    return dates, totals


def annual_hours(records: Iterable[EvaRecord]) -> dict[int, float]:
    """Total EVA hours per year, chronological order."""
    totals: defaultdict[int, float] = defaultdict(float)
    for record in _chronological(records):
        totals[record.date.year] += record.duration_hours
    return dict(totals)
