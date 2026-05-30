"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: STZ
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class STZ(HL7Model):
    """HL7 v2 STZ segment.

    Attributes
    ----------
    stz_1 : CWE | None
        STZ.1 (opt) - Sterilization Type (CWE)

    stz_2 : CWE | None
        STZ.2 (opt) - Sterilization Cycle (CWE)

    stz_3 : CWE | None
        STZ.3 (opt) - Maintenance Cycle (CWE)

    stz_4 : CWE | None
        STZ.4 (opt) - Maintenance Type (CWE)
    """

    stz_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stz_1",
            "sterilization_type",
            "STZ.1",
        ),
        serialization_alias="STZ.1",
        title="Sterilization Type",
        description="Item #2213 | Table HL70806",
    )

    stz_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stz_2",
            "sterilization_cycle",
            "STZ.2",
        ),
        serialization_alias="STZ.2",
        title="Sterilization Cycle",
        description="Item #2214 | Table HL70702",
    )

    stz_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stz_3",
            "maintenance_cycle",
            "STZ.3",
        ),
        serialization_alias="STZ.3",
        title="Maintenance Cycle",
        description="Item #2215 | Table HL70809",
    )

    stz_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stz_4",
            "maintenance_type",
            "STZ.4",
        ),
        serialization_alias="STZ.4",
        title="Maintenance Type",
        description="Item #2216 | Table HL70811",
    )

    model_config = {"populate_by_name": True}
