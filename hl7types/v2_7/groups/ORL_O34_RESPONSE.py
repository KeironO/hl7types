"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORL_O34.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORL_O34_SPECIMEN import ORL_O34_SPECIMEN

_ORL_O34_SPECIMEN = ORL_O34_SPECIMEN
_PID = PID
_PRT = PRT


class ORL_O34_RESPONSE(BaseModel):
    """HL7 v2 ORL_O34.RESPONSE group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        SPECIMEN (List[ORL_O34_SPECIMEN]): required
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

    SPECIMEN: List[_ORL_O34_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
