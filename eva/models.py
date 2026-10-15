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
