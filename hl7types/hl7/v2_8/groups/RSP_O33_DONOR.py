"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_O33.DONOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.PID import PID

_ARV = ARV
_PID = PID


class RSP_O33_DONOR(HL7Model):
    """HL7 v2 RSP_O33.DONOR group.

    Attributes:
        PID (PID): Patient Identification, required
        ARV (Optional[List[ARV]]): Access Restriction, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    model_config = ConfigDict(populate_by_name=True)
