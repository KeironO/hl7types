"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Z73
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP

_MSH = MSH
_QPD = QPD
_RCP = RCP


class QBP_Z73(HL7Model):
    """HL7 v2 QBP_Z73 message.

    Attributes:
        MSH (MSH): required
        QPD (QPD): required
        RCP (RCP): required
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

    model_config = {"populate_by_name": True}
