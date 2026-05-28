"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: TS
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class TS(BaseModel):
    """HL7 v2 TS data type."""

    ts_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_1",
            "time_of_an_event",
            "TS.1",
        ),
        serialization_alias="TS.1",
        title="time of an event",
    )

    ts_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_2",
            "degree_of_precision",
            "TS.2",
        ),
        serialization_alias="TS.2",
        title="degree of precision",
    )

    model_config = {"populate_by_name": True}
