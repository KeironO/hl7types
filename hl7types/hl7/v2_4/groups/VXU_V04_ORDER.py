"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VXU_V04.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .VXU_V04_OBSERVATION import VXU_V04_OBSERVATION

_ORC = ORC
_RXA = RXA
_RXR = RXR
_VXU_V04_OBSERVATION = VXU_V04_OBSERVATION


class VXU_V04_ORDER(HL7Model):
    """HL7 v2 VXU_V04.ORDER group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        RXA (RXA): Pharmacy/Treatment Administration, required
        RXR (Optional[RXR]): Pharmacy/Treatment Route, optional
        OBSERVATION (Optional[List[VXU_V04_OBSERVATION]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    RXA: _RXA = Field(
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    RXR: Optional[_RXR] = Field(
        default=None,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    OBSERVATION: Optional[List[_VXU_V04_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
