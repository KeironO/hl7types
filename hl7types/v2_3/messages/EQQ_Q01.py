"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: EQQ_Q01
Type: Message
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.EQL import EQL
from ..segments.MSH import MSH

_DSC = DSC
_EQL = EQL
_MSH = MSH


class EQQ_Q01(BaseModel):
    """HL7 v2 EQQ_Q01 message.

    Attributes:
        MSH (MSH): required
        EQL (EQL): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    EQL: _EQL = Field(
        default=...,
        title="EQL",
        description="Required",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
