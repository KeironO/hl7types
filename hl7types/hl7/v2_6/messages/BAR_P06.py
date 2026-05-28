"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BAR_P06
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.BAR_P06_PATIENT import BAR_P06_PATIENT
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_BAR_P06_PATIENT = BAR_P06_PATIENT
_EVN = EVN
_MSH = MSH
_SFT = SFT
_UAC = UAC


class BAR_P06(BaseModel):
    """HL7 v2 BAR_P06 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PATIENT (List[BAR_P06_PATIENT]): required
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    PATIENT: list[_BAR_P06_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
