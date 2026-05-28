"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SSR_U04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.SSR_U04_SPECIMEN_CONTAINER import SSR_U04_SPECIMEN_CONTAINER

_EQU = EQU
_MSH = MSH
_SFT = SFT
_SSR_U04_SPECIMEN_CONTAINER = SSR_U04_SPECIMEN_CONTAINER
_UAC = UAC


class SSR_U04(BaseModel):
    """HL7 v2 SSR_U04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        SPECIMEN_CONTAINER (List[SSR_U04_SPECIMEN_CONTAINER]): required
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

    SPECIMEN_CONTAINER: List[_SSR_U04_SPECIMEN_CONTAINER] = Field(
        default=...,
        title="SPECIMEN_CONTAINER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
