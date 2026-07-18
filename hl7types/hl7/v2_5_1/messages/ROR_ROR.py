"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ROR_ROR
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.ROR_ROR_DEFINITION import ROR_ROR_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_ROR_ROR_DEFINITION = ROR_ROR_DEFINITION
_SFT = SFT


class ROR_ROR(HL7Model):
    """ROR - Pharmacy prescription order query response (S4.13.15).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        DEFINITION (List[ROR_ROR_DEFINITION]): required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    DEFINITION: List[_ROR_ROR_DEFINITION] = Field(
        min_length=1,
        title="DEFINITION",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
