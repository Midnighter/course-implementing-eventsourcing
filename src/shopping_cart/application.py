"""Provide a customized shopping cart application."""

from eventsourcing.application import Application
from eventsourcing.persistence import Mapper

from .persistence import PydanticMapper


class ShoppingCartApplication(Application):
    """
    Define the customized shopping cart application.

    We only really need an `EventStore`. We could construct one directly using the
    `InfrastructureFactory`, but we use the provided application object to
    benefit from the built-in configuration via environment and customization via
    method overrides.

    Example:

        Create an application instance and construct an event store.

        ```py
        event_store = ShoppingCartApplication().construct_event_store()
        ```

    """

    def construct_mapper(self) -> Mapper:
        return self.factory.mapper(
            transcoder=self.construct_transcoder(),
            mapper_class=PydanticMapper,
        )
