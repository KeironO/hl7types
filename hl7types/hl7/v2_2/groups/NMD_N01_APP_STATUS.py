"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NMD_N01.APP_STATUS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NSC import NSC
from ..segments.NTE import NTE

_NSC = NSC
_NTE = NTE


class NMD_N01_APP_STATUS(HL7Model):
    """HL7 v2 NMD_N01.APP_STATUS group.

    Attributes:
        NSC (NSC): STATUS CHANGE, required
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
    """

    NSC: _NSC = Field(
        title="NSC",
        description="STATUS CHANGE",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NOTES AND COMMENTS",
    )

    model_config = ConfigDict(populate_by_name=True)
