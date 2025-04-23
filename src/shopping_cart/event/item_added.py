from decimal import Decimal
from uuid import UUID

from .domain_event import DomainEvent


class ItemAdded(DomainEvent):
    item_id: UUID
    product_id: UUID
    name: str
    description: str
    price: Decimal
