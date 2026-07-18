"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: EQQ_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.EQL import EQL
from ..segments.MSH import MSH

_DSC = DSC
_EQL = EQL
_MSH = MSH


class EQQ_Q01(HL7Model):
    """QRY/DSR - Query sent for immediate response.

    Attributes:
        MSH (MSH): Message header segment, required
        EQL (EQL): Embedded Query Language, required
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    EQL: _EQL = Field(
        title="EQL",
        description="Embedded Query Language",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
