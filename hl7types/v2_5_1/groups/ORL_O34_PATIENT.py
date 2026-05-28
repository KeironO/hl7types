"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORL_O34.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PID import PID

from .ORL_O34_SPECIMEN import ORL_O34_SPECIMEN

_ORL_O34_SPECIMEN = ORL_O34_SPECIMEN
_PID = PID


class ORL_O34_PATIENT(BaseModel):
    """HL7 v2 ORL_O34.PATIENT group.

    Attributes:
        PID (PID): required
        SPECIMEN (List[ORL_O34_SPECIMEN]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    SPECIMEN: List[_ORL_O34_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
