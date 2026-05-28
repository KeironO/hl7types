"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: MCF_Q02
Type: Message
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.MSA import MSA
from ..segments.MSH import MSH

_MSA = MSA
_MSH = MSH


class MCF_Q02(BaseModel):
    """HL7 v2 MCF_Q02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
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

    model_config = {"populate_by_name": True}
