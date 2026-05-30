"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RAR_RAR.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_RXC = RXC
_RXE = RXE
_RXR = RXR


class RAR_RAR_ENCODING(HL7Model):
    """HL7 v2 RAR_RAR.ENCODING group.

    Attributes:
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

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
