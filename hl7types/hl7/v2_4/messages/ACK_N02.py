"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ACK_N02
Type: Message
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH

_MSA = MSA
_MSH = MSH


class ACK_N02(HL7Model):
    """NMD/ACK - Application management data message (unsolicited) (S3).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    model_config = ConfigDict(populate_by_name=True)
