from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict


class EventMetaData(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    originator_id: UUID
    originator_version: int
    timestamp: datetime


class DomainEvent(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    metadata: EventMetaData
    payload: Any

    @classmethod
    def create_id(cls) -> UUID:
        return uuid4()

    @classmethod
    def now(cls) -> datetime:
        return datetime.now(tz=timezone.utc)
