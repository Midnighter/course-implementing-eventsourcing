"""Provide an add item command."""

from decimal import Decimal
from uuid import UUID

from pydantic import Field

from .abstract_command import AbstractCommand


class AddItem(AbstractCommand):
    """Define the add item command."""

    cart_id: UUID
    item_id: UUID
    product_id: UUID
    name: str
    description: str
    price: Decimal = Field(ge=0)
