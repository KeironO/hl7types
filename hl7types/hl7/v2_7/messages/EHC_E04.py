"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E04_REASSESSMENT_REQUEST_INFO import EHC_E04_REASSESSMENT_REQUEST_INFO

_EHC_E04_REASSESSMENT_REQUEST_INFO = EHC_E04_REASSESSMENT_REQUEST_INFO
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E04(HL7Model):
    """Re-Assess HealthCare Services Invoice Request (S16.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        REASSESSMENT_REQUEST_INFO (EHC_E04_REASSESSMENT_REQUEST_INFO): required
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

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    REASSESSMENT_REQUEST_INFO: _EHC_E04_REASSESSMENT_REQUEST_INFO = Field(
        title="REASSESSMENT_REQUEST_INFO",
    )

    model_config = {"populate_by_name": True}
