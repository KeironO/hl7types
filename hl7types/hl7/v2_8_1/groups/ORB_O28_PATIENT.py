"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORB_O28.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORB_O28_ORDER import ORB_O28_ORDER

_ARV = ARV
_ORB_O28_ORDER = ORB_O28_ORDER
_PID = PID
_PRT = PRT


class ORB_O28_PATIENT(BaseModel):
    """HL7 v2 ORB_O28.PATIENT group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        ORDER (Optional[List[ORB_O28_ORDER]]): optional
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

    ORDER: Optional[List[_ORB_O28_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
