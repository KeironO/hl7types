"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORB_O28.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.BPO import BPO
from ..segments.ORC import ORC

from .ORB_O28_TIMING import ORB_O28_TIMING

_BPO = BPO
_ORB_O28_TIMING = ORB_O28_TIMING
_ORC = ORC


class ORB_O28_ORDER(BaseModel):
    """HL7 v2 ORB_O28.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[ORB_O28_TIMING]]): optional
        BPO (Optional[BPO]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_ORB_O28_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    BPO: Optional[_BPO] = Field(
        default=None,
        title="BPO",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
