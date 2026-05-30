"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BRP_O30.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .BRP_O30_ORDER import BRP_O30_ORDER

_BRP_O30_ORDER = BRP_O30_ORDER
_PID = PID


class BRP_O30_PATIENT(HL7Model):
    """HL7 v2 BRP_O30.PATIENT group.

    Attributes:
        PID (PID): required
        ORDER (Optional[List[BRP_O30_ORDER]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    ORDER: Optional[List[_BRP_O30_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
