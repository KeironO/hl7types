"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A16.INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AUT import AUT
from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3
from ..segments.RF1 import RF1
from ..segments.ROL import ROL

_AUT = AUT
_IN1 = IN1
_IN2 = IN2
_IN3 = IN3
_RF1 = RF1
_ROL = ROL


class ADT_A16_INSURANCE(BaseModel):
    """HL7 v2 ADT_A16.INSURANCE group.

    Attributes:
        IN1 (IN1): required
        IN2 (Optional[IN2]): optional
        IN3 (Optional[List[IN3]]): optional
        ROL (Optional[List[ROL]]): optional
        AUT (Optional[List[AUT]]): optional
        RF1 (Optional[List[RF1]]): optional
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

    AUT: Optional[List[_AUT]] = Field(
        default=None,
        title="AUT",
        description="Optional, repeating",
    )

    RF1: Optional[List[_RF1]] = Field(
        default=None,
        title="RF1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
