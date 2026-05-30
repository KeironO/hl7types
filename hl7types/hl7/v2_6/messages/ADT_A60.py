"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ADT_A60
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.EVN import EVN
from ..segments.IAM import IAM
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ADT_A60_VISIT import ADT_A60_VISIT

_ADT_A60_VISIT = ADT_A60_VISIT
_ARV = ARV
_EVN = EVN
_IAM = IAM
_MSH = MSH
_PID = PID
_SFT = SFT
_UAC = UAC


class ADT_A60(HL7Model):
    """HL7 v2 ADT_A60 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        ARV (Optional[List[ARV]]): optional
        VISIT (Optional[ADT_A60_VISIT]): optional
        IAM (Optional[List[IAM]]): optional
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

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    VISIT: Optional[_ADT_A60_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    IAM: Optional[List[_IAM]] = Field(
        default=None,
        title="IAM",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
