"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DER_O44.DONOR
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .DER_O44_DONOR_REGISTRATION import DER_O44_DONOR_REGISTRATION

_AL1 = AL1
_ARV = ARV
_DER_O44_DONOR_REGISTRATION = DER_O44_DONOR_REGISTRATION
_NTE = NTE
_OBX = OBX
_PD1 = PD1
_PID = PID


class DER_O44_DONOR(BaseModel):
    """HL7 v2 DER_O44.DONOR group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
        AL1 (Optional[List[AL1]]): optional
        ARV (Optional[List[ARV]]): optional
        DONOR_REGISTRATION (Optional[DER_O44_DONOR_REGISTRATION]): optional
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

    DONOR_REGISTRATION: Optional[_DER_O44_DONOR_REGISTRATION] = Field(
        default=None,
        title="DONOR_REGISTRATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
