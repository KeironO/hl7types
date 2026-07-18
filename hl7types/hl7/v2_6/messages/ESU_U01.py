"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ESU_U01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.ISD import ISD
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EQU = EQU
_ISD = ISD
_MSH = MSH
_ROL = ROL
_SFT = SFT
_UAC = UAC


class ESU_U01(HL7Model):
    """ESU/ACK - Automated equipment status update (S13.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EQU (EQU): Equipment Detail, required
        ISD (Optional[List[ISD]]): Interaction Status Detail, optional
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    ISD: Optional[List[_ISD]] = Field(
        default=None,
        title="ISD",
        description="Interaction Status Detail",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
