"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFR_M05.MF_QUERY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.LCC import LCC
from ..segments.LCH import LCH
from ..segments.LDP import LDP
from ..segments.LOC import LOC
from ..segments.LRL import LRL
from ..segments.MFE import MFE

_LCC = LCC
_LCH = LCH
_LDP = LDP
_LOC = LOC
_LRL = LRL
_MFE = MFE


class MFR_M05_MF_QUERY(BaseModel):
    """HL7 v2 MFR_M05.MF_QUERY group.

    Attributes:
        MFE (MFE): required
        LOC (LOC): required
        LCH (Optional[List[LCH]]): optional
        LRL (Optional[List[LRL]]): optional
        LDP (List[LDP]): required
        LCC (Optional[List[LCC]]): optional
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

    LCH: list[_LCH] | None = Field(
        default=None,
        title="LCH",
        description="Optional, repeating",
    )

    LRL: list[_LRL] | None = Field(
        default=None,
        title="LRL",
        description="Optional, repeating",
    )

    LDP: list[_LDP] = Field(
        default=...,
        title="LDP",
        description="Required, repeating",
    )

    LCC: list[_LCC] | None = Field(
        default=None,
        title="LCC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
