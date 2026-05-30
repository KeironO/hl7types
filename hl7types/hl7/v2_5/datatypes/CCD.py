"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CCD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .TS import TS


class CCD(HL7Model):
    """HL7 v2 CCD data type.

    Attributes
    ----------
    ccd_1 : str | None
        CCD.1 (opt) - Invocation Event (ID)

    ccd_2 : TS | None
        CCD.2 (opt) - Date/time (TS)
    """

    ccd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccd_1",
            "invocation_event",
            "CCD.1",
        ),
        serialization_alias="CCD.1",
        title="Invocation Event",
    )

    ccd_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccd_2",
            "date_time",
            "CCD.2",
        ),
        serialization_alias="CCD.2",
        title="Date/time",
    )

    model_config = {"populate_by_name": True}
