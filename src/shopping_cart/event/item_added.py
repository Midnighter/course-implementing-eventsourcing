from __future__ import annotations

from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from .domain_event import DomainEvent


class ItemAddedPayload(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    item_id: int
    product_id: UUID
    name: str
    description: str
    price: Decimal


class ItemAdded(DomainEvent):

    payload: ItemAddedPayload

