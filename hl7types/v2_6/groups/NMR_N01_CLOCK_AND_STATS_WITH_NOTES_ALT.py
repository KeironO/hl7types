"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NMR_N01.CLOCK_AND_STATS_WITH_NOTES_ALT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from .NMR_N01_APP_STATS import NMR_N01_APP_STATS
from .NMR_N01_APP_STATUS import NMR_N01_APP_STATUS
from .NMR_N01_CLOCK import NMR_N01_CLOCK

_NMR_N01_APP_STATS = NMR_N01_APP_STATS
_NMR_N01_APP_STATUS = NMR_N01_APP_STATUS
_NMR_N01_CLOCK = NMR_N01_CLOCK


class NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT(BaseModel):
    """HL7 v2 NMR_N01.CLOCK_AND_STATS_WITH_NOTES_ALT group.

    Attributes:
        CLOCK (Optional[NMR_N01_CLOCK]): optional
        APP_STATS (Optional[NMR_N01_APP_STATS]): optional
        APP_STATUS (Optional[NMR_N01_APP_STATUS]): optional
    """

    CLOCK: Optional[_NMR_N01_CLOCK] = Field(
        default=None,
        title="CLOCK",
        description="Optional",
    )

    APP_STATS: Optional[_NMR_N01_APP_STATS] = Field(
        default=None,
        title="APP_STATS",
        description="Optional",
    )

    APP_STATUS: Optional[_NMR_N01_APP_STATUS] = Field(
        default=None,
        title="APP_STATUS",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
