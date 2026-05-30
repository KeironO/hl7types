"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NMR_N01.CLOCK_AND_STATS_WITH_NOTES_ALT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NCK import NCK
from ..segments.NSC import NSC
from ..segments.NST import NST
from ..segments.NTE import NTE

_NCK = NCK
_NSC = NSC
_NST = NST
_NTE = NTE


class NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT(HL7Model):
    """HL7 v2 NMR_N01.CLOCK_AND_STATS_WITH_NOTES_ALT group.

    Attributes:
        NCK (Optional[NCK]): optional
        NTE (Optional[List[NTE]]): optional
        NST (Optional[NST]): optional
        NSC (Optional[NSC]): optional
    """

    NCK: Optional[_NCK] = Field(
        default=None,
        title="NCK",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    NST: Optional[_NST] = Field(
        default=None,
        title="NST",
        description="Optional",
    )

    NSC: Optional[_NSC] = Field(
        default=None,
        title="NSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
