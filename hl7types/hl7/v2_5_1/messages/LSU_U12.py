"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: LSU_U12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EQP import EQP
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

_EQP = EQP
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT


class LSU_U12(HL7Model):
    """LSU/ACK - Automated equipment log/service update (S13.3.12).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EQU (EQU): Equipment Detail, required
        EQP (List[EQP]): Equipment/log Service, required
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

    model_config = ConfigDict(populate_by_name=True)
