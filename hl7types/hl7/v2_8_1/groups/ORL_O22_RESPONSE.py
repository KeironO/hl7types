"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O22.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.PID import PID
from ..segments.PRT import PRT
from .ORL_O22_ORDER import ORL_O22_ORDER

_ARV = ARV
_ORL_O22_ORDER = ORL_O22_ORDER
_PID = PID
_PRT = PRT


class ORL_O22_RESPONSE(BaseModel):
    """HL7 v2 ORL_O22.RESPONSE group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        ORDER (Optional[List[ORL_O22_ORDER]]): optional
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

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    ORDER: list[_ORL_O22_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
