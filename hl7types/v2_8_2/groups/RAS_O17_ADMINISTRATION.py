"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RAS_O17.ADMINISTRATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .RAS_O17_OBSERVATION import RAS_O17_OBSERVATION

_PRT = PRT
_RAS_O17_OBSERVATION = RAS_O17_OBSERVATION
_RXA = RXA
_RXR = RXR


class RAS_O17_ADMINISTRATION(BaseModel):
    """HL7 v2 RAS_O17.ADMINISTRATION group.

    Attributes:
        RXA (List[RXA]): required
        PRT (Optional[List[PRT]]): optional
        RXR (RXR): required
        OBSERVATION (Optional[List[RAS_O17_OBSERVATION]]): optional
    """

    RXA: List[_RXA] = Field(
        default=...,
        title="RXA",
        description="Required, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    OBSERVATION: Optional[List[_RAS_O17_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
