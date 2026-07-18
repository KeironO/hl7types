"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORB_O28
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ORB_O28_RESPONSE import ORB_O28_RESPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORB_O28_RESPONSE = ORB_O28_RESPONSE
_SFT = SFT
_UAC = UAC


class ORB_O28(HL7Model):
    """ORB - Blood product order acknowledgment (S4.13.2).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RESPONSE (Optional[ORB_O28_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    RESPONSE: Optional[_ORB_O28_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    model_config = ConfigDict(populate_by_name=True)
