"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORL_O22.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORL_O22_ORDER import ORL_O22_ORDER

_ORL_O22_ORDER = ORL_O22_ORDER
_PID = PID
_PRT = PRT


class ORL_O22_RESPONSE(BaseModel):
    """HL7 v2 ORL_O22.RESPONSE group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ORDER (Optional[List[ORL_O22_ORDER]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_ORL_O22_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
