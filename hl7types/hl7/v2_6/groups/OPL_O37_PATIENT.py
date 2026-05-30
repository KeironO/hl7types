"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .OPL_O37_INSURANCE import OPL_O37_INSURANCE

_AL1 = AL1
_OBX = OBX
_OPL_O37_INSURANCE = OPL_O37_INSURANCE
_PD1 = PD1
_PID = PID


class OPL_O37_PATIENT(HL7Model):
    """HL7 v2 OPL_O37.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        OBX (Optional[List[OBX]]): optional
        INSURANCE (Optional[List[OPL_O37_INSURANCE]]): optional
        AL1 (Optional[List[AL1]]): optional
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

    INSURANCE: Optional[List[_OPL_O37_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
