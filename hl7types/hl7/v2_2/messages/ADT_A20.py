"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
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
    """HL7 v2 ADT_A20 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        EVN (EVN): EVENT TYPE, required
        NPU (NPU): BED STATUS UPDATE, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVENT TYPE",
    )

    NPU: _NPU = Field(
        title="NPU",
        description="BED STATUS UPDATE",
    )

    model_config = {"populate_by_name": True}
