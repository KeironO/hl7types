"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
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
from ..segments.SFT import SFT
from ..segments.STF import STF
from ..segments.UAC import UAC

_EVN = EVN
_MSH = MSH
_ORG = ORG
_PRA = PRA
_SFT = SFT
_STF = STF
_UAC = UAC


class PMU_B04(HL7Model):
    """HL7 v2 PMU_B04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        STF (STF): required
        PRA (Optional[List[PRA]]): optional
        ORG (Optional[List[ORG]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Required",
    )

    STF: _STF = Field(
        title="STF",
        description="Required",
    )

    PRA: Optional[List[_PRA]] = Field(
        default=None,
        title="PRA",
        description="Optional, repeating",
    )

    ORG: Optional[List[_ORG]] = Field(
        default=None,
        title="ORG",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
