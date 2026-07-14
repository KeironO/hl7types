"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E21
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E21_AUTHORIZATION_REQUEST import EHC_E21_AUTHORIZATION_REQUEST

_EHC_E21_AUTHORIZATION_REQUEST = EHC_E21_AUTHORIZATION_REQUEST
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E21(HL7Model):
    """Cancel Authorization Request (S16.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        AUTHORIZATION_REQUEST (EHC_E21_AUTHORIZATION_REQUEST): required
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

    AUTHORIZATION_REQUEST: _EHC_E21_AUTHORIZATION_REQUEST = Field(
        title="AUTHORIZATION_REQUEST",
    )

    model_config = {"populate_by_name": True}
