import math
from collections import defaultdict
from itertools import accumulate
from typing import TYPE_CHECKING

from eva.models import CountryComparison, CountryStats

if TYPE_CHECKING:
    from collections.abc import Iterable
    from datetime import datetime

    from eva.models import EvaRecord, YearRange


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


def countries(records: Iterable[EvaRecord]) -> list[str]:
    """Sorted names of all countries with at least one EVA."""
    return sorted({record.country for record in records})


def country_stats(records: Iterable[EvaRecord], country: str, years: YearRange) -> CountryStats:
    """EVA count, total and average hours for `country` within `years`."""
    in_years = [record for record in records if record.date.year in years]
    total = country_total(in_years, country)
    count = sum(1 for record in in_years if record.country == country)
    return CountryStats(
        country=country,
        eva_count=count,
        total_hours=total,
        average_hours=total / count if count else None,
    )


def compare_countries(records: Iterable[EvaRecord], first: str, second: str, years: YearRange) -> CountryComparison:
    """Stats for both countries within `years`, and which has the greater total."""
    records = list(records)
    first_stats = country_stats(records, first, years)
    second_stats = country_stats(records, second, years)

    if math.isclose(first_stats.total_hours, second_stats.total_hours):
        leader = None
    elif first_stats.total_hours > second_stats.total_hours:
        leader = first
    else:
        leader = second

    return CountryComparison(years=years, first=first_stats, second=second_stats, leader=leader)
