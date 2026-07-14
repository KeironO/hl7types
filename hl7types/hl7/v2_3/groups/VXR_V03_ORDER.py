"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VXR_V03.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .VXR_V03_OBSERVATION import VXR_V03_OBSERVATION

_ORC = ORC
_RXA = RXA
_RXR = RXR
_VXR_V03_OBSERVATION = VXR_V03_OBSERVATION


class VXR_V03_ORDER(HL7Model):
    """HL7 v2 VXR_V03.ORDER group.

    Attributes:
        ORC (Optional[ORC]): Common order segment, optional
        RXA (RXA): Pharmacy administration segment, required
        RXR (Optional[RXR]): Pharmacy route segment, optional
        OBSERVATION (Optional[List[VXR_V03_OBSERVATION]]): optional
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

    OBSERVATION: Optional[List[_VXR_V03_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
