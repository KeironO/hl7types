"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_Z82.TIMING_ENCODED
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.TQ1 import TQ1
from ..segments.TQ2 import TQ2

_TQ1 = TQ1
_TQ2 = TQ2


class RSP_Z82_TIMING_ENCODED(BaseModel):
    """HL7 v2 RSP_Z82.TIMING_ENCODED group.

    Attributes:
        TQ1 (TQ1): required
        TQ2 (Optional[List[TQ2]]): optional
    """

    TQ1: _TQ1 = Field(
        default=...,
        title="TQ1",
        description="Required",
    )

    TQ2: list[_TQ2] | None = Field(
        default=None,
        title="TQ2",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
