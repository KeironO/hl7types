"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: BRP_O30
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

from ..groups.BRP_O30_RESPONSE import BRP_O30_RESPONSE

_BRP_O30_RESPONSE = BRP_O30_RESPONSE
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_SFT = SFT


class BRP_O30(HL7Model):
    """BRP - Blood product dispense status acknowledgment (S4.20.4).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RESPONSE (Optional[BRP_O30_RESPONSE]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    RESPONSE: Optional[_BRP_O30_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    model_config = {"populate_by_name": True}
