"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O36
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ORL_O36_RESPONSE import ORL_O36_RESPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORL_O36_RESPONSE = ORL_O36_RESPONSE
_SFT = SFT
_UAC = UAC


class ORL_O36(HL7Model):
    """ORL - Laboratory order response message to a single container of a specimen OML (S4.4.11.1).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RESPONSE (Optional[ORL_O36_RESPONSE]): optional
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

    RESPONSE: Optional[_ORL_O36_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    model_config = {"populate_by_name": True}
