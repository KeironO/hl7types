"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BAR_P02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.BAR_P02_PATIENT import BAR_P02_PATIENT

_BAR_P02_PATIENT = BAR_P02_PATIENT
_EVN = EVN
_MSH = MSH
_SFT = SFT
_UAC = UAC


class BAR_P02(HL7Model):
    """HL7 v2 BAR_P02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PATIENT (List[BAR_P02_PATIENT]): required
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

    EVN: _EVN = Field(
        title="EVN",
        description="Required",
    )

    PATIENT: List[_BAR_P02_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
