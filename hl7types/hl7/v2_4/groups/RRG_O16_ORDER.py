"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRG_O16.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RRG_O16_GIVE import RRG_O16_GIVE

_ORC = ORC
_RRG_O16_GIVE = RRG_O16_GIVE


class RRG_O16_ORDER(HL7Model):
    """HL7 v2 RRG_O16.ORDER group.

    Attributes:
        ORC (ORC): required
        GIVE (Optional[RRG_O16_GIVE]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    GIVE: Optional[_RRG_O16_GIVE] = Field(
        default=None,
        title="GIVE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
