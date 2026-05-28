"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PAT_ID
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_PAT_ID(BaseModel):
    """HL7 v2 CM_PAT_ID data type."""

    cm_pat_id_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_1",
            "patient_id",
            "CM_PAT_ID.1",
        ),
        serialization_alias="CM_PAT_ID.1",
        title="Patient ID",
    )

    cm_pat_id_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_2",
            "check_digit",
            "CM_PAT_ID.2",
        ),
        serialization_alias="CM_PAT_ID.2",
        title="Check digit",
    )

    cm_pat_id_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_3",
            "check_digit_scheme",
            "CM_PAT_ID.3",
        ),
        serialization_alias="CM_PAT_ID.3",
        title="Check digit scheme",
    )

    cm_pat_id_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_4",
            "facility_id",
            "CM_PAT_ID.4",
        ),
        serialization_alias="CM_PAT_ID.4",
        title="Facility ID",
    )

    cm_pat_id_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_5",
            "type_",
            "CM_PAT_ID.5",
        ),
        serialization_alias="CM_PAT_ID.5",
        title="type",
    )

    model_config = {"populate_by_name": True}
