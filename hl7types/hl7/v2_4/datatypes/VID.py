"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VID
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE


class VID(HL7Model):
    """HL7 v2 VID data type.

    Attributes
    ----------
    vid_1 : str | None
        VID.1 (opt) - version ID (ID)

    vid_2 : CE | None
        VID.2 (opt) - internationalization code (CE)

    vid_3 : CE | None
        VID.3 (opt) - international version ID (CE)
    """

    vid_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_1",
            "version_id",
            "VID.1",
        ),
        serialization_alias="VID.1",
        title="version ID",
    )

    vid_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_2",
            "internationalization_code",
            "VID.2",
        ),
        serialization_alias="VID.2",
        title="internationalization code",
    )

    vid_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_3",
            "international_version_id",
            "VID.3",
        ),
        serialization_alias="VID.3",
        title="international version ID",
    )

    model_config = {"populate_by_name": True}
