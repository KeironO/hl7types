"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RPA_I08.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.PR1 import PR1

from .RPA_I08_AUTHORIZATION2 import RPA_I08_AUTHORIZATION2

_PR1 = PR1
_RPA_I08_AUTHORIZATION2 = RPA_I08_AUTHORIZATION2


class RPA_I08_PROCEDURE(BaseModel):
    """HL7 v2 RPA_I08.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTHORIZATION2 (Optional[RPA_I08_AUTHORIZATION2]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    AUTHORIZATION2: Optional[_RPA_I08_AUTHORIZATION2] = Field(
        default=None,
        title="AUTHORIZATION2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
