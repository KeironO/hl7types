"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NMQ_N01.CLOCK_AND_STATISTICS
Type: Group
"""

from __future__ import annotations

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

    NCK: _NCK | None = Field(
        default=None,
        title="NCK",
        description="Optional",
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
