import sys
from typing import TYPE_CHECKING

from eva.models import YearRange

if TYPE_CHECKING:
    from collections.abc import Sequence

    from eva.models import CountryComparison, CountryStats


def _print_error(msg: str) -> None:
    print(msg, file=sys.stderr)


def prompt_country() -> str:
    return input("Enter a country: ")


def print_country_total(country: str, total_hours: float) -> None:
    print(f"Total EVA duration for {country}: {total_hours:.2f} hours")


def prompt_known_country(prompt: str, known: Sequence[str]) -> str:
    """Re-prompt until answer matches a country in `known` (case-insensitive)."""
    by_lowercase = {country.lower(): country for country in known}
    while True:
        answer = input(prompt).strip()
        if (country := by_lowercase.get(answer.lower())) is not None:
            return country
        _print_error(f"Unknown country {answer!r} -- choose from: {', '.join(known)}")


def _prompt_year(prompt: str) -> int:
    while True:
        answer = input(prompt).strip()

        try:
            return int(answer)
        except ValueError:
            _print_error(f"{answer!r} is not a year")


def prompt_year_range() -> YearRange:
    """Re-prompt until start year is not after end year."""
    while True:
        start = _prompt_year("Start year: ")
        end = _prompt_year("End year: ")

        try:
            return YearRange(start, end)
        except ValueError as err:
            _print_error(f"Invalid year range: {err}")


def _format_stats(stats: CountryStats) -> str:
    average = "unavailable" if stats.average_hours is None else f"{stats.average_hours:.2f} hours"
    return f"{stats.country}: {stats.eva_count} EVAs, total {stats.total_hours:.2f} hours, average {average}"


def print_comparison(comparison: CountryComparison) -> None:
    years = comparison.years
    print(f"\nEVA comparison, {years.start}-{years.end}:")
    print(f"  {_format_stats(comparison.first)}")
    print(f"  {_format_stats(comparison.second)}")

    if comparison.leader is None:
        print("Tie: both countries have the same total EVA duration")
    else:
        print(f"{comparison.leader} has the greater total EVA duration")
