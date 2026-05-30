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
    """HL7 v2 EHC_E04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        REASSESSMENT_REQUEST_INFO (EHC_E04_REASSESSMENT_REQUEST_INFO): required
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

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    REASSESSMENT_REQUEST_INFO: _EHC_E04_REASSESSMENT_REQUEST_INFO = Field(
        default=...,
        title="REASSESSMENT_REQUEST_INFO",
        description="Required",
    )

    model_config = {"populate_by_name": True}
