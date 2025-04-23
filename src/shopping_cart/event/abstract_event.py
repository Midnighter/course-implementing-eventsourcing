"""Provide an abstract base event model."""

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict


class AbstractEvent(BaseModel):
    """Define the abstract base event model."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    @classmethod
    def create_id(cls) -> UUID:
        """Return a random UUID."""
        return uuid4()

    @classmethod
    def now(cls) -> datetime:
        """Return the current time localized to the UTC timezone."""
        return datetime.now(tz=timezone.utc)
