"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: UVC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class UVC(BaseModel):
    """HL7 v2 UVC data type."""

    uvc_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_1",
            "value_code",
            "UVC.1",
        ),
        serialization_alias="UVC.1",
        title="value code",
    )

    uvc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_2",
            "value_amount",
            "UVC.2",
        ),
        serialization_alias="UVC.2",
        title="value amount",
    )

    model_config = {"populate_by_name": True}
