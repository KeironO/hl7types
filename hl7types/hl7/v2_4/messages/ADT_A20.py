"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A20
Type: Message
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.NPU import NPU

_EVN = EVN
_MSH = MSH
_NPU = NPU


class ADT_A20(HL7Model):
    """ADT/ACK -  Bed status update (S3).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        NPU (NPU): Bed status update, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    NPU: _NPU = Field(
        title="NPU",
        description="Bed status update",
    )

    model_config = ConfigDict(populate_by_name=True)
