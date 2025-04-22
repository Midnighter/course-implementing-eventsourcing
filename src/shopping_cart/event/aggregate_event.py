"""Provide an aggregate event object."""


from datetime import datetime
from uuid import UUID

from .abstract_event import AbstractEvent


class AggregateEvent(AbstractEvent):
    """Define the aggregate event object."""

    id: UUID
    version: int
    created_on: datetime
    modified_on: datetime
