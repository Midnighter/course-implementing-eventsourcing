"""Provide fixtures to the entire test suite."""

import pytest
from eventsourcing.persistence import EventStore
from eventsourcing.utils import Environment

from shopping_cart.application import ShoppingCartApplication


@pytest.fixture(scope="session")
def memory_store() -> EventStore:
    """Provide an in-memory event store."""
    environ = Environment()
    environ["PERSISTENCE_MODULE"] = "eventsourcing.popo"
    return ShoppingCartApplication(env=environ).construct_event_store()
