"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BPS_O29.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class BPS_O29_ORDER(HL7Model):
    """HL7 v2 BPS_O29.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING (Optional[List[BPS_O29_TIMING]]): optional
        BPO (BPO): Blood product order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRODUCT (Optional[List[BPS_O29_PRODUCT]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TIMING: Optional[List[_BPS_O29_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    BPO: _BPO = Field(
        title="BPO",
        description="Blood product order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PRODUCT: Optional[List[_BPS_O29_PRODUCT]] = Field(
        default=None,
        title="PRODUCT",
    )

    model_config = {"populate_by_name": True}
