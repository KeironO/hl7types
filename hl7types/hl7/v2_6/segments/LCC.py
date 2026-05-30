"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: LCC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL


class LCC(HL7Model):
    """HL7 v2 LCC segment.

    Attributes
    ----------
    lcc_1 : PL
        LCC.1 (req) - Primary Key Value - LCC (PL)

    lcc_2 : CWE
        LCC.2 (req) - Location Department (CWE)

    lcc_3 : list[CWE] | None
        LCC.3 (opt, rep) - Accommodation Type (CWE)

    lcc_4 : list[CWE]
        LCC.4 (req, rep) - Charge Code (CWE)
    """

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
