from typing import Literal

from pydantic import ConfigDict, PositiveInt

from fia_doc_parser.models.foreign_key import PitStopForeignKeys

class PitStopObject():
    number: PositiveInt | None = None
    local_timestamp: str | None = None
    duration: dict[str, str | int]

    model_config = ConfigDict(extra="forbid")


class PitStopData():
    object_type: Literal["PitStop", "pit_stop"]
    foreign_keys: PitStopForeignKeys
    objects: list[PitStopObject]

    model_config = ConfigDict(extra="forbid")
