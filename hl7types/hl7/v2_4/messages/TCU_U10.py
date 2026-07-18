"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: TCU_U10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.TCC import TCC

_EQU = EQU
_MSH = MSH
_ROL = ROL
_TCC = TCC


class TCU_U10(HL7Model):
    """TCU/ACK - Automated equipment test code settings update (S13).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        TCC (List[TCC]): Test Code Configuration, required
        ROL (Optional[ROL]): Role, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    TCC: List[_TCC] = Field(
        min_length=1,
        title="TCC",
        description="Test Code Configuration",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
