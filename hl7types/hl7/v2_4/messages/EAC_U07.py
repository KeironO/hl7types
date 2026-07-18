"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAC_U07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CNS import CNS
from ..segments.ECD import ECD
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SAC import SAC

_CNS = CNS
_ECD = ECD
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SAC = SAC


class EAC_U07(HL7Model):
    """EAC/ACK - Automated equipment command (S13).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        ECD (List[ECD]): Equipment Command, required
        SAC (Optional[SAC]): Specimen and container detail, optional
        CNS (Optional[CNS]): Clear Notification, optional
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

    ECD: List[_ECD] = Field(
        min_length=1,
        title="ECD",
        description="Equipment Command",
    )

    SAC: Optional[_SAC] = Field(
        default=None,
        title="SAC",
        description="Specimen and container detail",
    )

    CNS: Optional[_CNS] = Field(
        default=None,
        title="CNS",
        description="Clear Notification",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
