"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BTS_O31.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.BPO import BPO
from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .BTS_O31_PRODUCT_STATUS import BTS_O31_PRODUCT_STATUS
from .BTS_O31_TIMING import BTS_O31_TIMING

_BPO = BPO
_BTS_O31_PRODUCT_STATUS = BTS_O31_PRODUCT_STATUS
_BTS_O31_TIMING = BTS_O31_TIMING
_NTE = NTE
_ORC = ORC


class BTS_O31_ORDER(BaseModel):
    """HL7 v2 BTS_O31.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[BTS_O31_TIMING]]): optional
        BPO (BPO): required
        NTE (Optional[List[NTE]]): optional
        PRODUCT_STATUS (Optional[List[BTS_O31_PRODUCT_STATUS]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_BTS_O31_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    BPO: _BPO = Field(
        default=...,
        title="BPO",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRODUCT_STATUS: Optional[List[_BTS_O31_PRODUCT_STATUS]] = Field(
        default=None,
        title="PRODUCT_STATUS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
