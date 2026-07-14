"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RAS_O17.ADMINISTRATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .RAS_O17_OBSERVATION import RAS_O17_OBSERVATION

_PRT = PRT
_RAS_O17_OBSERVATION = RAS_O17_OBSERVATION
_RXA = RXA
_RXR = RXR


class RAS_O17_ADMINISTRATION(HL7Model):
    """HL7 v2 RAS_O17.ADMINISTRATION group.

    Attributes:
        RXA (List[RXA]): Pharmacy/Treatment Administration, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        RXR (RXR): Pharmacy/Treatment Route, required
        OBSERVATION (Optional[List[RAS_O17_OBSERVATION]]): optional
    """

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    OBSERVATION: Optional[List[_RAS_O17_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
