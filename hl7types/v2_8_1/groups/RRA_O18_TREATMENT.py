"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RRA_O18.TREATMENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
