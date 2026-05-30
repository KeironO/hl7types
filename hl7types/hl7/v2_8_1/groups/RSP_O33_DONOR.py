"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_O33.DONOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.PID import PID

_ARV = ARV
_PID = PID


class RSP_O33_DONOR(HL7Model):
    """HL7 v2 RSP_O33.DONOR group.

    Attributes:
        PID (PID): required
        ARV (Optional[List[ARV]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
