"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: INR_U06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.INV import INV
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EQU = EQU
_INV = INV
_MSH = MSH
_SFT = SFT
_UAC = UAC


class INR_U06(HL7Model):
    """HL7 v2 INR_U06 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        INV (List[INV]): required
    """

    MSH: _MSH = Field(
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

    EQU: _EQU = Field(
        title="EQU",
        description="Required",
    )

    INV: List[_INV] = Field(
        min_length=1,
        title="INV",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
