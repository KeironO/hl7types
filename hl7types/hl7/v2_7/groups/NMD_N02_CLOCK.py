"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: NMD_N02.CLOCK
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NCK import NCK
from ..segments.NTE import NTE

_NCK = NCK
_NTE = NTE


class NMD_N02_CLOCK(BaseModel):
    """HL7 v2 NMD_N02.CLOCK group.

    Attributes:
        NCK (NCK): required
        NTE (Optional[List[NTE]]): optional
    """

    NCK: _NCK = Field(
        default=...,
        title="NCK",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
