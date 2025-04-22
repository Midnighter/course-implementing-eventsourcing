"""Provide an abstract base command model."""


from pydantic import BaseModel, ConfigDict


class AbstractCommand(BaseModel):
    """Define the abstract base command model."""

    model_config = ConfigDict(frozen=True, extra="forbid")
