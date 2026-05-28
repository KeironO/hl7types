"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SSU_U03
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL

from ..groups.SSU_U03_SPECIMEN_CONTAINER import SSU_U03_SPECIMEN_CONTAINER

_EQU = EQU
_MSH = MSH
_ROL = ROL
_SSU_U03_SPECIMEN_CONTAINER = SSU_U03_SPECIMEN_CONTAINER


class SSU_U03(BaseModel):
    """HL7 v2 SSU_U03 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        SPECIMEN_CONTAINER (List[SSU_U03_SPECIMEN_CONTAINER]): required
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

    SPECIMEN_CONTAINER: List[_SSU_U03_SPECIMEN_CONTAINER] = Field(
        default=...,
        title="SPECIMEN_CONTAINER",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
