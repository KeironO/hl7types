"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: VR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class VR(BaseModel):
    """HL7 v2 VR data type."""

    vr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_1",
            "first_data_code_value",
            "VR.1",
        ),
        serialization_alias="VR.1",
        title="First Data Code Value",
    )

    vr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_2",
            "last_data_code_value",
            "VR.2",
        ),
        serialization_alias="VR.2",
        title="Last Data Code Value",
    )

    model_config = {"populate_by_name": True}
