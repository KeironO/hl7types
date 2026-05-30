"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMN_O07.TIMING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.TQ1 import TQ1
from ..segments.TQ2 import TQ2

_TQ1 = TQ1
_TQ2 = TQ2


class OMN_O07_TIMING(HL7Model):
    """HL7 v2 OMN_O07.TIMING group.

    Attributes:
        TQ1 (TQ1): required
        TQ2 (Optional[List[TQ2]]): optional
    """

    TQ1: _TQ1 = Field(
        default=...,
        title="TQ1",
        description="Required",
    )

    TQ2: Optional[List[_TQ2]] = Field(
        default=None,
        title="TQ2",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
