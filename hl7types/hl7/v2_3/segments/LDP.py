"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: LDP
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.VH import VH
from ..datatypes.XTN import XTN


class LDP(HL7Model):
    """Location Department (S8.8.5).

    Attributes
    ----------
    ldp_1 : PL
        LDP.1 (req) - LDP Primary Key Value (PL) S8.8.5.1

    ldp_2 : str
        LDP.2 (req) - Location Department (IS) S8.8.5 | 0264 - Location Department

    ldp_3 : list[str] | None
        LDP.3 (opt, rep) - Location Service (IS) S8.8.5.3 | 0069 - Hospital Service

    ldp_4 : list[CE] | None
        LDP.4 (opt, rep) - Speciality Type (CE) S8.8.5.4 | 0265 - Specialty Type

    ldp_5 : list[str] | None
        LDP.5 (opt, rep) - Valid Patient Classes (ID) S8.8.5.5 | 0004 - Patient Class

    ldp_6 : str | None
        LDP.6 (opt) - Active/Inactive Flag (ID) S8.6.2 | 0183 - Active/Inactive

    ldp_7 : TS | None
        LDP.7 (opt) - Activation Date (TS) S8.8.5.7

    ldp_8 : TS | None
        LDP.8 (opt) - Inactivation Date - LDP (TS) S8.8.5.8

    ldp_9 : str | None
        LDP.9 (opt) - Inactivated Reason (ST) S8.8.5.9

    ldp_10 : list[VH] | None
        LDP.10 (opt, rep) - Visiting Hours (VH) S8.8.5.10 | 0267 - Days of the Week

    ldp_11 : XTN | None
        LDP.11 (opt) - Contact Phone (XTN) S8.8.5.11
    """

    ldp_1: PL = Field(
        validation_alias=AliasChoices(
            "ldp_1",
            "ldp_primary_key_value",
            "LDP.1",
        ),
        serialization_alias="LDP.1",
        title="LDP Primary Key Value",
        description="Item #963",
    )

    ldp_2: str = Field(
        validation_alias=AliasChoices(
            "ldp_2",
            "location_department",
            "LDP.2",
        ),
        serialization_alias="LDP.2",
        title="Location Department",
        description="Item #964 | Table HL70264",
    )

    ldp_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_3",
            "location_service",
            "LDP.3",
        ),
        serialization_alias="LDP.3",
        title="Location Service",
        description="Item #965 | Table HL70069",
    )

    ldp_4: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_4",
            "speciality_type",
            "LDP.4",
        ),
        serialization_alias="LDP.4",
        title="Speciality Type",
        description="Item #966 | Table HL70265",
    )

    ldp_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_5",
            "valid_patient_classes",
            "LDP.5",
        ),
        serialization_alias="LDP.5",
        title="Valid Patient Classes",
        description="Item #967 | Table HL70004",
    )

    ldp_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_6",
            "active_inactive_flag",
            "LDP.6",
        ),
        serialization_alias="LDP.6",
        title="Active/Inactive Flag",
        description="Item #675 | Table HL70183",
    )

    ldp_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_7",
            "activation_date",
            "LDP.7",
        ),
        serialization_alias="LDP.7",
        title="Activation Date",
        description="Item #969",
    )

    ldp_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_8",
            "inactivation_date_ldp",
            "LDP.8",
        ),
        serialization_alias="LDP.8",
        title="Inactivation Date - LDP",
        description="Item #970",
    )

    ldp_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_9",
            "inactivated_reason",
            "LDP.9",
        ),
        serialization_alias="LDP.9",
        title="Inactivated Reason",
        description="Item #971",
    )

    ldp_10: Optional[List[VH]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_10",
            "visiting_hours",
            "LDP.10",
        ),
        serialization_alias="LDP.10",
        title="Visiting Hours",
        description="Item #976 | Table HL70267",
    )

    ldp_11: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_11",
            "contact_phone",
            "LDP.11",
        ),
        serialization_alias="LDP.11",
        title="Contact Phone",
        description="Item #978",
    )

    model_config = {"populate_by_name": True}
