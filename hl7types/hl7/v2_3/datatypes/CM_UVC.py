"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_UVC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_UVC(BaseModel):
    """HL7 v2 CM_UVC data type."""

    cm_uvc_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_uvc_1",
            "value_code",
            "CM_UVC.1",
        ),
        serialization_alias="CM_UVC.1",
        title="value code",
    )

    cm_uvc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_uvc_2",
            "value_amount",
            "CM_UVC.2",
        ),
        serialization_alias="CM_UVC.2",
        title="value amount",
    )

    model_config = {"populate_by_name": True}
