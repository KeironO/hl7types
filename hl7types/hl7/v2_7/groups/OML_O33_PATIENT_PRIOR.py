"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OML_O33.PATIENT_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

_PD1 = PD1
_PID = PID
_PRT = PRT


class OML_O33_PATIENT_PRIOR(HL7Model):
    """HL7 v2 OML_O33.PATIENT_PRIOR group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
