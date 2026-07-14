"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PMU_B03
Type: Message
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.STF import STF

_EVN = EVN
_MSH = MSH
_STF = STF


class PMU_B03(HL7Model):
    """PMU/ACK - Delete personnel re cord (S15).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        STF (STF): Staff Identification, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    STF: _STF = Field(
        title="STF",
        description="Staff Identification",
    )

    model_config = {"populate_by_name": True}
