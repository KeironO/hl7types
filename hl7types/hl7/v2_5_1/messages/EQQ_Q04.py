"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EQQ_Q04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EQL (EQL): Embedded Query Language, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    EQL: _EQL = Field(
        title="EQL",
        description="Embedded Query Language",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
