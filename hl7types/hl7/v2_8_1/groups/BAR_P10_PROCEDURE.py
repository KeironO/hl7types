"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BAR_P10.PROCEDURE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GP2 import GP2
from ..segments.PR1 import PR1

_GP2 = GP2
_PR1 = PR1


class BAR_P10_PROCEDURE(BaseModel):
    """HL7 v2 BAR_P10.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        GP2 (Optional[GP2]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    GP2: _GP2 | None = Field(
        default=None,
        title="GP2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
