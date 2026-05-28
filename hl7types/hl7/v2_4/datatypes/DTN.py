"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DTN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class DTN(BaseModel):
    """HL7 v2 DTN data type."""

    dtn_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dtn_1",
            "day_type",
            "DTN.1",
        ),
        serialization_alias="DTN.1",
        title="day type",
    )

    dtn_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dtn_2",
            "number_of_days",
            "DTN.2",
        ),
        serialization_alias="DTN.2",
        title="number of days",
    )

    model_config = {"populate_by_name": True}
