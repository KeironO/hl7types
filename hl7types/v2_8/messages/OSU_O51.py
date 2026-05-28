"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OSU_O51
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OSU_O51_ORDER_STATUS import OSU_O51_ORDER_STATUS

_ARV = ARV
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_OSU_O51_ORDER_STATUS = OSU_O51_ORDER_STATUS
_PID = PID
_SFT = SFT
_UAC = UAC


class OSU_O51(BaseModel):
    """HL7 v2 OSU_O51 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PID (Optional[PID]): optional
        ARV (Optional[List[ARV]]): optional
        ORDER_STATUS (List[OSU_O51_ORDER_STATUS]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    ORDER_STATUS: List[_OSU_O51_ORDER_STATUS] = Field(
        default=...,
        title="ORDER_STATUS",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
