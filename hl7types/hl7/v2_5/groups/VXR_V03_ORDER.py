"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: VXR_V03.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class VXR_V03_ORDER(BaseModel):
    """HL7 v2 VXR_V03.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[VXR_V03_TIMING]]): optional
        RXA (RXA): required
        RXR (Optional[RXR]): optional
        OBSERVATION (Optional[List[VXR_V03_OBSERVATION]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_VXR_V03_TIMING] | None = Field(
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

    OBSERVATION: list[_VXR_V03_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
