"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RQQ_Q09
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


class RQQ_Q09(HL7Model):
    """RQQ - event replay query.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        ERQ (ERQ): ERQ - event replay query segment, required
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    ERQ: _ERQ = Field(
        title="ERQ",
        description="ERQ - event replay query segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
