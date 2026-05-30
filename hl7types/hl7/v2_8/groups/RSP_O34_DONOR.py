"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_O34.DONOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RSP_O34_DONOR_REGISTRATION import RSP_O34_DONOR_REGISTRATION

_AL1 = AL1
_ARV = ARV
_NTE = NTE
_OBX = OBX
_PD1 = PD1
_PID = PID
_RSP_O34_DONOR_REGISTRATION = RSP_O34_DONOR_REGISTRATION


class RSP_O34_DONOR(HL7Model):
    """HL7 v2 RSP_O34.DONOR group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
        AL1 (Optional[List[AL1]]): optional
        ARV (Optional[List[ARV]]): optional
        DONOR_REGISTRATION (Optional[RSP_O34_DONOR_REGISTRATION]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    DONOR_REGISTRATION: Optional[_RSP_O34_DONOR_REGISTRATION] = Field(
        default=None,
        title="DONOR_REGISTRATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
