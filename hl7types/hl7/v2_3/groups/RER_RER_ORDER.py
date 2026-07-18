"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RER_RER.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_ORC = ORC
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RER_RER_ORDER(HL7Model):
    """HL7 v2 RER_RER.ORDER group.

    Attributes:
        ORC (ORC): Common order segment, required
        RXE (RXE): Pharmacy encoded order segment, required
        RXR (List[RXR]): Pharmacy route segment, required
        RXC (Optional[List[RXC]]): Pharmacy component order segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common order segment",
    )

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy encoded order segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy route segment",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy component order segment",
    )

    model_config = ConfigDict(populate_by_name=True)
