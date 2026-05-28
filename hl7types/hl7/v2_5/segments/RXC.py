"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RXC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE


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

    rxc_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_5",
            "component_strength",
            "RXC.5",
        ),
        serialization_alias="RXC.5",
        title="Component Strength",
        description="Item #1124",
    )

    rxc_6: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_6",
            "component_strength_units",
            "RXC.6",
        ),
        serialization_alias="RXC.6",
        title="Component Strength Units",
        description="Item #1125",
    )

    rxc_7: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_7",
            "supplementary_code",
            "RXC.7",
        ),
        serialization_alias="RXC.7",
        title="Supplementary Code",
        description="Item #1476",
    )

    rxc_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_8",
            "component_drug_strength_volume",
            "RXC.8",
        ),
        serialization_alias="RXC.8",
        title="Component Drug Strength Volume",
        description="Item #1671",
    )

    rxc_9: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_9",
            "component_drug_strength_volume_units",
            "RXC.9",
        ),
        serialization_alias="RXC.9",
        title="Component Drug Strength Volume Units",
        description="Item #1672",
    )

    model_config = {"populate_by_name": True}
