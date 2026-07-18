"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: VXR_V03.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .VXR_V03_OBSERVATION import VXR_V03_OBSERVATION
from .VXR_V03_TIMING import VXR_V03_TIMING

_ORC = ORC
_RXA = RXA
_RXR = RXR
_VXR_V03_OBSERVATION = VXR_V03_OBSERVATION
_VXR_V03_TIMING = VXR_V03_TIMING


class VXR_V03_ORDER(HL7Model):
    """HL7 v2 VXR_V03.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[VXR_V03_TIMING]]): optional
        RXA (RXA): Pharmacy/Treatment Administration, required
        RXR (Optional[RXR]): Pharmacy/Treatment Route, optional
        OBSERVATION (Optional[List[VXR_V03_OBSERVATION]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_VXR_V03_TIMING]] = Field(
        default=None,
        title="TIMING",
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

    OBSERVATION: Optional[List[_VXR_V03_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
