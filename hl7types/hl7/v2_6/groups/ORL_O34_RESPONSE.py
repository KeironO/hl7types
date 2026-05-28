"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O34.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from .ORL_O34_SPECIMEN import ORL_O34_SPECIMEN

_ORL_O34_SPECIMEN = ORL_O34_SPECIMEN
_PID = PID


class ORL_O34_RESPONSE(BaseModel):
    """HL7 v2 ORL_O34.RESPONSE group.

    Attributes:
        PID (PID): required
        SPECIMEN (List[ORL_O34_SPECIMEN]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    SPECIMEN: list[_ORL_O34_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
