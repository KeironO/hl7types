"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ACK
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_ERR = ERR
_MSA = MSA
_MSH = MSH


class ACK(BaseModel):
    """HL7 v2 ACK message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
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

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
