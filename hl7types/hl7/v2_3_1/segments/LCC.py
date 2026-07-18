"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: LCC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL


class LCC(HL7Model):
    """LCC - location charge code segment (S8.8.6).

    Attributes
    ----------
    lcc_1 : PL
        LCC.1 - Primary Key Value - LCC (PL) R S8.8.6.1

    lcc_2 : str
        LCC.2 - Location Department (IS) R S8.8.6.2 | 0264 - Location Department

    lcc_3 : list[CE] | None
        LCC.3 - Accommodation Type (CE) O rep S8.8.6.3 | 0129 - Accommodation Code

    lcc_4 : list[CE]
        LCC.4 - Charge Code (CE) R rep S8.8.6.4 | 0132 - Transaction Code
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

    lcc_2: str = Field(
        validation_alias=AliasChoices(
            "lcc_2",
            "location_department",
            "LCC.2",
        ),
        serialization_alias="LCC.2",
        title="Location Department",
        description=(
            "R | Item #00964 | Table 0264 - Location Department | LEN:10"
        ),
    )

    lcc_3: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lcc_3",
            "accommodation_type",
            "LCC.3",
        ),
        serialization_alias="LCC.3",
        title="Accommodation Type",
        description="O | Item #00980 | Table 0129 - Accommodation Code",
    )

    lcc_4: List[CE] = Field(
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

    model_config = ConfigDict(populate_by_name=True)
