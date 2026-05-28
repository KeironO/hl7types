"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: BPS_O29.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.BPO import BPO
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .BPS_O29_PRODUCT import BPS_O29_PRODUCT
from .BPS_O29_TIMING import BPS_O29_TIMING

_BPO = BPO
_BPS_O29_PRODUCT = BPS_O29_PRODUCT
_BPS_O29_TIMING = BPS_O29_TIMING
_NTE = NTE
_ORC = ORC
_PRT = PRT


class BPS_O29_ORDER(BaseModel):
    """HL7 v2 BPS_O29.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[BPS_O29_TIMING]]): optional
        BPO (BPO): required
        NTE (Optional[List[NTE]]): optional
        PRODUCT (Optional[List[BPS_O29_PRODUCT]]): optional
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

    TIMING: Optional[List[_BPS_O29_TIMING]] = Field(
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

    PRODUCT: Optional[List[_BPS_O29_PRODUCT]] = Field(
        default=None,
        title="PRODUCT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
