"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QBP_Z73
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.SFT import SFT

_MSH = MSH
_QPD = QPD
_RCP = RCP
_SFT = SFT


class QBP_Z73(HL7Model):
    """HL7 v2 QBP_Z73 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QPD (QPD): required
        RCP (RCP): required
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

    QPD: _QPD = Field(
        title="QPD",
        description="Required",
    )

    RCP: _RCP = Field(
        title="RCP",
        description="Required",
    )

    model_config = {"populate_by_name": True}
