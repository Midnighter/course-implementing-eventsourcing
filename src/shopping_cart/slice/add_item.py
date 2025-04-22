from __future__ import annotations

from functools import reduce

from shopping_cart.event import ItemAdded, DomainEvent
from shopping_cart.command import AddItem


def _project_item_ids(items: list, event: DomainEvent) -> list:
    match event:
        case ItemAdded():
            items.append(event.payload.item_id)

    return items


def add_item(events: list[DomainEvent], command: AddItem) -> list[DomainEvent]:
    item_ids = reduce(_project_item_ids, events, [])

    if len(item_ids) >= 3:
        raise AssertionError("You can have only three items in your cart.")

    return [ItemAdded(
        metadata=EventMetaData(
            originator_id=DomainEvent.create_id(),
            originator_version=1,
            timestamp=DomainEvent.now(),
        ),
        payload=ItemAddedPayload(
            item_id=command.item_id,
            product_id=command.product_id,
            name=command.name,
            description=command.description,
            price=command.price,
        ),
    )]
