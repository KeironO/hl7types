"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A60
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.IAM import IAM
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.SFT import SFT

_EVN = EVN
_IAM = IAM
_MSH = MSH
_PID = PID
_PV1 = PV1
_PV2 = PV2
_SFT = SFT


class ADT_A60(HL7Model):
    """HL7 v2 ADT_A60 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PV1 (Optional[PV1]): optional
        PV2 (Optional[PV2]): optional
        IAM (Optional[List[IAM]]): optional
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

    EVN: _EVN = Field(
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    IAM: Optional[List[_IAM]] = Field(
        default=None,
        title="IAM",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
