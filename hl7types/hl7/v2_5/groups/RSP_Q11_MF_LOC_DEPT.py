"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Q11.MF_LOC_DEPT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.LCC import LCC
from ..segments.LCH import LCH
from ..segments.LDP import LDP

_LCC = LCC
_LCH = LCH
_LDP = LDP


class RSP_Q11_MF_LOC_DEPT(BaseModel):
    """HL7 v2 RSP_Q11.MF_LOC_DEPT group.

    Attributes:
        LDP (LDP): required
        LCH (Optional[List[LCH]]): optional
        LCC (Optional[List[LCC]]): optional
    """

    LDP: _LDP = Field(
        default=...,
        title="LDP",
        description="Required",
    )

    LCH: list[_LCH] | None = Field(
        default=None,
        title="LCH",
        description="Optional, repeating",
    )

    LCC: list[_LCC] | None = Field(
        default=None,
        title="LCC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
