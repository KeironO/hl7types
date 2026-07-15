"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: LCC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL


class LCC(HL7Model):
    """Location Charge Code (S8.9.6).

    Attributes
    ----------
    lcc_1 : PL
        LCC.1 - Primary Key Value - LCC (PL) R S8.9.6.1

    lcc_2 : CE
        LCC.2 - Location Department (CE) R S8.9.6.2 | 0264 - Location department

    lcc_3 : list[CE] | None
        LCC.3 - Accommodation Type (CE) O rep S8.9.6.3 | 0129 - Accommodation code

    lcc_4 : list[CE]
        LCC.4 - Charge Code (CE) R rep S8.9.6.4 | 0132 - Transaction code
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

    lcc_2: CE = Field(
        validation_alias=AliasChoices(
            "lcc_2",
            "location_department",
            "LCC.2",
        ),
        serialization_alias="LCC.2",
        title="Location Department",
        description="R | Item #00964 | Table 0264 - Location department",
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
        description="O | Item #00980 | Table 0129 - Accommodation code",
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
        description="R | Item #00981 | Table 0132 - Transaction code",
    )

    model_config = {"populate_by_name": True}
