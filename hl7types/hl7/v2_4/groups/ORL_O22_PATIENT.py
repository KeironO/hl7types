"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORL_O22.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PID import PID

from .ORL_O22_GENERAL_ORDER import ORL_O22_GENERAL_ORDER

_ORL_O22_GENERAL_ORDER = ORL_O22_GENERAL_ORDER
_PID = PID


class ORL_O22_PATIENT(BaseModel):
    """HL7 v2 ORL_O22.PATIENT group.

    Attributes:
        PID (PID): required
        GENERAL_ORDER (List[ORL_O22_GENERAL_ORDER]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    GENERAL_ORDER: List[_ORL_O22_GENERAL_ORDER] = Field(
        default=...,
        title="GENERAL_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
