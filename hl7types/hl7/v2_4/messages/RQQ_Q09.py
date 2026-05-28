"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RQQ_Q09
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.ERQ import ERQ
from ..segments.MSH import MSH

_DSC = DSC
_ERQ = ERQ
_MSH = MSH


class RQQ_Q09(BaseModel):
    """HL7 v2 RQQ_Q09 message.

    Attributes:
        MSH (MSH): required
        ERQ (ERQ): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    ERQ: _ERQ = Field(
        default=...,
        title="ERQ",
        description="Required",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
