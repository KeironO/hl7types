"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ACK_N02
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH

_MSA = MSA
_MSH = MSH


class ACK_N02(HL7Model):
    """HL7 v2 ACK_N02 message.

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
