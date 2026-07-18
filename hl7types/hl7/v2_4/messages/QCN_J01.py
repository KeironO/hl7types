"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QCN_J01
Type: Message
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QID import QID

_MSH = MSH
_QID = QID


class QCN_J01(HL7Model):
    """QCN/ACK - Cancel query/acknowledge message (S5).

    Attributes:
        MSH (MSH): Message Header, required
        QID (QID): Query Identification, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    QID: _QID = Field(
        title="QID",
        description="Query Identification",
    )

    model_config = ConfigDict(populate_by_name=True)
