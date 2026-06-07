"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RGR_RGR
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

from ..groups.RGR_RGR_DEFINTION import RGR_RGR_DEFINTION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_RGR_RGR_DEFINTION = RGR_RGR_DEFINTION


class RGR_RGR(HL7Model):
    """HL7 v2 RGR_RGR message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        DEFINTION (List[RGR_RGR_DEFINTION]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    DEFINTION: List[_RGR_RGR_DEFINTION] = Field(
        min_length=1,
        title="DEFINTION",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
