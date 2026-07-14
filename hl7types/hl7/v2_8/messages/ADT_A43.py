"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A43
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

from ..groups.ADT_A43_PATIENT import ADT_A43_PATIENT

_ADT_A43_PATIENT = ADT_A43_PATIENT
_EVN = EVN
_MSH = MSH
_SFT = SFT
_UAC = UAC


class ADT_A43(HL7Model):
    """ADT/ACK - Move patient information - patient identifier list (S3.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PATIENT (List[ADT_A43_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PATIENT: List[_ADT_A43_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}
