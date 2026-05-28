"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OSM_R26.PATIENT_INFORMATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from ..segments.PRT import PRT

_PID = PID
_PRT = PRT


class OSM_R26_PATIENT_INFORMATION(BaseModel):
    """HL7 v2 OSM_R26.PATIENT_INFORMATION group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
