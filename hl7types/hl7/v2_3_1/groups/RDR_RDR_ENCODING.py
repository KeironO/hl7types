"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDR_RDR.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_RXC = RXC
_RXE = RXE
_RXR = RXR


class RDR_RDR_ENCODING(HL7Model):
    """HL7 v2 RDR_RDR.ENCODING group.

    Attributes:
        RXE (RXE): RXE - pharmacy/treatment encoded order segment, required
        RXR (List[RXR]): RXR - pharmacy/treatment route segment, required
        RXC (Optional[List[RXC]]): RXC - pharmacy/treatment component order segment, optional
    """

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
