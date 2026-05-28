"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORN_O02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ORN_O02_RESPONSE import ORN_O02_RESPONSE
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORN_O02_RESPONSE = ORN_O02_RESPONSE


class ORN_O02(BaseModel):
    """HL7 v2 ORN_O02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[ORN_O02_RESPONSE]): optional
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

    RESPONSE: _ORN_O02_RESPONSE | None = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
