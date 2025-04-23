import pytest
from eventsourcing.persistence import EventStore
from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture

from shopping_cart.command import AddItem
from shopping_cart.event import ItemAdded
from shopping_cart.slice.add_item import add_item, handle_add_item


@register_fixture(name="command_factory")
class AddItemCommandFactory(ModelFactory[AddItem]): ...


@register_fixture(name="event_factory")
class ItemAddedEventFactory(ModelFactory[ItemAdded]): ...


def test_adding_one_item_succeeds(command_factory: AddItemCommandFactory):
    add_item(events=[], command=command_factory.build())


def test_adding_more_than_three_items_fails(
    event_factory: ItemAddedEventFactory, command_factory: AddItemCommandFactory
):
    with pytest.raises(AssertionError):
        add_item(
            events=[
                event_factory.build(),
                event_factory.build(),
                event_factory.build(),
            ],
            command=command_factory.build(),
        )


def test_handle_add_item(
    memory_store: EventStore,
    event_factory: ItemAddedEventFactory,
    command_factory: AddItemCommandFactory,
):
    cart_id = ItemAdded.create_id()
    add_item_cmd = command_factory.build(cart_id=cart_id)
    events = [
        event_factory.build(originator_id=cart_id),
        event_factory.build(originator_id=cart_id),
        event_factory.build(originator_id=cart_id),
    ]
    memory_store.put(events)
    with pytest.raises(AssertionError):
        handle_add_item(memory_store, add_item_cmd)
