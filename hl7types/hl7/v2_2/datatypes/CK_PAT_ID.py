"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CK_PAT_ID
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CK_PAT_ID(BaseModel):
    """HL7 v2 CK_PAT_ID data type."""

    ck_pat_id_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_1",
            "patient_id",
            "CK_PAT_ID.1",
        ),
        serialization_alias="CK_PAT_ID.1",
        title="Patient ID",
    )

    ck_pat_id_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_2",
            "check_digit",
            "CK_PAT_ID.2",
        ),
        serialization_alias="CK_PAT_ID.2",
        title="Check digit",
    )

    ck_pat_id_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_3",
            "check_digit_scheme",
            "CK_PAT_ID.3",
        ),
        serialization_alias="CK_PAT_ID.3",
        title="Check digit scheme",
    )

    ck_pat_id_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_4",
            "facility_id",
            "CK_PAT_ID.4",
        ),
        serialization_alias="CK_PAT_ID.4",
        title="Facility ID",
    )

    model_config = {"populate_by_name": True}
