"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EAN_U09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

from ..groups.EAN_U09_NOTIFICATION import EAN_U09_NOTIFICATION

_EAN_U09_NOTIFICATION = EAN_U09_NOTIFICATION
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT


class EAN_U09(HL7Model):
    """HL7 v2 EAN_U09 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        NOTIFICATION (List[EAN_U09_NOTIFICATION]): required
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

    NOTIFICATION: List[_EAN_U09_NOTIFICATION] = Field(
        min_length=1,
        title="NOTIFICATION",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
