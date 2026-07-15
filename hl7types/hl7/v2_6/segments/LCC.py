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
    """Location Charge Code (S8.9.6).

    Attributes
    ----------
    lcc_1 : PL
        LCC.1 - Primary Key Value - LCC (PL) R S8.9.6.1

    lcc_2 : CWE
        LCC.2 - Location Department (CWE) R S8.9.5.2 | 0264 - Location Department

    lcc_3 : list[CWE] | None
        LCC.3 - Accommodation Type (CWE) O rep S8.9.6.3 | 0129 - Accommodation code

    lcc_4 : list[CWE]
        LCC.4 - Charge Code (CWE) R rep S8.9.6.4 | 0132 - Transaction Code
    """

    lcc_1: PL = Field(
        validation_alias=AliasChoices(
            "lcc_1",
            "primary_key_value_lcc",
            "LCC.1",
        ),
        serialization_alias="LCC.1",
        title="Primary Key Value - LCC",
        description="R | Item #00979",
    )

    lcc_2: CWE = Field(
        validation_alias=AliasChoices(
            "lcc_2",
            "location_department",
            "LCC.2",
        ),
        serialization_alias="LCC.2",
        title="Location Department",
        description="R | Item #00964 | Table 0264 - Location Department",
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
        description="O | Item #00980 | Table 0129 - Accommodation code",
    )

    lcc_4: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "lcc_4",
            "charge_code",
            "LCC.4",
        ),
        serialization_alias="LCC.4",
        title="Charge Code",
        description="R | Item #00981 | Table 0132 - Transaction Code",
    )

    model_config = {"populate_by_name": True}
