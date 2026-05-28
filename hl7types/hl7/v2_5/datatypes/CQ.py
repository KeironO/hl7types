"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CQ
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CQ(BaseModel):
    """HL7 v2 CQ data type."""

    cq_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_1",
            "quantity",
            "CQ.1",
        ),
        serialization_alias="CQ.1",
        title="Quantity",
    )

    cq_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_2",
            "units",
            "CQ.2",
        ),
        serialization_alias="CQ.2",
        title="Units",
    )

    model_config = {"populate_by_name": True}
