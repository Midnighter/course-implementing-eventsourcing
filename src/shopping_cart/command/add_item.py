from __future__ import annotations

from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AddItem(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    item_id: int
    product_id: UUID
    name: str
    description: str
    price: Decimal