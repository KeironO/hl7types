"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QVR_Q17
Type: Message
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP

_DSC = DSC
_MSH = MSH
_QPD = QPD
_RCP = RCP


class QVR_Q17(HL7Model):
    """QVR - Query for previous events (S5).

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
        anyzsegment (Optional[Any]): optional
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    QPD: _QPD = Field(
        title="QPD",
        description="Query Parameter Definition",
    )

    anyzsegment: Optional[Any] = None

    RCP: _RCP = Field(
        title="RCP",
        description="Response Control Parameter",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
