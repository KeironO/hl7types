"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: EQQ_Q04
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.EQL import EQL
from ..segments.MSH import MSH

_DSC = DSC
_EQL = EQL
_MSH = MSH


class EQQ_Q04(BaseModel):
    """HL7 v2 EQQ_Q04 message.

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

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
