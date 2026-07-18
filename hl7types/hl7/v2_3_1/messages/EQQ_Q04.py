"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: EQQ_Q04
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


class EQQ_Q04(HL7Model):
    """EQQ - Embedded query language query.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EQL (EQL): EQL - embedded query language segment, required
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    EQL: _EQL = Field(
        title="EQL",
        description="EQL - embedded query language segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
