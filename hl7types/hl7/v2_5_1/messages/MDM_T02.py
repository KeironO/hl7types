"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MDM_T02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MDM_T02_COMMON_ORDER import MDM_T02_COMMON_ORDER
from ..groups.MDM_T02_OBXNTE_SUPPGRP import MDM_T02_OBXNTE_SUPPGRP
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.TXA import TXA

_EVN = EVN
_MDM_T02_COMMON_ORDER = MDM_T02_COMMON_ORDER
_MDM_T02_OBXNTE_SUPPGRP = MDM_T02_OBXNTE_SUPPGRP
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT
_TXA = TXA


class MDM_T02(BaseModel):
    """HL7 v2 MDM_T02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        COMMON_ORDER (Optional[List[MDM_T02_COMMON_ORDER]]): optional
        TXA (TXA): required
        OBXNTE_SUPPGRP (List[MDM_T02_OBXNTE_SUPPGRP]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
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

    COMMON_ORDER: list[_MDM_T02_COMMON_ORDER] | None = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional, repeating",
    )

    TXA: _TXA = Field(
        default=...,
        title="TXA",
        description="Required",
    )

    OBXNTE_SUPPGRP: list[_MDM_T02_OBXNTE_SUPPGRP] = Field(
        default=...,
        title="OBXNTE_SUPPGRP",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
