"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: DDI
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .MO import MO


class DDI(BaseModel):
    """HL7 v2 DDI data type."""

    ddi_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ddi_1",
            "delay_days",
            "DDI.1",
        ),
        serialization_alias="DDI.1",
        title="Delay Days",
    )

    ddi_2: MO = Field(
        default=...,
        validation_alias=AliasChoices(
            "ddi_2",
            "monetary_amount",
            "DDI.2",
        ),
        serialization_alias="DDI.2",
        title="Monetary Amount",
    )

    ddi_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ddi_3",
            "number_of_days",
            "DDI.3",
        ),
        serialization_alias="DDI.3",
        title="Number of Days",
    )

    model_config = {"populate_by_name": True}
