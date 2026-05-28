"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BAR_P05.INSURANCE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3
from ..segments.ROL import ROL

_IN1 = IN1
_IN2 = IN2
_IN3 = IN3
_ROL = ROL


class BAR_P05_INSURANCE(BaseModel):
    """HL7 v2 BAR_P05.INSURANCE group.

    Attributes:
        IN1 (IN1): required
        IN2 (Optional[IN2]): optional
        IN3 (Optional[List[IN3]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    IN1: _IN1 = Field(
        default=...,
        title="IN1",
        description="Required",
    )

    IN2: Optional[_IN2] = Field(
        default=None,
        title="IN2",
        description="Optional",
    )

    IN3: Optional[List[_IN3]] = Field(
        default=None,
        title="IN3",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
