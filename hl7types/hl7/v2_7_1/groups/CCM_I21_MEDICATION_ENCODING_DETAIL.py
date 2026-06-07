"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCM_I21.MEDICATION_ENCODING_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_OBX = OBX
_RXC = RXC
_RXE = RXE
_RXR = RXR


class CCM_I21_MEDICATION_ENCODING_DETAIL(HL7Model):
    """HL7 v2 CCM_I21.MEDICATION_ENCODING_DETAIL group.

    Attributes:
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
