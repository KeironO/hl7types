"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RXC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class RXC(HL7Model):
    """Pharmacy component order segment (S4.8.4).

    Attributes
    ----------
    rxc_1 : str
        RXC.1 - RX Component Type (ID) R S4.8.4.1 | 0166 - RX Component Type

    rxc_2 : CE
        RXC.2 - Component Code (CE) R S4.8.4.2

    rxc_3 : str
        RXC.3 - Component Amount (NM) R S4.8.4.3

    rxc_4 : CE
        RXC.4 - Component Units (CE) R S4.8.4.4

    rxc_5 : str | None
        RXC.5 - Component Strength (NM) O S4.8.4.5

    rxc_6 : CE | None
        RXC.6 - Component Strength Units (CE) O S4.8.4.6
    """

    rxc_1: str = Field(
        validation_alias=AliasChoices(
            "rxc_1",
            "rx_component_type",
            "RXC.1",
        ),
        serialization_alias="RXC.1",
        title="RX Component Type",
        description="R | Item #00313 | Table 0166 - RX Component Type | LEN:1",
    )

    rxc_2: CE = Field(
        validation_alias=AliasChoices(
            "rxc_2",
            "component_code",
            "RXC.2",
        ),
        serialization_alias="RXC.2",
        title="Component Code",
        description="R | Item #00314",
    )

    rxc_3: str = Field(
        validation_alias=AliasChoices(
            "rxc_3",
            "component_amount",
            "RXC.3",
        ),
        serialization_alias="RXC.3",
        title="Component Amount",
        description="R | Item #00315 | LEN:20",
    )

    rxc_4: CE = Field(
        validation_alias=AliasChoices(
            "rxc_4",
            "component_units",
            "RXC.4",
        ),
        serialization_alias="RXC.4",
        title="Component Units",
        description="R | Item #00316",
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
        description="O | Item #01124 | LEN:20",
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
        description="O | Item #01125",
    )

    @field_validator("rxc_3", "rxc_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
