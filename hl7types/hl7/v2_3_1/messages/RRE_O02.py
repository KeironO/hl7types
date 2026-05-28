"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRE_O02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RRE_O02_RESPONSE import RRE_O02_RESPONSE
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_RRE_O02_RESPONSE = RRE_O02_RESPONSE


class RRE_O02(BaseModel):
    """HL7 v2 RRE_O02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[RRE_O02_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: _ERR | None = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESPONSE: _RRE_O02_RESPONSE | None = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
