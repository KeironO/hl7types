"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRO_O02
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

from ..groups.RRO_O02_RESPONSE import RRO_O02_RESPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_RRO_O02_RESPONSE = RRO_O02_RESPONSE


class RRO_O02(HL7Model):
    """HL7 v2 RRO_O02 message.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        RESPONSE (Optional[RRO_O02_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERR - error segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    RESPONSE: Optional[_RRO_O02_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    model_config = {"populate_by_name": True}
