"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: LSU_U12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQP import EQP
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL

_EQP = EQP
_EQU = EQU
_MSH = MSH
_ROL = ROL


class LSU_U12(HL7Model):
    """LSU/ACK - Automated equipment log/service update (S13).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        EQP (List[EQP]): Equipment/log Service, required
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

    EQP: List[_EQP] = Field(
        min_length=1,
        title="EQP",
        description="Equipment/log Service",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
