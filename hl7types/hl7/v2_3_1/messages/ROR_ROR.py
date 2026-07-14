"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ROR_ROR
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

from ..groups.ROR_ROR_DEFINITION import ROR_ROR_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_ROR_ROR_DEFINITION = ROR_ROR_DEFINITION


class ROR_ROR(HL7Model):
    """HL7 v2 ROR_ROR message.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        DEFINITION (List[ROR_ROR_DEFINITION]): required
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERR - error segment",
    )

    DEFINITION: List[_ROR_ROR_DEFINITION] = Field(
        min_length=1,
        title="DEFINITION",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
