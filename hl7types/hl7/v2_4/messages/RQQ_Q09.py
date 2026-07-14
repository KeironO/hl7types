"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RQQ_Q09
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERQ import ERQ
from ..segments.MSH import MSH

_DSC = DSC
_ERQ = ERQ
_MSH = MSH


class RQQ_Q09(HL7Model):
    """RQQ - event replay query (S5).

    Attributes:
        MSH (MSH): Message Header, required
        ERQ (ERQ): Event Replay Query, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    ERQ: _ERQ = Field(
        title="ERQ",
        description="Event Replay Query",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
