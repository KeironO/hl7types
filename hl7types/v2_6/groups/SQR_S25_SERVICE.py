"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SQR_S25.SERVICE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AIS import AIS
from ..segments.NTE import NTE

_AIS = AIS
_NTE = NTE


class SQR_S25_SERVICE(BaseModel):
    """HL7 v2 SQR_S25.SERVICE group.

    Attributes:
        AIS (AIS): required
        NTE (Optional[List[NTE]]): optional
    """

    AIS: _AIS = Field(
        default=...,
        title="AIS",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
