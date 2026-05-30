"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DEL_O46.DONOR
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

from .DEL_O46_DONOR_REGISTRATION import DEL_O46_DONOR_REGISTRATION

_AL1 = AL1
_ARV = ARV
_DEL_O46_DONOR_REGISTRATION = DEL_O46_DONOR_REGISTRATION
_NTE = NTE
_OBX = OBX
_PD1 = PD1
_PID = PID


class DEL_O46_DONOR(HL7Model):
    """HL7 v2 DEL_O46.DONOR group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
        AL1 (Optional[List[AL1]]): optional
        ARV (Optional[List[ARV]]): optional
        DONOR_REGISTRATION (Optional[DEL_O46_DONOR_REGISTRATION]): optional
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

    DONOR_REGISTRATION: Optional[_DEL_O46_DONOR_REGISTRATION] = Field(
        default=None,
        title="DONOR_REGISTRATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
