"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O21.PATIENT_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

_PD1 = PD1
_PID = PID
_PRT = PRT


class OML_O21_PATIENT_PRIOR(HL7Model):
    """HL7 v2 OML_O21.PATIENT_PRIOR group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    model_config = ConfigDict(populate_by_name=True)
