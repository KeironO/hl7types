"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PMU_B03
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.STF import STF

_EVN = EVN
_MSH = MSH
_STF = STF


class PMU_B03(HL7Model):
    """HL7 v2 PMU_B03 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        STF (STF): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    STF: _STF = Field(
        default=...,
        title="STF",
        description="Required",
    )

    model_config = {"populate_by_name": True}
