"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: VXU_V04.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.RXA import RXA
from ..segments.RXR import RXR
from .VXU_V04_OBSERVATION import VXU_V04_OBSERVATION
from .VXU_V04_TIMING import VXU_V04_TIMING

_ORC = ORC
_PRT = PRT
_RXA = RXA
_RXR = RXR
_VXU_V04_OBSERVATION = VXU_V04_OBSERVATION
_VXU_V04_TIMING = VXU_V04_TIMING


class VXU_V04_ORDER(BaseModel):
    """HL7 v2 VXU_V04.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
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

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: list[_VXU_V04_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: _RXR | None = Field(
        default=None,
        title="RXR",
        description="Optional",
    )

    OBSERVATION: list[_VXU_V04_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
