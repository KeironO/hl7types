"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: VID
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CWE import CWE


class VID(HL7Model):
    """HL7 v2 VID data type.

    Attributes
    ----------
    vid_1 : str
        VID.1 (req) - Version ID (ID)

    vid_2 : CWE | None
        VID.2 (opt) - Internationalization Code (CWE)

    vid_3 : CWE | None
        VID.3 (opt) - International Version ID (CWE)
    """

    vid_1: str = Field(
        max_length=5,
        validation_alias=AliasChoices(
            "vid_1",
            "version_id",
            "VID.1",
        ),
        serialization_alias="VID.1",
        title="Version ID",
    )

    vid_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vid_2",
            "internationalization_code",
            "VID.2",
        ),
        serialization_alias="VID.2",
        title="Internationalization Code",
    )

    vid_3: Optional[CWE] = Field(
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
