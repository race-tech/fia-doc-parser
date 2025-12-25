from typing import Annotated
from datetime import timedelta

from pydantic import (
    BaseModel,
    ConfigDict,
    BeforeValidator,
    PositiveInt,
    NonNegativeFloat,
    NonNegativeInt,
)

from fia_doc_parser.models.foreign_key import SessionEntryForeignKeys
from fia_doc_parser.models.utils import mutate_timedelta_from_dict


class SessionEntryObject(BaseModel):
    position: PositiveInt | None = None
    is_classified: bool | None = None
    status: int | None = None
    detail: str | None = None
    points: NonNegativeFloat | None = None
    is_eligible_for_points: bool | None = None
    grid: PositiveInt | None = None
    time: Annotated[timedelta | None, BeforeValidator(mutate_timedelta_from_dict)] = (
        None
    )
    fastest_lap_rank: PositiveInt | None = None
    laps_completed: NonNegativeInt | None = None
    time: dict[str, str | int] | None = None

    model_config = ConfigDict(extra="forbid")


class SessionEntryImport(BaseModel):
    object_type: str = "SessionEntry"
    foreign_keys: SessionEntryForeignKeys
    objects: list[SessionEntryObject]

    model_config = ConfigDict(extra="forbid")
