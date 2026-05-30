"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RXC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class RXC(HL7Model):
    """HL7 v2 RXC segment.

    Attributes
    ----------
    rxc_1 : str
        RXC.1 (req) - RX Component Type (ID)

    rxc_2 : CE
        RXC.2 (req) - Component Code (CE)

    rxc_3 : str
        RXC.3 (req) - Component Amount (NM)

    rxc_4 : CE
        RXC.4 (req) - Component Units (CE)

    rxc_5 : str | None
        RXC.5 (opt) - Component Strength (NM)

    rxc_6 : CE | None
        RXC.6 (opt) - Component Strength Units (CE)

    rxc_7 : list[CE] | None
        RXC.7 (opt, rep) - Supplementary Code (CE)
    """

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

    rxc_5: Optional[str] = Field(
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

    rxc_6: Optional[CE] = Field(
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

    rxc_7: Optional[List[CE]] = Field(
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

    model_config = {"populate_by_name": True}
