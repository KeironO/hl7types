"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
from .VXU_V04_TIMING import VXU_V04_TIMING

_ORC = ORC
_RXA = RXA
_RXR = RXR
_VXU_V04_OBSERVATION = VXU_V04_OBSERVATION
_VXU_V04_TIMING = VXU_V04_TIMING


class VXU_V04_ORDER(HL7Model):
    """HL7 v2 VXU_V04.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[VXU_V04_TIMING]]): optional
        RXA (RXA): required
        RXR (Optional[RXR]): optional
        OBSERVATION (Optional[List[VXU_V04_OBSERVATION]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_VXU_V04_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: Optional[_RXR] = Field(
        default=None,
        title="RXR",
        description="Optional",
    )

    OBSERVATION: Optional[List[_VXU_V04_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
