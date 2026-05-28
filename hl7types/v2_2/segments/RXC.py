"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class RXC(BaseModel):
    """HL7 v2 RXC segment."""

    rxc_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxc_1",
            "rx_component_type",
            "RXC.1",
        ),
        serialization_alias="RXC.1",
        title="RX Component Type",
        description="Item #313 | Table HL70166",
    )

    rxc_2: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxc_2",
            "component_code",
            "RXC.2",
        ),
        serialization_alias="RXC.2",
        title="Component Code",
        description="Item #314",
    )

    rxc_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxc_3",
            "component_amount",
            "RXC.3",
        ),
        serialization_alias="RXC.3",
        title="Component Amount",
        description="Item #315",
    )

    rxc_4: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxc_4",
            "component_units",
            "RXC.4",
        ),
        serialization_alias="RXC.4",
        title="Component Units",
        description="Item #316",
    )

    model_config = {"populate_by_name": True}
