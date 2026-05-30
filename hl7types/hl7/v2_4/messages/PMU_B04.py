"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PMU_B04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.STF import STF

_EVN = EVN
_MSH = MSH
_ORG = ORG
_PRA = PRA
_STF = STF


class PMU_B04(HL7Model):
    """HL7 v2 PMU_B04 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        STF (STF): required
        PRA (Optional[List[PRA]]): optional
        ORG (Optional[ORG]): optional
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

    PRA: Optional[List[_PRA]] = Field(
        default=None,
        title="PRA",
        description="Optional, repeating",
    )

    ORG: Optional[_ORG] = Field(
        default=None,
        title="ORG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
