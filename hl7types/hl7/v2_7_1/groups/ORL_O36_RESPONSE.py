"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ORL_O36.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from ..segments.PRT import PRT
from .ORL_O36_SPECIMEN import ORL_O36_SPECIMEN

_ORL_O36_SPECIMEN = ORL_O36_SPECIMEN
_PID = PID
_PRT = PRT


class ORL_O36_RESPONSE(BaseModel):
    """HL7 v2 ORL_O36.RESPONSE group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        SPECIMEN (List[ORL_O36_SPECIMEN]): required
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

    SPECIMEN: list[_ORL_O36_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
