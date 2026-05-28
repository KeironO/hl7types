"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Q11
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP

_DSC = DSC
_MSH = MSH
_QPD = QPD
_RCP = RCP


class QBP_Q11(BaseModel):
    """HL7 v2 QBP_Q11 message.

    Attributes:
        MSH (MSH): required
        QPD (QPD): required
        RCP (RCP): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    RCP: _RCP = Field(
        default=...,
        title="RCP",
        description="Required",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
