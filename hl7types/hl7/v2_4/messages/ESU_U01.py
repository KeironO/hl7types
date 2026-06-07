"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ESU_U01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.ISD import ISD
from ..segments.MSH import MSH
from ..segments.ROL import ROL

_EQU = EQU
_ISD = ISD
_MSH = MSH
_ROL = ROL


class ESU_U01(HL7Model):
    """HL7 v2 ESU_U01 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        ISD (Optional[List[ISD]]): optional
        ROL (Optional[ROL]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Required",
    )

    ISD: Optional[List[_ISD]] = Field(
        default=None,
        title="ISD",
        description="Optional, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
