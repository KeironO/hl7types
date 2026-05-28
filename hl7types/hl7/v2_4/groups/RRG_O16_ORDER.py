"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRG_O16.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .RRG_O16_GIVE import RRG_O16_GIVE

_ORC = ORC
_RRG_O16_GIVE = RRG_O16_GIVE


class RRG_O16_ORDER(BaseModel):
    """HL7 v2 RRG_O16.ORDER group.

    Attributes:
        ORC (ORC): required
        GIVE (Optional[RRG_O16_GIVE]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    GIVE: _RRG_O16_GIVE | None = Field(
        default=None,
        title="GIVE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
