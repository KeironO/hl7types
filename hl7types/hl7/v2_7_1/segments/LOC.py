"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: LOC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class LOC(HL7Model):
    """HL7 v2 LOC segment.

    Attributes
    ----------
    loc_1 : PL
        LOC.1 (req) - Primary Key Value - LOC (PL)

    loc_2 : str | None
        LOC.2 (opt) - Location Description (ST)

    loc_3 : list[CWE]
        LOC.3 (req, rep) - Location Type - LOC (CWE)

    loc_4 : list[XON] | None
        LOC.4 (opt, rep) - Organization Name - LOC (XON)

    loc_5 : list[XAD] | None
        LOC.5 (opt, rep) - Location Address (XAD)

    loc_6 : list[XTN] | None
        LOC.6 (opt, rep) - Location Phone (XTN)

    loc_7 : list[CWE] | None
        LOC.7 (opt, rep) - License Number (CWE)

    loc_8 : list[CWE] | None
        LOC.8 (opt, rep) - Location Equipment (CWE)

    loc_9 : CWE | None
        LOC.9 (opt) - Location Service Code (CWE)
    """

    loc_1: PL = Field(
        validation_alias=AliasChoices(
            "loc_1",
            "primary_key_value_loc",
            "LOC.1",
        ),
        serialization_alias="LOC.1",
        title="Primary Key Value - LOC",
        description="Item #1307",
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
        description="Item #944",
    )

    loc_3: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "loc_3",
            "location_type_loc",
            "LOC.3",
        ),
        serialization_alias="LOC.3",
        title="Location Type - LOC",
        description="Item #945 | Table HL70260",
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
        description="Item #947",
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
        description="Item #948",
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
        description="Item #949",
    )

    loc_7: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_7",
            "license_number",
            "LOC.7",
        ),
        serialization_alias="LOC.7",
        title="License Number",
        description="Item #951 | Table HL70461",
    )

    loc_8: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_8",
            "location_equipment",
            "LOC.8",
        ),
        serialization_alias="LOC.8",
        title="Location Equipment",
        description="Item #953 | Table HL70261",
    )

    loc_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "loc_9",
            "location_service_code",
            "LOC.9",
        ),
        serialization_alias="LOC.9",
        title="Location Service Code",
        description="Item #1583 | Table HL70442",
    )

    model_config = {"populate_by_name": True}
