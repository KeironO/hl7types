"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: BRP_O30.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.PID import PID
from ..segments.PRT import PRT

from .BRP_O30_ORDER import BRP_O30_ORDER

_ARV = ARV
_BRP_O30_ORDER = BRP_O30_ORDER
_PID = PID
_PRT = PRT


class BRP_O30_PATIENT(BaseModel):
    """HL7 v2 BRP_O30.PATIENT group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        ORDER (Optional[List[BRP_O30_ORDER]]): optional
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

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_BRP_O30_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
