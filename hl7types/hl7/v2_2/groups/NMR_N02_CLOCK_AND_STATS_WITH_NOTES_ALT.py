"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NMR_N02.CLOCK_AND_STATS_WITH_NOTES_ALT
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


class NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT(HL7Model):
    """HL7 v2 NMR_N02.CLOCK_AND_STATS_WITH_NOTES_ALT group.

    Attributes:
        NCK (Optional[NCK]): System Clock, optional
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
        NST (Optional[NST]): Statistics, optional
        NSC (Optional[NSC]): STATUS CHANGE, optional
    """

    NCK: Optional[_NCK] = Field(
        default=None,
        title="NCK",
        description="System Clock",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NOTES AND COMMENTS",
    )

    NST: Optional[_NST] = Field(
        default=None,
        title="NST",
        description="Statistics",
    )

    NSC: Optional[_NSC] = Field(
        default=None,
        title="NSC",
        description="STATUS CHANGE",
    )

    model_config = {"populate_by_name": True}
