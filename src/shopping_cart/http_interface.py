"""Provide an HTTP interface to the shopping cart application."""

from contextlib import asynccontextmanager
from typing import TypedDict, AsyncIterator
from uuid import UUID

from eventsourcing.persistence import EventStore
from fastapi import FastAPI, Request

from .application import ShoppingCartApplication
from .slice.add_item import router as add_item_router


class ApplicationState(TypedDict):
    event_store: EventStore


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[ApplicationState]:
    yield ApplicationState(
        event_store=ShoppingCartApplication().construct_event_store()
    )


app = FastAPI(title="Shopping Cart Application", lifespan=lifespan)
app.include_router(add_item_router, prefix="/carts/{cart_id}")


@app.get("/carts/{cart_id}/log", tags=["carts"])
def read_events(request: Request, cart_id: UUID):
    events = request.state.event_store.get(originator_id=cart_id)
    return {"events": [type(event).__name__ for event in events]}
