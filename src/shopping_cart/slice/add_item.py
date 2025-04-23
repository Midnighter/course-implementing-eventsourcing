from functools import reduce
from typing import cast
from uuid import UUID

from eventsourcing.persistence import EventStore
from fastapi import APIRouter, status, Request

from shopping_cart.command import AddItem
from shopping_cart.event import DomainEvent, ItemAdded


def _project_item_ids(items: list, event: DomainEvent) -> list[UUID]:
    match event:
        case ItemAdded():
            items.append(event.item_id)

    return items


def add_item(events: list[DomainEvent], command: AddItem) -> list[DomainEvent]:
    item_ids: list[UUID] = reduce(_project_item_ids, events, [])

    if len(item_ids) >= 3:
        raise AssertionError("You can have only three items in your cart.")

    return [
        ItemAdded(
            originator_id=command.cart_id,
            originator_version=1,
            timestamp=DomainEvent.now(),
            item_id=command.item_id,
            product_id=command.product_id,
            name=command.name,
            description=command.description,
            price=command.price,
        ),
    ]


def handle_add_item(event_store: EventStore, command: AddItem) -> None:
    events = cast("list[DomainEvent]", event_store.get(originator_id=command.cart_id))
    result = add_item(events, command)
    event_store.put(result)


router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def http_add_item(request: Request, cart_id: UUID, item: AddItem):
    handle_add_item(request.state.event_store, item)
