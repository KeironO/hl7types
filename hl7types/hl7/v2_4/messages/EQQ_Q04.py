"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    """EQQ - Embedded query language query (S5).

    Attributes:
        MSH (MSH): Message Header, required
        EQL (EQL): Embedded Query Language, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EQL: _EQL = Field(
        title="EQL",
        description="Embedded Query Language",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
