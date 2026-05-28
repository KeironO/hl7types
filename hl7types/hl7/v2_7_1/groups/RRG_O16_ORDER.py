"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RRG_O16.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .RRG_O16_GIVE import RRG_O16_GIVE
from .RRG_O16_TIMING import RRG_O16_TIMING

_ORC = ORC
_PRT = PRT
_RRG_O16_GIVE = RRG_O16_GIVE
_RRG_O16_TIMING = RRG_O16_TIMING


class RRG_O16_ORDER(BaseModel):
    """HL7 v2 RRG_O16.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[RRG_O16_TIMING]]): optional
        GIVE (Optional[RRG_O16_GIVE]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: list[_RRG_O16_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    GIVE: _RRG_O16_GIVE | None = Field(
        default=None,
        title="GIVE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
