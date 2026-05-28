"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_VR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_VR(BaseModel):
    """HL7 v2 CM_VR data type."""

    cm_vr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_vr_1",
            "first_data_code_value",
            "CM_VR.1",
        ),
        serialization_alias="CM_VR.1",
        title="first data code value",
    )

    cm_vr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_vr_2",
            "last_data_code_calue",
            "CM_VR.2",
        ),
        serialization_alias="CM_VR.2",
        title="Last data code calue",
    )

    model_config = {"populate_by_name": True}
