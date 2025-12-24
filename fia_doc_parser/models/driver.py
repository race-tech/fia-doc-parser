"""Driver entry models"""
from typing import Literal

from pydantic import (
    ConfigDict,
    BaseModel,
    PositiveInt
)

from .foreign_key import RoundEntry

class RoundEntryObject(BaseModel):
    model_config = ConfigDict(extra="forbid")

    car_number: PositiveInt | None = None

class RoundEntryImport(BaseModel):
    object_type: Literal["RoundEntry"]
    foreign_keys: RoundEntry
    objects: list[RoundEntryObject]

    model_config = ConfigDict(extra="forbid")
