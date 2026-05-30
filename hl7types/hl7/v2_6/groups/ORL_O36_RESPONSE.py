"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O36.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .ORL_O36_SPECIMEN import ORL_O36_SPECIMEN

_ORL_O36_SPECIMEN = ORL_O36_SPECIMEN
_PID = PID


class ORL_O36_RESPONSE(HL7Model):
    """HL7 v2 ORL_O36.RESPONSE group.

    Attributes:
        PID (PID): required
        SPECIMEN (List[ORL_O36_SPECIMEN]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    SPECIMEN: List[_ORL_O36_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
