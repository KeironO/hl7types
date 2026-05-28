"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: DOC_T12.EVNPIDPV1TXAOBX_SUPPGRP
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.TXA import TXA

_EVN = EVN
_OBX = OBX
_PID = PID
_PV1 = PV1
_TXA = TXA


class DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP(BaseModel):
    """HL7 v2 DOC_T12.EVNPIDPV1TXAOBX_SUPPGRP group.

    Attributes:
        EVN (Optional[EVN]): optional
        PID (PID): required
        PV1 (PV1): required
        TXA (TXA): required
        OBX (Optional[List[OBX]]): optional
    """

    EVN: Optional[_EVN] = Field(
        default=None,
        title="EVN",
        description="Optional",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    TXA: _TXA = Field(
        default=...,
        title="TXA",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
