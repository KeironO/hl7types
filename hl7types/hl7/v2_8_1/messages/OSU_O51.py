"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OSU_O51
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OSU_O51_ORDER_STATUS import OSU_O51_ORDER_STATUS
from ..segments.ARV import ARV
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PID: _PID | None = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    ORDER_STATUS: list[_OSU_O51_ORDER_STATUS] = Field(
        default=...,
        title="ORDER_STATUS",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
