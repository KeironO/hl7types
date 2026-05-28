"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O34.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.PID import PID
from ..segments.PRT import PRT
from .ORL_O34_SPECIMEN import ORL_O34_SPECIMEN

_ARV = ARV
_ORL_O34_SPECIMEN = ORL_O34_SPECIMEN
_PID = PID
_PRT = PRT


class ORL_O34_RESPONSE(BaseModel):
    """HL7 v2 ORL_O34.RESPONSE group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        SPECIMEN (List[ORL_O34_SPECIMEN]): required
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

    SPECIMEN: list[_ORL_O34_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
