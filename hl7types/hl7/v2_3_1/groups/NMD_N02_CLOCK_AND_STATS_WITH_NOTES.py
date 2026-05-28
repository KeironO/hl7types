"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NMD_N02.CLOCK_AND_STATS_WITH_NOTES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .NMD_N02_APP_STATS import NMD_N02_APP_STATS
from .NMD_N02_APP_STATUS import NMD_N02_APP_STATUS
from .NMD_N02_CLOCK import NMD_N02_CLOCK

_NMD_N02_APP_STATS = NMD_N02_APP_STATS
_NMD_N02_APP_STATUS = NMD_N02_APP_STATUS
_NMD_N02_CLOCK = NMD_N02_CLOCK


class NMD_N02_CLOCK_AND_STATS_WITH_NOTES(BaseModel):
    """HL7 v2 NMD_N02.CLOCK_AND_STATS_WITH_NOTES group.

    Attributes:
        CLOCK (Optional[NMD_N02_CLOCK]): optional
        APP_STATS (Optional[NMD_N02_APP_STATS]): optional
        APP_STATUS (Optional[NMD_N02_APP_STATUS]): optional
    """

    CLOCK: _NMD_N02_CLOCK | None = Field(
        default=None,
        title="CLOCK",
        description="Optional",
    )

    APP_STATS: _NMD_N02_APP_STATS | None = Field(
        default=None,
        title="APP_STATS",
        description="Optional",
    )

    APP_STATUS: _NMD_N02_APP_STATUS | None = Field(
        default=None,
        title="APP_STATUS",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
