"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: BRT_O32.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.BPO import BPO
from ..segments.BTX import BTX
from ..segments.ORC import ORC

from .BRT_O32_TIMING import BRT_O32_TIMING

_BPO = BPO
_BRT_O32_TIMING = BRT_O32_TIMING
_BTX = BTX
_ORC = ORC


class BRT_O32_ORDER(HL7Model):
    """HL7 v2 BRT_O32.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[BRT_O32_TIMING]]): optional
        BPO (Optional[BPO]): Blood product order, optional
        BTX (Optional[List[BTX]]): Blood Product Transfusion/Disposition, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_BRT_O32_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    BPO: Optional[_BPO] = Field(
        default=None,
        title="BPO",
        description="Blood product order",
    )

    BTX: Optional[List[_BTX]] = Field(
        default=None,
        title="BTX",
        description="Blood Product Transfusion/Disposition",
    )

    model_config = ConfigDict(populate_by_name=True)
