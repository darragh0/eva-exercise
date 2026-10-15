from dataclasses import dataclass
from typing import TYPE_CHECKING, NotRequired, TypedDict

if TYPE_CHECKING:
    from datetime import datetime


class RawEva(TypedDict):
    country: str
    date: NotRequired[str]
    duration: NotRequired[str]


@dataclass(frozen=True, slots=True)
class EvaRecord:
    date: datetime
    duration_hours: float
    country: str


@dataclass(frozen=True, slots=True)
class YearRange:
    """Inclusive range of years; raises `ValueError` if `start` is after `end`."""

    start: int
    end: int

    def __post_init__(self) -> None:
        if self.start > self.end:
            msg = f"start year ({self.start}) is after end year ({self.end})"
            raise ValueError(msg)

    def __contains__(self, year: int) -> bool:
        return self.start <= year <= self.end


@dataclass(frozen=True, slots=True)
class CountryStats:
    country: str
    eva_count: int
    total_hours: float
    average_hours: float | None  # None when there are no EVAs


@dataclass(frozen=True, slots=True)
class CountryComparison:
    years: YearRange
    first: CountryStats
    second: CountryStats
    leader: str | None  # None on a tie
