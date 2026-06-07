"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: LDP
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.VH import VH
from ..datatypes.XTN import XTN


class LDP(HL7Model):
    """HL7 v2 LDP segment.

    Attributes
    ----------
    ldp_1 : PL
        LDP.1 (req) - Primary Key Value - LDP (PL)

    ldp_2 : CWE
        LDP.2 (req) - Location Department (CWE)

    ldp_3 : list[CWE] | None
        LDP.3 (opt, rep) - Location Service (CWE)

    ldp_4 : list[CWE] | None
        LDP.4 (opt, rep) - Specialty Type (CWE)

    ldp_5 : list[CWE] | None
        LDP.5 (opt, rep) - Valid Patient Classes (CWE)

    ldp_6 : str | None
        LDP.6 (opt) - Active/Inactive Flag (ID)

    ldp_7 : str | None
        LDP.7 (opt) - Activation Date - LDP (DTM)

    ldp_8 : str | None
        LDP.8 (opt) - Inactivation Date - LDP (DTM)

    ldp_9 : str | None
        LDP.9 (opt) - Inactivated Reason (ST)

    ldp_10 : list[VH] | None
        LDP.10 (opt, rep) - Visiting Hours (VH)

    ldp_11 : XTN | None
        LDP.11 (opt) - Contact Phone (XTN)

    ldp_12 : CWE | None
        LDP.12 (opt) - Location Cost Center (CWE)
    """

    ldp_1: PL = Field(
        validation_alias=AliasChoices(
            "ldp_1",
            "primary_key_value_ldp",
            "LDP.1",
        ),
        serialization_alias="LDP.1",
        title="Primary Key Value - LDP",
        description="Item #963",
    )

    ldp_2: CWE = Field(
        validation_alias=AliasChoices(
            "ldp_2",
            "location_department",
            "LDP.2",
        ),
        serialization_alias="LDP.2",
        title="Location Department",
        description="Item #964 | Table HL70264",
    )

    ldp_3: Optional[List[CWE]] = Field(
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

    ldp_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_4",
            "specialty_type",
            "LDP.4",
        ),
        serialization_alias="LDP.4",
        title="Specialty Type",
        description="Item #966 | Table HL70265",
    )

    ldp_5: Optional[List[CWE]] = Field(
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

    ldp_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_7",
            "activation_date_ldp",
            "LDP.7",
        ),
        serialization_alias="LDP.7",
        title="Activation Date - LDP",
        description="Item #969",
    )

    ldp_8: Optional[str] = Field(
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

    ldp_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_12",
            "location_cost_center",
            "LDP.12",
        ),
        serialization_alias="LDP.12",
        title="Location Cost Center",
        description="Item #1584 | Table HL70462",
    )

    @field_validator("ldp_7", "ldp_8", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
