"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
    """HL7 v2 RQQ_Q09 message.

    Attributes:
        MSH (MSH): required
        ERQ (ERQ): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    ERQ: _ERQ = Field(
        title="ERQ",
        description="Required",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
