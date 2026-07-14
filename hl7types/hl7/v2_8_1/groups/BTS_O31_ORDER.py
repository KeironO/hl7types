"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BTS_O31.ORDER
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

from .BTS_O31_PRODUCT_STATUS import BTS_O31_PRODUCT_STATUS
from .BTS_O31_TIMING import BTS_O31_TIMING

_BPO = BPO
_BTS_O31_PRODUCT_STATUS = BTS_O31_PRODUCT_STATUS
_BTS_O31_TIMING = BTS_O31_TIMING
_NTE = NTE
_ORC = ORC
_PRT = PRT


class BTS_O31_ORDER(HL7Model):
    """HL7 v2 BTS_O31.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING (Optional[List[BTS_O31_TIMING]]): optional
        BPO (BPO): Blood product order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRODUCT_STATUS (Optional[List[BTS_O31_PRODUCT_STATUS]]): optional
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

    TIMING: Optional[List[_BTS_O31_TIMING]] = Field(
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

    PRODUCT_STATUS: Optional[List[_BTS_O31_PRODUCT_STATUS]] = Field(
        default=None,
        title="PRODUCT_STATUS",
    )

    model_config = {"populate_by_name": True}
