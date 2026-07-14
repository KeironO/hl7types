"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ACK
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_ERR = ERR
_MSA = MSA
_MSH = MSH


class ACK(HL7Model):
    """General acknowledgment message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (MSA): MESSAGE ACKNOWLEDGMENT, required
        ERR (Optional[ERR]): ERROR, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERROR",
    )

    model_config = {"populate_by_name": True}
