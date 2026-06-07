"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ORG_O20_RESPONSE import ORG_O20_RESPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORG_O20_RESPONSE = ORG_O20_RESPONSE
_SFT = SFT
_UAC = UAC


class ORG_O20(HL7Model):
    """HL7 v2 ORG_O20 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[ORG_O20_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESPONSE: Optional[_ORG_O20_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
