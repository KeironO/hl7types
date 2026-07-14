"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ESR_U02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT


class ESR_U02(HL7Model):
    """ESR/ACK - Automated equipment status request (S13.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EQU (EQU): Equipment Detail, required
        ROL (Optional[ROL]): Role, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
