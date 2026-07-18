"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCQ_I19
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.REL import REL
from ..segments.RF1 import RF1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CCQ_I19_PROVIDER_CONTACT import CCQ_I19_PROVIDER_CONTACT

_CCQ_I19_PROVIDER_CONTACT = CCQ_I19_PROVIDER_CONTACT
_MSH = MSH
_REL = REL
_RF1 = RF1
_SFT = SFT
_UAC = UAC


class CCQ_I19(HL7Model):
    """Collaborative Care Query/Collaborative Care Query Update (S11.7.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        RF1 (RF1): Referral Information, required
        PROVIDER_CONTACT (Optional[List[CCQ_I19_PROVIDER_CONTACT]]): optional
        REL (Optional[List[REL]]): Clinical Relationship Segment, optional
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

    RF1: _RF1 = Field(
        title="RF1",
        description="Referral Information",
    )

    PROVIDER_CONTACT: Optional[List[_CCQ_I19_PROVIDER_CONTACT]] = Field(
        default=None,
        title="PROVIDER_CONTACT",
    )

    REL: Optional[List[_REL]] = Field(
        default=None,
        title="REL",
        description="Clinical Relationship Segment",
    )

    model_config = ConfigDict(populate_by_name=True)
