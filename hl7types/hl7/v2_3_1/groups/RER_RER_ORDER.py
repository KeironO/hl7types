"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        ORC (ORC): ORC - common order segment, required
        RXE (RXE): RXE - pharmacy/treatment encoded order segment, required
        RXR (List[RXR]): RXR - pharmacy/treatment route segment, required
        RXC (Optional[List[RXC]]): RXC - pharmacy/treatment component order segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    RXE: _RXE = Field(
        title="RXE",
        description="RXE - pharmacy/treatment encoded order segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="RXC - pharmacy/treatment component order segment",
    )

    model_config = ConfigDict(populate_by_name=True)
