"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: VID
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class VID(BaseModel):
    """HL7 v2 VID data type."""

    vid_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "vid_1",
            "version_id",
            "VID.1",
        ),
        serialization_alias="VID.1",
        title="Version ID",
    )

    vid_2: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_2",
            "internationalization_code",
            "VID.2",
        ),
        serialization_alias="VID.2",
        title="Internationalization Code",
    )

    vid_3: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_3",
            "international_version_id",
            "VID.3",
        ),
        serialization_alias="VID.3",
        title="International Version ID",
    )

    model_config = {"populate_by_name": True}
