"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QSB_Q16
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.SFT import SFT

_DSC = DSC
_MSH = MSH
_QPD = QPD
_RCP = RCP
_SFT = SFT


class QSB_Q16(BaseModel):
    """HL7 v2 QSB_Q16 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QPD (QPD): required
        RCP (RCP): required
        DSC (Optional[DSC]): optional
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

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    RCP: _RCP = Field(
        default=...,
        title="RCP",
        description="Required",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
