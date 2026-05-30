"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M05.MF_LOCATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.LCH import LCH
from ..segments.LOC import LOC
from ..segments.LRL import LRL
from ..segments.MFE import MFE

from .MFN_M05_MF_LOC_DEPT import MFN_M05_MF_LOC_DEPT

_LCH = LCH
_LOC = LOC
_LRL = LRL
_MFE = MFE
_MFN_M05_MF_LOC_DEPT = MFN_M05_MF_LOC_DEPT


class MFN_M05_MF_LOCATION(HL7Model):
    """HL7 v2 MFN_M05.MF_LOCATION group.

    Attributes:
        MFE (MFE): required
        LOC (LOC): required
        LCH (Optional[List[LCH]]): optional
        LRL (Optional[List[LRL]]): optional
        MF_LOC_DEPT (List[MFN_M05_MF_LOC_DEPT]): required
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    LOC: _LOC = Field(
        default=...,
        title="LOC",
        description="Required",
    )

    LCH: Optional[List[_LCH]] = Field(
        default=None,
        title="LCH",
        description="Optional, repeating",
    )

    LRL: Optional[List[_LRL]] = Field(
        default=None,
        title="LRL",
        description="Optional, repeating",
    )

    MF_LOC_DEPT: List[_MFN_M05_MF_LOC_DEPT] = Field(
        default=...,
        title="MF_LOC_DEPT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
