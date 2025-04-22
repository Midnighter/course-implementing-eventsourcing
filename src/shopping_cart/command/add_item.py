"""Provide an add item command."""


from decimal import Decimal
from uuid import UUID

from .abstract_command import AbstractCommand


class AddItem(AbstractCommand):
    """Define the add item command."""

    item_id: int
    product_id: UUID
    name: str
    description: str
    price: Decimal
