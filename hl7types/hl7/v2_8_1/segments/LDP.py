"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: LDP
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.VH import VH
from ..datatypes.XTN import XTN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class LDP(HL7Model):
    """Location Department (S8.9.5).

    Attributes
    ----------
    ldp_1 : PL
        LDP.1 - Primary Key Value - LDP (PL) R S8.9.5.1

    ldp_2 : CWE
        LDP.2 - Location Department (CWE) R S8.9.5.2 | 0264 - Location Department

    ldp_3 : list[CWE] | None
        LDP.3 - Location Service (CWE) O rep S8.9.5.3 | 0069 - Hospital Service

    ldp_4 : list[CWE] | None
        LDP.4 - Specialty Type (CWE) O rep S8.9.5.4 | 0265 - Specialty Type

    ldp_5 : list[CWE] | None
        LDP.5 - Valid Patient Classes (CWE) O rep S8.10.3.4 | 0004 - Patient Class

    ldp_6 : str | None
        LDP.6 - Active/Inactive Flag (ID) O S15.4.8.7 | 0183 - Active/Inactive

    ldp_7 : str | None
        LDP.7 - Activation Date - LDP (DTM) O S8.9.5.7

    ldp_8 : str | None
        LDP.8 - Inactivation Date - LDP (DTM) O S8.9.5.8

    ldp_9 : str | None
        LDP.9 - Inactivated Reason (ST) O S8.9.5.9

    ldp_10 : list[VH] | None
        LDP.10 - Visiting Hours (VH) O rep S8.9.5.10 | 0267 - Days of the Week

    ldp_11 : XTN | None
        LDP.11 - Contact Phone (XTN) O S8.9.5.11

    ldp_12 : CWE | None
        LDP.12 - Location Cost Center (CWE) O S8.9.5.12 | 0462 - Location Cost Center
    """

    ldp_1: PL = Field(
        validation_alias=AliasChoices(
            "ldp_1",
            "primary_key_value_ldp",
            "LDP.1",
        ),
        serialization_alias="LDP.1",
        title="Primary Key Value - LDP",
        description="R | Item #00963",
    )

    ldp_2: CWE = Field(
        validation_alias=AliasChoices(
            "ldp_2",
            "location_department",
            "LDP.2",
        ),
        serialization_alias="LDP.2",
        title="Location Department",
        description="R | Item #00964 | Table 0264 - Location Department",
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
        description="O | Item #00965 | Table 0069 - Hospital Service",
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
        description="O | Item #00966 | Table 0265 - Specialty Type",
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
        description="O | Item #00967 | Table 0004 - Patient Class",
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

    ldp_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_7",
            "activation_date_ldp",
            "LDP.7",
        ),
        serialization_alias="LDP.7",
        title="Activation Date - LDP",
        description="O | Item #00969",
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
        description="O | Item #00971",
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

    ldp_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ldp_12",
            "location_cost_center",
            "LDP.12",
        ),
        serialization_alias="LDP.12",
        title="Location Cost Center",
        description="O | Item #01584 | Table 0462 - Location Cost Center",
    )

    @field_validator("ldp_7", "ldp_8", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
