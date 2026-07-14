"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A20
Type: Message
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.NPU import NPU

_EVN = EVN
_MSH = MSH
_NPU = NPU


class ADT_A20(HL7Model):
    """ADT/ACK -  Bed status update.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        NPU (NPU): NPU - bed status update segment, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVN - event type segment",
    )

    NPU: _NPU = Field(
        title="NPU",
        description="NPU - bed status update segment",
    )

    model_config = {"populate_by_name": True}
