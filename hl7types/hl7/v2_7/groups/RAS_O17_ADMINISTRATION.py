"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RAS_O17.ADMINISTRATION
Type: Group
"""

from __future__ import annotations

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

    RXA: list[_RXA] = Field(
        default=...,
        title="RXA",
        description="Required, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    OBSERVATION: list[_RAS_O17_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
