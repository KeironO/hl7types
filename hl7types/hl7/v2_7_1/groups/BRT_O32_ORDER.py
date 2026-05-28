"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BRT_O32.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BPO import BPO
from ..segments.BTX import BTX
from ..segments.ORC import ORC
from .BRT_O32_TIMING import BRT_O32_TIMING

_BPO = BPO
_BRT_O32_TIMING = BRT_O32_TIMING
_BTX = BTX
_ORC = ORC


class BRT_O32_ORDER(BaseModel):
    """HL7 v2 BRT_O32.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[BRT_O32_TIMING]]): optional
        BPO (Optional[BPO]): optional
        BTX (Optional[List[BTX]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_BRT_O32_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    BPO: _BPO | None = Field(
        default=None,
        title="BPO",
        description="Optional",
    )

    BTX: list[_BTX] | None = Field(
        default=None,
        title="BTX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
