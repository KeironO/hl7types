"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: NMR_N01.CLOCK_AND_STATS_WITH_NOTES_ALT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NCK import NCK
from ..segments.NSC import NSC
from ..segments.NST import NST
from ..segments.NTE import NTE

_NCK = NCK
_NSC = NSC
_NST = NST
_NTE = NTE


class NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT(BaseModel):
    """HL7 v2 NMR_N01.CLOCK_AND_STATS_WITH_NOTES_ALT group.

    Attributes:
        NCK (Optional[NCK]): optional
        NTE (Optional[List[NTE]]): optional
        NST (Optional[NST]): optional
        NSC (Optional[NSC]): optional
    """

    NCK: _NCK | None = Field(
        default=None,
        title="NCK",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    NST: _NST | None = Field(
        default=None,
        title="NST",
        description="Optional",
    )

    NSC: _NSC | None = Field(
        default=None,
        title="NSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
