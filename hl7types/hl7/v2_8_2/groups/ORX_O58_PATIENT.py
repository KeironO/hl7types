"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORX_O58.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.PRT import PRT

_ARV = ARV
_NTE = NTE
_PID = PID
_PRT = PRT


class ORX_O58_PATIENT(HL7Model):
    """HL7 v2 ORX_O58.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
