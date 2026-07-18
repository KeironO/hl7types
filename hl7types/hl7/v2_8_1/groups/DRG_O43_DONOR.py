"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DRG_O43.DONOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .DRG_O43_DONOR_REGISTRATION import DRG_O43_DONOR_REGISTRATION

_AL1 = AL1
_ARV = ARV
_DRG_O43_DONOR_REGISTRATION = DRG_O43_DONOR_REGISTRATION
_NTE = NTE
_OBX = OBX
_PD1 = PD1
_PID = PID


class DRG_O43_DONOR(HL7Model):
    """HL7 v2 DRG_O43.DONOR group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        DONOR_REGISTRATION (Optional[DRG_O43_DONOR_REGISTRATION]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    DONOR_REGISTRATION: Optional[_DRG_O43_DONOR_REGISTRATION] = Field(
        default=None,
        title="DONOR_REGISTRATION",
    )

    model_config = ConfigDict(populate_by_name=True)
