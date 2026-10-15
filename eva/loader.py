import json
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pathlib import Path

    from eva.models import RawEva


def load_evas(path: Path) -> list[RawEva]:
    with path.open(encoding="utf-8") as file:
        return cast("list[RawEva]", json.load(file))
