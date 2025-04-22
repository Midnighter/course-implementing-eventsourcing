"""Provide a domain event object."""


from datetime import datetime
from uuid import UUID

from .abstract_event import AbstractEvent


class DomainEvent(AbstractEvent):
    """Define the domain event object."""

    originator_id: UUID
    originator_version: int
    timestamp: datetime
