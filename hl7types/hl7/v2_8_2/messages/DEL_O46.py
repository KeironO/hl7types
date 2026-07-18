"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DEL_O46
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DON import DON
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DEL_O46_DONOR import DEL_O46_DONOR

_DEL_O46_DONOR = DEL_O46_DONOR
_DON = DON
_MSH = MSH
_NTE = NTE
_SFT = SFT
_UAC = UAC


class DEL_O46(HL7Model):
    """Donor Eligiblity Message (S4.16.13).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        DONOR (Optional[DEL_O46_DONOR]): optional
        DON (DON): Donation, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
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

    DONOR: Optional[_DEL_O46_DONOR] = Field(
        default=None,
        title="DONOR",
    )

    DON: _DON = Field(
        title="DON",
        description="Donation",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
