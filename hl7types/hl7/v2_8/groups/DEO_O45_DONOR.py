"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DEO_O45.DONOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class DEO_O45_DONOR(HL7Model):
    """HL7 v2 DEO_O45.DONOR group.

    Attributes:
        PID (PID): Patient Identification, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        DONOR_REGISTRATION (Optional[DEO_O45_DONOR_REGISTRATION]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    DONOR_REGISTRATION: Optional[_DEO_O45_DONOR_REGISTRATION] = Field(
        default=None,
        title="DONOR_REGISTRATION",
    )

    model_config = ConfigDict(populate_by_name=True)
