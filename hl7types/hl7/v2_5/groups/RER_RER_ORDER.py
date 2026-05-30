"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RER_RER.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
        ORC (ORC): required
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
