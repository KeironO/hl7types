"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NMQ_N01.CLOCK_AND_STATISTICS
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.NCK import NCK
from ..segments.NSC import NSC
from ..segments.NST import NST

_NCK = NCK
_NSC = NSC
_NST = NST


class NMQ_N01_CLOCK_AND_STATISTICS(BaseModel):
    """HL7 v2 NMQ_N01.CLOCK_AND_STATISTICS group.

    Attributes:
        NCK (Optional[NCK]): optional
        NST (Optional[NST]): optional
        NSC (Optional[NSC]): optional
    """

    NCK: Optional[_NCK] = Field(
        default=None,
        title="NCK",
        description="Optional",
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
