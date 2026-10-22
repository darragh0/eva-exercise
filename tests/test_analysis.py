from datetime import datetime

import pytest

from eva.analysis import annual_hours, compare_countries
from eva.models import CountryStats, EvaRecord, YearRange

RECORDS = [
    EvaRecord(date=datetime(2001, 3, 1), duration_hours=4.0, country="USA"),
    EvaRecord(date=datetime(2000, 6, 1), duration_hours=2.0, country="USA"),
    EvaRecord(date=datetime(2001, 9, 1), duration_hours=3.0, country="Russia"),
    EvaRecord(date=datetime(2005, 1, 1), duration_hours=6.0, country="Russia"),
]


def test_compare_countries() -> None:
    comparison = compare_countries(RECORDS, "USA", "Russia", YearRange(2000, 2001))

    assert comparison.first == CountryStats("USA", eva_count=2, total_hours=6.0, average_hours=3.0)
    assert comparison.second == CountryStats("Russia", eva_count=1, total_hours=3.0, average_hours=3.0)
    assert comparison.leader == "USA"


def test_annual_hours() -> None:
    assert annual_hours(RECORDS) == {2000: 2.0, 2001: 7.0, 2005: 6.0}


def test_year_range_rejects_start_after_end() -> None:
    with pytest.raises(ValueError, match="after end year"):
        _ = YearRange(2001, 2000)
