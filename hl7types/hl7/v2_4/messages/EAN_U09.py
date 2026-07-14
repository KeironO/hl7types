"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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

from ..groups.EAN_U09_NOTIFICATION import EAN_U09_NOTIFICATION

_EAN_U09_NOTIFICATION = EAN_U09_NOTIFICATION
_EQU = EQU
_MSH = MSH
_ROL = ROL


class EAN_U09(HL7Model):
    """EAN/ACK - Automated equipment notification (S13).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        NOTIFICATION (List[EAN_U09_NOTIFICATION]): required
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

    NOTIFICATION: List[_EAN_U09_NOTIFICATION] = Field(
        min_length=1,
        title="NOTIFICATION",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
