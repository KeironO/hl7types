"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QCN_J01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QID import QID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_QID = QID
_SFT = SFT
_UAC = UAC


class QCN_J01(HL7Model):
    """QCN/ACK - Cancel query/acknowledge message (S5.4.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QID (QID): Query Identification, required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    QID: _QID = Field(
        title="QID",
        description="Query Identification",
    )

    model_config = ConfigDict(populate_by_name=True)
