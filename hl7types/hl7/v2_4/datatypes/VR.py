"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VR
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class VR(BaseModel):
    """HL7 v2 VR data type."""

    vr_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_1",
            "first_data_code_value",
            "VR.1",
        ),
        serialization_alias="VR.1",
        title="first data code value",
    )

    vr_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_2",
            "last_data_code_calue",
            "VR.2",
        ),
        serialization_alias="VR.2",
        title="Last data code calue",
    )

    model_config = {"populate_by_name": True}
