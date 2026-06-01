"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RXC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE


class RXC(HL7Model):
    """HL7 v2 RXC segment.

    Attributes
    ----------
    rxc_1 : str
        RXC.1 (req) - RX Component Type (ID)

    rxc_2 : CWE
        RXC.2 (req) - Component Code (CWE)

    rxc_3 : str
        RXC.3 (req) - Component Amount (NM)

    rxc_4 : CWE
        RXC.4 (req) - Component Units (CWE)

    rxc_5 : str | None
        RXC.5 (opt) - Component Strength (NM)

    rxc_6 : CWE | None
        RXC.6 (opt) - Component Strength Units (CWE)

    rxc_7 : list[CWE] | None
        RXC.7 (opt, rep) - Supplementary Code (CWE)

    rxc_8 : str | None
        RXC.8 (opt) - Component Drug Strength Volume (NM)

    rxc_9 : CWE | None
        RXC.9 (opt) - Component Drug Strength Volume Units (CWE)

    rxc_10 : str | None
        RXC.10 (opt) - Dispense Amount (NM)

    rxc_11 : CWE | None
        RXC.11 (opt) - Dispense Units (CWE)
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

    rxc_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxc_2",
            "component_code",
            "RXC.2",
        ),
        serialization_alias="RXC.2",
        title="Component Code",
        description="Item #314 | Table HL79999",
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

    rxc_4: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxc_4",
            "component_units",
            "RXC.4",
        ),
        serialization_alias="RXC.4",
        title="Component Units",
        description="Item #316 | Table HL79999",
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

    rxc_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_6",
            "component_strength_units",
            "RXC.6",
        ),
        serialization_alias="RXC.6",
        title="Component Strength Units",
        description="Item #1125 | Table HL79999",
    )

    rxc_7: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_7",
            "supplementary_code",
            "RXC.7",
        ),
        serialization_alias="RXC.7",
        title="Supplementary Code",
        description="Item #1476 | Table HL79999",
    )

    rxc_8: Optional[str] = Field(
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

    rxc_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_9",
            "component_drug_strength_volume_units",
            "RXC.9",
        ),
        serialization_alias="RXC.9",
        title="Component Drug Strength Volume Units",
        description="Item #1672 | Table HL79999",
    )

    rxc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_10",
            "dispense_amount",
            "RXC.10",
        ),
        serialization_alias="RXC.10",
        title="Dispense Amount",
        description="Item #3314",
    )

    rxc_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxc_11",
            "dispense_units",
            "RXC.11",
        ),
        serialization_alias="RXC.11",
        title="Dispense Units",
        description="Item #3315 | Table HL79999",
    )

    @field_validator("rxc_3", "rxc_5", "rxc_8", "rxc_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
