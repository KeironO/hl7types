"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORG_O20
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

from ..groups.ORG_O20_RESPONSE import ORG_O20_RESPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORG_O20_RESPONSE = ORG_O20_RESPONSE


class ORG_O20(HL7Model):
    """ORG/ORL - General clinical order response (S4).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RESPONSE (Optional[ORG_O20_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    RESPONSE: Optional[_ORG_O20_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    model_config = {"populate_by_name": True}
