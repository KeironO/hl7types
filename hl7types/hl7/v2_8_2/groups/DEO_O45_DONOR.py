"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DEO_O45.DONOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PID import PID
from .DEO_O45_DONOR_REGISTRATION import DEO_O45_DONOR_REGISTRATION

_ARV = ARV
_DEO_O45_DONOR_REGISTRATION = DEO_O45_DONOR_REGISTRATION
_NTE = NTE
_OBX = OBX
_PID = PID


class DEO_O45_DONOR(BaseModel):
    """HL7 v2 DEO_O45.DONOR group.

    Attributes:
        PID (PID): required
        OBX (Optional[List[OBX]]): optional
        ARV (Optional[List[ARV]]): optional
        NTE (Optional[List[NTE]]): optional
        DONOR_REGISTRATION (Optional[DEO_O45_DONOR_REGISTRATION]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    DONOR_REGISTRATION: _DEO_O45_DONOR_REGISTRATION | None = Field(
        default=None,
        title="DONOR_REGISTRATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
