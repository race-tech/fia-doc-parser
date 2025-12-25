from typing import Any
from datetime import timedelta

from pydantic import BaseModel, ConfigDict, NonNegativeInt


class TimedeltaModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    milliseconds: NonNegativeInt = 0
    seconds: NonNegativeInt = 0
    minutes: NonNegativeInt = 0
    hours: NonNegativeInt = 0
    days: NonNegativeInt = 0

    def to_timedelta(self) -> timedelta:
        return timedelta(**self.model_dump())


def mutate_timedelta_from_dict(value: Any) -> Any:
    if isinstance(value, dict) and value.get("_type") == "timedelta":
        return TimedeltaModel(
            **{key: val for key, val in value.items() if key != "_type"}
        ).to_timedelta()
    return value
