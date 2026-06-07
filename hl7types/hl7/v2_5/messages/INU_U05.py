"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: INU_U05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.INV import INV
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

_EQU = EQU
_INV = INV
_MSH = MSH
_ROL = ROL
_SFT = SFT


class INU_U05(HL7Model):
    """HL7 v2 INU_U05 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        INV (List[INV]): required
        ROL (Optional[ROL]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Required",
    )

    INV: List[_INV] = Field(
        min_length=1,
        title="INV",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
