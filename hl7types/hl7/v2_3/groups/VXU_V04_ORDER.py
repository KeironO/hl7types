"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VXU_V04.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        ORC (Optional[ORC]): Common order segment, optional
        RXA (RXA): Pharmacy administration segment, required
        RXR (Optional[RXR]): Pharmacy route segment, optional
        OBSERVATION (Optional[List[VXU_V04_OBSERVATION]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common order segment",
    )

    RXA: _RXA = Field(
        title="RXA",
        description="Pharmacy administration segment",
    )

    RXR: Optional[_RXR] = Field(
        default=None,
        title="RXR",
        description="Pharmacy route segment",
    )

    OBSERVATION: Optional[List[_VXU_V04_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
