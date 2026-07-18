"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RAR_RAR
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

from ..groups.RAR_RAR_DEFINITION import RAR_RAR_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_RAR_RAR_DEFINITION = RAR_RAR_DEFINITION


class RAR_RAR(HL7Model):
    """RAR - Pharmacy administration information query response (S4).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        DEFINITION (List[RAR_RAR_DEFINITION]): required
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

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    DEFINITION: List[_RAR_RAR_DEFINITION] = Field(
        min_length=1,
        title="DEFINITION",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
