"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RRA_O18.TREATMENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.RXA import RXA

_PRT = PRT
_RXA = RXA


class RRA_O18_TREATMENT(BaseModel):
    """HL7 v2 RRA_O18.TREATMENT group.

    Attributes:
        RXA (RXA): required
        PRT (Optional[List[PRT]]): optional
    """

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
