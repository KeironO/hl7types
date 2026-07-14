"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RGR_RGR
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

from ..groups.RGR_RGR_DEFINITION import RGR_RGR_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_RGR_RGR_DEFINITION = RGR_RGR_DEFINITION


class RGR_RGR(HL7Model):
    """RGR - Pharmacy dose information query response.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        DEFINITION (List[RGR_RGR_DEFINITION]): required
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error segment",
    )

    DEFINITION: List[_RGR_RGR_DEFINITION] = Field(
        min_length=1,
        title="DEFINITION",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
