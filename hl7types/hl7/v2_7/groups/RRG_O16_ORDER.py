"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RRG_O16.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .RRG_O16_GIVE import RRG_O16_GIVE
from .RRG_O16_TIMING import RRG_O16_TIMING

_ORC = ORC
_PRT = PRT
_RRG_O16_GIVE = RRG_O16_GIVE
_RRG_O16_TIMING = RRG_O16_TIMING


class RRG_O16_ORDER(HL7Model):
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_RRG_O16_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    GIVE: Optional[_RRG_O16_GIVE] = Field(
        default=None,
        title="GIVE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
