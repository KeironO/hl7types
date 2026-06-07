"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BAR_P10.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GP2 import GP2
from ..segments.PR1 import PR1

_GP2 = GP2
_PR1 = PR1


class BAR_P10_PROCEDURE(HL7Model):
    """HL7 v2 BAR_P10.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        GP2 (Optional[GP2]): optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="Required",
    )

    GP2: Optional[_GP2] = Field(
        default=None,
        title="GP2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
