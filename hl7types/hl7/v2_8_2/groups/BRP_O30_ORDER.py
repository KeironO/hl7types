"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: BRP_O30.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BPO import BPO
from ..segments.BPX import BPX
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .BRP_O30_TIMING import BRP_O30_TIMING

_BPO = BPO
_BPX = BPX
_BRP_O30_TIMING = BRP_O30_TIMING
_ORC = ORC
_PRT = PRT


class BRP_O30_ORDER(BaseModel):
    """HL7 v2 BRP_O30.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[BRP_O30_TIMING]]): optional
        BPO (Optional[BPO]): optional
        BPX (Optional[List[BPX]]): optional
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

    TIMING: list[_BRP_O30_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    BPO: _BPO | None = Field(
        default=None,
        title="BPO",
        description="Optional",
    )

    BPX: list[_BPX] | None = Field(
        default=None,
        title="BPX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
