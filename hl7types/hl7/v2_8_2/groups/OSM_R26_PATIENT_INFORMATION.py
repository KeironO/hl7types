"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OSM_R26.PATIENT_INFORMATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID
from ..segments.PRT import PRT

_PID = PID
_PRT = PRT


class OSM_R26_PATIENT_INFORMATION(HL7Model):
    """HL7 v2 OSM_R26.PATIENT_INFORMATION group.

    Attributes:
        PID (PID): Patient Identification, required
        PRT (Optional[List[PRT]]): Participation Information, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    model_config = ConfigDict(populate_by_name=True)
