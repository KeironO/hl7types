"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: LCC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL


class LCC(BaseModel):
    """HL7 v2 LCC segment."""

    lcc_1: PL = Field(
        default=...,
        validation_alias=AliasChoices(
            "lcc_1",
            "primary_key_value_lcc",
            "LCC.1",
        ),
        serialization_alias="LCC.1",
        title="Primary Key Value - LCC",
        description="Item #979",
    )

    lcc_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "lcc_2",
            "location_department",
            "LCC.2",
        ),
        serialization_alias="LCC.2",
        title="Location Department",
        description="Item #964 | Table HL70264",
    )

    lcc_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lcc_3",
            "accommodation_type",
            "LCC.3",
        ),
        serialization_alias="LCC.3",
        title="Accommodation Type",
        description="Item #980 | Table HL70129",
    )

    lcc_4: List[CWE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "lcc_4",
            "charge_code",
            "LCC.4",
        ),
        serialization_alias="LCC.4",
        title="Charge Code",
        description="Item #981 | Table HL70132",
    )

    model_config = {"populate_by_name": True}
