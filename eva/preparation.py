from datetime import datetime
from typing import TYPE_CHECKING

from eva.models import EvaRecord

if TYPE_CHECKING:
    from collections.abc import Iterable

    from eva.models import RawEva


def parse_duration(text: str) -> float:
    """Convert "H:MM" duration string to hours."""
    hours, minutes = map(int, text.split(":"))
    return hours + minutes / 60


def prepare(raw_evas: Iterable[RawEva]) -> list[EvaRecord]:
    """Convert raw EVAs to records; skip any without a date or duration."""
    return [
        EvaRecord(
            date=datetime.fromisoformat(date_text),
            duration_hours=parse_duration(duration_text),
            country=eva["country"],
        )
        for eva in raw_evas
        if (date_text := eva.get("date")) and (duration_text := eva.get("duration"))
    ]
