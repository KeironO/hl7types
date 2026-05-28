"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: VXU_V04.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR
from .VXU_V04_OBSERVATION import VXU_V04_OBSERVATION

_ORC = ORC
_RXA = RXA
_RXR = RXR
_VXU_V04_OBSERVATION = VXU_V04_OBSERVATION


class VXU_V04_ORDER(BaseModel):
    """HL7 v2 VXU_V04.ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        RXA (RXA): required
        RXR (Optional[RXR]): optional
        OBSERVATION (Optional[List[VXU_V04_OBSERVATION]]): optional
    """

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
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
