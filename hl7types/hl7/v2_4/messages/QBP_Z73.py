"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Z73
Type: Message
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP

_MSH = MSH
_QPD = QPD
_RCP = RCP


class QBP_Z73(HL7Model):
    """Information about Phone Calls (S15).

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    QPD: _QPD = Field(
        title="QPD",
        description="Query Parameter Definition",
    )

    RCP: _RCP = Field(
        title="RCP",
        description="Response Control Parameter",
    )

    model_config = ConfigDict(populate_by_name=True)
