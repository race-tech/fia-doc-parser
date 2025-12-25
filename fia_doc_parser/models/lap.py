from pydantic import ConfigDict, PositiveFloat, PositiveInt

from fia_doc_parser.models.foreign_key import SessionEntryForeignKeys


class LapObject:
    number: PositiveInt | None = None
    position: PositiveInt | None = None
    average_speed: PositiveFloat | None = None
    is_entry_fastest_lap: bool | None = None
    is_deleted: bool | None = None

    time: dict[str, str | int]
    model_config = ConfigDict(extra="forbid")


class LapImport:
    foreign_keys: SessionEntryForeignKeys
    objects: list[LapObject]

    model_config = ConfigDict(extra="forbid")
