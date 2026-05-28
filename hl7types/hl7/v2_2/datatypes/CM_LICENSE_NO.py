"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_LICENSE_NO
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_LICENSE_NO(BaseModel):
    """HL7 v2 CM_LICENSE_NO data type."""

    cm_license_no_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_license_no_1",
            "license_number",
            "CM_LICENSE_NO.1",
        ),
        serialization_alias="CM_LICENSE_NO.1",
        title="License Number",
    )

    cm_license_no_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_license_no_2",
            "issuing_state_province_country",
            "CM_LICENSE_NO.2",
        ),
        serialization_alias="CM_LICENSE_NO.2",
        title="issuing state,province,country",
    )

    model_config = {"populate_by_name": True}
