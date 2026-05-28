"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SSU_U03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.SSU_U03_SPECIMEN_CONTAINER import SSU_U03_SPECIMEN_CONTAINER

_EQU = EQU
_MSH = MSH
_SFT = SFT
_SSU_U03_SPECIMEN_CONTAINER = SSU_U03_SPECIMEN_CONTAINER
_UAC = UAC


class SSU_U03(BaseModel):
    """HL7 v2 SSU_U03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        SPECIMEN_CONTAINER (List[SSU_U03_SPECIMEN_CONTAINER]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
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

    model_config = {"populate_by_name": True}
