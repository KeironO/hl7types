"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: MCF_Q02
Type: Message
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH

_MSA = MSA
_MSH = MSH


class MCF_Q02(HL7Model):
    """HL7 v2 MCF_Q02 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (MSA): MESSAGE ACKNOWLEDGMENT, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
    )

    model_config = {"populate_by_name": True}
