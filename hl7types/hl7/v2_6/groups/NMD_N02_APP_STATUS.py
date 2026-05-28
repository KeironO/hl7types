"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NMD_N02.APP_STATUS
Type: Group
"""

from __future__ import annotations

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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
