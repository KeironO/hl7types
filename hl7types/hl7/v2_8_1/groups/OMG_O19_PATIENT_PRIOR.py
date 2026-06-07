"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMG_O19.PATIENT_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

_ARV = ARV
_PD1 = PD1
_PID = PID
_PRT = PRT


class OMG_O19_PATIENT_PRIOR(HL7Model):
    """HL7 v2 OMG_O19.PATIENT_PRIOR group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        ARV (Optional[List[ARV]]): optional
        PRT (Optional[List[PRT]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
