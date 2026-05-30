"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
        VID.1 (opt) - Version ID (ID)

    vid_2 : CE | None
        VID.2 (opt) - Internationalization Code (CE)

    vid_3 : CE | None
        VID.3 (opt) - International Version ID (CE)
    """

    vid_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_1",
            "version_id",
            "VID.1",
        ),
        serialization_alias="VID.1",
        title="Version ID",
    )

    vid_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_2",
            "internationalization_code",
            "VID.2",
        ),
        serialization_alias="VID.2",
        title="Internationalization Code",
    )

    vid_3: Optional[CE] = Field(
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
