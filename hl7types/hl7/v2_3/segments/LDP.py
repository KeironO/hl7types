"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: LDP
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
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
        LDP.1 - LDP Primary Key Value (PL) R S8.8.5.1

    ldp_2 : str
        LDP.2 - Location Department (IS) R S8.8.5 | 0264 - Location Department

    ldp_3 : list[str] | None
        LDP.3 - Location Service (IS) O rep S8.8.5.3 | 0069 - Hospital Service

    ldp_4 : list[CE] | None
        LDP.4 - Speciality Type (CE) O rep S8.8.5.4 | 0265 - Specialty Type

    ldp_5 : list[str] | None
        LDP.5 - Valid Patient Classes (ID) O rep S8.8.5.5 | 0004 - Patient Class

    ldp_6 : str | None
        LDP.6 - Active/Inactive Flag (ID) O S8.6.2 | 0183 - Active/Inactive

    ldp_7 : TS | None
        LDP.7 - Activation Date (TS) O S8.8.5.7

    ldp_8 : TS | None
        LDP.8 - Inactivation Date - LDP (TS) O S8.8.5.8

    ldp_9 : str | None
        LDP.9 - Inactivated Reason (ST) O S8.8.5.9

    ldp_10 : list[VH] | None
        LDP.10 - Visiting Hours (VH) O rep S8.8.5.10 | 0267 - Days of the Week

    ldp_11 : XTN | None
        LDP.11 - Contact Phone (XTN) O S8.8.5.11
    """

    ldp_1: PL = Field(
        validation_alias=AliasChoices(
            "ldp_1",
            "ldp_primary_key_value",
            "LDP.1",
        ),
        serialization_alias="LDP.1",
        title="LDP Primary Key Value",
        description="R | Item #00963",
    )

    ldp_2: str = Field(
        validation_alias=AliasChoices(
            "ldp_2",
            "location_department",
            "LDP.2",
        ),
        serialization_alias="LDP.2",
        title="Location Department",
        description=(
            "R | Item #00964 | Table 0264 - Location Department | LEN:10"
        ),
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
        description="O | Item #00965 | Table 0069 - Hospital Service | LEN:3",
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
        description="O | Item #00966 | Table 0265 - Specialty Type",
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
        description="O | Item #00967 | Table 0004 - Patient Class | LEN:1",
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
        description="O | Item #00675 | Table 0183 - Active/Inactive | LEN:1",
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
        description="O | Item #00969",
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
        description="O | Item #00970",
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
        description="O | Item #00971 | LEN:80",
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
        description="O | Item #00976 | Table 0267 - Days of the Week",
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
        description="O | Item #00978",
    )

    model_config = ConfigDict(populate_by_name=True)
