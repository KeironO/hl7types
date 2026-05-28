"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ORL_O40.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from ..segments.PRT import PRT
from .ORL_O40_ORDER import ORL_O40_ORDER

_ORL_O40_ORDER = ORL_O40_ORDER
_PID = PID
_PRT = PRT


class ORL_O40_PATIENT(BaseModel):
    """HL7 v2 ORL_O40.PATIENT group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ORDER (Optional[List[ORL_O40_ORDER]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ORDER: list[_ORL_O40_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
