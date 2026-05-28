"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NMD_N02.APP_STATUS
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NSC import NSC
from ..segments.NTE import NTE

_NSC = NSC
_NTE = NTE


class NMD_N02_APP_STATUS(BaseModel):
    """HL7 v2 NMD_N02.APP_STATUS group.

    Attributes:
        NSC (NSC): required
        NTE (Optional[List[NTE]]): optional
    """

    NSC: _NSC = Field(
        default=...,
        title="NSC",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
