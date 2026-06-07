"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EQQ_Q04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.EQL import EQL
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_DSC = DSC
_EQL = EQL
_MSH = MSH
_SFT = SFT


class EQQ_Q04(HL7Model):
    """HL7 v2 EQQ_Q04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQL (EQL): required
        DSC (Optional[DSC]): optional
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

    EQL: _EQL = Field(
        title="EQL",
        description="Required",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
