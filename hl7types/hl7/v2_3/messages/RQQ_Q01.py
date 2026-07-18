"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RQQ_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERQ import ERQ
from ..segments.MSH import MSH

_DSC = DSC
_ERQ = ERQ
_MSH = MSH


class RQQ_Q01(HL7Model):
    """QRY/DSR - Query sent for immediate response.

    Attributes:
        MSH (MSH): Message header segment, required
        ERQ (ERQ): Event Replay Query Segment, required
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    ERQ: _ERQ = Field(
        title="ERQ",
        description="Event Replay Query Segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
