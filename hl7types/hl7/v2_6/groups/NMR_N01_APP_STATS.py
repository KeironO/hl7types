"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NMR_N01.APP_STATS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NST import NST
from ..segments.NTE import NTE

_NST = NST
_NTE = NTE


class NMR_N01_APP_STATS(BaseModel):
    """HL7 v2 NMR_N01.APP_STATS group.

    Attributes:
        NST (NST): required
        NTE (Optional[List[NTE]]): optional
    """

    NST: _NST = Field(
        default=...,
        title="NST",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
