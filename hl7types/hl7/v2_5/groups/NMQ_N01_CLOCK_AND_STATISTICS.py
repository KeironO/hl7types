"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: NMQ_N01.CLOCK_AND_STATISTICS
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NCK import NCK
from ..segments.NSC import NSC
from ..segments.NST import NST

_NCK = NCK
_NSC = NSC
_NST = NST


class NMQ_N01_CLOCK_AND_STATISTICS(HL7Model):
    """HL7 v2 NMQ_N01.CLOCK_AND_STATISTICS group.

    Attributes:
        NCK (Optional[NCK]): System Clock, optional
        NST (Optional[NST]): Application control level statistics, optional
        NSC (Optional[NSC]): Application Status Change, optional
    """

    NCK: Optional[_NCK] = Field(
        default=None,
        title="NCK",
        description="System Clock",
    )

    NST: Optional[_NST] = Field(
        default=None,
        title="NST",
        description="Application control level statistics",
    )

    NSC: Optional[_NSC] = Field(
        default=None,
        title="NSC",
        description="Application Status Change",
    )

    model_config = ConfigDict(populate_by_name=True)
