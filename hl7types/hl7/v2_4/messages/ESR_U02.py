"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ESR_U02
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL

_EQU = EQU
_MSH = MSH
_ROL = ROL


class ESR_U02(HL7Model):
    """HL7 v2 ESR_U02 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        ROL (Optional[ROL]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    EQU: _EQU = Field(
        default=...,
        title="EQU",
        description="Required",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
