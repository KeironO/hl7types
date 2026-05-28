"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SIU_S12.SERVICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AIS import AIS
from ..segments.NTE import NTE

_AIS = AIS
_NTE = NTE


class SIU_S12_SERVICE(BaseModel):
    """HL7 v2 SIU_S12.SERVICE group.

    Attributes:
        AIS (AIS): required
        NTE (Optional[List[NTE]]): optional
    """

    AIS: _AIS = Field(
        default=...,
        title="AIS",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
