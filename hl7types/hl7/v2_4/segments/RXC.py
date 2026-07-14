"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RXC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class RXC(HL7Model):
    """Pharmacy/Treatment Component Order (S4.14.3).

    Attributes
    ----------
    rxc_1 : str
        RXC.1 (req) - RX Component Type (ID) S4.14.3.1 | 0166 - RX component type

    rxc_2 : CE
        RXC.2 (req) - Component Code (CE) S4.14.3.2

    rxc_3 : str
        RXC.3 (req) - Component Amount (NM) S4.14.3.3

    rxc_4 : CE
        RXC.4 (req) - Component Units (CE) S4.14.3.4

    rxc_5 : str | None
        RXC.5 (opt) - Component Strength (NM) S4.14.3.5

    rxc_6 : CE | None
        RXC.6 (opt) - Component Strength Units (CE) S4.14.3.6

    rxc_7 : list[CE] | None
        RXC.7 (opt, rep) - Supplementary Code (CE) S4.14.5.25
    """

    rxc_1: str = Field(
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

    @field_validator("rxc_3", "rxc_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
