"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O44.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID
from ..segments.PRT import PRT

_PID = PID
_PRT = PRT


class ORL_O44_PATIENT(HL7Model):
    """HL7 v2 ORL_O44.PATIENT group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
