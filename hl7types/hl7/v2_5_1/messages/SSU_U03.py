"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SSU_U03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

from ..groups.SSU_U03_SPECIMEN_CONTAINER import SSU_U03_SPECIMEN_CONTAINER

_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT
_SSU_U03_SPECIMEN_CONTAINER = SSU_U03_SPECIMEN_CONTAINER


class SSU_U03(HL7Model):
    """SSU/ACK - Specimen status update (S13.3.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EQU (EQU): Equipment Detail, required
        SPECIMEN_CONTAINER (List[SSU_U03_SPECIMEN_CONTAINER]): required
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

    SPECIMEN_CONTAINER: List[_SSU_U03_SPECIMEN_CONTAINER] = Field(
        min_length=1,
        title="SPECIMEN_CONTAINER",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
