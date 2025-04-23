"""Test that domain events are persisted and fetched as expected."""

from eventsourcing.persistence import EventStore
from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture

from shopping_cart.event import DomainEvent


@register_fixture(name="event_factory")
class DomainEventFactory(ModelFactory[DomainEvent]):
    """Provide a factory for domain events."""
    ...


def test_event_persistence(memory_store: EventStore, event_factory: DomainEventFactory):
    """Test that domain events are persisted to and fetched from memory."""
    originator_id = DomainEvent.create_id()
    events = [event_factory.build(originator_id=originator_id),
              event_factory.build(originator_id=originator_id),
              event_factory.build(originator_id=originator_id)]
    memory_store.put(events)

    restored = memory_store.get(originator_id=originator_id)

    for event, expected in zip(restored, events):
        assert event == expected
