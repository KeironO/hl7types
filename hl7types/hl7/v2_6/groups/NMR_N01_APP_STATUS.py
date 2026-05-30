"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NMR_N01.APP_STATUS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NSC import NSC
from ..segments.NTE import NTE

_NSC = NSC
_NTE = NTE


class NMR_N01_APP_STATUS(HL7Model):
    """HL7 v2 NMR_N01.APP_STATUS group.

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
