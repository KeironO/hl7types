"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NMR_N01.APP_STATUS
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


class NMR_N01_APP_STATUS(HL7Model):
    """HL7 v2 NMR_N01.APP_STATUS group.

    Attributes:
        NSC (NSC): Application Status Change, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    NSC: _NSC = Field(
        title="NSC",
        description="Application Status Change",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
