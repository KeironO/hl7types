"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAN_U09
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL

from ..groups.EAN_U09_NOTIFICATION import EAN_U09_NOTIFICATION

_EAN_U09_NOTIFICATION = EAN_U09_NOTIFICATION
_EQU = EQU
_MSH = MSH
_ROL = ROL


class EAN_U09(BaseModel):
    """HL7 v2 EAN_U09 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        NOTIFICATION (List[EAN_U09_NOTIFICATION]): required
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

    NOTIFICATION: List[_EAN_U09_NOTIFICATION] = Field(
        default=...,
        title="NOTIFICATION",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
