"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MDM_T01
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CON import CON
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.TXA import TXA
from ..segments.UAC import UAC

from ..groups.MDM_T01_COMMON_ORDER import MDM_T01_COMMON_ORDER

_CON = CON
_EVN = EVN
_MDM_T01_COMMON_ORDER = MDM_T01_COMMON_ORDER
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT
_TXA = TXA
_UAC = UAC


class MDM_T01(BaseModel):
    """HL7 v2 MDM_T01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        COMMON_ORDER (Optional[List[MDM_T01_COMMON_ORDER]]): optional
        TXA (TXA): required
        CON (Optional[List[CON]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
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

    COMMON_ORDER: Optional[List[_MDM_T01_COMMON_ORDER]] = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional, repeating",
    )

    TXA: _TXA = Field(
        default=...,
        title="TXA",
        description="Required",
    )

    CON: Optional[List[_CON]] = Field(
        default=None,
        title="CON",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
