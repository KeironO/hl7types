"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: LOC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class LOC(HL7Model):
    """Location Identification (S8.9.2).

    Attributes
    ----------
    loc_1 : PL
        LOC.1 - Primary Key Value - LOC (PL) R S8.9.2.1

    loc_2 : str | None
        LOC.2 - Location Description (ST) O S8.9.2.2

    loc_3 : list[str]
        LOC.3 - Location Type - LOC (IS) R rep S8.9.2.3 | 0260 - Patient location type

    loc_4 : list[XON] | None
        LOC.4 - Organization Name - LOC (XON) O rep S8.9.2.4

    loc_5 : list[XAD] | None
        LOC.5 - Location Address (XAD) O rep S8.9.2.5

    loc_6 : list[XTN] | None
        LOC.6 - Location Phone (XTN) O rep S8.9.2.6

    loc_7 : list[CE] | None
        LOC.7 - License Number (CE) O rep S8.9.2.7 | 0461 - License number

    loc_8 : list[str] | None
        LOC.8 - Location Equipment (IS) O rep S8.9.2.8 | 0261 - Location equipment

    loc_9 : str | None
        LOC.9 - Location Service Code (IS) O S8.9.2.9 | 0442 - Location service code
    """

    loc_1: PL = Field(
        validation_alias=AliasChoices(
            "loc_1",
            "primary_key_value_loc",
            "LOC.1",
        ),
        serialization_alias="LOC.1",
        title="Primary Key Value - LOC",
        description="R | Item #01307",
    )

    loc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_2",
            "location_description",
            "LOC.2",
        ),
        serialization_alias="LOC.2",
        title="Location Description",
        description="O | Item #00944 | LEN:48",
    )

    loc_3: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "loc_3",
            "location_type_loc",
            "LOC.3",
        ),
        serialization_alias="LOC.3",
        title="Location Type - LOC",
        description=(
            "R | Item #00945 | Table 0260 - Patient location type | LEN:2"
        ),
    )

    loc_4: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_4",
            "organization_name_loc",
            "LOC.4",
        ),
        serialization_alias="LOC.4",
        title="Organization Name - LOC",
        description="O | Item #00947",
    )

    loc_5: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_5",
            "location_address",
            "LOC.5",
        ),
        serialization_alias="LOC.5",
        title="Location Address",
        description="O | Item #00948",
    )

    loc_6: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_6",
            "location_phone",
            "LOC.6",
        ),
        serialization_alias="LOC.6",
        title="Location Phone",
        description="O | Item #00949",
    )

    loc_7: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_7",
            "license_number",
            "LOC.7",
        ),
        serialization_alias="LOC.7",
        title="License Number",
        description="O | Item #00951 | Table 0461 - License number",
    )

    loc_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_8",
            "location_equipment",
            "LOC.8",
        ),
        serialization_alias="LOC.8",
        title="Location Equipment",
        description="O | Item #00953 | Table 0261 - Location equipment | LEN:3",
    )

    loc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_9",
            "location_service_code",
            "LOC.9",
        ),
        serialization_alias="LOC.9",
        title="Location Service Code",
        description=(
            "O | Item #01583 | Table 0442 - Location service code | LEN:1"
        ),
    )

    model_config = {"populate_by_name": True}
